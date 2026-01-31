---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [energy_reservoir, mana, energy, magic, resources]
status: implemented
rarity: varies
---

# Energy Reservoir

## Description
Une corruption énergétique qui augmente le mana maximum. Cette corruption crée un réservoir d'énergie mystique plus profond, permettant de canaliser plus de magie et d'utiliser des sorts plus puissants ou plus fréquents.

## Lore
Dans l'Éther Sombre, l'énergie magique existe sous sa forme la plus pure et la plus concentrée. Cette corruption transforme l'âme du porteur en un réceptacle plus vaste pour ces énergies primordiales, creusant des canaux spirituels plus profonds qui peuvent contenir des quantités exponentiellement plus importantes de mana. Chaque fibre de l'être devient un conduit, chaque pensée une antenne pour capter et stocker l'énergie mystique ambiante.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Energy | Spécialisation énergétique |
| **Focus** | Mana Pool | Réserves magiques |

## Mécaniques de Réservoir Énergétique

### Système de Capacité Magique
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Mana Bonus** | +15/30/60 | Variable selon tier |
| **Application** | Flat bonus | Ajout direct au pool |
| **Synergie** | Avec regen effects | Plus de mana à regen |
| **Stacking** | Avec autres mana bonus | Se cumule |
| **Durée** | Permanente | Toujours actif |

### Calcul de l'Énergie
```
Mana_Total = Base_Mana + Energy_Reservoir_Bonus
Effective_Mana = Mana_Total × (1 + Mana_Efficiency_Modifiers)
```

## Système de Tiers

### Valeurs par Tier
| Tier | Mana Bonus | Impact Magique | Capacité Globale |
|------|------------|----------------|------------------|
| **Minor** | +15 | Modéré | Bonne |
| **Moderate** | +30 | Solide | Très bonne |
| **Major** | +60 | Important | Excellente |
| **Epic** | +60 | Majeur | Puissante |
| **Legendary** | +60 | Exceptionnel | Mystique |

### Code Couleur des Tiers
- **Blanc** : +15 mana
- **Vert** : +30 mana
- **Bleu** : +60 mana
- **Violet** : +60 mana (meilleures synergies)
- **Or** : +60 mana (efficacité maximale)

## Avantages Stratégiques

**Forces :**
- Augmentation directe des ressources magiques
- Excellent early game impact
- Permet l'utilisation de sorts coûteux
- Foundation pour builds mana-intensive
- Compatible avec tous caster builds
- Scaling avec mana regeneration

**Synergies Exceptionnelles :**
- **Forbidden Knowledge** : Mana + cast speed combo
- **Elemental Resonance** : Pool + damage magique
- **Echo Chamber** : Plus de mana pour double casts
- **High-cost Spells** : Accès à sorts puissants
- **Mana-based Builds** : Foundation essentielle

## Applications Tactiques

### Builds Caster Spécialisés
- Core corruption pour mages
- Essential pour builds mana-hungry
- Permet des rotations complexes

### Builds Hybrides
- Excellent pour characters mixed
- Améliore la versatilité magique
- Permet l'intégration de sorts utilitaires

### Synergies Cross-Corruption
- **Avec Forbidden Knowledge** : Ultimate caster setup
- **Avec Elemental Resonance** : Mage élémentaire puissant
- **Avec Echo Chamber** : Double cast sustainable
- **Avec Storm Caller** : Pool pour sorts de support

## Considérations de Balance

### Mécaniques d'Équilibrage
- Bonus flat (plus impactant early game)
- Permet l'accès à content magique avancé
- Encourage les builds caster
- Balance entre utility et power

### Impact sur la Progression
- Transformateur pour la magie early game
- Permet l'utilisation de sorts tier élevé
- Foundation pour magical character development
- Scaling avec magical gear et abilities

## Implémentation Technique

### Fichiers Source
- **Corruption** : `energy_reservoir.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Mana maximum flat bonus

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [StatType.MANA_MAX]
values = [tier_mana_bonus]
# Flat addition to maximum mana pool
```

### Valeurs Techniques
- **Mana Bonus** : Valeur plate (15/30/60)
- **Application** : Addition directe au pool mana

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Caster builds, mages, spell-heavy builds
- **Medium Priority** : Builds hybrides avec magie
- **Low Priority** : Builds pure physical, non-magic

### Moment Optimal
- **Early Game** : Impact maximum (flat bonus)
- **Mid Game** : Permet l'accès à sorts avancés
- **Late Game** : Foundation pour builds caster complexes

## Risques et Contreparties

### Limitations
- Bonus flat (scaling diminishing late game)
- Purely utility (pas d'amélioration directe DPS)
- Plus impactant early game
- Nécessite l'utilisation de magie pour être optimal

### Gestion Optimale
- Acquérir tôt pour maximum d'impact
- Combiner avec cast speed bonuses
- Stack avec autres mana improvements
- Foundation pour builds magiques avancés

## Interaction avec d'Autres Systèmes

### Système de Mana
- Augmente directement le pool magique
- Synergie avec mana regeneration
- Compatible avec mana leech effects
- Base pour percentage-based mana effects

### Système Magique
- Permet l'utilisation de sorts coûteux
- Plus de flexibility dans spell selection
- Foundation pour complex magical rotations
- Compatible avec tous types de magie

## Builds Recommandés

### Pure Mage
```
Core: Energy Reservoir + Forbidden Knowledge + Elemental Resonance
Style: Maximum magical power
Focus: High-cost spell mastery
```

### Battle Caster
```
Core: Energy Reservoir + Echo Chamber + Critical Mass
Style: Combat magic hybrid
Focus: Sustainable spell combat
```

### Support Caster
```
Core: Energy Reservoir + Storm Caller + Time Distortion
Style: Utility magic focus
Focus: Sustained magical support
```

## Calculs d'Efficacité

### Impact Early Game
- **+15 Mana** : ~30-50% increase typical
- **+30 Mana** : ~60-100% increase potential
- **+60 Mana** : Transformative pour new casters

### Late Game Synergies
- Base pour percentage bonuses
- Foundation pour complex spell rotations
- Multiplier effects avec magical gear

## Related

- [[Corruptions]] - Système principal
- [[Mana System]] - Système de mana
- **Synergies** : [[Forbidden Knowledge]], [[Elemental Resonance]], [[Echo Chamber]]
- [[Caster Builds]] - Style de jeu optimal
- [[Magic System]] - Système magique
- [[Stat Bonuses]] - Catégorie
- [[Resource Management]] - Gestion des ressources

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\energy_reservoir.tres`