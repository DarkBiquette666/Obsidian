#!/usr/bin/env python3
"""
Convertisseur de stat blocks Markdown vers YAML dnd-monstre.
Supporte plusieurs formats d'entree:
- Format aidedd.org
- Format Homebrewery/GM Binder
- Format texte simple

Usage:
    python convert_md_to_yaml.py input.md
    python convert_md_to_yaml.py --text "Gobelin\nHumanoide de taille P..."
    python convert_md_to_yaml.py --interactive
"""

import re
import sys
import argparse
from pathlib import Path


def parse_stat_block(text):
    """Parse un stat block en texte et extrait les donnees."""
    data = {}

    # Normaliser les sauts de ligne
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    if not lines:
        return None

    # Premiere ligne = nom (peut etre avec # ou sans)
    name_line = lines[0]
    data['name'] = re.sub(r'^#+\s*', '', name_line).strip()

    # Type, taille, alignement (ligne en italique ou avec format standard)
    for line in lines[1:5]:
        # Format: "Humanoide de taille M, neutre" ou "_Humanoide de taille M, neutre_"
        clean_line = re.sub(r'^[_*]+|[_*]+$', '', line).strip()

        if 'taille' in clean_line.lower():
            parts = clean_line.split(',')
            if len(parts) >= 1:
                type_size = parts[0].strip()

                # Extraire taille
                size_match = re.search(r'taille\s+(TP|P|M|G|TG|Gig)', type_size, re.IGNORECASE)
                if size_match:
                    size_map = {
                        'TP': 'Tres petit', 'P': 'Petit', 'M': 'Moyen',
                        'G': 'Grand', 'TG': 'Tres grand', 'Gig': 'Gigantesque'
                    }
                    data['taille'] = size_map.get(size_match.group(1).upper(), size_match.group(1))

                # Extraire type
                type_match = re.match(r'^([A-Za-zéèêëàâäùûüîïôö\-]+)', type_size)
                if type_match:
                    data['type'] = type_match.group(1).capitalize()

            if len(parts) >= 2:
                data['alignement'] = parts[1].strip()
            break

    # Rejoindre tout le texte pour les patterns
    full_text = '\n'.join(lines)

    # Classe d'armure
    ca_match = re.search(r'\*?\*?Classe d.armure\*?\*?\s*[:\s]*(\d+[^*\n]*)', full_text, re.IGNORECASE)
    if ca_match:
        data['ca'] = ca_match.group(1).strip()

    # Points de vie
    pv_match = re.search(r'\*?\*?Points de vie\*?\*?\s*[:\s]*(\d+[^*\n]*)', full_text, re.IGNORECASE)
    if pv_match:
        data['pv'] = pv_match.group(1).strip()

    # Vitesse
    vitesse_match = re.search(r'\*?\*?Vitesse\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if vitesse_match:
        data['vitesse'] = vitesse_match.group(1).strip()

    # Caracteristiques (format table ou inline)
    # Format: FOR 10 (+0) DEX 14 (+2) ...
    # ou: | FOR | DEX | CON | INT | SAG | CHA |
    stats_pattern = r'FOR[:\s]*(\d+)[^A-Z]*DEX[:\s]*(\d+)[^A-Z]*CON[:\s]*(\d+)[^A-Z]*INT[:\s]*(\d+)[^A-Z]*SAG[:\s]*(\d+)[^A-Z]*CHA[:\s]*(\d+)'
    stats_match = re.search(stats_pattern, full_text, re.IGNORECASE)
    if stats_match:
        data['for'] = int(stats_match.group(1))
        data['dex'] = int(stats_match.group(2))
        data['con'] = int(stats_match.group(3))
        data['int'] = int(stats_match.group(4))
        data['sag'] = int(stats_match.group(5))
        data['cha'] = int(stats_match.group(6))

    # Jets de sauvegarde
    save_match = re.search(r'\*?\*?Jets? de sauvegarde\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if save_match:
        data['sauvegardes'] = save_match.group(1).strip()

    # Competences
    skills_match = re.search(r'\*?\*?Comp[ée]tences?\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if skills_match:
        skills_text = skills_match.group(1).strip()
        data['competences'] = [s.strip() for s in skills_text.split(',')]

    # Immunites aux degats
    imm_match = re.search(r'\*?\*?Immunit[ée]s? aux d[ée]g[aâ]ts\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if imm_match:
        imm_text = imm_match.group(1).strip()
        data['immunites'] = [i.strip() for i in imm_text.split(',')]

    # Resistances aux degats
    res_match = re.search(r'\*?\*?R[ée]sistances? aux d[ée]g[aâ]ts\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if res_match:
        res_text = res_match.group(1).strip()
        data['resistances'] = [r.strip() for r in res_text.split(',')]

    # Vulnerabilites aux degats
    vul_match = re.search(r'\*?\*?Vuln[ée]rabilit[ée]s? aux d[ée]g[aâ]ts\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if vul_match:
        vul_text = vul_match.group(1).strip()
        data['vulnerabilites'] = [v.strip() for v in vul_text.split(',')]

    # Immunites aux etats
    imm_etat_match = re.search(r'\*?\*?Immunit[ée]s? aux [ée]tats\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if imm_etat_match:
        data['immunites_etats'] = imm_etat_match.group(1).strip()

    # Sens
    sens_match = re.search(r'\*?\*?Sens\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if sens_match:
        data['sens'] = sens_match.group(1).strip()

    # Langues
    langues_match = re.search(r'\*?\*?Langues?\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if langues_match:
        data['langues'] = langues_match.group(1).strip()

    # Puissance / Facteur de puissance
    fp_match = re.search(r'\*?\*?(?:Puissance|Facteur de puissance|FP)\*?\*?\s*[:\s]*([^*\n]+)', full_text, re.IGNORECASE)
    if fp_match:
        data['facteur_puissance'] = fp_match.group(1).strip()

    # Traits, Actions, Reactions, Legendaires
    # Format: ***Nom du trait.*** Description...
    # ou: **_Nom du trait._** Description...
    # ou: **Nom du trait.** Description...

    data['traits'] = []
    data['actions'] = []
    data['reactions'] = []
    data['legendaires'] = []

    current_section = 'traits'

    # Detecter les sections
    sections = {
        'actions': re.compile(r'^#+\s*Actions?\s*$|^\*?\*?Actions?\*?\*?\s*$', re.IGNORECASE),
        'reactions': re.compile(r'^#+\s*R[ée]actions?\s*$|^\*?\*?R[ée]actions?\*?\*?\s*$', re.IGNORECASE),
        'legendaires': re.compile(r'^#+\s*Actions?\s+l[ée]gendaires?\s*$|^\*?\*?Actions?\s+l[ée]gendaires?\*?\*?\s*$', re.IGNORECASE),
    }

    # Pattern pour les capacites/traits
    ability_pattern = re.compile(r'^\*?\*?\*?_?([^.*_]+)_?\*?\*?\*?\.\s*(.+)$')

    for line in lines:
        # Verifier si c'est un changement de section
        for section_name, section_pattern in sections.items():
            if section_pattern.match(line):
                current_section = section_name
                break
        else:
            # C'est peut-etre un trait/action
            match = ability_pattern.match(line)
            if match:
                name = match.group(1).strip()
                desc = match.group(2).strip()

                # Ignorer les lignes de stats
                if any(x in name.lower() for x in ['classe d', 'points de vie', 'vitesse', 'for', 'dex', 'con', 'int', 'sag', 'cha', 'sens', 'langues', 'puissance', 'competences']):
                    continue

                entry = {
                    'name': name,
                    'description': desc
                }

                if current_section == 'traits':
                    data['traits'].append(entry)
                elif current_section == 'actions':
                    # Extraire attaque si present
                    attack_match = re.search(r'([+-]\d+)\s*au toucher', desc)
                    if attack_match:
                        entry['attaque'] = attack_match.group(1) + ' au toucher'
                    data['actions'].append(entry)
                elif current_section == 'reactions':
                    data['reactions'].append(entry)
                elif current_section == 'legendaires':
                    data['legendaires'].append(entry)

    return data


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


def convert_file(input_path, output_path=None):
    """Convertit un fichier Markdown en YAML dnd-monstre."""
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    data = parse_stat_block(text)

    if not data:
        print("Erreur: Impossible de parser le stat block")
        return False

    yaml_block = generate_yaml_block(data)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(yaml_block)
        print(f"Fichier genere: {output_path}")
    else:
        print(yaml_block)

    return True


def interactive_mode():
    """Mode interactif: l'utilisateur colle le texte."""
    print("=== Convertisseur Markdown vers YAML dnd-monstre ===")
    print("Collez votre stat block (terminez par une ligne vide puis Ctrl+D ou Ctrl+Z):")
    print()

    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    text = '\n'.join(lines)

    if not text.strip():
        print("Aucun texte fourni.")
        return

    data = parse_stat_block(text)

    if not data:
        print("Erreur: Impossible de parser le stat block")
        return

    print("\n=== YAML genere ===\n")
    print(generate_yaml_block(data))


def main():
    parser = argparse.ArgumentParser(description='Convertit un stat block Markdown en YAML dnd-monstre')
    parser.add_argument('input', nargs='?', help='Fichier Markdown a convertir')
    parser.add_argument('-o', '--output', help='Fichier de sortie (optionnel)')
    parser.add_argument('-t', '--text', help='Texte a convertir directement')
    parser.add_argument('-i', '--interactive', action='store_true', help='Mode interactif')

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.text:
        data = parse_stat_block(args.text)
        if data:
            print(generate_yaml_block(data))
        else:
            print("Erreur: Impossible de parser le texte")
    elif args.input:
        convert_file(args.input, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
