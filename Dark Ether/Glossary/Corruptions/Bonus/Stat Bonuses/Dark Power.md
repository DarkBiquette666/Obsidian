---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: StatModifierReward
tags: [damage, global, power, legendary, scaling]
status: implemented
rarity: tier_based
---

# Dark Power

## Description
A corruption of pure power that increases all types of damage dealt. This corruption channels the raw energy of the Dark Ether to significantly amplify the bearer's destructive capacity, transforming every attack into a manifestation of absolute power.

## Lore
Dark Power is the very essence of domination in the Dark Ether. This corruption allows direct tapping into the corrupted energy reservoirs that permeate this dimension, transforming the bearer into a conduit of pure destruction. The stronger the corruption, the deeper and more dangerous the connection to these primordial energies becomes.

## Statistics

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Bonus Corruption | Positive effect |
| **Category** | Global Damage | Universal multiplier |
| **Base Class** | StatModifierReward | Stat modifier |
| **Affected Stat** | GLOBAL_DAMAGE | All damage types |
| **Value Type** | MULTIPLIER | Multiplicative percentage |

## Tier System

### Tier Progression
| Tier | Damage Bonus | Rarity | Color | Weight |
|------|-------------|--------|-------|--------|
| **Minor** | 10% | Common | White | 10.0 |
| **Moderate** | 15% | Rare | Green | 5.0 |
| **Major** | 20% | Epic | Blue | 2.0 |
| **Epic** | 30% | Legendary | Purple | 1.0 |
| **Legendary** | 40% | Mythic | Gold | 0.5 |

### Probability Distribution
- **75% chance**: Minor/Moderate tiers (moderate bonuses)
- **20% chance**: Major tier (significant bonuses)
- **5% chance**: Epic/Legendary tiers (exceptional bonuses)

## Power Mechanics

### Universal Application
| Damage Type | Affected | Notes |
|-------------|----------|-------|
| **Physical** | ✅ | Attacks, weapons, physical skills |
| **Fire** | ✅ | Ether Ball, fire spells |
| **Ether** | ✅ | Etheric magic, Anti Matter Ball |
| **Lightning** | ✅ | Storm Caller, electricity |
| **Cold** | ✅ | Frost Aura, ice effects |
| **Poison** | ✅ | Poison DoT, Tainted Blood |
| **Bleed** | ✅ | Blood Blade, bleed effects |

### Multiplicative Calculation
```
Final Damage = Base Damage × (1 + Global Damage Bonus)
Example with Dark Power Epic (30%):
100 base damage → 130 final damage
```

## Strategic Impact

### Universal Advantages
**Strengths:**
- Improves ALL builds without exception
- Excellent scaling at all game stages
- Perfect synergy with all other corruptions
- Immediately visible on all damage
- No activation conditions

**Optimal Applications:**
- **DPS builds**: Direct damage multiplier
- **Hybrid builds**: Improves attacks AND spells
- **DoT builds**: Increases poison, bleed, burn
- **Burst builds**: Maximizes big hits

## Cross-Corruption Synergies

### Multiplicative Combos
- **+ Corrupted Rage**: Double multiplier (Global + Berserker)
- **+ Elemental Resonance**: Triple bonus for elemental spells
- **+ Echo Chamber**: More damage on each double cast
- **+ Critical Mass**: More damage on criticals

### Recommended Builds
- **Pure Damage**: Dark Power + Corrupted Rage + Critical Mass
- **Elemental Powerhouse**: Dark Power + Elemental Resonance + Ether builds
- **Physical Destroyer**: Dark Power + Battle Frenzy + Blood Blade
- **Hybrid Dominator**: Dark Power + Echo Chamber + mixed skills

## Value Comparisons

### vs Other Damage Corruptions
- **Dark Power**: Universal, all damage, 10-40%
- **Elemental Resonance**: Elemental specialized, 15-25%
- **Corrupted Rage**: Global + attack speed, 20-25%
- **Blood Thirst**: Conditional kills, dynamic scaling

### Relative Effectiveness
- **Early Game**: Moderate immediate impact
- **Mid Game**: Becomes very powerful with other multipliers
- **Late Game**: Foundational for all optimized builds

## Balance Considerations

### Balanced Progression
- **Minor Tier** (10%): Notable improvement without domination
- **Epic Tier** (30%): Powerful but rare
- **Legendary Tier** (40%): Game-changing but extremely rare

### Rarity Gating
- The higher the bonus, the more exponentially the rarity increases
- Prevents easy acquisition of higher tiers
- Maintains the system's risk/reward balance

## Build Impact

### Universally Enhanced Builds
**All archetypes benefit:**
- **Casters**: More powerful spells
- **Fighters**: More destructive attacks
- **Supports**: Enhanced utility damage
- **Hybrids**: Boost to all abilities

### Acquisition Priority
- **High Priority**: All offensive builds
- **Medium Priority**: Defensive builds with utility damage
- **Low Priority**: Pure support builds (rare in PoE Survivor)

## Meta-Game Impact

### Influence on Choices
- Universally desirable corruption
- Can influence build decisions toward more offense
- Creates a "tax" on other corruption choices
- Standard of comparison for other corruptions

### Interaction with Difficulty
- Allows tackling more difficult content
- Accelerates general progression
- Makes boss fights more manageable
- Improves farming efficiency

## Optimization Strategies

### Efficiency Maximization
**Stackable Multipliers:**
- Seek other sources of Global Damage
- Combine with critical multipliers
- Use with attack/cast speed for total DPS
- Synergy with area damage for clear speed

### Acquisition Timing
- **As soon as possible**: Immediate benefit
- **Early priority**: Foundation for scaling
- **Reroll consideration**: Too low tiers may justify reroll

## Risks and Limitations

### No Direct Malus
- This corruption has no negative counterpart
- The only "cost" is the opportunity cost vs other corruptions
- Can create over-reliance on pure damage

### Diminishing Returns
- Combines multiplicatively with other sources
- The more multipliers you have, the less each new one has relative impact
- Requires diversification for complete optimization

## Technical Implementation

### Source Files
- **Corruption**: `dark_power_reward.tres`
- **Script**: `corruption_stat_modifier_reward.gd`
- **Path**: `Bonus\Stat_Bonuses\Damage\Global\More\`

### Data Structure
```gdscript
# Type: StatModifierReward
stat_modifier = GLOBAL_DAMAGE (MULTIPLIER)
tier_values = [Minor: 10%, Moderate: 15%, Major: 20%, Epic: 30%, Legendary: 40%]
display_name = "Global Damage"
```

### Description Template
```
"{globaldamage_percentage}{globaldamage_type_suffix} Global Damage"
```

## Related

- [[Corruptions]] - Main system
- [[Global Damage]] - Stat mechanism
- [[Damage Scaling]] - Multiplier theory
- [[Stat Modifiers]] - Technical system
- [[Tier System]] - Rarity system
- [[Build Optimization]] - Advanced strategies

---

**Implementation**: `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\Damage\Global\More\dark_power_reward.tres`