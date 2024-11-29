import os
from openai import OpenAI
from pathlib import Path

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

CONTENT_DIR = Path("content/")  # Folder synced from GitBook
OUTPUT_DIR = Path("translated/ja/")  # Translated content folder

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
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Iterate through Markdown files in the content folder
    for file in CONTENT_DIR.rglob("*.md"):
        print(f"Processing file: {file}")
        relative_path = file.relative_to(CONTENT_DIR)
        output_path = OUTPUT_DIR / relative_path

        # Read file content
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Translate content
        try:
            translated_content = translate_to_japanese(content)
        except Exception as e:
            print(f"Error during translation: {e}")
            continue

        # Write to output directory
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)
        print(f"Translated file saved to: {output_path}")

if __name__ == "__main__":
    main()
