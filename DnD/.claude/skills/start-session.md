# Skill: /start-session

## Description
Initialise une nouvelle note de session pour la campagne en cours.

## Usage
```
/start-session [Numéro] [Titre Optionnel]
```

## Comportement
1.  **Dossier**: `Campagne/Wah et Ny/Campagne 1 - 1/Ch1 - Le Secret du Puits de Trépied/Sessions/`.
2.  **Nom du fichier**: `Session [N] - [Titre ou Date].md`.
3.  **Contenu**:
    - **Metadonnées**: Date réelle, Participants, Lieu en jeu.
    - **Structure**:
        - `## Log` (Notes brutes).
        - `## Résumé` (Synthèse pour la prochaine fois).
        - `## Loots & Récompenses`.
        - `## PNJ Rencontrés`.

## Exemple
```markdown
---
type: session
campaign: "Wah et Ny"
session_number: 12
date: 2026-01-10
tags: [session]
---
# Session 12 - Le Retour de l'Hermite

## Participants
- [ ] @Joueur1
- [ ] @Joueur2
```
