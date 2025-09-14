import os
import shutil
from datetime import datetime
import logging
import argparse
import json

# ---------------- Configuration ----------------
# Default file type mapping
DEFAULT_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
}

# Logging setup
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ---------------- Core Functions ----------------
def load_categories(config_file=None):
    """Load custom categories from JSON file if provided."""
    if config_file and os.path.exists(config_file):
        try:
            with open(config_file) as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: Invalid JSON config. Using default categories.")
    return DEFAULT_CATEGORIES

def organize_files(directory, categories, dry_run=False, date_based=False):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            # Determine the target folder
            moved = False
            for folder, extensions in categories.items():
                if filename.lower().endswith(tuple(extensions)):
                    folder_name = folder
                    moved = True
                    break
            if not moved:
                folder_name = "Others"

            # Apply date-based subfolder
            if date_based:
                creation_time = os.path.getctime(filepath)
                date_folder = datetime.fromtimestamp(creation_time).strftime("%Y-%m")
                folder_name = os.path.join(folder_name, date_folder)

            dest_folder = os.path.join(directory, folder_name)
            if not os.path.exists(dest_folder) and not dry_run:
                os.makedirs(dest_folder)

            dest_path = os.path.join(dest_folder, filename)

            if dry_run:
                print(f"[DRY RUN] Would move '{filename}' to '{folder_name}/'")
            else:
                shutil.move(filepath, dest_path)
                print(f"Moved '{filename}' to '{folder_name}/'")
                logging.info(f"Moved '{filename}' to '{folder_name}/'")

# ---------------- Command-Line Interface ----------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Automated File Organizer")
    parser.add_argument("directory", help="Directory to organize")
    parser.add_argument("--config", help="JSON config file for custom categories")
    parser.add_argument("--dry-run", action="store_true", help="Simulate organization without moving files")
    parser.add_argument("--date-based", action="store_true", help="Organize files by creation date (YYYY-MM)")
    args = parser.parse_args()

    categories = load_categories(args.config)
    organize_files(args.directory, categories, dry_run=args.dry_run, date_based=args.date_based)
    print("Organization complete!")
