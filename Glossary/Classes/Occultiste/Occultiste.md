---
Class: Class

aliases:
  - Occultiste
  - occultiste
  - Warlock
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d8
saving_throws:
  - sag
  - cha
armor_proficiencies:
  - legeres
weapon_proficiencies:
  - courantes
tool_proficiencies: []
skill_choices: 2
skill_options:
  - Arcanes
  - Histoire
  - Intimidation
  - Investigation
  - Nature
  - Religion
  - Tromperie
spellcasting_ability: cha
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Patron d'Outremonde"
      - "Magie de pacte"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Manifestations occultes"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "Faveur de pacte"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "Capacité de patron"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "Capacité de patron"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "Arcanum mystique (6e)"
  - type: ClassLevelEntry
    level: 12
    proficiency_bonus: 4
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 5
    features:
      - "Arcanum mystique (7e)"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 5
    features:
      - "Capacité de patron"
  - type: ClassLevelEntry
    level: 15
    proficiency_bonus: 5
    features:
      - "Arcanum mystique (8e)"
  - type: ClassLevelEntry
    level: 16
    proficiency_bonus: 5
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 17
    proficiency_bonus: 6
    features:
      - "Arcanum mystique (9e)"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Maître de l'occulte"
starting_equipment_draft: "- Une arbalète légère et 20 carreaux OU une arme courante - Une sacoche à composantes OU un focaliseur arcanique - Un sac d'érudit OU un sac de donjon - Une armure de cuir, une arme courante et deux dagues"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: EquipmentGroup
        selection_mode: AND
        items:
          - type: SpecificItem
            item: "[[Arbalète légère]]"
            quantity: 1
          - type: SpecificItem
            item: "[[Carreaux]]"
            quantity: 20
      - type: CategoryItem
        category: "Arme courante"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Sacoche à composantes]]"
        quantity: 1
      - type: CategoryItem
        category: "Focaliseur arcanique"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Sac d'érudit]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'exploration souterraine]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        item: "[[Armure de cuir]]"
        quantity: 1
      - type: CategoryItem
        category: "Arme courante"
        quantity: 1
      - type: SpecificItem
        item: "[[Dague]]"
        quantity: 2
---



# Occultiste

Les occultistes sont des chercheurs de la connaissance dissimulée dans la trame du multivers qui obtiennent leurs pouvoirs via des pactes avec des entités surnaturelles puissantes. Contrairement aux magiciens, ils combinent la magie avec une certaine aptitude au combat rapproché.

## Tableau de progression

| Niveau | Bonus | Capacités | Mineurs | Sorts connus | Emplacements | Niveau sort | Invocations |
|--------|-------|-----------|---------|--------------|--------------|-------------|-------------|
| 1 | +2 | Patron d'Outremonde, Magie de pacte | 2 | 2 | 1 | 1er | - |
| 2 | +2 | Manifestations occultes | 2 | 3 | 2 | 1er | 2 |
| 3 | +2 | Faveur de pacte | 2 | 4 | 2 | 2e | 2 |
| 4 | +2 | Amélioration de caractéristiques | 3 | 5 | 2 | 2e | 2 |
| 5 | +3 | - | 3 | 6 | 2 | 3e | 3 |
| 6 | +3 | Capacité de patron | 3 | 7 | 2 | 3e | 3 |
| 7 | +3 | - | 3 | 8 | 2 | 4e | 4 |
| 8 | +3 | Amélioration de caractéristiques | 3 | 9 | 2 | 4e | 4 |
| 9 | +4 | - | 3 | 10 | 2 | 5e | 5 |
| 10 | +4 | Capacité de patron | 4 | 10 | 2 | 5e | 5 |
| 11 | +4 | Arcanum mystique (6e) | 4 | 11 | 3 | 5e | 5 |
| 12 | +4 | Amélioration de caractéristiques | 4 | 11 | 3 | 5e | 6 |
| 13 | +5 | Arcanum mystique (7e) | 4 | 12 | 3 | 5e | 6 |
| 14 | +5 | Capacité de patron | 4 | 12 | 3 | 5e | 6 |
| 15 | +5 | Arcanum mystique (8e) | 4 | 13 | 3 | 5e | 7 |
| 16 | +5 | Amélioration de caractéristiques | 4 | 13 | 3 | 5e | 7 |
| 17 | +6 | Arcanum mystique (9e) | 4 | 14 | 4 | 5e | 7 |
| 18 | +6 | - | 4 | 14 | 4 | 5e | 8 |
| 19 | +6 | Amélioration de caractéristiques | 4 | 15 | 4 | 5e | 8 |
| 20 | +6 | Maître de l'occulte | 4 | 15 | 4 | 5e | 8 |

## Tableau de Mana (Sorcier)

| Niveau | Niveau de sort max. | Mana |
|--------|---------------------|------|
| 1 | 1er | 1 |
| 2 | 1er | 2 |
| 3 | 2e | 4 |
| 4 | 2e | 4 |
| 5 | 3e | 6 |
| 6 | 3e | 6 |
| 7 | 4e | 8 |
| 8 | 4e | 8 |
| 9 | 5e | 10 |
| 10 | 5e | 10 |
| 11 | 5e | 15 |
| 12 | 5e | 15 |
| 13 | 5e | 15 |
| 14 | 5e | 15 |
| 15 | 5e | 15 |
| 16 | 5e | 15 |
| 17 | 5e | 20 |
| 18 | 5e | 20 |
| 19 | 5e | 20 |
| 20 | 5e | 20 |

> **Récupération de mana** : L'occultiste récupère 100% de son mana après un repos court ou long. Voir [[Mana]] pour les règles complètes du système de mana.

## Caractéristiques de classe

**Dés de vie** : 1d8 par niveau d'occultiste
**Points de vie au niveau 1** : 8 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d8 (ou 5) + modificateur de Constitution

### Maîtrises

- **Armures** : Armures légères
- **Armes** : Armes courantes
- **Outils** : Aucun
- **Jets de sauvegarde** : Sagesse, Charisme
- **Compétences** : Choisissez 2 parmi Arcanes, Histoire, Intimidation, Investigation, Nature, Religion, Tromperie

### Équipement de départ

- Une arbalète légère et 20 carreaux OU une arme courante
- Une sacoche à composantes OU un focaliseur arcanique
- Un sac d'érudit OU un sac de donjon
- Une armure de cuir, une arme courante et deux dagues

---

## Capacités de classe

### Patron d'Outremonde (niveau 1)

Vous avez conclu un pacte avec un être surnaturel. Votre patron vous confère des capacités aux niveaux 1, 6, 10 et 14.

### Magie de pacte (niveau 1)

L'occultiste connaît ses sorts de manière innée. Ses emplacements de sorts sont tous du même niveau et se récupèrent après un repos court ou long.

**Caractéristique d'incantation** : Charisme
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Charisme
**Modificateur d'attaque** : bonus de maîtrise + modificateur de Charisme
**Focaliseur** : Focaliseur arcanique

### Manifestations occultes (niveau 2)

Vous apprenez des fragments de connaissances interdites qui vous confèrent des capacités magiques permanentes. Vous apprenez 2 manifestations au niveau 2 et d'autres selon le tableau.

Lorsque vous gagnez un niveau d'occultiste, vous pouvez remplacer une manifestation par une autre.

### Faveur de pacte (niveau 3)

Votre patron vous accorde un don en fonction de votre pacte.

#### Pacte de la Chaîne
Vous apprenez le sort *appel de familier* et pouvez le lancer comme rituel. Votre familier peut prendre une forme spéciale : diablotin, pseudodragon, quasit ou sprite.

Lorsque vous utilisez l'action Attaquer, vous pouvez renoncer à une attaque pour permettre à votre familier d'attaquer avec sa réaction.

#### Pacte de la Lame
Vous pouvez utiliser une action pour créer une arme de pacte dans votre main. Vous maîtrisez cette arme tant que vous la tenez. L'arme compte comme magique.

Vous pouvez transformer une arme magique en votre arme de pacte par un rituel de 1 heure.

#### Pacte du Grimoire
Votre patron vous donne un grimoire appelé Livre des Ombres. Choisissez 3 sorts mineurs de n'importe quelle liste de sorts. Vous pouvez les lancer tant que vous avez le livre sur vous.

### Arcanum mystique (niveau 11, 13, 15, 17)

Votre patron vous enseigne un secret magique appelé arcanum. Choisissez un sort de niveau 6 de la liste d'occultiste. Vous pouvez le lancer une fois sans dépenser de mana. Vous devez terminer un repos long avant de le relancer.

Vous gagnez des arcanums supplémentaires de niveau 7 (niveau 13), 8 (niveau 15) et 9 (niveau 17).

### Maître de l'occulte (niveau 20)

Vous pouvez supplier votre patron pour regagner vos emplacements de sorts dépensés. Passez 1 minute à supplier votre patron pour regagner tous vos emplacements. Vous devez terminer un repos long avant de réutiliser cette capacité.

---

## Manifestations occultes

### Manifestations de base

| Manifestation | Prérequis | Effet |
|---------------|-----------|-------|
| Souffle agonisant | - | Ajoutez modificateur CHA aux dégâts de *représentation caduque* |
| Armure d'ombres | - | Lancez *armure du mage* à volonté sans mana |
| Vision occulte | - | Lancez *détection de la magie* à volonté sans mana |
| Regard perçant | - | Voyez normalement dans les ténèbres magiques et non-magiques (36m) |
| Yeux du gardien des runes | - | Lisez toutes les langues écrites |
| Mauvais oeil | - | Voyez la vraie forme des métamorphes et créatures déguisées (9m) |
| Saut effrayant | - | Lancez *saut* à volonté sur vous-même sans mana |
| Voix du maître des chaînes | Pacte Chaîne | Communiquez télépathiquement avec votre familier |
| Lame assoiffée | Pacte Lame, niv. 5 | Attaque supplémentaire avec votre arme de pacte |
| Souffle répulsif | - | *Représentation caduque* repousse de 3m |
| Livre des secrets anciens | Pacte Grimoire | 2 rituels de n'importe quelle classe dans votre Livre des Ombres |

### Manifestations avancées (niveau 5+)

| Manifestation | Prérequis | Effet |
|---------------|-----------|-------|
| Voile de cauchemar | Niv. 7 | Lancez *sanctuaire illusoire* une fois par repos long sans mana |
| Sculpture des ombres | Niv. 5 | Lancez *invisibilité* sur vous-même sans mana une fois par repos long |
| Signe de mauvais augure | Niv. 5 | Lancez *maléfice* sans mana une fois par repos long |
| Maître des myriades formes | Niv. 15 | Lancez *modification d'apparence* à volonté sans mana |
| Chaînes de Carceri | Niv. 15, Pacte Chaîne | Lancez *immobilisation de monstre* une fois par repos long sans mana |
| Visions de royaumes lointains | Niv. 15 | Lancez *oeil magique* une fois par repos long sans mana |

---

## Patrons d'Outremonde

### L'Archifée

Votre patron est une puissante entité des royaumes féeriques.

#### Sorts étendus

| Niveau d'occultiste | Sorts |
|---------------------|-------|
| 1 | Lueurs féeriques, Sommeil |
| 3 | Apaisement des émotions, Force fantasmagorique |
| 5 | Clignotement, Croissance végétale |
| 7 | Domination de bête, Invisibilité supérieure |
| 9 | Domination de personne, Apparence trompeuse |

#### Présence féerique (niveau 1)
Par une action, vous obligez les créatures dans un cube de 3 mètres centré sur vous à faire un jet de sauvegarde de Sagesse. Celles qui échouent sont charmées ou effrayées (votre choix) jusqu'à la fin de votre prochain tour. Utilisations : 1 par repos court ou long.

#### Échappatoire brumeuse (niveau 6)
Lorsque vous subissez des dégâts, vous pouvez utiliser votre réaction pour devenir invisible et vous téléporter jusqu'à 18 mètres. Vous restez invisible jusqu'au début de votre prochain tour. Utilisations : 1 par repos court ou long.

#### Défenses captivantes (niveau 10)
Vous ne pouvez pas être charmé et, lorsqu'une créature tente de vous charmer, vous pouvez utiliser votre réaction pour tenter de la charmer en retour (sauvegarde SAG).

#### Délire nocturne (niveau 14)
Vous pouvez plonger une créature dans un délire illusoire. Elle doit faire un jet de sauvegarde de Sagesse ou être charmée ou effrayée pendant 1 minute. Utilisations : 1 par repos long.

---

### Le Fiélon

Votre patron est un seigneur des plans inférieurs.

#### Sorts étendus

| Niveau d'occultiste | Sorts |
|---------------------|-------|
| 1 | Injonction, Mains brûlantes |
| 3 | Cécité/Surdité, Rayon ardent |
| 5 | Boule de feu, Nuage puant |
| 7 | Bouclier de feu, Mur de feu |
| 9 | Colonne de flamme, Sanctification |

#### Bénédiction du ténébreux (niveau 1)
Lorsque vous réduisez une créature hostile à 0 PV, vous gagnez des PV temporaires égaux à votre modificateur de Charisme + niveau d'occultiste (minimum 1).

#### Chance du ténébreux (niveau 6)
Vous pouvez faire appel à votre patron pour modifier le destin. Lorsque vous faites un jet de caractéristique ou de sauvegarde, vous pouvez ajouter 1d10 au résultat. Utilisations : 1 par repos court ou long.

#### Résistance fiélonne (niveau 10)
Choisissez un type de dégâts. Vous gagnez la résistance à ce type. Ce choix peut être changé à chaque repos court ou long.

#### Traversée des enfers (niveau 14)
Lorsque vous touchez une créature avec une attaque, vous pouvez la téléporter dans les plans inférieurs. Elle disparaît jusqu'à la fin de votre prochain tour, puis réapparaît à sa position d'origine et subit 10d10 dégâts psychiques. Utilisations : 1 par repos long.

---

### Le Grand Ancien

Votre patron est une entité d'au-delà des étoiles dont les motivations sont incompréhensibles.

#### Sorts étendus

| Niveau d'occultiste | Sorts |
|---------------------|-------|
| 1 | Bouche magique, Murmures dissonants |
| 3 | Détection des pensées, Force fantasmagorique |
| 5 | Clairvoyance, Communication à distance |
| 7 | Domination de bête, Tentacules noirs d'Evard |
| 9 | Domination de personne, Télékinésie |

#### Esprit éveillé (niveau 1)
Vous pouvez communiquer télépathiquement avec toute créature à 9 mètres que vous pouvez voir. La créature n'a pas besoin de partager une langue avec vous.

#### Protection entropique (niveau 6)
Lorsqu'une créature fait un jet d'attaque contre vous, vous pouvez utiliser votre réaction pour lui imposer un désavantage. Si l'attaque rate, vous gagnez l'avantage à votre prochaine attaque contre cette créature. Utilisations : 1 par repos court ou long.

#### Bouclier mental (niveau 10)
Vos pensées ne peuvent pas être lues par télépathie ou autres moyens. Vous avez la résistance aux dégâts psychiques, et si une créature vous inflige des dégâts psychiques, elle subit le même montant.

#### Asservissement mental (niveau 14)
Vous pouvez toucher une créature neutralisée et la charmer. Elle reste charmée jusqu'à ce qu'un sort de *lever une malédiction* soit lancé sur elle ou que vous utilisiez à nouveau cette capacité.

---

### Le Génie

Votre patron est un génie noble issu des plans élémentaires.

#### Types de génie

| Génie | Type de dégâts | Sorts étendus |
|-------|----------------|---------------|
| Dao (terre) | Contondants | Sanctuaire, Croissance d'épines, Mur de pierre |
| Djinn (air) | Tonnerre | Vague tonnante, Bourrasque, Contrôle du vent |
| Éfrit (feu) | Feu | Mains brûlantes, Rayon ardent, Mur de feu |
| Marid (eau) | Froid | Nappe de brouillard, Flou, Cône de froid |

#### Catalyseur du génie (niveau 1)
Vous possédez un réceptacle lié à votre génie. Une fois par tour, lorsque vous touchez avec une attaque, vous infligez des dégâts supplémentaires du type de votre génie égaux à votre bonus de maîtrise.

#### Répit embouteillé (niveau 1)
Par une action, vous pouvez entrer dans votre réceptacle pendant 2 x niveau d'occultiste heures. L'intérieur fait 6 mètres de diamètre. Vous pouvez sortir par une action bonus.

#### Don élémentaire (niveau 6)
Vous gagnez la résistance au type de dégâts de votre génie. De plus, par une action bonus, vous gagnez une vitesse de vol de 9 mètres pendant 10 minutes.

#### Sanctuaire du génie (niveau 10)
Lorsque vous entrez dans votre réceptacle, vous pouvez emmener jusqu'à 5 créatures consentantes. Chacune peut sortir par une action bonus.

#### Souhait limité (niveau 14)
Vous pouvez supplier votre génie d'exaucer un souhait. Vous pouvez lancer un sort de niveau 6 ou moins de n'importe quelle liste sans composantes matérielles. Utilisations : 1 par 1d4 repos longs.
