---
type: perk
skill: Life Leech Aura
category: Defense
tags: [blood, aura, shield, overflow, defense]
status: concept
---

# Sanguine Overflow

## Overview
When Life Leech Aura restores health beyond maximum capacity, the excess is converted into a temporary blood shield.

## Mechanics

### Primary Effect
- **Overflow Conversion**: Excess healing becomes temporary shield points
- **Shield Capacity**: Maximum shield equals 20% of maximum health
- **Shield Duration**: Temporary shield lasts 10 seconds before decay
- **Decay Rate**: Shield decays at 5% per second after duration expires

### Technical Details
- **Overflow Formula**: `shield_gain = min(excess_healing, max_health * 0.2 - current_shield)`
- **Shield Priority**: Shield absorbs damage before health
- **Visual Indicator**: Crimson aura around character intensifies with shield strength

## Synergies

### Simple Synergies
- **Blood Barrier**: Both shields stack, creating layered protection
- **Hemorrhagic Shield**: Shield damage reflection applies to Sanguine shield
- **Vital Link**: Overflow from linked targets also contributes to shield

### Complex Synergies
- **Pact of Pain + Sanguine Overflow**: Self-damage from pact can never reduce health below shield threshold
- **Tainted Blood**: Poisoned enemies provide corrupted overflow that adds poison resistance
- **Blood Blade + Health Scaling**: Higher health from blade scaling increases overflow capacity

## Trade-offs
- **Healing Efficiency**: 25% of overflow is lost in conversion process
- **Shield Fragility**: Sanguine shield is 15% less effective against magic damage
- **Dependency Risk**: Encourages aggressive positioning to maintain overflow

## Implementation Details

### Visual Effects
- Crimson energy swirling around character
- Shield intensity correlates with remaining shield points
- Distinct visual difference from other shield types

### Mechanics Integration
- Shield system integration with existing damage calculation
- Overflow detection system for healing beyond max health
- Timer system for shield duration and decay

## Advanced Mechanics

### Shield Interactions
- **Stacking Rules**: Multiple overflow instances extend duration rather than stack
- **Damage Types**: Physical damage reduces shield at normal rate, magic at 115% rate
- **Critical Hits**: Can penetrate 50% of sanguine shield on critical strikes

## Implementation Status
**Status**: To Do
**Priority**: High
**Dependencies**: Shield system, overflow healing detection, visual effect system