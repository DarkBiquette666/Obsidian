---
type: corruption
category: Malus
subcategory: Speed Reduction
reward_type: CorruptionStatReward
tags: [sluggish_actions, speed_reduction, slow, movement, actions]
status: implemented
rarity: varies
---

# Sluggish Actions

## Description
Une corruption ralentissante qui réduit la vitesse de déplacement, d'attaque et de cast. Cette corruption alourdit chaque geste, transformant le porteur en un être dont les actions semblent prisonnières d'un temps ralenti.

## Lore
L'Éther Sombre distord parfois le flux temporel de manière malveillante, créant des poches de temps dense où chaque seconde s'étire comme une éternité. Cette corruption emprisonne le porteur dans une bulle de temporalité épaisse, où chaque mouvement demande un effort surhumain, chaque action devient un combat contre l'inertie temporelle. C'est comme si l'univers lui-même conspirait pour ralentir l'existence du maudit, le condamnant à une danse éternelle au ralenti.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Malus Corruption | Effet négatif |
| **Catégorie** | Speed Reduction | Réduction de vitesse |
| **Classe de Base** | CorruptionStatReward | Malus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Impact** | Global | Toutes les vitesses |
| **Sévérité** | Modérée | -15% sur tout |

## Mécaniques de Ralentissement

### Système de Réduction Globale
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Movement Speed** | -15% | Déplacement ralenti |
| **Attack Speed** | -15% | Attaques plus lentes |
| **Cast Speed** | -15% | Sorts plus lents |
| **Application** | Multiplicateur | Affecte tout |
| **Type** | Percentage penalty | Réduction relative |

### Calcul du Ralentissement
```
Final_Movement = Base_Movement × 0.85
Final_Attack_Speed = Base_Attack × 0.85
Final_Cast_Speed = Base_Cast × 0.85
```

## Impact Systémique

### Effets sur le Gameplay
| Aspect | Réduction | Impact Ressenti |
|--------|-----------|-----------------|
| **Mobilité** | -15% | Kiting difficile |
| **DPS** | -15% | Damage réduit |
| **Casting** | -15% | Sorts plus lents |
| **Réactivité** | Global | Gameplay sluggish |
| **Qualité de vie** | Significatif | Frustration potentielle |

### Builds les Plus Affectés
- **Speed Builds** : Impact devastateur
- **Kiting Builds** : Mobilité compromise
- **Fast Attack** : DPS significativement réduit
- **Caster Builds** : Fluidité compromise
- **Hit-and-Run** : Tactiques compromises

## Inconvénients Stratégiques

**Désavantages :**
- Réduction globale de performance
- Qualité de vie dégradée
- Kiting rendu difficile
- DPS global réduit
- Vulnérabilité accrue
- Frustration du gameplay

**Impacts Critiques :**
- **Mobility Dependent Builds** : Quasi-impraticables
- **Speed Farmers** : Efficacité drastiquement réduite
- **Fast Combat** : Rythme cassé
- **Reactive Playstyles** : Réactivité compromise

## Stratégies de Compensation

### Contremesures Recommandées
- **Speed Bonuses** : Compenser avec autres corruptions
- **Positioning Builds** : Moins dependant de mobilité
- **Tank Builds** : Impact réduit sur statiques
- **DoT Builds** : Moins affecté par attack speed

### Adaptations de Build
```
Tank Adaptation: Focus défense, moins mobility dependent
DoT Build: Damage over time moins affecté
Positioning: Strategic placement over speed
```

## Synergies de Compensation

### Corruptions Compensatoires
- **Time Distortion** : Partiellement compensé (+10-20% vs -15%)
- **Lesharii's Grace** : Movement speed compensation
- **Battle Frenzy** : Attack speed compensation
- **Defensive Builds** : Moins dépendants de speed

### Builds Viables
- **Tank Builds** : Impact minimal
- **DoT Specialists** : Attack speed moins critique
- **Defensive Casters** : Positioning over speed
- **Strategic Builds** : Tactics over reflexes

## Calculs d'Impact

### Performance Reduction
- **15% slower** = 15% less efficiency globalement
- **DPS Impact** : Direct 15% reduction
- **Mobility Impact** : Kiting capability significantly reduced
- **Quality of Life** : Noticeable gameplay sluggishness

### Compensation Requirements
- Need **17.6% speed bonus** to neutralize (-15% → +17.6% = net 0%)
- Multiple speed corruptions required
- High investment to offset single malus

## Interaction avec d'Autres Systèmes

### Systèmes de Vitesse
- Affecte TOUS les systèmes de speed
- Multiplicatif avec autres speed bonuses/malus
- Global impact sur responsiveness
- Combat tous les aspects du timing

### Systèmes de Combat
- Réduit l'efficacité offensive globale
- Impact sur la survie (moins de mobility)
- Compromet les tactics speed-dependent
- Rend certains builds impraticables

## Gestion des Risques

### Évaluation de Viabilité
1. **High Priority Avoidance** : Speed-dependent builds
2. **Possible with Compensation** : Builds avec speed bonuses
3. **Manageable** : Tank et defensive builds
4. **Strategic Consideration** : Cost/benefit analysis

### Build Recommendations
- **Avoid** : Fast attack, kiting, speed farming
- **Consider** : Tank, DoT, defensive
- **Compensate** : Stack speed bonuses if taking

## Builds Déconseillés

### Builds Incompatibles
```
Speed Farmer: -15% speed = -15% farming efficiency
Kiter Build: Mobility critical for survival
Fast Attacker: DPS directly impacted
Mobile Caster: Casting + movement both affected
```

### Builds Viables
```
Tank Build: Speed less critical
DoT Build: Attack speed less important
Defensive Caster: Strategic positioning
Area Control: Less movement dependent
```

## Related

- [[Corruptions]] - Système principal
- [[Speed Systems]] - Systèmes de vitesse
- **Compensatory Synergies** : [[Time Distortion]], [[Lesharii's Grace]], [[Battle Frenzy]]
- [[Movement Speed]] - Vitesse de déplacement
- [[Attack Speed]] - Vitesse d'attaque
- [[Cast Speed]] - Vitesse de cast
- [[Malus]] - Catégorie
- [[Speed Reduction]] - Mécaniques de ralentissement

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Malus\slow_actions_malus.tres`