---
type: corruption
category: Bonus
subcategory: Stat Bonuses
reward_type: StatModifierReward
tags: [berserker, damage, attack_speed, combat_style, global]
status: implemented
rarity: fixed_values
---

# Corrupted Rage

## Description
A berserker combat style corruption that increases global damage and attack speed. This corruption transforms the bearer into a furious war machine, sacrificing finesse for brute force and pure aggression.

## Lore
Corrupted Rage was born from the bloodiest battlefields of the Dark Ether, where the most desperate warriors let their humanity evaporate in fury. This corruption feeds the primitive anger that slumbers in every fighter, transforming it into a devastating force that knows neither mercy nor restraint.

## Statistics

| Property | Value | Notes |
|-----------|--------|-------|
| **Type** | Bonus Corruption | Positive effect |
| **Category** | Combat Style | Berserker style |
| **Base Class** | StatModifierReward | Stat modifier |
| **Weight** | 1.0 | Standard probability |
| **Randomization** | No | Fixed values |

## Stat Bonuses

### Global Damage
| Property | Value | Type | Notes |
|----------|--------|------|-------|
| **Stat** | GLOBAL_DAMAGE | Multiplier | Affects all damage |
| **Min Value** | 20.0% | Percentage | Fixed value |
| **Max Value** | 25.0% | Percentage | Fixed value |
| **Display Name** | "Global Damage" | String | User interface |
| **Tier Color** | Red (1, 0.2, 0.2, 1) | Color | Berserker theme |

### Attack Speed
| Property | Value | Type | Notes |
|----------|--------|------|-------|
| **Stat** | ATTACK_SPEED | Multiplier | Affects all attacks |
| **Min Value** | 15.0% | Percentage | Fixed value |
| **Max Value** | 20.0% | Percentage | Fixed value |
| **Display Name** | "Attack Speed" | String | User interface |
| **Tier Color** | Red (1, 0.2, 0.2, 1) | Color | Visual consistency |

## Berserker Philosophy

### Style de Combat
La Corrupted Rage incarne l'archétype du berserker - un combattant qui abandonne la défense et la prudence pour maximiser l'aggressivité et les dégâts. Ce style favorise :

- **Attaque constante** : Plus d'attaques par seconde
- **Dégâts maximisés** : Bonus global à tous les types de dégâts
- **Agressivité** : Encouragement du combat au corps-à-corps
- **Simplicité** : Pas de mécaniques complexes, juste plus de puissance

### Synergies Thématiques
- **Builds de mêlée** : Parfait pour les combattants au contact
- **Builds d'attaque** : Excellent avec Blood Blade et armes physiques
- **Styles agressifs** : Récompense le jeu offensif
- **Combats prolongés** : Efficace dans les longues batailles

## Avantages Stratégiques

**Forces :**
- Bonus immédiat et visible sur les dégâts
- Augmentation de la cadence d'attaque
- Synergie parfaite avec les builds physiques
- Pas de conditions d'activation complexes
- Excellent pour le farming rapide

**Applications Optimales :**
- **Blood Blade builds** : Plus de lames, plus souvent
- **Melee fighters** : Dégâts et vitesse accrus
- **Hybrid attackers** : Bonus global affecte sorts et attaques
- **Rushers** : Parfait pour tuer rapidement

## Interactions avec les Stats

### Multiplication des Effets
- **Global Damage** : Se multiplie avec tous les autres bonus de dégâts
- **Attack Speed** : Se combine avec autres bonus de vitesse
- **Effet Cumulatif** : Les deux stats se renforcent mutuellement

### Calculs de Dégâts
```
Dégâts Finaux = Dégâts Base × (1 + Global Damage Bonuses)
Attaques/Seconde = Base Attack Rate × (1 + Attack Speed Bonuses)
DPS Effectif = Dégâts Finaux × Attaques/Seconde
```

## Synergies Cross-Corruption

### Combos Puissants
- **+ Dark Power** : Multiplicateurs de dégâts globaux stackent
- **+ Critical Mass** : Plus d'attaques = plus de chances de critique
- **+ Echo Chamber** : Plus d'attaques doublées
- **+ Battle Frenzy** : Stacks d'attaque speed s'accumulent plus vite

### Builds Recommandés
- **Pure Berserker** : Toutes les corruptions d'attaque/dégâts
- **Crit Berserker** : Combiné avec corruptions de critique
- **Blood Berserker** : Focus sur Blood Blade avec attack speed

## Considérations de Balance

### Valeurs Équilibrées
- **20-25% Global Damage** : Significatif sans être overpowered
- **15-20% Attack Speed** : Amélioration notable de la cadence
- **Couleur Rouge** : Indique clairement le style agressif
- **Pas de Malus** : Bonus pur, pas de contrepartie

### Impact sur la Progression
- Accélère la vitesse de farm
- Rend les combats plus dynamiques
- Encourage le jeu agressif
- Synergie naturelle avec gameplay action

## Comparaisons Style de Combat

### vs Assassin (Silent Blade)
- **Berserker** : Force brute, dégâts constants
- **Assassin** : Finesse, burst damage, critiques

### vs Scholar (Forbidden Knowledge)
- **Berserker** : Combat physique, attaques
- **Scholar** : Magie, sorts, cast speed

### vs Survivor (Corrupted Endurance)
- **Berserker** : Offense pure
- **Survivor** : Défense et sustain

## Implémentation Technique

### Fichiers Source
- **Corruption** : `berserker_reward.tres`
- **Script** : `corruption_stat_modifier_reward.gd`
- **Config** : `stat_modifier_configuration.gd`

### Structure de Données
```gdscript
# Type: StatModifierReward
stat_modifier_configs = [
    StatModifierConfiguration_damage,  # Global Damage 20-25%
    StatModifierConfiguration_attack_speed  # Attack Speed 15-20%
]
reward_name = "Corrupted Rage"
reward_type = 0  # Bonus
description_template = "{globaldamage_percentage}{globaldamage_type_suffix} Global Damage and {attackspeed_percentage}{attackspeed_type_suffix} Attack Speed"
```

### Template de Description
```
"{globaldamage_percentage}{globaldamage_type_suffix} Global Damage and {attackspeed_percentage}{attackspeed_type_suffix} Attack Speed"
```

## Stratégies d'Acquisition

### Priorité par Build
- **High Priority** : Builds d'attaque physique, mêlée
- **Medium Priority** : Builds hybrides attaque/sort
- **Low Priority** : Builds de sorts purs, supports

### Moment Optimal
- **Early Game** : Excellent boost de progression
- **Mid Game** : Foundational pour builds berserker
- **Late Game** : Se combine avec autres corruptions

## Tips et Stratégies

### Maximisation d'Efficacité
- Combiner avec armes à attack speed élevé
- Privilégier les skills d'attaque sur les sorts
- Rechercher d'autres bonus de dégâts globaux
- Éviter les builds défensifs passifs

### Gestion des Ressources
- Plus d'attaques = plus de consommation mana (si applicable)
- Nécessite sustain pour maintenir l'agression
- Synergise bien avec life leech

## Related

- [[Corruptions]] - Système principal
- [[Combat Styles]] - Catégorie de corruptions
- [[Berserker]] - Archétype de combat
- [[Global Damage]] - Mécanisme de stat
- [[Attack Speed]] - Mécanisme de stat
- [[Stat Modifiers]] - Système technique

---

**Implémentation** : `D:\Godot\PoE Survivor\scripts\Effect_BuffandDebuff\Corruption\Rewards\Bonus\Stat_Bonuses\Combat_Styles\berserker_reward.tres`