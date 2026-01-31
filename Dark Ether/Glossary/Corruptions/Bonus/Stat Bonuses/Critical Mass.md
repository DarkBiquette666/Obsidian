---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [critical_mass, critical, chance, damage, precision]
status: implemented
rarity: varies
---

# Critical Mass

## Description
A precision corruption that increases critical hit chances and critical damage. This corruption concentrates destructive energy toward vital points, allowing strikes of devastating precision and power.

## Lore
In the Dark Ether, the notion of "critical point" transcends simple anatomy. This corruption reveals the dimensional flaws present in every living being, these nexuses of vulnerability where energy can concentrate for devastating effects. The bearer develops a supernatural perception of these weak points, transforming each attack into a potentially fatal surgical strike.

## Statistics

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Bonus Corruption | Positive effect |
| **Category** | Stat Bonuses | Stat bonuses |
| **Base Class** | CorruptionStatReward | Stat bonus |
| **Duration** | Permanent | As long as corruption is active |
| **Style** | Critical | Critical specialization |
| **Focus** | Precision Strikes | Precision strikes |

## Critical Mass Mechanics

### Optimized Critical System
| Property | Details | Notes |
|----------|---------|-------|
| **Critical Chance** | +0.3-0.7% | Variable according to tier |
| **Critical Damage** | +20-30% | Variable according to tier |
| **Synergy** | Chance + Power | Double improvement |
| **Application** | Universal | All attack types |
| **Stacking** | With other crit | Cumulative |

### Critical Efficiency Calculation
```
Crit_Chance_Final = Base_Crit + Critical_Mass_Chance
Crit_Damage_Final = Base_Crit_Damage + Critical_Mass_Damage
DPS_Bonus = (Crit_Chance × Crit_Damage_Multiplier)
```

## Tier System

### Values by Tier
| Tier | Critical Chance | Critical Damage | Combined Efficiency |
|------|-----------------|-----------------|-------------------|
| **Minor** | +0.3% | +20% | Modest |
| **Moderate** | +0.4% | +22% | Solid |
| **Major** | +0.5% | +25% | Good |
| **Epic** | +0.6% | +27% | Very good |
| **Legendary** | +0.7% | +30% | Excellent |

### Tier Color Code
- **White**: +0.3% chance, +20% damage
- **Green**: +0.4% chance, +22% damage
- **Blue**: +0.5% chance, +25% damage
- **Purple**: +0.6% chance, +27% damage
- **Gold**: +0.7% chance, +30% damage

## Strategic Advantages

**Strengths:**
- Optimized double critical bonus
- Exceptional synergy with other crit
- Improves burst damage
- Universal on all builds
- Excellent multiplicative scaling
- Solid foundation for critical builds

**Exceptional Synergies:**
- **Silent Blade**: Triple critical stack
- **Fortunian's Eye**: Extreme critical chance
- **Echo Chamber**: Double critical chances
- **Dark Power**: Critical + global damage
- **High-damage Skills**: Maximizes impact

## Tactical Applications

### Specialized Critical Builds
- Core corruption for critical builds
- Foundation for assassin builds
- Excellent for single-target

### Generalist Builds
- Solid improvement for all builds
- Increases burst potential
- Excellent risk/reward ratio

### Cross-Corruption Synergies
- **With Silent Blade**: Intense critical stack
- **With Fortunian's Eye**: Massive critical chance
- **With Echo Chamber**: Double critical potential
- **With Dark Power**: Global damage + critical

## Balance Considerations

### Balancing Mechanics
- Moderate bonuses to avoid overpowered
- Balanced chance/damage scaling
- More effective on high base damage
- Dependent on chance (RNG factor)

### Impact on Progression
- Significantly improves burst DPS
- More effective with weapon/skill scaling
- Excellent for boss encounters
- Foundation for advanced critical builds

## Technical Implementation

### Source Files
- **Corruption**: `critical_mass_bonus.tres`
- **Script**: `corruption_stat_reward.gd`
- **Stats**: Critical chance + critical damage

### System Integration
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [
    StatType.CRITICAL_CHANCE,
    StatType.CRITICAL_DAMAGE
]
values = [tier_crit_chance, tier_crit_damage]
```

### Technical Values
- **Critical Chance**: Percentage value (0.3-0.7)
- **Critical Damage**: Percentage value (20-30)

## Acquisition Strategies

### Priority by Build
- **High Priority**: Critical builds, assassins, burst damage
- **Medium Priority**: Balanced builds, generalists
- **Low Priority**: DoT builds, pure support

### Optimal Timing
- **Early Game**: Good if available
- **Mid Game**: Excellent for progression
- **Late Game**: Essential for critical builds

## Risks and Trade-offs

### Limitations
- Dependent on chance (RNG)
- More effective on high base damage
- Scaling with equipment
- Less visible on fast, low-damage

### Optimal Management
- Combine with high-damage weapons
- Stack with other critical corruptions
- Focus on single-target encounters
- Optimize for burst moments

## Interaction with Other Systems

### Combat System
- Improves all attack types
- Synergy with weapon scaling
- Compatible with skill systems
- Multiplicative with damage bonuses

### Chance System
- Cumulates with base critical stats
- Compatible with luck mechanics
- Synergy with proc-based effects
- Stack with critical gear

## Recommended Builds

### Critical Master
```
Core: Critical Mass + Silent Blade + Fortunian's Eye
Style: Maximum critical potential
Focus: Burst damage optimization
```

### Balanced Striker
```
Core: Critical Mass + Echo Chamber + Dark Power
Style: Critical with versatility
Focus: Consistent performance
```

### Speed Critic
```
Core: Critical Mass + Time Distortion + Battle Frenzy
Style: Fast critical strikes
Focus: High-frequency critiques
```

## Related

- [[Corruptions]] - Main system
- [[Critical System]] - Critical mechanism
- **Synergies**: [[Silent Blade]], [[Fortunian's Eye]], [[Echo Chamber]]
- [[Critical Chance]] - Critical probability
- [[Critical Damage]] - Critical damage
- [[Stat Bonuses]] - Category
- [[Burst Damage]] - Damage style

---

**Implementation**: `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\critical_mass_bonus.tres`