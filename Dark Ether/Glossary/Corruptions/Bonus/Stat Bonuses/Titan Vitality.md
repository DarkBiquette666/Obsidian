---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [titan_vitality, health, vitality, endurance, life]
status: implemented
rarity: varies
---

# Titan Vitality

## Description
Une corruption de vitalité qui augmente les points de vie maximum. Cette corruption infuse le porteur avec la robustesse légendaire des titans, renforçant sa constitution jusqu'à atteindre des niveaux de résistance surhumains.

## Lore
Les titans de l'Éther Sombre étaient des êtres d'une vitalité incommensurable, capables de résister aux forces les plus destructrices de cette dimension. Cette corruption canalise un fragment de leur essence vitale, transformant le porteur en un bastion de vie. Chaque cellule se renforce, chaque organe se fortifie, créant une constitution qui défie les limites mortelles et repousse les frontières de la survie.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Titan | Spécialisation vitalité |
| **Focus** | Health Pool | Pool de vie |

## Mécaniques de Vitalité Titanesque

### Système de Constitution Renforcée
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Health Bonus** | +25/50/75/100 | Variable selon tier |
| **Application** | Flat bonus | Ajout direct au pool |
| **Synergie** | Avec regen effects | Scale avec % regen |
| **Stacking** | Avec autres HP bonus | Se cumule |
| **Durée** | Permanente | Toujours actif |

### Calcul de la Vitalité
```
Health_Total = Base_Health + Titan_Vitality_Bonus
Effective_HP = Health_Total × (1 + Defensive_Modifiers)
```

## Système de Tiers

### Valeurs par Tier
| Tier | Health Bonus | Impact Survie | Robustesse Globale |
|------|--------------|---------------|-------------------|
| **Minor** | +25 | Modéré | Bonne |
| **Moderate** | +50 | Solide | Très bonne |
| **Major** | +75 | Important | Excellente |
| **Epic** | +100 | Majeur | Puissante |
| **Legendary** | +100 | Exceptionnel | Titanesque |

### Code Couleur des Tiers
- **Blanc** : +25 health
- **Vert** : +50 health
- **Bleu** : +75 health
- **Violet** : +100 health
- **Or** : +100 health (meilleures synergies)

## Avantages Stratégiques

**Forces :**
- Augmentation directe de survie
- Excellent early game impact
- Synergie avec tous defensive builds
- Base solide pour tank builds
- Compatible avec tous playstyles
- Foundation pour builds HP-based

**Synergies Exceptionnelles :**
- **Corrupted Endurance** : HP + regen combo
- **Titan's Regeneration** : HP + regen percentage
- **Vampiric Essence** : Larger life leech pool
- **Defensive Skills** : Plus de HP à protéger
- **Tank Builds** : Core vitality enhancement

## Applications Tactiques

### Builds Tank Spécialisés
- Core corruption pour tanks
- Foundation pour defensive builds
- Améliore drastiquement la survie

### Builds Equilibrés
- Excellent pour tous characters
- Améliore la sécurité générale
- Permet des playstyles plus agressifs

### Synergies Cross-Corruption
- **Avec Corrupted Endurance** : Tank supreme
- **Avec Titan's Regeneration** : Sustain optimal
- **Avec Vampiric Essence** : Life leech efficace
- **Avec Storm Caller** : Tank avec DPS passif

## Considérations de Balance

### Mécaniques d'Équilibrage
- Bonus flat (plus impactant early game)
- Simple health increase (pas d'effets complexes)
- Encourage les builds défensifs
- Balance risk/reward pour glass cannons

### Impact sur la Progression
- Transformateur pour la survie early game
- Permet l'accès à contenu plus difficile
- Base solide pour character development
- Scaling naturel avec defensive gear

## Implémentation Technique

### Fichiers Source
- **Corruption** : `titan_vitality.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Health maximum flat bonus

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [StatType.HEALTH_MAX]
values = [tier_health_bonus]
# Flat addition to maximum health
```

### Valeurs Techniques
- **Health Bonus** : Valeur plate (25/50/75/100)
- **Application** : Addition directe au pool HP

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Tank builds, defensive builds, nouveau characters
- **Medium Priority** : Builds balanced, tous playstyles
- **Low Priority** : Glass cannons (dépend de la stratégie)

### Moment Optimal
- **Early Game** : Impact maximum (flat bonus)
- **Mid Game** : Solide foundation pour progression
- **Late Game** : Synergise avec autres corruptions

## Risques et Contreparties

### Limitations
- Bonus flat (scaling diminishing late game)
- Purely defensive (pas d'amélioration offensive)
- Plus impactant early que late game
- Simple effet (pas de mécaniques complexes)

### Gestion Optimale
- Acquérir tôt pour maximum d'impact
- Combiner avec defensive synergies
- Stack avec autres health bonuses
- Foundation pour builds tank avancés

## Interaction avec d'Autres Systèmes

### Système de Santé
- Augmente directement le pool de vie
- Synergie avec all healing effects
- Compatible avec damage reduction
- Base pour percentage-based effects

### Système de Survie
- Améliore la survivability globale
- Plus de marge d'erreur en combat
- Permet des engagements plus risqués
- Foundation pour aggressive defensive play

## Builds Recommandés

### Immortal Tank
```
Core: Titan Vitality + Corrupted Endurance + Titan's Regeneration
Style: Maximum survivability
Focus: Unkillable defense
```

### Balanced Warrior
```
Core: Titan Vitality + Critical Mass + Storm Caller
Style: Defensive with offense
Focus: Balanced sustainability
```

### Life Leech Master
```
Core: Titan Vitality + Vampiric Essence + Blood Thirst
Style: Aggressive sustain
Focus: Life steal optimization
```

## Progression Scaling

### Early Game Impact
- **+25 HP** : ~50% increase typical
- **+50 HP** : ~100% increase potential
- Transformative pour new characters

### Late Game Synergies
- Base pour percentage bonuses
- Foundation pour complex builds
- Multiplier effects avec defensive gear

## Related

- [[Corruptions]] - Système principal
- [[Health System]] - Système de santé
- **Synergies** : [[Corrupted Endurance]], [[Titan's Regeneration]], [[Vampiric Essence]]
- [[Tank Builds]] - Style de jeu optimal
- [[Defensive Stats]] - Statistiques défensives
- [[Stat Bonuses]] - Catégorie
- [[Survival]] - Mécaniques de survie

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\titan_vitality.tres`