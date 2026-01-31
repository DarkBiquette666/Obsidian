import os

file_path = r"D:\Git\Obsidian Plugins\obsidian-dnd-content\builder-styles.css"
with open(file_path, 'rb') as f:
    content_bytes = f.read()

# Decode with replacement to handle any previous corruption
content = content_bytes.decode('utf-8', errors='replace')

lines = content.splitlines()
new_lines = []
fixed = False

# The target string we want: content: "\2022 " !important; 
# Constructed safely:
backslash = chr(92)
target_content = f'        content: "{backslash}2022 " !important; /* Unicode bullet */'

for line in lines:
    if 'content:' in line and 'Unicode bullet' in line:
        new_lines.append(target_content)
        new_lines.append('        z-index: 5 !important;')
        new_lines.append('        display: inline-block !important;')
        fixed = True
    elif 'z-index: 5' in line and fixed:
        continue # Skip if we already added it (idempotencyish)
    elif 'display: inline-block' in line and fixed:
        continue
    else:
        new_lines.append(line)

new_content = "\n".join(new_lines)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Fixed: {fixed}")
