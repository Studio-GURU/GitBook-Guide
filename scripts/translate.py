import os
import yaml
import re
from pathlib import Path
from openai import OpenAI
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Paths
BASE_DIR = Path(".")
EXCLUDE_DIRS = {'.git', '.github', 'node_modules', '.gitbook', 'scripts'}

def extract_front_matter(content):
    """Extract YAML front matter from content if it exists."""
    front_matter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if front_matter_match:
        try:
            front_matter = yaml.safe_load(front_matter_match.group(1))
            content = front_matter_match.group(2)
            return front_matter, content
        except yaml.YAMLError as e:
            logger.warning(f"Error parsing front matter: {e}")
            return None, content
    return None, content

def translate_to_japanese(content, is_front_matter=False):
    """Translate content from Korean to Japanese using OpenAI API."""
    try:
        system_prompt = (
            "You are a professional translator specializing in Korean to Japanese translation. "
            "Maintain all formatting, markdown syntax, and code blocks exactly as they appear. "
            "If translating YAML front matter, preserve all keys and only translate values that are Korean text."
        )
        
        user_prompt = (
            "Please translate the following content from Korean to Japanese. "
            "Preserve all markdown formatting, code blocks, and special syntax exactly as they appear."
            if not is_front_matter else
            "Please translate the following YAML front matter values from Korean to Japanese. "
            "Keep all keys unchanged and only translate text values that are in Korean."
        )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{user_prompt}\n\n{content}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Translation error: {e}")
        raise

def should_translate_file(file_path):
    """Determine if a file should be translated based on its path and content."""
    # Skip files in excluded directories
    if any(excluded in file_path.parts for excluded in EXCLUDE_DIRS):
        return False
    
    # Only process certain file types
    if file_path.suffix not in {'.md', '.txt'}:
        return False
    
    return True

def translate_file(file_path):
    """Translate a single file from Korean to Japanese."""
    logger.info(f"Processing file: {file_path}")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Skip empty files
        if not content.strip():
            logger.info(f"Skipping empty file: {file_path}")
            return
        
        # Handle front matter and main content separately
        front_matter, main_content = extract_front_matter(content)
        
        if front_matter:
            # Translate front matter values
            translated_front_matter = yaml.dump(
                yaml.safe_load(translate_to_japanese(yaml.dump(front_matter), is_front_matter=True)),
                allow_unicode=True
            )
        else:
            translated_front_matter = ""
        
        # Translate main content
        translated_content = translate_to_japanese(main_content)
        
        # Combine translated parts
        final_content = ""
        if translated_front_matter:
            final_content = f"---\n{translated_front_matter}---\n\n"
        final_content += translated_content
        
        # Write translated content back to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        
        logger.info(f"Successfully translated: {file_path}")
        
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
        raise

def main():
    """Main function to process and translate files."""
    logger.info("Starting translation process...")
    
    try:
        # Get all files in the repository
        for file_path in BASE_DIR.rglob("*"):
            if file_path.is_file() and should_translate_file(file_path):
                translate_file(file_path)
    
    except Exception as e:
        logger.error(f"Fatal error in main process: {e}")
        raise
    
    logger.info("Translation process completed successfully!")

if __name__ == "__main__":
    main()
