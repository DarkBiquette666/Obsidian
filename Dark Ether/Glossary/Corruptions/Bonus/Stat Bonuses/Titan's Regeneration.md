---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [titans_regeneration, health_regen, regeneration, healing, recovery]
status: implemented
rarity: varies
---

# Titan's Regeneration

## Description
Une corruption de régénération qui augmente la vitesse de récupération des points de vie. Cette corruption accorde la capacité légendaire des titans à se remettre rapidement de leurs blessures, transformant le porteur en un être capable de guérison accélérée.

## Lore
Les titans de l'Éther Sombre possédaient une capacité de régénération qui défie l'entendement mortel. Leurs blessures se refermaient en temps réel, leur essence vitale se reconstituait sans cesse, faisant d'eux des adversaires presque impossibles à abattre définitivement. Cette corruption octroie une fraction de ce pouvoir ancestral, permettant au porteur de récupérer continuellement de ses blessures, comme si la mort elle-même était incapable de le retenir.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Titan | Spécialisation régénération |
| **Focus** | Health Recovery | Récupération vitale |

## Mécaniques de Régénération Titanesque

### Système de Guérison Accélérée
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Health Regen** | +1/2/3%/sec | Variable selon tier |
| **Application** | Percentage du HP total | Scaling avec max HP |
| **Synergie** | Avec max HP bonuses | Plus HP = plus regen |
| **Stacking** | Avec autres regen | Se cumule |
| **Durée** | Permanente | Toujours actif |

### Calcul de la Régénération
```
Regen_Per_Second = Total_Health × (Regen_Percentage/100)
Effective_Healing = Regen_Per_Second × Time_Factor
```

## Système de Tiers

### Valeurs par Tier
| Tier | Health Regen | Healing/Sec (100 HP) | Récupération Globale |
|------|--------------|---------------------|---------------------|
| **Minor** | +1%/sec | +1 HP/sec | Bonne |
| **Moderate** | +1.5%/sec | +1.5 HP/sec | Très bonne |
| **Major** | +2%/sec | +2 HP/sec | Excellente |
| **Epic** | +2.5%/sec | +2.5 HP/sec | Puissante |
| **Legendary** | +3%/sec | +3 HP/sec | Titanesque |

### Code Couleur des Tiers
- **Blanc** : +1%/sec health regen
- **Vert** : +1.5%/sec health regen
- **Bleu** : +2%/sec health regen
- **Violet** : +2.5%/sec health regen
- **Or** : +3%/sec health regen

## Avantages Stratégiques

**Forces :**
- Récupération passive constante
- Scaling avec total health
- Excellent pour sustain builds
- Améliore drastiquement la survie
- Synergie avec tous defensive builds
- Plus efficace avec high HP pools

**Synergies Exceptionnelles :**
- **Titan Vitality** : Plus HP = plus regen absolu
- **Corrupted Endurance** : Triple regen stack
- **Vampiric Essence** : Multiple healing sources
- **Tank Builds** : Sustain optimal
- **High HP Builds** : Scaling multiplicateur

## Applications Tactiques

### Builds Tank Immortels
- Core corruption pour ultra-tanks
- Permet le face-tanking prolongé
- Récupération entre les combats

### Builds Sustain
- Excellent pour builds endurance
- Améliore la survie générale
- Permet des engagements prolongés

### Synergies Cross-Corruption
- **Avec Titan Vitality** : Tank régénératif optimal
- **Avec Corrupted Endurance** : Triple healing stack
- **Avec Vampiric Essence** : Multiple recovery sources
- **Avec Storm Caller** : Tank DPS avec sustain

## Considérations de Balance

### Mécaniques d'Équilibrage
- Percentage-based (scale avec total HP)
- Plus efficace avec high health pools
- Encourage les builds défensifs
- Combat passive mais puissant

### Impact sur la Progression
- Transformateur pour la survie
- Permet l'exploration de contenu difficile
- Réduit le downtime entre combats
- Foundation pour builds sustain avancés

## Implémentation Technique

### Fichiers Source
- **Corruption** : `titan_regeneration.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Health regeneration rate

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [StatType.HEALTH_REGEN]
values = [tier_regen_percentage]
# Percentage of max health per second
```

### Valeurs Techniques
- **Health Regen** : Valeur en pourcentage (1-3)
- **Application** : Pourcentage du max HP par seconde

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Tank builds, sustain builds, high-HP builds
- **Medium Priority** : Tous builds (améliore survie)
- **Low Priority** : Glass cannons (peut être sub-optimal)

### Moment Optimal
- **Early Game** : Bon avec health bonuses
- **Mid Game** : Excellent scaling avec gear
- **Late Game** : Powerful avec max HP optimisé

## Risques et Contreparties

### Limitations
- Plus efficace avec high total HP
- Passive effect (pas d'amélioration active)
- Plus défensif qu'offensif
- Dépendant du total HP pour scaling

### Gestion Optimale
- Combiner avec health bonuses
- Stack avec autres defensive corruptions
- Optimiser le total HP pour scaling
- Utiliser pour builds sustain prolongés

## Interaction avec d'Autres Systèmes

### Système de Santé
- Scaling avec max health
- Synergie avec tous healing effects
- Compatible avec damage reduction
- Améliore recovery entre combats

### Système de Combat
- Permet des engagements prolongés
- Récupération passive en combat
- Synergie avec defensive gear
- Foundation pour aggressive tank play

## Builds Recommandés

### Immortal Regenerator
```
Core: Titan's Regeneration + Titan Vitality + Corrupted Endurance
Style: Maximum health sustain
Focus: Unkillable tank with regen
```

### Sustain Fighter
```
Core: Titan's Regeneration + Vampiric Essence + Critical Mass
Style: Self-sustaining combat
Focus: Multiple healing sources
```

### Endurance Tank
```
Core: Titan's Regeneration + Storm Caller + Elemental Resonance
Style: Tank with DPS
Focus: Sustained pressure
```

## Calculs d'Efficacité

### Scaling Examples
- **200 HP + 2% regen** : 4 HP/sec = 240 HP/min
- **300 HP + 3% regen** : 9 HP/sec = 540 HP/min
- **500 HP + 3% regen** : 15 HP/sec = 900 HP/min

### Synergy Calculations
- Avec Titan Vitality (+100 HP) : +3 HP/sec regen supplémentaire
- Avec defensive gear : Scaling multiplicatif
- Impact croissant avec total HP pool

## Related

- [[Corruptions]] - Système principal
- [[Health System]] - Système de santé
- **Synergies** : [[Titan Vitality]], [[Corrupted Endurance]], [[Vampiric Essence]]
- [[Regeneration]] - Mécanisme de régénération
- [[Tank Builds]] - Style de jeu optimal
- [[Stat Bonuses]] - Catégorie
- [[Sustain]] - Mécaniques de sustain

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\titan_regeneration.tres`