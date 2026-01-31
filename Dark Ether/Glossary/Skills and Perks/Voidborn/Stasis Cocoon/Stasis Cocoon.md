---
type: skill
category: Control
element:
  - Void
classes:
  - Voidborn
tags:
  - cc
  - stasis
  - defense
  - single
status: concept
locked: false
skill Family: voidborn
---

# Stasis Cocoon

## Description
Envelops an enemy (or the player) in a solid cocoon. The target cannot move or act but is immune to external damage (DoTs still apply).

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Control | Stasis effect |
| **Damage Type** | None | Base skill is non-damaging |
| **Duration** | 5.0 sec | Duration |
| **Immunity** | Yes | External damage immunity |

## Perks System

### Available Perks

1. **[[Internal Incubation]]** - The cocoon deals damage over time to the trapped enemy.
2. **[[Sanctuary]]** - If cast on player or ally, regenerates Health and Mana rapidly.
3. **[[Blood Prison]]** - Absorbs nearby blood pools to extend duration.
4. **[[Violent Rupture]]** - Cocoon explodes at the end, dealing Physical damage to nearby enemies.
5. **[[Vulnerable Prey]]** - Target suffers "Fragility" (+Damage Taken) for 5 seconds after exiting.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/StasisCocoon/stasis_cocoon.tres`
- **Main Skill:** Yes
