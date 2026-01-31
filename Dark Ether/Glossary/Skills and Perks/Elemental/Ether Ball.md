---
type: skill
category: Spell
element:
  - Fire
  - Ether
classes:
  - Astraliens
  - Voidborn
tags:
  - projectile
  - spell
  - area
  - blast
  - elemental
  - fire
  - ether
status: implemented
skill Family: elemental
---

# Ether Ball

## Description
A blazing projectile infused with the raw power of ether and fire. This dual-element spell creates a dangerous orb that travels toward enemies before exploding in a devastating blast.

## Lore
The Ether Ball represents the fusion of two fundamental forces: the chaotic energy of the Dark Ether and the primal power of fire. Mastered by the Astraliens and Voidborn, this spell channels the volatile nature of interdimensional energy.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Spell | Projectile spell |
| **Damage Base** | 9-14 | Base spell damage |
| **Damage Type** | 50% Fire + 50% Ether | Dual-element damage |
| **Cast Time** | 1.0 sec | Base casting time |
| **Critical Chance** | 5% | Base critical strike chance |
| **Cost** | 3 Mana | Per cast |
| **Cooldown** | None | Can be cast repeatedly |
| **Lifespan** | 3.0 sec | Projectile duration |
| **Speed** | 300 | Projectile travel speed |
| **Classes** | Astraliens, Voidborn | Class restrictions |
| **Weapon Required** | No | Can be cast without weapon |

## Projectile Properties

| Property | Value | Description |
|-----------|--------|-------------|
| **Projectile Count** | 1 | Base number of projectiles |
| **Spread Angle** | 15° (default) | Base spread between projectiles |
| **Piercing** | No | Cannot pierce through enemies |
| **Chaining** | No | Cannot chain between targets |
| **Homing** | No | Does not track enemies |
| **Explosion** | Yes | Explodes on impact or timeout |

## Perks

### Fire to Ether
- **Effect:** Converts all Fire damage to Ether damage
- **Tier 1:** Complete conversion (100% Ether damage)
- **Compatibility:** Mutually exclusive with "Ether to Fire"

### Ether to Fire  
- **Effect:** Converts all Ether damage to Fire damage
- **Tier 1:** Complete conversion (100% Fire damage)
- **Compatibility:** Mutually exclusive with "Fire to Ether"

### Increased Spread Angle
- **Effect:** Increases the spread angle between multiple projectiles
- **Tiers:** 
  - Tier 1: +15° spread angle
  - Tier 2: +25° spread angle  
  - Tier 3: +35° spread angle
- **Synergy:** Works well with projectile amount perks

### Generic Projectile Perks
Compatible with all generic projectile perks:
- **Add Projectile:** Increases projectile count
- **Projectile Chaining:** Enables chain mechanics
- **Projectile Homing:** Adds target tracking

## Tactical Usage

**Strengths:**
- Dual-element damage bypasses single resistances
- Area explosion damage for crowd control
- Good range for safe casting
- Moderate mana efficiency

**Weaknesses:**
- Slow projectile speed (300)
- No piercing or chaining by default
- Requires line of sight to target
- Limited by 3-second lifespan

**Synergies:**
- Fire damage modifiers boost fire portion
- Ether damage modifiers boost ether portion  
- Projectile speed improvements help reliability
- Area damage bonuses improve explosion

## Implementation

- **Skill File:** `Scenes/Skills/Skills/Ether Ball/ether_ball.tres`
- **Scene:** `Scenes/Skills/Skills/Ether Ball/Ether Ball.tscn`
- **Explosion:** `Scenes/Skills/Skills/Ether Ball/Explosion/ether_ball_explosion.tres`
- **Icon:** `EtherBall_Icon_256x256.jpg`
- **Last Update:** January 2025

## Related

- [[Fire Damage]] - One of the damage components
- [[Ether Damage]] - Primary damage component  
- [[Astraliens]] - Primary class user
- [[Voidborn]] - Secondary class user
- [[Spell]] - Skill category
- [[Projectile]] - Mechanics tag