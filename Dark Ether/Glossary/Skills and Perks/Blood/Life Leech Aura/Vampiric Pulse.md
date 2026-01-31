---
type: perk
skill: Life Leech Aura
category: Rhythm
tags: [blood, aura, pulse, vampiric, rhythm]
status: concept
---

# Vampiric Pulse

## Overview
The Life Leech Aura develops a rhythmic heartbeat, doubling its leech effectiveness for 1 second every 3 seconds, creating powerful healing bursts synchronized with combat rhythm.

## Mechanics

### Primary Effect
- **Pulse Timing**: Every 3 seconds, trigger a 1-second pulse of enhanced leech
- **Leech Multiplier**: During pulse, life leech effectiveness doubles (200% rate)
- **Pulse Duration**: Enhanced leech lasts exactly 1 second
- **Rhythm Consistency**: Pulse timing is consistent regardless of combat state

### Technical Details
- **Pulse Formula**: `enhanced_leech = base_leech * 2.0`
- **Timer System**: 3-second countdown with 1-second enhanced window
- **Stacking Rules**: Pulse enhancement stacks multiplicatively with other bonuses
- **Visual Indication**: Aura pulses with crimson energy during enhanced periods

## Synergies

### Simple Synergies
- **Sanguine Overflow**: Pulse bursts are more likely to create overflow shields
- **Bleeding Resonance**: Enhanced leech during pulse amplifies bleed stack bonuses
- **Toxic Symbiosis**: Pulse timing synchronizes with regeneration siphoning for maximum effect

### Complex Synergies
- **Vital Link + Vampiric Pulse**: Pulse synchronizes across all linked targets, creating network-wide healing waves
- **Pact of Pain**: Can time self-damage to coincide with pulse for maximum recovery
- **Burst Consumption**: Pulse periods contribute disproportionately to burst accumulation

## Trade-offs
- **Timing Dependency**: Maximum effectiveness requires understanding pulse rhythm
- **Predictable Pattern**: Enemies may adapt to predictable pulse timing
- **Base Efficiency**: Non-pulse periods have 10% reduced leech to balance the enhancement

## Implementation Details

### Pulse Mechanics
- **Timer Precision**: High-precision timing system for consistent 3-second intervals
- **Visual Feedback**: Clear indicators for pulse prediction and activation
- **Audio Cues**: Heartbeat sound effect synchronized with pulse rhythm

### Combat Integration
- **Rhythm Training**: Visual and audio cues help players learn pulse timing
- **Strategic Planning**: Players can plan aggressive moves around pulse windows
- **Emergency Timing**: Pulse can be briefly delayed by 0.5 seconds through skill activation

## Advanced Interactions

### Pulse Enhancement
- **Critical Pulse**: 15% chance for triple leech instead of double
- **Extended Pulse**: Certain conditions can extend pulse duration to 1.5 seconds
- **Synchronized Pulse**: Multiple Vampiric Pulse sources can synchronize for amplified effects

### Rhythm Variations
- **Combat Tempo**: Pulse speed can increase by 10% during intense combat
- **Health-Based Timing**: Pulse frequency increases when at low health
- **Resonance Matching**: Pulse can synchronize with other rhythmic abilities

## Tactical Applications

### Combat Timing
- **Aggressive Windows**: Use pulse periods for risky positioning
- **Recovery Planning**: Time retreats to coincide with pulse healing
- **Combo Integration**: Synchronize other abilities with pulse timing

### Strategic Positioning
- **Pulse Positioning**: Move into optimal position before pulse activation
- **Area Control**: Use pulse predictability to control enemy movement
- **Team Coordination**: Coordinate with allies around pulse timing

## Implementation Status
**Status**: To Do
**Priority**: Medium
**Dependencies**: Timer system, Life Leech Aura base mechanics, visual/audio feedback systems