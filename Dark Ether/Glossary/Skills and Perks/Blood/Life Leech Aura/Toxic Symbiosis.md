---
type: perk
skill: Life Leech Aura
category: Synergy
tags: [blood, aura, poison, regeneration, symbiosis]
status: concept
---

# Toxic Symbiosis

## Overview
Creates a symbiotic relationship between the Life Leech Aura and poisoned enemies, allowing the aura to siphon their natural regeneration while they suffer from toxic effects.

## Mechanics

### Primary Effect
- **Regeneration Siphon**: Life Leech Aura gains 50% of poisoned enemies' regeneration rate
- **Symbiotic Efficiency**: Siphoned regeneration is added to base leech amount
- **Poison Requirement**: Only affects enemies currently suffering from poison effects
- **Continuous Transfer**: Regeneration siphon occurs every second while poison persists

### Technical Details
- **Siphon Formula**: `bonus_leech = enemy_regen_rate * 0.5 * poison_potency_modifier`
- **Poison Detection**: Continuous monitoring of poison debuffs on enemies in range
- **Regeneration Calculation**: Based on enemy's natural and enhanced regeneration rates

## Synergies

### Simple Synergies
- **Tainted Blood**: Direct poison application enables immediate symbiosis
- **Blood Blade**: Poisoned blade attacks create symbiotic targets
- **Anemic Curse**: Weakened enemies may have altered regeneration patterns

### Complex Synergies
- **Vital Link + Toxic Symbiosis**: Linked targets share regeneration siphoning across the network
- **Pact of Pain**: Self-poison from corrupted pacts can contribute to symbiosis pool
- **Hemorrhagic Shield + Tainted**: Shield damage applies poison, creating defensive regeneration

## Trade-offs
- **Poison Dependency**: Requires external poison sources to function effectively
- **Enemy Type Limitation**: Only affects enemies with natural regeneration abilities
- **Diminishing Returns**: Each additional poisoned enemy provides 10% less benefit

## Implementation Details

### Symbiosis Mechanics
- **Detection System**: Real-time poison and regeneration monitoring
- **Transfer Rate**: Smooth regeneration transfer over time
- **Visual Indicators**: Green-tinted leech streams from poisoned enemies

### Poison Integration
- **Universal Compatibility**: Works with any poison source or type
- **Potency Scaling**: Stronger poisons provide better regeneration transfer
- **Duration Independence**: Symbiosis active as long as poison persists

## Advanced Interactions

### Regeneration Types
- **Natural Regeneration**: Base enemy healing over time
- **Enhanced Regeneration**: Buffed or magical healing effects  
- **Corrupted Regeneration**: Twisted healing that may provide unique benefits

### Symbiotic Evolution
- **Adaptation Bonus**: Prolonged symbiosis increases efficiency by 1% per 10 seconds
- **Toxic Immunity**: Eventually become immune to poison damage from symbiotic sources
- **Regeneration Mastery**: Learn to replicate siphoned regeneration patterns

## Environmental Considerations

### Poison Sources
- **Skill-Based**: Tainted Blood, poisoned weapons, toxic abilities
- **Environmental**: Poison clouds, toxic terrain, corrupted areas
- **Enemy-Applied**: Enemies that poison themselves or allies

## Implementation Status
**Status**: To Do
**Priority**: Medium
**Dependencies**: Poison system, regeneration mechanics, Life Leech Aura base system