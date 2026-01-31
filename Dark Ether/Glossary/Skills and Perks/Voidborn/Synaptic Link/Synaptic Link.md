---
type: skill
category: Support
element:
  - Void
classes:
  - Voidborn
tags:
  - buff
  - utility
  - minion
status: concept
locked: false
skill Family: voidborn
---

# Synaptic Link

## Description
Links the player to a target minion or ally, sharing damage taken and boosting damage dealt.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Support | Buff / Link |
| **Target** | Single Ally/Minion | |
| **Effect** | Damage Share | +Damage Buff |

## Perks System

### Available Perks

1. **[[Martyr]]** - Minion takes 80% of damage taken by player.
2. **[[Attack Feedback]]** - Player gains Attack Speed when the linked target attacks.
3. **[[Multi-Link]]** - Can link up to 2 targets.
4. **[[Heal Transmission]]** - Healing received by one is shared 50% to the other.
5. **[[Overload]]** - Active: Detonates the minion for massive damage.

## Implementation Details
- **Skill File:** `Scenes/Skills/Voidborn/SynapticLink/synaptic_link.tres`
- **Main Skill:** Yes
