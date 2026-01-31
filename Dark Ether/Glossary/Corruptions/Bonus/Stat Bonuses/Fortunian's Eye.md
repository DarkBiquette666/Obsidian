---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: StatModifierReward
tags: [critical, chance, fortunian, luck, flat]
status: implemented
rarity: tier_based
---

# Fortunian's Eye

## Description
A corruption that grants additional critical chance based on the legendary luck of the Fortunians. This corruption awakens the bearer's intuition, allowing them to perceive and exploit their enemies' weaknesses with supernatural precision inherited from the people of fortune.

## Lore
The Fortunian's Eye is a mystical blessing that reproduces the natural extrasensory perception of the Fortunian people. This corruption allows seeing beyond the veil of reality, revealing the hidden vulnerability points of enemies. The more powerful the corruption, the clearer and more precise this vision becomes, transforming chance into deadly certainty.

## Statistics

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Bonus Corruption | Positive effect |
| **Category** | Critical Enhancement | Critical improvement |
| **Base Class** | StatModifierReward | Stat modifier |
| **Affected Stat** | CRITICAL_STRIKE_CHANCE | Critical chance |
| **Value Type** | FLAT | Direct percentage |
| **Randomization** | Yes | Variable values per tier |

## Tier System

### Value Distribution
| Tier | Critical Chance | Rarity | Color | Weight | Range |
|------|----------------|--------|-------|--------|-------|
| **Minor** | 1-2% | Common | White | 10.0 | 1.0-2.0% |
| **Moderate** | 2-4% | Rare | Green | 7.0 | 2.0-4.0% |
| **Major** | 4-6% | Epic | Blue | 4.0 | 4.0-6.0% |
| **Epic** | 6-7% | Legendary | Purple | 1.0 | 6.0-7.0% |

### Randomization System
- **Randomize Value**: Enabled
- **Float Values**: No (integer values)
- **Min/Max Mode**: No (continuous range)
- **Weight System**: Decreasing according to rarity

## Critical Mechanics

### Chance Calculation
```
Final Critical Chance = Base Crit + Fortunian's Eye + Other Bonuses
Example with Epic Tier (6.5%):
5% base + 6.5% Fortunian's Eye = 11.5% total chance
```

### Impact by Tier
| Base Crit Build | +2% (Minor) | +4% (Moderate) | +6% (Major) | +6.5% (Epic) |
|-----------------|-------------|----------------|-------------|--------------|
| **5% base** | 7% (+40%) | 9% (+80%) | 11% (+120%) | 11.5% (+130%) |
| **10% base** | 12% (+20%) | 14% (+40%) | 16% (+60%) | 16.5% (+65%) |
| **15% base** | 17% (+13%) | 19% (+27%) | 21% (+40%) | 21.5% (+43%) |

## Fortunian Theme

### Fortune Heritage
**Racial Identity:**
- Represents the natural luck of Fortunians
- Manifests their intuitive perception of destiny
- Symbolizes mastery of chance and opportunity
- Transforms fortune into tactical skill

**Philosophy of Luck:**
- "Fortune favors the prepared"
- Vision beyond appearances
- Anticipation of opportunities
- Exploitation of hidden weaknesses

## Strategic Applications

### Critical Builds
**Optimal Synergies:**
- **Critical Mass**: Cumulative chance + critical damage
- **Silent Blade**: Double chance + multiplier
- **Dark Power**: More damage on criticals
- **Echo Chamber**: More attacks = more chances

### Impact by Build Type
| Build Type | Value | Notes |
|------------|-------|-------|
| **Crit Specialist** | Very High | Build foundation |
| **Hybrid Crit** | High | Excellent complement |
| **Non-Crit** | Medium | Adds new dimension |
| **DoT Builds** | Low | Criticals less important |

## Efficiency Calculations

### ROI by Tier
**Minor Tier (1-2%):**
- Investment: Low
- Return: 20-40% increase in crits
- Value: Excellent for early game

**Epic Tier (6-7%):**
- Investment: Very rare
- Return: 40-130% increase in crits
- Value: Game-changing for crit builds

### Important Breakpoints
- **10% total**: Notable critical (1 in 10)
- **20% total**: Frequent critical (1 in 5)
- **33% total**: Very frequent critical (1 in 3)

## Cross-Corruption Synergies

### Perfect Combinations
**Crit Trinity:**
- Fortunian's Eye (chance)
- Critical Mass (chance + damage)
- Silent Blade (chance + multiplier)

**DPS Maximization:**
- Fortunian's Eye + Dark Power + Echo Chamber
- More crits × more damage × double chance

### Build Archetypes
**Lucky Assassin:**
- Fortunian's Eye + Silent Blade + Corrupted Rage
- High crit chance + crit multi + attack speed

**Fortune Mage:**
- Fortunian's Eye + Critical Mass + Elemental Resonance
- Crit spells with elemental damage

## Balance Considerations

### Logarithmic Scaling
- **Early Game**: Very visible impact
- **Mid Game**: Still significant
- **Late Game**: Diluted with other sources

### Diminishing Returns
```
Efficiency = Bonus / (Base + Total Bonus)
The more crit you have, the less each additional % impacts
```

### Rarity vs Power
- High tiers rare enough to avoid OP
- Natural power progression
- Epic tier remains desirable but not game-breaking

## Meta-Game Impact

### Influence on Builds
- Can convert non-crit builds toward crit
- Reinforces the appeal of critical builds
- Creates decisions on corruption slot allocation

### Interaction with Classes
- **Fortunians**: Thematically perfect
- **Assassin styles**: Natural synergy
- **Torin**: Excellent with Blood Blade crits
- **Casters**: Transforms spell builds

## Advanced Optimization

### Crit Threshold Theory
**Comfort Zones:**
- 0-10%: Occasional crits
- 10-25%: Regular crits
- 25-50%: Frequent crits
- 50%+: Crit-dependent builds

### Investment Strategy
- **Early**: Take any tier
- **Mid**: Reroll for higher tiers
- **Late**: Combine with other crit corruptions

## Interaction with Skills

### Skills with High Crit Value
- **Blood Blade**: Multiple projectiles = multiple crit chances
- **Ether Ball**: Powerful elemental crits
- **Storm Caller**: Lightning crits with shock
- **Curses**: Crits for stronger debuffs

### Crit-Scaling Skills
Some skills have special bonuses on critical:
- Extended shock effects
- Increased bleed damage
- Increased status effect intensity

## Technical Implementation

### Source Files
- **Corruption**: `fortunian_eye.tres`
- **Path**: `Bonus\Stat_Bonuses\Critical\Chance\Flat\`
- **Script**: `corruption_stat_modifier_reward.gd`

### Data Structure
```gdscript
# Type: StatModifierReward
stat = CRITICAL_STRIKE_CHANCE
value_type = FLAT
randomize_value = true
tier_ranges = [
    Minor: 1.0-2.0%,
    Moderate: 2.0-4.0%,
    Major: 4.0-6.0%,
    Epic: 6.0-7.0%
]
```

### Description Template
```
"{criticalstrikechance_type_prefix} {criticalstrikechance_value}% {criticalstrikechance_type_suffix} Critical Strike Chance"
```

## Acquisition Strategies

### Priority by Build
- **High Priority**: Crit specialists, assassin builds
- **Medium Priority**: Hybrid builds, spell casters
- **Low Priority**: DoT builds, pure support builds

### Reroll Considerations
- **Minor/Moderate**: Acceptable early game
- **Major+**: Keep definitely
- **Epic**: Perfect roll, build around it

## Related

- [[Corruptions]] - Main system
- [[Critical Strike]] - Critical mechanism
- [[Fortunians]] - Thematic people
- [[Luck Mechanics]] - Chance systems
- [[Stat Modifiers]] - Technical system
- [[Build Optimization]] - Critical strategies

---

**Implementation**: `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\Critical\Chance\Flat\fortunian_eye.tres`