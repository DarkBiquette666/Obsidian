---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionStatReward
tags: [blood_thirst, damage, kills, stacking, combat]
status: implemented
rarity: varies
---

# Blood Thirst

## Description
Une corruption qui augmente les dégâts en fonction du nombre d'ennemis tués. Cette corruption transforme chaque victoire en une soif croissante de destruction, alimentant la puissance du porteur par le sang versé.

## Lore
Dans les profondeurs de l'Éther Sombre, certaines âmes développent une soif insatiable pour le combat et la destruction. Cette corruption canalise l'essence vitale des ennemis vaincus, transformant chaque mort en carburant pour une rage grandissante. Plus le carnage s'étend, plus la soif de sang devient dévorante, créant un cycle de violence qui se nourrit de lui-même.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Special Effects | Effet unique |
| **Classe de Base** | CorruptionStatReward | Bonus de statistique |
| **Durée** | Permanente | Tant que la corruption est active |
| **Scaling** | Par kill | Augmente avec les éliminations |
| **Maximum** | Variable | Dépend de l'implémentation |

## Mécaniques de Soif de Sang

### Système d'Accumulation
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Déclencheur** | Élimination d'ennemi | Tous types d'ennemis |
| **Accumulation** | +{value}% damage | Par kill |
| **Durée** | Permanente | Persistante durant le niveau |
| **Reset** | Nouveau niveau | Repart à zéro |
| **Affichage** | "{bonus}% total damage" | Bonus actuel cumulé |

### Calcul des Dégâts
```
Bonus_Total = Nombre_Kills × Pourcentage_Par_Kill
Dégâts_Finaux = Dégâts_Base × (1 + Bonus_Total/100)
```

## Système de Tiers

### Valeurs par Tier
| Tier | Bonus par Kill | Max Théorique (100 kills) |
|------|----------------|---------------------------|
| **Minor** | 0.5% | +50% damage |
| **Moderate** | 0.7% | +70% damage |
| **Major** | 1.0% | +100% damage |
| **Epic** | 1.3% | +130% damage |
| **Legendary** | 1.5% | +150% damage |

### Code Couleur des Tiers
- **Blanc** : 0.5% par kill
- **Vert** : 0.7% par kill
- **Bleu** : 1.0% par kill
- **Violet** : 1.3% par kill
- **Or** : 1.5% par kill

## Avantages Stratégiques

**Forces :**
- Scaling illimité durant un niveau
- Encourage le gameplay agressif
- Synergie avec tous les types de dégâts
- Particulièrement puissant dans les niveaux denses
- Excellent pour les builds de farming

**Synergies Exceptionnelles :**
- **AoE Skills** : Plus d'éliminations simultanées
- **Fast Attack Builds** : Kills rapides = accumulation rapide
- **Movement Speed** : Efficacité de farming accrue
- **Area Damage** : Maximise les éliminations multiples
- **Life Leech** : Sustain amélioré avec plus de dégâts

## Applications Tactiques

### Builds de Farming
- Maximise l'efficacité dans les zones denses
- Parfait pour les builds AoE et crowd control
- Excellent pour la progression rapide de niveau

### Stratégies de Combat
- Priorité aux ennemis faibles pour accumulation rapide
- Utilisation de skills AoE pour maximiser les kills
- Positioning pour optimiser les éliminations multiples

### Synergies Cross-Corruption
- **Avec Echo Chamber** : Plus de chances d'élimination
- **Avec Dark Power** : Multiplication des bonus de dégâts
- **Avec Critical Mass** : Kills plus faciles grâce aux critiques
- **Avec Movement Speed** : Farm plus efficace

## Considérations de Balance

### Mécaniques d'Équilibrage
- Reset à chaque nouveau niveau
- Scaling linéaire (non exponentiel)
- Nécessite des éliminations actives
- Plus efficace sur les niveaux longs

### Impact sur la Progression
- Reward les joueurs agressifs
- Crée une courbe de puissance durant le niveau
- Peut rendre les boss plus faciles en fin de niveau
- Encourage l'exploration complète des niveaux

## Implémentation Technique

### Fichiers Source
- **Corruption** : `blood_thirst_bonus.tres`
- **Script** : `corruption_stat_reward.gd`
- **Template** : Description dynamique

### Intégration Système
```gdscript
# Type: CorruptionStatReward
# Template avec variables dynamiques
description_template = "{value}% more damage per enemy killed ({bonus}% total damage)"
stat_modifiers = [StatType.DAMAGE_MULTIPLIER]
scaling_per_kill = tier_value  # Varie selon le tier
```

### Variables de Template
- `{value}` : Pourcentage par kill (ex: 1.0)
- `{bonus}` : Bonus total actuel (ex: 25.0 pour 25 kills)

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Builds AoE, farmers, speedrunners
- **Medium Priority** : Builds balanced, explorateurs
- **Low Priority** : Builds single-target, passifs

### Moment Optimal
- **Early Game** : Excellent pour la progression
- **Mid Game** : Très puissant pour le farming
- **Late Game** : Synergie avec autres corruptions

## Risques et Contreparties

### Limitations
- Reset à chaque niveau
- Nécessite un style de jeu agressif
- Plus faible sur les niveaux courts
- Dépendant de la densité d'ennemis

### Gestion Optimale
- Prioriser les zones denses en ennemis
- Utiliser des skills AoE efficaces
- Maintenir un rythme d'élimination élevé
- Combiner avec des bonus de vitesse de déplacement

## Interaction avec d'Autres Systèmes

### Systèmes de Kill
- Compte tous les types d'éliminations
- Fonctionne avec les éliminations indirectes (DoT, explosions)
- Synergie avec les mécaniques d'overkill

### Systèmes de Dégâts
- Applique un multiplicateur global
- Affecte tous les types de dégâts
- Se cumule avec autres bonus multiplicatifs

## Related

- [[Corruptions]] - Système principal
- [[Damage Scaling]] - Mécanisme de scaling
- **Synergies** : [[Echo Chamber]], [[Dark Power]], [[Critical Mass]]
- [[Kill Mechanics]] - Système d'élimination
- [[Farming Strategies]] - Optimisation de farm
- [[Special Effects]] - Catégorie

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\blood_thirst_bonus.tres`