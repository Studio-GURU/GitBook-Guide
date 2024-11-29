import os
import subprocess
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Paths
CONTENT_DIR = Path("content/")  # Update this to the directory containing your Korean content
# If your content is in the root directory, use Path("./")

def translate_to_japanese(content):
    """Translate the given content from Korean to Japanese using OpenAI API."""
    print("Translating content...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional translator proficient in Korean and Japanese."},
            {"role": "user", "content": f"Please translate the following content from Korean to Japanese:\n\n{content}"}
        ]
    )
    return response.choices[0].message.content

def main():
    """Main function to process and translate files."""
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

        # Overwrite the original file with the translated content
        with open(file, "w", encoding="utf-8") as f:
            f.write(translated_content)
        print(f"Translated and overwritten file: {file}")

    print("All files have been translated.")

if __name__ == "__main__":
    main()
