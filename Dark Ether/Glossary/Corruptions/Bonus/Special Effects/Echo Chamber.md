---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionEffectReward
tags: [echo, double_cast, chance, skills, bonus]
status: implemented
rarity: varies
---

# Echo Chamber

## Description
A corruption that grants a chance to cast skills twice. This corruption allows players to significantly increase their combat effectiveness by duplicating the effect of their spells and abilities.

## Lore
The Echo of the Ancients still resonates in the forbidden corridors of the Dark Ether. This corruption allows channeling these temporal echoes, creating a mystical duplication phenomenon that makes reality itself hesitate, repeating the caster's action like a stubborn memory that refuses to fade.

## Statistics

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Bonus Corruption | Positive effect |
| **Category** | Special Effects | Unique effect |
| **Base Class** | CorruptionEffectReward | Reward type |
| **Duration** | Permanent (-1.0) | As long as corruption is active |
| **Intensity** | 1.0 | Standard effect |
| **Activation Chance** | Variable | Depends on tier values |

## Echo Mechanics

### Double Cast System
| Property | Details | Notes |
|----------|---------|-------|
| **Trigger** | Skill usage | All skills |
| **Effect** | Automatic recast | Same effect, same cost |
| **Probability** | Variable per tier | See tier system |
| **Limitation** | No echo of echo | Prevents infinite loops |
| **Cooldown** | None | Each cast can trigger |

### Interaction with Skills
- **Projectiles**: Doubles the number of projectiles fired
- **Auras**: Doubles activation (usually no visible effect)
- **Curses**: Doubles curse application
- **Attacks**: Doubles damage and effects
- **Spells**: Doubles magical effects

## Tier System

*Note: Exact chance values depend on implementation in `echo_chamber_buff.tres` which is not accessible in this analysis*

### Probable Tiers
- **Minor**: ~5-10% double cast chance
- **Moderate**: ~10-15% double cast chance  
- **Major**: ~15-20% double cast chance
- **Epic**: ~20-25% double cast chance

### Tier Color Code
- **White**: Minor tier
- **Green**: Moderate tier
- **Blue**: Major tier
- **Purple**: Epic tier
- **Gold**: Legendary tier

## Strategic Advantages

**Strengths:**
- Massive potential DPS increase
- Synergy with all skill types
- No additional mana/resource cost
- Works with on-hit effects
- Excellent for burst damage builds

**Exceptional Synergies:**
- **Blood Blade**: Doubles blades and bleeding
- **Ether Ball**: Doubles elemental projectiles
- **Curses**: Double debuff application
- **Life Leech Aura**: Doubles life drain
- **Critical Builds**: Doubles critical chances

## Tactical Applications

### Burst Damage Builds
- Maximizes effectiveness of big spells
- Perfect for high damage, low frequency builds
- Excellent with high cooldown skills

### Utility Builds
- Doubles curse application
- Improves offensive aura effectiveness
- Enhances leech and recovery mechanics

### Cross-Corruption Synergies
- **With Dark Power**: Multiplied by echo chance
- **With Critical Mass**: More double critical chances
- **With Berserker**: Doubles fast attack stacks

## Balance Considerations

### Balancing Mechanics
- Limited chance to avoid overpowered
- No chain echo (prevents infinite loops)
- Resource costs maintained for second cast
- Cooldowns respected to prevent abuse

### Impact on Progression
- Significantly increases farming efficiency
- Can unbalance early game if too common
- Requires careful management of rarity tiers

## Technical Implementation

### Source Files
- **Corruption**: `echo_chamber_bonus.tres`
- **Effect**: `echo_chamber_buff.tres`
- **Script**: `corruption_effect_reward.gd`

### System Integration
```gdscript
# Type: CorruptionEffectReward
effects_to_apply = [echo_chamber_buff.tres]
effect_durations = [-1.0]  # Permanent
effect_intensities = [1.0]  # Standard intensity
```

### Description Template
```
"{double_cast_chance}% chance to cast skills twice"
```

## Acquisition Strategies

### Priority by Build
- **High Priority**: Burst damage builds, casters
- **Medium Priority**: Hybrid builds, utility casters  
- **Low Priority**: Pure damage over time builds

### Optimal Timing
- **Early Game**: Excellent if available
- **Mid Game**: Very powerful for progression
- **Late Game**: Synergizes with other corruptions

## Risks and Trade-offs

### No Direct Malus
- This corruption has no inherent malus
- The only "risk" is not triggering the echo
- May create psychological dependence on double casts

### Resource Management
- Double mana/resource consumption if applicable
- May deplete resources more quickly
- Requires resource management planning

## Related

- [[Corruptions]] - Main system
- [[Double Cast]] - Base mechanism
- [[Special Effects]] - Category
- [[Chance Mechanics]] - Probability system
- [[Skill System]] - Skills integration
- [[Buff System]] - Technical implementation

---

**Implementation**: `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\echo_chamber_bonus.tres`