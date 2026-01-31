---
type: perk
skill: Life Leech Aura
category: Ultimate
tags: [blood, aura, ultimate, transformation, blood-moon]
status: concept
---

# Blood Moon Rising

## Overview
After maintaining the Life Leech Aura for 10 seconds, it transforms into an empowered Blood Moon state with dramatically increased effectiveness, but at the cost of continuously draining the user's maximum health.

## Mechanics

### Primary Effect
- **Activation Timer**: Transforms after 10 seconds of continuous aura activation
- **Enhanced Leech**: +100% life leech effectiveness (double base rate)
- **Expanded Range**: +25% aura radius during Blood Moon state
- **Health Cost**: Drains 2% of maximum health per second while active

### Technical Details
- **Transformation Formula**: `blood_moon_leech = base_leech * 2.0`
- **Range Formula**: `blood_moon_radius = base_radius * 1.25`
- **Health Drain**: `health_drain = max_health * 0.02 per second`
- **Minimum Health**: Cannot drain health below 1 HP

### Transformation States
- **Rising Phase** (0-10s): Normal aura operation with building energy
- **Blood Moon** (10s+): Enhanced state with health drain trade-off
- **Eclipse** (30s+): Ultimate state with additional 50% effectiveness

## Synergies

### Simple Synergies
- **Sanguine Overflow**: Enhanced leech creates more frequent overflow shields
- **Vampiric Pulse**: Pulse effects doubled during Blood Moon state
- **Necrotic Field**: Blood Moon deaths create enhanced necrotic fields

### Complex Synergies
- **Pact of Pain + Blood Moon**: Self-damage from both sources can create dangerous but powerful feedback loops
- **Life Link Integration**: Blood Moon state propagates through entire link network at reduced health cost (1% per linked target)
- **Toxic Symbiosis**: Blood Moon amplifies regeneration siphoning, potentially offsetting health drain

## Trade-offs
- **High Risk**: Continuous health drain creates significant survival risk
- **Timing Challenge**: Must survive 10-second buildup period
- **Resource Management**: Requires careful health monitoring and emergency exits

## Implementation Details

### Transformation System
- **State Machine**: Multi-phase transformation with clear visual transitions
- **Health Monitoring**: Critical health warnings and automatic shutoff systems
- **Visual Evolution**: Aura changes from crimson to deep red to black-red

### Blood Moon Effects
- **Environmental Changes**: Area lighting shifts to red-tinted atmosphere
- **Enhanced Visuals**: Dramatic particle effects and screen modifications
- **Audio Design**: Ominous background effects and intensified heartbeat

## Advanced Interactions

### Eclipse State (30+ seconds)
- **Ultimate Power**: Additional 50% effectiveness bonus (total 250% base leech)
- **Lunar Resonance**: All blood abilities gain enhanced effectiveness
- **Gravitational Pull**: Combines with Crimson Vortex for extreme crowd control

### Emergency Protocols
- **Auto-Deactivation**: Automatically deactivates at 15% health
- **Override Control**: Can be manually deactivated at any time
- **Recovery Bonus**: Deactivation provides temporary healing bonus

## Risk Management

### Survival Strategies
- **Health Monitoring**: Constant awareness of health drain rate
- **Exit Planning**: Always have escape routes planned
- **Support Skills**: Coordinate with other healing abilities

### Optimal Usage Windows
- **High Health**: Activate only at near-maximum health
- **Enemy Density**: Maximum benefit in high-enemy-density areas
- **Support Available**: Best used when healing items/allies available

## Mastery Progression

### Blood Moon Mastery
- **Efficiency Training**: Reduced health drain with experience (minimum 1.5% per second)
- **Extended Duration**: Increased survivability in Blood Moon state
- **Eclipse Mastery**: Faster access to Eclipse state (25 seconds instead of 30)

## Implementation Status
**Status**: To Do
**Priority**: High
**Dependencies**: Multi-state aura system, health drain mechanics, visual transformation system