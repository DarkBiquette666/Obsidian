import re
import os

source_file = r"Z:\D&D\List - Sorts - DnD 5e.md"
output_dir = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Liste des Sorts"

os.makedirs(output_dir, exist_ok=True)

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Updated pattern - flexible newlines and explicit capture groups for niveau and school
spell_pattern = r'# \*\*([^*]+)\*\*\n+\*niveau ([45]) \\- ([^(*]+?)(?:\s*\(rituel\))?\*'
matches = list(re.finditer(spell_pattern, content))

print(f"Found {len(matches)} niveau 4 and 5 spells")

created_files = []
error_count = 0

for i, match in enumerate(matches):
    spell_name = match.group(1)
    niveau = match.group(2)
    school = match.group(3).strip()

    start_pos = match.start()

    if i + 1 < len(matches):
        end_pos = matches[i + 1].start()
    else:
        end_pos = len(content)

    spell_content = content[start_pos:end_pos].rstrip()
    is_ritual = '(rituel)' in spell_content[:200]

    props = {
        'niveau': niveau,
        'école': school,
        'temps_incantation': '',
        'portée': '',
        'composantes': '',
        'durée': '',
        'rituel': is_ritual
    }

    text = spell_content

    # Extract properties using regex to handle both inline and multiline
    timing_match = re.search(r"\*\*Temps d.incantation\*\*\s*:\s*([^\n*]+?)(?=\n|\*\*)", text)
    if timing_match:
        props['temps_incantation'] = timing_match.group(1).strip()

    range_match = re.search(r'\*\*Portée\*\*\s*:\s*([^\n*]+?)(?=\n|\*\*)', text)
    if range_match:
        props['portée'] = range_match.group(1).strip()

    components_match = re.search(r'(?:##\s*)?\*\*Composantes\*\*\s*:\s*([^\n*]+?)(?=\n|\*\*)', text)
    if components_match:
        props['composantes'] = components_match.group(1).strip()

    duration_match = re.search(r'\*\*Durée\*\*\s*:\s*([^\n*]+?)(?=\n|$)', text)
    if duration_match:
        props['durée'] = duration_match.group(1).strip()

    for key in ['temps_incantation', 'portée', 'composantes', 'durée']:
        props[key] = re.sub(r'\*\*([^*]+)\*\*', r'\1', props[key])
        props[key] = props[key].strip()
        props[key] = props[key].replace('"', '\\"')

    school_tag = school.lower().replace(' ', '-').replace('é', 'e').replace('à', 'a').replace('ç', 'c')

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
  - "niveau-{props['niveau']}"
  - "école-{school_tag}"
  - "DnD5e"
aliases:
  - "{spell_name}"
---

"""

    file_content = yaml_front + spell_content

    safe_name = spell_name
    for char in [':', '*', '?', '|', '<', '>', '"']:
        safe_name = safe_name.replace(char, '-')
    safe_name = safe_name.replace(chr(92), '-')

    filename = f"{safe_name}.md"
    filepath = os.path.join(output_dir, filename)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)
        created_files.append({
            'name': spell_name,
            'niveau': niveau,
            'school': school,
            'ritual': props['rituel']
        })
    except Exception as e:
        print(f"Error creating {filename}: {e}")
        error_count += 1

print(f"\n{'='*60}")
print(f"EXTRACTION COMPLETE")
print(f"{'='*60}")
print(f"Total spells found: {len(matches)}")
print(f"Files created successfully: {len(created_files)}")
print(f"Errors encountered: {error_count}")

niveau_4 = [s for s in created_files if s['niveau'] == '4']
niveau_5 = [s for s in created_files if s['niveau'] == '5']

print(f"\nNiveau 4 spells: {len(niveau_4)}")
print(f"Niveau 5 spells: {len(niveau_5)}")

print(f"\nNiveau 4 spells extracted:")
for spell in sorted(niveau_4, key=lambda x: x['name']):
    ritual_marker = " (rituel)" if spell['ritual'] else ""
    print(f"  {spell['name']} - {spell['school']}{ritual_marker}")

print(f"\nNiveau 5 spells extracted:")
for spell in sorted(niveau_5, key=lambda x: x['name']):
    ritual_marker = " (rituel)" if spell['ritual'] else ""
    print(f"  {spell['name']} - {spell['school']}{ritual_marker}")
