#!/usr/bin/env python3
"""Test de parsing d'un seul monstre pour valider la structure HTML."""

import requests
from bs4 import BeautifulSoup
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
}

def test_monster(slug="aboleth"):
    """Parse un monstre et affiche la structure HTML."""
    url = f"https://www.aidedd.org/dnd/monstres.php?vf={slug}"

    print(f"Fetching {url}...")
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver le bloc monstre (col1 contient les stats)
    col1 = soup.find('div', class_='col1')

    if not col1:
        print("col1 non trouve!")
        return

    print("\n=== Structure du monstre ===\n")

    # Nom (dans div.jaune ou h1)
    jaune = col1.find('div', class_='jaune')
    orange = col1.find('div', class_='orange')
    print(f"Nom (jaune): {jaune.text.strip() if jaune else 'Non trouve'}")
    print(f"Nom VO (orange): {orange.text.strip() if orange else 'Non trouve'}")

    # Type/taille/alignement
    type_div = col1.find('div', class_='type')
    print(f"Type: {type_div.text.strip() if type_div else 'Non trouve'}")

    # Section rouge (stats combat)
    red_div = col1.find('div', class_='red')
    if red_div:
        print(f"\nStats combat (red):")
        # Chercher les divs internes
        for line in red_div.stripped_strings:
            print(f"  - {line}")

    # Table des caracteristiques
    carac_divs = col1.find_all('div', class_='carac')
    if carac_divs:
        print(f"\nCaracteristiques ({len(carac_divs)} divs):")
        for div in carac_divs:
            print(f"  {div.text.strip()}")

    # Sections rub (Skills, Immunites, Sens, etc.)
    rub_divs = col1.find_all('div', class_='rub')
    if rub_divs:
        print(f"\nRubriques ({len(rub_divs)}):")
        for div in rub_divs:
            text = div.text.strip()[:100]
            print(f"  - {text}...")

    # Description (traits, actions)
    desc_div = col1.find('div', class_='description')
    if desc_div:
        print(f"\nDescription:")
        # Chercher les titres h3
        for h3 in desc_div.find_all('h3'):
            print(f"  [H3] {h3.text}")

        # Chercher les capacites (em/strong)
        print(f"\n  Capacites/Traits:")
        for p in desc_div.find_all('p'):
            em = p.find('em')
            strong = p.find('strong')
            if em:
                print(f"    - {em.text}: {p.text[:80]}...")
            elif strong:
                print(f"    - {strong.text}: {p.text[:80]}...")

    # Source
    source_div = col1.find('div', class_='source')
    print(f"\nSource: {source_div.text.strip() if source_div else 'Non trouve'}")

    # Afficher HTML extrait pour debug
    print("\n=== HTML col1 (extrait 4000 chars) ===\n")
    print(str(col1)[:4000])


if __name__ == "__main__":
    import sys
    slug = sys.argv[1] if len(sys.argv) > 1 else "aboleth"
    test_monster(slug)
