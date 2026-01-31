---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionStatReward
tags: [chain_reaction, explosion, death_effects, aoe, chain]
status: implemented
rarity: varies
---

# Chain Reaction

## Description
Une corruption explosive qui fait exploser les ennemis tués, infligeant des dégâts basés sur leurs points de vie maximum. Cette corruption transforme chaque élimination en une cascade de destruction, créant des réactions en chaîne dévastatrices.

## Lore
Dans l'Éther Sombre, la mort n'est jamais un simple arrêt - c'est une libération explosive d'énergie contenue. Cette corruption exploite cette vérité cosmique, transformant chaque ennemi vaincu en une bombe mystique dont la puissance dépend de la force vitale originelle de la créature. Plus l'ennemi était puissant, plus son explosion finale sera dévastatrice, créant des cascades de destruction qui peuvent anéantir des groupes entiers dans un spectacle pyrotechnique mortel.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Special Effects | Effet unique |
| **Classe de Base** | CorruptionStatReward | Bonus conditionnel |
| **Durée** | Permanente | Tant que la corruption est active |
| **Trigger** | Enemy Death | Activation à la mort |
| **Scaling** | Enemy Max HP | Basé sur la vitalité |

## Mécaniques Explosives

### Système d'Explosion à la Mort
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Damage Base** | {value}% of enemy max HP | Variable selon tier |
| **Trigger** | Enemy death | Toutes les éliminations |
| **Area** | Explosion radius | Zone d'effet autour du corps |
| **Type** | Area damage | Affecte ennemis proches |
| **Chain Potential** | Cascading explosions | Peut déclencher d'autres |

### Calcul des Dégâts d'Explosion
```
Explosion_Damage = Enemy_Max_HP × (value/100)
Area_Damage = Explosion_Damage to all nearby enemies
Chain_Reaction = If explosion kills → new explosion
```

## Système de Tiers

### Valeurs par Tier (Estimées)
| Tier | Explosion Damage | Radius | Chain Potential |
|------|------------------|--------|-----------------|
| **Minor** | 15% of max HP | Small | Faible |
| **Moderate** | 20% of max HP | Medium | Modéré |
| **Major** | 25% of max HP | Large | Bon |
| **Epic** | 30% of max HP | Large | Très bon |
| **Legendary** | 35% of max HP | Extra Large | Exceptionnel |

### Code Couleur des Tiers
- **Blanc** : 15% max HP explosion
- **Vert** : 20% max HP explosion
- **Bleu** : 25% max HP explosion
- **Violet** : 30% max HP explosion
- **Or** : 35% max HP explosion

## Avantages Stratégiques

**Forces :**
- Dégâts AoE passifs automatiques
- Scaling avec la puissance des ennemis
- Excellent contre groupes denses
- Potentiel de chain reactions
- Plus efficace contre ennemis tankés
- Synergie avec tous kill-based builds

**Synergies Exceptionnelles :**
- **Blood Thirst** : Plus de kills = plus d'explosions
- **AoE Builds** : Multiple kills = multiple explosions
- **High-density Areas** : Chain reactions optimal
- **Tank Enemies** : Explosions plus puissantes
- **Farming Builds** : Clear speed amélioré

## Applications Tactiques

### Builds de Farming
- Excellent pour clear de zones denses
- Accelere significativement le farming
- Particulièrement efficace contre swarms

### Builds AoE
- Synergie avec area abilities
- Multiplie l'efficacité de zone
- Chain reactions pour clear massive

### Synergies Cross-Corruption
- **Avec Blood Thirst** : Kill farming optimal
- **Avec Echo Chamber** : Plus de kills = plus d'explosions
- **Avec Movement Speed** : Fast farming avec explosions
- **Avec Area Skills** : Multiple triggers

## Considérations de Balance

### Mécaniques d'Équilibrage
- Scaling avec enemy HP (plus balancé)
- Area limited (pas d'explosion globale)
- Requires kills (pas passif pur)
- Chain potential balanced

### Impact sur la Progression
- Accelere significativement le farming
- Plus efficace contre tough enemies
- Excellent pour zone clearing
- Peut trivialiser dense areas

## Implémentation Technique

### Fichiers Source
- **Corruption** : `chain_reaction_bonus.tres`
- **Script** : `corruption_stat_reward.gd`
- **Template** : Description with dynamic value

### Intégration Système
```gdscript
# Type: CorruptionStatReward
# Triggered on enemy death
description_template = "Killed enemies explode, dealing {value}% of their max HP"
trigger_event = ENEMY_DEATH
explosion_scaling = tier_percentage
```

### Variables de Template
- `{value}` : Pourcentage des HP max (ex: 25.0 pour 25%)

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : AoE builds, farmers, clear-focused
- **Medium Priority** : Builds balanced, généralists
- **Low Priority** : Single-target builds, boss-focused

### Moment Optimal
- **Early Game** : Très bon pour progression
- **Mid Game** : Excellent pour farming
- **Late Game** : Essential pour clear efficiency

## Risques et Contreparties

### Limitations
- Nécessite des kills pour fonctionner
- Plus efficace contre groupes denses
- Moins utile contre boss isolés
- Scaling dépendant des enemy HP

### Gestion Optimale
- Focus sur area dense en ennemis
- Combiner avec AoE abilities
- Utiliser pour farming efficiency
- Priorité aux groupes over single targets

## Interaction avec d'Autres Systèmes

### Systèmes de Kill
- Triggered par toutes les éliminations
- Compatible avec tous damage types
- Works with indirect kills
- Synergie avec kill mechanics

### Systèmes d'Area
- Explosions create new AoE damage
- Chain with other area effects
- Multiplicatif avec zone abilities
- Compatible avec area scaling

## Mécaniques de Chain Reaction

### Cascade Potential
- Enemy A dies → explodes
- Explosion kills Enemy B → B explodes
- B's explosion kills Enemy C → C explodes
- Continue until no more kills

### Optimization Strategies
- Position pour maximum chain potential
- Target weak enemies in groups
- Use AoE to trigger multiple simultaneously
- Leverage enemy positioning

## Builds Recommandés

### Chain Farmer
```
Core: Chain Reaction + Blood Thirst + Movement Speed
Style: Efficient area farming
Focus: Maximum clear speed
```

### AoE Destroyer
```
Core: Chain Reaction + Echo Chamber + Area Skills
Style: Multiple explosion triggers
Focus: Zone devastation
```

### Swarm Clearer
```
Core: Chain Reaction + Storm Caller + Lesharii's Grace
Style: Mobile AoE clearing
Focus: Dense area efficiency
```

## Related

- [[Corruptions]] - Système principal
- [[Death Effects]] - Effets à la mort
- **Synergies** : [[Blood Thirst]], [[Echo Chamber]], [[Movement Speed]]
- [[Area of Effect]] - Zone d'effet
- [[Chain Mechanics]] - Mécaniques en chaîne
- [[Special Effects]] - Catégorie
- [[Farming Efficiency]] - Efficacité de farm

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\chain_reaction_bonus.tres`