---
type: skill
category: Area
element:
  - Void
classes:
  - Voidborn
tags:
  - aoe
  - debuff
  - dot
  - infestation
  - slow
status: concept
locked: false
skill Family: voidborn
---

# Parasitic Swarm

## Description
Sends a swarm of micro-insects to a target area. Enemies in the area are Slowed and rapidly gain stacks of **Infestation**.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Area Effect | Debuff / DoT |
| **Damage Type** | Void | Micro-insect bites |
| **Status Effect** | Slow, Infestation | |
| **Duration** | 5.0 sec | Area duration |

## Perks System

### Available Perks

1. **[[Flesh Eaters]]** - Infestation applied by this skill also reduces Armor (Physical Damage Synergy).
2. **[[Hemorrhagic Fever]]** - If an infested target takes Physical damage, they start to Bleed.
3. **[[Panic]]** - Enemies in the swarm have a chance to Flee (Fear) due to crawling insects.
4. **[[Lingering Swarm]]** - Swarm remains on the ground for 3 additional seconds.
5. **[[Viral Vector]]** - If an enemy dies inside, the swarm moves to the nearest living enemy.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/ParasiticSwarm/parasitic_swarm.tres`
- **Main Skill:** Yes
