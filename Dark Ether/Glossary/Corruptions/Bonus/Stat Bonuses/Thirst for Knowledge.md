---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [thirst_for_knowledge, experience, learning, progression, knowledge]
status: implemented
rarity: varies
---

# Thirst for Knowledge

## Description
Une corruption d'apprentissage qui augmente l'expérience gagnée. Cette corruption aiguise l'esprit et la soif de connaissances, permettant d'absorber plus rapidement les leçons de chaque combat et de chaque victoire.

## Lore
Dans l'Éther Sombre, la connaissance est plus qu'un simple outil - c'est une force de survie. Cette corruption éveille une faim insatiable pour l'apprentissage et l'expérience, transformant chaque rencontre en une leçon potentielle. Le porteur développe une capacité surnaturelle à extraire la sagesse de chaque adversaire vaincu, assimilant leur essence pour accélérer sa propre évolution.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Learning | Spécialisation progression |
| **Focus** | Experience Gain | Gain d'expérience |

## Mécaniques d'Apprentissage

### Système d'Expérience Accélérée
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Experience Bonus** | +20-40% | Variable selon tier |
| **Application** | Tous gains XP | Universal |
| **Synergie** | Progression speed | Accélération globale |
| **Stacking** | Avec autres bonus | Se cumule |
| **Durée** | Permanente | Toujours actif |

### Calcul de l'Expérience
```
XP_Final = Base_XP × (1 + Thirst_Bonus/100)
Application = [Combat_XP, Quest_XP, Discovery_XP, etc.]
```

## Système de Tiers

### Valeurs par Tier
| Tier | Experience Bonus | Vitesse Progression | Impact Long-terme |
|------|------------------|---------------------|-------------------|
| **Minor** | +20% | Modérée | Bonne |
| **Moderate** | +25% | Solide | Très bonne |
| **Major** | +30% | Rapide | Excellente |
| **Epic** | +35% | Très rapide | Puissante |
| **Legendary** | +40% | Exceptionnelle | Transformatrice |

### Code Couleur des Tiers
- **Blanc** : +20% experience
- **Vert** : +25% experience
- **Bleu** : +30% experience
- **Violet** : +35% experience
- **Or** : +40% experience

## Avantages Stratégiques

**Forces :**
- Accélération de progression permanente
- Effet cumulatif sur tout le jeu
- Plus impactant en early/mid game
- Excellent pour le farming d'XP
- Améliore l'efficacité du temps de jeu
- Investment long-terme excellent

**Synergies Exceptionnelles :**
- **High Kill-rate Builds** : Maximise les gains XP
- **AoE Skills** : Plus d'ennemis = plus d'XP
- **Farming Builds** : Efficacité de farm
- **Blood Thirst** : Kill bonus + XP bonus
- **Fast Clear Builds** : Speed + XP optimal

## Applications Tactiques

### Builds de Farming
- Core corruption pour farmers
- Excellente pour speedruns
- Optimise le ratio temps/progression

### Builds de Progression
- Essential pour characters secondaires
- Excellent pour catch-up mechanics
- Améliore l'efficacité générale

### Synergies Cross-Corruption
- **Avec Blood Thirst** : Kill scaling + XP
- **Avec Movement Speed** : Fast farm + XP
- **Avec AoE Corruptions** : Large clear + XP
- **Avec Echo Chamber** : More kills + XP

## Considérations de Balance

### Mécaniques d'Équilibrage
- Plus impactant en early/mid game
- Effet diminishing returns en late game
- Encourage le gameplay actif
- Plus efficace sur high-kill builds

### Impact sur la Progression
- Accélère significativement la progression
- Plus de levels = plus de skill points
- Permet d'atteindre les builds end-game plus vite
- Excellent ROI (Return on Investment)

## Implémentation Technique

### Fichiers Source
- **Corruption** : `thirst_of_knowledge.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Experience gain modifier

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [StatType.EXPERIENCE_GAIN]
values = [tier_experience_percentage]
# Appliqué sur tous les gains d'XP
```

### Valeurs Techniques
- **Experience Bonus** : Valeur en pourcentage (20-40)
- **Application** : Multiplicateur global XP

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Tous builds (investment long-terme)
- **Medium Priority** : Characters déjà high-level
- **Low Priority** : Builds end-game exclusifs

### Moment Optimal
- **Early Game** : Investment exceptionnel
- **Mid Game** : Très bon pour progression
- **Late Game** : Moins impactant mais toujours utile

## Risques et Contreparties

### Limitations
- Pas d'amélioration directe du combat
- Plus utility que power
- ROI diminue avec le level
- Plus effective sur active gameplay

### Gestion Optimale
- Acquérir le plus tôt possible
- Combiner avec high-kill builds
- Optimiser pour farming efficiency
- Focus sur active play sessions

## Interaction avec d'Autres Systèmes

### Système de Progression
- Accélère le gain de levels
- Plus de skill points disponibles
- Access plus rapide aux abilities
- Améliore la courbe de progression

### Système de Combat
- Indirect : plus de levels = plus de power
- Encourage l'engagement actif
- Synergie avec kill-based mechanics
- Compatible avec tous playstyles

## Builds Recommandés

### XP Farmer
```
Core: Thirst for Knowledge + Blood Thirst + Movement Speed
Style: Efficient farming
Focus: Maximum XP/hour
```

### Speedrunner
```
Core: Thirst for Knowledge + Echo Chamber + AoE Skills
Style: Fast progression
Focus: Quick level gains
```

### Balanced Learner
```
Core: Thirst for Knowledge + Critical Mass + Time Distortion
Style: Progression with power
Focus: Efficient balanced growth
```

## Métriques de Performance

### Calculs d'Efficacité
- **20% bonus** : 1 heure = 1.2 heures de progression
- **30% bonus** : 10 heures = 13 heures de progression
- **40% bonus** : 100 heures = 140 heures de progression

### ROI Analysis
- Plus impactant en early game
- Effet cumulatif sur toute la session
- Excellent pour alt characters
- Essential pour competitive progression

## Related

- [[Corruptions]] - Système principal
- [[Experience System]] - Système d'expérience
- **Synergies** : [[Blood Thirst]], [[Movement Speed]], [[Echo Chamber]]
- [[Progression]] - Mécanisme de progression
- [[Farming]] - Stratégies de farm
- [[Stat Bonuses]] - Catégorie
- [[Long-term Investment]] - Stratégie long-terme

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\thirst_of_knowledge.tres`