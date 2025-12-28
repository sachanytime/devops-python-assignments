import os
import sys
import shutil
from datetime import datetime


def backup_files(source_dir, destination_dir):
    try:
        # Check if source directory exists
        if not os.path.isdir(source_dir):
            print(f"❌ Error: Source directory does not exist -> {source_dir}")
            return

        # Check if destination directory exists
        if not os.path.isdir(destination_dir):
            print(f"❌ Error: Destination directory does not exist -> {destination_dir}")
            return

        # Iterate through files in source directory
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)

            # Process only files (skip directories)
            if os.path.isfile(source_file):
                destination_file = os.path.join(destination_dir, filename)

                # If file exists, append timestamp
                if os.path.exists(destination_file):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{timestamp}{ext}"
                    destination_file = os.path.join(destination_dir, new_filename)

                shutil.copy2(source_file, destination_file)
                print(f"✅ Backed up: {filename}")

        print("\nBackup completed successfully.")

    except PermissionError:
        print("❌ Permission denied. Run the script with proper access rights.")

    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")


# ------------------ Main ------------------
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    backup_files(source, destination)
