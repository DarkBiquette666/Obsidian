# Skill: /create-npc

## Description
Crée une nouvelle note de PNJ (Personnage Non-Joueur) dans le dossier de campagne approprié, structurée selon le format attendu par le plugin D&D Content Renderer.

## Usage
```
/create-npc [Nom] [Description/Détails]
```

## Comportement
1.  **Analyse**: Extrait le nom, la race, et le rôle du PNJ de la description.
2.  **Lieu de création**: `Campagne/Wah et Ny/Campagne 1 - 1/Ch1 - Le Secret du Puits de Trépied/PNJ/` (Par défaut, ou demande le chapitre).
3.  **Format**:
    - Frontmatter YAML complet.
    - `Class: Biography` (Pour le RPG Engine).
    - Tags: `pnj`, `[faction]`.
4.  **Contenu**:
    - Section Description physique.
    - Section Personnalité (Traits, Idéaux, Liens, Défauts).
    - Section Histoire/Background.
    - Section Statblock (si combattant).

## Exemple YAML
```yaml
---
name: "Garrick le Brave"
Class: Biography
race: "Humain"
alignment: "Neutre Bon"
location: "Trépied"
faction: "Milice"
tags:
  - pnj
  - humain
  - milice
---
```
