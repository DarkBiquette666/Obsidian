---
type: perk
skill: Blood Blade
category: transformation
tags:
  - aura_synergy
  - multi_target
  - area_effect
  - resource_scaling
  - life_leech
status: concept
skill Family: blood
---

# Blade Communion

## Description
When Life Leech Aura is active, Blood Blade transcends its single-target nature, achieving communion with all enemies within the aura's embrace. The blade splits its essence across multiple targets, attacking all simultaneously but dividing its power among them.

## Lore
The highest form of blood magic mastery - where the blade becomes one with the vampiric field itself. In this state of communion, the weapon exists in multiple places at once, its crimson essence flowing through the life-draining aura to strike at all who would dare enter its domain.

## Mechanics

### Transformation Requirements
- **Prerequisite:** Life Leech Aura must be active
- **Activation:** Automatic when both skills are active
- **Deactivation:** Reverts when Life Leech Aura is toggled off
- **Visual:** Blade appears ghostly, with ethereal copies at each target

### Multi-Target System
| Property | Base Value | With Communion |
|----------|------------|----------------|
| **Target Count** | 1 | All enemies in aura |
| **Damage Per Target** | 100% | 100% ÷ target count |
| **Bleed Application** | Single target | All targets simultaneously |
| **Range Limitation** | 1.5x weapon range | Aura radius only |
| **Attack Animation** | Single strike | Simultaneous strikes |

### Resource Scaling
- **Health Cost Multiplier:** Base cost × number of targets
- **Movement Penalty:** Additional -10% per target (max -50%)
- **Bleed Damage:** Full potency on each target despite damage split
- **Critical Strikes:** Calculated independently per target

## Strategic Applications

### Crowd Control Mastery
- **Area Dominance:** Control entire groups with bleeding
- **Positioning Power:** Force enemies to spread or suffer collective drain
- **Resource Management:** High costs require careful target selection
- **Escape Denial:** Mass bleeding prevents enemy retreat/healing

### Build Synergies

#### Perfect Synergies
- **Bleeding Resonance:** Each target's bleed amplifies Life Leech Aura
- **Drinker Blades:** Can consume bleeds from all targets for massive burst
- **Increased Bleed Damage:** Amplifies the guaranteed bleeds on all targets
- **Health Scaling:** More max health = more sustainable multi-targeting

#### Complex Interactions
- **Shared Siphon:** If enemies start bleeding, creates Vital Link network
- **Mimic Blades:** Spell casting triggers attacks on ALL communion targets
- **Conscious Blood:** Automated targeting becomes area-wide threat response

## Risk vs Reward

### Massive Benefits
- **Exponential Bleed Stacking:** Multiple targets = multiple bleeds for resonance
- **Area Control:** Complete battlefield domination when positioned correctly
- **Scaling Sustain:** More targets = more life leech (if they survive split damage)
- **Build Defining:** Transforms single-target into area-effect playstyle

### Significant Costs
- **Exponential Costs:** Health drain multiplies with targets
- **Positioning Vulnerability:** Must stay in range of multiple enemies
- **Movement Restriction:** Additional penalties for each target
- **Resource Starvation:** Can quickly drain health with large groups

## Playstyle Archetypes

### "Blade Conductor"
- **Core Concept:** Orchestrate blade strikes across battlefield
- **Positioning:** Central positioning to maximize aura coverage
- **Resource Management:** Balance targets vs sustainability
- **Combat Flow:** Enter groups, establish communion, control through bleeding

### "Vampiric Overlord"
- **Core Concept:** Maximum life leech from multiple sources
- **Synergy Focus:** Life Leech Aura + Bleeding Resonance + Blade Communion
- **Sustainability:** Extreme healing from multiple bleeding targets
- **Weakness:** Vulnerable to burst damage due to stationary nature

## Technical Implementation

### Detection System
- **Aura Integration:** Reads Life Leech Aura's target list
- **Real-time Updates:** Adjusts targets as enemies enter/leave aura
- **Performance Optimization:** Efficient multi-target calculation
- **Visual Feedback:** Clear indication of communion state

### Balance Mechanisms
- **Damage Split Formula:** `damage_per_target = base_damage / sqrt(target_count)`
- **Cost Scaling:** Linear multiplication prevents infinite scaling abuse
- **Movement Penalty Cap:** Prevents complete immobility
- **Range Dependency:** Maintains aura positioning requirements

## Implementation Status

**Status:** Concept - Ready for Development

### Development Requirements
- Integration with Life Leech Aura system
- Multi-target attack animation system
- Performance optimization for large groups
- Visual effects for simultaneous strikes
- Balance testing across different target counts

### Priority Justification
- **Build Defining:** Creates entirely new playstyle archetype
- **Synergy Rich:** Interacts meaningfully with multiple existing perks
- **Strategic Depth:** Adds positioning and resource management complexity
- **Visual Impact:** Spectacular multi-target blade strikes

## Related Concepts
- [[Blood Blade]] - Base skill
- [[Life Leech Aura]] - Required synergy
- [[Bleeding Resonance]] - Perfect combo perk
- [[Multi-Target]] - Gameplay transformation
- [[Area Effect]] - Coverage type
- [[Aura]] - Range dependency