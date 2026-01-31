# Story Engine - Commandes

Ce fichier documente les commandes personnalisées disponibles pour l'Assistant IA (Gemini/Claude) via le système de compétences (`.claude/skills`).

## Commandes Disponibles

### 1. Gestion de Contenu
*   **`/create-npc [Nom]`** : Crée une fiche de PNJ formatée dans le dossier du chapitre courant.
    *   *Source Skill*: `.claude/skills/create-npc.md`

### 2. Gestion de Session
*   **`/start-session [N]`** : Crée la note pour la nouvelle session de jeu.
    *   *Source Skill*: `.claude/skills/start-session.md`

### 3. Base de Données
*   **`/lookup [Terme]`** : Recherche une règle ou un objet dans le Glossaire sans hallucination.
    *   *Source Skill*: `.claude/skills/lookup.md`

## Ajouter une commande
Pour ajouter une commande, créez simplement un fichier Markdown dans le dossier `.claude/skills/` en suivant le format "Description / Usage / Comportement".
