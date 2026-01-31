---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionEffectReward
tags: [storm_caller, lightning, aoe, periodic, elemental]
status: implemented
rarity: varies
---

# Storm Caller

## Description
Une corruption qui fait apparaître des éclairs périodiques frappant les ennemis proches. Cette corruption transforme le porteur en un conduit vivant de l'énergie électrique, créant un champ de tempête permanent autour de lui.

## Lore
Les tempêtes de l'Éther Sombre ne sont pas des phénomènes naturels, mais les échos de fureurs divines oubliées. Cette corruption permet de canaliser ces énergies chaotiques, transformant l'aura du porteur en un nexus de foudre. Chaque battement de cœur résonne avec le tonnerre des anciens, et l'air lui-même se charge d'électricité meurtrière qui cherche constamment de nouvelles victimes.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Special Effects | Effet unique |
| **Classe de Base** | CorruptionEffectReward | Type de récompense |
| **Durée** | Permanente (-1.0) | Tant que la corruption est active |
| **Intensité** | 1.0 | Effet standard |
| **Fréquence** | Toutes les 3 secondes | Déclenchement automatique |

## Mécaniques de Tempête

### Système de Foudre Automatique
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Déclencheur** | Timer automatique | Toutes les 3 secondes |
| **Zone d'Effet** | Nearby enemies | Rayon autour du joueur |
| **Type de Dégâts** | Lightning/Elemental | Dégâts électriques |
| **Ciblage** | Automatique | Tous ennemis dans la zone |
| **Pénétration** | Multiple targets | Frappe plusieurs ennemis |

### Caractéristiques de l'Éclair
```
Fréquence: 3.0 secondes (fixe)
Zone: Radius autour du player
Dégâts: Variable selon le tier
Type: Lightning damage
Effet: Instant strike
```

## Système de Tiers

### Valeurs par Tier (Estimées)
| Tier | Dégâts par Éclair | Rayon d'Effet | DPS Moyen |
|------|-------------------|---------------|-----------|
| **Minor** | 50-75 | 3-4 unités | 17-25 DPS |
| **Moderate** | 75-100 | 4-5 unités | 25-33 DPS |
| **Major** | 100-150 | 5-6 unités | 33-50 DPS |
| **Epic** | 150-200 | 6-7 unités | 50-67 DPS |
| **Legendary** | 200-300 | 7-8 unités | 67-100 DPS |

### Code Couleur des Tiers
- **Blanc** : Éclairs faibles, petit rayon
- **Vert** : Éclairs modérés, rayon moyen
- **Bleu** : Éclairs puissants, bon rayon
- **Violet** : Éclairs très puissants, grand rayon
- **Or** : Éclairs dévastateurs, très grand rayon

## Avantages Stratégiques

**Forces :**
- Dégâts passifs constants
- Zone d'effet automatique
- Pas de coût en ressources
- Fonctionne pendant le mouvement
- Excellent pour le crowd control
- Synergise avec builds électriques

**Synergies Exceptionnelles :**
- **Elemental Resonance** : +25% dégâts élémentaires
- **Movement Speed Builds** : Kite tout en infligeant des dégâts
- **Tank Builds** : Dégâts passifs pendant le tanking
- **Lightning Skills** : Thème électrique cohérent
- **AoE Builds** : Multiplie les sources de dégâts de zone

## Applications Tactiques

### Builds de Kiting
- Parfait pour les joueurs mobiles
- Dégâts constants pendant les déplacements
- Excellent contre les swarms d'ennemis

### Builds Défensifs
- Dégâts passifs pour les tanks
- Décourage les ennemis de s'approcher
- Complément idéal aux builds de survie

### Synergies Cross-Corruption
- **Avec Elemental Resonance** : +25% de dégâts d'éclairs
- **Avec Movement Speed** : Kiting plus efficace
- **Avec Area Damage** : Multiple sources AoE
- **Avec Critical Mass** : Peut critiquer sur les éclairs

## Considérations de Balance

### Mécaniques d'Équilibrage
- Fréquence fixe (ne peut pas être accélérée)
- Dégâts modérés (pas d'one-shot)
- Portée limitée (encourage l'engagement)
- Type élémentaire (résistances applicables)

### Impact sur la Progression
- Excellent pour le farming passif
- Particulièrement efficace dans les zones denses
- Aide significativement les builds low-damage
- Peut trivialiser les weak enemies

## Implémentation Technique

### Fichiers Source
- **Corruption** : `storm_caller_bonus.tres`
- **Effect** : `storm_caller_buff.tres`
- **Script** : `corruption_effect_reward.gd`

### Intégration Système
```gdscript
# Type: CorruptionEffectReward
effects_to_apply = [storm_caller_buff.tres]
effect_durations = [-1.0]  # Permanent
effect_intensities = [1.0]  # Standard intensity
```

### Template de Description
```
"Nearby enemies are struck by lightning every 3 seconds"
```

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Builds mobiles, elemental builds, tanks
- **Medium Priority** : Builds hybrides, crowd controllers
- **Low Priority** : Builds pure single-target, glass cannons

### Moment Optimal
- **Early Game** : Très puissant pour la survie
- **Mid Game** : Excellent farming tool
- **Late Game** : Complément solide aux autres corruptions

## Risques et Contreparties

### Limitations
- Fréquence fixe non améliorable
- Portée limitée (nearby enemies)
- Dégâts élémentaires (résistances)
- Pas de contrôle direct

### Gestion Optimale
- Positionner proche des groupes d'ennemis
- Combiner avec des bonus de dégâts élémentaires
- Utiliser la mobilité pour maximiser l'exposition
- Synergie avec d'autres effets AoE

## Interaction avec d'Autres Systèmes

### Systèmes Élémentaires
- Profite des bonus de dégâts élémentaires
- Peut déclencher des effets on-hit électriques
- Synergise avec les résistances élémentaires du joueur

### Systèmes de Position
- Encourage le positioning agressif
- Reward la proximité avec les ennemis
- Complemente les builds de melee et tank

## Effets Visuels et Audio

### Feedback Visuel
- Éclairs visibles frappant les ennemis
- Effet de chain lightning possible
- Aura électrique autour du personnage
- Particules d'électricité atmosphérique

### Feedback Audio
- Son de tonnerre toutes les 3 secondes
- Crépitement électrique constant
- Impact d'éclair sur les ennemis
- Ambiance de tempête

## Related

- [[Corruptions]] - Système principal
- [[Elemental Damage]] - Type de dégâts
- **Synergies** : [[Elemental Resonance]], [[Movement Speed]]
- [[Passive Effects]] - Mécanisme passif
- [[Area of Effect]] - Zone d'effet
- [[Special Effects]] - Catégorie
- [[Lightning Damage]] - Type spécifique

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\storm_caller_bonus.tres`