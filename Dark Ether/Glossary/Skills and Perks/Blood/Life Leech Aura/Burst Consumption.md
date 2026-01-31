---
type: perk
skill: Life Leech Aura
category: Burst
tags: [blood, aura, burst, deactivation, damage]
status: concept
---

# Burst Consumption

## Overview
When the Life Leech Aura is deactivated, it releases all accumulated life energy in a devastating burst that deals damage equal to 3 seconds worth of accumulated drain to all enemies within range.

## Mechanics

### Primary Effect
- **Damage Calculation**: Burst deals damage equal to 3 seconds of accumulated drain
- **Accumulation Window**: Continuously tracks life drained over the last 3 seconds
- **Trigger Condition**: Manual aura deactivation or forced deactivation
- **Range**: Same as Life Leech Aura radius at time of deactivation

### Technical Details
- **Damage Formula**: `burst_damage = sum(drain_per_second) * 3`
- **Accumulation Buffer**: Rolling 3-second window of drain values
- **Damage Type**: Pure damage (bypasses all resistances)
- **Scaling**: Damage scales with aura level and Blood affinity

## Synergies

### Simple Synergies
- **Bleeding Resonance**: Higher leech rates from bleed stacks increase burst damage
- **Sanguine Overflow**: Overflow generation increases base drain for burst calculation
- **Vital Link**: Linked targets contribute their drain to burst accumulation

### Complex Synergies
- **Pact of Pain + Burst**: Self-damage from pact increases drain rate, amplifying burst significantly
- **Toxic Symbiosis**: Regeneration siphoning adds to accumulation buffer for massive burst potential
- **Crimson Vortex**: Pulled enemies take concentrated burst damage in confined area

## Trade-offs
- **Strategic Timing**: Requires tactical aura management for optimal burst timing
- **Cooldown Penalty**: 5-second cooldown before aura can be reactivated after burst
- **Resource Cost**: Burst consumes 150% of normal aura deactivation cost

## Implementation Details

### Burst Mechanics
- **Accumulation Tracking**: Continuous monitoring of drain values with timestamp buffer
- **Trigger System**: Multiple deactivation trigger types (manual, forced, emergency)
- **Visual Effects**: Explosive crimson burst with screen shake and particle effects

### Damage Application
- **Instant Application**: All burst damage applied simultaneously to all enemies
- **Damage Scaling**: Scales with enemy proximity to aura center
- **Critical Burst**: 10% chance for double damage burst

## Advanced Interactions

### Accumulation Sources
- **Base Drain**: Standard life leech from enemies in range
- **Synergy Drain**: Additional drain from perk interactions
- **Environmental Drain**: Drain from corrupted terrain or blood pools

### Burst Variations
- **Focused Burst**: Can target specific enemy for concentrated damage
- **Chain Burst**: Burst damage can chain between enemies
- **Lingering Burst**: Burst creates temporary damage field at deactivation point

## Tactical Applications

### Combat Scenarios
- **Emergency Escape**: Deactivate when overwhelmed for crowd control
- **Boss Finisher**: Save accumulated drain for critical damage phases
- **Area Denial**: Use burst to clear chokepoints or control space

## Implementation Status
**Status**: To Do
**Priority**: Medium
**Dependencies**: Life Leech Aura base system, damage accumulation tracking, burst damage mechanics