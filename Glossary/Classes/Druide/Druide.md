---
Class: Class

aliases:
  - Druide
  - druide
  - Druid
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d8
saving_throws:
  - int
  - sag
armor_proficiencies:
  - legeres
  - intermediaires
  - boucliers
weapon_proficiencies:
  - gourdin
  - dague
  - flechette
  - javeline
  - masse
  - baton
  - cimeterre
  - fronde
  - serpe
  - lance
tool_proficiencies:
  - kit d'herboriste
skill_choices: 2
skill_options:
  - Arcanes
  - Dressage
  - Intuition
  - Medecine
  - Nature
  - Perception
  - Religion
  - Survie
spellcasting_ability: sag
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Druidique"
      - "Incantation"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Forme sauvage"
      - "Cercle druidique"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "Amélioration de caractéristiques"
      - "Forme sauvage améliorée"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "Capacité de cercle"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "Amélioration de caractéristiques"
      - "Forme sauvage améliorée"
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "Capacité de cercle"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
  - type: ClassLevelEntry
    level: 12
    proficiency_bonus: 4
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 5
    features:
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 5
    features:
      - "Capacité de cercle"
  - type: ClassLevelEntry
    level: 15
    proficiency_bonus: 5
    features:
  - type: ClassLevelEntry
    level: 16
    proficiency_bonus: 5
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 17
    proficiency_bonus: 6
    features:
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "Jeunesse éternelle"
      - "Incantation animale"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Archidruide"
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 1
    features:
      - "Aucune"
starting_equipment_draft: "- Un bouclier en bois OU une arme courante - Un cimeterre OU une arme courante de corps à corps - Une armure de cuir, un sac d'explorateur et un focaliseur druidique"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Bouclier]]"
        quantity: 1
      - type: CategoryItem
        category: "Arme courante"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Cimeterre]]"
        quantity: 1
      - type: CategoryItem
        category: "Arme courante de corps à corps"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        item: "[[Armure de cuir]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'explorateur]]"
        quantity: 1
      - type: CategoryItem
        category: "Focaliseur druidique"
        quantity: 1
---



# Druide

Les druides incarnent la force, la ruse et la colère de la nature. Ils se voient comme des extensions de la volonté indomptable de la nature plutôt que comme ses maîtres. Ils obtiennent leurs pouvoirs magiques des forces naturelles elles-mêmes ou de divinités de la nature.

## Tableau de progression

| Niveau | Bonus | Capacités | Sorts mineurs |
|--------|-------|-----------|---------------|
| 1 | +2 | Druidique, Incantation | 2 |
| 2 | +2 | Forme sauvage, Cercle druidique | 2 |
| 3 | +2 | - | 2 |
| 4 | +2 | Amélioration de caractéristiques, Forme sauvage améliorée | 3 |
| 5 | +3 | - | 3 |
| 6 | +3 | Capacité de cercle | 3 |
| 7 | +3 | - | 3 |
| 8 | +3 | Amélioration de caractéristiques, Forme sauvage améliorée | 3 |
| 9 | +4 | - | 3 |
| 10 | +4 | Capacité de cercle | 4 |
| 11 | +4 | - | 4 |
| 12 | +4 | Amélioration de caractéristiques | 4 |
| 13 | +5 | - | 4 |
| 14 | +5 | Capacité de cercle | 4 |
| 15 | +5 | - | 4 |
| 16 | +5 | Amélioration de caractéristiques | 4 |
| 17 | +6 | - | 4 |
| 18 | +6 | Jeunesse éternelle, Incantation animale | 4 |
| 19 | +6 | Amélioration de caractéristiques | 4 |
| 20 | +6 | Archidruide | 4 |

## Tableau de Mana

| Niveau | Niveau de sort max. | Mana |
|--------|---------------------|------|
| 1 | 1er | 2 |
| 2 | 1er | 4 |
| 3 | 2e | 8 |
| 4 | 2e | 10 |
| 5 | 3e | 16 |
| 6 | 3e | 20 |
| 7 | 4e | 24 |
| 8 | 4e | 28 |
| 9 | 5e | 36 |
| 10 | 5e | 42 |
| 11 | 6e | 48 |
| 12 | 6e | 50 |
| 13 | 7e | 54 |
| 14 | 7e | 58 |
| 15 | 8e | 62 |
| 16 | 8e | 64 |
| 17 | 9e | 72 |
| 18 | 9e | 76 |
| 19 | 9e | 82 |
| 20 | 9e | 90 |

> Voir [[Mana]] pour les règles complètes du système de mana.

## Caractéristiques de classe

**Dés de vie** : 1d8 par niveau de druide
**Points de vie au niveau 1** : 8 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d8 (ou 5) + modificateur de Constitution

### Maîtrises

- **Armures** : Armures légères, armures intermédiaires, boucliers (les druides n'utilisent pas d'armures ni de boucliers en métal)
- **Armes** : Gourdin, dague, fléchette, javeline, masse, bâton, cimeterre, fronde, serpe, lance
- **Outils** : Kit d'herboriste
- **Jets de sauvegarde** : Intelligence, Sagesse
- **Compétences** : Choisissez 2 parmi Arcanes, Dressage, Intuition, Médecine, Nature, Perception, Religion, Survie

### Équipement de départ

- Un bouclier en bois OU une arme courante
- Un cimeterre OU une arme courante de corps à corps
- Une armure de cuir, un sac d'explorateur et un focaliseur druidique

---

## Capacités de classe

### Druidique (niveau 1)

Vous connaissez le druidique, le langage secret des druides. Vous pouvez parler ce langage et l'utiliser pour laisser des messages secrets. Les autres remarquent un tel message avec un jet de Perception DD 15, mais ne peuvent pas le déchiffrer sans magie.

### Incantation (niveau 1)

Le druide prépare ses sorts chaque jour parmi la liste complète des sorts de druide.

**Caractéristique d'incantation** : Sagesse
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Sagesse
**Modificateur d'attaque** : bonus de maîtrise + modificateur de Sagesse
**Focaliseur** : Focaliseur druidique
**Sorts préparés** : niveau de druide + modificateur de Sagesse

### Forme sauvage (niveau 2)

Par une action, vous vous transformez magiquement en une bête que vous avez déjà vue. Vous pouvez utiliser cette capacité 2 fois par repos court ou long.

**Durée** : nombre d'heures égal à la moitié de votre niveau de druide (arrondi à l'inférieur)

**Restrictions de forme** :

| Niveau | FP max | Limitations | Exemple |
|--------|--------|-------------|---------|
| 2 | 1/4 | Pas de vol, pas de nage | Loup |
| 4 | 1/2 | Pas de vol | Crocodile |
| 8 | 1 | Aucune | Aigle géant |

**Règles de transformation** :
- Vos statistiques de jeu sont remplacées par celles de la bête
- Vous conservez votre alignement, personnalité, Intelligence, Sagesse et Charisme
- Vous conservez vos maîtrises de compétences et de jets de sauvegarde
- Vous gagnez les PV de la bête; les dégâts excès reviennent à votre forme normale
- Vous ne pouvez pas lancer de sorts sous forme sauvage (sauf avec Incantation animale)

### Cercle druidique (niveau 2)

Choisissez un cercle druidique qui vous confère des capacités aux niveaux 2, 6, 10 et 14.

### Jeunesse éternelle (niveau 18)

La magie primale que vous maniez vous permet de vieillir plus lentement. Pour chaque tranche de 10 ans qui passe, votre corps ne vieillit que d'un an.

### Incantation animale (niveau 18)

Vous pouvez lancer de nombreux sorts de druide sous n'importe quelle forme assumée par Forme sauvage. Vous pouvez effectuer les composantes somatiques et verbales d'un sort de druide sous forme de bête, mais vous ne pouvez pas fournir les composantes matérielles.

### Archidruide (niveau 20)

Vous pouvez utiliser Forme sauvage un nombre illimité de fois. De plus, vous pouvez ignorer les composantes verbales et somatiques de vos sorts de druide, ainsi que les composantes matérielles qui n'ont pas de coût et ne sont pas consommées par le sort.

---

## Cercles druidiques

### Cercle de la Lune

Les druides du Cercle de la Lune sont des gardiens sauvages qui assument des formes de combat puissantes.

#### Forme sauvage de combat (niveau 2)
Vous pouvez utiliser Forme sauvage en action bonus plutôt qu'en action. De plus, en forme sauvage, vous pouvez dépenser un emplacement de sort pour récupérer 1d8 points de vie par niveau d'emplacement.

#### Formes du cercle (niveau 2)
Vous pouvez vous transformer en bêtes de FP supérieur :
- FP 1 dès le niveau 2 (pas de vol)
- FP égal à votre niveau de druide divisé par 3 (arrondi à l'inférieur) dès le niveau 6

#### Frappe primitive (niveau 6)
Vos attaques sous forme de bête comptent comme magiques pour surmonter les résistances et immunités.

#### Forme sauvage élémentaire (niveau 10)
Vous pouvez dépenser deux utilisations de Forme sauvage pour vous transformer en un élémentaire d'air, d'eau, de terre ou de feu.

#### Mille formes (niveau 14)
Vous pouvez lancer le sort *modification d'apparence* à volonté.

---

### Cercle de la Terre

Les druides du Cercle de la Terre gardent les anciennes connaissances et rituels transmis depuis des générations.

#### Sort mineur supplémentaire (niveau 2)
Vous apprenez un sort mineur de druide supplémentaire de votre choix.

#### Récupération naturelle (niveau 2)
Lors d'un repos court, vous pouvez récupérer des emplacements de sorts dépensés. La somme des niveaux de ces emplacements ne peut pas excéder la moitié de votre niveau de druide (arrondi à l'inférieur), et aucun emplacement ne peut être de niveau 6 ou plus.

#### Sorts de cercle (niveau 3, 5, 7, 9)
Vous gagnez l'accès à des sorts de cercle selon votre terrain d'origine. Ces sorts sont toujours préparés et ne comptent pas dans le nombre de sorts préparés.

**Arctique**
| Niveau | Sorts |
|--------|-------|
| 3 | Immobilisation de personne, Croissance d'épines |
| 5 | Tempête de neige, Lenteur |
| 7 | Liberté de mouvement, Tempête de grêle |
| 9 | Communion avec la nature, Cône de froid |

**Désert**
| Niveau | Sorts |
|--------|-------|
| 3 | Flou, Silence |
| 5 | Création de nourriture et d'eau, Protection contre les énergies |
| 7 | Flétrissement, Terrain hallucinatoire |
| 9 | Fléaux d'insectes, Mur de pierre |

**Forêt**
| Niveau | Sorts |
|--------|-------|
| 3 | Peau d'écorce, Pattes d'araignée |
| 5 | Appel de la foudre, Croissance végétale |
| 7 | Divination, Liberté de mouvement |
| 9 | Communion avec la nature, Passage par les arbres |

**Littoral**
| Niveau | Sorts |
|--------|-------|
| 3 | Image miroir, Pas brumeux |
| 5 | Respiration aquatique, Marche sur l'eau |
| 7 | Contrôle de l'eau, Liberté de mouvement |
| 9 | Invocation d'élémentaire, Scrutation |

**Marais**
| Niveau | Sorts |
|--------|-------|
| 3 | Cécité/Surdité, Flèche acide de Melf |
| 5 | Marche sur l'eau, Nuage puant |
| 7 | Liberté de mouvement, Localisation de créature |
| 9 | Fléaux d'insectes, Scrutation |

**Montagne**
| Niveau | Sorts |
|--------|-------|
| 3 | Pattes d'araignée, Croissance d'épines |
| 5 | Éclair, Fusion dans la pierre |
| 7 | Façonnage de la pierre, Peau de pierre |
| 9 | Passe-muraille, Mur de pierre |

**Outreterre**
| Niveau | Sorts |
|--------|-------|
| 3 | Pattes d'araignée, Toile d'araignée |
| 5 | Forme gazeuse, Nuage puant |
| 7 | Invisibilité supérieure, Façonnage de la pierre |
| 9 | Nuage mortel, Fléaux d'insectes |

**Plaine**
| Niveau | Sorts |
|--------|-------|
| 3 | Invisibilité, Passage sans trace |
| 5 | Lumière du jour, Hâte |
| 7 | Divination, Liberté de mouvement |
| 9 | Rêve, Fléaux d'insectes |

#### Foulée tellurique (niveau 6)
Vous déplacer dans un terrain difficile non magique ne vous coûte pas de déplacement supplémentaire. Vous pouvez aussi traverser les plantes non magiques sans être ralenti et sans subir de dégâts de leurs épines ou dangers similaires.

#### Protégé de dame Nature (niveau 10)
Vous ne pouvez pas être charmé ou effrayé par les élémentaires ou les fées, et vous êtes immunisé contre les poisons et les maladies.

#### Sanctuaire de dame Nature (niveau 14)
Lorsqu'une bête ou une créature végétale vous attaque, elle doit effectuer un jet de sauvegarde de Sagesse contre votre DD de sauvegarde de sorts. En cas d'échec, elle doit choisir une cible différente ou l'attaque échoue automatiquement. En cas de réussite, la créature est immunisée contre cet effet pendant 24 heures.

---

### Cercle des Spores

Les druides du Cercle des Spores trouvent la beauté dans la décomposition et voient la mort comme faisant partie du cycle naturel.

#### Sorts de cercle

| Niveau | Sorts |
|--------|-------|
| 2 | Cécité/Surdité, Doux repos |
| 3 | Animation des morts, Forme gazeuse |
| 5 | Flétrissement, Confusion |
| 7 | Nuage mortel, Contagion |

#### Halo de spores (niveau 2)
Les créatures dans un rayon de 3 mètres subissent des dégâts nécrotiques (2d4, puis 2d6 au niveau 6, 2d8 au niveau 10, 2d10 au niveau 14) en réaction si elles échouent à un jet de sauvegarde de Constitution.

#### Animateur symbiotique (niveau 2)
Par une action, vous pouvez dépenser une utilisation de Forme sauvage pour éveiller les spores plutôt que de vous transformer. Vous gagnez 4 PV temporaires par niveau de druide et infligez 1d6 dégâts nécrotiques supplémentaires avec vos attaques d'arme de corps à corps.

#### Infestation fongique (niveau 6)
Les créatures tuées par vos dégâts nécrotiques se relèvent comme zombies avec 1 PV pendant 1 heure.

#### Propagation des spores (niveau 10)
Vous pouvez déplacer votre Halo de spores jusqu'à 9 mètres.

#### Corps fongique (niveau 14)
En Animateur symbiotique, vous êtes immunisé aux états aveugle, assourdi, effrayé et empoisonné, et les coups critiques contre vous deviennent des coups normaux.

---

### Cercle des Étoiles

Les druides du Cercle des Étoiles étudient les constellations et puisent leur magie dans le cosmos.

#### Carte stellaire (niveau 2)
Vous apprenez le sort mineur *assistance* et pouvez lancer *augure* sans dépenser de mana un nombre de fois égal à votre bonus de maîtrise par repos long. Votre carte stellaire est un focaliseur.

#### Forme stellaire (niveau 2)
Par une action bonus, vous pouvez dépenser une utilisation de Forme sauvage pour prendre une forme stellaire plutôt que de vous transformer en bête. Vous gagnez les bénéfices d'une constellation :
- **Archer** : Attaque à distance bonus, 1d8 + modificateur de Sagesse dégâts radiants
- **Calice** : Quand vous lancez un sort de guérison, vous ou une créature à 9 m regagnez 1d8 + modificateur de Sagesse PV
- **Dragon** : Considérez un résultat de 9 ou moins comme un 10 sur les jets de Concentration et d'Intelligence/Sagesse

#### Refuge cosmique (niveau 6)
Forme stellaire vous donne résistance aux dégâts contondants, perçants et tranchants.

#### Forme stellaire scintillante (niveau 10)
Les bénéfices de constellation s'améliorent (2d8, avantage aux jets d'initiative pour Dragon).

#### Forme stellaire complète (niveau 14)
Au début de chaque tour en Forme stellaire, vous pouvez changer de constellation.
