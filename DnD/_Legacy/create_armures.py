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

# Armures légères
armures_legeres = [
    {
        "nom": "Armure matelassée",
        "categorie": "Armure légère",
        "ca": "11 + modificateur de Dex",
        "force": "",
        "discretion": "Désavantage",
        "poids": 4,
        "prix": "5 po"
    },
    {
        "nom": "Armure de cuir",
        "categorie": "Armure légère",
        "ca": "11 + modificateur de Dex",
        "force": "",
        "discretion": "",
        "poids": 5,
        "prix": "10 po"
    },
    {
        "nom": "Armure de cuir clouté",
        "categorie": "Armure légère",
        "ca": "12 + modificateur de Dex",
        "force": "",
        "discretion": "",
        "poids": 6.5,
        "prix": "45 po"
    }
]

# Armures intermédiaires
armures_intermediaires = [
    {
        "nom": "Armure de peaux",
        "categorie": "Armure intermédiaire",
        "ca": "12 + modificateur de Dex (max 2)",
        "force": "",
        "discretion": "",
        "poids": 6,
        "prix": "10 po"
    },
    {
        "nom": "Chemise de mailles",
        "categorie": "Armure intermédiaire",
        "ca": "13 + modificateur de Dex (max 2)",
        "force": "",
        "discretion": "",
        "poids": 10,
        "prix": "50 po"
    },
    {
        "nom": "Armure d'écailles",
        "categorie": "Armure intermédiaire",
        "ca": "14 + modificateur de Dex (max 2)",
        "force": "",
        "discretion": "Désavantage",
        "poids": 22.5,
        "prix": "50 po"
    },
    {
        "nom": "Cuirasse",
        "categorie": "Armure intermédiaire",
        "ca": "14 + modificateur de Dex (max 2)",
        "force": "",
        "discretion": "",
        "poids": 10,
        "prix": "400 po"
    },
    {
        "nom": "Demi-plate",
        "categorie": "Armure intermédiaire",
        "ca": "15 + modificateur de Dex (max 2)",
        "force": "",
        "discretion": "Désavantage",
        "poids": 20,
        "prix": "750 po"
    }
]

# Armures lourdes
armures_lourdes = [
    {
        "nom": "Broigne",
        "categorie": "Armure lourde",
        "ca": "14",
        "force": "",
        "discretion": "Désavantage",
        "poids": 20,
        "prix": "30 po"
    },
    {
        "nom": "Cotte de mailles",
        "categorie": "Armure lourde",
        "ca": "16",
        "force": "For 13",
        "discretion": "Désavantage",
        "poids": 27.5,
        "prix": "75 po"
    },
    {
        "nom": "Clibanion",
        "categorie": "Armure lourde",
        "ca": "17",
        "force": "For 15",
        "discretion": "Désavantage",
        "poids": 30,
        "prix": "200 po"
    },
    {
        "nom": "Harnois",
        "categorie": "Armure lourde",
        "ca": "18",
        "force": "For 15",
        "discretion": "Désavantage",
        "poids": 32.5,
        "prix": "1 500 po"
    }
]

def create_armure_file(armure, folder):
    """Create a markdown file for an armor"""
    nom = armure["nom"]
    nom_file = remove_accents(nom)  # Filename without accents for simplicity

    # Generate aliases
    aliases = generate_aliases(nom)
    aliases_yaml = "\n".join(f"  - {alias}" for alias in aliases)

    # Build tags
    tags = ["glossaire", "equipement", "armure"]
    if "légère" in armure["categorie"].lower():
        tags.append("armure-legere")
    elif "intermédiaire" in armure["categorie"].lower():
        tags.append("armure-intermediaire")
    elif "lourde" in armure["categorie"].lower():
        tags.append("armure-lourde")

    if armure["discretion"] == "Désavantage":
        tags.append("discretion-desavantage")

    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)

    # Build force field
    force_yaml = f'Force: "{armure["force"]}"' if armure["force"] else 'Force: ""'

    # Build discretion field
    discretion_yaml = f'Discretion: "{armure["discretion"]}"' if armure["discretion"] else 'Discretion: ""'

    # Build content
    content = f"""---
Nom: {nom}
Categorie: {armure["categorie"]}
CA: {armure["ca"]}
{force_yaml}
{discretion_yaml}
Poids: {armure["poids"]}
Prix: {armure["prix"]}
Source: PHB 2024
tags:
{tags_yaml}
aliases:
{aliases_yaml}
---

# {nom}

*{armure["categorie"]}*

**Classe d'armure (CA):** {armure["ca"]}
**Poids:** {armure["poids"]} kg | **Prix:** {armure["prix"]}
"""

    # Add Force requirement if applicable
    if armure["force"]:
        content += f"\n**Force requise:** {armure['force']}\n"

    # Add Discretion penalty if applicable
    if armure["discretion"]:
        content += f"**Discrétion:** {armure['discretion']}\n"

    # Write file
    file_path = folder / f"{nom}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created: {file_path.name}")

# Create armor files
base_path = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Objets\Equipmement\Armures\Liste")

print("=== Creating Armures légères ===")
legeres_folder = base_path / "Armures légères"
for armure in armures_legeres:
    create_armure_file(armure, legeres_folder)

print("\n=== Creating Armures intermédiaires ===")
intermediaires_folder = base_path / "Armures intermédiaires"
for armure in armures_intermediaires:
    create_armure_file(armure, intermediaires_folder)

print("\n=== Creating Armures lourdes ===")
lourdes_folder = base_path / "Armures lourdes"
for armure in armures_lourdes:
    create_armure_file(armure, lourdes_folder)

# Create Bouclier separately
print("\n=== Creating Bouclier ===")
bouclier = {
    "nom": "Bouclier",
    "categorie": "Bouclier",
    "ca": "+2",
    "force": "",
    "discretion": "",
    "poids": 3,
    "prix": "10 po"
}

bouclier_content = f"""---
Nom: Bouclier
Categorie: Bouclier
CA: +2
Force: ""
Discretion: ""
Poids: 3
Prix: 10 po
Source: PHB 2024
tags:
  - glossaire
  - equipement
  - bouclier
aliases:
  - Bouclier
  - bouclier
---

# Bouclier

*Bouclier*

**Classe d'armure (CA):** +2
**Poids:** 3 kg | **Prix:** 10 po
"""

bouclier_path = base_path / "Bouclier.md"
with open(bouclier_path, 'w', encoding='utf-8') as f:
    f.write(bouclier_content)

print(f"Created: {bouclier_path.name}")

print("\nDone! Created 14 armor files.")
