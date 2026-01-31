---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [elemental_resonance, elemental, damage, magic, elements]
status: implemented
rarity: varies
---

# Elemental Resonance

## Description
Une corruption élémentaire qui augmente tous les dégâts élémentaires. Cette corruption harmonise le porteur avec les forces primordiales, amplifiant la puissance de feu, glace, foudre et autres énergies élémentaires.

## Lore
L'Éther Sombre pulse avec les énergies primordiales qui ont donné naissance aux éléments. Cette corruption permet de se synchroniser avec ces fréquences fondamentales, créant une résonance qui amplifie toute manifestation élémentaire. Le porteur devient un conduit vivant pour les forces de la création, capable de canaliser et d'amplifier les énergies élémentaires avec une efficacité surnaturelle.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Elemental | Spécialisation élémentaire |
| **Focus** | All Elements | Tous types élémentaires |

## Mécaniques de Résonance

### Système d'Amplification Élémentaire
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Elemental Damage** | +15/20/25% | Variable selon tier |
| **Types Affectés** | Tous éléments | Fire, Ice, Lightning, etc. |
| **Application** | Multiplicateur | Après calculs de base |
| **Synergie** | Universal elemental | Tous skills élémentaires |
| **Stacking** | Avec autres bonus | Se cumule |

### Calcul des Dégâts Élémentaires
```
Elemental_Damage_Final = Base_Elemental × (1 + Resonance_Bonus/100)
Types_Affected = [Fire, Ice, Lightning, Acid, etc.]
```

## Système de Tiers

### Valeurs par Tier
| Tier | Elemental Damage | Impact Magique | Puissance Globale |
|------|------------------|----------------|-------------------|
| **Minor** | +15% | Modéré | Bonne |
| **Moderate** | +17% | Solide | Très bonne |
| **Major** | +20% | Fort | Excellente |
| **Epic** | +22% | Très fort | Puissante |
| **Legendary** | +25% | Exceptionnel | Dévastatrice |

### Code Couleur des Tiers
- **Blanc** : +15% elemental damage
- **Vert** : +17% elemental damage
- **Bleu** : +20% elemental damage
- **Violet** : +22% elemental damage
- **Or** : +25% elemental damage

## Avantages Stratégiques

**Forces :**
- Bonus universal sur tous éléments
- Excellent pour builds magiques
- Synergie avec tous skills élémentaires
- Multiplicateur simple et efficace
- Compatible avec tous éléments
- Scaling excellent en late game

**Synergies Exceptionnelles :**
- **Storm Caller** : Lightning damage amplifié
- **Forbidden Knowledge** : Caster élémentaire optimal
- **Echo Chamber** : Double cast élémentaire
- **Elemental Skills** : Tous skills élémentaires
- **Elemental Weapons** : Armes enchantées

## Applications Tactiques

### Builds Caster Élémentaire
- Core corruption pour mages élémentaires
- Excellent pour builds spécialisés
- Synergie avec tous sorts élémentaires

### Builds Hybrides Élémentaires
- Améliore les weapons élémentaires
- Excellent pour builds mixed
- Polyvalent sur tous éléments

### Synergies Cross-Corruption
- **Avec Storm Caller** : Lightning build optimal
- **Avec Forbidden Knowledge** : Mage élémentaire
- **Avec Echo Chamber** : Double cast élémentaire
- **Avec Critical Mass** : Critique élémentaire

## Considérations de Balance

### Mécaniques d'Équilibrage
- Bonus pourcentage (scale avec progression)
- Limité aux dégâts élémentaires only
- Plus efficace avec high elemental base
- Encourage la spécialisation élémentaire

### Impact sur la Progression
- Transformateur pour builds élémentaires
- Scaling excellent en late game
- Encourage l'utilisation de skills élémentaires
- Foundation pour builds magiques avancés

## Implémentation Technique

### Fichiers Source
- **Corruption** : `elemental_resonance_bonus.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Elemental damage bonus

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [StatType.ELEMENTAL_DAMAGE]
values = [tier_elemental_percentage]
elements_affected = [FIRE, ICE, LIGHTNING, ACID, POISON, etc.]
```

### Valeurs Techniques
- **Elemental Damage** : Valeur en pourcentage (15-25)
- **Application** : Multiplicateur global élémentaire

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Builds élémentaires, casters, mages
- **Medium Priority** : Builds hybrides avec éléments
- **Low Priority** : Builds pure physique, non-élémentaires

### Moment Optimal
- **Early Game** : Bon pour builds élémentaires
- **Mid Game** : Excellent scaling
- **Late Game** : Essential pour casters élémentaires

## Risques et Contreparties

### Limitations
- Limité aux dégâts élémentaires only
- Pas d'effet sur dégâts physiques
- Plus efficace avec high elemental base
- Dépendant du style de build

### Gestion Optimale
- Focus sur skills élémentaires
- Combiner avec elemental weapons
- Stack avec autres bonus magiques
- Optimiser pour elemental synergies

## Interaction avec d'Autres Systèmes

### Système Élémentaire
- Améliore tous types d'éléments
- Synergie avec resistances ennemies
- Compatible avec elemental effects
- Stack avec elemental penetration

### Système Magique
- Excellent pour spell casters
- Synergie avec magical weapons
- Compatible avec enchantments
- Améliore elemental proc effects

## Types d'Éléments Affectés

### Éléments Principaux
- **Fire** : Dégâts de feu et combustion
- **Ice** : Dégâts de glace et ralentissement
- **Lightning** : Dégâts électriques et paralysie
- **Acid** : Dégâts d'acide et corrosion

### Éléments Avancés
- **Poison** : DoT toxique
- **Arcane** : Magie pure
- **Shadow** : Énergies sombres
- **Holy** : Énergies divines

## Builds Recommandés

### Elemental Master
```
Core: Elemental Resonance + Storm Caller + Forbidden Knowledge
Style: Pure elemental damage
Focus: Magical devastation
```

### Battle Mage
```
Core: Elemental Resonance + Echo Chamber + Critical Mass
Style: Elemental combat hybrid
Focus: Versatile elemental warrior
```

### Storm Lord
```
Core: Elemental Resonance + Storm Caller + Time Distortion
Style: Lightning specialist
Focus: Electrical domination
```

## Related

- [[Corruptions]] - Système principal
- [[Elemental System]] - Système élémentaire
- **Synergies** : [[Dark Ether/Glossary/Skills and Perks/Elemental/Storm Caller]], [[Forbidden Knowledge]], [[Echo Chamber]]
- [[Elemental Damage]] - Types de dégâts
- [[Magic System]] - Système magique
- [[Stat Bonuses]] - Catégorie
- [[Caster Builds]] - Style de jeu optimal

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\elemental_resonance_bonus.tres`