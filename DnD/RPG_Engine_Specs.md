# Obsidian RPG Engine - Spécifications & Architecture

## 1. Vision
Créer un environnement de gestion de données dans Obsidian inspiré des moteurs de jeux (Godot/Unity).
L'objectif est de transformer le coffre-fort (Vault) en une base de données typée, orientée objet, avec héritage et polymorphisme, tout en conservant la lisibilité du Markdown.

## 2. Concepts Cœurs (Mapping Godot -> Obsidian)

| Concept Godot | Concept Plugin RPG | Implémentation technique (Proposition) |
| :--- | :--- | :--- |
| **Scene / Node** | **Note (.md)** | Un fichier Markdown contenant des données en Frontmatter (YAML). |
| **Script / Class** | **Schéma (.json/.yaml)** | Un fichier de définition décrivant la structure de données. |
| **Inspector** | **Panneau Propriétés** | Une UI personnalisée (React) affichant les champs typés selon le schéma. |
| **Export Var** | **Propriété Typée** | Un champ dans le YAML validé par le plugin. |
| **Resource** | **Struct / Nested Object** | Un objet complexe défini par un schéma, imbriqué dans une note ou référencé. |
| **Inheritance** | **Parent Field** | Un champ `parent: [[Note]]` qui permet d'hériter des valeurs. |

## 3. Système de Types

Le système doit supporter un typage fort et des structures complexes.

*   **Primitifs** : `string`, `number`, `boolean`, `multiline_text`.
*   **Collections** :
    *   `Array<T>` : Liste typée (ex: `weapon_proficiencies`).
    *   `Dictionary<K, V>` : Map typée (ex: `augmentations: { str: 1, dex: 2 }`).
*   **Structures Complexes (Resources)** :
    *   **Embedded Resource** : Un objet défini par un schéma mais stocké directement dans le YAML parent (ex: Prérequis `{ class: "Mage", level: 1 }`).
    *   **Referenced Resource** : Lien vers une note externe qui contient la donnée (ex: `[[Armure de Cuir]]`).
*   **Polymorphisme** :
    *   Une liste peut contenir des `Resources` de types différents (ex: `Array<Requirement>` contenant des `ClassRequirement` et `FeatRequirement`).
*   **Spéciaux RPG** :
    *   `Dice` (ex: "1d6+2").
    *   `Selection<T>` : "Choisir N parmi Liste".

## 4. Héritage et Stratégies de Fusion (Merge)

L'héritage ne doit pas se contenter de copier, il doit savoir comment traiter les conflits.

*   **Override** (Défaut) : La valeur de l'enfant remplace celle du parent.
*   **Merge (Add)** : Pour les nombres ou les listes.
    *   *Exemple (Race)* : Parent a `[Hache]`, Enfant a `[Marteau]`. Résultat : `[Hache, Marteau]`.
*   **Merge (Dictionary)** : Pour les stats.
    *   *Exemple (Stats)* : Parent `{ Con: 2 }`, Enfant `{ Sag: 1 }`. Résultat : `{ Con: 2, Sag: 1 }`.

## 5. Stockage des Schémas

*   **Emplacement** : Dossier `_Engine/Schemas` à la racine du Vault (visible et éditable).
*   **Format** : YAML.

## 6. Architecture Technique (Plugin)

1.  **Schema Loader** : Scanne `_Engine/Schemas` et construit le graphe de types en mémoire.
2.  **Data Indexer** : Scanne les notes, lit le YAML, et résout l'héritage (calcul des valeurs finales).
3.  **UI (React)** :
    *   **Inspector View** : Remplace ou complète la vue native. Affiche les valeurs calculées (grisées si héritées) et permet l'édition (Override).
    *   **Error Reporting** : Affiche les erreurs de typage (ex: "Vous avez mis du texte dans un champ Nombre").

---
**Plan d'Action Immédiat :**
1.  Générer le squelette du plugin (`main.ts`, `manifest.json`).
2.  Créer le dossier `_Engine/Schemas`.
3.  Implémenter le premier schéma test (`Manifestation.yaml`).
