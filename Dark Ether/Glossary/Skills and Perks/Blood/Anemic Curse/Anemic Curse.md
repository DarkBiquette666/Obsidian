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
  - blood
  - vitality
  - weakness
status: implemented
locked: false
skill Family: blood
---

# Anemic Curse

## Description
Casts a curse that weakens enemies' vitality and resilience in the target area. The caster inflicts a debilitating curse on enemies, weakening their vitality and resilience by manipulating their blood.

## Lore
The Anemic Curse represents one of the most insidious forms of blood magic, directly attacking the life force that flows through an enemy's veins. By speaking words of enfeeblement and decay, the caster corrupts the very essence of vitality, leaving their foes weakened and vulnerable.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Curse Spell | Blood magic curse |
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

| Property | Value | Description |
|-----------|--------|-------------|
| **Target Area** | Cursor Position | Placed at mouse location |
| **Effect Type** | Vitality Debuff | Weakens health and resilience |
| **Duration** | Variable | Based on curse effect data |
| **Persistent** | No | Single application |
| **Stacking** | Depends on implementation | May stack with other curses |

## Curse Effects

### Primary Effects
- **Damage Amplification:** Increases damage taken by enemies
- **Movement Impairment:** Reduces enemy movement speed
- **Regeneration Suppression:** Decreases health regeneration rate
- **Vitality Weakness:** Overall health-based debuffs


### Implementation Tracking

See [[Anemic Curse Perks.base]] for the complete database with implementation status and priority tracking.

## Tactical Usage

**Strengths:**
- Versatile debuff with multiple effects
- Fast casting speed (0.1 seconds)
- Wide class availability (5 of 6 classes)
- Low cooldown (2 seconds)
- Powerful perk interactions
- Area application affects multiple enemies

**Weaknesses:**
- No direct damage contribution
- Mana cost (25 per cast)
- Limited duration window
- Movement speed penalty during cast
- Requires other damage sources to be effective

**Strategic Applications:**
- Setup for burst damage combos
- Support for bleed-based builds
- Crowd control through movement reduction
- Defensive utility through enemy weakening
- Essential for curse-stacking strategies

## Class Synergies

### Excluded Class
- **Astraliens:** Cannot use this blood-based curse
  - Thematic conflict with light/purity
  - Reinforces class identity distinctions

### Compatible Classes
- **Torin:** Perfect synergy with Blood Blade and bleed builds
- **Umbrathi:** Enhances shadow-based damage amplification
- **Voidborn:** Supports void damage with vulnerability
- **Others:** Provides universal damage amplification

## Build Synergies

**Bleed Builds:**
- **Hemorrhagic Wounds:** Accelerates bleed damage dramatically
- **Bleed Stacking:** Multiple sources trigger faster payoff
- **Blood Blade Combo:** Perfect pairing with Torin builds

**Physical Damage Builds:**
- **Flesh Ripper:** Massive physical damage amplification
- **Weapon Builds:** Enhances all physical attacks
- **Melee Synergy:** Close-range curse + melee attacks

**Curse Builds:**
- **Multi-Curse Strategy:** Stacks with other curse effects
- **Curse Effectiveness:** Enhances all curse applications
- **Support Role:** Amplifies team damage

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Anemic Curse/anemic_curse.tres`
- **Effect Resource:** `curse_anemic_effect.tres`
- **Scene:** `Anemic Curse.tscn`
- **Icon:** `Curse_Anemic_Icon.png`
- **Status:** Fully implemented with complete perk system
- **Main Skill:** Yes (primary curse option)

## Related

- [[Curse]] - Skill category and mechanics
- [[Blood]] - Thematic skill tree
- [[Bleed]] - Enhanced by Hemorrhagic Wounds perk
- [[Vitality]] - Primary target of the curse
- [[Spell]] - Casting mechanics
- [[Area]] - Application method