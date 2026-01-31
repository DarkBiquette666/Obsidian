# RPG Engine - Documentation Système

## Introduction
Ce système transforme Obsidian en un véritable moteur de gestion de données pour le Jeu de Rôle (type Godot/Unity). Il permet de structurer les données (Races, Classes, Sorts) avec un typage fort, de l'héritage, et une interface d'édition graphique.

## Architecture

### 1. Blueprints (Modèles)
Les modèles de données sont définis dans `_Engine/Blueprints/`. Ce sont des fichiers Markdown `.md` contenant un bloc YAML décrivant la structure.

*   **Format** :
    ```yaml
    name: NomDuType
    extends: ParentType (optionnel)
    properties:
      champ1:
        type: string | number | boolean | link | array | select
        default: valeur_par_défaut
    ```

### 2. Données (Notes)
Chaque note du `Glossary` peut être typée en ajoutant la propriété `Class` dans son Frontmatter.
*   Exemple : `Class: Spell`.

### 3. Inspecteur (UI)
L'interface d'édition se trouve dans le panneau de droite (commande "Open RPG Inspector"). Elle remplace l'édition manuelle du YAML.
*   **Sync** : Bouton pour mettre à jour la note avec les nouveaux champs du Blueprint.
*   **Preview** : Bouton pour voir les données finales (après héritage).

## Types de Données

### Classes (`Blueprint: Class`)
*   Définit une classe de personnage.
*   **Progression** : Tableau `ClassLevelEntry` (Bonus, Capacités).
*   **Équipement** : Liste de `EquipmentGroup` (Choix ET/OU d'objets).

### Races (`Blueprint: Race` / `SubRace`)
*   **Augmentations** : Liste de `AbilityBonus`.
*   **Traits** : Liste de liens vers des notes `RacialTrait`.
*   **Langues** : Liste de liens vers des notes `Language`.

### Sorts (`Blueprint: Spell`)
*   Définit le niveau, l'école, et si le sort inflige des dégâts.
*   **Domaines** : Liens vers les domaines divins.

### Équipement
*   **Hiérarchie** : `Equipment` -> `Weapon`, `Armor`, `MagicItem`, `EquipmentPack`.
*   **Propriétés** : Les propriétés d'armes et bottes sont des liens vers des notes dédiées.

### Prérequis (Système Polymorphe)
Utilisé pour les dons et manifestations.
*   **Base** : `Requirement` (Abstrait).
*   **Enfants** :
    *   `ClassRequirement` (Classe + Niveau).
    *   `SpellCriteriaRequirement` (Filtre sur les sorts : niveau, dégâts...).
    *   `ManifestationRequirement` (Lien vers une autre manifestation).

## Guide d'Utilisation

### Ajouter un nouveau type d'objet
1.  Créer un fichier dans `_Engine/Blueprints/`.
2.  Définir ses propriétés.
3.  Recharger les Blueprints dans Obsidian ("Reload Blueprints").

### Ajouter une note
1.  Créer la note.
2.  Ouvrir l'Inspecteur.
3.  Assigner la Classe correspondante.

### Modifier un Blueprint existant
1.  Ajouter le champ dans le fichier Blueprint.
2.  Utiliser le bouton **Sync** sur les notes existantes pour injecter la valeur par défaut.
