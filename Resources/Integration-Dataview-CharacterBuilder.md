# Intégration Dataview avec le Character Builder

## Contexte

Le character builder D&D actuel lit les données du vault en parsant des blocs de code spéciaux (`dnd-classe`, `dnd-race`, etc.). Cependant, les fichiers du vault utilisent maintenant le **frontmatter YAML** pour stocker les métadonnées.

## Problème actuel

### Ce que le builder cherche (ancien format)

```markdown
```dnd-classe
name: Barbare
des_de_vie: d12
maitrises:
  sauvegardes: [for, con]
  armures: [legeres, intermediaires, boucliers]
```
```

### Ce que les fichiers contiennent (format actuel)

```markdown
---
hit_dice: d12
saving_throws: [for, con]
armor_proficiencies: [legeres, intermediaires, boucliers]
weapon_proficiencies: [courantes, guerre]
skill_choices: 2
skill_options: [Athletisme, Dressage, ...]
---

# Barbare
[contenu de la classe]
```

**Résultat**: Le builder ne trouve aucune classe car il cherche les blocs `dnd-classe` qui n'existent pas.

## Solution: Utiliser l'API Dataview

Dataview est déjà installé et activé dans le vault. Il indexe automatiquement tous les fichiers markdown et leurs frontmatter.

### Avantages

1. **Pas de duplication**: Une seule source de données (le frontmatter)
2. **Mise en cache automatique**: Dataview maintient un index performant
3. **Requêtes puissantes**: Filtrage et tri avancés disponibles
4. **Compatibilité**: Les fichiers fonctionnent à la fois dans le builder et dans les notes Dataview
5. **Maintenance simplifiée**: Moins de code de parsing manuel

## Implémentation recommandée

### Étape 1: Vérifier la disponibilité de Dataview

```javascript
// Dans VaultDataLoader
static getDataviewAPI(app) {
    const dv = app.plugins.plugins.dataview?.api;
    if (!dv) {
        console.error('[DnD Builder] Dataview plugin non disponible');
        new Notice('Le plugin Dataview est requis pour le Character Builder');
        return null;
    }
    return dv;
}
```

### Étape 2: Remplacer loadClasses()

```javascript
static async loadClasses(app) {
    const dv = this.getDataviewAPI(app);
    if (!dv) return {};

    const classes = {};

    // Charger toutes les pages du dossier Classes
    const pages = dv.pages('"Glossary/Classes"')
        .where(p => !p.parent_class); // Exclure les sous-classes

    for (const page of pages) {
        const className = page.file.name;

        classes[className] = {
            name: className,
            des_de_vie: page.hit_dice || 'd8',
            pv_niveau_1: parseInt(page.hit_dice?.replace('d', '')) || 8,
            maitrises: {
                sauvegardes: page.saving_throws || [],
                armures: page.armor_proficiencies || [],
                armes: page.weapon_proficiencies || [],
                outils: page.tool_proficiencies || [],
                competences: {
                    nombre: page.skill_choices || 2,
                    options: page.skill_options || []
                }
            },
            capacites: page.capacites || [],
            source: page.source || 'PHB'
        };
    }

    console.log(`[DnD Builder] ${Object.keys(classes).length} classes chargées via Dataview`);
    return classes;
}
```

### Étape 3: Remplacer loadRaces()

```javascript
static async loadRaces(app) {
    const dv = this.getDataviewAPI(app);
    if (!dv) return {};

    const races = {};
    const pages = dv.pages('"Glossary/Races"');

    for (const page of pages) {
        const raceName = page.file.name;

        races[raceName] = {
            name: raceName,
            augmentations: page.augmentations || {},
            vitesse: this.parseSpeed(page.vitesse),
            taille: page.taille || 'M',
            langues: page.langues || ['Commun'],
            traits: page.traits || [],
            sous_races: page.sous_races || []
        };
    }

    console.log(`[DnD Builder] ${Object.keys(races).length} races chargées via Dataview`);
    return races;
}
```

### Étape 4: Charger les sous-classes

```javascript
static async loadSubclasses(app) {
    const dv = this.getDataviewAPI(app);
    if (!dv) return {};

    const subclasses = {};

    // Charger les fichiers qui ont un parent_class
    const pages = dv.pages('"Glossary/Classes"')
        .where(p => p.parent_class);

    for (const page of pages) {
        const parentClass = page.parent_class?.path || page.parent_class;

        if (!subclasses[parentClass]) {
            subclasses[parentClass] = [];
        }

        subclasses[parentClass].push({
            name: page.subclass_name || page.file.name,
            capacites: page.capacites || [],
            description: page.description || ''
        });
    }

    console.log(`[DnD Builder] Sous-classes chargées pour ${Object.keys(subclasses).length} classes`);
    return subclasses;
}
```

### Étape 5: Charger les sorts avec Dataview

```javascript
static async loadSpells(app) {
    const dv = this.getDataviewAPI(app);
    if (!dv) return {};

    const spells = {};
    const pages = dv.pages('"Glossary/Liste des Sorts"');

    for (const page of pages) {
        spells[page.file.name] = {
            name: page.file.name,
            niveau: page.niveau || 0,
            ecole: page.ecole || '',
            temps_incantation: page.temps_incantation || '1 action',
            portee: page.portee || 'Contact',
            composantes: page.composantes || [],
            duree: page.duree || 'Instantanée',
            classes: page.classes || [],
            description: page.description || ''
        };
    }

    console.log(`[DnD Builder] ${Object.keys(spells).length} sorts chargés via Dataview`);
    return spells;
}
```

## Mapping des propriétés

### Classes

| Ancien format (bloc dnd-classe) | Nouveau format (frontmatter) |
|--------------------------------|------------------------------|
| `des_de_vie` | `hit_dice` |
| `maitrises.sauvegardes` | `saving_throws` |
| `maitrises.armures` | `armor_proficiencies` |
| `maitrises.armes` | `weapon_proficiencies` |
| `maitrises.outils` | `tool_proficiencies` |
| (nombre de compétences hardcodé) | `skill_choices` |
| (compétences hardcodées) | `skill_options` |

### Races

| Ancien format | Nouveau format |
|--------------|----------------|
| `augmentations` | `augmentations` (identique) |
| `vitesse` | `vitesse` (identique) |
| `langues` | `langues` (identique) |
| `traits` | `traits` (identique) |

## Utilisation avancée de Dataview

### Filtrer les classes par source

```javascript
const phbClasses = dv.pages('"Glossary/Classes"')
    .where(p => p.source === "PHB");
```

### Trier par dé de vie

```javascript
const classesByHP = dv.pages('"Glossary/Classes"')
    .sort(p => p.hit_dice, 'desc');
```

### Recherche de sorts par niveau et classe

```javascript
const fireball = dv.page('"Glossary/Liste des Sorts/Boule de feu"');
const availableForWizard = fireball.classes?.includes("Magicien");
```

### Afficher les statistiques

```javascript
// Compter le nombre de classes par dé de vie
const statsByDice = dv.pages('"Glossary/Classes"')
    .groupBy(p => p.hit_dice);
```

## Migration progressive

### Option 1: Support des deux formats (transition)

```javascript
static async loadClasses(app) {
    const dv = this.getDataviewAPI(app);

    // Fallback si Dataview n'est pas disponible
    if (!dv) {
        console.warn('[DnD Builder] Dataview indisponible, utilisation du parsing manuel');
        return this.loadClassesLegacy(app);
    }

    // Utiliser Dataview
    return this.loadClassesWithDataview(app, dv);
}
```

### Option 2: Migration complète (recommandé)

Supprimer complètement les fonctions `parseClassBlock()`, `parseRaceBlock()`, etc. et utiliser uniquement Dataview.

## Tests recommandés

1. Vérifier que toutes les classes sont chargées correctement
2. Vérifier que les sous-classes sont associées à leur classe parente
3. Tester la sélection de compétences (skill_choices et skill_options)
4. Vérifier les augmentations de caractéristiques raciales
5. Tester la liste des sorts disponibles par classe

## Bénéfices à long terme

1. **Évolutivité**: Facile d'ajouter de nouvelles propriétés sans modifier le code
2. **Debuggage**: Utiliser les requêtes Dataview directement dans Obsidian pour tester
3. **Performance**: L'index Dataview est optimisé et mis en cache
4. **Cohérence**: Une seule façon de structurer les données
5. **Communauté**: Compatible avec d'autres plugins utilisant Dataview

## Questions / Points d'attention

1. **Dépendance**: Le builder dépend maintenant de Dataview - documenter cette exigence
2. **Rétrocompatibilité**: Décider si on garde le support des anciens blocs de code
3. **Gestion d'erreurs**: Que faire si Dataview n'est pas installé/activé?
4. **Performance**: Tester avec un grand nombre de fichiers (100+ sorts, 50+ classes)

## Prochaines étapes suggérées

1. Remplacer `loadClasses()` et tester
2. Remplacer `loadRaces()` et tester
3. Ajouter `loadSubclasses()` pour gérer les sous-classes
4. Remplacer `loadSpells()`
5. Remplacer `loadBackgrounds()` et `loadEquipment()`
6. Supprimer le code de parsing manuel
7. Mettre à jour la documentation du plugin

## Exemple complet: Fichier de classe

```markdown
---
aliases: [Barbare, barbare, Barbarian]
tags: [classe, creation-personnage]
hit_dice: d12
saving_throws: [for, con]
armor_proficiencies: [legeres, intermediaires, boucliers]
weapon_proficiencies: [courantes, guerre]
tool_proficiencies: []
skill_choices: 2
skill_options:
  - Athletisme
  - Dressage
  - Intimidation
  - Nature
  - Perception
  - Survie
spellcasting_ability:
source: PHB
---

# Barbare

Le barbare incarne la fureur primale...

[contenu markdown...]
```

Ce fichier est maintenant:
- Lisible par Dataview
- Utilisable par le character builder
- Affichable avec des requêtes Dataview dynamiques
- Compatible avec les templates Templater

---

**Auteur**: Documentation pour l'intégration Character Builder + Dataview
**Date**: 2026-01-04
**Version du builder**: 4.0.0
