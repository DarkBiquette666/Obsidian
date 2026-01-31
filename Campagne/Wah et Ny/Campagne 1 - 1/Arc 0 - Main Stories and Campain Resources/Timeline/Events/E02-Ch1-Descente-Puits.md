---
type: event
arc: "Ch1 - Puits Trépied"
chronologie: accompli
status: accompli
date_jeu: Séance 1
session: 1
dependencies:
  - "[[E01-Ch1-Reception-Mission]]"
  - "[[D01-Ch1-Approche-Hermite]]"
triggers:
  - "[[D02-Ch1-Descendre-Ou-Non]]"
  - "[[E03-Ch1-Rencontre-Mephit]]"
tags:
  - timeline
  - event
  - ch1
  - puits
  - combat
---

## Evenement: La Descente Périlleuse dans le Puits

### Prerequis

- Simon est au village
- Maître Renard lui a parlé des bruits du puits
- Pataud vient de sauter dans le puits

### Description

Alors que Simon et Maître Renard s'approchent du puits pour investiguer les bruits étranges, **Pataud saute soudainement dans le puits**.

Le maire panique et commence à préparer sa propre descente, mais Simon l'arrête et décide de descendre lui-même.

**Équipement:**
- Lanterne (occupe une main)
- Armure lourde
- Contrainte: Nage avec une seule main libre (lanterne)

**La descente:**
Simon descend et arrive dans l'eau souterraine de la grotte. Il doit nager vers la rive où Pataud attend.

**TEST CRITIQUE: Athlétisme**
- Résultat: **4 (Échec)**

**Conséquences de l'échec:**
1. Simon doit abandonner sa lanterne dans l'eau pour pouvoir nager à deux mains
2. De l'eau contaminée entre dans sa bouche
3. Il subit des effets légers de la potion violette
4. Il atteint la rive dans l'obscurité totale

### Personnages Impliques

- [[Simon-Fiche-Personnage|Simon]] - Descend dans le puits
- [[Maître Renard]] - Panique pour son chien
- [[Pataud]] - Déclenche tout en sautant dans le puits

### Lieux

- [[Le Puits]] - Point de descente
- [[La Grotte]] - Caverne souterraine sous le village

### Choix Possibles

**Décision prise:** [[D02-Ch1-Descendre-Ou-Non]]
- Simon choisit de descendre lui-même
- Alternative: Laisser le maire descendre

### Consequences Directes

- Perte d'équipement: Lanterne
- Exposition à la potion violette
- Arrive dans la grotte dans le noir
- Pataud sauvé, rejoint Simon

### Impact a Long Terme

- Court terme: Simon contaminé légèrement → effets à surveiller
- Moyen terme: Démonstration de bravoure (Aldric observe?)
- Long terme: Première épreuve physique

### Etat du Monde Apres

**Flags modifiés:**
```yaml
flags:
  puits_explore: true
  grotte_decouverte: true
  simon_contamine: true
  lanterne_perdue: true
  pataud_sauve: true
```

**Variables modifiées:**
```yaml
variables:
  equipement_lanterne: 0
  confiance_maitre_renard: +10
  exposition_potion_violette: 1
```

### Notes MJ

**Moment clé:** L'échec au test d'Athlétisme change toute la dynamique de l'exploration. Simon se retrouve dans le noir, contaminé, sans lanterne.

**Gestion de la contrainte:** Le joueur a dû gérer le fait de tenir sa lanterne hors de l'eau, ce qui a rendu la nage difficile.

**Tension narrative:** 20 minutes à tâtons dans le noir crée un vrai moment de tension.

**Choix héroïque:** Simon descend à la place du maire → montre son caractère protecteur (trait qu'Aldric recherche).

### Ressources

- Voir [[Résumé#La Descente Périlleuse]]
- Voir [[Le Puits]]
- Voir [[La Grotte]]
