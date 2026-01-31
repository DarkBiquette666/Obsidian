---
type: skill
category: Spell
element: []
classes:
  - Torin
tags:
  - blood
  - spell
  - leech
  - chain
  - single_target
  - drain
status:
  - implemented
locked: true
skill Family: blood
---

# Vital Link

## Description
The caster connects to an enemy with a blood chain, leeching life over time. The chain breaks if the target is too far away, creating a dynamic tether that requires strategic positioning and target management.

## Lore
The Vital Link represents the most intimate form of blood magic - a direct connection between the life forces of caster and target. This crimson tether creates a parasitic bond that slowly drains the enemy's vitality while nourishing the Torin, but the connection demands proximity and constant vigilance.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Targeted Spell | Blood magic drain |
| **Activation Cost** | Variable Mana | Initial targeting cost |
| **Health Drain** | Variable/second | Continuous life steal |
| **Healing** | Proportional | Based on damage dealt |
| **Range Limit** | Variable distance | Chain breaks if exceeded |
| **Duration** | Until broken | Maintained connection |
| **Classes** | Torin | Blood magic specialist only |
| **Targets** | Single (base) | One enemy at a time |
| **Weapon Required** | No | Independent of weapons |

## Chain Mechanics

### Vital Tether System
| Mechanic | Details | Notes |
|----------|---------|-------|
| **Connection** | Direct link to target | Visible blood chain |
| **Health Drain** | Continuous damage over time | Steady life steal |
| **Range Dependency** | Breaks if too far | Requires positioning |
| **Healing Conversion** | Damage becomes healing | Life force transfer |
| **Visual Indicator** | Blood chain effect | Clear connection display |

### Positioning Requirements
- **Proximity Maintenance:** Must stay within range
- **Movement Restrictions:** Limited by tether length
- **Tactical Positioning:** Balance safety with range
- **Target Priority:** Choose high-value, stationary targets

### Implementation Tracking

See [[Vital Link Perks.base]] for the complete database with implementation status and priority tracking.

## Tactical Usage

**Strengths:**
- Sustained health recovery over time
- No ongoing mana cost after activation
- Powerful single-target focus
- Strong synergy with armor reduction
- Excellent for prolonged encounters

**Weaknesses:**
- Requires constant positioning awareness
- Limited by range restrictions
- Vulnerable while maintaining link
- Single target limitation (base)
- Chain can break unexpectedly

**Strategic Applications:**
- Boss fight sustain and damage
- Elite enemy elimination
- Tank role with continuous healing
- Combo with positioning skills
- Area control through threat positioning

## Class Identity - Torin

**Parasitic Connection:**
- Represents intimate blood magic mastery
- Shows control over life force itself
- Requires tactical positioning skill
- Embodies predator-prey relationship

**Combat Philosophy:**
- Encourages close-range engagement
- Rewards careful target selection
- Requires positioning awareness
- Promotes sustained combat approach

## Synergies

**With Blood Blade:**
- Corrosive Link enhances blade damage
- Both require close positioning
- Bleeding application enables Shared Siphon
- Health costs offset by link healing

**With Life Leech Aura:**
- Double life leech sources
- Incredible sustain potential
- Overlapping healing from multiple sources
- Enhanced tank capabilities

**With Defensive Skills:**
- Blood Barrier protects during vulnerable linking
- Hemorrhagic Shield provides additional protection
- Defensive perks support aggressive positioning

**With Tainted Blood:**
- Bleeding spread enables Shared Siphon
- Poison + life drain combination
- Multi-target damage over time
- Complex resource management

## Positioning Strategies

**Range Management:**
- Learn chain break distance
- Anticipate enemy movement patterns
- Position for multiple target access
- Balance safety with effectiveness

**Target Selection:**
- Prioritize high-health enemies
- Choose relatively stationary targets
- Consider enemy threat level
- Plan escape routes

## Balance Considerations

**Healing vs Risk:**
- Life gain must justify positioning risk
- Chain break penalties should be meaningful
- Range limitations create skill requirement
- Sustained healing shouldn't trivialize combat

**Multi-Target Scaling:**
- Shared Siphon must be balanced
- Multiple drains shouldn't be overpowered
- Positioning complexity should increase with targets
- Resource management becomes critical

## Implementation Challenges

**Technical Requirements:**
- Dynamic chain rendering system
- Range detection and break mechanics
- Life drain and conversion systems
- Multi-target chaining for Shared Siphon

**Visual Design:**
- Clear chain visibility
- Range indication
- Target highlighting
- Break warning systems

**Balance Testing:**
- Drain rate optimization
- Range distance tuning
- Perk value validation
- Multi-target interaction testing

## Implementation Status

- **Status:** Conceptual design
- **Development:** Not yet implemented
- **Dependencies:** Chain system, life drain mechanics
- **UI Needs:** Range indicators, target highlighting
- **Animation:** Blood chain effects, drain visualization

## Related

- [[Torin]] - Exclusive class user
- [[Blood]] - Thematic skill tree
- [[Leech]] - Core mechanic
- [[Chain]] - Connection mechanism
- [[Spell]] - Skill category
- [[Positioning]] - Tactical requirement