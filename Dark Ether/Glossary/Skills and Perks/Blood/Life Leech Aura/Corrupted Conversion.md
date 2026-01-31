---
type: perk
skill: Life Leech Aura
category: Damage
tags: [blood, aura, corruption, conversion, damage]
status: concept
---

# Corrupted Conversion

## Overview
Transforms a portion of the Life Leech Aura's healing energy into corrupted damage that spreads through enemy networks, creating a twisted cycle of drain and destruction.

## Mechanics

### Primary Effect
- **Conversion Rate**: 25% of life leech is converted to corruption damage
- **Damage Application**: Corruption damage applied instantly to all enemies in aura
- **Healing Reduction**: Player receives 75% of original leech as healing
- **Damage Type**: Corruption damage bypasses physical resistances

### Technical Details
- **Conversion Formula**: `corruption_damage = total_leech * 0.25`
- **Healing Formula**: `actual_healing = total_leech * 0.75`
- **Damage Distribution**: Equal corruption damage to all enemies in range
- **Resistance Interaction**: Corruption damage has unique resistance calculations

## Synergies

### Simple Synergies
- **Tainted Blood**: Corruption damage amplifies existing poison effects
- **Pact of Pain**: Self-damage from pact increases total leech, boosting corruption
- **Anemic Curse**: Weakened enemies take increased corruption damage

### Complex Synergies
- **Vital Link + Corrupted Conversion**: Corruption spreads through linked networks, creating cascading damage
- **Blood Blade + Corruption**: Corrupted life force can empower blade manifestations with chaos energy
- **Hemorrhagic Shield**: Shield reflection can carry corruption properties to attackers

## Trade-offs
- **Healing Sacrifice**: 25% reduction in personal healing effectiveness
- **Mana Increase**: Corruption conversion increases aura mana cost by 15%
- **Resistance Vulnerability**: Player becomes 10% more vulnerable to corruption damage

## Implementation Details

### Corruption Mechanics
- **Damage Type System**: New damage type with unique properties
- **Visual Effects**: Dark tendrils emanating from aura, corrupt energy around enemies
- **Audio Design**: Whispers and crackling sounds accompanying corruption

### Conversion Process
- **Real-time Calculation**: Continuous conversion during aura operation
- **Priority System**: Healing applied first, then corruption damage
- **Overflow Handling**: Excess corruption can create lingering damage zones

## Advanced Interactions

### Corruption Properties
- **Soul Damage**: Corruption affects enemy mana/energy systems
- **Spreading Effect**: Corrupted enemies can infect nearby non-aura targets
- **Cumulative Buildup**: Repeated corruption exposure increases vulnerability

### Resistance Interactions
- **Chaos Resistance**: Primary defense against corruption damage
- **Holy Resistance**: Provides partial protection against corruption
- **Blood Resistance**: Ironically increases corruption vulnerability by 15%

## Corruption Evolution

### Adaptive Corruption
- **Enemy Type Learning**: Corruption becomes more effective against frequently encountered enemies
- **Resistance Bypassing**: Prolonged exposure reduces enemy corruption resistance
- **Mutation Effects**: Long-term corruption can cause permanent enemy changes

## Implementation Status
**Status**: To Do
**Priority**: High
**Dependencies**: Damage type system, corruption mechanics, Life Leech Aura base system