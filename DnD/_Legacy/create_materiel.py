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

# Matériel d'aventurier - items principaux
materiel = [
    {"nom": "Acide", "poids": 0.5, "prix": "25 po", "categorie": "Consommable"},
    {"nom": "Antidote", "poids": 0, "prix": "50 po", "categorie": "Consommable"},
    {"nom": "Beaux habits", "poids": 3, "prix": "15 po", "categorie": "Vêtement"},
    {"nom": "Bélier portable", "poids": 17.5, "prix": "4 po", "categorie": "Équipement"},
    {"nom": "Billes", "poids": 1, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Boîte à amadou", "poids": 0.5, "prix": "5 pa", "categorie": "Équipement"},
    {"nom": "Bougie", "poids": 0, "prix": "1 pc", "categorie": "Éclairage"},
    {"nom": "Bouteille, verre", "poids": 1, "prix": "2 po", "categorie": "Contenant"},
    {"nom": "Cadenas", "poids": 0.5, "prix": "10 po", "categorie": "Équipement"},
    {"nom": "Carquois", "poids": 0.5, "prix": "1 po", "categorie": "Contenant"},
    {"nom": "Carte", "poids": 0, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Chaîne", "poids": 5, "prix": "5 po", "categorie": "Équipement"},
    {"nom": "Chausse-trappes", "poids": 1, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Cloche", "poids": 0, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Coffre", "poids": 12.5, "prix": "5 po", "categorie": "Contenant"},
    {"nom": "Corde", "poids": 2.5, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Costume", "poids": 2, "prix": "5 po", "categorie": "Vêtement"},
    {"nom": "Couverture", "poids": 1.5, "prix": "5 pa", "categorie": "Équipement"},
    {"nom": "Cruche", "poids": 2, "prix": "2 pc", "categorie": "Contenant"},
    {"nom": "Eau bénite", "poids": 0.5, "prix": "25 po", "categorie": "Consommable"},
    {"nom": "Échelle", "poids": 12.5, "prix": "1 pa", "categorie": "Équipement"},
    {"nom": "Encre", "poids": 0, "prix": "10 po", "categorie": "Équipement"},
    {"nom": "Étui à cartes ou à parchemins", "poids": 0.5, "prix": "1 po", "categorie": "Contenant"},
    {"nom": "Étui pour carreaux d'arbalète", "poids": 0.5, "prix": "1 po", "categorie": "Contenant"},
    {"nom": "Feu grégeois", "poids": 0.5, "prix": "50 po", "categorie": "Consommable"},
    {"nom": "Ficelle", "poids": 0, "prix": "1 pa", "categorie": "Équipement"},
    {"nom": "Filet", "poids": 1.5, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Fiole", "poids": 0, "prix": "1 po", "categorie": "Contenant"},
    {"nom": "Flasque", "poids": 0.5, "prix": "2 pc", "categorie": "Contenant"},
    {"nom": "Grappin", "poids": 2, "prix": "2 po", "categorie": "Équipement"},
    {"nom": "Huile", "poids": 0.5, "prix": "1 pa", "categorie": "Consommable"},
    {"nom": "Lampe", "poids": 0.5, "prix": "5 pa", "categorie": "Éclairage"},
    {"nom": "Lanterne à capote", "poids": 1, "prix": "5 po", "categorie": "Éclairage"},
    {"nom": "Lanterne sourde", "poids": 1, "prix": "10 po", "categorie": "Éclairage"},
    {"nom": "Livre", "poids": 2.5, "prix": "25 po", "categorie": "Équipement"},
    {"nom": "Longue-vue", "poids": 0.5, "prix": "1 000 po", "categorie": "Équipement"},
    {"nom": "Loupe", "poids": 0, "prix": "100 po", "categorie": "Équipement"},
    {"nom": "Matériel d'escalade", "poids": 6, "prix": "25 po", "categorie": "Équipement"},
    {"nom": "Menottes", "poids": 3, "prix": "2 po", "categorie": "Équipement"},
    {"nom": "Miroir", "poids": 0.25, "prix": "5 po", "categorie": "Équipement"},
    {"nom": "Outre", "poids": 2.5, "prix": "2 pa", "categorie": "Contenant"},
    {"nom": "Palan", "poids": 2.5, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Panier", "poids": 1, "prix": "4 pa", "categorie": "Contenant"},
    {"nom": "Papier", "poids": 0, "prix": "2 pa", "categorie": "Équipement"},
    {"nom": "Parchemin", "poids": 0, "prix": "1 pa", "categorie": "Équipement"},
    {"nom": "Parchemin de sort (1er niveau)", "poids": 0, "prix": "50 po", "categorie": "Objet magique"},
    {"nom": "Parchemin de sort (sort mineur)", "poids": 0, "prix": "30 po", "categorie": "Objet magique"},
    {"nom": "Parfum", "poids": 0, "prix": "5 po", "categorie": "Équipement"},
    {"nom": "Pelle", "poids": 2.5, "prix": "2 po", "categorie": "Équipement"},
    {"nom": "Perche", "poids": 3.5, "prix": "5 pc", "categorie": "Équipement"},
    {"nom": "Pied-de-biche", "poids": 2.5, "prix": "2 po", "categorie": "Équipement"},
    {"nom": "Piège à mâchoires", "poids": 12.5, "prix": "5 po", "categorie": "Équipement"},
    {"nom": "Pointes en fer", "poids": 2.5, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Poison standard", "poids": 0, "prix": "100 po", "categorie": "Consommable"},
    {"nom": "Porte-plume", "poids": 0, "prix": "2 pc", "categorie": "Équipement"},
    {"nom": "Pot en fer", "poids": 5, "prix": "2 po", "categorie": "Contenant"},
    {"nom": "Potion de guérison", "poids": 0.25, "prix": "50 po", "categorie": "Objet magique"},
    {"nom": "Rations", "poids": 1, "prix": "5 pa", "categorie": "Consommable"},
    {"nom": "Robe", "poids": 2, "prix": "1 po", "categorie": "Vêtement"},
    {"nom": "Sac", "poids": 0.25, "prix": "1 pc", "categorie": "Contenant"},
    {"nom": "Sac à dos", "poids": 2.5, "prix": "2 po", "categorie": "Contenant"},
    {"nom": "Sac de couchage", "poids": 3.5, "prix": "1 po", "categorie": "Équipement"},
    {"nom": "Sacoche", "poids": 0.5, "prix": "5 pa", "categorie": "Contenant"},
    {"nom": "Sacoche à composantes", "poids": 1, "prix": "25 po", "categorie": "Équipement"},
    {"nom": "Seau", "poids": 1, "prix": "5 pc", "categorie": "Contenant"},
    {"nom": "Sifflet", "poids": 0, "prix": "5 pc", "categorie": "Équipement"},
    {"nom": "Tente", "poids": 10, "prix": "2 po", "categorie": "Équipement"},
    {"nom": "Tenue de voyage", "poids": 2, "prix": "2 po", "categorie": "Vêtement"},
    {"nom": "Tonneau", "poids": 35, "prix": "2 po", "categorie": "Contenant"},
    {"nom": "Torche", "poids": 0.5, "prix": "1 pc", "categorie": "Éclairage"},
    {"nom": "Trousse de soins", "poids": 1.5, "prix": "5 po", "categorie": "Équipement"}
]

# Paquetages
paquetages = [
    {"nom": "Paquetage d'artiste", "poids": 29, "prix": "40 po"},
    {"nom": "Paquetage d'ecclésiastique", "poids": 14.5, "prix": "33 po"},
    {"nom": "Paquetage d'érudit", "poids": 11, "prix": "40 po"},
    {"nom": "Paquetage d'explorateur", "poids": 27.5, "prix": "10 po"},
    {"nom": "Paquetage d'exploration souterraine", "poids": 27.5, "prix": "12 po"},
    {"nom": "Paquetage de cambrioleur", "poids": 21, "prix": "16 po"},
    {"nom": "Paquetage de diplomate", "poids": 19.5, "prix": "39 po"}
]

# Focaliseurs arcaniques
focaliseurs_arcaniques = [
    {"nom": "Baguette", "parent": "Focaliseur arcanique", "poids": 0.5, "prix": "10 po"},
    {"nom": "Bâton", "parent": "Focaliseur arcanique", "poids": 2, "prix": "5 po"},
    {"nom": "Cristal", "parent": "Focaliseur arcanique", "poids": 0.5, "prix": "10 po"},
    {"nom": "Orbe", "parent": "Focaliseur arcanique", "poids": 1.5, "prix": "20 po"},
    {"nom": "Sceptre", "parent": "Focaliseur arcanique", "poids": 1, "prix": "10 po"}
]

# Focaliseurs druidiques
focaliseurs_druidiques = [
    {"nom": "Baguette d'if", "parent": "Focaliseur druidique", "poids": 0.5, "prix": "10 po"},
    {"nom": "Bâton en bois", "parent": "Focaliseur druidique", "poids": 2, "prix": "5 po"},
    {"nom": "Branche de houx", "parent": "Focaliseur druidique", "poids": 0, "prix": "1 po"}
]

# Symboles sacrés
symboles_sacres = [
    {"nom": "Amulette", "parent": "Symbole sacré", "poids": 0.5, "prix": "5 po"},
    {"nom": "Emblème", "parent": "Symbole sacré", "poids": 0, "prix": "5 po"},
    {"nom": "Reliquaire", "parent": "Symbole sacré", "poids": 1, "prix": "5 po"}
]

# Munitions
munitions = [
    {"nom": "Balles d'arme à feu", "parent": "Munitions", "poids": 1, "prix": "3 po", "quantite": "10"},
    {"nom": "Billes de fronde", "parent": "Munitions", "poids": 0.75, "prix": "4 pc", "quantite": "20"},
    {"nom": "Carreaux", "parent": "Munitions", "poids": 0.75, "prix": "1 po", "quantite": "20"},
    {"nom": "Dards", "parent": "Munitions", "poids": 0.5, "prix": "1 po", "quantite": "50"},
    {"nom": "Flèches", "parent": "Munitions", "poids": 0.5, "prix": "1 po", "quantite": "20"}
]

def create_materiel_file(item, folder, is_variant=False):
    """Create a markdown file for adventuring gear"""
    nom = item["nom"]

    # Generate aliases
    aliases = generate_aliases(nom)
    aliases_yaml = "\n".join(f"  - {alias}" for alias in aliases)

    # Build tags
    tags = ["glossaire", "equipement", "materiel-aventurier"]

    if "categorie" in item:
        cat = item["categorie"].lower()
        if "consommable" in cat:
            tags.append("consommable")
        elif "éclairage" in cat or "eclairage" in cat:
            tags.append("eclairage")
        elif "contenant" in cat:
            tags.append("contenant")
        elif "vêtement" in cat or "vetement" in cat:
            tags.append("vetement")
        elif "magique" in cat:
            tags.append("objet-magique")

    if is_variant:
        if "parent" in item:
            if "Focaliseur arcanique" in item["parent"]:
                tags.append("focaliseur-arcanique")
            elif "Focaliseur druidique" in item["parent"]:
                tags.append("focaliseur-druidique")
            elif "Symbole" in item["parent"]:
                tags.append("symbole-sacre")
            elif "Munitions" in item["parent"]:
                tags.append("munitions")

    if "Paquetage" in nom:
        tags.append("paquetage")

    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)

    # Build poids field
    poids_str = f"{item['poids']} kg" if item['poids'] > 0 else "—"

    # Build parent info if variant
    parent_info = f"\n*Variante de {item['parent']}*\n" if is_variant else ""

    # Build quantité info for munitions
    quantite_info = f"\n**Quantité:** {item['quantite']}" if "quantite" in item else ""

    # Build content
    content = f"""---
Nom: {nom}
Type: Matériel d'aventurier
Categorie: {item.get("categorie", "Variante" if is_variant else "Équipement")}
Poids: {item["poids"]}
Prix: {item["prix"]}
Source: PHB 2024
tags:
{tags_yaml}
aliases:
{aliases_yaml}
---

# {nom}
{parent_info}
*Matériel d'aventurier*

**Poids:** {poids_str} | **Prix:** {item["prix"]}{quantite_info}
"""

    # Write file
    file_path = folder / f"{nom}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created: {file_path.name}")

# Create materiel files
base_path = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Objets\Equipmement\Matériel d'aventurier\Liste")

print("=== Creating Matériel d'aventurier ===")
for item in materiel:
    create_materiel_file(item, base_path)

print("\n=== Creating Paquetages ===")
for paquetage in paquetages:
    paquetage["categorie"] = "Paquetage"
    create_materiel_file(paquetage, base_path)

print("\n=== Creating Focaliseurs arcaniques ===")
for focaliseur in focaliseurs_arcaniques:
    create_materiel_file(focaliseur, base_path, is_variant=True)

print("\n=== Creating Focaliseurs druidiques ===")
for focaliseur in focaliseurs_druidiques:
    create_materiel_file(focaliseur, base_path, is_variant=True)

print("\n=== Creating Symboles sacrés ===")
for symbole in symboles_sacres:
    create_materiel_file(symbole, base_path, is_variant=True)

print("\n=== Creating Munitions ===")
for munition in munitions:
    create_materiel_file(munition, base_path, is_variant=True)

total = len(materiel) + len(paquetages) + len(focaliseurs_arcaniques) + len(focaliseurs_druidiques) + len(symboles_sacres) + len(munitions)
print(f"\nDone! Created {total} adventuring gear files.")
