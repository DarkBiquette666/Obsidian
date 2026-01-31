---
type: perk
skill: Life Leech Aura
category: Persistent
tags: [blood, aura, necrotic, field, death, persistent]
status: concept
---

# Necrotic Field

## Overview
When enemies die within the Life Leech Aura, their death creates stationary zones of necrotic energy that continue to provide life leech to anyone standing within them.

## Mechanics

### Primary Effect
- **Death Trigger**: Enemy death within aura creates a necrotic field at death location
- **Field Duration**: Necrotic fields persist for 5 seconds after enemy death
- **Leech Rate**: Fields provide 2% life leech per second to anyone within their radius
- **Field Radius**: 2-meter radius around death location

### Technical Details
- **Field Creation**: `create_field(death_position, field_radius, duration)`
- **Leech Formula**: `field_leech = 0.02 * player_max_health`
- **Multiple Fields**: Fields stack additively up to maximum of 5 concurrent fields
- **Visual Indicator**: Dark crimson pools with subtle particle effects

## Synergies

### Simple Synergies
- **Crimson Vortex**: Pulled enemies more likely to die near each other, creating overlapping fields
- **Burst Consumption**: Burst kills create multiple fields simultaneously
- **Vampiric Pulse**: Pulse timing can be used strategically to maximize field benefit

### Complex Synergies
- **Vital Link + Necrotic Field**: Linked enemy deaths can create fields at both death location and link origin point
- **Toxic Symbiosis**: Poisoned enemy deaths create toxic necrotic fields with additional poison resistance
- **Corrupted Conversion**: Corrupted deaths create enhanced necrotic fields with 3% leech rate

## Trade-offs
- **Positioning Requirement**: Must stand within field radius to benefit from leech
- **Limited Duration**: Fields have short 5-second lifespan requiring constant movement
- **Death Dependency**: Effectiveness depends on enemy kill rate within aura

## Implementation Details

### Field Mechanics
- **Spatial System**: Ground-based area effect system with precise positioning
- **Duration Tracking**: Timer system for individual field lifespans
- **Stack Management**: System to track and manage multiple overlapping fields

### Visual Design
- **Ground Effects**: Dark pools of blood with swirling necrotic energy
- **Particle Systems**: Subtle wisps of dark energy rising from fields
- **Visual Feedback**: Field intensity indicates remaining duration

## Advanced Interactions

### Field Enhancement
- **Elite Deaths**: Elite enemy deaths create larger fields (3-meter radius)
- **Boss Deaths**: Boss deaths create permanent necrotic zones until area exit
- **Critical Deaths**: 20% chance for enhanced fields with 3% leech rate

### Field Evolution
- **Field Merging**: Overlapping fields can merge into larger, more potent zones
- **Necrotic Spread**: Long-lasting fields can slowly expand over time
- **Field Resonance**: Multiple fields near each other create resonance bonuses

## Environmental Integration

### Terrain Interaction
- **Surface Adaptation**: Fields adapt to different terrain types (water, stone, dirt)
- **Elevation Effects**: Fields on elevated terrain have slightly larger radius
- **Environmental Hazards**: Fields can interact with environmental damage sources

### Strategic Applications
- **Area Control**: Use fields to control enemy movement and positioning
- **Healing Stations**: Create temporary healing zones during intense combat
- **Tactical Retreats**: Fields provide safe zones for brief recovery periods

## Implementation Status
**Status**: To Do
**Priority**: Medium
**Dependencies**: Spatial field system, death event tracking, Life Leech Aura integration