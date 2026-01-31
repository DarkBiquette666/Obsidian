import re
import os

source_file = r"Z:\D&D\List - Sorts - DnD 5e.md"
output_dir = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Liste des Sorts"

os.makedirs(output_dir, exist_ok=True)

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all spells with niveau 4 or 5
spell_pattern = r'# \*\*([^*]+)\*\*\n\n\*niveau ([45]) \\- ([^(*]+)(?:\s*\(rituel\))?\*'
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

    lines = spell_content.split('\n')
    for j, line in enumerate(lines):
        if '**Temps d\'incantation**' in line:
            if ':' in line:
                props['temps_incantation'] = line.split(':', 1)[1].strip()
        elif '**Portée**' in line:
            if ':' in line:
                portee = line.split(':', 1)[1].strip()
                if '**Composantes**' in portee:
                    props['portée'] = portee.split('**Composantes**')[0].strip()
                else:
                    props['portée'] = portee
        elif '**Composantes**' in line and '**Portée**' not in line:
            if ':' in line:
                props['composantes'] = line.split(':', 1)[1].strip()
        elif '## **Composantes**' in line:
            if ':' in line:
                props['composantes'] = line.split(':', 1)[1].strip()
        elif '**Durée**' in line:
            if ':' in line:
                props['durée'] = line.split(':', 1)[1].strip()

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

print(f"\nNiveau 4 spells:")
for spell in sorted(niveau_4, key=lambda x: x['name']):
    ritual_marker = " (rituel)" if spell['ritual'] else ""
    print(f"  {spell['name']} - {spell['school']}{ritual_marker}")

print(f"\nNiveau 5 spells:")
for spell in sorted(niveau_5, key=lambda x: x['name']):
    ritual_marker = " (rituel)" if spell['ritual'] else ""
    print(f"  {spell['name']} - {spell['school']}{ritual_marker}")
