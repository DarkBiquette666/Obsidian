---
type: skill
category: Spell
element:
  - Ether
classes:
  - All Classes
tags:
  - spell
  - projectile
  - ether
  - orbital
  - dangerous
  - follow
status: implemented
locked: true
skill Family: ether
---

# Anti Matter Ball

## Description
A dangerous ball that follows its caster and attacks suddenly towards its owner, damaging every living thing on its path. This volatile sphere of antimatter energy orbits the caster before launching devastating attacks at nearby enemies.

## Lore
The Anti Matter Ball represents the most dangerous aspect of void manipulation - the creation of antimatter within normal space. This forbidden technique creates a sphere of pure annihilation that exists in an unstable orbit around the caster, ready to unleash its destructive power at a moment's notice.

## ⚠️ Warning
**Dangerous to Caster:** This skill can damage the player! The antimatter ball's unpredictable nature makes it as dangerous to its creator as to enemies.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Spell | Orbital projectile spell |
| **Damage Base** | 9-14 | Moderate ether damage |
| **Damage Type** | 100% Ether | Pure void damage |
| **Cast Time** | 0.0 sec | Instant activation |
| **Critical Chance** | 5% | Standard spell crit rate |
| **Cost** | 0 Mana | No resource cost |
| **Cooldown** | None | Continuously active |
| **Charge Cooldown** | 8.0 sec | Time between attacks |
| **Lifespan** | Infinite | Persistent until dismissed |
| **Classes** | All Classes | Universal access |
| **Weapon Required** | No | Independent of weapons |
| **Movement Speed** | 100% | No movement penalty |
| **Can Hit Owner** | **YES** | ⚠️ Dangerous to caster |

## Orbital Properties

| Propriété | Valeur | Description |
|-----------|--------|-------------|
| **Follow Distance** | 80 units | Orbital radius from caster |
| **Follow Speed** | 100 | Speed of orbital movement |
| **Projectile Count** | 1 | Single antimatter sphere |
| **Speed** | 300 | Attack projectile speed |
| **Persistent** | Yes | Remains active indefinitely |
| **Automatic** | Yes | Attacks without player input |
| **Target Selection** | Automatic | Chooses targets independently |

## Unique Mechanics

### Orbital Behavior
- **Follows Caster:** Maintains 80-unit orbit around player
- **Continuous Presence:** Remains active until manually dismissed
- **Attack Cycles:** Launches attacks every 8 seconds
- **Unpredictable Targeting:** May attack any valid target

### Danger to Caster
- **Self-Damage:** Can damage the player who summoned it
- **Unpredictable Nature:** Attack timing and targeting not fully controlled
- **Risk vs Reward:** High damage potential with significant personal risk

## Tactical Usage

**Strengths:**
- Zero mana cost for sustained damage
- Continuous presence in combat
- No movement speed penalty
- Available to all classes
- Moderate damage output

**Weaknesses:**
- **Can damage the caster** - Major safety risk
- Currently locked and unavailable
- Limited player control over attacks
- 8-second charge cooldown between attacks
- Unpredictable behavior patterns

**Strategic Considerations:**
- High-risk, high-reward playstyle
- Requires careful positioning
- Better for experienced players
- Situational utility only
- Risk assessment before activation

## Risk Management

**Safety Precautions:**
- Maintain distance from enemies when ball charges
- Be aware of ball position at all times
- Have escape routes planned
- Consider health/shield levels before use
- Monitor charge cooldown timing

**Mitigation Strategies:**
- High mobility builds reduce self-damage risk
- Damage reduction affects incoming self-damage
- Health regeneration counteracts accidents
- Shield mechanics may absorb friendly fire

## Build Considerations

**Ether Damage Builds:**
- Ether damage bonuses increase ball damage
- Void mastery may improve control
- Ether penetration helps against resistant enemies

**High Mobility Builds:**
- Movement speed helps avoid self-damage
- Dash/teleport skills provide emergency escape
- Positioning tools reduce risk

**Tanky Builds:**
- High health pool absorbs accidental damage
- Damage reduction mitigates self-harm
- Regeneration counters friendly fire

## Implementation Details

- **Skill File:** `Scenes/Skills/Skills/Anti Matter Ball/anti_matter_ball.tres`
- **Behavior:** `anti_matter_ball_behavior.gd`
- **Scene:** `AntiMatterBallScene.tscn`
- **Icon:** `Anti_Matter_Ball_Effect_Icon.png`
- **Status:** Implemented but locked
- **Main Skill:** No (special/bonus skill)

## Technical Notes

- Orbital mechanics implemented
- Self-damage functionality active
- Charge system controls attack frequency
- Available to all classes (unusual design)
- No resource consumption

## Balance Philosophy

The skill's ability to damage its own caster is an intentional design choice representing the volatile nature of antimatter manipulation. This creates a unique risk-reward dynamic where power comes at the cost of safety.

## Future Considerations

- Unlock conditions to be determined
- Possible safety improvements
- Control mechanism enhancements
- Class-specific interactions

## Related

- [[Ether Damage]] - Primary damage type
- [[Spell]] - Skill category
- [[Projectile]] - Mechanics type
- [[Void]] - Thematic element
- [[Orbital]] - Movement pattern
- **⚠️ Safety Warning** - Can damage caster