# Gemini Context: D&d - Artefact - Demon's Mark

## Project Overview
This directory is an **Obsidian Vault** dedicated to a Dungeons & Dragons campaign titled "Artefact - Demon's Mark". The game uses the **D&D 3.5** ruleset. It contains session notes, lore, and world-building information. The content is primarily written in **French**.

## Directory Structure

### `Session/`
Contains chronological logs of gameplay sessions. Files are named by date (e.g., `13-01-2026.md`).
*   **Purpose:** To track the narrative progression, encounters, NPC interactions, and rewards/transactions from each game session.

### `.obsidian/`
Standard Obsidian configuration directory containing workspace settings, plugin configurations, and themes.

## Key Files
*   **`Session/13-01-2026.md`**: Example session note detailing travel to "Col Givré", rumors about "Tor'gul" fortress, and item purchases (poisons, magical items).

## Usage
*   **Context:** This vault is used to maintain the state of the game world and the party's progress.
*   **Note Taking:** New entries should likely follow the established pattern in the `Session/` folder for chronological updates.
*   **Language:** Maintain French as the primary language for notes unless otherwise specified.

## Workflow: Fin de Session DnD
À la fin de chaque session (ou sur demande), l'agent doit :
1.  **Lire la nouvelle note de session** (ex: `Session/DD-MM-YYYY.md`).
2.  **Mettre à jour le Glossaire (`Glossaire/`)** :
    *   **Atomicité STRICTE :** Créer une fiche unique pour **TOUTE entité nommée** ou **concept clé**.
        *   Ceci inclut : PNJ (même mineurs ou mentionnés), Lieux, Objets, Monstres, Factions, **Concepts magiques/Lore** (Marque, Malédiction), **Événements historiques**, **Savoirs & Textes** (Livres, Archives, Légendes résumées), **Rituels**.
        *   **Ne jamais grouper** plusieurs entités dans une seule note. Si une entité est mentionnée, elle doit avoir sa fiche (ou un lien vers sa fiche future).
    *   **Alias :** Chaque note doit impérativement commencer par un bloc YAML `aliases` incluant le pluriel, les minuscules et les variantes orthographiques courantes pour faciliter le linking automatique.
    *   **Style :** Ne **JAMAIS** utiliser d'émojis dans les titres ou le corps des notes. Le style doit rester sobre et textuel. **Utiliser Mermaid** pour les diagrammes (relations, chronologies complexes) ou les **Canvas** Obsidian pour les vues d'ensemble visuelles quand cela est judicieux.
    *   Mettre à jour les fiches existantes avec les nouvelles informations.
3.  **Mettre à jour le Journal de Quêtes (`Glossaire/Journal de Quêtes.md`)** : Cocher les objectifs atteints et ajouter les nouvelles pistes.
4.  **Mettre à jour la Synthèse (`Glossaire/Résumé Campagne.md`)** : Ajouter les faits marquants à la chronologie ou au résumé global.
5.  **Déplacer/Archiver** les notes "en vrac" après traitement.
