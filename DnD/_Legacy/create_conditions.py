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

# États/Conditions
conditions = [
    {
        "nom": "À terre",
        "description": """Une créature à terre ne peut se déplacer qu'en rampant, sauf si elle se relève et met ainsi un terme à l'état.

La créature subit un Désavantage aux jets d'attaque.

Un jet d'attaque contre une créature bénéficie d'un Avantage si l'attaquant se trouve dans un rayon de 1,50 m de la créature. Dans le cas contraire, le jet d'attaque subit un Désavantage."""
    },
    {
        "nom": "Agrippé",
        "description": """La vitesse d'une créature agrippée passe à 0 et elle ne peut bénéficier d'aucun bonus de vitesse.

L'état prend fin si l'agresseur est neutralisé.

L'état prend fin également si un effet retire la créature agrippée de la portée de l'agresseur ou de l'effet d'empoignade, par exemple lorsqu'une créature est projetée par le sort vague tonnante."""
    },
    {
        "nom": "Assourdi",
        "description": """Une créature assourdie n'entend pas et rate automatiquement tout jet de caractéristique qui nécessite l'ouïe."""
    },
    {
        "nom": "Aveuglé",
        "description": """Une créature aveuglée ne voit pas et rate automatiquement tout jet de caractéristique qui nécessite la vue.

Les jets d'attaque contre la créature bénéficient d'un Avantage et les jets d'attaque de la créature subissent un Désavantage."""
    },
    {
        "nom": "Charmé",
        "description": """Une créature charmée ne peut pas attaquer celui qui l'a charmée ni le cibler avec des capacités ou des effets magiques nuisibles.

Celui qui a charmé la créature bénéficie d'un Avantage à tout jet de caractéristique visant à interagir socialement avec elle."""
    },
    {
        "nom": "Effrayé",
        "description": """Une créature effrayée subit un Désavantage aux jets de caractéristique et d'attaque tant que la source de sa peur se trouve dans sa ligne de mire.

La créature ne peut pas se rapprocher de plein gré de la source de sa peur."""
    },
    {
        "nom": "Empoisonné",
        "description": """Une créature empoisonnée subit un Désavantage aux jets d'attaque et de caractéristique."""
    },
    {
        "nom": "Entravé",
        "description": """La vitesse d'une créature entravée passe à 0 et elle ne peut bénéficier d'aucun bonus de vitesse.

Les jets d'attaque contre la créature bénéficient d'un Avantage et les jets d'attaque de la créature subissent un Désavantage.

La créature subit un Désavantage aux jets de sauvegarde de Dextérité."""
    },
    {
        "nom": "Étourdi",
        "description": """Une créature étourdie est neutralisée, ne peut pas se déplacer et ne parle que de façon hésitante.

La créature rate automatiquement les jets de sauvegarde de Force et de Dextérité.

Les jets d'attaque contre la créature bénéficient d'un Avantage."""
    },
    {
        "nom": "Incapable d'agir",
        "description": """Une créature incapable d'agir ne peut pas entreprendre d'action ni de réaction."""
    },
    {
        "nom": "Inconscient",
        "description": """Une créature inconsciente est neutralisée, ne peut pas se déplacer ni parler et n'a pas conscience de ce qui l'entoure.

La créature lâche tout ce qu'elle tenait et tombe à terre.

La créature rate automatiquement les jets de sauvegarde de Force et de Dextérité.

Les jets d'attaque contre la créature bénéficient d'un Avantage.

Toute attaque qui touche la créature est un coup critique si l'attaquant se trouve dans un rayon de 1,50 m de la créature."""
    },
    {
        "nom": "Invisible",
        "description": """Une créature invisible est impossible à voir sans l'aide de la magie ou d'un sens spécial. Dans le cadre de cet état, la créature est considérée comme lourdement obscurcie. La position de la créature peut être détectée par les bruits qu'elle fait ou les traces qu'elle laisse.

Les jets d'attaque contre la créature subissent un Désavantage et les jets d'attaque de la créature bénéficient d'un Avantage."""
    },
    {
        "nom": "Paralysé",
        "description": """Une créature paralysée est neutralisée et ne peut pas se déplacer ni parler.

La créature rate automatiquement les jets de sauvegarde de Force et de Dextérité.

Les jets d'attaque contre la créature bénéficient d'un Avantage.

Toute attaque qui touche la créature est un coup critique si l'attaquant se trouve dans un rayon de 1,50 m de la créature."""
    },
    {
        "nom": "Pétrifié",
        "description": """Une créature pétrifiée est transformée, ainsi que tous les objets non magiques qu'elle porte ou transporte, en une substance inanimée solide (généralement de la pierre). Son poids est multiplié par dix et elle cesse de vieillir.

La créature est neutralisée, ne peut pas se déplacer ni parler et n'a pas conscience de ce qui l'entoure.

Les jets d'attaque contre la créature bénéficient d'un Avantage.

La créature rate automatiquement les jets de sauvegarde de Force et de Dextérité.

La créature est résistante à tous les dégâts.

La créature est immunisée contre le poison et la maladie, mais un poison ou une maladie déjà dans son organisme est seulement suspendu, pas neutralisé."""
    },
    {
        "nom": "Épuisement",
        "description": """Certaines capacités spéciales et certains périls environnementaux, comme la famine et les effets d'une exposition prolongée au froid ou à la chaleur, peuvent entraîner un état spécial appelé épuisement. L'épuisement se mesure en six niveaux. Un effet peut infliger un ou plusieurs niveaux d'épuisement, comme indiqué dans la description de l'effet.

**Niveau 1** : Désavantage aux jets de caractéristique
**Niveau 2** : Vitesse divisée par 2
**Niveau 3** : Désavantage aux jets d'attaque et de sauvegarde
**Niveau 4** : Maximum de points de vie divisé par 2
**Niveau 5** : Vitesse réduite à 0
**Niveau 6** : Mort

Si une créature déjà épuisée subit un autre effet qui provoque l'épuisement, son niveau d'épuisement actuel augmente du montant indiqué dans la description de l'effet.

Une créature souffre des effets de son niveau d'épuisement actuel ainsi que de tous les niveaux inférieurs. Par exemple, une créature souffrant d'un épuisement de niveau 2 voit sa vitesse divisée par 2 et subit un désavantage à tous ses jets de caractéristique.

Un effet qui supprime l'épuisement réduit son niveau tel qu'indiqué dans la description de l'effet, tous les effets de l'épuisement prenant fin si le niveau d'épuisement d'une créature est réduit à moins de 1.

Terminer un repos long réduit le niveau d'épuisement d'une créature de 1, à condition qu'elle ait pu également s'alimenter et s'abreuver."""
    }
]

def create_condition_file(condition, folder):
    """Create a markdown file for a condition"""
    nom = condition["nom"]

    # Generate aliases
    aliases = generate_aliases(nom)
    aliases_yaml = "\n".join(f"  - {alias}" for alias in aliases)

    # Build tags
    tags = ["glossaire", "condition", "etat"]

    # Add specific tag for Épuisement
    if nom == "Épuisement":
        tags.append("epuisement")
    else:
        tags.append("combat")

    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)

    # Build content
    content = f"""---
Nom: {nom}
Type: Condition
Categorie: État
Source: PHB 2024
tags:
{tags_yaml}
aliases:
{aliases_yaml}
---

# {nom}

*Condition*

{condition["description"]}
"""

    # Write file
    file_path = folder / f"{nom}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created: {file_path.name}")

# Create condition files
base_path = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Conditions")

print("=== Creating Conditions/États ===")
for condition in conditions:
    create_condition_file(condition, base_path)

print(f"\nDone! Created {len(conditions)} condition files.")
