---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionStatReward
tags: [shadow_clone, clone, duplicate, chance, assistance]
status: implemented
rarity: varies
---

# Shadow Clone

## Description
A summoning corruption that periodically creates a shadow clone that attacks with the bearer. This corruption manifests the bearer's dark essence in the form of a spectral double that reproduces their offensive actions.

## Lore
The Dark Ether never forgets the souls that traverse it, keeping in memory the spiritual imprint of each being. This corruption exploits this mystical property, allowing the bearer to temporarily manifest their own shadowed reflection. This spectral clone is not a simple illusion, but a crystallized soul fragment that retains the combat capabilities of the original, creating a tangible echo of violence that strikes in perfect synchronization with its creator.

## Statistics

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Bonus Corruption | Positive effect |
| **Category** | Special Effects | Unique effect |
| **Base Class** | CorruptionStatReward | Conditional bonus |
| **Duration** | Permanent | As long as corruption is active |
| **Trigger** | 15% chance | Per attack/cast |
| **Clone Duration** | Temporary | Limited duration |

## Clone Mechanics

### Shadow Manifestation System
| Property | Details | Notes |
|----------|---------|-------|
| **Spawn Chance** | 15% fixed | Per attack/spell |
| **Clone Duration** | Variable | According to implementation |
| **Clone Abilities** | Mirror player | Copies abilities |
| **Clone Damage** | Full power | Identical damage |
| **Clone Behavior** | Aggressive | Attacks automatically |

### Clone Action Calculation
```
Per_Attack_Or_Cast:
    If Random(1-100) <= 15:
        Spawn_Shadow_Clone()
        Clone_Mimics_Player_Actions()
        Clone_Duration = Fixed_Time
```

## Power System

### Clone Capabilities (Estimated)
| Aspect | Clone Performance | Notes |
|--------|------------------|-------|
| **Damage Output** | 100% of player | Full power |
| **Attack Speed** | Match player | Synchronized |
| **Abilities** | Mirror current | Copies active skills |
| **Duration** | 5-10 seconds | Temporary |
| **AI Behavior** | Aggressive | Auto-target enemies |

### Efficiency by Build
- **High Attack Rate**: More spawn chances
- **Burst Damage**: Clone effective during duration
- **Sustained DPS**: Significant increase
- **AoE Builds**: Clone doubles zone coverage

## Strategic Advantages

**Strengths:**
- Significant DPS increase
- Chance-based (excitement factor)
- Clone with full power
- Synergy with all offensive builds
- Temporary ally for assistance
- Combat effectiveness multiplier

**Exceptional Synergies:**
- **High Attack Speed**: More trigger chances
- **Echo Chamber**: More attacks = more clones
- **Critical Builds**: Clone can also critical hit
- **AoE Abilities**: Clone doubles coverage
- **Burst Builds**: Clone maximizes damage windows

## Tactical Applications

### High-Frequency Builds
- Excellent for fast attack builds
- More attacks = more clone chances
- Synergy with attack speed bonuses

### Burst Damage Builds
- Clone amplifies damage windows
- Temporary but significant DPS boost
- Excellent for boss encounters

### Cross-Corruption Synergies
- **With Echo Chamber**: More actions = more clones
- **With Time Distortion**: More speed = more triggers
- **With Critical Mass**: Clone can also critical hit
- **With Battle Frenzy**: Optimal speed stacking

## Balance Considerations

### Balancing Mechanics
- Chance-based activation (15% only)
- Temporary clone (not permanent)
- Full power but limited duration
- Requires active combat to trigger

### Impact on Progression
- Significant DPS boost when active
- More effective with high activity builds
- Temporary nature prevents overpowered
- Excitement factor improves gameplay

## Technical Implementation

### Source Files
- **Corruption**: `shadow_clone_bonus.tres`
- **Script**: `corruption_stat_reward.gd`
- **Template**: Fixed description

### System Integration
```gdscript
# Type: CorruptionStatReward
# Triggered on attack/cast actions
description_template = "15% chance to create a clone that attacks with you"
trigger_chance = 15.0
clone_duration = fixed_time
clone_power = 100% # Full player power
```

## Acquisition Strategies

### Priority by Build
- **High Priority**: High attack rate, DPS builds, active combat
- **Medium Priority**: Balanced builds, frequent actions
- **Low Priority**: Passive builds, low action frequency

### Optimal Timing
- **Early Game**: Excellent DPS boost
- **Mid Game**: Significant combat advantage
- **Late Game**: Powerful multiplier

## Risks and Trade-offs

### Limitations
- Chance-based (not guaranteed)
- Temporary clone only
- Requires active engagement
- More effective with high action frequency

### Optimal Management
- Focus on high attack/cast frequency
- Combine with speed bonuses
- Use during sustained combat
- Maximize action count per encounter

## Interaction with Other Systems

### Action Systems
- Triggered by all offensive actions
- Compatible with all attack/cast types
- More actions = more opportunities
- Synergy with speed systems

### Damage Systems
- Clone mirrors player capabilities
- Full damage scaling applied
- Compatible with all damage bonuses
- Multiplicative effect on DPS

## Tactical Applications

### Combat Burst Windows
- Clone provides temporary DPS spike
- Excellent pour critical moments
- Boss fight advantage
- Overwhelming enemy positioning

### Sustained Combat
- Regular clone spawns during long fights
- Cumulative advantage over time
- More effective avec sustained engagement
- Pressure multiplication

## Recommended Builds

### Shadow Warrior
```
Core: Shadow Clone + Time Distortion + Echo Chamber
Style: High action frequency
Focus: Maximum clone spawn rate
```

### Critical Shadow
```
Core: Shadow Clone + Critical Mass + Silent Blade
Style: Critical burst with clone
Focus: Maximum damage windows
```

### Speed Clone
```
Core: Shadow Clone + Battle Frenzy + Lesharii's Grace
Style: Fast actions, frequent clones
Focus: Speed and multiplication
```

## Clone Mechanics Details

### Spawn Conditions
- Every attack or cast action rolls 15%
- Clone spawns at player location
- Immediately begins attacking nearby enemies
- Inherits player's current abilities

### Clone Behavior
- Aggressive AI targeting
- Mimics player attack patterns
- Full damage potential
- Temporary duration limitation

## Related

- [[Corruptions]] - Main system
- [[Clone Mechanics]] - Clone mechanics
- **Synergies**: [[Echo Chamber]], [[Time Distortion]], [[Critical Mass]]
- [[Temporary Allies]] - Temporary allies
- [[Chance Mechanics]] - Chance mechanics
- [[Special Effects]] - Category
- [[DPS Multiplication]] - Damage multiplication

---

**Implementation**: `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\shadow_clone_bonus.tres`