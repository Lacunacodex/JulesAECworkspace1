import os
import google.generativeai as genai

# 1. Pull the key directly from the GitHub Cloud Secret
API_KEY = os.environ.get("GEMINI_API_KEY")

STAGING_DIR = "Pending Review"
INVENTORY_DIR = "Structured_Inventory"
BEHAVIOR_FILE = os.path.join(STAGING_DIR, "AIStudios_Executor_Behavior_V1_06232026.md")

# 2. Read the master alignment rules
with open(BEHAVIOR_FILE, 'r', encoding='utf-8') as file:
    behavior_instructions = file.read()

# 3. Wake up Executor Jules
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-2.5-pro", 
    system_instruction=behavior_instructions,
    generation_config={"response_mime_type": "application/json"}
)

# 4. Process the files
for filename in os.listdir(STAGING_DIR):
    # Ignore the rules file itself
    if filename == "AIStudios_Executor_Behavior_V1_06232026.md":
        continue
        
    if filename.endswith(".md"):
        file_path = os.path.join(STAGING_DIR, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_content = file.read()
            
        print(f"Jules processing: {filename}")
        
        # Enforce the formatting
        response = model.generate_content(
            f"Process this intercepted file into the master wiki taxonomy:\n\n{raw_content}"
        )
        
        # Save the structured JSON
        output_filename = filename.replace(".md", ".json")
        output_path = os.path.join(INVENTORY_DIR, output_filename)
        
        # Ensure the destination folder exists
        os.makedirs(INVENTORY_DIR, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(response.text)
            
        # Clean up the raw file so it doesn't process twice
        os.remove(file_path)
