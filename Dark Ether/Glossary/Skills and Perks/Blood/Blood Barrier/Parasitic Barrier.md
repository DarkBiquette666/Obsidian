---
type: perk
skill: Blood Barrier
category: resource_manipulation
tags:
  - bleed_consumption
  - duration_extension
  - tactical_timing
  - stack_management
status: concept
---

# Parasitic Barrier

## Description
The Blood Barrier feeds on nearby bleeding effects to sustain itself, consuming bleed stacks from enemies within range to extend its duration. This creates a symbiotic relationship between offensive bleeding and defensive protection.

## Mechanics

### Consumption System
- **Range:** 8-meter radius from caster
- **Trigger:** Every 2 seconds while active
- **Consumes:** 1 bleed stack per enemy
- **Extension:** +1 second per stack consumed
- **Maximum:** Cannot exceed 200% base duration
- **Priority:** Targets highest stack count first

### Duration Calculation
- **Base Duration:** Standard barrier duration
- **Extension Rate:** 1 second per bleed stack
- **Consumption Frequency:** Every 2 seconds
- **Efficiency:** 100% conversion rate
- **Cap:** 2x base duration maximum

### Resource Management
- **Bleed Detection:** Automatic scanning
- **Stack Preservation:** Consumes only 1 stack per enemy
- **Multi-Source:** Works with all bleed types
- **Feedback:** Visual indicator when consuming
- **Range Indicator:** Shows consumption radius

## Tactical Applications

### Battlefield Control
- **Area Denial:** Longer barriers in bloody zones
- **Positioning Strategy:** Fight near bleeding enemies
- **Combo Timing:** Apply bleeds before barrier
- **Crowd Control:** Use enemy bleeding against them

### Resource Synergy
- **Bleed Spreaders:** Maximize available stacks
- **DoT Builds:** Turn offense into defense
- **Multi-Enemy:** More enemies = longer duration
- **Battle Flow:** Sustain through prolonged fights

## Strategic Applications

### Combat Phases
- **Engagement:** Apply bleeds first
- **Defense:** Activate barrier in bloody zone
- **Sustain:** Maintain through consumption
- **Adaptation:** Move to bleeding enemies

### Build Integration
- **Bleed Specialist:** Perfect synergy
- **Hybrid Builds:** Offense fuels defense
- **Crowd Fighter:** Excel in multi-enemy scenarios
- **Sustain Tank:** Extended defensive windows

## Synergies

### Bleed Sources
- **Tainted Blood:** Area bleed spreading
- **Blood Blade:** Direct bleed application
- **Anemic Curse:** Hemorrhagic Wounds stacks
- **Crimson Explosion:** AOE bleed effects

### Duration Multipliers
- **Base Blood Barrier:** Longer baseline duration
- **Other Duration Perks:** Multiplicative stacking
- **Cooldown Reduction:** More frequent usage
- **Area Effects:** Larger consumption range

## Risk vs Reward

### Advantages
- **Extended Protection:** Potentially double duration
- **Resource Efficiency:** Uses enemy debuffs
- **Positioning Reward:** Benefits skilled placement
- **Scaling Potential:** Better with more enemies

### Trade-offs
- **Positional Dependency:** Must stay near bleeding foes
- **Setup Required:** Need existing bleeds
- **Enemy Dependent:** Useless without bleeding targets
- **Range Limitation:** Must remain within consumption radius

## Implementation Status

**Status:** To Do

### Technical Requirements
- Bleed stack detection system
- Range-based scanning mechanism
- Duration extension calculations
- Visual consumption feedback
- Stack consumption priority logic

### Balance Considerations
- Maximum duration caps
- Consumption frequency tuning
- Range balance vs positioning risk
- Stack consumption efficiency
- Multi-enemy scaling limits

### Visual Design
- Consumption range indicator
- Bleed stack absorption effects
- Duration extension feedback
- Enemy stack reduction visuals
- Barrier sustainability indicators

## Related Concepts
- [[Blood Barrier]] - Base skill
- [[Bleed]] - Consumed resource
- [[Duration Extension]] - Core mechanic
- [[Resource Management]] - Gameplay pattern
- [[Tactical Positioning]] - Strategic element