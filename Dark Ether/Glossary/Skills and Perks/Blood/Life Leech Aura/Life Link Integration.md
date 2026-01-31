---
type: perk
skill: Life Leech Aura
category: Integration
tags: [blood, aura, vital-link, integration, network]
status: concept
---

# Life Link Integration

## Overview
The Life Leech Aura extends through Vital Link connections, allowing the aura to drain life from enemies connected to linked targets at reduced efficiency, creating a network-based leech system.

## Mechanics

### Primary Effect
- **Network Extension**: Aura effect extends through Vital Link connections
- **Efficiency Reduction**: Leech through links operates at 50% efficiency
- **Link Propagation**: Effect can chain through multiple link connections
- **Range Independence**: Linked targets can be beyond normal aura range

### Technical Details
- **Leech Formula**: `link_leech = base_leech * 0.5 * link_efficiency`
- **Network Mapping**: Dynamic tracking of all Vital Link connections
- **Propagation Rules**: Effect diminishes by additional 10% per link hop
- **Maximum Hops**: Effect can propagate through up to 3 link connections

## Synergies

### Simple Synergies
- **Vital Link**: Direct integration with existing link network
- **Sanguine Overflow**: Overflow can be generated from linked target leech
- **Bleeding Resonance**: Bleed stacks on linked network contribute to resonance

### Complex Synergies
- **Crimson Vortex + Life Link**: Pull effect extends through link network, creating distributed crowd control
- **Vampiric Pulse**: Pulse synchronizes across entire link network for coordinated healing waves
- **Toxic Symbiosis**: Regeneration siphoning from linked poisoned enemies amplifies network efficiency

## Trade-offs
- **Efficiency Loss**: 50% reduced leech effectiveness through links
- **Link Dependency**: Requires active Vital Link connections to function
- **Network Vulnerability**: Link breaks disable extended leech from that branch

## Implementation Details

### Network Integration
- **Link Detection**: Real-time monitoring of Vital Link network topology
- **Efficiency Calculation**: Dynamic efficiency computation based on network structure
- **Visual Feedback**: Enhanced link visuals showing aura energy flow

### Propagation System
- **Hop Tracking**: System to track and limit propagation through network
- **Efficiency Degradation**: Gradual reduction of effect strength per hop
- **Network Optimization**: Intelligent routing for maximum leech efficiency

## Advanced Interactions

### Network Effects
- **Link Amplification**: Strong links (high health difference) provide better aura propagation
- **Network Resonance**: Large networks (5+ links) gain 10% efficiency bonus
- **Cascade Healing**: Healing from network leech can trigger additional link effects

### Strategic Network Management
- **Link Priority**: Can prioritize aura flow through specific link branches
- **Network Cycling**: Ability to temporarily disable links to redirect aura energy
- **Emergency Network**: Critical health triggers maximum efficiency through all links

## Network Topology Considerations

### Optimal Configurations
- **Star Network**: Central hub with multiple spoke links maximizes coverage
- **Chain Network**: Linear chains good for area denial and movement
- **Mesh Network**: Interconnected links provide redundancy and efficiency

### Network Vulnerabilities
- **Central Points**: Loss of central links can fragment network
- **Range Limitations**: Physical distance can strain link efficiency  
- **Enemy Interference**: Enemies can disrupt links to break network

## Implementation Status
**Status**: To Do
**Priority**: High
**Dependencies**: Vital Link system, network topology tracking, Life Leech Aura base mechanics