---
type: perk
skill: Life Leech Aura
category: Control
tags: [blood, aura, crowd-control, positioning]
status: concept
---

# Crimson Vortex

## Overview
Transform the Life Leech Aura into a gravitational force that draws enemies toward its center while draining their life force.

## Mechanics

### Primary Effect
- Enemies within the aura experience a **10-20% pull force** toward the center
- Pull strength increases with proximity to aura center
- Pull force scales with aura level and Blood affinity

### Technical Details
- **Pull Calculation**: `pull_force = base_pull * (1 - distance_from_center / aura_radius)`
- **Movement Override**: Pull force applies as velocity modifier to enemy movement
- **Resistance**: Larger enemies have natural resistance to pull effects

## Synergies

### Simple Synergies
- **Blood Blade**: Pulled enemies are more likely to hit spinning blades
- **Hemorrhagic Shield**: Concentrated enemies trigger shield effects more frequently
- **Tainted Blood**: Clustered poisoned enemies amplify toxic damage spread

### Complex Synergies
- **Vital Link + Crimson Vortex**: Linked targets create secondary pull points, forming blood constellation patterns
- **Pact of Pain**: Self-damage from pact creates explosive pull bursts every few seconds
- **Anemic Curse**: Weakened enemies become easier to pull, creating cascading crowd control

## Trade-offs
- **Energy Cost**: Pull effect increases aura's mana drain by 25%
- **Positioning Risk**: Pulling enemies closer increases danger to the player
- **Boss Resistance**: Elite enemies and bosses have 75% pull resistance

## Implementation Details

### Visual Effects
- Blood streams flowing toward aura center
- Spiral patterns of crimson energy
- Enemy movement trails showing pull vectors

### Audio Cues
- Subtle whooshing sound as enemies are drawn in
- Intensity increases with number of affected enemies

## Implementation Status
**Status**: To Do
**Priority**: Medium
**Dependencies**: Life Leech Aura base system, enemy movement override system