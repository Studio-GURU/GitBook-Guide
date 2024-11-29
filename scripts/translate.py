import os
import openai
from pathlib import Path

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Paths
CONTENT_DIR = Path("content/")  # Folder synced from GitBook
OUTPUT_DIR = Path("translated/ja/")  # Translated content folder

def translate_to_japanese(content):
    """Translate text to Japanese using OpenAI GPT-4 API."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional translator."},
            {"role": "user", "content": f"Translate this Markdown content to Japanese:\n\n{content}"}
        ]
    )
    return response['choices'][0]['message']['content']

def main():
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Iterate through Markdown files in the content folder
    for file in CONTENT_DIR.rglob("*.md"):
        relative_path = file.relative_to(CONTENT_DIR)
        output_path = OUTPUT_DIR / relative_path

        # Read file content
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Translate content
        translated_content = translate_to_japanese(content)

        # Write to output directory
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

if __name__ == "__main__":
    main()
