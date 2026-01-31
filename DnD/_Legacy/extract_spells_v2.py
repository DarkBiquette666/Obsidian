import re
import os
import shutil

# Source file
source_file = r"Z:\D&D\List - Sorts - DnD 5e.md"
output_dir = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Liste des Sorts"

# Delete existing files to start fresh
if os.path.exists(output_dir):
    for f in os.listdir(output_dir):
        if f.endswith('.md'):
            os.remove(os.path.join(output_dir, f))

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the entire file
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by spell headers (# **Spell Name**) with required blank line
spell_pattern = r'# \*\*([^*]+)\*\*\n+\*niveau (\d+)'
matches = list(re.finditer(spell_pattern, content))

print(f"Found {len(matches)} total spell headers")

# Filter for level 1 and build list with proper info
level_1_indices = []
for i, match in enumerate(matches):
    spell_name = match.group(1)
    level = int(match.group(2))
    if level == 1:
        level_1_indices.append(i)

print(f"Found {len(level_1_indices)} niveau 1 spells")

spell_count = 0
error_count = 0
level_1_spells = []

for idx in level_1_indices:
    match = matches[idx]
    spell_name = match.group(1)
    level = int(match.group(2))
    
    start_pos = match.start()
    
    # Find the end of this spell (start of next spell or end of file)
    if idx + 1 < len(matches):
        end_pos = matches[idx + 1].start()
    else:
        end_pos = len(content)
    
    spell_content = content[start_pos:end_pos].rstrip()
    
    # Extract school and ritual status from the niveau line
    # Pattern: *niveau X \- school_name (rituel)?*
    level_line_match = re.search(r'\*niveau \d+ \- ([^(*]+?)(?:\s*\(rituel\))?\*', spell_content)
    school = level_line_match.group(1).strip() if level_line_match else "Unknown"
    is_ritual = '(rituel)' in spell_content[:200]
    
    # Extract properties
    props = {
        'niveau': 1,
        'école': school,
        'temps_incantation': '',
        'portée': '',
        'composantes': '',
        'durée': '',
        'rituel': is_ritual
    }
    
    # Extract properties from spell content - look for lines after the level line
    lines = spell_content.split('\n')
    
    # Find the position of the level line
    level_line_idx = -1
    for j, line in enumerate(lines):
        if '*niveau' in line:
            level_line_idx = j
            break
    
    # Extract properties from lines after the level line
    if level_line_idx >= 0:
        for j in range(level_line_idx + 1, len(lines)):
            line = lines[j]
            
            # Stop when we hit the spell description (empty line followed by non-property text)
            if line.strip() == '' and j + 1 < len(lines) and not any(prop in lines[j+1] for prop in ['**Temps', '**Portée', '**Composantes', '**Durée']):
                break
            
            # Look for property lines with colons
            if '**Temps d\'incantation**' in line and ':' in line:
                props['temps_incantation'] = line.split(':', 1)[1].strip()
            elif '**Portée**' in line and ':' in line:
                props['portée'] = line.split(':', 1)[1].strip()
            elif ('**Composantes**' in line or '## **Composantes**' in line) and ':' in line:
                props['composantes'] = line.split(':', 1)[1].strip()
            elif '**Durée**' in line and ':' in line:
                props['durée'] = line.split(':', 1)[1].strip()
    
    # Clean up properties
    for key in ['temps_incantation', 'portée', 'composantes', 'durée']:
        props[key] = re.sub(r'\*\*([^*]+)\*\*', r'\1', props[key])
        props[key] = props[key].strip()
    
    # Create YAML frontmatter
    yaml_front = f"""---
properties:
  niveau: {props['niveau']}
  école: "{props['école']}"
  temps_incantation: "{props['temps_incantation']}"
  portée: "{props['portée']}"
  composantes: "{props['composantes']}"
  durée: "{props['durée']}"
  rituel: {"true" if props['rituel'] else "false"}
source: "DnD 5e"
tags:
  - "niveau-1"
  - "école-{props['école'].lower().replace(' ', '-')}"
  - "DnD5e"
aliases:
  - "{spell_name}"
---

"""
    
    # Combine frontmatter with spell content
    file_content = yaml_front + spell_content
    
    # Create safe filename
    safe_name = spell_name
    # Replace forbidden characters with dash
    forbidden_chars = [':', '*', '?', '|', '<', '>', '"', chr(92)]  # chr(92) is backslash
    for char in forbidden_chars:
        safe_name = safe_name.replace(char, '-')
    
    filename = f"{safe_name}.md"
    filepath = os.path.join(output_dir, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)
        spell_count += 1
        print(f"Created: {filename} ({school})")
    except Exception as e:
        print(f"Error creating {filename}: {e}")
        error_count += 1
    
    level_1_spells.append({
        'name': spell_name,
        'school': school,
        'ritual': is_ritual,
        'filename': filename
    })

print(f"\n{'='*60}")
print(f"EXTRACTION COMPLETE")
print(f"{'='*60}")
print(f"Total niveau 1 spells extracted: {spell_count}")
print(f"Errors encountered: {error_count}")
print(f"\nSchools found:")
schools = {}
for spell in level_1_spells:
    if spell['school'] not in schools:
        schools[spell['school']] = 0
    schools[spell['school']] += 1

for school in sorted(schools.keys()):
    count = schools[school]
    ritual_spells = len([s for s in level_1_spells if s['school'] == school and s['ritual']])
    print(f"  - {school}: {count} spells ({ritual_spells} ritual)")

