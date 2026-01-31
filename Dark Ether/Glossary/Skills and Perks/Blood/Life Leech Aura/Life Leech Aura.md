---
type: skill
category: Aura
element: []
classes:
  - Torin
tags:
  - spell
  - aura
  - leech
  - toggle
  - blood
status: implemented
locked: false
skill Family: blood
---

# Life Leech Aura

## Description
Drain all enemies' health within the area. This blood magic aura creates a vampiric field that continuously siphons life force from nearby enemies, transferring it to the caster for sustenance and power.

## Lore
The Life Leech Aura represents the darkest aspect of blood magic, where the Torin channels their connection to vitality itself. This forbidden technique transforms the caster into a walking nexus of vampiric energy, slowly draining the life from all who dare approach.

## Statistics

| Property            | Value    | Notes                        |
| ------------------- | -------- | ---------------------------- |
| **Type**            | Spell    | Blood magic aura             |
| **Damage Base**     | 0        | No direct damage             |
| **Cast Time**       | 0.8 sec  | Moderate activation time     |
| **Critical Chance** | 0%       | Cannot critically strike     |
| **Cost**            | 10 Mana  | Activation cost              |
| **Cooldown**        | None     | Can be reactivated freely    |
| **Duration**        | Infinite | Remains active until toggled |
| **Lifespan**        | Infinite | Persistent effect            |
| **Classes**         | Torin    | Blood magic specialist only  |
| **Weapon Required** | No       | Independent of weapons       |
| **Toggleable**      | Yes      | Can be turned on/off         |

## Leech Properties

| Property | Value | Description |
|-----------|--------|-------------|
| **Life Leech Percent** | 1% | Base leech rate per enemy |
| **Max Life Leech Percent** | 10% | Maximum total leech rate |
| **Follow Caster** | Yes | Moves with the player |
| **Attach to Caster** | Yes | Centered on player |
| **Range** | Variable | Depends on aura radius |
| **Effect Type** | Continuous | Constant drain |

## Mechanics

### Life Leech System
- **Base Rate:** 1% of enemy health per second per enemy
- **Maximum Rate:** Capped at 10% of caster's health per second
- **Stacking:** Multiple enemies stack up to cap
- **Healing:** All leeched life heals the caster
- **Resistance:** Not affected by damage resistance

### Aura Behavior
- **Persistent Effect:** Remains active until manually toggled off
- **Movement Penalty:** Reduces movement speed to 50%
- **No Ongoing Cost:** Only initial mana cost required
- **Toggle Freedom:** Can be turned on/off at will

## Tactical Usage

**Strengths:**
- Incredible sustain in enemy-dense areas
- No ongoing resource cost
- Scales with number of enemies
- Perfect for prolonged combat
- Excellent defensive utility

**Weaknesses:**
- Severe movement speed penalty (50%)
- No direct damage contribution
- Requires close proximity to enemies
- Limited to Torin class only
- Useless against single targets

**Strategic Applications:**
- Tank builds for group encounters
- Sustained combat scenarios
- Emergency healing in dangerous situations
- Crowd farming strategies
- Boss fights with multiple phases/adds

## Class Synergy - Torin

**Blood Magic Mastery:**
- Complements other blood-based skills
- Synergizes with health-based mechanics
- Enhances survivability for risky blood costs

**Life Scaling Builds:**
- Maximum health increases leech cap
- Health regeneration stacks with leech
- Life-based damage modifiers benefit

**Defensive Specialization:**
- Torin's natural tankiness enhanced
- Compensates for aggressive playstyles
- Supports front-line positioning

## Synergies

**Health-Based Builds:**
- Maximum life bonuses increase leech cap
- Life regeneration effects stack
- Health scaling damage benefits

**Aura Builds:**
- Aura effectiveness improves leech rate
- Aura radius increases coverage area
- Aura duration bonuses (if applicable)

**Sustain Builds:**
- Combines with other healing sources
- Enhances overall survivability
- Supports resource-intensive strategies

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Life Leech Aura/life_drain_aura.tres`
- **Behavior:** `life_drain_aura_behavior.gd`
- **Scene:** `Life Drain Aura.tscn`
- **Cast VFX:** `CastingRune.tscn`
- **Icon:** `Vitality_skill_icon.webp`
- **Status:** Implemented and functional
- **Main Skill:** Yes (primary skill for Torin)

## Technical Notes

- Uses percentage-based leech calculation
- Leech rate scales with enemy count
- Maximum leech prevents exploitation
- Toggle mechanism for tactical control
- Class restriction enforced in data

## Balance Considerations

- Movement penalty prevents abuse
- Leech cap prevents overpowered scaling
- Mana cost ensures tactical decision
- Class restriction maintains identity

### Implementation Tracking

See [[Life Leech Aura Perks.base]] for the complete database with implementation status and priority tracking.

## Related

- [[Torin]] - Exclusive class user
- [[Leech]] - Core mechanic
- [[Blood]] - Thematic skill tree
- [[Aura]] - Skill mechanism
- [[Toggle Skill]] - Activation type
- [[Spell]] - Skill category