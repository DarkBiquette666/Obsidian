---
type: skill
category: Buff
element:
  - Void
classes:
  - Voidborn
tags:
  - buff
  - burst
  - minion
  - command
status: concept
locked: false
skill Family: voidborn
---

# Order: Assault

## Description
Marks a single target. All active minions gain Attack Speed and Movement Speed bonuses and focus their attacks on this target.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Buff / Command | Minion director |
| **Targeting** | Single Enemy | |
| **Effect** | Buff Minions | +AS, +MS, Forced Target |
| **Duration** | 5.0 sec | Mark duration |

## Perks System

### Available Perks

1. **[[Feeding Frenzy]]** - Each minion attack on marked target heals player for 1% Health.
2. **[[Weak Point]]** - Marked target has 0% Block and Dodge chance.
3. **[[Serrated Claws]]** - Minion attacks against marked target have 100% chance to Bleed.
4. **[[Critical Impact]]** - First attack of each minion on target is a guaranteed Critical Strike.
5. **[[Mark Contagion]]** - If target dies, mark jumps to nearest enemy.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/OrderAssault/order_assault.tres`
- **Main Skill:** Yes
