import os
from pathlib import Path

def remove_accents(text):
    """Remove accents from text"""
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
    result = text
    for accented, unaccented in accent_map.items():
        result = result.replace(accented, unaccented)
    return result

def generate_aliases(name):
    """Generate all variations of a name (with/without accents, upper/lowercase)"""
    name_no_accent = remove_accents(name)

    variations = set()
    variations.add(name)  # Original with accents
    variations.add(name.lower())  # lowercase with accents

    if name_no_accent != name:
        variations.add(name_no_accent)  # Capitalized without accents
        variations.add(name_no_accent.lower())  # lowercase without accents

    return sorted(list(variations))

# Outils d'artisan
outils_artisan = [
    {"nom": "Matériel d'alchimiste", "caracteristique": "Intelligence", "poids": 4, "prix": "50 po"},
    {"nom": "Matériel de brasseur", "caracteristique": "Intelligence", "poids": 4.5, "prix": "20 po"},
    {"nom": "Matériel de calligraphe", "caracteristique": "Dextérité", "poids": 2.5, "prix": "10 po"},
    {"nom": "Matériel de peintre", "caracteristique": "Sagesse", "poids": 2.5, "prix": "10 po"},
    {"nom": "Outils de bricoleur", "caracteristique": "Dextérité", "poids": 5, "prix": "50 po"},
    {"nom": "Outils de cartographe", "caracteristique": "Sagesse", "poids": 3, "prix": "15 po"},
    {"nom": "Outils de charpentier", "caracteristique": "Force", "poids": 3, "prix": "8 po"},
    {"nom": "Outils de cordonnier", "caracteristique": "Dextérité", "poids": 2.5, "prix": "5 po"},
    {"nom": "Outils de forgeron", "caracteristique": "Force", "poids": 4, "prix": "20 po"},
    {"nom": "Outils de joaillier", "caracteristique": "Intelligence", "poids": 1, "prix": "25 po"},
    {"nom": "Outils de maçon", "caracteristique": "Force", "poids": 4, "prix": "10 po"},
    {"nom": "Outils de menuisier", "caracteristique": "Dextérité", "poids": 2.5, "prix": "1 po"},
    {"nom": "Outils de potier", "caracteristique": "Intelligence", "poids": 1.5, "prix": "10 po"},
    {"nom": "Outils de souffleur de verre", "caracteristique": "Intelligence", "poids": 2.5, "prix": "30 po"},
    {"nom": "Outils de tanneur", "caracteristique": "Dextérité", "poids": 2.5, "prix": "5 po"},
    {"nom": "Outils de tisserand", "caracteristique": "Dextérité", "poids": 2.5, "prix": "1 po"},
    {"nom": "Ustensiles de cuisinier", "caracteristique": "Sagesse", "poids": 4, "prix": "1 po"}
]

# Autres outils
autres_outils = [
    {"nom": "Accessoires de déguisement", "caracteristique": "Charisme", "poids": 1.5, "prix": "25 po"},
    {"nom": "Instruments de navigateur", "caracteristique": "Sagesse", "poids": 1, "prix": "25 po"},
    {"nom": "Matériel d'empoisonneur", "caracteristique": "Intelligence", "poids": 1, "prix": "50 po"},
    {"nom": "Matériel d'herboriste", "caracteristique": "Intelligence", "poids": 1.5, "prix": "5 po"},
    {"nom": "Matériel de contrefaçon", "caracteristique": "Dextérité", "poids": 2.5, "prix": "15 po"},
    {"nom": "Outils de voleur", "caracteristique": "Dextérité", "poids": 0.5, "prix": "25 po"}
]

# Boîtes de jeux (variantes)
boites_jeux = [
    {"nom": "Cartes à jouer", "parent": "Boîte de jeux", "caracteristique": "Sagesse", "poids": 0, "prix": "5 pa"},
    {"nom": "Dés", "parent": "Boîte de jeux", "caracteristique": "Sagesse", "poids": 0, "prix": "1 pa"},
    {"nom": "Échecs draconiques", "parent": "Boîte de jeux", "caracteristique": "Sagesse", "poids": 0, "prix": "1 po"},
    {"nom": "Jeu des dragons", "parent": "Boîte de jeux", "caracteristique": "Sagesse", "poids": 0, "prix": "1 po"}
]

# Instruments de musique (variantes)
instruments = [
    {"nom": "Chalemie", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 0.5, "prix": "2 po"},
    {"nom": "Cor", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 1, "prix": "3 po"},
    {"nom": "Cornemuse", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 3, "prix": "30 po"},
    {"nom": "Flûte", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 0.5, "prix": "2 po"},
    {"nom": "Flûte de pan", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 1, "prix": "12 po"},
    {"nom": "Luth", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 1, "prix": "35 po"},
    {"nom": "Lyre", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 1, "prix": "30 po"},
    {"nom": "Tambour", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 1.5, "prix": "6 po"},
    {"nom": "Tympanon", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 5, "prix": "25 po"},
    {"nom": "Viole", "parent": "Instrument de musique", "caracteristique": "Charisme", "poids": 0.5, "prix": "30 po"}
]

def create_outil_file(outil, folder, is_variant=False):
    """Create a markdown file for a tool"""
    nom = outil["nom"]

    # Generate aliases
    aliases = generate_aliases(nom)
    aliases_yaml = "\n".join(f"  - {alias}" for alias in aliases)

    # Build tags
    tags = ["glossaire", "equipement", "outil"]
    if is_variant:
        if "parent" in outil and "Boîte" in outil["parent"]:
            tags.append("jeu")
        elif "parent" in outil and "Instrument" in outil["parent"]:
            tags.append("instrument-musique")
    else:
        tags.append("outil-artisan")

    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)

    # Build poids field
    poids_str = f"{outil['poids']} kg" if outil['poids'] > 0 else "—"

    # Build parent info if variant
    parent_info = f"\n*Variante de {outil['parent']}*\n" if is_variant else ""

    # Build content
    content = f"""---
Nom: {nom}
Type: Outil
Categorie: {"Variante" if is_variant else "Outil d'artisan" if folder.name == "Outils d'artisan" else "Autre outil"}
Caracteristique: {outil["caracteristique"]}
Poids: {outil["poids"]}
Prix: {outil["prix"]}
Source: PHB 2024
tags:
{tags_yaml}
aliases:
{aliases_yaml}
---

# {nom}
{parent_info}
*Outil*

**Caractéristique:** {outil["caracteristique"]}
**Poids:** {poids_str} | **Prix:** {outil["prix"]}
"""

    # Write file
    file_path = folder / f"{nom}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created: {file_path.name}")

# Create tool files
base_path = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Objets\Equipmement\Outils\Liste")

print("=== Creating Outils d'artisan ===")
artisan_folder = base_path / "Outils d'artisan"
for outil in outils_artisan:
    create_outil_file(outil, artisan_folder)

print("\n=== Creating Autres outils ===")
autres_folder = base_path / "Autres outils"
for outil in autres_outils:
    create_outil_file(outil, autres_folder)

print("\n=== Creating Boîtes de jeux ===")
for jeu in boites_jeux:
    create_outil_file(jeu, autres_folder, is_variant=True)

print("\n=== Creating Instruments de musique ===")
for instrument in instruments:
    create_outil_file(instrument, autres_folder, is_variant=True)

print(f"\nDone! Created {len(outils_artisan) + len(autres_outils) + len(boites_jeux) + len(instruments)} tool files.")
