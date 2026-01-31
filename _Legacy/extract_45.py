import re
import os

source_file = r"Z:\D&D\List - Sorts - DnD 5e.md"
output_dir = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Liste des Sorts"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all niveau 4 and 5 spells with flexible pattern
spell_pattern = r'# \*\*(.+?)\*\*.+?\*niveau ([45]) \\- (.+?)\*'
matches = list(re.finditer(spell_pattern, content, re.DOTALL))

print(f"Found {len(matches)} spells")

created = 0
errors = 0

for i, match in enumerate(matches):
    spell_name = match.group(1)
    niveau = match.group(2)
    school = match.group(3).strip()

    start_pos = match.start()
    end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)

    spell_content = content[start_pos:end_pos].rstrip()
    is_ritual = '(rituel)' in spell_content[:300]

    # Extract properties
    props = {'niveau': niveau, 'école': school, 'temps_incantation': '', 'portée': '', 'composantes': '', 'durée': '', 'rituel': is_ritual}

    timing_match = re.search(r"\*\*Temps d.incantation\*\*\s*:\s*([^\n*]+?)(?=\n|\*\*)", spell_content)
    if timing_match:
        props['temps_incantation'] = timing_match.group(1).strip()

    range_match = re.search(r'\*\*Portée\*\*\s*:\s*([^\n*]+?)(?=\n|\*\*)', spell_content)
    if range_match:
        props['portée'] = range_match.group(1).strip()

    components_match = re.search(r'(?:##\s*)?\*\*Composantes\*\*\s*:\s*([^\n*]+?)(?=\n|\*\*)', spell_content)
    if components_match:
        props['composantes'] = components_match.group(1).strip()

    duration_match = re.search(r'\*\*Durée\*\*\s*:\s*([^\n*]+?)(?=\n|$)', spell_content)
    if duration_match:
        props['durée'] = duration_match.group(1).strip()

    for key in ['temps_incantation', 'portée', 'composantes', 'durée']:
        props[key] = re.sub(r'\*\*([^*]+)\*\*', r'\1', props[key]).strip().replace('"', '\\"')

    school_tag = school.lower().replace(' ', '-').replace('é', 'e')

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
        created += 1
    except Exception as e:
        print(f"Error: {filename} - {e}")
        errors += 1

print(f"\nResult: {created} files created, {errors} errors")
