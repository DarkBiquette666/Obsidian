---
type: skill
category: Movement
element:
  - Void
classes:
  - Voidborn
tags:
  - movement
  - teleport
  - invulnerable
status: concept
locked: false
skill Family: voidborn
---

# Hive Shift

## Description
The Voidborn dissolves into a swarm of invulernable insects and reforms at a target location.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Movement | Teleport |
| **Damage Type** | None | Base skill is utility only |
| **Invulnerability** | Yes | During travel/dissolve |
| **Range** | Medium | |

## Perks System

### Available Perks

1. **[[Toxic Trail]]** - Leaves a trail of poison between start and end points.
2. **[[Offensive Materialization]]** - Reforming deals AoE damage and knocks back enemies.
3. **[[Decoy]]** - Leaves a static copy (shed skin) at start point that attracts enemies and explodes.
4. **[[Blood Thirst]]** - Passing through Bleeding enemies reduces cooldown. (Torin Synergy)
5. **[[Ethereal Form]]** - After teleporting, gain 30% Dodge chance for 3 seconds.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/HiveShift/hive_shift.tres`
- **Main Skill:** Yes
