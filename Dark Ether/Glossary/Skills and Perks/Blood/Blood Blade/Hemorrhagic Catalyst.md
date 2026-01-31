---
type: perk
skill: Blood Blade
category: amplification
tags:
  - bleed_amplification
  - dot_enhancement
  - transformation
  - synergy_enabler
  - support_role
status: concept
skill Family: blood
---

# Hemorrhagic Catalyst

## Description
Blood Blade abandons its natural bleeding properties to become a catalyst for existing wounds. Instead of applying new bleeds, each strike dramatically amplifies all bleeding effects already present on the target, transforming the blade into a wound-enhancing instrument of prolonged agony.

## Lore
The blade learns to read the crimson map of existing wounds, not to add new cuts but to tear them deeper, wider, longer. This technique represents the difference between a warrior and a true blood artist - knowing when to strike and when to perfect the masterpiece already begun.

## Mechanics

### Core Transformation
- **Removes:** Direct bleed application from Blood Blade strikes
- **Adds:** Amplification of existing bleeding effects
- **Requires:** Target must already be bleeding for effect to trigger
- **Timing:** Amplification occurs on successful blade hit

### Amplification Formula
| Bleed Property | Base Value | With Catalyst |
|----------------|------------|---------------|
| **Bleed Damage** | 100% | 300% (+200%) |
| **Bleed Duration** | 100% | 200% (+100%) |
| **Stack Limit** | Normal | +2 additional stacks |
| **Spread Chance** | Base | +25% spread chance |

### Interaction Rules
- **Multiple Bleeds:** Amplifies ALL bleeding effects on target
- **Different Sources:** Works with any bleed (weapon, skill, environmental)
- **Stack Preservation:** Existing stacks maintained, new enhanced stacks added
- **Diminishing Returns:** Each amplification on same target reduces effect by 20%

## Strategic Applications

### Setup-Finish Playstyle
- **Phase 1:** Apply bleeds through other sources
- **Phase 2:** Blood Blade strikes to amplify wounds  
- **Phase 3:** Maintain blade presence for continuous amplification
- **Optimization:** Time amplification at maximum bleed stacks

### Multi-Source Integration
- **Tainted Blood:** Applies initial bleeds for amplification
- **Weapon Bleeds:** Base bleeding enhanced by blade strikes
- **Environmental Hazards:** Amplify naturally occurring bleeding
- **Team Play:** Amplify party member bleeds in multiplayer

## Build Synergies

### Perfect Combinations
- **Drinker Blades:** Amplified bleeds = massive burst consumption
- **Tainted Blood:** Reliable bleed application for amplification setup
- **Increased Bleed Damage:** Multiplicative with amplification (300% × 150% = 450%)
- **Health Scaling:** More health = more blade uptime = more amplifications

### Complex Interactions
- **Bleeding Resonance:** Amplified bleeds provide more resonance bonus
- **Shared Siphon:** Amplified bleeding spreads enhanced Vital Links
- **Mimic Blades:** Spell casting triggers amplification on bleeding targets

## Risk vs Reward

### Transformation Benefits
- **Exponential Scaling:** Turns moderate bleeds into devastating wounds
- **Build Synergy:** Enables specialized bleed-focused builds
- **Tactical Depth:** Requires setup and timing mastery
- **Late Game Power:** Scales incredibly well with other bleed sources

### Strategic Trade-offs
- **Setup Dependency:** Useless against non-bleeding targets
- **Source Requirement:** Must have other bleed application methods
- **Timing Critical:** Optimal use requires bleed stack management
- **Specialization Lock:** Commits build heavily toward bleed focus

## Playstyle Archetypes

### "Wound Artist"
- **Core Philosophy:** Perfect existing damage rather than create new
- **Weapon Choice:** High bleed chance weapons for setup
- **Skill Priority:** Tainted Blood → Blood Blade → Amplification mastery
- **Combat Flow:** Apply, amplify, consume cycle

### "Bleed Surgeon" 
- **Precision Focus:** Surgical strikes to enhance existing wounds
- **Timing Mastery:** Wait for optimal bleed stacks before amplifying
- **Resource Efficiency:** Maximize amplification value per health cost
- **Synergy Web:** Integrate with all available bleed sources

## Technical Implementation

### Bleed Detection System
- **Stack Recognition:** Identify all bleeding effects on target
- **Source Tracking:** Distinguish between different bleed sources
- **Amplification Application:** Apply enhancements without overriding
- **Duration Management:** Handle extended durations properly

### Visual Design
- **Amplification Effect:** Blood wounds visibly intensify on blade hit
- **Stack Visualization:** Clear indication of enhanced bleeding
- **Blade Animation:** Different strike pattern for amplification
- **Feedback Systems:** Audio/visual confirmation of successful amplification

## Balance Considerations

### Power Scaling Control
- **Diminishing Returns:** Prevents infinite amplification loops
- **Stack Limits:** Caps maximum enhancement potential  
- **Duration Caps:** Prevents permanent bleeding effects
- **Cost Scaling:** Health costs increase with amplification count

### Build Diversity Impact
- **Specialization Reward:** High payoff for focused builds
- **Versatility Penalty:** Less effective in general-purpose builds
- **Synergy Requirement:** Encourages specific perk combinations
- **Skill Floor/Ceiling:** Easy to use poorly, hard to master

## Implementation Status

**Status:** Concept - High Priority

### Technical Challenges
- Bleed effect modification system
- Multiple source interaction handling
- Performance with many simultaneous amplifications
- Balance testing across different bleed sources

### Design Innovation
- **First Support-Role Weapon Perk:** Changes fundamental weapon role
- **Interaction Complexity:** Creates new perk combination strategies
- **Build Archetype:** Enables entirely new playstyle possibilities

## Related Concepts
- [[Blood Blade]] - Base skill
- [[Bleed]] - Core mechanic
- [[Drinker Blades]] - Perfect synergy perk
- [[Tainted Blood]] - Setup skill
- [[Dot Enhancement]] - Damage type
- [[Amplification]] - Core mechanic