# Progression System Rework - Summary

Document récapitulatif de toutes les mécaniques refactorisées lors de la refonte du système de progression.

---

## Philosophie de Design

### Problème résolu

| Frustration | Solution Dark Ether |
|-------------|---------------------|
| **PoE:** Bloqué dans un build, pas d'expérimentation | Jouer 6 classes simultanément, switch en temps réel |
| **Roguelite:** Le RNG dicte ton build chaque run | Ton build est permanent ; seules les adaptations tactiques sont per-run |

### Mantra

> **"Your build identity is permanent. Your tactical adaptation is per-run."**

---

## Structure de Progression

### Permanent (Ton Identité)

| Élément | Description | Notes |
|---------|-------------|-------|
| **Stuff** | Équipement (armes, armures, accessoires) | Jamais perdu |
| **[[Support Runes]]** | Runes gravées dans la chair qui modifient les skills | Par skill, système de tiers I-V |
| **Stat-ups** | Arbre passif personnel | Débloqué via méta-progression |
| **[[Perks]]** | Modifications majeures de skills | Build-defining, équipables avant run |

### Temporaire (Adaptation Per-Run)

| Élément | Description | Notes |
|---------|-------------|-------|
| **[[Anomalies]]** | Modificateurs de Floor (distorsions temporelles) | Challengent ton build |
| **[[Mutations]]** | Adaptations ADN achetées au Merchant | 6 slots max, tactiques |
| **Blessings** | Buffs purs (Trial Rooms) | Scalent selon performance |
| **Corruptions** | Bonus + Malus (Corrupted Rooms) | Risk/reward |

---

## Changements de Terminologie

| Ancien Terme | Nouveau Terme | Raison |
|--------------|---------------|--------|
| Floor Mutations | **Anomalies** | Les "mutations" sont maintenant réservées au joueur ; les floors ont des "anomalies temporelles" |
| Augments | **Mutations** | Cohérence narrative : Vorathros est un shapeshifter qui manipule son ADN |
| Skill Supports | **Support Runes** | Runes gravées dans la chair de Vorathros |

---

## Support Runes (Nouveau Système)

### Concept
Runes gravées dans la chair de Vorathros. Grâce à ses pouvoirs de shapeshifter, il peut régénérer sa peau pour changer les inscriptions.

### Propriétés

| Propriété | Détail |
|-----------|--------|
| **Unlock** | Permanent (jamais perdu) |
| **Equip** | Par skill, modifiable entre runs |
| **Active** | Toutes les runes équipées sont actives |
| **Tiers** | 5 niveaux (I → V) |
| **Fusion** | 3 runes même type/tier → 1 rune tier supérieur |

### Compatibilité Skill Tags

Les Support Runes ont des **tag requirements** :
- Chaque skill a des tags (`Attack`, `Blood`, `Bleed`, `Projectile`, etc.)
- Chaque rune requiert certains tags pour être équipée
- Certaines runes sont universelles (aucun tag requis)

### Reclassification

Certains anciens Perks sont devenus des Support Runes :
- Multiple Projectiles Support (ex: Amount Perks)
- Vitality Support (ex: Health Scaling)
- Vicious Ailments Support (ex: Increased Bleed Damage)
- Long Reach Support (ex: Increased Range)
- Efficiency Support (ex: Reduce Cost)
- Elemental Conversion Support (ex: Change Damage Type)

---

## Perks (Clarifié)

### Propriétés

| Propriété | Détail |
|-----------|--------|
| **Unlock** | Permanent (une fois débloqué, jamais perdu) |
| **Equip** | Modifiable (peut changer entre runs) |
| **Impact** | Majeur, build-defining |

### Distinction Perks vs Support Runes

| Aspect | Perks | Support Runes |
|--------|-------|---------------|
| **Effet** | CHANGE le fonctionnement du skill | AJOUTE un effet au skill |
| **Exemple** | "Bloodblades chain to enemies" | "Bloodblades inflict Poison" |
| **Poids** | Lourd, définit le build | Léger, amélioration incrémentale |

---

## Structure de Run (Corrigée)

### Hiérarchie

```
RUN
└── 4 DUNGEONS
    └── Multiple FLOORS par dungeon
        └── Multiple ROOMS par floor
```

### Détails

| Niveau | Contenu | Boss |
|--------|---------|------|
| **Dungeon** | Thème unique, pool d'ennemis | Major Boss → Key Fragment |
| **Floor** | Anomaly révélée, rooms variées | Mini-Boss |
| **Room** | Encounter unique | Rewards selon type |

### 4 Key Fragments

Chaque Major Boss drop un Key Fragment. Les 4 fragments débloquent le Final Boss (The Supreme Void).

---

## Système de Rooms (Refactorisé)

### Types de Rooms

| Room | Description | Reward |
|------|-------------|--------|
| **Normal Room** | Combat standard | Gold, ressources, consumables |
| **Trial Room** | Objectif gradé | Blessings (selon performance) |
| **Corrupted Room** | Choix avant combat | Corruptions (bonus + malus) |
| **Boss Room** | Mini/Major boss | Meta-loot, progression |
| **Merchant Room** | Shop | Mutations, consumables, healing |
| **Chamber of Lost Time** | Rare, mécanique unique | Reward spéciale aléatoire |

### Purity/Corruption Balance

Système inspiré de Binding of Isaac :

```
[PURITY] ◄━━━━━━━━━━●━━━━━━━━━► [CORRUPTION]
  100%           50/50           100%
```

| État | Pool de Rewards |
|------|-----------------|
| **Neutral (0-99%)** | Standard Blessings / Standard Corruptions |
| **Locked Purity (100%)** | + Sacred Blessings (exclusifs) |
| **Locked Corruption (100%)** | + Abyssal Corruptions (exclusifs) |

---

## Mutations (Nouveau Système)

### Concept Narratif
Vorathros manipule son propre ADN pour s'adapter aux anomalies de la timeline courante.

### Propriétés

| Propriété | Détail |
|-----------|--------|
| **Slots** | 6 maximum (miroir des 6 classes) |
| **Durée** | Per-run uniquement |
| **Acquisition** | Achat au Merchant Room |
| **Poids** | Tactique, pas build-defining |

### Catégories

- **Conversion** : Changement de type de dégâts
- **Resistance** : Protection contre éléments
- **Penetration** : Ignore les résistances
- **Status** : Application de status effects
- **Combat** : Bonus offensifs
- **Survival** : Bonus défensifs

---

## Anomalies (Nouveau Système)

### Concept Narratif
Chaque run est une timeline différente. Les Anomalies représentent les distorsions uniques de cette timeline.

### Propriétés

| Propriété | Détail |
|-----------|--------|
| **Scope** | Par floor |
| **Reveal** | Au début de chaque floor |
| **Design Rule** | Challenge le build sans le hard-counter |

### Catégories

- **Resistance** : Ennemis résistants à certains types
- **Damage** : Modificateurs de dégâts
- **Healing** : Altération des mécaniques de soin
- **Environmental** : Effets de zone

---

## Éléments Supprimés

| Élément | Raison |
|---------|--------|
| **The Nexus of Destinies** | Redondant avec Global Level, Perks, et Purity/Corruption |
| **Temporary Boosts between runs** | Contradictoire avec la philosophie "permanent build identity" |

---

## Skill Tags (Documenté)

Système de tags pour la compatibilité des Support Runes :

### Catégories de Tags

| Catégorie | Tags |
|-----------|------|
| **Damage Type** | Physical, Fire, Cold, Lightning, Poison, Ether |
| **Damage Source** | Attack, Spell, Over Time |
| **Delivery** | Projectile, Melee, AoE, Chaining |
| **Mechanic** | Minion, Aura, Curse, Buff, Duration, Channeling |
| **Weapon** | Bow, One-Handed, Two-Handed |
| **Class-Specific** | Blood, etc. |

---

## Notes Créées/Mises à Jour

### Créées
- [[Anomalies]]
- [[Mutations]]
- [[Perks]]
- [[Support Runes]]
- [[Skill Tags]]
- [[Chamber of Lost Time]]

### Mises à Jour
- [[GDD]] (refonte complète section 4-5)
- [[Rooms]] (overview)
- [[Normal Room]]
- [[Trial Room]]
- [[Corrupted Room]]
- [[Boss Room]]
- [[Merchant Room]]
- [[Dungeons]]
- [[Floors]]
- [[Blood Blade]] (reclassification perks → support runes)

### Supprimées
- The Nexus of Destinies

---

## Related

- [[GDD]]
- [[Progression System Rework - Tracker]]
