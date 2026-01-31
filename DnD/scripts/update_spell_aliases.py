import os

SPELLS_DIR = r"Y:\\Shared drives\\Ubiquity\\Perso\\Obsidian\\D&D\\Glossary\\Liste des Sorts"

def generate_aliases(name):
    aliases = set()
    
    # 1. Lowercase
    lower_name = name.lower()
    aliases.add(lower_name)
    
    # 2. Plural/Singular Simple Logic
    # Case sensitive variants
    if name.endswith('s'):
        aliases.add(name[:-1]) # Try removing s
    else:
        aliases.add(name + 's') # Try adding s
        
    # Lowercase variants
    if lower_name.endswith('s'):
        aliases.add(lower_name[:-1])
    else:
        aliases.add(lower_name + 's')
        
    return aliases

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    filename = os.path.basename(filepath)
    name = os.path.splitext(filename)[0]
    
    new_aliases_set = generate_aliases(name)
    # Remove self-reference to avoid redundancy if it matches exactly
    if name in new_aliases_set:
        new_aliases_set.remove(name)
    
    if content.startswith('---\n'):
        end_frontmatter = content.find('\n---\n', 4)
        if end_frontmatter != -1:
            frontmatter_str = content[4:end_frontmatter]
            body = content[end_frontmatter+5:]
            
            lines = frontmatter_str.split('\n')
            new_lines = []
            existing_aliases = set()
            
            has_aliases_key = False
            alias_start_index = -1
            alias_end_index = -1
            
            # Pass 1: Find existing aliases block
            for i, line in enumerate(lines):
                if line.strip().startswith('aliases:'):
                    has_aliases_key = True
                    alias_start_index = i
                    # Find where it ends (next line that doesn't start with space or dash)
                    for j in range(i + 1, len(lines)):
                        if lines[j].strip() and not lines[j].startswith(' ') and not lines[j].startswith('\t') and not lines[j].startswith('-'):
                             alias_end_index = j
                             break
                    if alias_end_index == -1: # Goes to end of frontmatter
                        alias_end_index = len(lines)
                    
                    # Extract existing
                    for k in range(alias_start_index + 1, alias_end_index):
                        val = lines[k].strip().lstrip('- ').strip("'\"")
                        if val:
                            existing_aliases.add(val)
                    break
            
            # Combine
            final_aliases = sorted(list(existing_aliases.union(new_aliases_set)))
            
            # Reconstruct Frontmatter
            if has_aliases_key:
                # Add lines before aliases
                new_lines.extend(lines[:alias_start_index])
                # Add aliases header
                new_lines.append("aliases:")
                # Add all aliases
                for alias in final_aliases:
                    new_lines.append(f'  - "{alias}"')
                # Add lines after aliases
                new_lines.extend(lines[alias_end_index:])
            else:
                # Just copy everything and append aliases at the end
                new_lines = lines
                if new_lines and new_lines[-1].strip() == "":
                    new_lines.pop() # Remove trailing empty line if present
                new_lines.append("aliases:")
                for alias in final_aliases:
                    new_lines.append(f'  - "{alias}"')

            new_frontmatter = '\n'.join(new_lines)
            new_content = f"---\n{new_frontmatter}\n---\n{body}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            # print(f"Updated: {name}")

count = 0
for filename in os.listdir(SPELLS_DIR):
    if filename.endswith(".md"):
        update_file(os.path.join(SPELLS_DIR, filename))
        count += 1

print(f"Finished processing {count} files.")
