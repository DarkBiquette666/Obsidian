---
type: skill
category: Spell
element:
  - Cold
classes: []
tags:
  - spell
  - aura
  - cold
  - chill
  - persistent
  - toggle
status: implemented
locked: false
skill Family: elemental
---

# Frost Aura

## Description
A chilling aura that surrounds the caster, continuously applying cold effects to nearby enemies. This persistent spell creates a field of intense cold that follows the caster and weakens all enemies within its radius.

## Lore
The Frost Aura channels the numbing cold of the void, creating a sphere of freezing energy that saps the strength and speed of enemies. This ancient technique was developed by mages who sought to control the battlefield through environmental manipulation.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Spell | Persistent aura spell |
| **Damage Base** | 9-14 | Continuous cold damage |
| **Damage Type** | Cold | Freezing damage over time |
| **Cast Time** | 0.0 sec | Instant activation |
| **Critical Chance** | 5% | Standard spell crit rate |
| **Cost** | 10 Mana | Activation cost only |
| **Cooldown** | None | Can be toggled freely |
| **Duration** | 10.0 sec | Base duration per activation |
| **Lifespan** | Infinite | While toggled on |
| **Classes** | None | Currently unrestricted |
| **Weapon Required** | No | Independent of weapons |
| **Movement Speed** | 50% | Significantly reduced |
| **Toggleable** | Yes | Can be turned on/off |

## Aura Properties

| Propriété | Valeur | Description |
|-----------|--------|-------------|
| **Follow Caster** | Yes | Moves with the player |
| **Chill Intensity** | 100% | Maximum chill effect |
| **Persistent** | Yes | Remains active until toggled |
| **Range** | Variable | Depends on aura radius |
| **Effect Type** | Continuous | Constant application |
| **Mana Drain** | None | No ongoing cost |

## Effects

### Primary Effects
- **Chill Application:** Continuously applies chill to enemies in range
- **Cold Damage:** Deals steady cold damage over time  
- **Movement Debuff:** Slows affected enemies
- **Area Denial:** Controls battlefield positioning

### Chill Mechanics
- **Intensity:** 100% chill power
- **Duration:** Continuous while in aura
- **Stacking:** Effects stack with other cold sources
- **Resistance:** Reduced by cold resistance

## Tactical Usage

**Strengths:**
- No ongoing mana cost after activation
- Toggleable for resource management
- Continuous area control
- Excellent for defensive strategies
- Synergizes with cold damage builds

**Weaknesses:**
- Severely reduces movement speed (50%)
- Limited initial duration (10 seconds)
- No direct damage burst potential
- Currently no class restrictions (may be oversight)
- Requires close proximity to enemies

**Strategic Applications:**
- Tank builds for sustained combat
- Area denial in chokepoints
- Crowd control for group combat
- Defensive positioning tool
- Setup for cold-based combos

## Synergies

**Cold Damage Builds:**
- Cold damage bonuses increase damage
- Chill effect bonuses improve crowd control
- Cold penetration helps against resistant enemies

**Aura Builds:**
- Aura effect bonuses improve all aspects
- Aura radius increases expand coverage
- Aura duration extends effectiveness

**Defensive Builds:**
- Combines well with damage reduction
- Synergizes with life/energy shield builds
- Good with regeneration effects

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Frost Aura/frost_aura.tres`
- **Behavior:** `frost_aura_behavior.gd`
- **Scene:** `Frost Aura.tscn`
- **Icon:** `frost_aura_icon_1024x1024.png`
- **Status:** Implemented and unlocked
- **Main Skill:** No (secondary skill)

## Technical Notes

- Toggle mechanism allows resource management
- Follows caster movement automatically
- Chill intensity set to maximum (100%)
- Duration timer resets on re-activation
- No weapon dependency

## Future Considerations

- Class restrictions may be added
- Perk system not yet implemented
- Balance adjustments for movement penalty
- Potential mana drain over time

## Related

- [[Cold Damage]] - Primary damage type
- [[Chill]] - Primary status effect
- [[Spell]] - Skill category
- [[Aura]] - Skill mechanics
- [[Toggle Skill]] - Activation mechanism