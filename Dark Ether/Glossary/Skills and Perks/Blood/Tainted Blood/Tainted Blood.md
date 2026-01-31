---
type: skill
category: Aura
element:
  - Poison
classes:
  - Torin
tags:
  - blood
  - aura
  - poison
  - toggle
  - self_damage
  - spread
status: concept
locked: true
skill Family: blood
TQ_show_tree: true
---

# Tainted Blood

## Description
An aura (toggle) that infects the caster with a potent toxin, allowing him to spread this poison to his enemies through his blood attacks. The caster becomes a living weapon of toxic vengeance, transforming their own corruption into a contagious curse.

## Lore
Tainted Blood represents the darkest aspect of Torin blood magic - the willingness to poison one's own life force to become a vector of destruction. This forbidden technique transforms the caster into a walking plague, their very blood becoming a weapon that spreads suffering to all who dare spill it.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Toggle Aura | Self-poisoning aura |
| **Activation Cost** | None | No initial cost |
| **Ongoing Cost** | Health drain | Continuous self-damage |
| **Self-Poison Rate** | 1 stack/second | Progressive self-harm |
| **Self-Poison Damage** | Variable per stack | Escalating damage |
| **Maximum Stacks** | Variable | Self-damage cap |
| **Classes** | Torin | Blood magic specialist only |
| **Duration** | Infinite | Until toggled off |
| **Weapon Required** | No | Independent of weapons |

## Toxin Mechanics

### Self-Poisoning System
| Mechanic | Details | Notes |
|----------|---------|-------|
| **Stack Accumulation** | +1 stack per second | Continuous buildup |
| **Damage Scaling** | Variable per stack | Escalating danger |
| **Stack Maximum** | Configurable cap | Prevents infinite buildup |
| **Stack Transfer** | Bleeding removes 1 self-stack | Risk mitigation |
| **Toggle Control** | Can be turned off | Player agency |

### Poison Spreading
- **Trigger:** All bleeding effects applied by caster
- **Effect:** Target gains poison stack + caster loses 1 self-stack
- **Synergy:** Rewards frequent bleeding application
- **Risk Management:** Active bleeding reduces self-damage
- **Scaling:** More enemies = less self-poison

## Perks System

The Tainted Blood skill can be enhanced with various perks that modify its behavior and effectiveness. Each perk offers unique strategic opportunities and build possibilities.

### Implementation Tracking

See [[Tainted Blood Perks.base]] for the complete database with implementation status and priority tracking.

## Tactical Usage

**Strengths:**
- Spreads poison without additional mana cost
- Risk mitigation through active bleeding
- Powerful area control with right perks
- Synergizes with all blood/bleed skills
- Toggle control allows tactical usage

**Weaknesses:**
- Continuous self-damage when active
- Requires frequent bleeding to stay safe
- Stack buildup creates escalating danger
- Must maintain aggressive playstyle
- Risk of death if not carefully managed

**Strategic Applications:**
- Crowd control through poison spreading
- Sustained damage-over-time builds
- Aggressive multi-target combat
- Synergy with Blood Blade and bleeding weapons
- Area denial through toxic explosions

## Class Identity - Torin

**Ultimate Sacrifice:**
- Represents willingness to corrupt own body
- Shows commitment to victory at any cost
- Transforms personal suffering into weapon
- Epitomizes blood magic risk philosophy

**Tactical Integration:**
- Perfect with Blood Blade (constant bleeding)
- Synergizes with Life Leech Aura (health recovery)
- Complements all bleeding-focused builds
- Requires defensive skills for survival

## Synergies

**With Blood Blade:**
- Constant bleeding application transfers poison
- Reduces self-poison stacks continuously
- Creates poison + bleed combos on enemies
- Enables Toxic Explosion triggers

**With Life Leech Aura:**
- Health recovery offsets self-poison damage
- Sustained combat viability
- Better risk management
- Enables longer aura usage

**With Blood Barrier:**
- Blood Purge perk creates powerful synergy
- Stack conversion to invulnerability
- Defensive option for accumulated risk
- Strategic resource management

## Risk Management Strategies

**Active Mitigation:**
- Frequent bleeding application essential
- Target multiple enemies when possible
- Monitor stack levels carefully
- Toggle off during dangerous moments

**Build Requirements:**
- Reliable bleeding sources mandatory
- Health recovery highly recommended
- Defensive options for emergencies
- Careful resource management

## Balance Considerations

**Self-Damage Scaling:**
- Must be meaningful threat
- Should encourage active play
- Cannot be trivially ignored
- Scales with risk tolerance

**Poison Effectiveness:**
- Enemy poison must justify self-risk
- Damage should scale appropriately
- Duration should matter tactically
- Spread mechanics must feel impactful

## Implementation Challenges

**Technical Requirements:**
- Poison stack system (self and enemies)
- Toggle aura mechanics
- Stack transfer on bleeding
- Cross-skill interactions (Blood Purge)

**Balance Testing:**
- Self-damage vs enemy damage ratios
- Stack accumulation rates
- Perk value propositions
- Risk vs reward optimization

## Implementation Status

- **Status:** Conceptual design
- **Development:** Not yet implemented
- **Dependencies:** Poison system, aura mechanics
- **UI Needs:** Stack indicators, toggle status
- **Animation:** Toxic aura effects

## Related

- [[Torin]] - Exclusive class user
- [[Blood]] - Thematic skill tree
- [[Poison]] - Status effect
- [[Aura]] - Skill mechanism
- [[Toggle Skill]] - Activation type
- [[Bleed]] - Synergy mechanism