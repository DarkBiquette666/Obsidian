#!/usr/bin/env python3
"""
Script d'importation des monstres depuis aidedd.org vers le vault Obsidian.
Genere des fichiers Markdown avec des blocs dnd-monstre en YAML.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from pathlib import Path

# Configuration
BASE_URL = "https://www.aidedd.org"
MONSTERS_LIST_URL = f"{BASE_URL}/dnd-filters/monstres.php"
MONSTER_DETAIL_URL = f"{BASE_URL}/dnd/monstres.php?vf="
OUTPUT_DIR = Path(r"y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\Glossary\Bestiaire")
DELAY_BETWEEN_REQUESTS = 0.3  # Respecter le serveur

# Headers pour les requetes
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
}


def get_monster_list():
    """Recupere la liste de tous les monstres depuis la page de filtres."""
    print("Recuperation de la liste des monstres...")

    response = requests.get(MONSTERS_LIST_URL, headers=HEADERS)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    monsters = []

    # Trouver la table des monstres
    table = soup.find('table', {'id': 'liste'})
    if not table:
        print("Table des monstres non trouvee!")
        return monsters

    rows = table.find_all('tr')[1:]  # Skip header row

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            # Le lien est dans la cellule 1 (index 1), pas la cellule 0 (checkbox)
            link = cells[1].find('a')
            if link:
                name_vf = link.text.strip()
                href = link.get('href', '')

                if 'vf=' in href:
                    slug = href.split('vf=')[-1]
                else:
                    slug = name_vf.lower().replace(' ', '-').replace(',', '').replace("'", '-')

                monsters.append({
                    'name_vf': name_vf,
                    'slug': slug
                })

    print(f"Trouve {len(monsters)} monstres")
    return monsters


def parse_ability_score(text):
    """Parse une valeur de caracteristique comme '21 (+5)' et retourne le score."""
    match = re.search(r'(\d+)', text)
    return int(match.group(1)) if match else 10


def clean_text(text):
    """Nettoie le texte en supprimant les espaces superflus."""
    if not text:
        return ""
    return ' '.join(text.split())


def parse_monster_page(slug):
    """Parse une page de monstre et extrait toutes les donnees."""
    url = f"{MONSTER_DETAIL_URL}{slug}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        # Conteneur principal du monstre (div.col1)
        col1 = soup.find('div', class_='col1')
        if not col1:
            print(f"  col1 non trouve pour {slug}")
            return None

        data = {}

        # Nom (dans h1)
        h1 = col1.find('h1')
        data['name'] = h1.text.strip() if h1 else slug.replace('-', ' ').title()

        # Type/taille/alignement (dans div.type)
        type_div = col1.find('div', class_='type')
        if type_div:
            type_text = type_div.text.strip()
            parts = type_text.split(',')
            if len(parts) >= 1:
                type_size = parts[0].strip()
                size_match = re.search(r'taille\s+(TP|P|M|G|TG|Gig)', type_size, re.IGNORECASE)
                if size_match:
                    size_map = {
                        'TP': 'Tres petit', 'P': 'Petit', 'M': 'Moyen',
                        'G': 'Grand', 'TG': 'Tres grand', 'Gig': 'Gigantesque'
                    }
                    data['taille'] = size_map.get(size_match.group(1).upper(), size_match.group(1))

                type_match = re.match(r'^([A-Za-zéèêëàâäùûüîïôö\-]+)', type_size)
                if type_match:
                    data['type'] = type_match.group(1).capitalize()

            if len(parts) >= 2:
                data['alignement'] = parts[1].strip()

        # Section rouge (stats combat et proprietes)
        red_div = col1.find('div', class_='red')
        if red_div:
            red_html = str(red_div)

            # CA
            ca_match = re.search(r'Classe d.armure</strong>\s*([^<]+)', red_html)
            if ca_match:
                data['ca'] = ca_match.group(1).strip()

            # PV
            pv_match = re.search(r'Points de vie</strong>\s*([^<]+)', red_html)
            if pv_match:
                data['pv'] = pv_match.group(1).strip()

            # Vitesse
            vitesse_match = re.search(r'Vitesse</strong>\s*([^<]+)', red_html)
            if vitesse_match:
                data['vitesse'] = vitesse_match.group(1).strip()

            # Jets de sauvegarde
            save_match = re.search(r'Jets de sauvegarde</strong>\s*([^<]+)', red_html)
            if save_match:
                data['sauvegardes'] = save_match.group(1).strip()

            # Competences
            skills_match = re.search(r'Comp.tences</strong>\s*([^<]+)', red_html)
            if skills_match:
                skills_text = skills_match.group(1).strip()
                data['competences'] = [s.strip() for s in skills_text.split(',')]

            # Immunites aux degats
            imm_match = re.search(r'Immunit.s? aux d.g.ts</strong>\s*([^<]+)', red_html)
            if imm_match:
                imm_text = imm_match.group(1).strip()
                data['immunites'] = [i.strip() for i in imm_text.split(',')]

            # Resistances aux degats
            res_match = re.search(r'R.sistances? aux d.g.ts</strong>\s*([^<]+)', red_html)
            if res_match:
                res_text = res_match.group(1).strip()
                data['resistances'] = [r.strip() for r in res_text.split(',')]

            # Vulnerabilites aux degats
            vul_match = re.search(r'Vuln.rabilit.s? aux d.g.ts</strong>\s*([^<]+)', red_html)
            if vul_match:
                vul_text = vul_match.group(1).strip()
                data['vulnerabilites'] = [v.strip() for v in vul_text.split(',')]

            # Immunites aux etats
            imm_etat_match = re.search(r'Immunit.s? aux .tats</strong>\s*([^<]+)', red_html)
            if imm_etat_match:
                data['immunites_etats'] = imm_etat_match.group(1).strip()

            # Sens
            sens_match = re.search(r'Sens</strong>\s*([^<]+)', red_html)
            if sens_match:
                data['sens'] = sens_match.group(1).strip()

            # Langues
            langues_match = re.search(r'Langues</strong>\s*([^<]+)', red_html)
            if langues_match:
                data['langues'] = langues_match.group(1).strip()

            # Puissance (FP)
            fp_match = re.search(r'Puissance</strong>\s*([^<]+)', red_html)
            if fp_match:
                data['facteur_puissance'] = fp_match.group(1).strip()

        # Caracteristiques (6 divs avec class="carac")
        carac_divs = col1.find_all('div', class_='carac')
        if len(carac_divs) >= 6:
            stat_names = ['for', 'dex', 'con', 'int', 'sag', 'cha']
            for i, div in enumerate(carac_divs[:6]):
                data[stat_names[i]] = parse_ability_score(div.text)

        # Collecter tous les paragraphes <p> avec <strong><em>
        all_paragraphs = col1.find_all('p')
        rub_divs = col1.find_all('div', class_='rub')

        # Creer une liste ordonnee de tous les elements (p et rub)
        # pour determiner les sections
        traits = []
        actions = []
        reactions = []
        legendaires = []

        current_section = 'traits'

        # Trouver les positions des rubriques
        rub_positions = {}
        for rub in rub_divs:
            rub_text = rub.text.strip().lower()
            if 'légendaires' in rub_text or 'legendaires' in rub_text:
                rub_positions[rub] = 'legendaires'
            elif 'réactions' in rub_text or 'reactions' in rub_text:
                rub_positions[rub] = 'reactions'
            elif 'actions' in rub_text:
                rub_positions[rub] = 'actions'

        for p in all_paragraphs:
            # Determiner la section actuelle en verifiant les rubriques precedentes
            for rub in rub_divs:
                # Verifier si ce rub est avant le paragraphe courant dans le DOM
                if rub in rub_positions:
                    # Comparer positions
                    rub_pos = str(col1).find(str(rub))
                    p_pos = str(col1).find(str(p))
                    if rub_pos < p_pos:
                        current_section = rub_positions[rub]

            # Extraire le nom et la description
            strong = p.find('strong')
            if not strong:
                continue

            em = strong.find('em')
            if em:
                name = em.text.strip().rstrip('.')
            else:
                name = strong.text.strip().rstrip('.')

            # Description = tout le texte du paragraphe moins le nom
            full_text = p.get_text()
            desc = full_text.replace(name, '', 1).strip().lstrip('.')

            if not name or not desc:
                continue

            entry = {
                'name': name,
                'description': clean_text(desc)
            }

            if current_section == 'traits':
                traits.append(entry)
            elif current_section == 'actions':
                attack_match = re.search(r'([+-]\d+)\s*au toucher', desc)
                if attack_match:
                    entry['attaque'] = attack_match.group(1) + ' au toucher'
                actions.append(entry)
            elif current_section == 'reactions':
                reactions.append(entry)
            elif current_section == 'legendaires':
                legendaires.append(entry)

        data['traits'] = traits
        data['actions'] = actions
        data['reactions'] = reactions
        data['legendaires'] = legendaires

        # Source
        source_div = col1.find('div', class_='source')
        if source_div:
            data['source'] = source_div.text.strip()

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
    """Genere un bloc YAML dnd-monstre a partir des donnees."""
    lines = ['```dnd-monstre']

    simple_fields = [
        ('name', 'name'),
        ('type', 'type'),
        ('taille', 'taille'),
        ('alignement', 'alignement'),
        ('ca', 'ca'),
        ('pv', 'pv'),
        ('vitesse', 'vitesse'),
        ('for', 'for'),
        ('dex', 'dex'),
        ('con', 'con'),
        ('int', 'int'),
        ('sag', 'sag'),
        ('cha', 'cha'),
        ('sauvegardes', 'sauvegardes'),
        ('sens', 'sens'),
        ('langues', 'langues'),
        ('facteur_puissance', 'facteur_puissance'),
        ('immunites_etats', 'immunites_etats'),
        ('source', 'source'),
    ]

    for yaml_key, data_key in simple_fields:
        if data_key in data and data[data_key]:
            value = data[data_key]
            if isinstance(value, int):
                lines.append(f'{yaml_key}: {value}')
            else:
                lines.append(f'{yaml_key}: {escape_yaml_string(str(value))}')

    list_fields = ['competences', 'immunites', 'resistances', 'vulnerabilites']
    for field in list_fields:
        if field in data and data[field]:
            lines.append(f'{field}:')
            for item in data[field]:
                lines.append(f'  - {escape_yaml_string(item)}')

    if data.get('traits'):
        lines.append('traits:')
        for trait in data['traits']:
            lines.append(f'  - name: {escape_yaml_string(trait["name"])}')
            lines.append(f'    description: {escape_yaml_string(trait["description"])}')

    if data.get('actions'):
        lines.append('actions:')
        for action in data['actions']:
            lines.append(f'  - name: {escape_yaml_string(action["name"])}')
            lines.append(f'    description: {escape_yaml_string(action["description"])}')
            if 'attaque' in action:
                lines.append(f'    attaque: {escape_yaml_string(action["attaque"])}')

    if data.get('reactions'):
        lines.append('reactions:')
        for reaction in data['reactions']:
            lines.append(f'  - name: {escape_yaml_string(reaction["name"])}')
            lines.append(f'    description: {escape_yaml_string(reaction["description"])}')

    if data.get('legendaires'):
        lines.append('legendaires:')
        for legendary in data['legendaires']:
            lines.append(f'  - name: {escape_yaml_string(legendary["name"])}')
            lines.append(f'    description: {escape_yaml_string(legendary["description"])}')

    lines.append('```')
    return '\n'.join(lines)


def generate_markdown_file(data, slug):
    """Genere un fichier Markdown complet pour un monstre."""
    yaml_block = generate_yaml_block(data)

    name = data.get('name', slug)
    monster_type = data.get('type', 'Creature')
    fp = data.get('facteur_puissance', 'Inconnu')

    content = f"""---
aliases:
  - {name}
tags:
  - monstre
  - bestiaire
type: {monster_type}
facteur_puissance: "{fp}"
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
    print("=== Importation des monstres AideDD ===\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    monsters = get_monster_list()

    if not monsters:
        print("Aucun monstre trouve. Verifiez la connexion.")
        return

    errors = []
    success_count = 0
    skipped_count = 0

    print(f"\nImportation de {len(monsters)} monstres...\n")

    for i, monster in enumerate(monsters, 1):
        slug = monster['slug']
        name = monster['name_vf']

        print(f"[{i}/{len(monsters)}] {name}...", end=" ", flush=True)

        filename = sanitize_filename(name) + ".md"
        filepath = OUTPUT_DIR / filename

        if filepath.exists():
            print("(existe deja)")
            skipped_count += 1
            continue

        data = parse_monster_page(slug)

        if data:
            content = generate_markdown_file(data, slug)

            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("OK")
                success_count += 1
            except Exception as e:
                print(f"ERREUR ecriture: {e}")
                errors.append((name, str(e)))
        else:
            print("ERREUR parsing")
            errors.append((name, "Parsing echoue"))

        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\n=== Resume ===")
    print(f"Monstres importes: {success_count}")
    print(f"Monstres ignores (existants): {skipped_count}")
    print(f"Erreurs: {len(errors)}")

    if errors:
        print(f"\nListe des erreurs:")
        for name, error in errors[:20]:
            print(f"  - {name}: {error}")
        if len(errors) > 20:
            print(f"  ... et {len(errors) - 20} autres erreurs")


if __name__ == "__main__":
    main()
