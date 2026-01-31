---
type: perk
skill: Blood Blade
category: automation
tags:
  - spell_trigger
  - automation
  - combo_potential
  - tiered
status:
  - implemented
---

# Mimic Blades

## Description
Blood Blades have a chance to automatically attack when casting other skills, creating powerful spell-blade combos. This perk transforms Blood Blade into a reactive companion that enhances spell-casting playstyles.

## Mechanics

### Trigger System
- **Activation:** On any skill cast
- **Independent Check:** Each blade rolls separately
- **No Cooldown:** Can trigger repeatedly
- **Animation:** Quick strike animation

### Tier Scaling
| Tier | Trigger Chance | Notes |
|------|----------------|-------|
| Tier 1 | 25-35% | Occasional triggers |
| Tier 2 | 35-50% | Reliable activation |
| Tier 3 | 50-75% | Near-constant attacks |

### Incompatibility
- **Cannot combine with:** Conscious Blood
- **Reason:** Both automate blade behavior
- **Choice:** Reactive vs constant automation

## Strategic Applications

### Spell-Blade Hybrid
- **Casting Rhythm:** Weave spells for blade triggers
- **Combo Potential:** Chain skills for multiple attacks
- **Burst Windows:** Rapid casting = rapid blade strikes
- **Resource Efficiency:** Free attacks on spell casts

### Skill Synergies
- **Blood Barrier:** Defensive cast triggers offense
- **Anemic Curse:** Curse application with blade strike
- **Tainted Blood:** Poison spread with blade follow-up
- **Any Spell:** Universal trigger potential

## Build Considerations

### Ideal Builds
- **Caster Hybrids:** Spell-focused with blade support
- **Combo Specialists:** Chain multiple skills
- **Reactive Playstyle:** Response-based combat
- **Versatile Fighters:** Mixed damage types

### Optimization Tips
- **Cast Speed:** Faster casting = more triggers
- **Skill Rotation:** Plan casts for blade timing
- **Mana Management:** Balance casting for triggers
- **Positioning:** Stay in blade range

## Risk vs Reward

### Benefits
- **Free Damage:** No additional cost per trigger
- **Combo Enabler:** Links spells and attacks
- **Flexible Playstyle:** Adapts to any build
- **High Ceiling:** Skill expression through timing

### Limitations
- **RNG Dependent:** Not guaranteed triggers
- **Requires Casting:** Passive without spells
- **Positioning Needed:** Must be in blade range
- **Incompatibility:** Locks out Conscious Blood

## Implementation Status

**Status:** To Do

### Technical Requirements
- Skill cast detection system
- Per-blade probability rolls
- Trigger animation system
- Cast queuing compatibility
- Performance with rapid casting

### Balance Priorities
- Trigger chance tuning per tier
- Animation speed balancing
- Cast detection timing
- Combo prevention limits

### Visual Design
- Distinct trigger animation
- Cast-link visual effect
- Blade reaction feedback
- Clear activation indicators

## Related Concepts
- [[Blood Blade]] - Base skill
- [[Conscious Blood]] - Incompatible perk
- [[Spell]] - Trigger source
- [[Attack]] - Blade action
- [[Automation]] - Perk category
- [[Combo]] - Gameplay pattern