import os
import yaml
import re
import json
from pathlib import Path
from openai import OpenAI
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('translation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Constants
BASE_DIR = Path(".")
EXCLUDE_DIRS = {'.git', '.github', 'node_modules', '.gitbook', 'scripts'}
PROGRESS_FILE = Path("translation_progress.json")

def load_progress():
    """Load translation progress from file."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_progress(progress):
    """Save translation progress to file."""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2)

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

def translate_content(content, is_front_matter=False):
    """Translate content from Korean to Japanese."""
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
    """Determine if a file should be translated."""
    if any(excluded in file_path.parts for excluded in EXCLUDE_DIRS):
        return False
    
    if file_path.suffix not in {'.md', '.txt'}:
        return False
    
    return True

def translate_file(file_path, progress):
    """Translate a single file from Korean to Japanese."""
    file_str = str(file_path)
    
    # Skip if file was already translated successfully
    if progress.get(file_str, {}).get('status') == 'completed':
        logger.info(f"Skipping already translated file: {file_path}")
        return
    
    logger.info(f"Processing file: {file_path}")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if not content.strip():
            logger.info(f"Skipping empty file: {file_path}")
            progress[file_str] = {'status': 'completed', 'empty': True}
            save_progress(progress)
            return
        
        # Handle front matter and main content
        front_matter, main_content = extract_front_matter(content)
        translated_parts = []
        
        # Translate front matter if exists
        if front_matter:
            front_matter_yaml = yaml.dump(front_matter, allow_unicode=True)
            translated_front_matter = translate_content(front_matter_yaml, is_front_matter=True)
            translated_parts.append(f"---\n{translated_front_matter}---\n")
        
        # Translate main content
        translated_content = translate_content(main_content)
        translated_parts.append(translated_content)
        
        # Write translated content back to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('\n'.join(translated_parts))
        
        progress[file_str] = {'status': 'completed'}
        save_progress(progress)
        logger.info(f"Successfully translated: {file_path}")
        
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
        progress[file_str] = {'status': 'failed', 'error': str(e)}
        save_progress(progress)
        raise

def main():
    """Main function to process and translate files."""
    logger.info("Starting translation process...")
    
    # Load previous progress
    progress = load_progress()
    
    try:
        # Get all files in the repository
        for file_path in BASE_DIR.rglob("*"):
            if file_path.is_file() and should_translate_file(file_path):
                translate_file(file_path, progress)
    
    except Exception as e:
        logger.error(f"Fatal error in main process: {e}")
        raise
    
    logger.info("Translation process completed successfully!")

if __name__ == "__main__":
    main()
