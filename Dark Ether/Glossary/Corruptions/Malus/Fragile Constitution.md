---
type: corruption
category: Malus
subcategory: Conditional Penalties
reward_type: FragileConstitutionReward
tags: [malus, low_life, damage_taken, conditional, penalty]
status: implemented
danger_level: moderate
---

# Fragile Constitution

## Description
A malus corruption that increases damage taken when the player is in "Low Life" state. This corruption represents physical weakening that makes the bearer more vulnerable when already in a critical situation.

## Lore
Fragile Constitution is an insidious curse that seeps into the very fibers of one's being. It transforms the natural vulnerability of injury into extreme weakness, where every blow received when the organism is weakened becomes potentially lethal. This is the price to pay for those who dare to draw too deeply from the corrupted energies of the Dark Ether.

## Statistics

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Malus Corruption | Negative effect |
| **Category** | Conditional Penalty | Conditional penalty |
| **Base Class** | FragileConstitutionReward | Specialized class |
| **Penalty** | +25% damage taken | Fixed increase |
| **Condition** | Low Life (State 1) | Conditional activation |
| **Duration** | Permanent (-1.0) | While corruption is active |

## Vulnerability Mechanics

### Low Life System
| Property | Details | Notes |
|----------|---------|-------|
| **Activation Threshold** | Low Life State | Generally <35% HP |
| **Trigger** | Health state | Continuously checked |
| **Penalty Type** | Incoming damage | 1.25x multiplier |
| **Application** | All damage types | Physical, elemental, etc. |
| **Effect Duration** | While Low Life | Dynamic activation/deactivation |

### Damage Calculation
```
Final Damage = Base Damage × 1.25 (if Low Life)
Condition: Current Health ≤ Low Life Threshold
```

## Life States

### Standard Definitions
- **Full Life** : 100% HP
- **Half Life** : ~50% HP  
- **Low Life** : <35% HP (State 1 in code)

### Fragile Constitution Impact
- **Full/Half Life** : No effect
- **Low Life** : +25% damage taken from all sources
- **Transition** : Effect applied/removed instantly

## Risks and Dangers

### Increased Vulnerability
**In Low Life :**
- Death more likely on big hits
- Enemy combos become lethal
- Room for error drastically reduced
- Requires constant micro-management

**Critical Situations :**
- Boss fights with predictable patterns
- Rooms with numerous enemies
- Active damage over time effects
- Lack of healing/recovery

## Strategic Counterplay

### Low Life Build Mechanics
Some builds deliberately exploit the Low Life state:
- **Blood Magic builds** : Health cost instead of mana
- **Adrenaline builds** : Bonuses when health is low
- **Risk/Reward builds** : More risk for more reward

### Negative Synergies
This corruption can ruin these specialized builds:
- Makes Low Life builds non-viable
- Forces maintenance of High Life
- Limits blood magic strategies
- Eliminates certain tactical options

## Management and Mitigation

### Defensive Strategies
**Prevention :**
- Maintain health above Low Life threshold
- Prioritize healing sources
- Avoid risky situations
- More defensive build

**Recovery Options :**
- Life Leech effects
- Health Potions
- Regeneration stats
- Healing skills/auras

### Compatible Builds
**Recommended :**
- High Life builds with sustain
- Defensive builds with armor/resistances
- Ranged builds avoiding contact
- Builds with constant passive healing

**To Avoid :**
- Low Life specialists
- Blood Magic heavy users
- Builds without recovery
- Glass cannon builds

## Cross-Corruption Synergies

### Dangerous Corruption Combinations
- **+ Slow Actions** : Less dodging + more damage
- **+ Echo Backlash** : Reflection + vulnerability = quick death
- **+ Anti-Matter Orb** : Increased self-damage risk

### Compensatory Corruptions
- **+ Titan Vitality** : More HP = higher Low Life threshold
- **+ Titan Regeneration** : Constant recovery
- **+ Corrupted Endurance** : Health bonus + regeneration

## Balance Considerations

### Gameplay Impact
- Encourages more careful play
- Increases tension in combat
- Rewards resource management
- Creates critical decision-making moments

### Risk vs Reward
- The malus must be compensated by significant bonuses
- Should not make the game impossible
- Must create tension without frustration
- Delicate balance between challenge and fairness

## Stat Interactions

### Damage Reduction
- **Armor** : Reduces damage before malus application
- **Resistances** : Same for elemental damage
- **Damage Reduction** : Multipliers combine

### Health Management
- **Max Health bonuses** : Increase buffer before Low Life
- **Health %** : Low Life threshold remains proportional
- **Flat Health** : Same effect as Max Health bonuses

## Technical Implementation

### Source Files
- **Corruption** : `fragile_constitution_malus.tres`
- **Script** : `fragile_constitution_reward.gd`
- **Effect** : `conditional_fragile_constitution_debuff.tres`

### Data Structure
```gdscript
# Type: FragileConstitutionReward
damage_taken_penalty = 25.0  # +25% damage taken
life_state = 1  # Low Life state
effects_to_apply = [conditional_fragile_constitution_debuff.tres]
effect_durations = [-1.0]  # Permanent
reward_type = 1  # Malus
```

### Description Template
```
"25% damage taken when you're on Low Life"
```

## Avoidance Strategies

### When to Avoid This Corruption
- **Low Life Builds** : Total incompatibility
- **Blood Magic users** : Risk too high  
- **Glass cannon builds** : Already fragile
- **Beginners** : Too punitive for learning

### Preferable Alternatives
- Corruptions with constant but manageable maluses
- Maluses not directly affecting survival
- Corruptions with more balanced trade-offs

## Survival Tips

### Early Warning Systems
- Constantly monitor HP bar
- Identify danger thresholds
- Anticipate enemy attack patterns
- Keep healing items available

### Build Adjustments
- Invest more in maximum HP
- Prioritize regeneration/leech
- Avoid poke damage situations
- Adapt playstyle

## Related

- [[Corruptions]] - Main system
- [[Low Life]] - Health state
- [[Life States]] - Life mechanism
- [[Conditional Effects]] - Conditional effects
- [[Damage Taken]] - Damage mechanism
- [[Risk Management]] - Risk management strategies

---

**Implementation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Malus\Resources\fragile_constitution_malus.tres`