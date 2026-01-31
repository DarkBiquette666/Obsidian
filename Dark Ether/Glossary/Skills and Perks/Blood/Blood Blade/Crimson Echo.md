---
type: perk
skill: Blood Blade
category: memory
tags:
  - vital_link_synergy
  - memory_system
  - progressive_bonus
  - target_tracking
  - tactical_complexity
status: concept
skill Family: blood
---

# Crimson Echo

## Description
Blood Blade develops a supernatural memory for targets that have been connected through Vital Link. When a vital connection is severed - whether by distance, death, or choice - the blade retains an echo of that bond, gaining devastating accuracy and power against those who have felt its vampiric touch.

## Lore
Blood remembers blood. Once the crimson tether has tasted an enemy's life force, that essence becomes permanently etched into the blade's consciousness. Even when the link breaks, the weapon carries forward the memory of that connection, growing stronger with each severed bond until it becomes a hunter of familiar prey.

## Mechanics

### Echo Generation System
- **Trigger:** Vital Link breaks (any reason: distance, death, manual toggle)
- **Memory Duration:** 60 seconds per echo
- **Maximum Echoes:** 5 simultaneous echoes
- **Stack Behavior:** New echoes replace oldest when at capacity
- **Target Recognition:** Blade identifies echoed enemies automatically

### Progressive Echo Bonuses
| Echo Count | Damage Bonus | Additional Effects |
|------------|--------------|-------------------|
| **1 Echo** | +50% damage | +10% critical chance |
| **2 Echoes** | +75% damage | +15% attack speed |
| **3 Echoes** | +100% damage | +20% bleed penetration |
| **4 Echoes** | +125% damage | +25% range extension |
| **5 Echoes** | +150% damage | Echoes spread to nearby enemies |

### Memory Mechanics
- **Individual Tracking:** Each echo applies only to its specific target
- **Damage Stacking:** Multiple echoes on same target stack multiplicatively
- **Visual Marking:** Echoed enemies have distinctive crimson outline
- **Range Independence:** Echo bonuses work at any distance

## Strategic Applications

### Link Breaking Mastery
- **Tactical Severing:** Deliberately break links to generate echoes
- **Positioning Play:** Use distance to create echoes while maintaining safety
- **Target Cycling:** Rotate through enemies to build echo library
- **Memory Banking:** Build echoes during setup phase for later advantage

### Echo Management
- **Priority Targeting:** Focus echoes on high-value enemies
- **Duration Awareness:** Refresh important echoes before expiration
- **Stack Optimization:** Plan link breaks to maximize echo overlap
- **Battlefield Memory:** Track echoed enemies across complex fights

## Build Synergies

### Vital Link Integration
- **Shared Siphon:** Multiple links = multiple potential echoes
- **Elastic Tether:** Extended range helps create controlled breaks
- **Life Link Mastery:** Enhanced links create more powerful echoes
- **Twin Tethers:** Double links provide echo generation redundancy

### Blood Blade Enhancement
- **Health Scaling:** More max health supports aggressive linking for echoes
- **Increased Range:** Better positioning for echo-enhanced strikes
- **Mimic Blades:** Spell triggers benefit from echo damage bonuses
- **Drinker Blades:** Echo-enhanced bleeds provide massive burst potential

### Complex Interactions
- **Blade Communion:** Echo bonuses apply to all communion targets
- **Hemorrhagic Catalyst:** Echo-enhanced amplification effects
- **Conscious Blood:** Automated targeting prioritizes echoed enemies

## Risk vs Reward

### Echo System Benefits
- **Escalating Power:** Each broken link makes blade more dangerous
- **Tactical Flexibility:** Choose when to break links for optimal timing
- **Long-term Planning:** Build echo library for future encounters
- **Counter-Play:** Turn link vulnerabilities into strategic advantages

### Memory System Costs
- **Link Dependency:** Requires Vital Link investment for full effectiveness
- **Setup Time:** Must establish and break links before reaching peak power
- **Target Limitation:** Echoes only work against specific remembered enemies
- **Memory Management:** Must track multiple timers and targets

## Playstyle Archetypes

### "Link Breaker"
- **Philosophy:** Connections are meant to be severed for power
- **Tactics:** Strategic link establishment and controlled breaking
- **Timing:** Master the rhythm of connect-break-strike cycles
- **Build Focus:** Maximize link establishment speed and range

### "Memory Hunter"
- **Identity:** Blade that never forgets its prey
- **Strategy:** Build comprehensive echo library early in encounters
- **Execution:** Patient setup followed by devastating focused strikes
- **Mastery:** Perfect timing of link breaks for maximum echo value

### "Echo Assassin" 
- **Concept:** Use echoes for single-target elimination
- **Approach:** Accumulate multiple echoes on priority targets
- **Finisher:** Massive echo-stacked damage for instant kills
- **Risk Management:** Balance aggressive linking with survival needs

## Advanced Mechanics

### Echo Resonance (5-Echo Bonus)
- **Spread Radius:** 3 units around echoed target
- **Spread Duration:** 30 seconds (half of original echo)
- **Spread Damage:** 50% of original echo bonus
- **Chain Limit:** Spread echoes cannot create new spreads

### Echo Refresh System
- **Re-linking:** Establishing new Vital Link to echoed target refreshes echo
- **Duration Reset:** Fresh echo gets full 60-second duration
- **Bonus Preservation:** Echo count and bonuses maintained
- **Strategic Value:** Allows indefinite echo maintenance with active play

## Technical Implementation

### Memory Database
- **Target Identification:** Unique enemy ID tracking system
- **Timer Management:** Individual countdown per echo
- **Bonus Calculation:** Real-time damage modifier application
- **Visual Integration:** Echo status display and target highlighting

### Performance Optimization
- **Memory Cleanup:** Automatic removal of expired echoes
- **Target Validation:** Handle enemy death and respawning
- **Effect Caching:** Pre-calculate bonus combinations
- **UI Updates:** Efficient echo status communication

## Implementation Status

**Status:** Concept - Medium Priority

### Development Complexity
- **Medium:** Requires memory system and target tracking
- **Dependencies:** Vital Link implementation, visual marking system
- **Innovation:** First perk with persistent memory mechanics
- **Testing Needs:** Complex timing and interaction scenarios

### Balance Considerations
- **Power Curve:** Echoes provide significant but not overwhelming bonuses
- **Time Pressure:** 60-second duration creates urgency without stress
- **Skill Expression:** Rewards strategic thinking and timing mastery
- **Build Investment:** Requires commitment to both skills for full value

## Related Concepts
- [[Blood Blade]] - Base skill
- [[Vital Link]] - Required synergy
- [[Memory System]] - Core mechanic
- [[Progressive Bonus]] - Scaling type
- [[Target Tracking]] - Technical system
- [[Link Breaking]] - Strategic technique