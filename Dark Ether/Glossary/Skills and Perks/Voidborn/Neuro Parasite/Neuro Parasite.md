---
type: skill
category: Manipulation
element:
  - Void
classes:
  - Voidborn
tags:
  - mind-control
  - minion
  - utility
status: concept
locked: false
skill Family: voidborn
---

# Neuro-Parasite

## Description
Launches a parasite that takes control of a non-Boss enemy for a short duration. The enemy fights for you.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Manipulation | Mind Control |
| **Target** | Single Enemy | Non-Boss |
| **Duration** | Short | |

## Perks System

### Available Perks

1. **[[Kamikaze]]** - Controlled enemy explodes (Void damage) at the end of duration.
2. **[[Superior Host]]** - Controlled enemy gains +50% Damage and Attack Speed.
3. **[[Exsanguination]]** - Enemy loses 10% HP/sec as Bleed that spawns blood on ground.
4. **[[Plague Spreader]]** - Controlled enemy emits a Poison aura. (Tainted Blood Synergy)
5. **[[Mind Domination]]** - Allows controlling Elite enemies (but duration reduced by 50%).

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/NeuroParasite/neuro_parasite.tres`
- **Main Skill:** Yes
