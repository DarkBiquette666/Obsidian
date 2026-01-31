import os
import re

# Get all .md files from the Magic Items directory
directory = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Resources\Magic Items"
files = [f for f in os.listdir(directory) if f.endswith('.md')]
files.sort()

# Print files 79-156 (0-indexed, so 78-155)
print("Files 79-156 (alphabetically):")
print("=" * 80)
for i in range(78, min(156, len(files))):
    print(f"{i+1}: {files[i]}")

print(f"\nTotal files: {len(files)}")
print(f"Files to process: {min(156, len(files)) - 78}")
