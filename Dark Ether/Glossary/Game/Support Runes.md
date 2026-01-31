---
aliases:
  - Support Rune
  - Support
  - Supports
  - Rune
  - Runes
  - support
  - supports
---

# Support Runes

Runes engraved into Vorathros's flesh that modify how skills behave. Each skill has a limited number of rune slots—all equipped runes are always active.

---

## Narrative Context

Vorathros carves **ancient runes** directly into his flesh. As a shapeshifter who controls his own DNA, he can **heal and reshape his skin** to change which runes are inscribed. This allows him to swap runes between runs without permanent scarring.

Unlike [[Perks]] (which represent mastery over a skill), Support Runes are external magical inscriptions that augment abilities with additional effects.

---

## Properties

| Property | Detail |
|----------|--------|
| **Unlock** | Permanent (once acquired, never lost) |
| **Equip** | Applied per skill (can change between runs) |
| **Active** | All equipped runes are always active |
| **Impact** | Skill modifier (adds effects) |
| **Acquisition** | Drops, crafting, fusion |
| **When equipped** | Before starting a run |
| **Slots per skill** | Limited (TBD) |
| **Tiers** | 5 tiers (I → V) |

---

## Rune Tiers

Support Runes have **5 tiers of power**. Higher tiers provide stronger effects.

| Tier | Name | Effect Multiplier |
|------|------|-------------------|
| **I** | Common | Base effect |
| **II** | Uncommon | ~1.5x |
| **III** | Rare | ~2x |
| **IV** | Epic | ~3x |
| **V** | Legendary | ~4x |

### Fusion System

To upgrade a rune to the next tier, combine **3 runes of the same type and tier**:

```
3x Rune of Flames (I) → 1x Rune of Flames (II)
3x Rune of Flames (II) → 1x Rune of Flames (III)
...
```

This creates a meaningful resource sink and long-term progression goal.

---

## Key Principle

**Support Runes ADD effects. Perks CHANGE how skills work.**

- A **Perk** transforms the skill: "Bloodblades chain to enemies"
- A **Support Rune** adds an effect: "Bloodblades inflict Poison"

Each skill has a limited number of rune slots. You choose which runes to apply to each skill, and all equipped runes are active simultaneously.

---

## Skill Tags Compatibility

Support Runes work with the [[Skill Tags]] system. Each rune has **tag requirements** that determine which skills it can be applied to.

### How It Works

1. Each skill has tags (e.g., Blood Blade = `Attack`, `Blood`, `Bleed`, `Persistent`, `Weapon`)
2. Each rune requires specific tags to function
3. A rune can only be equipped on skills that have **all required tags**

### Examples

| Rune | Required Tags | Compatible With |
|------|---------------|-----------------|
| **Rune of Hemorrhage** | `Bleed` | Blood Blade, skills that inflict Bleed |
| **Rune of Piercing** | `Projectile` | Void Spitters, any projectile skill |
| **Rune of Swarm** | `Minion` | Call of the Colony, Praetorian Guard |
| **Rune of Echoes** | `Spell` | Most caster skills |
| **Rune of Flames** | *(none)* | Any skill (universal) |

### Tag Categories

- **Damage Type**: `Physical`, `Fire`, `Cold`, `Lightning`, `Poison`, `Ether`
- **Damage Source**: `Attack`, `Spell`, `Over Time`
- **Delivery**: `Projectile`, `Melee`, `AoE`, `Chaining`
- **Mechanic**: `Minion`, `Aura`, `Curse`, `Buff`, `Duration`, `Channeling`
- **Weapon**: `Bow`, `One-Handed`, `Two-Handed`

See Skill Tags for the full list. 

---

## Support Rune Categories

### Elemental Infusion
| Rune                | Effect                                   |
| ------------------- | ---------------------------------------- |
| **Rune of Flames**  | Skill gains Fire damage penetration      |
| **Rune of Frost**   | Skill gains Cold damage penetration      |
| **Rune of Thunder** | Skill gains Lightning damage penetration |

### Status Application
| Rune                 | Effect                             |
| -------------------- | ---------------------------------- |
| **Rune of Venom**    | Skill has chance to inflict Poison |
| **Rune of Bleeding** | Skill has chance to inflict Bleed  |


### Scaling
| Rune | Effect |
|------|--------|
| **Rune of Amplification** | Increases skill damage |
| **Rune of Swiftness** | Reduces skill cooldown |
| **Rune of Efficiency** | Reduces skill resource cost |

### Utility
| Rune | Effect |
|------|--------|
| **Rune of Reach** | Increases skill range/AoE |
| **Rune of Persistence** | Increases skill duration |
| **Rune of Echoes** | Skill has chance to trigger twice |

---

## Support Runes vs Perks vs Mutations

| Aspect            | Support Runes  | Perks            | Mutations           |
| ----------------- | -------------- | ---------------- | ------------------- |
| **Duration**      | Permanent      | Permanent        | Per-run             |
| **Scope**         | Per skill      | Per skill        | Global              |
| **Impact**        | Adds effects   | Changes behavior | Tactical adaptation |
| **Acquisition**   | Drop/Craft     | Meta-progression | Buy at Merchant     |
| **When equipped** | Before run     | Before run       | During run          |
| **Narrative**     | Runes in flesh | Skill mastery    | DNA adaptation      |

---

## Acquisition Methods

- **Drops**: From enemies and bosses (mostly Tier I-II)
- **Fusion**: Combine 3 same-tier runes to upgrade
- **Rewards**: Trial Room completions, achievements
- **[[Chamber of Lost Time]]**: Rare high-tier runes
- **Bosses**: Major Bosses can drop Tier III+ runes

---

## Design Notes

- Support Runes should be **generic enough** to work with multiple skills
- They provide incremental power, not build-defining changes
- Encourage experimentation: "What if I put Fire on my summons?"
- Tier system creates long-term progression (collecting duplicates matters)
- 3→1 fusion ratio means 81 Tier I runes to reach Tier V (meaningful grind)
- Can drop raw higher level rune to reduce grind
- Limited slots per skill forces meaningful choices

---

## Related

- [[Perks]]
- [[Mutations]]
- [[Skills Index]]
- [[GDD#4.1 Permanent Progression (Meta)]]
