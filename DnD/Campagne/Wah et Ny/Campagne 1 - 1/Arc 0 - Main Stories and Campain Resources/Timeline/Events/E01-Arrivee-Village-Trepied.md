---
type: event
arc: 1
status: possible
date_ingame: Début de la campagne
dependencies: []
triggers:
  - "[[D01-Enquete-Village]]"
tags:
  - timeline
  - event
  - arc1
  - village-trepied
---

# Arrivée au Village de Trépied

## Contexte

**Quand:** Session 1, début de la campagne
**Où:** Village de Trépied, région rurale
**Qui:** Les aventuriers (niveau 1-3)

## Prérequis

- [x] Formation du groupe d'aventuriers
- [ ] Rumeurs de disparitions dans la région

## Description

### Ce qui se passe

Les aventuriers arrivent au paisible village de Trépied, une petite communauté agricole apparemment tranquille. Ils peuvent être là pour diverses raisons:
- Répondre à un appel à l'aide
- Passer par hasard
- Enquêter sur des rumeurs
- Mission donnée par une faction

**Première impression:** Village calme, habitants méfiants mais accueillants, atmosphère légèrement tendue.

**La vérité cachée:** Le village est sous l'influence subtile de l'Assemblée de l'Éveil Vigilant. Certains habitants ont été convertis, d'autres sont surveillés.

### Informations révélées

**Immédiatement accessibles:**
- Le village a connu des "incidents" récents
- Les habitants semblent nerveux
- Un puits ancien au centre du village
- L'auberge locale: bon point de départ

**Avec investigation (DC 12-15):**
- Disparitions occasionnelles
- Réunions étranges la nuit
- Certains villageois ont changé de comportement
- Rumeurs d'un "protecteur" mystérieux

**Difficile à découvrir (DC 18+):**
- L'existence de l'Assemblée
- Connexion avec des événements régionaux plus larges

## Choix Possibles

### Option A: Investigation Active

**Description:** Les joueurs décident d'enquêter activement sur les mystères du village.

**Conséquences immédiates:**
- Rencontre avec les PNJ clés
- Découverte d'indices
- Possibilité d'attirer l'attention de l'Assemblée

**Conséquences à long terme:**
- Mise en marche de l'intrigue principale
- Relations avec les villageois
- Premier contact indirect avec Aldric

**Triggers:** [[D01-Enquete-Village]], [[E02-Decouverte-Puits]]

---

### Option B: Approche Passive

**Description:** Les joueurs restent discrets, observent sans intervenir immédiatement.

**Conséquences immédiates:**
- Information limitée
- Pas d'alarme déclenchée
- Temps pour planifier

**Conséquences à long terme:**
- Découverte plus lente de l'intrigue
- Possibilité qu'un événement se produise sans leur intervention
- Relations neutres avec le village

**Triggers:** [[E03-Incident-Village]]

---

### Option C: Départ Immédiat

**Description:** Les joueurs ne trouvent rien d'intéressant et partent rapidement.

**Conséquences immédiates:**
- Arc 1 manqué
- Pas d'exposition à l'intrigue principale

**Conséquences à long terme:**
- L'Assemblée continue ses plans sans opposition
- Les joueurs peuvent revenir plus tard et trouver la situation empirée
- Arc alternatif nécessaire

**Triggers:** [[E04-Assemblee-Non-Stoppee]]

## État du Monde Après

### Changements majeurs
- Les aventuriers sont maintenant dans la région
- L'Assemblée peut avoir conscience de leur présence (selon les choix)
- Le village réagit à la présence d'étrangers

### Flags modifiés
```yaml
flags:
  joueurs_village_trepied: true
  assemblee_consciente_joueurs: false  # peut changer
  investigation_commencee: false  # selon choix
```

### Variables modifiées
```yaml
variables:
  reputation_village_trepied: 0
  niveau_alerte_assemblee: 0
  indices_decouverts: 0
```

## Notes MJ

**Hook d'entrée:** Assurez-vous que les joueurs ont une bonne raison d'être là. Utilisez leurs backgrounds si possible.

**Ambiance:** Mystère rural, tension sous-jacente, pas d'horreur immédiate mais un malaise croissant.

**PNJ clés à introduire:**
- Aubergiste du Trépied d'Or
- Maire du village
- Un villageois suspect (membre de l'Assemblée)
- Un villageois résistant (potentiel allié)

**Rythme:** Session 1 devrait être exploration et établissement du mystère, pas encore de combat majeur.

**Sidequests disponibles:**
- Le fermier qui a perdu son bétail
- L'enfant qui a vu quelque chose près du puits
- La veuve qui cherche son mari disparu

