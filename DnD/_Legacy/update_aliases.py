import os
import re
from pathlib import Path

def generate_aliases(name):
    """Generate all variations of a name (with/without accents, upper/lowercase)"""
    # Map of accented to unaccented characters
    accent_map = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'à': 'a', 'â': 'a', 'ä': 'a',
        'î': 'i', 'ï': 'i',
        'ô': 'o', 'ö': 'o',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'À': 'A', 'Â': 'A', 'Ä': 'A',
        'Î': 'I', 'Ï': 'I',
        'Ô': 'O', 'Ö': 'O',
        'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ç': 'C'
    }

    # Remove accents
    name_no_accent = name
    for accented, unaccented in accent_map.items():
        name_no_accent = name_no_accent.replace(accented, unaccented)

    # Generate variations
    variations = set()

    # Capitalize first letter
    variations.add(name)  # Original with accents
    variations.add(name.lower())  # lowercase with accents

    if name_no_accent != name:
        variations.add(name_no_accent)  # Capitalized without accents
        variations.add(name_no_accent.lower())  # lowercase without accents

    return sorted(list(variations))

def update_file_aliases(file_path):
    """Update aliases in a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract current aliases section
    alias_match = re.search(r'aliases:\n((?:  - .+\n)+)', content)
    if not alias_match:
        print(f"No aliases found in {file_path}")
        return

    # Use the filename (with accents) as the main name
    main_name = file_path.stem

    # Generate all variations
    new_aliases = generate_aliases(main_name)

    # Create new aliases section
    new_aliases_text = "aliases:\n" + "\n".join(f"  - {alias}" for alias in new_aliases)

    # Replace in content
    content = re.sub(r'aliases:\n(?:  - .+\n)+', new_aliases_text + '\n', content)

    # Remove wikilinks [[]]
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {file_path.name}: {len(new_aliases)} aliases")

# Update Propriétés
props_dir = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Objets\Equipmement\Armes\Proprietes")
print("=== Updating Propriétés ===")
for file in props_dir.glob("*.md"):
    update_file_aliases(file)

# Update Bottes
bottes_dir = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Objets\Equipmement\Armes\Botte d'arme")
print("\n=== Updating Bottes ===")
for file in bottes_dir.glob("*.md"):
    if file.name != "Botte d'arme.md":  # Skip the index file
        update_file_aliases(file)

# Update Armes
armes_base = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Objets\Equipmement\Armes\Liste")
print("\n=== Updating Armes ===")
arme_categories = [
    "Armes courantes de corps a corps",
    "Armes courantes a distance",
    "Armes de guerre de corps a corps",
    "Armes de guerre a distance"
]

for category in arme_categories:
    cat_dir = armes_base / category
    if cat_dir.exists():
        for file in cat_dir.glob("*.md"):
            update_file_aliases(file)

print("\nDone!")
