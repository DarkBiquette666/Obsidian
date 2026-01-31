---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [silent_blade, assassin, critical, stealth, precision]
status: implemented
rarity: varies
---

# Silent Blade

## Description
Une corruption assassine qui augmente les chances de critique et la puissance des coups critiques. Cette corruption transforme le porteur en un tueur silencieux, capable de frapper avec une précision mortelle dans les moments cruciaux.

## Lore
Dans les brumes de l'Éther Sombre, les assassins les plus redoutés ont appris à fusionner avec les ombres elles-mêmes. Cette corruption affûte non seulement la lame, mais aussi l'esprit, permettant de percevoir les failles dans les défenses ennemies et de frapper avec une précision chirurgicale. Chaque attaque devient une danse de mort silencieuse, où seul le résultat compte.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Assassin | Spécialisation assassin |
| **Focus** | Critical System | Système de critique |

## Mécaniques d'Assassinat

### Système de Critique Amélioré
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Critical Chance** | +0.5-1.5% | Augmente les chances de critique |
| **Critical Multiplier** | +20-50% | Multiplie les dégâts critiques |
| **Synergie** | Dual bonus | Chance ET puissance |
| **Application** | Toutes attaques | Universal sur tous dégâts |
| **Stacking** | Avec autres crit bonuses | Se cumule |

### Calcul des Critiques
```
Chance_Critique_Finale = Base_Crit + Silent_Blade_Bonus
Dégâts_Critiques = Base_Damage × (Base_Crit_Multi + Silent_Blade_Multi)
```

## Système de Tiers

### Valeurs par Tier
| Tier | Critical Chance | Critical Multiplier | Puissance Combinée |
|------|-----------------|---------------------|-------------------|
| **Minor** | +0.5% | +20% | Modeste |
| **Moderate** | +0.8% | +30% | Solide |
| **Major** | +1.0% | +35% | Puissant |
| **Epic** | +1.2% | +40% | Très puissant |
| **Legendary** | +1.5% | +50% | Dévastateur |

### Code Couleur des Tiers
- **Blanc** : +0.5% chance, +20% multiplier
- **Vert** : +0.8% chance, +30% multiplier
- **Bleu** : +1.0% chance, +35% multiplier
- **Violet** : +1.2% chance, +40% multiplier
- **Or** : +1.5% chance, +50% multiplier

## Avantages Stratégiques

**Forces :**
- Double bonus (chance + puissance)
- Synergie exceptionnelle avec builds critiques
- Augmente significativement le DPS en burst
- Excellent pour les builds single-target
- Scaling multiplicatif avec base crit
- Synergise avec tous types d'armes

**Synergies Exceptionnelles :**
- **Critical Mass** : Stack les bonus de critique
- **Fortunian's Eye** : Triple synergie critique
- **Echo Chamber** : Double les chances de critiques
- **High-damage Skills** : Maximise l'impact des critiques
- **Single-target Builds** : Optimise les boss fights

## Applications Tactiques

### Builds Assassin Pur
- Core corruption pour builds critiques
- Parfait pour les joueurs single-target focused
- Excellent pour les boss encounters

### Builds Hybrides
- Complément solide pour tous builds
- Améliore la versatilité offensive
- Bon investissement risk/reward

### Synergies Cross-Corruption
- **Avec Critical Mass** : Stack critique intense
- **Avec Dark Power** : Critique + damage global
- **Avec Echo Chamber** : Plus de chances de critiques doubles
- **Avec Fortunian's Eye** : Triple bonus critique

## Considérations de Balance

### Mécaniques d'Équilibrage
- Bonus modestes pour éviter l'overpowered
- Scaling linéaire (non exponentiel)
- Dépendant des dégâts de base
- Plus efficace sur high-damage attacks

### Impact sur la Progression
- Améliore significativement le boss killing
- Plus efficace sur les weapons/skills à gros dégâts
- Scaling naturel avec la progression du jeu
- Devient plus puissant avec d'autres corruptions critiques

## Implémentation Technique

### Fichiers Source
- **Corruption** : `assassin_reward.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Critical chance + multiplier

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [
    StatType.CRITICAL_CHANCE,
    StatType.CRITICAL_MULTIPLIER
]
values = [tier_crit_chance, tier_crit_multiplier]
```

### Valeurs Techniques
- **Critical Chance** : Valeur en pourcentage (0.5-1.5)
- **Critical Multiplier** : Valeur en pourcentage (20-50)

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Builds critiques, assassins, single-target
- **Medium Priority** : Builds hybrides, balanced damage
- **Low Priority** : Builds pure AoE, support builds

### Moment Optimal
- **Early Game** : Très bon si disponible
- **Mid Game** : Excellent pour la progression
- **Late Game** : Synergie avec autres corruptions critiques

## Risques et Contreparties

### Limitations
- Plus efficace sur high base damage
- Dépendant de la chance (RNG)
- Scaling avec l'équipement
- Moins visible sur fast, low-damage attacks

### Gestion Optimale
- Combiner avec des armes à gros dégâts
- Stack avec d'autres bonus critiques
- Focus sur single-target encounters
- Optimiser le timing des attaques importantes

## Interaction avec d'Autres Systèmes

### Système de Combat
- Affecte tous les types d'attaques
- Synergie avec weapon scaling
- Compatible avec tous les skill types
- Améliore l'efficacité des cooldowns

### Systèmes de Chance
- Se cumule avec base critical chance
- Multiplicatif avec critical damage scaling
- Synergie avec luck-based effects
- Compatible avec proc-based abilities

## Builds Recommandés

### Assassin Pur
```
Core: Silent Blade + Critical Mass + Fortunian's Eye
Style: High single-target damage
Focus: Boss killing, precision strikes
```

### Hybrid Critical
```
Core: Silent Blade + Echo Chamber + Dark Power
Style: Balanced offensive
Focus: Versatile damage output
```

### Glass Cannon
```
Core: Silent Blade + Anti-Matter Orb + Dark Power
Style: High risk, high reward
Focus: Maximum damage potential
```

## Related

- [[Corruptions]] - Système principal
- [[Critical System]] - Mécanisme de critique
- **Synergies** : [[Critical Mass]], [[Fortunian's Eye]], [[Echo Chamber]]
- [[Assassin Builds]] - Style de jeu
- [[Single Target]] - Application tactique
- [[Stat Bonuses]] - Catégorie
- [[Damage Scaling]] - Mécanisme de scaling

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\assassin_reward.tres`