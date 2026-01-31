---
type: perk
skill: Blood Blade
category: automation
tags:
  - auto_attack
  - passive_combat
  - health_cost
  - incompatible
status:
  - implemented
---

# Conscious Blood

## Description
Blood Blades gain sentience and attack automatically without player input, but double the health drain per second. This transforms the skill into a fully automated combat companion at significant health cost.

## Mechanics

### Automation System
- **Full Autonomy:** No player input needed
- **Target Selection:** Nearest enemy priority
- **Attack Rate:** Consistent intervals
- **Range Detection:** Automatic enemy scanning

### Cost Modification
- **Base Drain:** 3% max health per second
- **Modified Drain:** 6% max health per second
- **Per Blade:** Each blade costs individually
- **Total with 3 blades:** 18% per second

### Incompatibility
- **Cannot combine with:** Mimic Blades
- **Reason:** Conflicting automation systems
- **Design Choice:** Constant vs triggered automation

## Strategic Value

### Hands-Off Combat
- **Passive Damage:** Continues while casting
- **Multi-Tasking:** Focus on other skills
- **Consistent DPS:** Reliable damage output
- **No Micro-Management:** Simplified gameplay

### High-Risk Automation
- **Severe Drain:** Double health costs
- **Sustain Required:** Mandatory healing sources
- **Time Limit:** Natural duration cap from health
- **Death Risk:** Can drain to Low Life quickly

## Build Requirements

### Essential Components
- **High Health Pool:** Support the drain
- **Life Leech:** Offset health costs
- **Regeneration:** Constant healing needed
- **Defensive Layers:** Protect remaining health

### Synergy Optimization
- **Life Leech Aura:** Critical sustain source
- **Reduce Cost:** Mitigate doubled drain
- **Health Scaling:** Leverage high HP
- **Regenerative Barrier:** Periodic healing

## Playstyle Impact

### Benefits
- **Simplified Combat:** Less actions required
- **Spell Focus:** Cast freely while blades work
- **Consistent Pressure:** Never stops attacking
- **Positioning Freedom:** Blades handle themselves

### Drawbacks
- **Resource Intensive:** Extreme health management
- **Less Control:** Can't direct attacks
- **Predictable:** AI targeting patterns
- **Build Restrictive:** Requires specific setup

## Implementation Status

**Status:** To Do

### Technical Requirements
- AI targeting system
- Automatic attack patterns
- Enemy detection algorithms
- Performance optimization
- State management system

### AI Behavior
- Target prioritization logic
- Attack timing calculations
- Range checking systems
- Target switching rules
- Multiple blade coordination

### Balance Considerations
- Drain multiplier value
- AI effectiveness tuning
- Target selection intelligence
- Attack frequency balance

## Related Concepts
- [[Blood Blade]] - Base skill
- [[Mimic Blades]] - Incompatible perk
- [[Automation]] - Core mechanic
- [[Health Cost]] - Resource system
- [[AI Behavior]] - Implementation detail