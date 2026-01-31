---
type: perk
skill: Vital Link
category: range_modifier
tags:
  - positioning
  - flexibility
  - tradeoff
  - range
status:
  - implemented
---

# Elastic Tether

## Description
Extends the maximum range of Vital Link by 50% before it breaks, but reduces life drain efficiency by 50% when beyond the normal maximum distance. This perk offers positional flexibility at the cost of sustain power.

## Mechanics

### Range Modification
- **Base Range Extension:** +50% maximum distance
- **Normal Range:** 100% life drain efficiency
- **Extended Range:** 50% life drain efficiency
- **Break Point:** 1.5x normal maximum range
- **Smooth Transition:** Gradual efficiency reduction

### Efficiency Scaling
- **0-100% Range:** Full drain rate
- **100-150% Range:** Half drain rate
- **Visual Indicator:** Chain dims at extended range
- **Warning System:** Visual/audio cue near break point

## Trade-off Philosophy

### Benefits
- **Safety:** Maintain connection while retreating
- **Flexibility:** Adapt to dynamic combat situations
- **Kiting Potential:** Enable hit-and-run tactics
- **Emergency Option:** Escape without losing link

### Costs
- **Reduced Sustain:** Half healing at distance
- **Resource Efficiency:** Less life per mana spent
- **Risk Assessment:** Must balance safety vs effectiveness

## Strategic Usage

### Positioning Strategies
- **Hybrid Positioning:** Dance in and out of optimal range
- **Safe Engagement:** Start fights from safer distance
- **Tactical Retreat:** Maintain link while repositioning
- **Boss Mechanics:** Avoid attacks without breaking connection

### Build Integration
- **Ranged Hybrids:** Perfect for mixed damage builds
- **Safety-First:** Conservative positioning playstyle
- **Mobility Builds:** Synergizes with movement skills

## Synergies

### Complementary Perks
- **Crimson Anchor:** Ultimate range flexibility
- **Twin Tethers:** Manage multiple links safely
- **Sanguine Refuge:** Safe initial engagement

### Skill Combinations
- **Movement Skills:** Dash/teleport without breaking
- **Ranged Attacks:** Attack while maintaining drain
- **Defensive Skills:** Create distance when threatened

## Implementation Status

**Status:** To Do

### Technical Requirements
- Range calculation system
- Efficiency scaling algorithm
- Visual feedback for range zones
- Smooth transition mechanics
- Break point warnings

### Balance Considerations
- Extension percentage tuning
- Efficiency reduction curve
- Interaction with other range modifiers
- Visual clarity requirements

### UI/UX Elements
- Range indicator overlay
- Efficiency display
- Chain visual changes
- Audio feedback system

## Related Concepts
- [[Vital Link]] - Base skill
- [[Positioning]] - Core mechanic
- [[Range]] - Modified attribute
- [[Crimson Anchor]] - Related range perk
- [[Kiting]] - Enabled tactic