import os
from openai import OpenAI
from pathlib import Path

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Paths
CONTENT_DIR = Path("TreasureIsland-JP/")  # Target space content folder
OUTPUT_DIR = CONTENT_DIR  # Overwrite directly in the same directory

def translate_to_japanese(content):
    print("Translating content...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional translator."},
            {"role": "user", "content": f"Translate this Markdown content to Japanese:\n\n{content}"}
        ]
    )
    return response.choices[0].message.content

def main():
    # Iterate through Markdown files in the content folder
    for file in CONTENT_DIR.rglob("*.md"):
        print(f"Processing file: {file}")
        
        # Read file content
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Translate content
        try:
            translated_content = translate_to_japanese(content)
        except Exception as e:
            print(f"Error during translation: {e}")
            continue

        # Overwrite the original file
        with open(file, "w", encoding="utf-8") as f:
            f.write(translated_content)
        print(f"Translated file written to: {file}")

if __name__ == "__main__":
    main()
