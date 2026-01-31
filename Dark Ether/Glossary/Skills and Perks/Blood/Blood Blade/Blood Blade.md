---
type: skill
category: Attack
element:
  - Physical
classes:
  - Torin
tags:
  - attack
  - blood
  - bleed
  - persistent
  - weapon
status: implemented
locked: false
skill Family: blood
---

# Blood Blade

## Description
The Torin uses his own blood to form and maintain a blade that he can project towards an enemy at medium range to inflict bleeds. The blood blade disappears when the caster is on Low Life.

## Lore
One of the most iconic abilities of the Torin warrior-priests, Blood Blade represents the ultimate sacrifice - using one's own life force as both weapon and ammunition. This technique embodies the Torin philosophy that true power requires sacrifice, transforming vitality into deadly projectiles.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Attack | Weapon-based skill |
| **Damage Base** | Weapon-based | 60% of weapon damage |
| **Damage Type** | 100% Physical | Pure physical damage |
| **Attack Speed** | Weapon-based | 100% of weapon attack speed |
| **Attack Range** | 1.5x weapon range | Extended reach |
| **Cost** | 30 Health | Initial summon cost |
| **Cost Per Second** | 3% Max Health | Maintenance cost |
| **Cooldown** | 2.0 sec | Recast limitation |
| **Lifespan** | Infinite | Until dismissed or Low Life |
| **Classes** | Torin | Blood magic specialist only |
| **Weapon Required** | Yes | Must have weapon equipped |
| **Movement Speed** | 50% | Significantly reduced |
| **Bleed Chance** | 100% | Guaranteed bleeding |
| **Bleed Damage Factor** | 200% | 2x damage multiplier |
| **Bleed Duration** | 5.0 sec | Standard bleed duration |

## Blood Blade Properties

| Property | Value | Description |
|-----------|--------|-------------|
| **Blade Count** | 1 (base) | Number of active blades |
| **Radius** | 35 units | Operating radius around caster |
| **Persistent** | Yes | Remains active until toggled off |
| **Attach to Caster** | No | Independent positioning |
| **Can Be Recast** | No | Cannot recast while active |
| **Disable on Low Life** | Yes | Automatically dismissed |

## Cost Mechanics

### Health Costs
- **Initial Cost:** 30 Health to summon the blade
- **Maintenance:** 3% of maximum health per second (0.03 factor)
- **Per Blade:** Each additional blade has individual cost
- **Low Life Protection:** Blade disappears to prevent death

### Risk vs Reward
- High health costs require careful management
- Massive bleed damage (200% factor) compensates risk
- Persistent nature provides sustained damage
- Movement penalty requires tactical positioning

## Perks System

The Blood Blade skill can be enhanced with various perks that modify its behavior and effectiveness. Each perk offers unique strategic opportunities and build possibilities.

### Available Perks

#### Core Enhancement Perks
1. **[[Drinker Blades]]** - Hits consume bleed stacks for instant damage

#### Transformative Perks
2. **[[Blade Communion]]** - When Life Leech Aura is active, blade attacks all enemies in aura simultaneously
3. **[[Hemorrhagic Catalyst]]** - Blade no longer applies bleed directly but amplifies existing bleeds (+200% damage, +100% duration)
4. **[[Crimson Echo]]** - Blade remembers targets from broken Vital Links, gaining escalating damage bonuses (up to +150%)
5. **[[Sanguine Metamorphosis]]** - Blade transforms based on life state: Guardian (Low Life), Balance (Half Life), Reaper (Full Life)
6. **[[Tainted Resonance]]** - When self-poisoned by Tainted Blood, blade applies poison instead of bleed and heals on hit
7. **[[Barrier Symbiosis]]** - Creates additional blades equal to active Blood Barriers, all share properties but fail together

### Support Runes
The following former perks have been reclassified as **Support Runes** and can be equipped in support slots:
- **[[Multiple Projectiles Support]]** (formerly Amount Perks)
- **[[Vitality Support]]** (formerly Health Scaling)
- **[[Vicious Ailments Support]]** (formerly Increased Bleed Damage)
- **[[Long Reach Support]]** (formerly Increased Range)
- **[[Efficiency Support]]** (formerly Reduce Cost)
- **[[Elemental Conversion Support]]** (formerly Change Damage Type)

### Perk Categories

**Core Enhancement:**
- Drinker Blades

**Transformative Synergies:**
- Blade Communion (Life Leech Aura synergy), Hemorrhagic Catalyst (bleed amplification), Crimson Echo (Vital Link synergy)

**Adaptive Mechanics:**
- Sanguine Metamorphosis (life state reactive), Tainted Resonance (self-poison synergy)

**Network Systems:**
- Barrier Symbiosis (Blood Barrier integration)

### Implementation Tracking

See [[Blood Blade Perks.base]] for the complete database with implementation status and priority tracking.

## Tactical Usage

**Strengths:**
- Extremely high bleed damage (200% factor)
- Guaranteed bleed application (100% chance)
- Extended attack range (1.5x weapon)
- Persistent sustained damage
- Powerful perk interactions

**Weaknesses:**
- Severe health costs (30 + 3% per second)
- Major movement penalty (50% speed)
- Requires weapon to function
- Disabled on Low Life state
- Cannot recast while active

**Strategic Applications:**
- Sustained damage in prolonged fights
- Bleed-stacking builds
- High-health tank builds
- Crowd control through bleeding
- Boss encounters with phases

## Class Identity - Torin

**Blood Magic Mastery:**
- Core class identity skill
- Represents sacrifice for power philosophy
- Synergizes with health-based mechanics
- Defines Torin combat style

**Build Archetypes:**
- **Blood Warrior:** High health, sustained blade combat
- **Bleed Master:** Maximum bleed damage and stacking
- **Conscious Fighter:** Automated blade combat
- **Mimic Specialist:** Blade triggers with spell combos
- **Blade Conductor:** Multi-target communion with Life Leech Aura
- **Wound Artist:** Bleed amplification specialist with Hemorrhagic Catalyst
- **Memory Hunter:** Vital Link synergy with Crimson Echo bonuses
- **Life Dancer:** Adaptive combat with Sanguine Metamorphosis
- **Toxic Vampire:** Self-poison synergy with Tainted Resonance
- **Network Commander:** Multi-blade systems with Barrier Symbiosis

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Blood Blade/blood_blade.tres`
- **Behavior:** `blood_blade_behavior.gd`
- **Scene:** `Blood Blade.tscn`
- **Cast VFX:** `CastingRune.tscn`
- **Icon:** `bloodblade_icon_256x256.png`
- **Status:** Fully implemented with complete perk system
- **Main Skill:** Yes (signature Torin skill)

## Related

- [[Torin]] - Exclusive class user
- [[Blood]] - Thematic skill tree
- [[Bleed]] - Primary status effect
- [[Attack]] - Skill category
- [[Physical Damage]] - Damage type
- [[Low Life]] - Interaction state

## Corruption Synergies

- **[[Echo Chamber]]**: Doubles the number of blades launched
- **[[Corrupted Rage]]**: Perfect berserker style for Blood Blade builds
- **[[Battle Frenzy]]**: Attack speed stacks with each blade hit
- **[[Blood Thirst]]**: More damage per enemy killed, natural synergy
- **[[Critical Mass]]**: More critical chances with multiple blades