import os
import subprocess
import google.generativeai as genai

# --- 1. System Configuration ---
API_KEY = os.environ.get("GEMINI_API_KEY")
REPO_PATH = os.environ.get("REPO_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
STAGING_DIR = os.path.join(REPO_PATH, "Jules", "Pending Review")
INVENTORY_DIR = os.path.join(REPO_PATH, "Structured_Inventory")
BEHAVIOR_FILE_NAME = "AIStudios_Executor_Behavior_V1_06232026.md"

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit(1)

# Initialize Jules via the API
genai.configure(api_key=API_KEY)

def get_system_instructions():
    """Finds and reads the behavior file to use as system instructions."""
    behavior_path = os.path.join(STAGING_DIR, BEHAVIOR_FILE_NAME)
    if os.path.exists(behavior_path):
        try:
            with open(behavior_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading behavior file: {e}")
            exit(1)
    else:
        print(f"Error: Behavior file {BEHAVIOR_FILE_NAME} not found in {STAGING_DIR}.")
        exit(1)

system_instruction = get_system_instructions()

model = genai.GenerativeModel(
    model_name="gemini-2.5-pro",
    system_instruction=system_instruction,
    generation_config={"response_mime_type": "application/json"}
)

# --- 2. Git Execution Protocol ---
def execute_git_push(commit_message):
    """Allows Jules to take control of the terminal and push changes."""
    try:
        print("Executing Git sync...")
        # Stage all new changes
        subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)
        # Commit the changes
        subprocess.run(["git", "commit", "-m", commit_message], cwd=REPO_PATH, check=True)
        # Push to GitHub
        subprocess.run(["git", "push"], cwd=REPO_PATH, check=True)
        print(f"Success: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Git execution failed. Please check repository status. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during Git execution: {e}")

# --- 3. The Read & Write Loop ---
def process_staging_notes():
    """Reads raw notes, passes them to Jules, writes the output, and pushes."""
    if not os.path.exists(STAGING_DIR):
        print(f"Staging directory {STAGING_DIR} not found.")
        return

    # Ensure output directory exists
    os.makedirs(INVENTORY_DIR, exist_ok=True)

    files_processed = False

    for filename in os.listdir(STAGING_DIR):
        if filename == BEHAVIOR_FILE_NAME:
            continue

        if filename.endswith(".md") or filename.endswith(".txt"):
            file_path = os.path.join(STAGING_DIR, filename)

            # Read the raw note
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    raw_content = file.read()
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
                continue

            print(f"Jules is processing: {filename}...")

            try:
                # Pass to Jules
                response = model.generate_content(
                    f"Convert the following raw notes into a structured inventory object:\n\n{raw_content}"
                )

                # Write the structured output
                output_filename = filename.replace(".md", ".json").replace(".txt", ".json")
                output_path = os.path.join(INVENTORY_DIR, output_filename)

                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(response.text)

                print(f"Successfully generated {output_filename}")

                # Clean up the staging folder
                os.remove(file_path)
                files_processed = True
            except Exception as e:
                print(f"Error processing {filename} with Gemini API: {e}")

    # Hand over execution to push the new inventory to GitHub
    if files_processed:
        execute_git_push("Jules: Automated inventory generation and repository sync.")
    else:
        print("No new files were processed. Skipping git sync.")

if __name__ == "__main__":
    process_staging_notes()
