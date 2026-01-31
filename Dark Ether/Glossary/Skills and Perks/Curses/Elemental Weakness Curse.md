---
type: skill
category: Curse
element: []
classes:
  - Fortunians
  - Lesharii
  - Torin
  - Umbrathi
  - Voidborn
  - Vorathros
tags:
  - spell
  - area
  - curse
  - elemental
  - weakness
status: implemented
locked: false
skill Family: curse
---

# Elemental Weakness Curse

## Description
Casts a curse that reduces elemental resistances of enemies in the target area. This malevolent spell weakens the natural defenses of foes against fire, cold, lightning, and other elemental forces.

## Lore
The Elemental Weakness Curse represents the mastery of elemental balance and the ability to disrupt the natural resistances that protect living beings. By speaking forbidden words of unmaking, the caster tears holes in the elemental defenses of their enemies, leaving them vulnerable to the fury of the elements.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Curse Spell | Area curse magic |
| **Damage Base** | 0 | No direct damage |
| **Cast Time** | 0.1 sec | Very fast casting |
| **Critical Chance** | 0% | Curses cannot crit |
| **Cost** | 25 Mana | Per cast |
| **Cooldown** | 2.0 sec | Short cooldown |
| **Lifespan** | 2.0 sec | Effect application window |
| **Classes** | All except Astraliens | Wide class access |
| **Weapon Required** | No | Independent casting |
| **Movement Speed** | 80% | Slight reduction while casting |
| **Affects Allies** | No | Enemy-only targeting |

## Curse Properties

| Propriété | Valeur | Description |
|-----------|--------|-------------|
| **Target Area** | Cursor Position | Placed at mouse location |
| **Effect Type** | Resistance Reduction | Lowers elemental resistances |
| **Duration** | Variable | Based on curse effect data |
| **Persistent** | No | Single application |
| **Stacking** | Depends on implementation | May stack with other curses |
| **Resistance Type** | All Elemental | Fire, Cold, Lightning, etc. |

## Elemental Resistance Reduction

### Affected Elements
- **Fire Resistance** - Reduced vulnerability to flame
- **Cold Resistance** - Reduced protection from frost  
- **Lightning Resistance** - Reduced electrical immunity
- **Poison Resistance** - Reduced toxin protection (if elemental)
- **Ether Resistance** - Reduced void protection

### Curse Mechanics
- **Application Method:** Area-based curse placement
- **Resistance Penetration:** Bypasses curse resistance partially
- **Duration:** Determined by curse effect resource
- **Magnitude:** Based on curse power and enemy level

## Tactical Usage

**Strengths:**
- Amplifies all elemental damage significantly
- Fast casting speed (0.1 seconds)
- Wide class availability (5 of 6 classes)
- Low cooldown (2 seconds)
- Area application affects multiple enemies

**Weaknesses:**
- No direct damage contribution
- Mana cost (25 per cast)
- Requires elemental damage to be effective
- Limited duration window
- Movement speed penalty during cast

**Strategic Applications:**
- Setup for elemental damage dealers
- Support role in team compositions
- Amplifies spell damage builds
- Combines with elemental weapons
- Essential for elemental penetration builds

## Class Synergies

### Excluded Class
- **Astraliens:** Notably excluded from this curse
  - May have thematic reasons (light vs darkness)
  - Possibly conflicts with class identity
  - Could indicate elemental purity concept

### Compatible Classes
- **Fortunians:** Enhances their versatile magic
- **Lesharii:** Supports nature-based elemental attacks
- **Torin:** Complements their diverse combat options
- **Umbrathi:** Amplifies shadow and elemental combinations
- **Voidborn:** Enhances ether and elemental damage
- **Vorathros:** Supports their metamorphic elemental forms

## Build Synergies

**Elemental Damage Builds:**
- **Fire Builds:** Dramatically increases fire damage
- **Cold Builds:** Enhances frost and chill effects
- **Lightning Builds:** Amplifies shock and electrical damage
- **Multi-Element Builds:** Benefits all elemental components

**Spell Damage Builds:**
- **Cast Speed:** Reduces 0.1 second cast time
- **Mana Efficiency:** Reduces 25 mana cost
- **Curse Effectiveness:** Increases resistance reduction

**Support Builds:**
- **Aura Effectiveness:** May enhance curse power
- **Area of Effect:** Increases curse coverage
- **Duration:** Extends curse application window

## Combination Strategies

**With Other Curses:**
- Stack multiple debuffs for maximum effect
- Coordinate with damage-over-time curses
- Combine with physical weakness for hybrid builds

**With Elemental Skills:**
- **Ether Ball:** Amplifies both fire and ether components
- **Storm Caller:** Enhances lightning strike damage
- **Frost Aura:** Increases cold damage and chill
- **Elemental Weapons:** Boosts weapon elemental damage

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Elemental Weakness Curse/elemental_weakness_curse.tres`
- **Effect Resource:** `curse_elemental_weakness_effect.tres`
- **Scene:** `Elemental Weakness Curse.tscn`
- **Icon:** `Curse_ElementalWeakness_Icon.png`
- **Status:** Fully implemented
- **Main Skill:** Yes (primary curse option)

## Technical Notes

- Uses standard curse behavior system
- References external curse effect resource
- Area-based application at cursor position
- No damage component (disable_damage = true)
- Standard spell casting framework

## Balance Considerations

- Moderate mana cost prevents spam
- Short cooldown allows tactical use
- Class restriction maintains balance
- No direct damage prevents overpowering

## Related

- [[Curse]] - Skill category and mechanics
- [[Elemental Weakness]] - Status effect applied
- [[Spell]] - Casting mechanics
- [[Area]] - Application method
- [[Resistance]] - Affected mechanic
- [[Fire Damage]], [[Cold Damage]], [[Lightning Damage]] - Enhanced damage types