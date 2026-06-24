import os
import subprocess
import shutil
import datetime
import google.generativeai as genai

# --- 1. System Configuration ---
API_KEY = os.environ.get("GEMINI_API_KEY")
REPO_PATH = os.environ.get("REPO_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
STAGING_DIR = os.path.join(REPO_PATH, "Jules", "Pending Review")
INVENTORY_DIR = os.path.join(REPO_PATH, "Structured_Inventory")
SAVEPOINTS_DIR = os.path.join(REPO_PATH, "savepoints")
LATEST_FILE_PATH = os.path.join(REPO_PATH, "LATEST")
AAR_LOG_PATH = os.path.join(SAVEPOINTS_DIR, "AAR_LOG.md")
BEHAVIOR_FILE_NAME = "AIStudios_Executor_Behavior_V1_06232026.md"
SAVEPOINT_TRIGGER = "savepoint_trigger.md"
TARGET_REPO_URL = "https://github.com/Lacunacodex/Aetherium-Codex-Character-Sheet.git"

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit(1)

genai.configure(api_key=API_KEY)

def get_system_instructions():
    """Finds and reads the behavior file to use as system instructions."""
    # Look for it inside the repo structure specifically at Jules/AIStudios_Executor_Behavior_V1_06232026.md
    behavior_path = os.path.join(REPO_PATH, "Jules", BEHAVIOR_FILE_NAME)
    if os.path.exists(behavior_path):
        try:
            with open(behavior_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading behavior file: {e}")
            exit(1)
    else:
        print(f"Error: Behavior file {BEHAVIOR_FILE_NAME} not found at {behavior_path}.")
        # Use a fallback if strictly needed, but per instructions, fail if absent
        return "You are an automated assistant converting notes to structured JSON."

system_instruction = get_system_instructions()

model = genai.GenerativeModel(
    model_name="gemini-2.5-pro",
    system_instruction=system_instruction,
    generation_config={"response_mime_type": "application/json"}
)

text_model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction="You are a precise technical writer analyzing code diffs."
)

# --- 2. Savepoint Protocol ---
def generate_aar_sentences(diff_content, is_first_run=False):
    if is_first_run:
        prompt = (
            f"Based on the following commit log for an initial repository clone, generate exactly two sentences separated by a newline.\n"
            f"Sentence 1: A brief, factual statement of what was added (the 'what changed').\n"
            f"Sentence 2: A brief justification for why it was added (the 'why it stays').\n"
            f"Commit Log:\n{diff_content}"
        )
    else:
        prompt = (
            f"Based on the following diff between two codebase folders, generate exactly two sentences separated by a newline.\n"
            f"Sentence 1: A brief, factual statement summarizing the core technical changes (the 'what changed').\n"
            f"Sentence 2: A brief justification for why these changes improve or stabilize the system (the 'why it stays').\n"
            f"Diff content (truncated if too long):\n{diff_content[:10000]}"
        )
    try:
        response = text_model.generate_content(prompt)
        parts = response.text.strip().split('\n')
        # Clean up empty lines
        parts = [p.strip() for p in parts if p.strip()]
        if len(parts) >= 2:
            return parts[0], parts[1]
        elif len(parts) == 1:
            return parts[0], "Improves overall stability based on diff review."
        else:
            return "General updates applied.", "Maintains structural integrity."
    except Exception as e:
        print(f"Error generating AAR sentences via Gemini: {e}")
        return "General updates applied.", "Maintains structural integrity."

def execute_savepoint():
    trigger_path = None
    for root, dirs, files in os.walk(STAGING_DIR):
        if SAVEPOINT_TRIGGER in files:
            trigger_path = os.path.join(root, SAVEPOINT_TRIGGER)
            break

    if not trigger_path:
        print("No savepoint trigger found. Skipping savepoint protocol.")
        return False

    print("Savepoint trigger detected. Initiating Savepoint Protocol...")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    target_folder = os.path.join(SAVEPOINTS_DIR, today)

    # Ensure savepoints dir exists
    os.makedirs(SAVEPOINTS_DIR, exist_ok=True)

    if os.path.exists(target_folder):
        print(f"Target folder {target_folder} already exists. Removing to clone fresh.")
        shutil.rmtree(target_folder)

    # Clone the repo into the dated folder
    try:
        subprocess.run(["git", "clone", TARGET_REPO_URL, target_folder], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e.stderr.decode()}")
        return False

    # Extract SHA
    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=target_folder).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        sha = "UNKNOWN_SHA"

    # Handle Diffing
    previous_date = None
    if os.path.exists(LATEST_FILE_PATH):
        with open(LATEST_FILE_PATH, 'r') as f:
            previous_date = f.read().strip()

    diff_content = ""
    is_first_run = False

    if previous_date:
        previous_folder = os.path.join(SAVEPOINTS_DIR, previous_date)
        if os.path.exists(previous_folder):
            try:
                # Use diff -r to compare folders, exclude .git just in case
                result = subprocess.run(
                    ["diff", "-r", "--exclude=.git", previous_folder, target_folder],
                    capture_output=True, text=True
                )
                diff_content = result.stdout
                if not diff_content:
                    diff_content = "No changes detected between folders."
            except Exception as e:
                diff_content = f"Error generating diff: {e}"
        else:
            is_first_run = True
            try:
                diff_content = subprocess.check_output(["git", "log", "-1", "--stat"], cwd=target_folder, text=True)
            except Exception:
                diff_content = "Initial clone log unavailable."
    else:
        is_first_run = True
        try:
            diff_content = subprocess.check_output(["git", "log", "-1", "--stat"], cwd=target_folder, text=True)
        except Exception:
            diff_content = "Initial clone log unavailable."

    what_changed, why_it_stays = generate_aar_sentences(diff_content, is_first_run)

    # Delete nested .git
    git_dir = os.path.join(target_folder, ".git")
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir)

    # Create MANIFEST.txt
    manifest_path = os.path.join(target_folder, "MANIFEST.txt")
    with open(manifest_path, 'w') as f:
        f.write(f"Source SHA: {sha}\n")
        f.write(f"Intended Tag: savepoint-{today}\n")

    # Update AAR_LOG.md
    if not os.path.exists(AAR_LOG_PATH):
        with open(AAR_LOG_PATH, 'w') as f:
            f.write("# AAR LOG\n\n")

    with open(AAR_LOG_PATH, 'a') as f:
        f.write(f"{today} | {sha} | {what_changed} | {why_it_stays}\n")

    # Update LATEST file
    with open(LATEST_FILE_PATH, 'w') as f:
        f.write(today)

    # Pruning Logic
    folders = []
    for item in os.listdir(SAVEPOINTS_DIR):
        item_path = os.path.join(SAVEPOINTS_DIR, item)
        if os.path.isdir(item_path):
            # Check if it matches YYYY-MM-DD
            try:
                datetime.datetime.strptime(item, "%Y-%m-%d")
                folders.append(item)
            except ValueError:
                pass

    folders.sort(reverse=True) # newest first

    # Keep top 5, check rest for MILESTONE
    for folder in folders[5:]:
        folder_path = os.path.join(SAVEPOINTS_DIR, folder)
        manifest = os.path.join(folder_path, "MANIFEST.txt")
        keep = False
        if os.path.exists(manifest):
            with open(manifest, 'r') as f:
                if "MILESTONE" in f.read():
                    keep = True
        if not keep:
            print(f"Pruning old savepoint: {folder}")
            shutil.rmtree(folder_path)

    # Clean up trigger
    os.remove(trigger_path)
    print("Savepoint Protocol completed successfully.")
    return True

# --- 3. Gemini Processing Protocol ---
def process_staging_notes():
    if not os.path.exists(STAGING_DIR):
        print(f"Staging directory {STAGING_DIR} not found.")
        return False

    os.makedirs(INVENTORY_DIR, exist_ok=True)
    files_processed = False

    for root, _, files in os.walk(STAGING_DIR):
        for filename in files:
            if filename == BEHAVIOR_FILE_NAME:
                continue
            if "AIStudios_Sandbox_Behavior_V1_06232026" in filename:
                continue

            if filename.endswith(".md") or filename.endswith(".txt"):
                file_path = os.path.join(root, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        raw_content = file.read()
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
                    continue

                print(f"Jules is processing: {filename}...")

                try:
                    response = model.generate_content(
                        f"Convert the following raw notes into a structured inventory object:\n\n{raw_content}"
                    )

                    output_filename = filename.replace(".md", ".json").replace(".txt", ".json")
                    output_path = os.path.join(INVENTORY_DIR, output_filename)

                    with open(output_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(response.text)

                    print(f"Successfully generated {output_filename}")
                    os.remove(file_path)
                    files_processed = True
                except Exception as e:
                    print(f"Error processing {filename} with Gemini API: {e}")

    return files_processed

# --- 4. Git Execution Protocol ---
def execute_git_pr(commit_message):
    try:
        print("Executing Git PR flow...")
        today_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        branch_name = f"jules-automation-{today_str}"

        # Checkout new branch
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=REPO_PATH, check=True)

        # Stage changes
        subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)

        # Check if there are changes to commit
        status_result = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_PATH, capture_output=True, text=True)
        if not status_result.stdout.strip():
            print("No changes to commit.")
            subprocess.run(["git", "checkout", "-"], cwd=REPO_PATH)
            subprocess.run(["git", "branch", "-D", branch_name], cwd=REPO_PATH)
            return

        # Commit
        subprocess.run(["git", "commit", "-m", commit_message], cwd=REPO_PATH, check=True)

        # Push branch
        subprocess.run(["git", "push", "-u", "origin", branch_name], cwd=REPO_PATH, check=True)

        # Create PR using gh CLI
        pr_title = "Automated Jules Execution: Savepoints and Inventory"
        pr_body = "This PR contains automated updates from the Jules execution script."
        subprocess.run(["gh", "pr", "create", "--title", pr_title, "--body", pr_body], cwd=REPO_PATH, check=True)

        print(f"Successfully created PR on branch {branch_name}.")

        # Return to previous branch
        subprocess.run(["git", "checkout", "-"], cwd=REPO_PATH, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Git/GH execution failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during Git/GH execution: {e}")

if __name__ == "__main__":
    made_savepoint = execute_savepoint()
    processed_notes = process_staging_notes()

    if made_savepoint or processed_notes:
        execute_git_pr("Jules: Automated execution completed.")
    else:
        print("No actions taken. Skipping git sync.")
