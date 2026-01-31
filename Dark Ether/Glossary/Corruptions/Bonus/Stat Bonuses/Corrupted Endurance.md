---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: CorruptionStatReward
tags: [corrupted_endurance, survivor, health, regeneration, tank]
status: implemented
rarity: varies
---

# Corrupted Endurance

## Description
Une corruption de survie qui augmente les points de vie maximum et la régénération de santé. Cette corruption transforme le porteur en un bastion de résistance, capable d'endurer les assauts les plus féroces.

## Lore
Les survivants de l'Éther Sombre développent une résistance surnaturelle aux forces corrosives de cette dimension. Cette corruption cristallise cette adaptation, renforçant le corps et l'esprit jusqu'à atteindre des niveaux de résistance qui défient la compréhension mortelle. Chaque blessure guérit plus vite, chaque coup reçu fait moins mal, comme si la mort elle-même reculait devant une telle détermination.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Stat Bonuses | Bonus de statistiques |
| **Classe de Base** | CorruptionStatReward | Bonus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Style** | Survivor | Spécialisation survie |
| **Focus** | Health & Regen | Système de vitalité |

## Mécaniques de Survie

### Système de Robustesse
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Health Bonus** | +100 points | Fixe pour tous tiers |
| **Health Regen** | +2-3%/sec | Variable selon tier |
| **Synergie** | HP + Recovery | Double protection |
| **Application** | Permanent | Toujours actif |
| **Stacking** | Avec autres bonus | Se cumule |

### Calcul de la Survie
```
Health_Total = Base_Health + 100
Regen_Final = (Health_Total × Regen_Percentage/100) par seconde
```

## Système de Tiers

### Valeurs par Tier
| Tier | Health Bonus | Health Regen | Survie Globale |
|------|--------------|--------------|----------------|
| **Minor** | +100 | +2.0%/sec | Bonne |
| **Moderate** | +100 | +2.3%/sec | Solide |
| **Major** | +100 | +2.5%/sec | Très bonne |
| **Epic** | +100 | +2.7%/sec | Excellente |
| **Legendary** | +100 | +3.0%/sec | Exceptionnelle |

### Code Couleur des Tiers
- **Blanc** : +100 HP, +2.0%/sec regen
- **Vert** : +100 HP, +2.3%/sec regen
- **Bleu** : +100 HP, +2.5%/sec regen
- **Violet** : +100 HP, +2.7%/sec regen
- **Or** : +100 HP, +3.0%/sec regen

## Avantages Stratégiques

**Forces :**
- Double bonus (pool + recovery)
- Excellent pour tous builds défensifs
- Health bonus substantiel early game
- Regen percentage scale avec total HP
- Améliore drastiquement la survie
- Synergie avec tous styles de jeu

**Synergies Exceptionnelles :**
- **Titan Vitality** : Stack HP pour pool massive
- **Titan's Regeneration** : Triple stack regen
- **Storm Caller** : Tank avec dégâts passifs
- **Vampiric Essence** : Recovery multiple
- **All Defensive Builds** : Core corruption

## Applications Tactiques

### Builds Tank Pur
- Core corruption pour tanks
- Permet le face-tanking de boss
- Améliore drastiquement la survie

### Builds Hybrides
- Excellent pour tous characters
- Améliore la sécurité générale
- Permet des plays plus agressifs

### Synergies Cross-Corruption
- **Avec Titan Vitality** : Pool HP massive
- **Avec Titan's Regeneration** : Regen extrême
- **Avec Storm Caller** : Tank avec dégâts AoE
- **Avec Vampiric Essence** : Multiple recovery sources

## Considérations de Balance

### Mécaniques d'Équilibrage
- Health fixe (non scaling avec tiers)
- Regen percentage (scale avec total HP)
- Plus efficace avec high total HP
- Encourage le gameplay défensif

### Impact sur la Progression
- Transformateur pour la survie
- Permet d'explorer des builds risqués
- Améliore significativement la qualité de vie
- Base solide pour tous builds

## Implémentation Technique

### Fichiers Source
- **Corruption** : `survivor_reward.tres`
- **Script** : `corruption_stat_reward.gd`
- **Stats** : Health max + regen rate

### Intégration Système
```gdscript
# Type: CorruptionStatReward
stat_modifiers = [
    StatType.HEALTH_MAX,
    StatType.HEALTH_REGEN
]
values = [100, tier_regen_percentage]
```

### Valeurs Techniques
- **Health Bonus** : Valeur plate (+100)
- **Health Regen** : Valeur en pourcentage (2.0-3.0)

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Tous builds, spécialement tanks
- **Medium Priority** : Glass cannons (balance survie)
- **Low Priority** : Aucun (toujours utile)

### Moment Optimal
- **Early Game** : Excellent investissement sécurité
- **Mid Game** : Permet des plays plus agressifs
- **Late Game** : Base pour builds défensifs avancés

## Risques et Contreparties

### Limitations
- Health bonus fixe (scaling relatif)
- Regen basé sur percentage (slow early)
- Plus défensif qu'offensif
- Pas d'amélioration directe de damage

### Gestion Optimale
- Acquérir tôt pour maximum de sécurité
- Combiner avec autres bonus HP
- Utiliser pour équilibrer builds glass cannon
- Stack avec autres sources de regen

## Interaction avec d'Autres Systèmes

### Système de Health
- Augmente le pool de vie disponible
- Améliore tous les defensive stats
- Synergie avec damage reduction
- Compatible avec healing effects

### Système de Regeneration
- Améliore le recovery passif
- Synergie avec active healing
- Compatible avec life leech
- Stack avec autres regen sources

## Builds Recommandés

### Tank Immortel
```
Core: Corrupted Endurance + Titan Vitality + Titan's Regeneration
Style: Pure defensive
Focus: Maximum survivability
```

### Balanced Survivor
```
Core: Corrupted Endurance + Storm Caller + Critical Mass
Style: Defensive with damage
Focus: Safe aggressive play
```

### Glass Cannon Balancé
```
Core: Corrupted Endurance + Anti-Matter Orb + Dark Power
Style: High risk balanced
Focus: Damage with safety net
```

## Related

- [[Corruptions]] - Système principal
- [[Health System]] - Gestion de la vie
- **Synergies** : [[Titan Vitality]], [[Titan's Regeneration]], [[Dark Ether/Glossary/Skills and Perks/Elemental/Storm Caller]]
- [[Regeneration]] - Mécanisme de recovery
- [[Tank Builds]] - Style de jeu
- [[Stat Bonuses]] - Catégorie
- [[Defensive Stats]] - Statistiques défensives

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\survivor_reward.tres`