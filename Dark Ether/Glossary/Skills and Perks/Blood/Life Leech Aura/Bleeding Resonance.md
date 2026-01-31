---
type: perk
skill: Life Leech Aura
category: Enhancement
tags: [blood, aura, bleed, synergy, stacking]
status: concept
---

# Bleeding Resonance

## Overview
The Life Leech Aura resonates with bleeding wounds, increasing its drain effectiveness based on the number of bleed stacks affecting enemies within range.

## Mechanics

### Primary Effect
- **Resonance Bonus**: +0.5% life leech per bleed stack on enemies within aura
- **Maximum Bonus**: +5% total life leech (capped at 10 bleed stacks)
- **Stack Counting**: All bleed effects on all enemies within aura contribute to bonus
- **Real-time Calculation**: Bonus updates instantly as bleed stacks change

### Technical Details
- **Bonus Formula**: `leech_bonus = min(total_bleed_stacks * 0.005, 0.05)`
- **Stack Detection**: Continuous monitoring of debuff states on enemies in range
- **Efficiency Scaling**: Bonus applies multiplicatively to base leech rate

## Synergies

### Simple Synergies
- **Blood Blade**: Blade attacks can apply bleed, feeding into resonance bonus
- **Hemorrhagic Shield**: Shield damage can cause bleeding, creating feedback loop
- **Anemic Curse**: Curse can amplify existing bleed effects

### Complex Synergies
- **Vital Link + Bleeding Resonance**: Linked targets share bleed stacks, multiplying resonance across the network
- **Tainted Blood + Bleeding**: Poisoned bleeding enemies provide dual resonance (bleed + poison interaction)
- **Pact of Pain**: Self-inflicted damage can apply bleed to self, contributing to resonance when near other bleeding enemies

## Trade-offs
- **Dependency**: Effectiveness requires other sources of bleed application
- **Positioning**: Must maintain proximity to bleeding enemies for maximum benefit
- **Diminishing Returns**: Limited maximum bonus prevents infinite scaling

## Implementation Details

### Resonance Mechanics
- **Detection Range**: Same as Life Leech Aura range
- **Update Frequency**: Real-time monitoring with 60fps update rate
- **Visual Feedback**: Aura intensity increases with resonance level

### Bleed Stack Integration
- **Universal Detection**: Works with any source of bleed effect
- **Stack Quality**: Different bleed sources may have different resonance values
- **Duration Independence**: Resonance based on current stacks, not duration

## Advanced Interactions

### Bleed Source Compatibility
- **Weapon Bleeds**: Standard 1.0x resonance value
- **Skill Bleeds**: Enhanced 1.2x resonance value
- **Environmental Bleeds**: Reduced 0.8x resonance value

### Resonance Cascade Effects
- **Threshold Bonuses**: Every 5 stacks unlocks additional resonance effects
- **Critical Resonance**: At maximum stacks, chance for double leech pulses
- **Resonance Overflow**: Excess resonance can extend to nearby non-bleeding enemies

## Implementation Status
**Status**: To Do
**Priority**: Medium
**Dependencies**: Bleed system, debuff tracking, Life Leech Aura base mechanics