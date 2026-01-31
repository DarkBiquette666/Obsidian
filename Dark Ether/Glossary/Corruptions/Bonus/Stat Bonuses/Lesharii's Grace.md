---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [leshariis_grace, movement_speed, mobility, agility, lesharii]
status: implemented
rarity: varies
---

# Lesharii's Grace

## Description
Une corruption de mobilité qui augmente la vitesse de déplacement. Cette corruption octroie la grâce légendaire des Lesharii, transformant le porteur en un être d'une agilité et d'une fluidité de mouvement surnaturelles.

## Lore
Les Lesharii étaient les danseurs de l'Éther Sombre, des êtres éthérés qui se mouvaient avec une grâce qui défiait les lois de la physique. Leurs mouvements n'étaient pas seulement rapides, mais empreints d'une beauté hypnotique qui semblait rendre l'espace lui-même plus malléable. Cette corruption canalise un fragment de leur essence divine, permettant au porteur de glisser à travers le monde avec une fluidité qui transforme chaque pas en une danse, chaque déplacement en une œuvre d'art martiale.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Lesharii | Spécialisation mobilité |
| **Focus** | Movement Speed | Vitesse de déplacement |

## Mécaniques de Grâce Lesharii

### Système de Mobilité Améliorée
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Movement Speed** | +5/10/20% | Variable selon tier |
| **Application** | Percentage bonus | Multiplicateur de vitesse |
| **Synergie** | Avec mobility builds | Kiting et positioning |
| **Stacking** | Avec autres speed | Se cumule |
| **Durée** | Permanente | Toujours actif |

### Calcul de la Mobilité
```
Movement_Speed_Final = Base_Speed × (1 + Grace_Bonus/100)
Effective_Mobility = Movement_Speed × Terrain_Modifiers
```

## Système de Tiers

### Valeurs par Tier
| Tier | Movement Speed | Impact Mobilité | Agilité Globale |
|------|----------------|-----------------|----------------|
| **Minor** | +5% | Modéré | Bonne |
| **Moderate** | +8% | Solide | Très bonne |
| **Major** | +10% | Important | Excellente |
| **Epic** | +15% | Majeur | Puissante |
| **Legendary** | +20% | Exceptionnel | Gracieuse |

### Code Couleur des Tiers
- **Blanc** : +5% movement speed
- **Vert** : +8% movement speed
- **Bleu** : +10% movement speed
- **Violet** : +15% movement speed
- **Or** : +20% movement speed

## Avantages Stratégiques

**Forces :**
- Améliore la qualité de vie générale
- Excellent pour kiting et positioning
- Améliore l'efficacité de farming
- Synergie avec tous playstyles
- Essential pour builds mobiles
- Améliore la survie par évasion

**Synergies Exceptionnelles :**
- **Blood Thirst** : Fast farming pour plus de kills
- **Storm Caller** : Kiting avec DPS passif
- **Ranged Builds** : Positioning optimal
- **Farming Builds** : Efficacité de déplacement
- **Hit-and-Run Tactics** : Mobilité tactique

## Applications Tactiques

### Builds Kiting Spécialisés
- Core corruption pour kiters
- Essential pour ranged builds
- Améliore la survie par mobility

### Builds Farming
- Excellent pour efficiency farming
- Améliore la vitesse de clear
- Plus de zones explorées par minute

### Synergies Cross-Corruption
- **Avec Blood Thirst** : Fast kill farming
- **Avec Storm Caller** : Mobile AOE DPS
- **Avec Thirst for Knowledge** : Efficient XP farming
- **Avec Echo Chamber** : Mobile burst DPS

## Considérations de Balance

### Mécaniques d'Équilibrage
- Amélioration de qualité de vie
- Plus utility que direct power
- Améliore indirectement la survie
- Universal benefit pour tous builds

### Impact sur la Progression
- Améliore l'efficacité générale
- Plus de contenu accessible par unité temps
- Meilleur positioning en combat
- Foundation pour builds speed-based

## Implémentation Technique

### Fichiers Source
- **Corruption** : `lesharii_grace.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Movement speed percentage

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [StatType.MOVEMENT_SPEED]
values = [tier_speed_percentage]
# Percentage bonus to base movement speed
```

### Valeurs Techniques
- **Movement Speed** : Valeur en pourcentage (5-20)
- **Application** : Multiplicateur de la vitesse de base

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Ranged builds, kiters, farmers
- **Medium Priority** : Tous builds (qualité de vie)
- **Low Priority** : Tank builds statiques (moins critique)

### Moment Optimal
- **Early Game** : Excellent pour exploration
- **Mid Game** : Améliore l'efficacité farming
- **Late Game** : Essential pour builds speed avancés

## Risques et Contreparties

### Limitations
- Plus utility que direct power
- Moins impactant pour builds statiques
- Benefit indirect (positional advantage)
- Peut encourager overextension

### Gestion Optimale
- Utiliser pour améliorer positioning
- Combiner avec ranged/mobile builds
- Optimiser pour farming efficiency
- Essential pour kiting strategies

## Interaction avec d'Autres Systèmes

### Système de Combat
- Améliore le positioning tactique
- Permet les hit-and-run tactics
- Améliore la survie par évasion
- Synergie avec ranged combat

### Système d'Exploration
- Plus de zones couvertes rapidement
- Améliore l'efficacité de farming
- Plus d'opportunités de loot
- Meilleur temps/reward ratio

## Builds Recommandés

### Speed Farmer
```
Core: Lesharii's Grace + Blood Thirst + Thirst for Knowledge
Style: Efficient farming
Focus: Maximum efficiency per minute
```

### Mobile Ranger
```
Core: Lesharii's Grace + Storm Caller + Critical Mass
Style: Mobile ranged DPS
Focus: Kiting with constant damage
```

### Scout Explorer
```
Core: Lesharii's Grace + Echo Chamber + Time Distortion
Style: Fast exploration
Focus: Speed and mobility
```

## Calculs d'Efficacité

### Impact sur Farming
- **+10% speed** : 10% more areas per hour
- **+20% speed** : 20% more encounters per session
- Multiplicatif avec other efficiency bonuses

### Combat Benefits
- Better positioning = reduced damage taken
- Improved escape opportunities
- Enhanced tactical options

## Synergies Raciales

### Lore Connection
- Tribute aux Lesharii ancestraux
- Canalise leur grace légendaire
- Respect de leur héritage de mobilité
- Harmonie avec leur essence spirituelle

## Related

- [[Corruptions]] - Système principal
- [[Movement System]] - Système de déplacement
- **Synergies** : [[Blood Thirst]], [[Dark Ether/Glossary/Skills and Perks/Elemental/Storm Caller]], [[Thirst for Knowledge]]
- [[Mobility]] - Mécaniques de mobilité
- [[Kiting Builds]] - Style de jeu mobile
- [[Stat Bonuses]] - Catégorie
- [[Lesharii Lore]] - Héritage racial

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\lesharii_grace.tres`