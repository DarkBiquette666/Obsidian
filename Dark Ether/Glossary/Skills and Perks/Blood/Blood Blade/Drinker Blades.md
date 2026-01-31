---
type: perk
skill: Blood Blade
category: damage_conversion
tags:
  - bleed_consumption
  - burst_damage
  - dot_conversion
  - combo_mechanic
status: concept
---

# Drinker Blades

## Description
Blood Blade hits consume bleeding stacks on enemies to deal instant damage, converting damage-over-time into immediate burst. This creates a unique rhythm of applying and consuming bleeds for maximum damage.

## Mechanics

### Consumption System
- **Trigger:** On blade hit
- **Consumes:** All bleeding stacks
- **Conversion:** DoT damage to instant
- **Reset:** Target can be re-bled
- **Per Hit:** Each blade consumes independently

### Damage Calculation
- **Base Hit:** Normal blade damage
- **Plus:** Total remaining bleed damage
- **Instant Application:** All at once
- **Efficiency:** ~80-100% of DoT value

### Strategic Timing
- **Build Phase:** Apply bleeding stacks
- **Consume Phase:** Blade hit for burst
- **Repeat Cycle:** Reapply and consume
- **Optimization:** Time consumption at peak stacks

## Tactical Applications

### Burst Damage Windows
- **Execute Potential:** Massive instant damage
- **Boss Phases:** Burst before immunity
- **Priority Targets:** Quick elimination
- **PvP:** Unpredictable burst

### Stack Management
- **Pre-Stacking:** Build bleeds before consume
- **Multi-Source:** Various bleed applications
- **Timing Control:** Choose when to burst
- **Reset Advantage:** Can immediately reapply

## Synergies

### Bleed Sources
- **Base Blood Blade:** 200% bleed factor
- **Tainted Blood:** Additional bleed spreading
- **Anemic Curse:** Hemorrhagic Wounds combo
- **Multiple Blades:** Faster stack building

### Build Strategies
- **Burst Assassin:** High stack instant kills
- **Rhythm Fighter:** Apply-consume cycles
- **Hybrid Damage:** Mix DoT and burst
- **Control Burst:** Timed eliminations

## Risk vs Reward

### Advantages
- **Instant Damage:** No waiting for DoT
- **Burst Potential:** Massive spike damage
- **Flexible Timing:** Control when to consume
- **Counter Healing:** Instant damage beats regen

### Trade-offs
- **Loses DoT:** No persistent damage
- **Requires Setup:** Need stacks first
- **Timing Dependent:** Must optimize consumption
- **Single Use:** Stacks consumed per hit

## Implementation Status

**Status:** To Do

### Technical Requirements
- Stack detection system
- Damage calculation formula
- Consumption mechanics
- Visual feedback for consumption
- Stack tracking per enemy

### Balance Considerations
- Conversion efficiency rate
- Stack consumption rules
- Multi-blade interactions
- Maximum burst potential
- Cooldown requirements

### Visual Design
- Stack consumption effect
- Burst damage numbers
- Blade "drinking" animation
- Enemy stack indicators

## Related Concepts
- [[Blood Blade]] - Base skill
- [[Bleed]] - Consumed resource
- [[Burst Damage]] - Damage type
- [[DoT]] - Converted mechanic
- [[Stack Management]] - Gameplay pattern