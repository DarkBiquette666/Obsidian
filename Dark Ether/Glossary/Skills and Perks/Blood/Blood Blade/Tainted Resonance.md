---
type: perk
skill: Blood Blade
category: self_poison
tags:
  - tainted_blood_synergy
  - poison_transformation
  - self_harm_benefit
  - damage_conversion
  - vampiric_healing
status: concept
skill Family: blood
---

# Tainted Resonance

## Description
When the wielder embraces corruption by allowing their own Tainted Blood to poison their veins, Blood Blade resonates with this toxic sacrifice. The blade abandons its bleeding nature to become a conduit of poisonous vitality, applying venomous wounds while drawing sustenance from its toxic strikes.

## Lore
Only the most devoted practitioners of blood magic dare to poison their own life force for power. When tainted essence flows through both wielder and weapon, a dark resonance forms - the blade learns to channel corruption as strength, transforming self-inflicted suffering into a weapon that both poisons enemies and nourishes its master.

## Mechanics

### Activation Requirements
- **Prerequisite:** Must have Tainted Blood active on yourself
- **Poison Immunity:** Must be poisoned by your own Tainted Blood
- **Sustain Condition:** Effect lasts only while self-poisoned
- **Deactivation:** Reverts when poison is removed/expires

### Poison Transformation
| Property | Base Blood Blade | Tainted Resonance |
|----------|------------------|-------------------|
| **Status Effect** | 100% Bleed chance | 100% Poison chance |
| **Effect Duration** | 5.0 sec bleed | 6.0 sec poison |
| **Damage Factor** | 200% bleed damage | 250% poison damage |
| **Damage Type** | Physical + DoT | Poison + DoT |
| **Life Steal** | None | 3% max HP per hit |
| **Stack Behavior** | Bleed stacks | Poison stacks |

### Vampiric Poison System
- **Healing Per Hit:** 3% of maximum health regardless of damage dealt
- **Healing Source:** Direct life force absorption from poisoned targets
- **Multi-Target:** Each target hit provides individual healing
- **Poison Synergy:** Healing scales with poison damage multipliers

## Strategic Applications

### Self-Poison Mastery
- **Controlled Corruption:** Maintain poison levels for sustained transformation  
- **Risk Management:** Balance poison damage against healing benefits
- **Timing Windows:** Activate when poison benefits outweigh costs
- **Purification Strategy:** Know when to cleanse for tactical advantages

### Combat Transformation
- **Damage Type Shift:** Switch from physical/bleed to poison-based builds
- **Sustain Integration:** Reliable healing source independent of enemy types  
- **Stack Interaction:** Poison stacks enable different perk synergies
- **Build Pivot:** Transform blood blade builds into poison-hybrid builds

## Build Synergies

### Tainted Blood Integration
- **Symbiotic Toxin:** Enhanced self-poison effects boost blade transformation
- **Blood Purge:** Strategic poison cleansing for tactical form changes
- **Virulent Strain:** Poison spread mechanics work with blade-applied poison
- **Toxic Explosion:** Poisoned enemies become area damage sources

### Transformed Blood Blade Interactions
- **Drinker Blades:** Consume poison stacks for massive burst damage
- **Health Scaling:** More max health = better healing per hit sustainability
- **Increased Range:** Extended reach for poison application and healing
- **Mimic Blades:** Spell triggers apply poison instead of bleed

### Complex Synergies  
- **Blade Communion:** Poison all aura enemies + mass healing from multiple hits
- **Hemorrhagic Catalyst:** Amplifies existing poisons instead of bleeds
- **Crimson Echo:** Echo bonuses enhance poison damage and healing

## Risk vs Reward Analysis

### Poison Transformation Benefits
- **Consistent Healing:** 3% max HP per hit provides reliable sustain
- **Enhanced DoT:** 250% poison factor exceeds base 200% bleed factor
- **Damage Type Flexibility:** Access poison-specific resistances and bonuses
- **Build Diversification:** Opens poison-focused build paths

### Self-Poison Costs
- **Ongoing Damage:** Must maintain poison on self for transformation
- **Resource Competition:** Tainted Blood competes with other skill slots
- **Vulnerability Window:** Poison cleansing removes both damage and benefits
- **Build Commitment:** Requires investment in poison resistance/management

## Playstyle Archetypes

### "Toxic Vampire"
- **Philosophy:** Embrace corruption to gain power over life and death
- **Core Loop:** Self-poison → Transform blade → Heal through poison strikes
- **Mastery:** Balance poison damage taken with healing gained
- **Identity:** Warrior who thrives on controlled self-destruction

### "Venom Dancer"
- **Strategy:** Master poison timing for optimal transformation windows
- **Tactics:** Apply/cleanse poison strategically for form control
- **Resource Management:** Optimize poison duration vs healing opportunities  
- **Advanced Play:** Chain poison applications for extended transformed state

### "Corruption Conduit"
- **Concept:** Channel environmental poison into weapon power
- **Environmental Abuse:** Use poison hazards to maintain transformation
- **Sustain Focus:** Maximize healing per hit through positioning
- **Survival Specialist:** Turn poison weakness into defensive strength

## Technical Implementation

### Poison Detection System
- **Self-Poison Verification:** Confirm poison source is own Tainted Blood
- **State Monitoring:** Continuous tracking of poison status
- **Transformation Toggle:** Instant property changes on poison state change
- **Effect Application:** Replace bleed with poison on successful hits

### Healing Integration
- **Health Calculation:** 3% of current maximum health (not base)
- **Hit Registration:** Ensure healing occurs on successful blade contact
- **Multi-Target Handling:** Individual healing per target struck
- **Display Integration:** Show healing numbers distinctly from damage

## Balance Mechanisms

### Power Level Control
- **Self-Damage Cost:** Ongoing poison damage balances increased power
- **Healing Rate:** 3% per hit provides good sustain without triviality
- **Poison Factor:** 250% strong enough to justify transformation costs
- **Activation Requirement:** Need Tainted Blood prevents free access

### Abuse Prevention
- **Poison Source Verification:** Only works with self-inflicted poison
- **State Dependency:** No transformation without active self-poison
- **Duration Limits:** Tied to poison duration prevents permanent state
- **Resource Competition:** Competes with other perk/skill combinations

## Advanced Mechanics

### Poison Stack Interactions
- **Stack Building:** Each hit applies fresh poison stack
- **Duration Refresh:** New poisons don't override, they stack
- **Maximum Stacks:** Standard poison stacking rules apply
- **Cross-Source Compatibility:** Works with any poison on target

### Healing Optimization
- **Health Scaling Bonuses:** Effects that increase max health improve healing
- **Hit Rate Scaling:** Attack speed directly affects healing rate
- **Multi-Target Scaling:** Area effects multiply healing opportunities
- **Efficiency Calculation:** Healing vs self-poison damage optimization

## Implementation Status

**Status:** Concept - Medium Priority  

### Technical Requirements
- Self-poison detection and verification system
- Damage type transformation mechanics
- Healing per hit implementation
- Visual effects for poison transformation
- Integration with Tainted Blood skill system

### Design Innovation
- **Self-Harm Synergy:** First perk requiring deliberate self-damage
- **Damage Type Pivot:** Dynamic weapon behavior transformation
- **Sustain Integration:** Built-in healing mechanic for aggressive play
- **Cross-Skill Dependency:** Complex interaction between two distinct skills

## Related Concepts
- [[Blood Blade]] - Base skill
- [[Tainted Blood]] - Required synergy skill
- [[Poison]] - Transformed damage type
- [[Self Poison]] - Activation mechanic
- [[Vampiric]] - Healing type
- [[Damage Conversion]] - Core transformation
- [[DoT]] - Damage over time mechanics