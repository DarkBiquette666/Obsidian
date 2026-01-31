---
type: skill
category: Attack
element:
  - Physical
  - Void
classes:
  - Voidborn
tags:
  - dot
  - single-target
  - spawner
  - infestation
status: concept
locked: false
skill Family: voidborn
---

# Parasitic Implant

## Description
Infects a single target with a high-damage parasite. If the target dies, 2 Void Scarabs spawn from the corpse.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Attack | Single Target DoT |
| **Damage Type** | Physical + Void | |
| **Duration** | Medium | |
| **Effect** | Spawn on Death | 2 Scarabs |

## Perks System

### Available Perks

1. **[[Accelerated Gestation]]** - Shorter duration, faster damage ticks.
2. **[[Larval Queen]]** - Spawns a Praetorian Guard (if available) instead of Scarabs from Elites.
3. **[[Contagion]]** - Spreads to a nearby enemy if the target dies.
4. **[[Hemophilia]]** - Increases effectiveness of Bleeds on the target.
5. **[[Vital Extraction]]** - Restores Mana to the player on each damage tick.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/ParasiticImplant/parasitic_implant.tres`
- **Main Skill:** Yes
