#!/usr/bin/env python3
"""
Script d'importation des classes depuis aidedd.org vers le vault Obsidian.
Genere des fichiers Markdown avec des blocs dnd-classe en YAML.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from pathlib import Path

# Configuration
BASE_URL = "https://www.aidedd.org"
OUTPUT_DIR = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Classes")
DELAY_BETWEEN_REQUESTS = 0.5

# Headers pour les requetes
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
}

# Liste des classes a scraper avec leurs slugs
CLASSES = [
    {'name': 'Barbare', 'slug': 'barbare', 'en': 'Barbarian'},
    {'name': 'Barde', 'slug': 'barde', 'en': 'Bard'},
    {'name': 'Clerc', 'slug': 'clerc', 'en': 'Cleric'},
    {'name': 'Druide', 'slug': 'druide', 'en': 'Druid'},
    {'name': 'Ensorceleur', 'slug': 'ensorceleur', 'en': 'Sorcerer'},
    {'name': 'Guerrier', 'slug': 'guerrier', 'en': 'Fighter'},
    {'name': 'Magicien', 'slug': 'magicien', 'en': 'Wizard'},
    {'name': 'Moine', 'slug': 'moine', 'en': 'Monk'},
    {'name': 'Occultiste', 'slug': 'occultiste', 'en': 'Warlock'},
    {'name': 'Paladin', 'slug': 'paladin', 'en': 'Paladin'},
    {'name': 'Rodeur', 'slug': 'rodeur', 'en': 'Ranger'},
    {'name': 'Roublard', 'slug': 'roublard', 'en': 'Rogue'},
]

# Donnees de base des classes (pour completer le scraping)
CLASS_DATA = {
    'barbare': {
        'des_de_vie': 'd12',
        'pv_niveau_1': '12 + Con',
        'pv_niveaux_suivants': '1d12 (ou 7) + Con',
        'sauvegardes': ['Force', 'Constitution'],
        'armures': ['armures legeres', 'armures intermediaires', 'boucliers'],
        'armes': ['armes courantes', 'armes de guerre'],
        'outils': [],
        'competences_choix': 2,
        'competences_liste': ['Athletisme', 'Dressage', 'Intimidation', 'Nature', 'Perception', 'Survie'],
    },
    'barde': {
        'des_de_vie': 'd8',
        'pv_niveau_1': '8 + Con',
        'pv_niveaux_suivants': '1d8 (ou 5) + Con',
        'sauvegardes': ['Dexterite', 'Charisme'],
        'armures': ['armures legeres'],
        'armes': ['armes courantes', 'arbalete de poing', 'epee courte', 'epee longue', 'rapiere'],
        'outils': ['trois instruments de musique au choix'],
        'competences_choix': 3,
        'competences_liste': ['toutes'],
        'incantation': True,
    },
    'clerc': {
        'des_de_vie': 'd8',
        'pv_niveau_1': '8 + Con',
        'pv_niveaux_suivants': '1d8 (ou 5) + Con',
        'sauvegardes': ['Sagesse', 'Charisme'],
        'armures': ['armures legeres', 'armures intermediaires', 'boucliers'],
        'armes': ['armes courantes'],
        'outils': [],
        'competences_choix': 2,
        'competences_liste': ['Histoire', 'Intuition', 'Medecine', 'Persuasion', 'Religion'],
        'incantation': True,
    },
    'druide': {
        'des_de_vie': 'd8',
        'pv_niveau_1': '8 + Con',
        'pv_niveaux_suivants': '1d8 (ou 5) + Con',
        'sauvegardes': ['Intelligence', 'Sagesse'],
        'armures': ['armures legeres', 'armures intermediaires', 'boucliers (non metalliques)'],
        'armes': ['gourdin', 'dague', 'flechette', 'javeline', 'masse', 'baton', 'cimeterre', 'fronde'],
        'outils': ['kit d\'herboriste'],
        'competences_choix': 2,
        'competences_liste': ['Arcanes', 'Dressage', 'Intuition', 'Medecine', 'Nature', 'Perception', 'Religion', 'Survie'],
        'incantation': True,
    },
    'ensorceleur': {
        'des_de_vie': 'd6',
        'pv_niveau_1': '6 + Con',
        'pv_niveaux_suivants': '1d6 (ou 4) + Con',
        'sauvegardes': ['Constitution', 'Charisme'],
        'armures': [],
        'armes': ['dague', 'flechette', 'fronde', 'baton', 'arbalete legere'],
        'outils': [],
        'competences_choix': 2,
        'competences_liste': ['Arcanes', 'Intimidation', 'Intuition', 'Persuasion', 'Religion', 'Tromperie'],
        'incantation': True,
    },
    'guerrier': {
        'des_de_vie': 'd10',
        'pv_niveau_1': '10 + Con',
        'pv_niveaux_suivants': '1d10 (ou 6) + Con',
        'sauvegardes': ['Force', 'Constitution'],
        'armures': ['toutes les armures', 'boucliers'],
        'armes': ['armes courantes', 'armes de guerre'],
        'outils': [],
        'competences_choix': 2,
        'competences_liste': ['Acrobaties', 'Athletisme', 'Dressage', 'Histoire', 'Intimidation', 'Intuition', 'Perception', 'Survie'],
    },
    'magicien': {
        'des_de_vie': 'd6',
        'pv_niveau_1': '6 + Con',
        'pv_niveaux_suivants': '1d6 (ou 4) + Con',
        'sauvegardes': ['Intelligence', 'Sagesse'],
        'armures': [],
        'armes': ['dague', 'flechette', 'fronde', 'baton', 'arbalete legere'],
        'outils': [],
        'competences_choix': 2,
        'competences_liste': ['Arcanes', 'Histoire', 'Intuition', 'Investigation', 'Medecine', 'Religion'],
        'incantation': True,
    },
    'moine': {
        'des_de_vie': 'd8',
        'pv_niveau_1': '8 + Con',
        'pv_niveaux_suivants': '1d8 (ou 5) + Con',
        'sauvegardes': ['Force', 'Dexterite'],
        'armures': [],
        'armes': ['armes courantes', 'epee courte'],
        'outils': ['un type d\'outil d\'artisan ou un instrument de musique'],
        'competences_choix': 2,
        'competences_liste': ['Acrobaties', 'Athletisme', 'Discretion', 'Histoire', 'Intuition', 'Religion'],
    },
    'occultiste': {
        'des_de_vie': 'd8',
        'pv_niveau_1': '8 + Con',
        'pv_niveaux_suivants': '1d8 (ou 5) + Con',
        'sauvegardes': ['Sagesse', 'Charisme'],
        'armures': ['armures legeres'],
        'armes': ['armes courantes'],
        'outils': [],
        'competences_choix': 2,
        'competences_liste': ['Arcanes', 'Histoire', 'Intimidation', 'Investigation', 'Nature', 'Religion', 'Tromperie'],
        'incantation': True,
    },
    'paladin': {
        'des_de_vie': 'd10',
        'pv_niveau_1': '10 + Con',
        'pv_niveaux_suivants': '1d10 (ou 6) + Con',
        'sauvegardes': ['Sagesse', 'Charisme'],
        'armures': ['toutes les armures', 'boucliers'],
        'armes': ['armes courantes', 'armes de guerre'],
        'outils': [],
        'competences_choix': 2,
        'competences_liste': ['Athletisme', 'Intimidation', 'Intuition', 'Medecine', 'Persuasion', 'Religion'],
        'incantation': True,
    },
    'rodeur': {
        'des_de_vie': 'd10',
        'pv_niveau_1': '10 + Con',
        'pv_niveaux_suivants': '1d10 (ou 6) + Con',
        'sauvegardes': ['Force', 'Dexterite'],
        'armures': ['armures legeres', 'armures intermediaires', 'boucliers'],
        'armes': ['armes courantes', 'armes de guerre'],
        'outils': [],
        'competences_choix': 3,
        'competences_liste': ['Athletisme', 'Discretion', 'Dressage', 'Intuition', 'Investigation', 'Nature', 'Perception', 'Survie'],
        'incantation': True,
    },
    'roublard': {
        'des_de_vie': 'd8',
        'pv_niveau_1': '8 + Con',
        'pv_niveaux_suivants': '1d8 (ou 5) + Con',
        'sauvegardes': ['Dexterite', 'Intelligence'],
        'armures': ['armures legeres'],
        'armes': ['armes courantes', 'arbalete de poing', 'epee courte', 'epee longue', 'rapiere'],
        'outils': ['outils de voleur'],
        'competences_choix': 4,
        'competences_liste': ['Acrobaties', 'Athletisme', 'Discretion', 'Escamotage', 'Intimidation', 'Intuition', 'Investigation', 'Perception', 'Persuasion', 'Representation', 'Tromperie'],
    },
}


def clean_text(text):
    """Nettoie le texte en supprimant les espaces superflus."""
    if not text:
        return ""
    return ' '.join(text.split())


def parse_class_page(slug):
    """Parse une page de classe et extrait les donnees complementaires."""
    url = f"{BASE_URL}/regles/classes/{slug}/"

    try:
        response = requests.get(url, headers=HEADERS)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        data = {
            'name': '',
            'description': '',
            'capacites': [],
            'archetypes': [],
            'source': "Player's Handbook"
        }

        # Trouver le contenu principal
        content = soup.find('div', class_='col1') or soup.find('article') or soup.find('main')
        if not content:
            content = soup

        # Nom de la classe (h1)
        h1 = content.find('h1')
        if h1:
            data['name'] = h1.text.strip()

        # Description (premier paragraphe)
        first_p = content.find('p')
        if first_p:
            data['description'] = clean_text(first_p.get_text())[:500]

        # Chercher les capacites de classe
        capacites = []
        for h3 in content.find_all(['h3', 'h4']):
            cap_name = h3.get_text().strip()

            # Ignorer certains titres
            if any(skip in cap_name.lower() for skip in ['equipement', 'creation', 'multiclass', 'table']):
                continue

            # Trouver la description
            desc = ''
            next_elem = h3.next_sibling
            while next_elem:
                if hasattr(next_elem, 'name') and next_elem.name in ['h2', 'h3', 'h4']:
                    break
                if hasattr(next_elem, 'get_text'):
                    desc += next_elem.get_text() + ' '
                next_elem = next_elem.next_sibling

            desc = clean_text(desc)[:300]
            if cap_name and desc:
                capacites.append({
                    'name': cap_name,
                    'description': desc
                })

        data['capacites'] = capacites[:15]

        # Chercher les archetypes/voies (h2 avec certains mots cles)
        archetypes = []
        for h2 in content.find_all('h2'):
            h2_text = h2.get_text().strip()

            # Detecter les titres d'archetypes
            if any(kw in h2_text.lower() for kw in ['voie', 'archetype', 'college', 'domaine', 'cercle', 'origine', 'ecole', 'tradition', 'serment', 'patron']):
                # C'est un titre de section d'archetypes, chercher les sous-sections
                pass
            elif len(h2_text) > 3 and len(h2_text) < 50:
                # Pourrait etre un archetype
                desc = ''
                next_elem = h2.next_sibling
                while next_elem:
                    if hasattr(next_elem, 'name') and next_elem.name == 'h2':
                        break
                    if hasattr(next_elem, 'get_text'):
                        desc += next_elem.get_text() + ' '
                    next_elem = next_elem.next_sibling

                desc = clean_text(desc)[:200]
                if desc and not any(skip in h2_text.lower() for skip in ['aptitude', 'capacite', 'creation', 'equipement', 'multiclass']):
                    archetypes.append({
                        'name': h2_text,
                        'description': desc
                    })

        data['archetypes'] = archetypes[:10]

        # Source
        source_div = content.find('div', class_='source')
        if source_div:
            data['source'] = source_div.get_text().strip()

        return data

    except Exception as e:
        print(f"  Erreur lors du parsing de {slug}: {e}")
        import traceback
        traceback.print_exc()
        return None


def escape_yaml_string(s):
    """Echappe une chaine pour YAML."""
    if not s:
        return '""'
    s = str(s)
    if any(c in s for c in [':', '"', "'", '\n', '#', '[', ']', '{', '}']):
        s = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{s}"'
    return s


def generate_yaml_block(name, slug, class_info, scraped_data):
    """Genere un bloc YAML dnd-classe a partir des donnees."""
    lines = ['```dnd-classe']

    # Nom
    lines.append(f'name: {escape_yaml_string(name)}')

    # Des de vie
    lines.append(f'des_de_vie: {class_info["des_de_vie"]}')
    lines.append(f'pv_niveau_1: {escape_yaml_string(class_info["pv_niveau_1"])}')
    lines.append(f'pv_niveaux_suivants: {escape_yaml_string(class_info["pv_niveaux_suivants"])}')

    # Maitrises
    lines.append('maitrises:')

    # Armures
    if class_info.get('armures'):
        lines.append('  armures:')
        for armure in class_info['armures']:
            lines.append(f'    - {escape_yaml_string(armure)}')
    else:
        lines.append('  armures: []')

    # Armes
    if class_info.get('armes'):
        lines.append('  armes:')
        for arme in class_info['armes']:
            lines.append(f'    - {escape_yaml_string(arme)}')
    else:
        lines.append('  armes: []')

    # Outils
    if class_info.get('outils'):
        lines.append('  outils:')
        for outil in class_info['outils']:
            lines.append(f'    - {escape_yaml_string(outil)}')
    else:
        lines.append('  outils: []')

    # Sauvegardes
    lines.append('  sauvegardes:')
    for save in class_info['sauvegardes']:
        lines.append(f'    - {escape_yaml_string(save)}')

    # Competences
    lines.append('  competences:')
    lines.append(f'    choix: {class_info["competences_choix"]}')
    lines.append('    liste:')
    for comp in class_info['competences_liste']:
        lines.append(f'      - {escape_yaml_string(comp)}')

    # Incantation
    if class_info.get('incantation'):
        lines.append('incantation: true')

    # Capacites de classe (depuis le scraping)
    if scraped_data and scraped_data.get('capacites'):
        lines.append('capacites:')
        for cap in scraped_data['capacites'][:10]:
            lines.append(f'  - name: {escape_yaml_string(cap["name"])}')
            lines.append(f'    description: {escape_yaml_string(cap["description"])}')

    # Archetypes (depuis le scraping)
    if scraped_data and scraped_data.get('archetypes'):
        lines.append('archetypes:')
        for arch in scraped_data['archetypes']:
            lines.append(f'  - name: {escape_yaml_string(arch["name"])}')
            lines.append(f'    description: {escape_yaml_string(arch["description"])}')

    # Source
    source = scraped_data.get('source', "Player's Handbook") if scraped_data else "Player's Handbook"
    lines.append(f'source: {escape_yaml_string(source)}')

    lines.append('```')
    return '\n'.join(lines)


def generate_markdown_file(name, slug, en_name, class_info, scraped_data):
    """Genere un fichier Markdown complet pour une classe."""
    yaml_block = generate_yaml_block(name, slug, class_info, scraped_data)

    description = ''
    if scraped_data and scraped_data.get('description'):
        description = f"\n{scraped_data['description']}\n"

    content = f"""---
aliases:
  - {name}
  - {name.lower()}
  - {en_name}
tags:
  - classe
  - creation-personnage
---

# {name}
{description}
{yaml_block}
"""

    return content


def sanitize_filename(name):
    """Nettoie un nom pour en faire un nom de fichier valide."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '-')
    return name.strip()


def main():
    """Fonction principale d'importation."""
    print("=== Importation des classes AideDD ===\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    errors = []
    success_count = 0
    skipped_count = 0

    print(f"Importation de {len(CLASSES)} classes...\n")

    for i, cls in enumerate(CLASSES, 1):
        slug = cls['slug']
        name = cls['name']
        en_name = cls['en']

        print(f"[{i}/{len(CLASSES)}] {name}...", end=" ", flush=True)

        filename = sanitize_filename(name) + ".md"
        filepath = OUTPUT_DIR / filename

        # Ne pas ecraser le fichier Inquisiteur existant (homebrew)
        if filepath.exists() and name != 'Inquisiteur':
            print("(existe deja)")
            skipped_count += 1
            continue

        # Recuperer les donnees de base
        class_info = CLASS_DATA.get(slug)
        if not class_info:
            print("ERREUR: donnees de base manquantes")
            errors.append((name, "Donnees de base manquantes"))
            continue

        # Scraper les donnees complementaires
        scraped_data = parse_class_page(slug)

        if scraped_data:
            content = generate_markdown_file(name, slug, en_name, class_info, scraped_data)

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                caps = len(scraped_data.get('capacites', []))
                archs = len(scraped_data.get('archetypes', []))
                print(f"OK ({caps} capacites, {archs} archetypes)")
                success_count += 1
            except Exception as e:
                print(f"ERREUR ecriture: {e}")
                errors.append((name, str(e)))
        else:
            # Utiliser les donnees de base meme sans scraping
            content = generate_markdown_file(name, slug, en_name, class_info, None)
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("OK (donnees de base uniquement)")
                success_count += 1
            except Exception as e:
                print(f"ERREUR ecriture: {e}")
                errors.append((name, str(e)))

        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\n=== Resume ===")
    print(f"Classes importees: {success_count}")
    print(f"Classes ignorees (existantes): {skipped_count}")
    print(f"Erreurs: {len(errors)}")

    if errors:
        print(f"\nListe des erreurs:")
        for name, error in errors:
            print(f"  - {name}: {error}")


if __name__ == "__main__":
    main()
