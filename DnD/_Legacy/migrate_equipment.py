import os
import glob
import re

def main():
    root_folder = os.path.join('Glossary', 'Objets', 'Equipement')
    
    # 1. Armes
    migrate_folder(os.path.join(root_folder, 'Armes'), "Weapon", parse_weapon)
    
    # 2. Armures
    migrate_folder(os.path.join(root_folder, 'Armures'), "Armor", parse_armor)
    
    # 3. Outils (Simple Equipment for now, or Tool blueprint if we make one)
    # Let's use Equipment for generic stuff
    migrate_folder(os.path.join(root_folder, 'Outils'), "Equipment", parse_basic)
    
    # 4. Matériel
    migrate_folder(os.path.join(root_folder, "Matériel d'aventurier"), "Equipment", parse_basic)

def migrate_folder(folder, class_name, parser_func):
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            if f.endswith('.md'):
                files.append(os.path.join(dirpath, f))
                
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.startswith('---'): continue
        parts = content.split('---', 2)
        if len(parts) < 3: continue
        
        fm = parts[1]
        body = parts[2]
        
        # Check if already migrated
        if "Class:" in fm: continue
        
        # Parse fields
        updates = parser_func(fm)
        
        # Update FM
        new_fm = f"Class: {class_name}\n" + fm
        
        # Apply updates (simple append/replace logic)
        for k, v in updates.items():
            if k in new_fm:
                # Replace existing line
                new_fm = re.sub(f"{k}:.*", f"{k}: {v}", new_fm)
            else:
                # Append
                new_fm += f"{k}: {v}\n"
                
        final_content = f"---\n{new_fm.strip()}\n---\n{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Migrated {os.path.basename(file_path)} to {class_name}")

def parse_basic(fm):
    updates = {}
    # Map french keys to blueprint keys
    if "Prix:" in fm:
        val = re.search(r'Prix: (.*)', fm).group(1).strip()
        updates['cost'] = val
    if "Poids:" in fm:
        val = re.search(r'Poids: (.*)', fm).group(1).strip()
        updates['weight'] = val
    return updates

def parse_weapon(fm):
    updates = parse_basic(fm)
    if "Dégâts:" in fm:
        val = re.search(r'Dégâts: (.*)', fm).group(1).strip()
        updates['damage'] = val
    if "TypeDegats:" in fm:
        val = re.search(r'TypeDegats: (.*)', fm).group(1).strip()
        updates['damage_type'] = val
    if "Catégorie:" in fm:
        val = re.search(r'Catégorie: (.*)', fm).group(1).strip()
        updates['category'] = val
    if "Type:" in fm:
        val = re.search(r'Type: (.*)', fm).group(1).strip()
        updates['range_type'] = val
    return updates

def parse_armor(fm):
    updates = parse_basic(fm)
    if "CA:" in fm:
        val_line = re.search(r'CA: (.*)', fm).group(1).strip()
        # Extract number "14" from "14 + Dex"
        base_ac_match = re.search(r'^(\d+)', val_line)
        if base_ac_match:
            updates['ac_base'] = int(base_ac_match.group(1))
        
        if "+ modificateur de Dex" in val_line:
            updates['dex_bonus'] = "true"
            if "max 2" in val_line:
                updates['max_dex_bonus'] = 2
        else:
            updates['dex_bonus'] = "false"
            updates['max_dex_bonus'] = 0
            
    if "Discretion:" in fm and "Désavantage" in fm:
        updates['stealth_disadvantage'] = "true"
        
    if "Catégorie:" in fm:
        val = re.search(r'Catégorie: (.*)', fm).group(1).strip()
        updates['category'] = val

    return updates

if __name__ == '__main__':
    main()
