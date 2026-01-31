---
type: perk
skill: Vital Link
category: scaling_enhancement
tags:
  - bleeding_synergy
  - stacking_bonus
  - scaling_drain
  - preparation_reward
status:
  - implemented
---

# Hemorrhagic Catalyst

## Description
Increases life drain by 5% per bleeding stack on the linked enemy, up to a maximum of +150% (30 stacks). This perk rewards patience and preparation, turning sustained bleeding application into massive sustain potential.

## Mechanics

### Scaling System
- **Base Bonus:** +5% per bleeding stack
- **Maximum Stacks:** 30 for full bonus
- **Total Bonus:** Up to +150% drain rate
- **Real-Time Update:** Adjusts with stack changes
- **Multiplicative:** Stacks with other bonuses

### Stack Calculation
| Bleed Stacks | Drain Bonus | Total Efficiency |
|--------------|-------------|------------------|
| 1 | +5% | 105% |
| 5 | +25% | 125% |
| 10 | +50% | 150% |
| 20 | +100% | 200% |
| 30 | +150% | 250% (cap) |

### Dynamic Adjustment
- **Stack Gain:** Instant drain increase
- **Stack Loss:** Immediate reduction
- **Continuous Monitoring:** Real-time tracking
- **Visual Feedback:** Stack counter display

## Bleeding Synergy

### Application Methods
- **Blood Blade:** Primary bleeding source
- **Multi-Hit:** Rapid stack building
- **Duration Extension:** Maintain high stacks
- **Refresh Timing:** Keep stacks active

### Stack Management
- **Building Phase:** Apply bleeding rapidly
- **Maintenance Phase:** Refresh before expiry
- **Peak Performance:** Sustain maximum stacks
- **Resource Balance:** Mana for applications

## Strategic Depth

### Preparation Rewards
- **Setup Time:** Investment in stacking
- **Patience Payoff:** Massive drain at peak
- **Skill Expression:** Stack management mastery
- **Risk vs Reward:** Time to build vs immediate drain

### Combat Patterns
- **Ramp-Up:** Gradual power increase
- **Burst Potential:** High stacks = high heal
- **Sustained Fighting:** Better in long battles
- **Boss Specialization:** Excel against high HP

## Build Integration

### Bleeding Focused Builds
- **Blood Blade Mastery:** Maximum synergy
- **Attack Speed:** Faster stack application
- **Bleeding Duration:** Easier maintenance
- **Multi-Strike:** Multiple applications

### Synergy Combinations
- **Shared Siphon:** Spread to bleeding enemies
- **Parasitic Resonance:** Combine with poison
- **Twin Tethers:** Stack on both targets
- **Vampiric Overdrain:** Multiplicative scaling

## Optimization Strategies

### Stack Building
- **Fast Application:** Priority on speed
- **Efficient Rotation:** Optimal skill sequence
- **Resource Management:** Sustain applications
- **Target Selection:** High-health for payoff

### Peak Performance
- **30-Stack Goal:** Maximum efficiency
- **Maintenance Priority:** Never let stacks fall
- **Burst Windows:** Time high-drain phases
- **Recovery Planning:** Rebuild if stacks drop

## Mathematical Scaling

### Efficiency Curves
- **Linear Growth:** Consistent 5% per stack
- **Breakpoints:** 10 (50%), 20 (100%), 30 (150%)
- **Sweet Spot:** 15-20 stacks for efficiency
- **Diminishing Returns:** After 20, less critical

### Damage Calculation
- **Base Drain:** X health/second
- **With 30 Stacks:** 2.5X health/second
- **Other Multipliers:** Stack multiplicatively
- **Final Output:** Can exceed 5X with full build

## Implementation Status

**Status:** To Do

### Technical Requirements
- Bleeding stack tracking system
- Real-time drain calculation
- Stack visualization UI
- Performance optimization
- Dynamic update system

### Balance Considerations
- Per-stack bonus tuning
- Maximum stack limit
- Interaction with other multipliers
- Stack duration vs refresh
- Build diversity impact

### Visual Design
- Stack counter display
- Drain rate indicator
- Visual scaling with stacks
- Bleeding effect intensity
- UI clarity at high stacks

### Testing Priorities
- Stack building feel
- Maintenance difficulty
- Payoff satisfaction
- Performance impact
- Visual clarity

## Related Concepts
- [[Vital Link]] - Base skill
- [[Bleed]] - Core mechanic
- [[Blood Blade]] - Primary synergy
- [[Stacking]] - Scaling system
- [[Preparation]] - Playstyle
- [[Scaling]] - Growth mechanic
- [[Shared Siphon]] - Combo potential