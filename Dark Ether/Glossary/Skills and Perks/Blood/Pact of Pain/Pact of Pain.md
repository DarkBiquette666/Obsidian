---
type: skill
category: Buff
element: []
classes:
  - Torin
tags:
  - blood
  - buff
  - leech
  - risk_reward
  - divine
status: concept
locked: true
skill Family: blood
---

# Pact of Pain

## Description
The caster establishes a temporary pact with his God to increase his damage and Life Leech at the cost of increased damage received for a certain duration. This divine bargain trades safety for overwhelming power.

## Lore
The Pact of Pain represents the most dangerous covenant a Torin can make - a direct bargain with their deity for power at the cost of vulnerability. This sacred ritual channels divine blessing through suffering, transforming the caster into a vessel of terrible might that walks the razor's edge between triumph and destruction.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Self Buff | Divine blood magic |
| **Activation Cost** | 20% Max Health | Significant health sacrifice |
| **Duration** | Variable seconds | Time-limited power |
| **Damage Bonus** | +20% | All damage increased |
| **Life Leech** | 1% of damage dealt | Built-in sustain |
| **Vulnerability** | +20% damage taken | Increased incoming damage |
| **Classes** | Torin | Divine covenant exclusive |
| **Cooldown** | Variable | Likely significant |
| **Weapon Required** | No | Independent of weapons |

## Pact Mechanics

### Divine Bargain
| Aspect | Benefit | Cost |
|--------|---------|------|
| **Damage Output** | +20% all damage | 20% max health sacrifice |
| **Sustain** | 1% life leech on damage | +20% damage vulnerability |
| **Duration** | Extended power window | Time pressure |
| **Risk Level** | High reward potential | High death risk |

### Risk vs Reward Balance
- **High Health Cost:** 20% max health is substantial
- **Power Spike:** Significant damage increase with sustain
- **Vulnerability Window:** Increased incoming damage
- **Time Pressure:** Must maximize value during duration

### Implementation Tracking

See [[Pact of Pain Perks.base]] for the complete database with implementation status and priority tracking.

## Tactical Usage

**Strengths:**
- Massive damage and sustain boost (20% + 1% leech)
- Built-in life leech provides sustainability
- Multiple perk paths for different strategies
- Divine thematic power fantasy
- Can turn tide of difficult encounters

**Weaknesses:**
- Enormous health cost (20% max health)
- Significantly increased vulnerability (+20%)
- Time-limited effectiveness
- High risk of death if mistimed
- Requires careful health management

**Strategic Applications:**
- Boss encounter damage phases
- Elite enemy elimination
- Crowd clearing with appropriate perks
- Emergency damage when low on resources
- Combination with defensive skills

## Class Identity - Torin

**Divine Connection:**
- Represents covenant with Torin deity
- Epitomizes risk-reward philosophy
- Shows divine blessing through sacrifice
- Reinforces warrior-priest identity

**Thematic Integration:**
- Blood sacrifice for divine power
- Pain as pathway to strength
- Temporary transcendence of mortal limits
- Sacred duty requiring sacrifice

## Synergies

**With Life Leech Aura:**
- Double life leech sources
- Improved sustainability during pact
- Better health recovery after pact ends
- Enhanced risk mitigation

**With Blood Blade:**
- Both skills require health sacrifice
- Compound damage bonuses
- Compound life leech effects
- High-risk, extreme reward combination

**With Defensive Skills:**
- Blood Barrier helps mitigate vulnerability
- Hemorrhagic Shield provides protection
- Defensive perks offset increased damage taken

## Balance Considerations

**Power Level:**
- 20% damage + 1% leech is substantial
- 20% vulnerability is serious risk
- Health cost prevents casual usage
- Duration must balance power vs exposure

**Risk Management:**
- Multiple health costs strain resource pool
- Vulnerability timing creates skill requirement
- Perk choices dramatically alter risk profile
- Player skill determines effectiveness

## Divine Lore Integration

**Religious Significance:**
- Sacred covenant with Torin deity
- Pain as offering for divine blessing
- Temporary divine channeling
- Sacred risk undertaken for greater purpose

**Thematic Consistency:**
- Aligns with Torin sacrifice philosophy
- Reinforces blood magic themes
- Connects physical and spiritual power
- Shows cost of divine intervention

## Implementation Challenges

**Technical Requirements:**
- Buff/debuff system integration
- Health cost calculation
- Life leech implementation
- Damage modifier systems

**Balance Testing:**
- Health cost vs power relationship
- Vulnerability vs benefit balance
- Duration optimization
- Perk value propositions

## Implementation Status

- **Status:** Conceptual design
- **Development:** Not yet implemented
- **Dependencies:** Buff system, health mechanics
- **UI Needs:** Buff indicator, health cost warning
- **Animation:** Divine transformation effects

## Related

- [[Torin]] - Exclusive class user
- [[Blood]] - Thematic skill tree
- [[Divine]] - Power source
- [[Buff]] - Skill category
- [[Leech]] - Life sustain mechanic
- [[Risk]] - Core design principle