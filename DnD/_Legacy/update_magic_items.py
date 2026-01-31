#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Directory containing magic items
MAGIC_ITEMS_DIR = r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Resources\Magic Items"

# Rarity mapping
RARITY_MAP = {
    "Peu commun": "Uncommon",
    "peu commun": "Uncommon",
    "Commun": "Common",
    "commun": "Common",
    "Rare": "Rare",
    "rare": "Rare",
    "Très rare": "Very Rare",
    "très rare": "Very Rare",
    "Légendaire": "Legendary",
    "légendaire": "Legendary",
    "Artéfact": "Artifact",
    "artéfact": "Artifact",
    "Artifact": "Artifact",
    "Uncommon": "Uncommon",
    "Common": "Common",
    "Very Rare": "Very Rare",
    "Legendary": "Legendary"
}

# Damage types to look for
DAMAGE_TYPES = ["Feu", "Froid", "Radiant", "Nécrotique", "Tranchant", "Contondant",
                "Perforant", "Acide", "Foudre", "Poison", "Psychique", "Force", "Tonnerre"]

def deduce_category_type(filename, content):
    """Deduce category and type from filename and content"""
    fname_lower = filename.lower()
    content_lower = content.lower()

    # Bijoux
    if 'anneau' in fname_lower:
        return 'Bijou', 'Anneau', None
    elif 'amulette' in fname_lower:
        return 'Bijou', 'Amulette', None
    elif 'collier' in fname_lower:
        return 'Bijou', 'Collier', None
    elif 'bracelet' in fname_lower:
        return 'Bijou', 'Bracelet', None

    # Armes
    elif 'épée' in fname_lower or 'epee' in fname_lower:
        return 'Arme', 'Épée', None
    elif 'arc' in fname_lower and 'arc' not in 'arcanoloth':
        return 'Arme', 'Arc', None
    elif 'arbalète' in fname_lower or 'arbalete' in fname_lower:
        return 'Arme', 'Arbalète', None
    elif 'hache' in fname_lower:
        return 'Arme', 'Hache', None
    elif 'marteau' in fname_lower:
        return 'Arme', 'Marteau', None
    elif 'masse' in fname_lower:
        return 'Arme', 'Masse', None
    elif 'dague' in fname_lower:
        return 'Arme', 'Dague', None
    elif 'lance' in fname_lower:
        return 'Arme', 'Lance', None
    elif 'javeline' in fname_lower:
        return 'Arme', 'Javeline', None
    elif 'trident' in fname_lower:
        return 'Arme', 'Trident', None
    elif 'fouet' in fname_lower:
        return 'Arme', 'Fouet', None
    elif 'fléau' in fname_lower or 'fleau' in fname_lower:
        return 'Arme', 'Fléau', None

    # Items magiques spéciaux
    elif 'baguette' in fname_lower:
        return 'Baguette', 'Baguette', None
    elif 'bâton' in fname_lower or 'baton' in fname_lower:
        return 'Bâton', 'Bâton', None
    elif 'sceptre' in fname_lower:
        return 'Sceptre', 'Sceptre', None

    # Armures et vêtements
    elif 'armure' in fname_lower:
        return 'Armure', 'Armure', None
    elif 'bouclier' in fname_lower:
        return 'Armure', 'Bouclier', None
    elif 'bottes' in fname_lower or 'botte' in fname_lower:
        return 'Armure', 'Bottes', None
    elif 'gants' in fname_lower or 'gant' in fname_lower or 'gantelets' in fname_lower:
        return 'Armure', 'Gants', None
    elif 'heaume' in fname_lower or 'casque' in fname_lower:
        return 'Armure', 'Heaume', None
    elif 'cape' in fname_lower or 'manteau' in fname_lower or 'mante' in fname_lower:
        return 'Armure', 'Cape', None
    elif 'robe' in fname_lower:
        return 'Armure', 'Robe', None
    elif 'cuirasse' in fname_lower or 'harnois' in fname_lower or 'mailles' in fname_lower:
        return 'Armure', 'Torse', None

    # Consommables
    elif 'potion' in fname_lower:
        return 'Potion', 'Potion', None
    elif 'parchemin' in fname_lower:
        return 'Parchemin', 'Parchemin', None
    elif 'elixir' in fname_lower or 'élixir' in fname_lower:
        return 'Potion', 'Élixir', None
    elif 'philtre' in fname_lower:
        return 'Potion', 'Philtre', None

    # Objets merveilleux spécifiques
    elif 'livre' in fname_lower or 'manuel' in fname_lower or 'grimoire' in fname_lower or 'traité' in fname_lower or 'tome' in fname_lower:
        return 'Objet merveilleux', 'Livre', None
    elif 'instrument' in fname_lower or 'luth' in fname_lower or 'flûte' in fname_lower or 'lyre' in fname_lower or 'cor' in fname_lower or 'tambour' in fname_lower or 'accordéon' in fname_lower:
        return 'Objet merveilleux', 'Instrument', None

    # Default
    else:
        return 'Objet merveilleux', 'Objet merveilleux', None

def extract_rarity(content):
    """Extract rarity from content"""
    # Look for patterns like "*Objet merveilleux, rare*" or "Rarity: Rare"
    patterns = [
        r'\*[^*]+,\s*(très rare|rare|peu commun|commun|légendaire|artéfact|artefact|legendary|very rare|uncommon|common|artifact)[^*]*\*',
        r'rarity:\s*(très rare|rare|peu commun|commun|légendaire|artéfact|artefact|legendary|very rare|uncommon|common|artifact)',
        r'Rarity:\s*(Very Rare|Rare|Uncommon|Common|Legendary|Artifact)'
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            rarity_text = match.group(1).strip()
            return RARITY_MAP.get(rarity_text, RARITY_MAP.get(rarity_text.capitalize(), "Uncommon"))

    return "Uncommon"

def requires_attunement(content):
    """Check if item requires attunement"""
    return bool(re.search(r'nécessite un lien|requires attunement', content, re.IGNORECASE))

def extract_damage_types(content):
    """Extract damage types mentioned in content"""
    damages = []
    content_lower = content.lower()

    for dtype in DAMAGE_TYPES:
        if dtype.lower() in content_lower or f"dégâts de {dtype.lower()}" in content_lower or f"degats de {dtype.lower()}" in content_lower:
            damages.append(dtype)

    return damages

def extract_resistances(content):
    """Extract resistance types from content"""
    resistances = []

    # Look for "résistance aux dégâts de X" or "resistance to X damage"
    for dtype in DAMAGE_TYPES:
        if re.search(rf'résistance aux dégâts de {dtype.lower()}|résistance au {dtype.lower()}|resistance to {dtype.lower()}', content, re.IGNORECASE):
            resistances.append(dtype)

    return resistances

def process_file(filepath):
    """Process a single magic item file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already processed
    if content.startswith('---') and 'Categorie:' in content[:200]:
        return False, "Already processed"

    # Extract old frontmatter if exists
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if frontmatter_match:
        body = content[frontmatter_match.end():]
    else:
        body = content

    # Deduce properties
    filename = os.path.basename(filepath)
    categorie, item_type, subtype = deduce_category_type(filename, body)
    rarity = extract_rarity(body)
    attunement = requires_attunement(body)
    damage_types = extract_damage_types(body)
    resistances = extract_resistances(body)

    # Build new frontmatter
    new_frontmatter = "---\n"
    new_frontmatter += f"Categorie: {categorie}\n"
    new_frontmatter += f"Type: {item_type}\n"
    new_frontmatter += f"SubType: {subtype if subtype else 'null'}\n"
    new_frontmatter += f"Rarity: {rarity}\n"
    new_frontmatter += f"RequiresAttunement: {'true' if attunement else 'false'}\n"

    if damage_types:
        new_frontmatter += "DamageType:\n"
        for dt in damage_types:
            new_frontmatter += f"  - {dt}\n"
    else:
        new_frontmatter += "DamageType: []\n"

    if resistances:
        new_frontmatter += "Resistance:\n"
        for res in resistances:
            new_frontmatter += f"  - {res}\n"
    else:
        new_frontmatter += "Resistance: []\n"

    new_frontmatter += "---\n"

    # Write new content
    new_content = new_frontmatter + body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, f"Updated: {categorie} / {item_type}"

def main():
    """Main processing function"""
    files = sorted([f for f in os.listdir(MAGIC_ITEMS_DIR) if f.endswith('.md')])

    print(f"Found {len(files)} markdown files")

    updated_count = 0
    skipped_count = 0

    for i, filename in enumerate(files, 1):
        filepath = os.path.join(MAGIC_ITEMS_DIR, filename)

        try:
            updated, msg = process_file(filepath)
            if updated:
                updated_count += 1
                print(f"[{i}/{len(files)}] OK {filename}: {msg}")
            else:
                skipped_count += 1
                if i % 50 == 0:
                    print(f"[{i}/{len(files)}] -- {filename}: {msg}")
        except Exception as e:
            print(f"[{i}/{len(files)}] !! {filename}: ERROR - {str(e)}")

    print(f"\n=== Summary ===")
    print(f"Total files: {len(files)}")
    print(f"Updated: {updated_count}")
    print(f"Skipped: {skipped_count}")

if __name__ == "__main__":
    main()
