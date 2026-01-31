# Progression System Rework - Tracker

Ce document sert de suivi pour la refonte du système de progression de Dark Ether. Il contient le contexte, les décisions prises, et les tâches à accomplir.

---

## Contexte de la Refonte

### Problème Initial
Dark Ether cherche à combiner la profondeur de build de **Path of Exile** avec le gameplay roguelite de **Hades/Ravenswatch**, tout en évitant deux frustrations communes :

1. **Frustration PoE** : Être bloqué sur un seul build, ne pas pouvoir expérimenter
2. **Frustration Roguelite** : Être à la merci du RNG, espérer avoir les mêmes upgrades à chaque run

### Solution Adoptée
**"Ton identité de build est permanente. Ton adaptation tactique est par run."**

La variance roguelite ne vient plus de **ce que tu es** (ton build), mais de **ce que tu affrontes** (les anomalies) et **comment tu t'adaptes** (les mutations).

---

## Terminologie Narrative

| Terme | Signification | Justification Narrative |
|-------|---------------|------------------------|
| **Anomalies** | Modificateurs de floor | Chaque run est une timeline différente, les anomalies sont les distorsions temporelles de cette timeline |
| **Mutations** | Adaptations tactiques per-run | Vorathros est un shapeshifter qui manipule son propre ADN pour s'adapter |

---

## Architecture du Nouveau Système

### Progression Permanente (Méta)

| Élément | Description | Statut |
|---------|-------------|--------|
| **Stuff** | Équipement (armes, armures, accessoires) | Existant |
| **Skill Supports** | Runes qui modifient les skills (comme support gems PoE) | Existant |
| **Stat-ups** | Passive tree personnel | Existant |
| **Perks** | Modifications majeures et permanentes des skills | À METTRE À JOUR |

### Progression Temporaire (Per-Run)

| Élément | Description | Statut |
|---------|-------------|--------|
| **Anomalies** | Distorsions temporelles par floor qui challengent le build | À CRÉER |
| **Mutations** | Adaptations ADN achetées au Merchant | À CRÉER |
| **Blessings** | Buffs purs (Trial Rooms) | À CRÉER |
| **Corruptions** | Bonus + Malus (Corrupted Rooms) | EXISTANT - À METTRE À JOUR |

---

## Système de Rooms

### Types de Rooms

| Room | Reward | Statut Doc |
|------|--------|------------|
| **Normal Room** | Ressources, consommables, minor stat-ups | OK |
| **Trial Room** | Blessings (gradués selon performance) | OK |
| **Corrupted Room** | Corruptions (choisir avant, survivre pour garder) | OK |
| **Boss Room** | Meta-loot, progression story | OK |
| **Merchant Room** | Mutations, consommables, heal | OK |
| **Chamber of Lost Time** | Mécaniques uniques aléatoires | OK |

### Système de Balance Purity/Corruption

- Jauge 50/50 au départ
- Trial Room → shift vers Purity
- Corrupted Room → shift vers Corruption
- Lock à 100% = point de non-retour
- Lock débloque pool exclusive (Sacred Blessings / Abyssal Corruptions)

---

## Tâches à Accomplir

### 1. Perks des Skills Existants
**Objectif** : Revoir tous les perks pour qu'ils soient des modifications majeures et permanentes (pas des buffs temporaires).

**Fichiers concernés** :
- `Glossary/Skills and Perks/Blood/` (Blood Blade, Vital Link, Blood Barrier, etc.)
- `Glossary/Skills and Perks/Voidborn/` (Void Spitters, Parasitic Swarm, etc.)
- `Glossary/Skills and Perks/Curses/`
- `Glossary/Skills and Perks/Elemental/`
- `Glossary/Skills and Perks/Ether/`
- `Glossary/Skills and Perks/Ground/`

**Index des skills** : `Glossary/Skills and Perks/Skills Index.md`

**Statut** : [ ] Non commencé

---

### 2. Liste des Blessings
**Objectif** : Créer la liste complète des Blessings pour les Trial Rooms.

**Tiers à créer** :
- [ ] Minor Blessings (failed objective)
- [ ] Standard Blessings (partial success)
- [ ] Major Blessings (full success)
- [ ] Sacred Blessings (Locked Purity only)

**Thématique** : Lumière, ordre, pureté. Buffs purs sans contrepartie.

**Fichier à créer** : `Glossary/Blessings/` (nouveau dossier)

**Statut** : [ ] Non commencé

---

### 3. Mise à Jour des Corruptions
**Objectif** : Revoir les corruptions existantes et ajouter le tier Abyssal.

**Fichiers existants** :
- `Glossary/Corruptions/Bonus/Special Effects/` (8 fichiers)
- `Glossary/Corruptions/Bonus/Stat Bonuses/` (14 fichiers)
- `Glossary/Corruptions/Malus/` (4 fichiers)
- `Glossary/Corruptions/Corruptions Index.md`
- `Glossary/Corruptions/Corruption List.base`

**Tiers** :
- [ ] Standard Corruptions (existantes - à revoir)
- [ ] Abyssal Corruptions (à créer - Locked Corruption only)

**Thématique** : Ténèbres, chaos, corruption. Bonus puissants avec contreparties.

**Statut** : [ ] Non commencé

---

### 4. Liste des Mutations
**Objectif** : Créer la liste des Mutations (adaptations ADN) pour le Merchant Room.

**Contexte narratif** : Vorathros manipule son propre ADN pour s'adapter aux anomalies de la timeline.

**Caractéristiques** :
- 6 slots maximum (miroir des 6 classes)
- Plus légers que les Perks (tactiques, pas build-defining)
- Servent à patcher les faiblesses contre les anomalies

**Exemples déjà documentés** :
- "Convert 30% Physical damage to Fire"
- "Your Bloodblades inflict Bleed even on immune enemies"
- "+20% damage against the dominant enemy type"
- "Gain 5% of damage dealt as Energy Shield"
- "Your summons taunt enemies for 2 seconds on spawn"
- "Lightning Resistance +30%"

**Fichier à créer** : `Glossary/Mutations/` (nouveau dossier)

**Statut** : [ ] Non commencé

---

### 5. Liste des Anomalies
**Objectif** : Créer la liste des Anomalies (distorsions temporelles) par floor.

**Contexte narratif** : Chaque run est une timeline différente. Les anomalies sont les distorsions uniques de cette timeline.

**Règle de design** : Les anomalies **challenge** le build sans le **hard-counter**.

**Exemples déjà documentés** :
- "Physical Resistance +50% on all enemies"
- "Enemies explode on death (Fire damage)"
- "No natural healing, but Lifesteal +30%"
- "Elite enemies have Frost Aura"
- "Lightning damage +100%, Movement speed -20%"
- "Enemies regenerate HP, but have -30% max HP"

**Fichier à créer** : `Glossary/Anomalies/` (nouveau dossier)

**Statut** : [ ] Non commencé

---

### 6. Liste des Consommables
**Objectif** : Définir les consommables obtenus en Normal Room.

**Fichier à créer** : `Glossary/Consumables/` (nouveau dossier)

**Statut** : [ ] Non commencé

---

### 7. Variantes Chamber of Lost Time
**Objectif** : Définir les mécaniques possibles pour cette room.

**Variantes documentées** :
- Single chest guaranteeing a Unique item
- Room full of treasure chests
- Choice of 3 Blessings
- Perk unlock (meta-progression during run)
- Special merchant with rare Mutations
- One-shot crafting station
- Narrative event with meaningful choice
- Healing fountain with a trade-off

**Fichier créé** : `Glossary/Game/Rooms/Chamber of Lost Time.md`

**Statut** : [x] Complété

---

## Documents de Référence

### Principaux
- **GDD** : `GDD.md` - Document principal mis à jour
- **Classes** : `Classes Description.md` - Description des 6 classes et leurs spécialisations
- **Rooms** : `Glossary/Game/Rooms.md` - Overview des rooms
- **Gameplay Loop** : `Glossary/Game/Gameplay Loop.md` - Flow général

### Skills par Catégorie
- **Blood Skills** : `Glossary/Skills and Perks/Blood/`
- **Voidborn Skills** : `Glossary/Skills and Perks/Voidborn/`
- **Curses** : `Glossary/Skills and Perks/Curses/`
- **Elemental** : `Glossary/Skills and Perks/Elemental/`

### Corruptions Existantes
- **Index** : `Glossary/Corruptions/Corruptions Index.md`
- **Bonus (Special Effects)** : `Glossary/Corruptions/Bonus/Special Effects/`
- **Bonus (Stat Bonuses)** : `Glossary/Corruptions/Bonus/Stat Bonuses/`
- **Malus** : `Glossary/Corruptions/Malus/`

---

## Décisions de Design Importantes

### Perks vs Mutations vs Supports
| Aspect | Perks | Mutations | Supports |
|--------|-------|-----------|----------|
| **Durée** | Permanent | Per-run | Permanent |
| **Impact** | Majeur (change le skill) | Tactique (patch faiblesses) | Modificateur (ajoute effets) |
| **Acquisition** | Méta-progression | Achat Merchant | Drop/Craft |
| **Équipement** | Avant la run | Pendant la run | Avant la run |
| **Narratif** | Maîtrise du skill | Manipulation ADN | Runes de support |

### Balance Purity/Corruption
- **Neutre (0-99%)** : Accès aux deux types de rooms, pas de rewards exclusives
- **Locked (100%)** : Un seul type de room, accès aux rewards exclusives (Sacred/Abyssal)
- **Stratégie** : Rester flexible vs s'engager pour des rewards puissantes

### 6 Mutation Slots
Miroir des 6 classes :
- 1 Mutation par classe pour couvrir chaque faiblesse
- Ou 6 Mutations sur une classe pour hyper-spécialiser

---

## Historique des Modifications

| Date | Modification |
|------|--------------|
| Session initiale | Refonte complète du système de progression |
| Session initiale | Création du système Augments |
| Session initiale | Redéfinition des rooms |
| Session initiale | Système Balance Purity/Corruption |
| Session initiale | Chamber of Lost Time (ex-Secret Room) |
| Session initiale | Création de ce tracker |
| Session initiale | **Renommage** : Floor Mutations → Floor Anomalies (timeline) |
| Session initiale | **Renommage** : Augments → Mutations (manipulation ADN de Vorathros) |

---

## Prochaine Session

Commencer par : **[À DÉFINIR]**

Options :
1. Update des Perks des skills existants
2. Création de la liste des Blessings
3. Création de la liste des Mutations (ex-Augments)
4. Mise à jour des Corruptions (ajouter tier Abyssal)
5. Création de la liste des Anomalies (ex-Floor Mutations)
