---
type: perk
skill: Vital Link
category: multi_target
tags:
  - chain
  - bleeding
  - area_effect
  - life_drain
  - synergy
status: implemented
---

# Shared Siphon

## Description
When an enemy within radius starts to bleed, the Vital Link automatically spreads to them, creating a network of parasitic connections. This allows simultaneous life drain from multiple sources, dramatically increasing sustain potential.

## Mechanics

### Trigger System
- **Activation Condition:** Enemy in range begins bleeding
- **Range Detection:** Automatic scanning for bleeding targets
- **Chain Spread:** Link bounces to valid targets
- **Multi-Target Cap:** May have maximum connection limit
- **Resource Cost:** Additional mana per extra target

### Drain Distribution
- **Simultaneous Drain:** All connected enemies drain together
- **Life Gain Stacking:** Healing from all sources combined
- **Individual Tracking:** Each link calculated separately
- **Range Management:** Each link has its own range limit

### Visual Effects
- **Network Display:** Multiple blood chains visible
- **Bleeding Detection:** Visual indicator for potential targets
- **Connection Animation:** Chain spread effect

## Synergies

### Primary Synergies
- **Blood Blade:** Area bleeding enables mass connections
- **Tainted Blood:** Bleeding spread creates chain reactions
- **Hemorrhagic Effects:** Any bleeding source triggers spread

### Build Potential
- **Area Control:** Transform single-target into area effect
- **Sustain Multiplication:** Exponential healing with targets
- **Crowd Management:** Drain multiple enemies simultaneously

## Strategic Usage

### Positioning Requirements
- **Central Positioning:** Stay within range of multiple enemies
- **Risk Management:** More targets = more positioning complexity
- **Escape Planning:** Multiple tethers limit mobility

### Target Selection
- **Bleeding Priority:** Focus on enemies that bleed easily
- **Group Engagement:** Maximize targets in range
- **Chain Optimization:** Position for maximum spread

## Risk vs Reward

### Benefits
- Massive life sustain from multiple sources
- Area control through life drain network
- Synergizes with bleeding builds perfectly

### Challenges
- Complex positioning requirements
- Range management for multiple links
- Increased vulnerability from stationary positioning

## Implementation Status

**Status:** To Do

### Technical Requirements
- Bleeding detection system
- Multi-target link management
- Network visualization
- Performance optimization for multiple drains
- Range calculation for each link

### Balance Considerations
- Maximum target limit
- Drain efficiency per target
- Mana cost scaling
- Performance impact with many connections

### Development Priority
- High priority due to unique gameplay
- Core perk for area-effect builds
- Requires robust testing for edge cases

## Related Concepts
- [[Vital Link]] - Base skill
- [[Blood Blade]] - Primary bleeding source
- [[Bleed]] - Trigger condition
- [[Chain]] - Spread mechanic
- [[Area Effect]] - Coverage type
- [[Life Drain]] - Core mechanic