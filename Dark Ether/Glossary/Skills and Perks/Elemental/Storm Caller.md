---
type: skill
category: Spell
element:
  - Lightning
classes: []
tags:
  - spell
  - area
  - lightning
  - automatic
  - aura
  - persistent
status: implemented
locked: true
skill Family: elemental
---

# Storm Caller

## Description
Automatically strikes nearby enemies with lightning. This powerful spell creates a persistent electrical field around the caster that continuously seeks and destroys enemies within range.

## Lore
The Storm Caller represents mastery over the raw power of lightning and thunder. This ancient technique channels the fury of tempests, creating a localized storm that follows the caster and strikes down their foes with relentless electrical fury.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Spell | Automatic area spell |
| **Damage Base** | 1-55 | High damage variance |
| **Damage Type** | 100% Lightning | Pure electrical damage |
| **Cast Time** | 0.1 sec | Very fast activation |
| **Critical Chance** | 8% | Higher than average crit |
| **Cost** | 0 Mana | No mana cost |
| **Cooldown** | None | Continuously active |
| **Lifespan** | Infinite | Persistent effect |
| **Lightning Radius** | 250 | Strike detection range |
| **Lightning Interval** | 3.0 sec | Time between strikes |
| **Classes** | None | Currently class-locked |
| **Weapon Required** | No | Independent of weapons |
| **Movement Speed** | 80% | Reduced while active |

## Behavior Properties

| Propriété | Valeur | Description |
|-----------|--------|-------------|
| **Persistent** | Yes | Remains active until toggled off |
| **Automatic** | Yes | Strikes enemies without input |
| **Range** | 250 units | Detection and strike radius |
| **Target Priority** | Nearest | Strikes closest enemies first |
| **Multiple Targets** | Yes | Can strike multiple enemies |
| **Spawn Location** | Mouse Cursor | Activated at cursor position |

## Tactical Usage

**Strengths:**
- Zero mana cost for sustained damage
- High critical strike chance (8%)
- Large area of effect (250 radius)
- Completely automatic operation
- High maximum damage (55)

**Weaknesses:**
- Currently locked and unavailable
- Long interval between strikes (3 seconds)
- Reduces movement speed to 80%
- Cannot be manually targeted
- No direct player control over strikes

**Strategic Applications:**
- Ideal for crowd control situations
- Excellent for area denial
- Perfect for sustained combat encounters
- Useful for farming lower-tier enemies
- Great for defensive positioning

## Synergies

**Lightning Damage Modifiers:**
- All lightning damage bonuses apply
- Shock effects can be triggered
- Lightning resistance penetration helps

**Critical Strike Builds:**
- High base crit chance (8%) scales well
- Critical multipliers are very effective
- Critical strike chance increases compound

**Area Damage Builds:**
- Area damage bonuses affect all strikes
- Area of effect increases expand radius
- Multiple target scenarios maximize value

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Storm Caller/storm_caller_skill.tres`
- **Behavior:** `storm_caller_behavior.gd`
- **Scene:** `StormCallerSkillScene.tscn`
- **Casting VFX:** `CastingStormCaller.tscn`
- **Icon:** `Storm_Caller_Skill_Icon.png`
- **Status:** Implemented but locked
- **Main Skill:** No (secondary/bonus skill)

## Technical Notes

- Uses automatic targeting system
- Persistent behavior attached to caster
- Lightning strikes are spawned at cursor position
- No resource consumption during operation
- Compatible with spell damage modifiers

## Related

- [[Lightning Damage]] - Primary damage type
- [[Spell]] - Skill category
- [[Shock]] - Potential status effect
- [[Area]] - Damage mechanism
- [[Aura]] - Similar persistent behavior