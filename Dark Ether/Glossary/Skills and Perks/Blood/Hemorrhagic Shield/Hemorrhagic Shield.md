---
type: skill
category: Defensive
element: []
classes:
  - Torin
tags:
  - blood
  - shield
  - defensive
  - reflect
  - bleed
status: concept
locked: true
skill Family: blood
---

# Hemorrhagic Shield

## Description
The caster uses his blood to form a temporary shield that absorbs damage. The shield converts a percentage of the caster's maximum health into protective barrier and reflects part of absorbed damage back to attackers as bleeding wounds.

## Lore
The Hemorrhagic Shield embodies the Torin's mastery over their own life force, transforming precious vitality into a living barrier. This crimson defense not only protects but actively punishes those who dare attack it, turning every assault into a bleeding wound that feeds back to the caster's enemies.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Defensive Skill | Blood magic shield |
| **Shield Source** | % of Max Health | Converts health to shield |
| **Health Conversion** | Variable % | Configurable percentage |
| **Damage Reflection** | Bleed | Reflects as bleeding damage |
| **Duration** | Variable | Until depleted or dismissed |
| **Classes** | Torin | Blood magic specialist only |
| **Activation Cost** | Health | Uses own vitality |
| **Cooldown** | Variable | Likely moderate cooldown |
| **Weapon Required** | No | Independent of weapons |

## Shield Mechanics

### Core Functionality
| Mechanic | Details | Notes |
|----------|---------|-------|
| **Shield Generation** | Converts max health % to shield | Sacrifices potential health |
| **Damage Absorption** | Shield takes damage before health | Standard shield behavior |
| **Bleed Reflection** | Attackers suffer bleeding | Offensive defense |
| **Shield Persistence** | Remains until depleted | No time decay |
| **Health Recovery** | Unknown mechanism | May recover unused shield |

### Risk vs Reward
- **Health Sacrifice:** Uses own vitality for protection
- **Offensive Defense:** Shield damages attackers
- **Strategic Resource:** Balance health vs shield
- **Combat Duration:** Longer fights benefit more

### Implementation Tracking

See [[Hemorrhagic Shield Perks.base]] for the complete database with implementation status and priority tracking.

## Tactical Usage

**Strengths:**
- Converts health into temporary protection
- Offensive capabilities through reflection
- Synergizes with aggressive playstyles
- Multiple upgrade paths for different builds
- No mana cost (uses health instead)

**Weaknesses:**
- Reduces maximum effective health
- Health sacrifice is permanent until recovered
- Limited by maximum health pool
- No protection during casting
- Requires careful health management

**Strategic Applications:**
- Pre-engagement preparation
- Boss fight phases with heavy damage
- Crowd control through bleed reflection
- Area denial with Reactive Barrier
- Sustain builds with Parasite Shield

## Class Identity - Torin

**Blood Magic Philosophy:**
- Epitomizes sacrifice for power
- Transforms weakness (health loss) into strength (protection)
- Encourages bold, aggressive positioning
- Represents blood magic's risk-reward nature

**Build Archetypes:**
- **Reactive Warrior:** Focus on Reactive Barrier explosions
- **Parasitic Fighter:** Self-sustaining shield through damage
- **Thorn Guardian:** Bleeding punishment for attackers
- **Balanced Defender:** Mixed defensive and offensive benefits

## Synergies

**With Blood Blade:**
- Both use health as resource
- Bleed synergies with all perks
- Risk management across multiple skills
- High-risk, high-reward playstyle

**With Life Leech Aura:**
- Health recovery supports shield costs
- Sustained combat viability
- Reduced risk from health sacrifice

**With Blood Barrier:**
- Layered defensive capabilities
- Different timing requirements
- Comprehensive protection strategy

## Balance Considerations

**Resource Management:**
- Health is finite and precious
- Shield efficiency must justify cost
- Recovery mechanisms needed
- Multiple blood skills compete for health

**Power Level:**
- Reflection damage must be meaningful
- Shield absorption must be substantial
- Perks provide clear value propositions
- Not overpowered compared to other defenses

## Implementation Challenges

**Technical Requirements:**
- Health-to-shield conversion system
- Damage reflection mechanics
- Bleed application on hit
- Shield visual effects

**Balance Testing:**
- Health percentage tuning
- Reflection damage scaling
- Perk value propositions
- Interaction with other systems

## Implementation Status

- **Status:** Conceptual design
- **Development:** Not yet implemented
- **Dependencies:** Shield system, health conversion
- **UI Needs:** Shield indicator, health cost display
- **Animation:** Shield formation and reflection effects

## Related

- [[Torin]] - Exclusive class user
- [[Blood]] - Thematic skill tree
- [[Shield]] - Protection mechanism
- [[Bleed]] - Reflection effect
- [[Defensive]] - Skill category
- [[Health]] - Resource cost