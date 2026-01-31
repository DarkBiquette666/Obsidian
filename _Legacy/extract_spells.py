#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract individual D&D 5e spells from master list into separate Markdown files.
"""

import re
import os
from pathlib import Path

# Configuration
SOURCE_FILE = r"Z:\D&D\List - Sorts - DnD 5e.md"
TARGET_DIR = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Liste des Sorts"

# Schools of magic mapping
SCHOOLS = {
    "abjuration": "abjuration",
    "transmutation": "transmutation",
    "enchantement": "enchantement",
    "invocation": "invocation",
    "divination": "divination",
    "évocation": "évocation",
    "nécromancie": "nécromancie",
    "illusion": "illusion"
}

def sanitize_filename(name):
    """Sanitize spell name for use as filename."""
    # Keep French accents, replace forbidden Windows characters
    forbidden = ['<', '>', ':', '"', '|', '?', '*', '\\', '/']
    for char in forbidden:
        name = name.replace(char, '-')
    return name.strip()

def extract_property(lines, prop_name, start_idx=0):
    """Extract a property value from spell lines."""
    pattern = rf'\*\*{re.escape(prop_name)}\*\*\s*:\s*(.+?)(?=\*\*|$)'
    pattern_h2 = rf'##\s*\*\*{re.escape(prop_name)}\*\*\s*:\s*(.+?)(?=\*\*|$)'

    for i in range(start_idx, min(start_idx + 20, len(lines))):
        line = lines[i]
        # Try regular pattern
        match = re.search(pattern, line)
        if match:
            return match.group(1).strip()
        # Try H2 pattern
        match = re.search(pattern_h2, line)
        if match:
            return match.group(1).strip()

    return ""

def parse_spell(lines, start_idx):
    """Parse a single spell from lines starting at start_idx."""
    spell = {}

    # Extract spell name from H1 header
    name_match = re.match(r'^#\s+\*\*([^*]+)\*\*', lines[start_idx])
    if not name_match:
        return None

    spell['name'] = name_match.group(1).strip()

    # Find level/school line
    spell['niveau'] = 0
    spell['école'] = ""
    spell['rituel'] = False

    for i in range(start_idx + 1, min(start_idx + 10, len(lines))):
        level_match = re.match(r'^\*niveau\s+(\d+)\s+\\-\s+([^*\(]+)(?:\s*\(rituel\))?\*', lines[i])
        if level_match:
            spell['niveau'] = int(level_match.group(1))
            spell['école'] = level_match.group(2).strip()
            spell['rituel'] = '(rituel)' in lines[i]
            break

    # Extract properties
    spell['temps_incantation'] = extract_property(lines, "Temps d'incantation", start_idx)
    spell['portée'] = extract_property(lines, "Portée", start_idx)
    spell['composantes'] = extract_property(lines, "Composantes", start_idx)
    spell['durée'] = extract_property(lines, "Durée", start_idx)

    # Find spell end (next H1 header or section header or EOF)
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if re.match(r'^#\s+\*\*', lines[i]) or re.match(r'^\*\*NIVEAU\s+\d+\*\*', lines[i]):
            end_idx = i
            break

    # Collect spell content
    spell['content'] = '\n'.join(lines[start_idx:end_idx]).strip()

    return spell, end_idx

def create_spell_file(spell, target_dir):
    """Create a Markdown file for a spell."""
    # Create frontmatter
    frontmatter = f"""---
Niveau: {spell['niveau']}
Ecole: {spell['école']}
Temps d'incantation: {spell['temps_incantation']}
Durée: {spell['durée']}
Portée: {spell['portée']}
Composante: {spell['composantes']}
Rituel: {str(spell['rituel']).lower()}
Source: DnD 5e
tags:
  - niveau-{spell['niveau']}
  - école-{spell['école']}
  - DnD5e
aliases:
  - {spell['name']}
---

"""

    # Combine frontmatter and content
    content = frontmatter + spell['content']

    # Create filename
    filename = sanitize_filename(spell['name']) + '.md'
    filepath = os.path.join(target_dir, filename)

    # Write file (overwrite if exists to fix broken properties)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename

def main():
    """Main extraction function."""
    print(f"Reading source file: {SOURCE_FILE}")

    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Strip newlines but keep lines
    lines = [line.rstrip('\n') for line in lines]

    print(f"Total lines: {len(lines)}")

    # Find all spell headers
    spell_indices = []
    for i, line in enumerate(lines):
        if re.match(r'^#\s+\*\*[^*]+\*\*\s*$', line):
            # Skip empty headers like "# "
            if len(line.strip()) > 3:
                spell_indices.append(i)

    print(f"Found {len(spell_indices)} spell headers")

    # Parse and create files
    created = 0
    errors = []

    idx = 0
    while idx < len(lines):
        # Find next spell header
        if not re.match(r'^#\s+\*\*[^*]+\*\*\s*$', lines[idx]):
            idx += 1
            continue

        try:
            result = parse_spell(lines, idx)
            if result is None:
                idx += 1
                continue

            spell, next_idx = result

            # Create file
            filename = create_spell_file(spell, TARGET_DIR)
            if filename:
                created += 1

            if created % 50 == 0:
                print(f"Processed {created} spells...")

            idx = next_idx

        except Exception as e:
            errors.append(f"Error at line {idx}: {e}")
            idx += 1

    print(f"\n=== EXTRACTION COMPLETE ===")
    print(f"Files created: {created}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors encountered:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")

if __name__ == "__main__":
    main()
