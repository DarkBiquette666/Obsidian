#!/usr/bin/env python3
"""Test d'importation d'un seul monstre."""

import sys
sys.path.insert(0, '.')

from import_aidedd_monsters import parse_monster_page, generate_markdown_file

def test_one(slug="aboleth"):
    print(f"Test de parsing pour: {slug}\n")

    data = parse_monster_page(slug)

    if not data:
        print("ERREUR: Parsing echoue!")
        return

    print("=== Donnees extraites ===\n")
    for key, value in data.items():
        if isinstance(value, list) and len(value) > 0:
            print(f"{key}:")
            for item in value[:3]:  # Afficher les 3 premiers
                if isinstance(item, dict):
                    print(f"  - {item.get('name', '?')}: {str(item.get('description', ''))[:60]}...")
                else:
                    print(f"  - {item}")
            if len(value) > 3:
                print(f"  ... et {len(value) - 3} autres")
        else:
            print(f"{key}: {str(value)[:80]}{'...' if len(str(value)) > 80 else ''}")

    print("\n=== Fichier Markdown genere ===\n")
    md_content = generate_markdown_file(data, slug)
    print(md_content[:2000])
    if len(md_content) > 2000:
        print(f"\n... ({len(md_content) - 2000} caracteres supplementaires)")


if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "aboleth"
    test_one(slug)
