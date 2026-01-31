---
type: corruption
category: Malus
subcategory: Defensive Weakness
reward_type: CorruptionStatReward
tags: [adaptive_armor, resistance_reduction, vulnerability, adaptive, weakness]
status: implemented
rarity: varies
---

# Adaptive Armor

## Description
Une corruption de vulnérabilité qui réduit la résistance au dernier type de dégâts reçu. Cette corruption crée une faiblesse adaptative qui expose le porteur aux attaques répétées du même type, transformant la défense en un système fragile et prévisible.

## Lore
L'Éther Sombre a ses propres lois d'adaptation, mais elles ne favorisent pas toujours le survivant. Cette corruption malveillante transforme le système de défense naturel du porteur en un mécanisme autodestructeur qui s'affaiblit face aux menaces récurrentes. Chaque coup reçu grave une faiblesse dans l'âme, créant une vulnérabilité qui s'approfondit avec chaque attaque similaire, comme si l'esprit oubliait comment se défendre contre les dangers qu'il a déjà affrontés.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Malus Corruption | Effet négatif |
| **Catégorie** | Defensive Weakness | Faiblesse défensive |
| **Classe de Base** | CorruptionStatReward | Malus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Penalty** | -20% resistance | Réduction fixe |
| **Target** | Last damage type | Type le plus récent |

## Mécaniques d'Adaptation Destructrice

### Système de Vulnérabilité Adaptative
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Resistance Reduction** | -20% fixe | Réduction significative |
| **Target Type** | Last damage received | S'adapte dynamiquement |
| **Duration** | Until new damage type | Persiste jusqu'au changement |
| **Application** | Immediate | Effect instantané |
| **Stacking** | No | Une seule vulnérabilité active |

### Calcul de la Vulnérabilité
```
On_Damage_Received(damage_type):
    Current_Vulnerability = damage_type
    Resistance[damage_type] -= 20%
    
Effective_Resistance = Base_Resistance - 20%
Damage_Taken = Incoming_Damage × (1 + Vulnerability_Modifier)
```

## Système de Danger

### Vulnérabilité par Type de Dégâts
| Damage Type | Vulnerability Risk | Common Sources |
|-------------|-------------------|----------------|
| **Physical** | Élevé | Attacks, projectiles |
| **Fire** | Modéré | Elemental enemies |
| **Ice** | Modéré | Elemental enemies |
| **Lightning** | Modéré | Storm enemies |
| **Poison/Acid** | Variable | DoT enemies |

### Risques Tactiques
- **Repeated Damage** : Vulnérabilité augmentée
- **Single Damage Source** : Exploitation prolongée
- **Elemental Enemies** : Specialization dangereuse
- **Environmental** : Hazards persistants

## Inconvénients Stratégiques

**Dangers :**
- Vulnérabilité accrue aux attaques répétées
- Exploitation par enemies specialized
- Reduces effective health pool
- Predictable weakness pattern
- Encourage enemy focusing
- Defensive planning complicated

**Situations Critiques :**
- **Elemental Areas** : Vulnérabilité constante au même type
- **Specialized Enemies** : Exploitation de faille
- **Environmental Hazards** : Damage type fixe dangereux
- **Boss Encounters** : Pattern attacks exploitent vulnérabilité

## Stratégies d'Atténuation

### Techniques de Défense
- **Damage Type Diversification** : Force enemy variety
- **Mobility Tactics** : Avoid repeated exposure
- **Resistance Stacking** : Compensate avec gear
- **Quick Engagement** : Minimize exposure time

### Adaptations de Build
- **High HP Builds** : Absorb increased damage
- **Mobility Builds** : Avoid prolonged exposure
- **Damage Prevention** : Avoid taking damage
- **Balanced Resistance** : General defensive approach

## Gestion des Risques

### Combat Strategies
- Engage diverse enemy types
- Avoid standing in damage zones
- Quick repositioning after hits
- Diversify combat encounters

### Build Adaptations
```
Safe Approach: High HP + Mobility + General Resistances
Risky Approach: Glass cannon (éviter)
Balanced: Moderate defenses + tactical awareness
```

## Interaction avec d'Autres Systèmes

### Systèmes de Résistance
- Directly reduces effectiveness
- Compounds with other resistance penalties
- Makes resistance investment less reliable
- Creates defensive gaps

### Systèmes de Combat
- Changes damage calculation significantly
- Encourages tactical adaptation
- Punishes predictable patterns
- Rewards diverse engagement

## Synergies Problématiques

### Corruptions à Éviter
- **Other Defensive Penalties** : Compound vulnerability
- **Glass Cannon Builds** : Amplify fragility
- **Single Damage Focus** : Create predictable patterns

### Corruptions Bénéfiques
- **Titan Vitality** : More HP to absorb damage
- **Corrupted Endurance** : Additional HP + regen
- **Mobility Bonuses** : Avoid repeated exposure
- **Damage Prevention** : Avoid triggering vulnerability

## Calculs d'Impact

### Damage Increase Examples
- **100 damage + 20% vulnerability** = 120 effective damage
- **50% base resistance - 20%** = 30% effective resistance
- **Repeated fire damage** = Consistent 20% damage increase

### Defensive Impact
- **20% resistance loss** = Significant vulnerability
- **Repeated exposure** = Cumulative damage increase
- **Predictable pattern** = Enemy exploitation potential

## Contremesures Recommandées

### Defensive Strategies
1. **Diversify Damage Sources** : Force vulnerability switching
2. **High Mobility** : Minimize exposure time
3. **Resistance Stacking** : Compensate for penalty
4. **Damage Avoidance** : Prevent vulnerability activation

### Tactical Considerations
- Monitor last damage type received
- Plan engagement variety
- Avoid environmental damage repetition
- Quick decisive combat preferred

## Environmental Hazards

### High-Risk Situations
- **Fire Zones** : Consistent fire vulnerability
- **Poison Areas** : Persistent poison weakness
- **Electrical Fields** : Lightning vulnerability
- **Physical Trap Areas** : Physical damage focus

### Mitigation Techniques
- Quick traversal of hazard zones
- Resistance gear for known areas
- Alternative routing when possible
- Emergency healing preparation

## Related

- [[Corruptions]] - Système principal
- [[Resistance Systems]] - Systèmes de résistance
- **Dangerous Combinations** : Glass cannon builds, defensive penalties
- **Safe Combinations** : [[Titan Vitality]], [[Corrupted Endurance]]
- [[Vulnerability]] - Mécaniques de vulnérabilité
- [[Malus]] - Catégorie
- [[Defensive Weaknesses]] - Faiblesses défensives

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Malus\adaptive_armor_malus.tres`