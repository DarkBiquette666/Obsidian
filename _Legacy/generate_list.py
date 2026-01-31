#!/usr/bin/env python3
import os

directory = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Resources\Magic Items"
files = sorted([f for f in os.listdir(directory) if f.endswith('.md')])

# Write files 79-156 to a text file
with open(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\files_to_process.txt", 'w', encoding='utf-8') as f:
    for i in range(78, min(156, len(files))):
        f.write(files[i] + '\n')

# Also print to console
for i in range(78, min(156, len(files))):
    print(f"{i+1}: {files[i]}")
