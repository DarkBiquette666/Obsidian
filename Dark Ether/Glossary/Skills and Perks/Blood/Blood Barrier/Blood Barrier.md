---
type: skill
category: Defensive
element: []
classes:
  - Torin
tags:
  - blood
  - barrier
  - defensive
  - energy
  - bleed_synergy
status: concept
locked: true
skill Family: blood
---

# Blood Barrier

## Description
The caster uses his mastery of blood to create a protective aura that accumulates energy from bleed inflicted on enemies. This energy can be released to reduce incoming damage for a short duration.

## Lore
The Blood Barrier represents the defensive aspect of Torin blood magic, transforming the suffering of enemies into protective power. By channeling the life force drained through bleeding wounds, the caster weaves a shield of vitality that can absorb tremendous punishment when properly charged.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Defensive Skill | Blood magic barrier |
| **Activation Cost** | 0 | Uses accumulated charges |
| **Resource Type** | Blood Energy Charges | Unique resource system |
| **Maximum Charges** | 100 | Charge capacity |
| **Charge Rate Limit** | 1 per 0.2 sec | Maximum accumulation speed |
| **Base Duration** | 0.5 sec | Barrier active time |
| **Base Reduction** | 1% per charge | 100 charges = 100% reduction |
| **Classes** | Torin | Blood magic specialist only |
| **Cooldown** | None (base) | Depends on charge accumulation |
| **Weapon Required** | No | Independent of weapons |

## Energy Accumulation System

### Passive Mechanics
| Mechanic | Details | Notes |
|----------|---------|-------|
| **Charge Source** | Enemy bleed effects | Any bleed on any enemy |
| **Charge Rate** | 1 charge per bleed tick | Limited by rate cap |
| **Rate Limit** | 0.2 sec minimum | Prevents instant charging |
| **Maximum Storage** | 100 charges | Full protection potential |
| **Charge Decay** | None | Charges persist indefinitely |
| **Visual Indicator** | Energy accumulation | Likely UI element |

### Synergy Requirements
- **Bleed Sources Required:** Blood Blade, weapon effects, other bleeding skills
- **Positioning:** Must stay engaged to accumulate charges
- **Timing:** Save charges for dangerous moments

## Activation Effects

### Damage Reduction
- **Base Effect:** 1% damage reduction per charge consumed
- **Maximum Protection:** 100% damage negation (100 charges)
- **Duration:** 0.5 seconds of protection
- **Consumption:** All charges used instantly
- **Timing:** Manual activation required

### Strategic Usage
- **Emergency Defense:** Save for dangerous attacks
- **Perfect Timing:** 0.5 seconds requires precision
- **Charge Management:** Balance accumulation vs usage

### Implementation Tracking

See [[Blood Barrier Perks.base]] for the complete database with implementation status and priority tracking.

## Tactical Usage

**Strengths:**
- Potential for complete damage immunity
- Synergizes perfectly with bleed builds
- No resource cost (uses charges)
- Scales with combat engagement
- Multiple perk options for different playstyles

**Weaknesses:**
- Requires bleed sources to function
- Very short duration (0.5 seconds)
- Manual activation timing critical
- Must stay in combat to charge
- All-or-nothing charge consumption

**Strategic Applications:**
- Perfect for Blood Blade builds
- Essential for high-risk blood magic
- Boss fight survival tool
- Burst damage mitigation
- Sustain build component (with perks)

## Class Identity - Torin

**Blood Magic Synergy:**
- Perfect companion to Blood Blade
- Transforms offensive bleeding into defense
- Represents blood magic balance (offense + defense)
- Encourages aggressive playstyle

**Build Archetypes:**
- **Balanced Blood Warrior:** Offense and defense combined
- **Parasitic Fighter:** Close-range with barrier extensions
- **Persistent Guardian:** Sustained protection focus
- **Perfect Timer:** High-skill ephemeral barrier usage

## Balance Considerations

**Risk vs Reward:**
- High potential protection requires constant engagement
- Short duration demands precise timing
- Charge accumulation requires bleed management
- Perk choices dramatically change playstyle

**Synergy Dependencies:**
- Completely dependent on bleed sources
- Better with multiple bleed skills
- Scales with combat duration
- Rewards aggressive positioning

## Implementation Status

- **Status:** Conceptual design
- **Development:** Not yet implemented
- **Dependencies:** Requires bleed tracking system
- **UI Needs:** Charge indicator, timing display
- **Animation:** Barrier visual effects

## Related

- [[Torin]] - Exclusive class user
- [[Blood]] - Thematic skill tree
- [[Blood Blade]] - Primary synergy skill
- [[Bleed]] - Resource generation mechanic
- [[Defensive]] - Skill category
- [[Barrier]] - Protection mechanism