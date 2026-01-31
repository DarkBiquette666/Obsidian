---
type: skill
category: Summon
element:
  - Physical
  - Void
classes:
  - Voidborn
tags:
  - summon
  - minion
  - ranged
  - void
  - physical
status: concept
locked: false
skill Family: voidborn
---

# Void Spitters

## Description
Summons 3 small immobile insects that act as turrets, spitting energy needles at nearby enemies.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Summon | Minion skill |
| **Damage Type** | Physical + Void | Mixed damage |
| **Count** | 3 | Base number of minions |
| **Behavior** | Turret | Immobile, ranged attack |
| **Infestation** | No | Base skill does not apply (see perks) |

## Perks System

### Available Perks

1. **[[Barbed Needles]]** - Projectiles have 20% chance to inflict Bleed. (Torin Synergy)
2. **[[Rapid Volley]]** - Increases attack speed but reduces lifespan.
3. **[[Bio-Artillery]]** - Spitters fire in an arc (mortar), dealing AoE damage on impact.
4. **[[Nutritious Sacrifice]]** - Interact to "eat" a spitter, restoring Health and Mana.
5. **[[Sanguine Symbiosis]]** - If player is under Life Leech Aura (Torin), Spitters also benefit from lifesteal to heal player.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/VoidSpitters/void_spitters.tres`
- **Main Skill:** Yes
