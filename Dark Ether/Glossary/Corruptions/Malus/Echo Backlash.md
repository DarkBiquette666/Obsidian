---
type: corruption
category: Malus
subcategory: Dangerous
reward_type: CorruptionStatReward
tags: [echo_backlash, reflected_damage, dangerous, risk, backlash]
status: implemented
rarity: varies
---

# Echo Backlash

## Description
Une corruption dangereuse qui reflète une partie des dégâts infligés vers le porteur. Cette corruption crée un écho douloureux de chaque attaque, transformant chaque victoire en un sacrifice sanglant.

## Lore
L'Éther Sombre se souvient de chaque violence commise en son sein. Cette corruption malveillante tisse un lien mystique entre le porteur et ses victimes, créant un écho de souffrance qui rebondit sur l'agresseur. Chaque coup porté résonne dans l'âme du combattant, chaque blessure infligée trouve son reflet dans sa propre chair. C'est le prix que l'Éther exige pour les actes de violence - une leçon douloureuse que la destruction engendre toujours plus de destruction.

## Statistiques

| Propriété | Valeur | Notes |
|-----------|--------|-------|
| **Type** | Malus Corruption | Effet négatif |
| **Catégorie** | Dangerous | Corruption dangereuse |
| **Classe de Base** | CorruptionStatReward | Malus de stats |
| **Durée** | Permanente | Tant que la corruption est active |
| **Risque** | Élevé | Auto-dégâts constants |
| **Impact** | Direct | Affecte tous les dégâts |

## Mécaniques de Réflexion

### Système de Dégâts Réfléchis
| Propriété | Détails | Notes |
|----------|---------|-------|
| **Damage Reflected** | 15% fixe | Tous types de dégâts |
| **Source** | Tous dégâts infligés | Universal application |
| **Type** | True damage | Ignore resistances |
| **Timing** | Simultané | Avec dégâts infligés |
| **Mitigation** | Défenses du porteur | Peut être réduit |

### Calcul de la Réflexion
```
Reflected_Damage = Damage_Dealt × 0.15
Self_Damage = Reflected_Damage × (1 - Defensive_Modifiers)
```

## Système de Danger

### Impact par Type de Build
| Build Type | Danger Level | Impact sur Survie |
|------------|--------------|-------------------|
| **High DPS** | Critique | Très dangereux |
| **AoE Builds** | Élevé | Dégâts multiplicatifs |
| **DoT Builds** | Modéré | Dégâts constants |
| **Tank Builds** | Faible | Dégâts gérables |
| **Burst Builds** | Variable | Spikes dangereux |

### Risques par Situation
- **Boss Fights** : Moins dangereux (single target)
- **Mob Clearing** : Très dangereux (multiple hits)
- **AoE Attacks** : Extrêmement dangereux
- **High Damage** : Proportionnellement risqué

## Inconvénients Stratégiques

**Dangers :**
- Auto-dégâts constants
- Plus dangereux avec high DPS
- Limite l'agressivité possible
- Risque de suicide accidentel
- Problématique pour AoE builds
- Scaling négatif avec puissance

**Builds à Éviter :**
- **High DPS Builds** : Reflection trop élevée
- **AoE Specialists** : Dégâts multiplicatifs dangereux
- **Glass Cannons** : Manque de défenses
- **Burst Damage** : Spikes auto-létaux
- **Multi-hit Attacks** : Accumulation dangereuse

## Stratégies de Mitigation

### Défenses Recommandées
- **High Health Pool** : Absorber les réflexions
- **Damage Reduction** : Réduire reflected damage
- **Health Regeneration** : Compenser les pertes
- **Life Leech** : Recovery active
- **Armor/Resistances** : Mitigation passive

### Adaptations de Build
- **Builds Défensifs** : Plus sûrs avec cette corruption
- **Sustain Focus** : Récupération constante
- **Moderated DPS** : Éviter les pics extrêmes
- **Tank Playstyle** : Damage control prioritaire

## Gestion des Risques

### Techniques de Survie
- Monitoring constant de la santé
- Éviter les engagements prolongés
- Prioriser la défense sur l'offense
- Utiliser cover et positioning

### Builds Compatibles
```
Safe Build: High HP + Regeneration + Moderate DPS
Risky Build: High DPS + Glass Cannon (éviter)
Balanced: Defense + Sustain + Controlled Offense
```

## Interaction avec d'Autres Systèmes

### Systèmes de Dégâts
- Reflète TOUS les types de dégâts
- Includes physical, magical, elemental
- Affects multi-hit abilities proportionally
- Scales with total damage output

### Systèmes Défensifs
- Reflected damage peut être mitigé
- Armor et resistances s'appliquent
- Damage reduction effects fonctionnent
- Health bonuses améliorent la survie

## Synergies Dangereuses

### Corruptions à Éviter
- **Dark Power** : Plus de dégâts = plus de reflection
- **Blood Thirst** : Scaling DPS dangereux
- **Critical Mass** : Burst critiques létaux
- **Echo Chamber** : Double damage = double reflection

### Corruptions Bénéfiques
- **Titan Vitality** : Plus de HP pour absorber
- **Titan's Regeneration** : Recovery pour compenser
- **Corrupted Endurance** : Défenses améliorées
- **Defensive Effects** : Mitigation générale

## Calculs de Danger

### Exemples de Reflection
- **100 damage dealt** → 15 self-damage
- **1000 damage AoE** → 150 self-damage
- **10 enemies hit for 100** → 150 total reflection

### Seuils Critiques
- **High DPS builds** : Reflection > Regeneration = Danger
- **Glass cannons** : Reflection > Health pool = Létal
- **AoE builds** : Multiple reflections = Multiplicatif

## Contremesures Recommandées

### Build Adaptation
1. **Priorité Défense** : HP, armor, regeneration
2. **Moderated Offense** : Damage control
3. **Sustain Focus** : Continuous recovery
4. **Safe Positioning** : Avoid overextension

### Gear Requirements
- **High Health** : Essential pour survival
- **Regeneration** : Constant recovery
- **Resistances** : Mitigation tools
- **Defensive Abilities** : Protection effects

## Related

- [[Corruptions]] - Système principal
- [[Reflected Damage]] - Mécanisme de réflexion
- **Dangerous Synergies** : [[Dark Power]], [[Blood Thirst]], [[Critical Mass]]
- **Safe Synergies** : [[Titan Vitality]], [[Corrupted Endurance]]
- [[Risk Management]] - Gestion des risques
- [[Malus]] - Catégorie
- [[Dangerous Corruptions]] - Corruptions risquées

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Malus\echo_backlash_malus.tres`