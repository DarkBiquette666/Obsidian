---
type: skill
category: Ultimate
element:
  - Physical
  - Void
classes:
  - Voidborn
tags:
  - ultimate
  - terrain
  - aoe
  - infestation
status: concept
locked: false
skill Family: voidborn
---

# The Living Abyss

## Description
Transforms the ground around the player into living insectoid matter. Tentacles and mandibles emerge to attack anything that moves.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Ultimate | Terrain / Zone |
| **Damage Type** | Physical + Void | |
| **Duration** | Medium | |
| **Effect** | Attack Enemies | |

## Perks System

### Available Perks

1. **[[Difficult Terrain]]** - Enemies in the zone are Slowed by 60%.
2. **[[Feast]]** - If an enemy dies in the zone, duration is extended by 1 second.
3. **[[Voracious Mandibles]]** - Zone deals Physical damage applies Bleed continuously (1 stack/sec).
4. **[[Continuous Hatching]]** - Periodically spawns free **Void Spitters** at the zone edge.
5. **[[Call of the Void]]** - Enemies are slowly Pulled towards the center.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/TheLivingAbyss/the_living_abyss.tres`
- **Main Skill:** Yes
