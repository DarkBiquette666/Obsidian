---
type: skill
category: Summon
element:
  - Physical
classes:
  - Voidborn
tags:
  - summon
  - minion
  - melee
  - tank
  - physical
status: concept
locked: false
skill Family: voidborn
---

# Praetorian Guard

## Description
Summons a massive void beetle that charges enemies and blocks physical projectiles. Limited to 1 active.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Summon | Tank Minion |
| **Damage Type** | 100% Physical | |
| **Count** | 1 | Limited to 1 |
| **Behavior** | Melee / Charge / Blocker | Blocks projectiles |

## Perks System

### Available Perks

1. **[[Razor Shell]]** - Enemies striking the Praetorian take physical damage and have a chance to Bleed.
2. **[[Aggression Pheromones]]** - Praetorian Taunts nearby enemies every 5 seconds.
3. **[[Siege Titan]]** - Replaces Charge with an AoE Stun attack.
4. **[[Vital Bond]]** - 50% of damage taken by player is redirected to Praetorian. (Tank Synergy)
5. **[[Chitinous Explosion]]** - On death, explodes dealing heavy physical damage and applying Bleed to all enemies.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/PraetorianGuard/praetorian_guard.tres`
- **Main Skill:** Yes
