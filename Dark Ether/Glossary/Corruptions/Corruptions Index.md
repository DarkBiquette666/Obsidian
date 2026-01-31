# Corruptions Index - Dark Ether

Complete index of all corruptions implemented in the PoE Survivor project.

## Overview

Total documented corruptions: **29 corruptions**
- ✅ Bonus (positive effects): **19 corruptions** (65.5%)
- ❌ Malus (negative effects): **4 corruptions** (13.8%)
- 🔧 To Fix (under repair): **6 corruptions** (20.7%)

## Classification by Category

### ✅ Bonus Corruptions

#### 🌟 Special Effects (5)
| Corruption | Type | Main Effect | Rarity | Description |
|------------|------|-------------|--------|-------------|
| [[Echo Chamber]] | CorruptionEffectReward | Double cast chance | Variable | Chance to cast skills twice |
| [[Battle Frenzy]] | CorruptionEffectReward | Attack speed stacks | Variable | Attack speed increased with each hit |
| [[Blood Thirst]] | CorruptionEffectReward | Damage per kill | Variable | More damage per enemy killed |
| [[Dark Ether/Glossary/Corruptions/Bonus/Special Effects/Frost Aura]] | SkillReward | Frost aura | Fixed | Grants the Frost Aura skill |
| [[Dark Ether/Glossary/Corruptions/Bonus/Special Effects/Storm Caller]] | CorruptionEffectReward | Lightning strikes | Variable | Lightning strikes nearby enemies |

#### ⚔️ Combat Styles (5)
| Corruption | Display Name | Main Stats | Values | Theme |
|------------|-------------|------------|--------|-------|
| [[Corrupted Rage]] | Berserker | Global Damage + Attack Speed | 20-25% + 15-20% | Berserker |
| [[Silent Blade]] | Assassin | Crit Chance + Crit Multi | 0.5-1.5% + 20-50% | Assassin |
| [[Forbidden Knowledge]] | Scholar | Mana + Cast Speed | +50 + 20-25% | Scholar |
| [[Corrupted Endurance]] | Survivor | Health + Regen | +100 + 2-3%/sec | Survivor |
| [[Time Distortion]] | - | Attack Speed + Cast Speed | 10/15/20% | Temporal |

#### 📊 Specialized Stat Bonuses (9)

##### Critical (2)
| Corruption | Focus | Values | Tiers |
|------------|-------|--------|-------|
| [[Fortunian's Eye]] | Crit Chance | 1-7% flat | Minor/Moderate/Major/Epic |
| [[Critical Mass]] | Crit Chance + Damage | 0.3-0.7% + 20-30% | Minor/Moderate/Major |

##### Damage (2)
| Corruption | Damage Type | Values | Tiers |
|------------|-------------|--------|-------|
| [[Dark Power]] | Global Damage | 10/15/20/30/40% | Minor → Legendary |
| [[Elemental Resonance]] | Elemental Damage | 15/20/25% | Minor/Moderate/Major |

##### Resources & Stats (5)
| Corruption | Stat | Type | Values | Tiers |
|------------|------|------|--------|-------|
| [[Thirst for Knowledge]] | Experience | Percentage | 20-40% | Minor/Moderate/Major |
| [[Titan Vitality]] | Health | Flat | +25/50/75/100 | Minor → Exceptional |
| [[Energy Reservoir]] | Mana | Flat | +15/30/60 | Minor/Moderate/Major |
| [[Titan's Regeneration]] | Health Regen | Percentage | 1/2/3%/sec | Minor/Moderate/Major |
| [[Lesharii's Grace]] | Movement Speed | Additive | +5/10/20 | Minor/Moderate/Major |

### ❌ Malus Corruptions (4)

| Corruption | Effect Type | Penalty | Condition | Danger |
|------------|-------------|---------|-----------|--------|
| [[Fragile Constitution]] | Damage Taken | +25% | Low Life | Moderate |
| [[Echo Backlash]] | Damage Reflection | 15% reflected | Always | High |
| [[Sluggish Actions]] | Speed Penalties | -15% Move/Attack/Cast | Always | Low |
| [[Anti-Matter Orb]] | Skill Malus | Dangerous orb | Always | Very High |

### 🔧 To Fix Corruptions (6)

#### Bonus Effects To Fix (5)
| Corruption | Intended Effect | Status | Type |
|------------|----------------|--------|------|
| [[Chain Reaction]] | Explosions on death | Broken | CorruptionEffectReward |
| [[Gravity Well]] | Enemy attraction | Broken | CorruptionEffectReward |
| [[Shadow Clone]] | Attack clone | Broken | CorruptionEffectReward |
| [[Vampiric Essence]] | Life steal | Broken | CorruptionEffectReward |
| [[Reckless Fury]] | Damage at low health | Broken | RecklessFuryReward |

#### Malus Effects To Fix (1)
| Corruption | Intended Effect | Status | Type |
|------------|----------------|--------|------|
| [[Adaptive Armor]] | Resistance penalty | Broken | AdaptiveArmorReward |

## Classification by Reward Type

### StatModifierReward (15)
Corruptions that directly modify player statistics:
- **Combat Styles**: 5 corruptions
- **Critical**: 2 corruptions  
- **Damage**: 2 corruptions
- **Resources**: 6 corruptions

### CorruptionEffectReward (10)
Corruptions that apply special effects:
- **Special Effects**: 4 corruptions
- **Skills**: 1 corruption (Frost Aura via SkillReward)
- **To Fix Effects**: 5 corruptions

### Specialized Rewards (4)
Corruptions with custom classes:
- **FragileConstitutionReward**: 1 corruption
- **EchoBacklashReward**: 1 corruption
- **RecklessFuryReward**: 1 corruption
- **AdaptiveArmorReward**: 1 corruption

## Tier and Rarity System

### Standard Tiers
- **Minor**: Weight 10.0, white color
- **Moderate**: Weight 5.0, green color
- **Major**: Weight 2.0, blue color
- **Epic**: Weight 1.0, purple color
- **Legendary**: Weight 0.5, golden color

### Distribution by Rarity
- **Fixed Values**: 6 corruptions (no randomization)
- **Tiered Random**: 15 corruptions (tiers with ranges)
- **Complex Tiers**: 8 corruptions (multiple tiers, variable ranges)

## Synergies and Builds

### 🗡️ Physical/Attack Builds
**Recommended Corruptions:**
- Corrupted Rage (Berserker)
- Silent Blade (Assassin)
- Dark Power
- Critical Mass
- Echo Chamber

### 🧙 Magical/Spell Builds
**Recommended Corruptions:**
- Forbidden Knowledge (Scholar)
- Elemental Resonance
- Time Distortion
- Energy Reservoir
- Echo Chamber

### 🛡️ Defensive/Survival Builds
**Recommended Corruptions:**
- Corrupted Endurance (Survivor)
- Titan Vitality
- Titan's Regeneration
- Lesharii's Grace
- Avoid all Malus

### ⚡ Critical Builds
**Recommended Corruptions:**
- Silent Blade (Assassin)
- Fortunian's Eye
- Critical Mass
- Dark Power
- Echo Chamber

## Advanced Mechanics

### Condition Systems
- **Low Life**: Fragile Constitution, Reckless Fury
- **Always Active**: Most corruptions
- **On Hit/Kill**: Battle Frenzy, Blood Thirst
- **Chance-Based**: Echo Chamber

### Modification Types
- **Multiplicative**: Global Damage, Attack Speed, Cast Speed
- **Additive**: Movement Speed, Flat Health/Mana
- **Percentage**: Health Regeneration, Experience
- **Flat Values**: Health, Mana, Critical Chance

## Gameplay Impact

### Early Game
**Recommendations:**
- Prioritize base stats (Health, Damage)
- Avoid complex malus
- Choose simple and direct effects

### Mid Game
**Opportunities:**
- Specialized builds with Combat Styles
- Synergies between corruptions
- Risk/reward management

### Late Game
**Optimization:**
- Stacking synergistic corruptions
- Ultra-specialized builds
- Managing malus for maximum reward

## Development Statistics

### Implementation Status
- **65.5% Bonus**: Encourage offensive builds
- **13.8% Malus**: Add tension and difficult choices
- **20.7% To Fix**: Content in development

### Mechanics Coverage
- **Pure stats**: 15 corruptions (51.7%)
- **Special effects**: 10 corruptions (34.5%)
- **Conditions**: 4 corruptions (13.8%)

### Class Distribution
- **All classes**: 25 corruptions (86.2%)
- **Class-specific**: 4 corruptions (13.8%)

## Acquisition Strategies

### Priority by Phase
1. **Survival**: Health, Regeneration, Defense
2. **Damage**: Global Damage, Elemental Damage
3. **Efficiency**: Attack/Cast Speed, Experience
4. **Specialization**: Combat Styles, Critical builds
5. **Optimization**: Synergistic combinations

### Risk Management
- **Low Risk**: Pure stat bonuses
- **Medium Risk**: Conditional bonuses  
- **High Risk**: Malus corruptions
- **Very High Risk**: Anti-Matter Orb, multiple malus

## Quick Navigation

### By Folder
- [[Corruptions/Bonus]] - Positive effects and improvements
- [[Corruptions/Malus]] - Negative effects and penalties
- [[Corruptions/Bonus/Special Effects]] - Unique effects
- [[Corruptions/Bonus/Stat Bonuses]] - Stat modifications

### By Mechanics
- [[Stat Modifiers]] - Stat modification system
- [[Tier System]] - Rarity and values system
- [[Conditional Effects]] - Conditional activation effects
- [[Risk Management]] - Managing malus corruptions
- [[Build Synergies]] - Synergies between corruptions

### By Build Types
- [[Physical Builds]] - Physical attack builds
- [[Magical Builds]] - Spell builds
- [[Critical Builds]] - Critical-focused builds  
- [[Defensive Builds]] - Survival builds
- [[Hybrid Builds]] - Mixed builds

---

## Links with Other Systems

### Skills System
- **Echo Chamber** ↔ All skills
- **Frost Aura** ↔ [[Dark Ether/Glossary/Corruptions/Bonus/Special Effects/Frost Aura]] skill
- **Storm Caller** ↔ Storm effects
- **Blood Thirst** ↔ [[Blood Blade]] synergy

### Stats System
- **Global Damage** ↔ Damage calculation
- **Critical Stats** ↔ Critical hit system
- **Speed Stats** ↔ Action speed mechanics
- **Resource Stats** ↔ Health/Mana systems

### Classes System
- **Combat Styles** ↔ Class identities
- **Fortunian's Eye** ↔ [[Fortunians]] luck theme
- **Lesharii's Grace** ↔ [[Lesharii]] nature affinity

---

*Last updated: January 2025*  
*Source: Automatic extraction from Godot project .tres files*