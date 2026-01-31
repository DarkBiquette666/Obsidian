---
type: corruption
category: Bonus
subcategory: Special Effects
reward_type: CorruptionEffectReward
tags: [frenzy, attack_speed, stacking, combat, momentum]
status: implemented
rarity: tier_based
---

# Battle Frenzy

## Description
A corruption that progressively increases attack speed with each successful hit, creating a growing momentum effect that transforms prolonged fights into frenzied storms of violence. The longer the combat lasts, the faster and more dangerous the bearer becomes.

## Lore
Battle Frenzy draws from the primitive adrenaline that sleeps within every warrior. This corruption amplifies and corrupts this natural combat response, creating an addictive spiral of violence where each blow feeds an ever-growing thirst for destruction. The bearer gradually becomes an uncontrollable war machine.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Effet positif |
| **Catégorie** | Special Effects | Effet de stacking |
| **Classe de Base** | CorruptionEffectReward | Effet temporaire |
| **Déclencheur** | Successful Hit | Toute attaque réussie |
| **Durée** | Permanente (-1.0) | Tant que corruption active |
| **Intensité** | 1.0 | Effet standard |

## Mécaniques de Frénésie

### Système de Stacking
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Trigger** | Chaque hit réussi | Attaques et sorts |
| **Gain par Hit** | Variable par tier | Augmentation attack speed |
| **Stack Maximum** | Limité ou illimité | Dépend de l'implémentation |
| **Decay** | Probablement temporel | Perte graduelle sans hits |
| **Reset** | Sur mort ou timeout | Retour à zéro |

### Progression des Stacks
```
Stack 1: Base + {value}% Attack Speed
Stack 2: Base + 2×{value}% Attack Speed  
Stack N: Base + N×{value}% Attack Speed
```

## Avantages du Momentum

### Combat Flow
**Early Combat :**
- Vitesse normale au début
- Premier hit active la frénésie
- Progression graduelle mais visible

**Extended Combat :**
- Vitesse augmente exponentiellement avec durée
- Devient machine de guerre en late fight
- Maintient pressure sur ennemis

**Burst Potential :**
- Parfait pour éliminer groupes d'ennemis
- Chaque kill accelere vers le suivant
- Snowball effect dans dense crowds

### Types d'Interactions

| Type d'Attaque | Compatibilité | Notes |
|----------------|---------------|-------|
| **Attaques de Mêlée** | Excellente | Hits fréquents |
| **Projectiles** | Très bonne | Multiple hits possibles |
| **DoT Effects** | Limitée | Dépend si DoT ticks comptent |
| **Spells** | Bonne | Si considérés comme hits |
| **Multi-hit Skills** | Exceptionnelle | Stack très rapidement |

## Synergies Strategiques

### Skills Optimaux
**Multi-Hit Skills :**
- **Blood Blade** : Plusieurs lames = stacks rapides
- **Ether Ball** : Hits multiples sur explosion
- **Storm Caller** : Lightning hits fréquents
- **Thorn Spike** : Multiple ennemis touchés

**High Frequency Skills :**
- Toute attaque rapide bénéficie double
- Skills avec low cooldown
- Auto-attacking abilities

### Cross-Corruption Synergies
**Combos Puissants :**
- **+ Corrupted Rage** : Base attack speed + stacking speed
- **+ Echo Chamber** : Double hits = double stacks
- **+ Dark Power** : Plus de dégâts sur attaques rapides
- **+ Critical Mass** : Plus d'attaques = plus de crits

## Stratégies de Build

### Frenzy Specialists
**Build Focus :**
- Skills avec high hit frequency
- Survivability pour longs combats
- Resource sustain pour maintenir attaques
- Positioning pour éviter interruptions

**Recommended Classes :**
- **Torin** : Blood Blade synergy parfaite
- **Combat-focused** : Toute classe axée attaque

### Hybrid Applications
**Secondary Benefit :**
- Même builds non-attack bénéficient
- Améliore clearing speed
- Ajoute dimension temporelle au combat

## Gestion du Momentum

### Stack Maintenance
**Strategies :**
- Maintenir combat actif
- Éviter les pauses entre fights
- Prioriser continuous engagement
- Target switching pour maintenir hits

**Stack Loss Prevention :**
- Comprendre decay timer
- Quick repositioning entre targets
- Emergency targets (environment?)
- Backup plan si stacks lost

### Optimal Fight Flow
1. **Initiation** : Premier hit pour start stacks
2. **Buildup** : Focus sur hit frequency
3. **Peak** : Maximum stacks atteints
4. **Maintenance** : Garder stacks actifs
5. **Transition** : Vers prochain combat

## Considérations Tactiques

### Avantages Situationnels
**Boss Fights :**
- Long combat = maximum benefit
- Sustained DPS excellente
- Peut compenser phases difficiles

**Mob Clearing :**
- Snowball through groups
- Plus rapide = plus efficace
- Chain kills avec momentum

**Elite Encounters :**
- Build-up pendant approach
- Peak performance sur target prioritaire

### Limitations
**Short Fights :**
- Peu de benefit sur quick kills
- Wasted potential si overkill rapide

**Interrupted Combat :**
- Stacks lost si forced disengagement
- Repositioning peut reset progress

## Balance Considerations

### Power Scaling
**Early Stacks :** Impact modéré mais notable
**High Stacks :** Peut devenir très puissant
**Maximum Stacks :** Nécessite cap pour éviter OP

### Counterplay
**Enemy Design :**
- Ennemis avec forced disengagement
- Phases qui break momentum
- Mobility challenges

**Resource Management :**
- Plus d'attaques = plus de mana used
- Sustain devient crucial
- Risk/reward pour maintaining frenzy

## Technical Implementation

### Fichiers Source
- **Corruption** : `battle_frenzy_bonus.tres`
- **Effect** : `battle_frenzy_buff.tres`
- **Path** : `Bonus\Special_Effects\`

### Effect Structure
```gdscript
# Type: CorruptionEffectReward
effects_to_apply = [battle_frenzy_buff.tres]
effect_durations = [-1.0]  # Permanent
effect_intensities = [1.0]  # Standard
description_template = "Attack Speed is increased by {value}% on each successful hit"
```

### Template de Description
```
"Attack Speed is increased by {value}% on each successful hit"
```

## Optimization Strategies

### Stack Efficiency
**Maximizing Gains :**
- Builds avec natural high hit rate
- Equipment/perks pour attack speed synergy
- Multi-target capabilities
- Sustain pour long engagements

### Risk Management
**Stack Protection :**
- Defensive options pour survive long fights
- Escape routes si overwhelmed
- Resource management planning
- Backup strategies si frenzy lost

## Psychological Impact

### Player Behavior
**Encourages :**
- Aggressive playstyle
- Sustained combat engagement
- Risk-taking pour maintain stacks
- Moment-to-moment tactical thinking

**Flow State :**
- Créé addiction au momentum
- Satisfying feedback loop
- "Just one more fight" mentality

## Related

- [[Corruptions]] - Système principal
- [[Attack Speed]] - Mécanisme de stat
- [[Stacking Effects]] - Mécaniques d'accumulation
- [[Combat Flow]] - Dynamiques de combat
- [[Momentum Builds]] - Stratégies basées timing
- [[Hit Detection]] - Système de hit

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Special_Effects\battle_frenzy_bonus.tres`