# Skill: /add card

## Description
Genere des fiches Obsidian structurees pour le contenu D&D (armes, armures, outils, materiel d'aventurier, regles, conditions, etc.) avec frontmatter YAML, tags coherents et aliases pour integration optimale.

## Usage
```
/add card [description optionnelle]
```

## Exemples
- `/add card` - Mode interactif, demande le type de fiche
- `/add card toutes les armes du tableau Armes.md` - Parse et cree toutes les fiches du tableau
- `/add card Epee longue` - Cree une fiche pour cette arme specifique
- `/add card armure Cotte de mailles` - Cree une fiche d'armure
- `/add card outil Outils de forgeron` - Cree une fiche d'outil
- `/add card materiel Corde` - Cree une fiche de materiel d'aventurier
- `/add card condition Aveugle` - Cree une fiche de condition
- `/add card propriete Finesse` - Cree une fiche de propriete d'arme

## Types de fiches supportes

### 1. Armes
**Chemin:** `Glossary/Objets/Equipmement/Armes/[Categorie]/[Nom].md`
**Categories:**
- `Armes courantes de corps a corps/`
- `Armes courantes a distance/`
- `Armes de guerre de corps a corps/`
- `Armes de guerre a distance/`

**Template:** `Resources/Templates/template-arme.md`

### 2. Proprietes d'armes
**Chemin:** `Glossary/Objets/Equipmement/Armes/Proprietes/[Nom].md`
**Template:** `Resources/Templates/template-propriete-arme.md`

### 3. Bottes d'armes
**Chemin:** `Glossary/Objets/Equipmement/Armes/Botte d'Arme/[Nom].md`
**Template:** `Resources/Templates/template-botte-arme.md`

### 4. Regles
**Chemin:** `Glossary/[Nom].md` ou `Glossary/Jets/[Nom].md`
**Template:** `Resources/Templates/template-regle.md`

### 5. Conditions
**Chemin:** `Glossary/Conditions/[Nom].md`
**Template:** `Resources/Templates/template-condition.md`

### 6. Armures
**Chemin:** `Glossary/Objets/Equipmement/Armures/Liste/[Categorie]/[Nom].md`
**Categories:**
- `Armures légères/`
- `Armures intermédiaires/`
- `Armures lourdes/`

**Template:** `Resources/Templates/template-armure.md`

### 7. Outils
**Chemin:** `Glossary/Objets/Equipmement/Outils/Liste/[Categorie]/[Nom].md`
**Categories:**
- `Outils d'artisan/`
- `Autres outils/`

**Template:** `Resources/Templates/template-outil.md`

### 8. Matériel d'aventurier
**Chemin:** `Glossary/Objets/Equipmement/Matériel d'aventurier/Liste/[Nom].md`
**Template:** `Resources/Templates/template-materiel-aventurier.md`

## Comportement

1. **Detection du type**: Analyse la description pour determiner le type de fiche
2. **Lecture du template**: Charge le template correspondant depuis `Resources/Templates/`
3. **Generation du frontmatter**: Cree le YAML avec les proprietes appropriees
4. **Tags coherents**: Applique la hierarchie de tags standard
5. **Aliases**: Genere les variations de casse (Nom, nom) pour l'auto-linking

## Structure des Tags

### Tags communs
- `glossaire` - Toutes les fiches de reference
- `regle` - Regles et mecaniques
- `mecanique` - Mecaniques de jeu
- `equipement` - Objets et equipement

### Tags specifiques par type
**Armes:** `arme`, `arme-courante`/`arme-de-guerre`, `corps-a-corps`/`a-distance`, `[type-degats]`
**Proprietes:** `propriete-arme`, `combat`
**Bottes:** `botte-arme`, `capacite`, `combat`
**Regles:** `regle`, `mecanique`, `[domaine]`
**Conditions:** `condition`, `etat`, `combat`
**Armures:** `armure`, `armure-legere`/`armure-intermediaire`/`armure-lourde`, `bouclier`, `discretion-desavantage`
**Outils:** `outil`, `outil-artisan`, `jeu`, `instrument-musique`
**Matériel d'aventurier:** `materiel-aventurier`, `consommable`, `eclairage`, `contenant`, `vetement`, `objet-magique`, `paquetage`, `focaliseur-arcanique`, `focaliseur-druidique`, `symbole-sacre`, `munitions`

## Conventions

- **Langue:** Francais uniquement pour les aliases
- **Source:** Toujours specifier (PHB 2024, DMG, etc.)
- **Pas de wikilinks:** Ne PAS utiliser `[[Nom]]` - un addon Obsidian gere l'auto-linking automatiquement via les noms de fichiers et aliases
- **Pas d'emojis:** Jamais d'emojis dans les fiches (voir CLAUDE.md)
- **Aliases complets:** Generer TOUTES les variations d'ecriture possibles pour maximiser l'auto-linking :
  - Avec et sans accents (Épée, Epée, Epee)
  - Majuscule et minuscule (Épée, épée, epee)
  - Variations courantes (Légère, Legere, légère, legere)

  Exemple pour "Épée longue":
  ```yaml
  aliases:
    - Épée longue
    - Epée longue
    - Epee longue
    - épée longue
    - epée longue
    - epee longue
  ```

## Fichiers sources de reference
- **Armes:** `Glossary/Objets/Equipmement/Armes/Armes.md`
- **Armures:** `Glossary/Objets/Equipmement/Armures/Armures.md`
- **Outils:** `Glossary/Objets/Equipmement/Outils/Outils.md`
- **Matériel d'aventurier:** `Glossary/Objets/Equipmement/Matériel d'aventurier/Matériel d'aventurier.md`
