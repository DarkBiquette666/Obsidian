---
type: skill
category: Curse
element: []
classes:
  - Fortunians
  - Lesharii
  - Torin
  - Umbrathi
  - Voidborn
  - Vorathros
tags:
  - spell
  - area
  - curse
  - defense
  - damage_reduction
status: implemented
locked: false
skill Family: curse
---

# Enfeeble Curse

## Description
Casts a curse that reduces enemies' damage output in the target area. This protective malediction weakens the offensive capabilities of foes, making them significantly less dangerous in combat.

## Lore
The Enfeeble Curse channels the ancient arts of vitality manipulation, sapping the strength and coordination from enemies. By speaking words of weakness and decay, the caster drains the martial prowess from their foes, turning deadly adversaries into feeble shadows of their former selves.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Curse Spell | Defensive curse magic |
| **Damage Base** | 0 | No direct damage |
| **Cast Time** | 0.1 sec | Very fast casting |
| **Critical Chance** | 0% | Curses cannot crit |
| **Cost** | 20 Mana | Lower than other curses |
| **Cooldown** | 2.0 sec | Short cooldown |
| **Lifespan** | 2.0 sec | Effect application window |
| **Classes** | All except Astraliens | Wide class access |
| **Weapon Required** | No | Independent casting |
| **Movement Speed** | 80% | Slight reduction while casting |
| **Affects Allies** | No | Enemy-only targeting |

## Curse Properties

| Propriété | Valeur | Description |
|-----------|--------|-------------|
| **Target Area** | Cursor Position | Placed at mouse location |
| **Effect Type** | Damage Reduction | Lowers enemy damage output |
| **Duration** | Variable | Based on curse effect data |
| **Persistent** | No | Single application |
| **Stacking** | Depends on implementation | May stack with other curses |
| **Defense Type** | Offensive Reduction | Reduces enemy attack power |

## Damage Reduction Mechanics

### Affected Damage Types
- **Physical Damage** - Reduced melee and ranged attacks
- **Spell Damage** - Weakened magical abilities
- **Elemental Damage** - Diminished elemental attacks
- **Status Effects** - Potentially reduced effect potency
- **Critical Strikes** - May reduce critical damage

### Curse Effects
- **Attack Power Reduction:** Significantly lowers enemy damage
- **Accuracy Debuff:** May reduce enemy hit chance
- **Coordination Loss:** Impairs enemy combat effectiveness
- **Vitality Drain:** Weakens overall offensive capability

## Tactical Usage

**Strengths:**
- Excellent defensive utility
- Fast casting speed (0.1 seconds)
- Lower mana cost than other curses (20 vs 25)
- Wide class availability (5 of 6 classes)
- Low cooldown (2 seconds)
- Area application affects multiple enemies

**Weaknesses:**
- No direct damage contribution
- Requires dangerous enemies to be effective
- Limited duration window
- Movement speed penalty during cast
- No benefit against weak enemies

**Strategic Applications:**
- Tank builds for damage mitigation
- Survival in dangerous encounters
- Boss fight damage management
- Group content survivability
- Emergency defensive measure

## Class Synergies

### Excluded Class
- **Astraliens:** Notably excluded from this curse
  - May relate to light/purity themes
  - Possibly conflicts with class philosophy
  - Could indicate divine protection concept

### Compatible Classes
- **Fortunians:** Enhances their defensive versatility
- **Lesharii:** Supports their natural resilience themes
- **Torin:** Complements their tank-focused gameplay
- **Umbrathi:** Provides defense for shadow builds
- **Voidborn:** Adds survivability to void manipulation
- **Vorathros:** Enhances their adaptive defensive capabilities

## Build Synergies

**Defensive Builds:**
- **Tank Builds:** Dramatically improves survivability
- **Life Builds:** Reduces incoming damage to health
- **Energy Shield Builds:** Protects energy shield pool
- **Damage Reduction Builds:** Stacks with other mitigation

**Support Builds:**
- **Cast Speed:** Reduces 0.1 second cast time
- **Mana Efficiency:** Reduces 20 mana cost
- **Curse Effectiveness:** Increases damage reduction amount
- **Area of Effect:** Increases curse coverage

**Survival Builds:**
- **Regeneration Builds:** Reduces need for healing
- **Leech Builds:** Allows leech to outpace damage
- **Mitigation Builds:** Multiplies defensive effectiveness

## Combination Strategies

**With Other Curses:**
- **Anemic Curse:** Combines weakness with vitality drain
- **Elemental Weakness:** Offense and defense combined
- **Poison Weakness:** Multi-layer debuff strategy

**With Defensive Skills:**
- **Life Leech Aura:** Safer positioning for leech
- **Frost Aura:** Combines damage reduction with slow
- **Blood Blade:** Safer health costs with reduced incoming damage

**With Tank Builds:**
- Essential for front-line positioning
- Enables aggressive melee strategies
- Supports risk-taking gameplay

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Enfeeble Curse/enfeeble_curse.tres`
- **Effect Resource:** `curse_enfeeble_effect.tres`
- **Scene:** `Enfeeble Curse.tscn`
- **Icon:** `Curse_Enfeeble_Icon.png`
- **Status:** Fully implemented
- **Main Skill:** Yes (primary curse option)

## Technical Notes

- Uses standard curse behavior system
- References external curse effect resource
- Area-based application at cursor position
- No damage component (disable_damage = true)
- Lower mana cost than other curses (20 vs 25)

## Balance Philosophy

Enfeeble represents the defensive counterpart to offensive curses. Its lower mana cost (20 vs 25) reflects its defensive nature and encourages its use as a survival tool rather than an offensive amplifier.

## Related

- [[Curse]] - Skill category and mechanics
- [[Enfeeble]] - Status effect applied (if documented)
- [[Spell]] - Casting mechanics
- [[Area]] - Application method
- [[Damage Reduction]] - Primary effect
- [[Defense]] - Thematic focus