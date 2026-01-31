# Skills Index - Dark Ether

Complete index of all skills implemented in the PoE Survivor project.

## Overview

Total documented skills: **15 skills**
- ✅ Implemented and playable: **11 skills**
- 🔒 Implemented but locked: **4 skills**

## Classification by Category

### 🩸 Blood Magic
| Skill | Classes | Status | Type | Description |
|-------|---------|--------|------|-------------|
| [[Blood Blade]] | Torin | ✅ | Attack | Forms blood blade projectiles that inflict bleeding |
| [[Anemic Curse]] | All except Astralians | ✅ | Curse | Weakens enemy vitality and resistance |
| [[Life Leech Aura]] | Torin | ✅ | Aura | Drains life from surrounding enemies |

### ⚡ Elemental
| Skill | Classes | Status | Type | Description |
|-------|---------|--------|------|-------------|
| [[Ether Ball]] | Astralians, Voidborn | ✅ | Spell | Dual Fire/Ether projectile with explosion |
| [[Dark Ether/Glossary/Skills and Perks/Elemental/Storm Caller]] | None | 🔒 | Spell | Automatically strikes enemies with lightning |
| [[Dark Ether/Glossary/Skills and Perks/Elemental/Frost Aura]] | None | ✅ | Aura | Frost aura that continuously applies chill |

### 🗡️ Melee & Physical
| Skill                    | Classes         | Status | Type   | Description                            |
| ------------------------ | --------------- | ------ | ------ | -------------------------------------- |
| [[Thorn Spike]]          | Torin, Voidborn | ✅      | Spell  | Makes spikes emerge from the ground in lines |
| [[Default Melee Attack]] | All             | ✅      | Attack | Basic melee attack                            |
|                          |                 |        |        |                                        |

### 🌀 Ether

| Skill | Classes | Status | Type | Description |
|-------|---------|--------|------|-------------|
| [[Anti Matter Ball]] | All | 🔒 | Spell | Dangerous orbital sphere (can harm the caster) |

### 😈 Curses
| Skill | Classes | Status | Type | Description |
|-------|---------|--------|------|-------------|
| [[Anemic Curse]] | All except Astralians | ✅ | Curse | Weakens vitality and resistance |
| [[Elemental Weakness Curse]] | All except Astralians | ✅ | Curse | Reduces elemental resistances |
| [[Enfeeble Curse]] | All except Astralians | ✅ | Curse | Reduces damage dealt by enemies |
| [[Poison Weakness Curse]] | All except Astralians | ✅ | Curse | Reduces poison resistance |

## Classification by Type

### ⚔️ Attack Skills
- [[Blood Blade]] - Weapon-based physical attack with bleeding
- [[Default Melee Attack]] - Standard melee attack

### 🧙 Spell Skills  
- [[Ether Ball]] - Dual elemental projectile
- [[Dark Ether/Glossary/Skills and Perks/Elemental/Storm Caller]] - Automatic lightning (locked)
- [[Thorn Spike]] - Spikes emerging from ground
- [[Anti Matter Ball]] - Dangerous orbiter (locked)
- [[Dark Ether/Glossary/Skills and Perks/Elemental/Frost Aura]] - Frost aura
- All Curses (technically spells)

### 🌟 Aura Skills
- [[Life Leech Aura]] - Continuous life drain
- [[Dark Ether/Glossary/Skills and Perks/Elemental/Frost Aura]] - Continuous cold application

### 😈 Curse Skills
- [[Anemic Curse]] - Vitality debuff
- [[Elemental Weakness Curse]] - Elemental resistance debuff  
- [[Enfeeble Curse]] - Enemy damage debuff
- [[Poison Weakness Curse]] - Poison resistance debuff

## Access by Class

### 🌟 Astralians
- **Exclusive access:** None
- **Shared access:** [[Ether Ball]], [[Default Melee Attack]]
- **Notable exclusions:** All Curses

### 🍀 Fortunians
- **Exclusive access:** None
- **Shared access:** All Curses, [[Default Melee Attack]]

### 🌿 Lesharii  
- **Exclusive access:** None
- **Shared access:** All Curses, [[Default Melee Attack]]

### 🩸 Torin
- **Exclusive access:** [[Blood Blade]], [[Life Leech Aura]]
- **Shared access:** [[Thorn Spike]], All Curses, [[Default Melee Attack]]

### 🌑 Umbrathi
- **Exclusive access:** None  
- **Shared access:** All Curses, [[Default Melee Attack]]

### 🌌 Voidborn
- **Exclusive access:** None
- **Shared access:** [[Ether Ball]], [[Thorn Spike]], All Curses, [[Default Melee Attack]]

### 🔄 Vorathros
- **Exclusive access:** None
- **Shared access:** All Curses, [[Default Melee Attack]]

## Perk System

### 🩸 Blood Blade Perks
- **Amount** - Adds additional blades
- **Mimic Blades** - Blades attack when you cast other spells
- **Conscious Blood** - Blades attack automatically (incompatible with Mimic)
- **Drinker Blades** - Consume bleeding stacks for instant damage
- **Health Scaling** - Damage increases with maximum health
- **Increased Bleed Damage** - Increases bleeding damage
- **Increased Range** - Increases blade range
- **Reduce Cost** - Reduces health cost
- **Change Damage Type** - Modifies damage type

### 😈 Anemic Curse Perks
- **Vitality Siphon** - Drains life from cursed enemies
- **Crippling Chains** - Reduces movement speed
- **Flesh Ripper** - Increases physical damage taken
- **Hemorrhagic Wounds** - Increases bleeding damage taken
- **Cognitive Decay** - Reduces accuracy and criticals

### 🌀 Ether Ball Perks
- **Fire to Ether** - Converts all Fire damage to Ether
- **Ether to Fire** - Converts all Ether damage to Fire
- **Increased Spread Angle** - Increases spread angle

### 🎯 Generic Projectile Perks
- **Add Projectile** - Adds additional projectiles
- **Projectile Chaining** - Allows chaining between targets
- **Projectile Homing** - Adds target tracking
- **Homing Distance/Attraction** - Improves tracking capabilities

## Implementation Status

### ✅ Fully Implemented
- Functional base skills system
- Perk system for Blood Blade and Anemic Curse
- Damage and effects mechanics
- Integrated user interface

### 🔧 In Development
- Perk system for other skills
- Balancing damage values
- Unlocking locked skills
- Adding new skills

### 📊 Development Statistics

**Distribution by Status:**
- 73% of skills are playable (11/15)
- 27% are locked (4/15)

**Class Coverage:**
- Torin: 4 exclusive/shared skills
- Astralians: Excluded from curses (intentional design)
- Other classes: Balanced access to curses

**Skill Types:**
- 27% Curses (4/15)
- 20% Blood Magic (3/15) 
- 20% Elemental (3/15)
- 13% Melee (2/15)
- 7% Void (1/15)
- 13% Others (2/15)

---

## Quick Navigation

### By Folder
- [[Skills/Blood]] - Blood magic and Torin skills
- [[Skills/Elemental]] - Elemental and magical skills
- [[Skills/Curses]] - Curses and debuffs
- [[Skills/Melee]] - Physical and melee attacks
- [[Skills/Void]] - Void manipulation and antimatter

### By Mechanics
- [[Projectile]] - Projectile skills
- [[Aura]] - Persistent effects and zones
- [[Toggle Skill]] - Activatable/deactivatable skills
- [[Bleed]] - Bleeding mechanics
- [[Leech]] - Life and mana drain

---

## Links with Corruptions

### Skills Referenced by Corruptions
- **[[Dark Ether/Glossary/Skills and Perks/Elemental/Frost Aura]]** ← Corruption [[Frost Aura Bonus]]
- **[[Dark Ether/Glossary/Skills and Perks/Elemental/Storm Caller]]** ← Corruption [[Storm Caller Bonus]]  
- **[[Anti Matter Ball]]** ← Corruption [[Anti-Matter Orb]]
- **[[Blood Blade]]** ← Synergy with [[Blood Thirst]] corruption

### Skills-Corruptions Synergies
- **[[Echo Chamber]]**: Doubles all skills (universal effect)
- **[[Corrupted Rage]]**: Berserker style with attack skills
- **[[Battle Frenzy]]**: Attack speed with physical skills
- **[[Elemental Resonance]]**: Bonus with [[Ether Ball]], elemental skills

---

*Last updated: January 2025*
*Source: Automatic extraction from Godot project .tres files*
*Corruption links added: January 2025*