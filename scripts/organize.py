#!/usr/bin/env python3
import shutil
import json
import argparse
from pathlib import Path


def move_file_based_on_json(file_path, base_path):
    """Move a JSON file to a subdirectory based on 'List' key and 'Is Completed' status in the JSON file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        list_key = data.get("List")
        is_completed = data.get(
            "Is Completed", False
        )  # False by default if key doesn't exist

        if list_key:
            target_dir = base_path / list_key
            if is_completed:
                target_dir /= "Completed"  # Add 'Completed' subfolder if the task is marked as completed
            target_dir.mkdir(
                parents=True, exist_ok=True
            )  # Create target directory if it does not exist
            shutil.move(str(file_path), str(target_dir / file_path.name))
            print(f"Moved {file_path.name} to {target_dir}")
    except json.JSONDecodeError:
        print(f"Error reading JSON from {file_path.name}; file will not be moved.")


def organize_files(directory):
    """Organize JSON files in the given directory based on 'List' key and 'Is Completed' status."""
    base_path = Path(directory)
    json_files = [f for f in base_path.iterdir() if f.suffix == ".json"]

    for file_path in json_files:
        move_file_based_on_json(file_path, base_path)


def main():
    parser = argparse.ArgumentParser(
        description="Organize JSON files based on 'List' key and 'Is Completed' status."
    )
    parser.add_argument(
        "directory", type=str, help="Directory containing JSON files to organize."
    )

    args = parser.parse_args()
    organize_files(args.directory)


if __name__ == "__main__":
    main()
