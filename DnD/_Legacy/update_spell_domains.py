import os
import re
import glob

def main():
    clerc_file = os.path.join('Glossary', 'Classes', 'Clerc.md')
    if not os.path.exists(clerc_file):
        print("Clerc.md not found")
        return

    with open(clerc_file, 'r', encoding='utf-8') as f:
        clerc_content = f.read()

    # 1. Extraction des domaines et sorts
    # On cherche les sections ### Domaine de ...
    # Et les tableaux de sorts qui suivent
    domain_map = {}
    
    sections = re.split(r'### Domaine de la |### Domaine du |### Domaine de ', clerc_content)
    for section in sections[1:]: # Skip header
        lines = section.split('\n')
        domain_name = lines[0].strip()
        
        # Trouver le tableau Markdown
        # On cherche les lignes qui contiennent des noms de sorts séparés par des virgules
        # entre des barres de tableau |
        spells = []
        table_match = re.findall(r'\| \d+ \| (.*?) \|', section)
        for spell_line in table_match:
            # Séparer par virgule ou slash
            parts = re.split(r',|/', spell_line)
            for p in parts:
                s = p.strip()
                if s and s != "Sorts":
                    spells.append(s)
        
        domain_map[domain_name] = spells
        print(f"Found Domain: {domain_name} with {len(spells)} spells")

    # 2. Mise à jour des fichiers de sorts
    spell_folder = os.path.join('Glossary', 'Liste des Sorts')
    all_spell_files = glob.glob(os.path.join(spell_folder, '*.md'))

    for domain, spells in domain_map.items():
        for spell_name in spells:
            # Trouver le fichier correspondant (par nom ou alias)
            target_file = None
            for f_path in all_spell_files:
                filename = os.path.basename(f_path).replace('.md', '')
                if filename.lower() == spell_name.lower():
                    target_file = f_path
                    break
            
            if target_file:
                update_spell_file(target_file, domain)
            else:
                print(f"Warning: Could not find file for spell '{spell_name}' (Domain: {domain})")

def update_spell_file(file_path, domain):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return

    parts = content.split('---', 2)
    if len(parts) < 3:
        return
        
    fm = parts[1]
    body = parts[2]
    
    # Gestion du champ domain_spells dans le YAML
    if "domain_spells:" in fm:
        # Si le domaine est déjà là, on ignore
        if domain in fm:
            return
        # Sinon on ajoute à la liste
        # Recherche de la fin de la liste ou ajout simple
        new_fm = fm.strip() + f"\n  - \"{domain}\""
    else:
        new_fm = fm.strip() + f"\ndomain_spells:\n  - \"{domain}\""
    
    final_content = f"---\n{new_fm.strip()}\n---\n{body}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Updated {os.path.basename(file_path)} with domain: {domain}")

if __name__ == '__main__':
    main()
