---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionStatReward
tags: [vampiric_essence, life_steal, sustain, healing, vampire]
status: implemented
rarity: varies
---

# Vampiric Essence

## Description
Une corruption de drain vital qui permet de récupérer des points de vie en infligeant des dégâts. Cette corruption transforme chaque attaque en un siphon d'énergie vitale, permettant au porteur de se sustenter du sang de ses ennemis.

## Lore
Dans les profondeurs de l'Éther Sombre résident des entités qui ont transcendé le besoin de nourriture conventionnelle, se sustentant directement de la force vitale d'autrui. Cette corruption octroie cette capacité parasitaire, transformant chaque coup porté en un conduit mystique qui draine l'essence vitale de la victime pour la transférer au porteur. Ce n'est pas seulement du vampirisme - c'est une symbiose forcée où la mort de l'ennemi nourrit littéralement la vie du prédateur.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Special Effects | Effet unique |
| **Classe de Base** | CorruptionStatReward | Bonus conditionnel |
| **Durée** | Permanente | Tant que la corruption est active |
| **Mechanism** | Life Steal | Drain de vie |
| **Rate** | {value}% | Variable selon tier |

## Mécaniques Vampiriques

### Système de Drain Vital
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Life Steal Rate** | {value}% | Variable selon tier |
| **Source** | All damage dealt | Tous types de dégâts |
| **Healing Type** | Instant | Récupération immédiate |
| **Application** | Per damage instance | Chaque hit |
| **Limit** | None | Pas de cap |

### Calcul du Drain de Vie
```
Life_Stolen = Damage_Dealt × (Vampiric_Rate/100)
Health_Healed = Min(Life_Stolen, Missing_Health)
Applies_To = All_Damage_Types
```

## Système de Tiers

### Valeurs par Tier (Estimées)
| Tier | Life Steal Rate | Sustain Power | Survival Impact |
|------|-----------------|---------------|----------------|
| **Minor** | 3-5% | Modéré | Bon |
| **Moderate** | 5-7% | Solide | Très bon |
| **Major** | 7-10% | Important | Excellent |
| **Epic** | 10-12% | Majeur | Puissant |
| **Legendary** | 12-15% | Exceptionnel | Vampirique |

### Code Couleur des Tiers
- **Blanc** : 3-5% life steal
- **Vert** : 5-7% life steal
- **Bleu** : 7-10% life steal
- **Violet** : 10-12% life steal
- **Or** : 12-15% life steal

## Avantages Stratégiques

**Forces :**
- Sustain passif automatique
- Scaling avec damage output
- Compatible avec tous damage types
- Améliore drastiquement la survie
- Plus efficace avec high DPS
- Permet des playstyles agressifs

**Synergies Exceptionnelles :**
- **High DPS Builds** : Plus de dégâts = plus de heal
- **Dark Power** : Damage bonus = healing bonus
- **Critical Builds** : Critical hits = big heals
- **Fast Attack** : Frequent healing ticks
- **AoE Builds** : Multiple enemies = multiple heals

## Applications Tactiques

### Builds Agressifs
- Permet un playstyle très agressif
- Self-sustain pendant le combat
- Moins dépendant des potions/regen

### Builds High-DPS
- Plus de dégâts = plus de healing
- Excellent pour burst builds
- Synergie avec damage bonuses

### Synergies Cross-Corruption
- **Avec Dark Power** : Plus de damage = plus de heal
- **Avec Critical Mass** : Critical heals significant
- **Avec Echo Chamber** : Double damage = double heal
- **Avec Blood Thirst** : Damage scaling = heal scaling

## Considérations de Balance

### Mécaniques d'Équilibrage
- Percentage-based (scale avec damage)
- Requires dealing damage (pas passif pur)
- Plus efficace avec high damage output
- Limited par missing health

### Impact sur la Progression
- Transformateur pour la survie
- Permet des builds glass cannon viable
- Reduces potion dependency
- Foundation pour aggressive playstyles

## Implémentation Technique

### Fichiers Source
- **Corruption** : `vampiric_essence_bonus.tres`
- **Script** : `corruption_stat_reward.gd`
- **Template** : Description avec value variable

### Intégration Système
```gdscript
# Type: CorruptionStatReward
# Triggered on damage dealt
description_template = "Gain {value}% life steal on all damage dealt"
lifesteal_percentage = tier_value
applies_to = ALL_DAMAGE_TYPES
```

### Variables de Template
- `{value}` : Pourcentage de life steal (ex: 8.0 pour 8%)

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : High DPS, aggressive builds, glass cannons
- **Medium Priority** : Builds balanced, sustained combat
- **Low Priority** : Pure tank builds (moins de damage)

### Moment Optimal
- **Early Game** : Excellent pour survie
- **Mid Game** : Transformateur pour aggressive play
- **Late Game** : Essential pour high-risk builds

## Risques et Contreparties

### Limitations
- Dépendant du damage output
- Moins efficace avec low DPS
- Ne fonctionne pas si pas d'ennemis
- Limited par missing health

### Gestion Optimale
- Focus sur high damage builds
- Combiner avec damage bonuses
- Utiliser pour aggressive engagement
- Balance avec other sustain sources

## Interaction avec d'Autres Systèmes

### Systèmes de Damage
- Scaling direct avec damage output
- Compatible avec tous damage types
- Multiplicatif avec damage bonuses
- Benefits from critical strikes

### Systèmes de Survie
- Forme active de healing
- Complement aux regen effects
- Permet reduced defensive investment
- Enables glass cannon viability

## Sustain Calculations

### Healing Examples
- **100 damage + 10% steal** = 10 HP healed
- **500 AoE damage + 8% steal** = 40 HP healed
- **Critical 1000 + 12% steal** = 120 HP healed

### Sustain Rates
- High DPS build: Significant healing per second
- AoE builds: Healing multiplicatif
- Critical builds: Burst healing spikes

## Builds Recommandés

### Vampire Lord
```
Core: Vampiric Essence + Dark Power + Critical Mass
Style: High damage with sustain
Focus: Aggressive self-sustaining DPS
```

### Life Leech Tank
```
Core: Vampiric Essence + Titan Vitality + Corrupted Endurance
Style: Tank with active healing
Focus: Multiple sustain sources
```

### Glass Cannon Vampire
```
Core: Vampiric Essence + Anti-Matter Orb + Echo Chamber
Style: High risk with sustain safety net
Focus: Maximum damage with heal backup
```

## Healing Efficiency

### Damage Type Compatibility
- **Physical** : Direct life steal
- **Magical** : Full compatibility
- **Elemental** : All elements work
- **DoT Effects** : Continuous healing
- **AoE Damage** : Multiple heal sources

### Combat Scenarios
- **Single Target** : Steady healing rate
- **Multiple Enemies** : Multiplicative healing
- **Boss Fights** : Sustained combat heal
- **AoE Clearing** : Burst healing spikes

## Related

- [[Corruptions]] - Système principal
- [[Life Steal]] - Mécanisme de drain de vie
- **Synergies** : [[Dark Power]], [[Critical Mass]], [[Echo Chamber]]
- [[Sustain Mechanics]] - Mécaniques de sustain
- [[Aggressive Builds]] - Builds agressifs
- [[Special Effects]] - Catégorie
- [[Vampiric Builds]] - Style vampirique

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\vampiric_essence_bonus.tres`