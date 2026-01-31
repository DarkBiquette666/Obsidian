import os

# Configuration
OUTPUT_DIR = r"Y:\\Shared drives\\Ubiquity\\Perso\\Obsidian\\Dark Ether\\Dark Ether\\Glossary\\Support Runes\\Assets"
SIZE = 512
CENTER = SIZE // 2
STROKE_BEAM = 22
STROKE_GLYPH = 12

# Colors
COLOR_MAIN = "#FFFFFF" # White for engine integration

def create_svg(filename, paths):
    """Generates the SVG content (Flat White, No Glow, Transparent Background)."""
    svg_header = f'''<svg width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}" xmlns="http://www.w3.org/2000/svg">
  <g stroke="{COLOR_MAIN}" fill="none" stroke-linecap="round" stroke-linejoin="round">
'''
    svg_body = ""
    for path_data in paths:
        d = path_data['d']
        width = path_data['width']
        dash = path_data.get('dash', "")
        opacity = path_data.get('opacity', 1.0)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        svg_body += f'    <path d="{d}" stroke-width="{width}" opacity="{opacity}"{dash_attr} />\n'

    svg_footer = '  </g>\n</svg>'
    
    with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(svg_header + svg_body + svg_footer)

# --- A. BEAMS & MORPHOLOGY ---

def get_force(variant="plain"):
    if variant == "double":
        return [
            {'d': f"M {CENTER-8} 80 L {CENTER-8} 432", 'width': STROKE_BEAM//1.5},
            {'d': f"M {CENTER+8} 80 L {CENTER+8} 432", 'width': STROKE_BEAM//1.5}
        ]
    elif variant == "segmented":
        return [{'d': f"M {CENTER} 80 L {CENTER} 432", 'width': STROKE_BEAM, 'dash': "40, 20"}]
    return [{'d': f"M {CENTER} 80 L {CENTER} 432", 'width': STROKE_BEAM}]

def get_flux(variant="plain"):
    d = "M 120 400 L 392 112"
    if variant == "double":
        return [
            {'d': "M 110 395 L 382 107", 'width': STROKE_BEAM//1.5},
            {'d': "M 130 405 L 402 117", 'width': STROKE_BEAM//1.5}
        ]
    return [{'d': d, 'width': STROKE_BEAM}]

def get_field(variant="plain"):
    d = "M 120 120 L 256 400 L 392 120"
    if variant == "segmented":
        return [{'d': d, 'width': STROKE_BEAM, 'dash': "30, 15"}]
    return [{'d': d, 'width': STROKE_BEAM}]

def get_system(variant="plain"):
    d = "M 256 80 L 392 256 L 256 432 L 120 256 Z"
    if variant == "node":
        return [
            {'d': d, 'width': STROKE_BEAM},
            {'d': f"M {CENTER-20} {CENTER-20} L {CENTER+20} {CENTER+20} M {CENTER+20} {CENTER-20} L {CENTER-20} {CENTER+20}", 'width': STROKE_GLYPH}
        ]
    return [{'d': d, 'width': STROKE_BEAM}]

def get_body(variant="plain"):
    return [{'d': "M 100 380 L 256 120 L 412 380", 'width': STROKE_BEAM}]

# --- B. GLYPHS & POSITIONING ---

def glyph_speed(pos="mid-right"):
    if pos == "high":
        return [{'d': "M 400 120 L 440 150 L 400 180 M 370 120 L 410 150 L 370 180", 'width': STROKE_GLYPH}]
    # Shifted mid-right to avoid collision with diamond tip (x=392)
    return [{'d': "M 440 240 L 480 270 L 440 300 M 410 240 L 450 270 L 410 300", 'width': STROKE_GLYPH}]

def glyph_multi():
    return [{'d': "M 220 220 L 300 220 M 210 290 L 290 290", 'width': STROKE_GLYPH}]

def glyph_fork():
    return [{'d': "M 392 112 L 350 60 M 392 112 L 440 80", 'width': STROKE_GLYPH}]

def glyph_chain():
    return [{'d': "M 392 112 L 460 112 L 460 180", 'width': STROKE_GLYPH}]

def glyph_life():
    return [{'d': "M 256 220 L 256 300 M 216 260 L 296 260", 'width': STROKE_GLYPH}]

def glyph_chaos():
    return [{'d': f"M {CENTER} 360 L {CENTER+20} 390 L {CENTER} 420 L {CENTER-20} 390 Z", 'width': STROKE_GLYPH}]

def glyph_cycle():
    return [{'d': "M 256 180 L 290 180 L 275 195 M 256 332 L 222 332 L 237 317", 'width': STROKE_GLYPH}]

def glyph_cut():
    return [{'d': "M 180 256 L 332 256", 'width': STROKE_GLYPH}]

def glyph_duration():
    return [{'d': "M 392 256 L 470 256", 'width': STROKE_GLYPH}]

def glyph_expansion():
    return [{'d': "M 80 100 L 256 460 L 432 100", 'width': STROKE_GLYPH, 'opacity': 0.6}]

def glyph_compression():
    return [{'d': "M 180 180 L 220 220 M 332 180 L 292 220", 'width': STROKE_GLYPH}]

def glyph_range():
    return [{'d': f"M {CENTER} 400 L {CENTER} 460", 'width': STROKE_GLYPH}]

def glyph_target():
    return [{'d': "M 150 150 L 200 150 L 200 200", 'width': STROKE_GLYPH}]

def glyph_bleed():
    return [{'d': "M 280 180 L 320 210 L 280 240", 'width': STROKE_GLYPH}]

# --- ANCHOR DETAILS ---
def anchor_dot(x, y):
    return [{'d': f"M {x} {y} L {x+2} {y+2}", 'width': STROKE_GLYPH+4}]

# --- MAPPING ---

runes = [
    ("Accelerated_Affliction", get_system("plain") + glyph_speed("high") + anchor_dot(CENTER, 432)),
    ("Chain", get_flux("plain") + glyph_chain()),
    ("Concentrated_Area", get_field("plain") + glyph_compression()),
    ("Efficiency", get_system("node") + glyph_cut()),
    ("Elemental_Conversion", get_system("plain") + glyph_cycle()),
    ("Extended_Duration", get_system("plain") + glyph_duration() + anchor_dot(120, 256)),
    ("Fork", get_flux("double") + glyph_fork()),
    ("Homing", get_flux("plain") + glyph_target()),
    ("Laceration", get_force("segmented") + glyph_bleed()),
    ("Long_Reach", get_field("plain") + glyph_range()),
    ("Massive_Area", get_field("segmented") + glyph_expansion()),
    ("Multiple_Projectiles", get_flux("double") + glyph_multi()),
    ("Rapid_Recharge", get_system("plain") + glyph_speed("mid-right")),
    ("Vicious_Ailments", get_force("plain") + glyph_chaos()),
    ("Vitality", get_body("plain") + glyph_life()),
]

if __name__ == "__main__":
    for name, paths in runes:
        create_svg(f"{name}_Rune.svg", paths)
    print(f"Generated {len(runes)} runes in Assets/")
