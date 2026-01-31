---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [forbidden_knowledge, scholar, mana, cast_speed, magic]
status: implemented
rarity: varies
---

# Forbidden Knowledge

## Description
Une corruption érudite qui augmente le mana maximum et la vitesse de cast. Cette corruption ouvre l'accès à des connaissances interdites, permettant de manipuler la magie avec une efficacité et une puissance accrues.

## Lore
Dans les bibliothèques oubliées de l'Éther Sombre, certains grimoires murmurent des secrets que l'esprit mortel ne devrait jamais connaître. Cette corruption brise les barrières mentales, permettant l'absorption de connaissances mystiques qui expandent les capacités magiques du porteur. Le prix à payer est une transformation graduelle de l'âme, mais le pouvoir acquis vaut tous les sacrifices.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Scholar | Spécialisation magique |
| **Focus** | Mana & Cast Speed | Système magique |

## Mécaniques de Savoir Interdit

### Système de Boost Magique
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Mana Bonus** | +50 points | Fixe pour tous tiers |
| **Cast Speed** | +20-25% | Variable selon tier |
| **Synergie** | Resources + Speed | Double amélioration |
| **Application** | Permanent | Toujours actif |
| **Stacking** | Avec autres bonus | Se cumule |

### Calcul des Améliorations
```
Mana_Total = Base_Mana + 50
Cast_Speed_Final = Base_Cast_Speed × (1 + Bonus_Percentage/100)
```

## Système de Tiers

### Valeurs par Tier
| Tier | Mana Bonus | Cast Speed | Efficacité Magique |
|------|------------|------------|-------------------|
| **Minor** | +50 | +20% | Bonne |
| **Moderate** | +50 | +21% | Solide |
| **Major** | +50 | +22% | Très bonne |
| **Epic** | +50 | +23% | Excellente |
| **Legendary** | +50 | +25% | Exceptionnelle |

### Code Couleur des Tiers
- **Blanc** : +50 mana, +20% cast speed
- **Vert** : +50 mana, +21% cast speed
- **Bleu** : +50 mana, +22% cast speed
- **Violet** : +50 mana, +23% cast speed
- **Or** : +50 mana, +25% cast speed

## Avantages Stratégiques

**Forces :**
- Double bonus (resources + speed)
- Excellent pour tous builds magiques
- Mana bonus substantiel early game
- Cast speed améliore le DPS et la qualité de vie
- Synergie exceptionnelle avec skills coûteux
- Permet des rotations de sorts plus complexes

**Synergies Exceptionnelles :**
- **Energy Reservoir** : Stack mana pour pool massive
- **Echo Chamber** : Plus de double casts grâce au speed
- **High-cost Skills** : Sustain amélioré
- **Elemental Resonance** : Caster build optimal
- **Storm Caller** : Thème magique cohérent

## Applications Tactiques

### Builds Caster Pur
- Core corruption pour mages
- Permet l'utilisation de skills coûteux
- Améliore la fluidité du gameplay

### Builds Hybrides
- Excellent pour characters mixed
- Améliore la versatilité magique
- Permet l'intégration de sorts utilitaires

### Synergies Cross-Corruption
- **Avec Energy Reservoir** : Pool mana massive
- **Avec Echo Chamber** : Cast speed + double cast
- **Avec Elemental Resonance** : Caster électrique optimal
- **Avec Time Distortion** : Speed global maximum

## Considérations de Balance

### Mécaniques d'Équilibrage
- Mana fixe (non scaling avec tiers)
- Cast speed modeste (évite l'overpowered)
- Plus efficace early game (mana flat)
- Scaling relatif avec progression

### Impact sur la Progression
- Transformateur en early game
- Permet l'accès à builds mana-hungry
- Améliore significativement la qualité de vie
- Base solide pour builds magiques avancés

## Implémentation Technique

### Fichiers Source
- **Corruption** : `scholar_reward.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Mana max + cast speed

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [
    StatType.MANA_MAX,
    StatType.CAST_SPEED
]
values = [50, tier_cast_speed_percentage]
```

### Valeurs Techniques
- **Mana Bonus** : Valeur plate (+50)
- **Cast Speed** : Valeur en pourcentage (20-25)

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Builds caster, mages, skill-heavy
- **Medium Priority** : Builds hybrides, utility users
- **Low Priority** : Builds pure physical, melee only

### Moment Optimal
- **Early Game** : Excellent investissement
- **Mid Game** : Solide pour transition magique
- **Late Game** : Base pour builds caster avancés

## Risques et Contreparties

### Limitations
- Mana bonus fixe (moins impactant late game)
- Cast speed modeste comparé à spécialisés
- Plus efficace sur characters mana-dependant
- Nécessite des sorts pour être optimal

### Gestion Optimale
- Acquérir tôt pour maximum d'impact
- Combiner avec autres bonus mana
- Utiliser pour débloquer builds mana-hungry
- Stack avec d'autres améliorations de cast

## Interaction avec d'Autres Systèmes

### Système de Mana
- Augmente le pool de ressources disponible
- Permet des rotations plus longues
- Synergie avec mana regeneration
- Compatible avec mana leech effects

### Système de Cast
- Améliore tous les types de sorts
- Réduit les temps de cast globalement
- Synergie avec channeling abilities
- Compatible avec cast-on-crit mechanics

## Builds Recommandés

### Scholar Pur
```
Core: Forbidden Knowledge + Energy Reservoir + Elemental Resonance
Style: Pure magical damage
Focus: High-cost spells, elemental mastery
```

### Hybrid Caster
```
Core: Forbidden Knowledge + Echo Chamber + Time Distortion
Style: Versatile magic + physical
Focus: Balanced approach, speed
```

### Battle Mage
```
Core: Forbidden Knowledge + Storm Caller + Critical Mass
Style: Close combat + magic
Focus: Aggressive caster
```

## Related

- [[Corruptions]] - Système principal
- [[Mana System]] - Gestion des ressources
- **Synergies** : [[Energy Reservoir]], [[Echo Chamber]], [[Time Distortion]]
- [[Cast Speed]] - Mécanisme de vitesse
- [[Scholar Builds]] - Style de jeu
- [[Stat Bonuses]] - Catégorie
- [[Magic System]] - Système magique

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\scholar_reward.tres`