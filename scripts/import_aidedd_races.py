#!/usr/bin/env python3
"""
Script d'importation des races depuis aidedd.org vers le vault Obsidian.
Genere des fichiers Markdown avec des blocs dnd-race en YAML.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from pathlib import Path

# Configuration
BASE_URL = "https://www.aidedd.org"
RACES_LIST_URL = f"{BASE_URL}/regles/races/"
OUTPUT_DIR = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Races")
DELAY_BETWEEN_REQUESTS = 0.5

# Headers pour les requetes
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
}

# Liste des races a scraper avec leurs slugs
RACES = [
    {'name': 'Elfe', 'slug': 'elfe'},
    {'name': 'Halfelin', 'slug': 'halfelin'},
    {'name': 'Humain', 'slug': 'humain'},
    {'name': 'Nain', 'slug': 'nain'},
    {'name': 'Demi-elfe', 'slug': 'demi-elfe'},
    {'name': 'Demi-orc', 'slug': 'demi-orc'},
    {'name': 'Drakeide', 'slug': 'drakeide'},
    {'name': 'Gnome', 'slug': 'gnome'},
    {'name': 'Tieffelin', 'slug': 'tieffelin'},
    {'name': 'Aarakocra', 'slug': 'aarakocra'},
    {'name': 'Genasi', 'slug': 'genasi'},
    {'name': 'Gnome des profondeurs', 'slug': 'gnome-des-profondeurs'},
    {'name': 'Goliath', 'slug': 'goliath'},
]


def clean_text(text):
    """Nettoie le texte en supprimant les espaces superflus."""
    if not text:
        return ""
    return ' '.join(text.split())


def parse_ability_increase(text):
    """Parse les augmentations de caracteristiques depuis le texte."""
    increases = {}
    text_lower = text.lower()

    patterns = [
        (r'force[^\d]*\+?\s*(\d+)', 'for'),
        (r'dext[ée]rit[ée][^\d]*\+?\s*(\d+)', 'dex'),
        (r'constitution[^\d]*\+?\s*(\d+)', 'con'),
        (r'intelligence[^\d]*\+?\s*(\d+)', 'int'),
        (r'sagesse[^\d]*\+?\s*(\d+)', 'sag'),
        (r'charisme[^\d]*\+?\s*(\d+)', 'cha'),
    ]

    for pattern, key in patterns:
        match = re.search(pattern, text_lower)
        if match:
            increases[key] = f"+{match.group(1)}"

    return increases


def parse_race_page(slug):
    """Parse une page de race et extrait toutes les donnees."""
    url = f"{BASE_URL}/regles/races/{slug}/"

    try:
        response = requests.get(url, headers=HEADERS)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        data = {
            'name': '',
            'augmentations': {},
            'taille': '',
            'vitesse': '',
            'vision': '',
            'langues': [],
            'traits': [],
            'sous_races': [],
            'source': ''
        }

        # Trouver le contenu principal
        content = soup.find('div', class_='col1') or soup.find('article') or soup.find('main')
        if not content:
            content = soup

        # Nom de la race (h1)
        h1 = content.find('h1')
        if h1:
            data['name'] = h1.text.strip()

        # Trouver toutes les sections
        all_text = content.get_text()

        # Augmentation de caracteristiques
        aug_match = re.search(r'Augmentation de caract[ée]ristiques?[.\s:]*([^.]+\.)', all_text, re.IGNORECASE)
        if aug_match:
            data['augmentations'] = parse_ability_increase(aug_match.group(1))

        # Taille
        taille_match = re.search(r'Taille[.\s:]*([^.]+)', all_text, re.IGNORECASE)
        if taille_match:
            taille_text = taille_match.group(1).strip()
            if 'moyenne' in taille_text.lower() or 'M' in taille_text:
                data['taille'] = 'Moyenne'
            elif 'petite' in taille_text.lower() or 'P' in taille_text:
                data['taille'] = 'Petite'
            else:
                data['taille'] = taille_text[:50]

        # Vitesse
        vitesse_match = re.search(r'Vitesse[.\s:]*(\d+)\s*m[èe]?t?r?e?s?', all_text, re.IGNORECASE)
        if vitesse_match:
            data['vitesse'] = f"{vitesse_match.group(1)} m"

        # Vision dans le noir
        vision_match = re.search(r'Vision dans le noir[.\s:]*(\d+)\s*m[èe]?t?r?e?s?', all_text, re.IGNORECASE)
        if vision_match:
            data['vision'] = f"Vision dans le noir {vision_match.group(1)} m"

        # Langues
        langues_match = re.search(r'Langues?[.\s:]*([^.]+)', all_text, re.IGNORECASE)
        if langues_match:
            langues_text = langues_match.group(1)
            # Extraire les langues
            langues = []
            if 'commun' in langues_text.lower():
                langues.append('Commun')
            if 'elfique' in langues_text.lower() or 'elfe' in langues_text.lower():
                langues.append('Elfique')
            if 'nain' in langues_text.lower():
                langues.append('Nain')
            if 'halfelin' in langues_text.lower():
                langues.append('Halfelin')
            if 'gnome' in langues_text.lower():
                langues.append('Gnome')
            if 'orc' in langues_text.lower():
                langues.append('Orc')
            if 'draconique' in langues_text.lower():
                langues.append('Draconique')
            if 'infernal' in langues_text.lower():
                langues.append('Infernal')
            if 'primordial' in langues_text.lower():
                langues.append('Primordial')
            if 'profond' in langues_text.lower():
                langues.append('Commun des profondeurs')
            if 'celeste' in langues_text.lower():
                langues.append('Celeste')
            if 'auran' in langues_text.lower():
                langues.append('Auran')
            data['langues'] = langues if langues else ['Commun']

        # Traits - chercher les paragraphes avec titres en gras
        traits = []

        # Methode 1: chercher les <strong> ou <b> suivis de texte
        for strong in content.find_all(['strong', 'b']):
            text = strong.get_text().strip()
            # Ignorer les titres de section connus
            if any(skip in text.lower() for skip in ['augmentation', 'taille', 'vitesse', 'vision', 'langue', 'sous-race', 'age', 'alignement']):
                continue

            # Trouver la description qui suit
            next_text = ''
            next_sibling = strong.next_sibling
            while next_sibling:
                if hasattr(next_sibling, 'name') and next_sibling.name in ['strong', 'b', 'h2', 'h3']:
                    break
                if hasattr(next_sibling, 'get_text'):
                    next_text += next_sibling.get_text()
                elif isinstance(next_sibling, str):
                    next_text += next_sibling
                next_sibling = next_sibling.next_sibling

            next_text = clean_text(next_text)
            if text and next_text and len(text) < 50:
                traits.append({
                    'name': text.rstrip('.').rstrip(':'),
                    'description': next_text[:500]
                })

        data['traits'] = traits[:10]  # Limiter a 10 traits

        # Sous-races - chercher les h3 ou h4
        sous_races = []
        for header in content.find_all(['h3', 'h4']):
            header_text = header.get_text().strip()
            # Ignorer si c'est un titre de section standard
            if any(skip in header_text.lower() for skip in ['trait', 'capacit', 'description']):
                continue

            # Collecter le contenu de la sous-race
            sous_race = {
                'name': header_text,
                'augmentations': {},
                'traits': []
            }

            # Parcourir les elements suivants
            next_elem = header.next_sibling
            sous_race_text = ''
            while next_elem:
                if hasattr(next_elem, 'name') and next_elem.name in ['h2', 'h3', 'h4']:
                    break
                if hasattr(next_elem, 'get_text'):
                    sous_race_text += next_elem.get_text() + ' '
                next_elem = next_elem.next_sibling

            # Parser les augmentations de la sous-race
            aug = parse_ability_increase(sous_race_text)
            if aug:
                sous_race['augmentations'] = aug

            if sous_race['name'] and (sous_race['augmentations'] or 'elfe' in header_text.lower() or 'nain' in header_text.lower()):
                sous_races.append(sous_race)

        data['sous_races'] = sous_races

        # Source
        source_div = content.find('div', class_='source')
        if source_div:
            data['source'] = source_div.get_text().strip()
        else:
            data['source'] = "Player's Handbook"

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


def generate_yaml_block(data):
    """Genere un bloc YAML dnd-race a partir des donnees."""
    lines = ['```dnd-race']

    # Nom
    lines.append(f'name: {escape_yaml_string(data["name"])}')

    # Augmentations
    if data['augmentations']:
        lines.append('augmentations:')
        for stat, bonus in data['augmentations'].items():
            lines.append(f'  {stat}: {bonus}')

    # Caracteristiques simples
    if data['taille']:
        lines.append(f'taille: {escape_yaml_string(data["taille"])}')
    if data['vitesse']:
        lines.append(f'vitesse: {escape_yaml_string(data["vitesse"])}')
    if data['vision']:
        lines.append(f'vision: {escape_yaml_string(data["vision"])}')

    # Langues
    if data['langues']:
        lines.append('langues:')
        for langue in data['langues']:
            lines.append(f'  - {escape_yaml_string(langue)}')

    # Traits
    if data['traits']:
        lines.append('traits:')
        for trait in data['traits']:
            lines.append(f'  - name: {escape_yaml_string(trait["name"])}')
            lines.append(f'    description: {escape_yaml_string(trait["description"])}')

    # Sous-races
    if data['sous_races']:
        lines.append('sous_races:')
        for sr in data['sous_races']:
            lines.append(f'  - name: {escape_yaml_string(sr["name"])}')
            if sr.get('augmentations'):
                lines.append('    augmentations:')
                for stat, bonus in sr['augmentations'].items():
                    lines.append(f'      {stat}: {bonus}')
            if sr.get('traits'):
                lines.append('    traits:')
                for trait in sr['traits']:
                    lines.append(f'      - name: {escape_yaml_string(trait["name"])}')
                    lines.append(f'        description: {escape_yaml_string(trait["description"])}')

    # Source
    if data.get('source'):
        lines.append(f'source: {escape_yaml_string(data["source"])}')

    lines.append('```')
    return '\n'.join(lines)


def generate_markdown_file(data):
    """Genere un fichier Markdown complet pour une race."""
    yaml_block = generate_yaml_block(data)

    name = data.get('name', 'Race inconnue')

    # Creer les aliases
    aliases = [name]
    if name != name.lower():
        aliases.append(name.lower())

    content = f"""---
aliases:
  - {name}
  - {name.lower()}
tags:
  - race
  - creation-personnage
---

# {name}

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
    print("=== Importation des races AideDD ===\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    errors = []
    success_count = 0
    skipped_count = 0

    print(f"Importation de {len(RACES)} races...\n")

    for i, race in enumerate(RACES, 1):
        slug = race['slug']
        name = race['name']

        print(f"[{i}/{len(RACES)}] {name}...", end=" ", flush=True)

        filename = sanitize_filename(name) + ".md"
        filepath = OUTPUT_DIR / filename

        if filepath.exists():
            print("(existe deja)")
            skipped_count += 1
            continue

        data = parse_race_page(slug)

        if data:
            # S'assurer que le nom est correct
            if not data['name']:
                data['name'] = name

            content = generate_markdown_file(data)

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"OK ({len(data.get('traits', []))} traits, {len(data.get('sous_races', []))} sous-races)")
                success_count += 1
            except Exception as e:
                print(f"ERREUR ecriture: {e}")
                errors.append((name, str(e)))
        else:
            print("ERREUR parsing")
            errors.append((name, "Parsing echoue"))

        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\n=== Resume ===")
    print(f"Races importees: {success_count}")
    print(f"Races ignorees (existantes): {skipped_count}")
    print(f"Erreurs: {len(errors)}")

    if errors:
        print(f"\nListe des erreurs:")
        for name, error in errors:
            print(f"  - {name}: {error}")


if __name__ == "__main__":
    main()
