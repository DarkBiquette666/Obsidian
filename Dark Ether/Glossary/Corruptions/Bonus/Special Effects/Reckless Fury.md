---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionStatReward
tags: [reckless_fury, low_health, damage_bonus, berserker, risk_reward]
status: implemented
rarity: varies
---

# Reckless Fury

## Description
Une corruption berserker qui augmente les dégâts quand la santé est faible. Cette corruption transforme la proximité de la mort en un carburant de rage, permettant des attaques d'une puissance dévastatrice quand le porteur frôle l'agonie.

## Lore
Dans l'Éther Sombre, la ligne entre la vie et la mort devient floue, et certaines âmes apprennent à puiser leur force dans cette proximité avec l'abîme. Cette corruption exploite l'instinct de survie le plus primitif, transformant la peur de mourir en une rage meurtrière incontrôlable. Plus le porteur s'approche de sa fin, plus ses attaques deviennent sauvages et destructrices, comme si la mort elle-même lui prêtait sa faux pour faucher ses ennemis.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Special Effects | Effet unique |
| **Classe de Base** | CorruptionStatReward | Bonus conditionnel |
| **Durée** | Permanente | Tant que la corruption est active |
| **Trigger** | Health ≤ 50% | Condition de santé |
| **Bonus** | +30% damage | Damage fixe |

## Mécaniques de Furie

### Système de Rage Désespérée
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Health Threshold** | ≤ 50% max HP | Seuil d'activation |
| **Damage Bonus** | +30% fixe | Tous types de dégâts |
| **Duration** | While condition met | Tant que HP ≤ 50% |
| **Application** | All damage sources | Universal |
| **Stacking** | With other bonuses | Se cumule |

### Calcul de la Furie
```
If Current_Health <= (Max_Health * 0.5):
    Damage_Bonus = +30%
    All_Damage = Base_Damage × 1.30
Else:
    Damage_Bonus = 0%
```

## Mécaniques Risk/Reward

### État de Danger vs Puissance
| Health Range | Damage Bonus | Risk Level | Strategic Value |
|--------------|--------------|------------|-----------------|
| **100-51%** | 0% | Sûr | Normal |
| **50-26%** | +30% | Élevé | High reward |
| **25-11%** | +30% | Critique | Très dangereux |
| **10-1%** | +30% | Extrême | Glass cannon |

### Balance Risk/Reward
- **High Reward** : +30% damage significant
- **High Risk** : Vulnérabilité extrême
- **Timing Critical** : Window de puissance limité
- **Skill Required** : Gestion précise de HP

## Avantages Stratégiques

**Forces :**
- Bonus de dégâts significatif (+30%)
- Universal sur tous damage types
- Peut transformer les combat situations
- High risk / high reward gameplay
- Synergie avec glass cannon builds
- Clutch potential énorme

**Synergies Exceptionnelles :**
- **Vampiric Essence** : Life steal pour maintenir threshold
- **High Burst Builds** : Maximize damage windows
- **Critical Builds** : Multiplied critical damage
- **Echo Chamber** : Double les dégâts boosted
- **Glass Cannon Style** : Naturellement low HP

## Applications Tactiques

### Builds Glass Cannon
- Naturellement dans le range optimal
- Maximum damage potential
- High skill ceiling required

### Builds Berserker
- Thème parfait pour berserker style
- Risk management critical
- Clutch gameplay rewarded

### Synergies Cross-Corruption
- **Avec Vampiric Essence** : Sustain dans danger zone
- **Avec Critical Mass** : Boosted critical strikes
- **Avec Echo Chamber** : Double damage boosted
- **Avec Anti-Matter Orb** : Double-down sur risk

## Considérations de Balance

### Mécaniques d'Équilibrage
- High risk pour high reward
- Requires skill pour optimal use
- Vulnerable window exploitation
- Risk of death vs reward power

### Impact sur la Progression
- Transforme les desperate situations
- Requires adaptation du playstyle
- High skill ceiling build enabler
- Clutch moment creator

## Implémentation Technique

### Fichiers Source
- **Corruption** : `reckless_fury_bonus.tres`
- **Script** : `corruption_stat_reward.gd`
- **Template** : Description fixe

### Intégration Système
```gdscript
# Type: CorruptionStatReward
# Conditional damage bonus
description_template = "+30% damage when health is below 50%"
health_threshold = 0.5  # 50% of max health
damage_bonus = 30.0     # 30% increase
```

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Glass cannon, berserker, high-skill players
- **Medium Priority** : Risk-tolerant builds
- **Low Priority** : Tank builds, safe players

### Moment Optimal
- **Early Game** : Risqué but rewarding
- **Mid Game** : Skill-dependent value
- **Late Game** : Master-level corruption

## Risques et Contreparties

### Dangers Majeurs
- Constant death threat
- Requires precise HP management
- One mistake = death
- High stress gameplay

### Gestion des Risques
- Combiner avec sustain effects
- Master timing et positioning
- Practice HP threshold management
- Backup defensive measures

## Interaction avec d'Autres Systèmes

### Systèmes de Health
- Critical dependency sur health management
- Requires monitoring constant
- Synergy avec controlled damage taking
- Balance avec healing effects

### Systèmes de Combat
- Transforme damage calculations
- Universal damage bonus application
- Multiplicative avec tous bonuses
- High impact sur DPS

## Strategic Considerations

### HP Management
- Maintain optimal 25-50% range
- Avoid dropping too low
- Use controlled damage sources
- Balance risk vs reward timing

### Combat Tactics
- Engage at optimal HP threshold
- Maximize damage windows
- Quick decisive combat preferred
- Avoid prolonged engagement

## Builds Recommandés

### Reckless Berserker
```
Core: Reckless Fury + Vampiric Essence + Critical Mass
Style: High risk glass cannon
Focus: Maximum damage in danger zone
```

### Fury Vampire
```
Core: Reckless Fury + Anti-Matter Orb + Echo Chamber
Style: Double-down on risk
Focus: All-or-nothing power
```

### Controlled Fury
```
Core: Reckless Fury + Corrupted Endurance + Dark Power
Style: Managed risk with sustain
Focus: Balanced berserker approach
```

## Mastery Techniques

### Advanced HP Management
- Damage calculation to reach optimal range
- Environmental damage utilization
- Timing healing for optimal windows
- Risk assessment pour each encounter

### Combat Optimization
- Burst damage timing
- Positioning pour maximum safety
- Escape plan preparation
- Clutch moment recognition

## Related

- [[Corruptions]] - Système principal
- [[Risk Reward]] - Mécaniques risque/récompense
- **Synergies** : [[Vampiric Essence]], [[Critical Mass]], [[Echo Chamber]]
- [[Glass Cannon]] - Style glass cannon
- [[Berserker Builds]] - Builds berserker
- [[Special Effects]] - Catégorie
- [[High Skill]] - Corruptions à haut skill

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\reckless_fury_bonus.tres`