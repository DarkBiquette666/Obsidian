---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [time_distortion, speed, attack_speed, cast_speed, temporal]
status: implemented
rarity: varies
---

# Time Distortion

## Description
Une corruption temporelle qui accélère les actions d'attaque et de cast. Cette corruption manipule le flux temporel autour du porteur, lui permettant d'agir avec une célérité surnaturelle.

## Lore
L'Éther Sombre n'obéit pas aux lois temporelles du monde matériel. Cette corruption permet de manipuler ces distorsions temporelles, créant une bulle de temps accéléré autour du porteur. Chaque geste devient plus fluide, chaque action plus rapide, comme si le temps lui-même pliait devant la volonté corrompue. Les observateurs ne voient qu'un flou de mouvements impossibles, témoins d'une maîtrise du temps qui défie toute logique.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Temporal | Manipulation temporelle |
| **Focus** | Speed Global | Vitesse d'action |

## Mécaniques Temporelles

### Système d'Accélération
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Attack Speed** | +10/15/20% | Variable selon tier |
| **Cast Speed** | +10/15/20% | Identique à attack speed |
| **Synergie** | Double speed boost | Attaque ET cast |
| **Application** | Permanent | Toujours actif |
| **Stacking** | Avec autres bonus | Se cumule |

### Calcul de la Vitesse
```
Attack_Speed_Final = Base_Attack_Speed × (1 + Bonus/100)
Cast_Speed_Final = Base_Cast_Speed × (1 + Bonus/100)
```

## Système de Tiers

### Valeurs par Tier
| Tier | Attack Speed | Cast Speed | Efficacité Globale |
|------|--------------|------------|-------------------|
| **Minor** | +10% | +10% | Bonne |
| **Moderate** | +12% | +12% | Solide |
| **Major** | +15% | +15% | Très bonne |
| **Epic** | +17% | +17% | Excellente |
| **Legendary** | +20% | +20% | Exceptionnelle |

### Code Couleur des Tiers
- **Blanc** : +10% attack/cast speed
- **Vert** : +12% attack/cast speed
- **Bleu** : +15% attack/cast speed
- **Violet** : +17% attack/cast speed
- **Or** : +20% attack/cast speed

## Avantages Stratégiques

**Forces :**
- Double bonus (attack + cast)
- Améliore tous les types de builds
- Augmente DPS et qualité de vie
- Synergie universelle
- Excellent pour builds hybrides
- Améliore la responsivité du gameplay

**Synergies Exceptionnelles :**
- **Forbidden Knowledge** : Speed + mana pour casters
- **Battle Frenzy** : Triple stack attack speed
- **Echo Chamber** : Plus de chances de doubles attaques
- **All Fast Builds** : Multiplicateur d'efficacité
- **Hybrid Builds** : Optimisation balanced

## Applications Tactiques

### Builds Hybrides
- Core corruption pour builds mixed
- Améliore l'efficacité attack + cast
- Parfait pour characters versatiles

### Builds Spécialisés
- Excellente addition à tous builds
- Améliore le DPS général
- Qualité de vie améliorée

### Synergies Cross-Corruption
- **Avec Forbidden Knowledge** : Speed + resources optimal
- **Avec Battle Frenzy** : Attack speed extrême
- **Avec Echo Chamber** : Vitesse + double cast
- **Avec Silent Blade** : Speed + critique

## Considérations de Balance

### Mécaniques d'Équilibrage
- Bonus modestes pour éviter l'overpowered
- Scaling linéaire avec tiers
- Améliore tous aspects sans spécialisation
- Plus généralist que specialist

### Impact sur la Progression
- Améliore la fluidité du gameplay
- Augmente l'efficacité générale
- Excellent à tous les moments du jeu
- Base solide pour builds avancés

## Implémentation Technique

### Fichiers Source
- **Corruption** : `time_distortion_bonus.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Attack speed + cast speed

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [
    StatType.ATTACK_SPEED,
    StatType.CAST_SPEED
]
values = [tier_speed_percentage, tier_speed_percentage]
```

### Valeurs Techniques
- **Attack Speed** : Valeur en pourcentage (10-20)
- **Cast Speed** : Valeur en pourcentage (10-20)

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Builds hybrides, balanced characters
- **Medium Priority** : Builds spécialisés (toujours utile)
- **Low Priority** : Aucun (améliore tout)

### Moment Optimal
- **Early Game** : Excellent pour la qualité de vie
- **Mid Game** : Améliore l'efficacité générale
- **Late Game** : Stack avec autres corruptions

## Risques et Contreparties

### Limitations
- Bonus généralist (non spécialisé)
- Modeste comparé aux corruptions focused
- Plus utility que game-changing
- Scaling avec équipement

### Gestion Optimale
- Acquérir pour améliorer la fluidité
- Combiner avec autres speed bonuses
- Excellent pour builds balanced
- Stack avec specializations

## Interaction avec d'Autres Systèmes

### Système d'Attaque
- Améliore la vitesse d'attaque globale
- Synergie avec weapon scaling
- Compatible avec tous weapon types
- Améliore l'efficacité DPS

### Système de Cast
- Améliore tous les spell casts
- Réduit les temps de cast
- Synergie avec channeling
- Compatible avec tous spell types

## Builds Recommandés

### Hybrid Master
```
Core: Time Distortion + Forbidden Knowledge + Critical Mass
Style: Balanced attack + magic
Focus: Versatile efficiency
```

### Speed Demon
```
Core: Time Distortion + Battle Frenzy + Echo Chamber
Style: Maximum action speed
Focus: Fast-paced combat
```

### Balanced Assassin
```
Core: Time Distortion + Silent Blade + Dark Power
Style: Quick critical strikes
Focus: Efficient burst damage
```

## Related

- [[Corruptions]] - Système principal
- [[Speed Systems]] - Mécanisme de vitesse
- **Synergies** : [[Forbidden Knowledge]], [[Battle Frenzy]], [[Echo Chamber]]
- [[Attack Speed]] - Vitesse d'attaque
- [[Cast Speed]] - Vitesse de cast
- [[Stat Bonuses]] - Catégorie
- [[Hybrid Builds]] - Style de jeu optimal

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\time_distortion_bonus.tres`