---
type: skill
category: Spell
element:
  - Physical
classes:
  - Torin
  - Voidborn
tags:
  - spell
  - projectile
  - physical
  - ground
  - bleed
status: implemented
locked: false
skill Family: ground
---

# Thorn Spike

## Description
Spikes erupt from the ground in devastating lines that track enemies and inflict bleeding wounds. This earth-based magic creates sequential waves of razor-sharp thorns that emerge from beneath foes' feet.

## Lore
The Thorn Spike technique channels the primal fury of nature itself, commanding the earth to birth deadly protrusions. Mastered by both the resilient Torin and the adaptive Voidborn, this spell represents the marriage of organic growth and lethal precision.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Spell | Ground-based projectile spell |
| **Damage Base** | 15-25 | High physical damage |
| **Damage Type** | 100% Physical | Pure physical damage |
| **Cast Time** | 0.2 sec | Very fast casting |
| **Critical Chance** | 5% | Standard spell crit rate |
| **Cost** | 10 Mana | Per cast |
| **Cooldown** | 3.0 sec | Moderate cooldown |
| **Bleed Chance** | 100% | Guaranteed bleeding |
| **Bleed Damage Factor** | 20% | Bleed damage multiplier |
| **Bleed Duration** | 5.0 sec | Standard bleed duration |
| **Classes** | Torin, Voidborn | Dual class access |
| **Weapon Required** | No | Independent casting |
| **Movement Speed** | 50% | Reduced while casting |

## Spike Behavior

| Propriété | Valeur | Description |
|-----------|--------|-------------|
| **Max Spikes Per Line** | 30 | Maximum spikes in one line |
| **Min Distance Between Spikes** | 20 units | Spacing between spikes |
| **Spike Delay** | 0.01 sec | Time between spike spawns |
| **Line Count** | 5 | Number of parallel lines |
| **Total Angle Spread** | 270° | Angular coverage |
| **Sequential Lines** | Yes | Lines appear one after another |
| **Sequential Line Delay** | 0.2 sec | Delay between lines |

## Targeting System

| Propriété | Valeur | Description |
|-----------|--------|-------------|
| **Track Target** | Yes | Follows enemy movement |
| **Tracking Intensity** | 100% | Full target tracking |
| **Tracking Delay Factor** | 20% | Prediction adjustment |
| **Tracking Angle Influence** | 10% | Angular tracking weight |
| **Continue Beyond Target** | Yes | Spikes extend past target |
| **Predict Target Movement** | Yes | Anticipates enemy position |
| **Prediction Time Factor** | 4.0x | Movement prediction multiplier |
| **Prediction Max Distance** | 500 units | Maximum prediction range |
| **Prediction Iterations** | 4 | Calculation refinement steps |

## Effects

### Primary Effects
- **Ground Eruption:** Spikes emerge from the earth
- **Bleeding Wounds:** 100% chance to inflict bleed
- **Area Coverage:** Multiple lines for wide coverage
- **Target Tracking:** Intelligent enemy following

### Bleed Mechanics
- **Guaranteed Application:** 100% bleed chance on hit
- **Damage Factor:** 20% of base damage per second
- **Duration:** 5 seconds of bleeding
- **Stacking:** Multiple spikes can stack bleeds
- **Physical Scaling:** Scales with physical damage bonuses

## Tactical Usage

**Strengths:**
- High guaranteed bleed application
- Excellent area coverage (270°)
- Intelligent target tracking
- Good damage per cast (15-25)
- Fast casting speed (0.2 sec)

**Weaknesses:**
- Moderate cooldown (3 seconds)
- Enemies can potentially dodge
- Limited to ground-based attacks
- Movement speed penalty during cast
- Requires line of sight to ground

**Strategic Applications:**
- Crowd control through bleed stacking
- Area denial with multiple lines
- Chasing fleeing enemies
- Corridor and chokepoint control
- Setting up combo attacks

## Class Synergies

### Torin Synergy
- Physical damage bonuses enhance spike damage
- Bleed-focused builds maximize DoT potential
- Health-based mechanics support aggressive play
- Blood magic themes align perfectly

### Voidborn Synergy
- Adaptability allows for versatile use
- Void energies may enhance tracking
- Multi-element access provides flexibility
- Positioning skills complement spike placement

## Build Synergies

**Physical Damage Builds:**
- Physical damage bonuses increase spike damage
- Physical penetration helps against armor
- Attack speed may affect casting

**Bleed Builds:**
- Bleed damage bonuses enhance DoT
- Bleed duration increases stack maintenance
- Bleed chance redundancy (already 100%)

**Area Damage Builds:**
- Area damage bonuses affect all spikes
- Area of effect increases may expand coverage
- Multiple target scenarios maximize efficiency

**Spell Builds:**
- Spell damage bonuses increase base damage
- Cast speed reduces the 0.2 second cast time
- Spell critical chance enhances burst potential

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Thorn Spike/Thorn Spike.tres`
- **Behavior:** `thorn_spike_behavior.gd`
- **Scene:** `Thorn Spike.tscn`
- **Icon:** `Thorn Spike_Icon_256x256.png`
- **Status:** Fully implemented
- **Main Skill:** Yes (primary skill option)

## Technical Features

- Advanced movement prediction system
- Sequential line spawning algorithm
- Dynamic target tracking
- Ground-based collision detection
- Bleed stacking mechanics

## Balance Notes

- Moderate cooldown prevents spam
- Movement penalty requires positioning
- Prediction system rewards skilled play
- Bleed guarantee ensures consistent damage

## Related

- [[Physical Damage]] - Primary damage type
- [[Bleed]] - Primary status effect
- [[Torin]] - Primary class user
- [[Voidborn]] - Secondary class user
- [[Spell]] - Skill category
- [[Projectile]] - Mechanics classification