---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionStatReward
tags: [gravity_well, pull, positioning, crowd_control, gravity]
status: implemented
rarity: varies
---

# Gravity Well

## Description
A gravitational corruption that automatically attracts enemies toward the bearer. This corruption creates a mystical gravitational field, transforming the bearer into an attraction nexus that manipulates the position of adversaries.

## Lore
In the Dark Ether, gravity does not obey conventional physical laws - it responds to will and emotion. This corruption exploits this anomaly, transforming the bearer into a living gravitational well. Every enemy within a certain radius feels an irresistible attraction, as if the bearer's corrupted soul had become so dense that it warped space-time around it, creating an invisible vortex that inexorably draws all life toward its center.

## Statistics

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Bonus Corruption | Positive effect |
| **Category** | Special Effects | Unique effect |
| **Base Class** | CorruptionStatReward | Conditional bonus |
| **Duration** | Permanent | As long as corruption is active |
| **Effect** | Continuous Pull | Constant attraction |
| **Range** | {pull_radius} units | Variable according to tier |

## Gravitational Mechanics

### Attraction System
| Property | Details | Notes |
|----------|---------|-------|
| **Pull Radius** | {pull_radius} units | Variable according to tier |
| **Pull Strength** | Constant | Fixed attraction force |
| **Target** | All enemies | All enemies in range |
| **Frequency** | Continuous | Permanent effect |
| **Override** | Enemy movement | Forces approach |

### Attraction Calculation
```
If Enemy_Distance <= Pull_Radius:
    Apply_Pull_Force_Toward_Player()
    Enemy_Movement = Forced_Toward_Player
Pull_Strength = Constant (overrides enemy movement)
```

## Tier System

### Values by Tier (Estimated)
| Tier | Pull Radius | Effectiveness | Tactical Impact |
|------|-------------|---------------|----------------|
| **Minor** | 3-4 units | Moderate | Good |
| **Moderate** | 4-5 units | Solid | Very good |
| **Major** | 5-6 units | Important | Excellent |
| **Epic** | 6-7 units | Major | Powerful |
| **Legendary** | 7-8 units | Exceptional | Dominant |

### Tier Color Code
- **White**: 3-4 units radius
- **Green**: 4-5 units radius
- **Blue**: 5-6 units radius
- **Purple**: 6-7 units radius
- **Gold**: 7-8 units radius

## Strategic Advantages

**Strengths:**
- Automatic positioning control
- Groups enemies for AoE
- Improves attack efficiency
- Prevents enemy escape
- Exceptional synergy with AoE
- Constant tactical advantage

**Exceptional Synergies:**
- **Storm Caller**: Pull + lightning AoE
- **Chain Reaction**: Grouped enemies = chain explosions
- **AoE Skills**: More grouped enemies
- **Melee Builds**: Enemies come to you
- **Area Damage**: Efficiency multiplier

## Tactical Applications

### Specialized AoE Builds
- Core corruption for AoE builds
- Maximizes area attack efficiency
- Automatically groups targets

### Control Builds
- Excellent for crowd control
- Prevents enemy dispersion
- Forces close engagement

### Cross-Corruption Synergies
- **With Storm Caller**: Lightning + optimal grouping
- **With Chain Reaction**: Grouped explosions
- **With Area Skills**: Maximum effectiveness
- **With Melee Builds**: Forced engagement

## Balance Considerations

### Balancing Mechanics
- Limited range (not global)
- Constant pull (no burst)
- Forces melee engagement
- Can be dangerous (too many enemies)

### Impact on Progression
- Transforms tactical positioning
- Drastically improves AoE builds
- Can create dangerous situations
- Requires playstyle adaptation

## Technical Implementation

### Source Files
- **Corruption**: `gravity_well_bonus.tres`
- **Script**: `corruption_stat_reward.gd`
- **Template**: Description with dynamic radius

### System Integration
```gdscript
# Type: CorruptionStatReward
# Continuous area effect
description_template = "Enemies within {pull_radius} units are drawn towards you"
effect_type = CONTINUOUS_PULL
pull_radius = tier_radius_value
```

### Template Variables
- `{pull_radius}`: Attraction radius (ex: 5.0 for 5 units)

## Acquisition Strategies

### Priority by Build
- **High Priority**: AoE builds, melee builds, area specialists
- **Medium Priority**: Hybrid builds, crowd controllers
- **Low Priority**: Ranged kiting builds, single-target focused

### Optimal Timing
- **Early Game**: Excellent for grouping
- **Mid Game**: Transformer for AoE builds
- **Late Game**: Essential for area mastery

## Risks and Trade-offs

### Limitations and Dangers
- Forces close engagement
- Can group too many enemies (dangerous)
- Incompatible with kiting builds
- Requires strong defenses

### Risk Management
- Combine with defensive corruptions
- Ensure adequate health/armor
- Use with controlled engagement
- Avoid if glass cannon build

## Interaction with Other Systems

### Position Systems
- Override enemy movement patterns
- Forces tactical positioning changes
- Creates new combat dynamics
- Enables new strategic options

### Area Systems
- Maximizes AoE effectiveness
- Concentrates damage potential
- Enables area combos
- Multiplicative with area skills

## Tactical Applications

### AoE Optimization
- Groups enemies for maximum AoE damage
- Enables efficient area clearing
- Multiplicative effect with area abilities
- Consistent enemy positioning

### Engagement Control
- Prevents enemy escape
- Forces close-range combat
- Controls battlefield positioning
- Enables aggressive strategies

## Recommended Builds

### Gravity Master
```
Core: Gravity Well + Storm Caller + Chain Reaction
Style: Area control with AoE damage
Focus: Maximum grouped enemy damage
```

### Melee Magnet
```
Core: Gravity Well + Corrupted Endurance + Critical Mass
Style: Forced melee engagement
Focus: Tank that pulls enemies in
```

### AoE Controller
```
Core: Gravity Well + Echo Chamber + Elemental Resonance
Style: Area spell mastery
Focus: Grouped magical devastation
```

## Positioning Strategies

### Optimal Positioning
- Center of enemy groups
- Near chokepoints for control
- Strategic retreats to group pursuers
- Defensive positions with pull advantage

### Risk Management
- Ensure escape routes
- Monitor enemy density
- Balance aggression with safety
- Coordinate with defensive abilities

## Related

- [[Corruptions]] - Main system
- [[Positioning]] - Position control
- **Synergies**: [[Dark Ether/Glossary/Corruptions/Bonus/Special Effects/Storm Caller]], [[Chain Reaction]], [[AoE Skills]]
- [[Crowd Control]] - Crowd control
- [[Area of Effect]] - Area of effect
- [[Special Effects]] - Category
- [[Tactical Positioning]] - Tactical positioning

---

**Implementation**: `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\gravity_well_bonus.tres`