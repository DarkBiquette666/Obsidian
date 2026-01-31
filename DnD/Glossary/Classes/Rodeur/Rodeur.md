---
Class: Class

aliases:
  - Rôdeur
  - rôdeur
  - Ranger
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d10
saving_throws:
  - for
  - dex
armor_proficiencies:
  - legeres
  - intermediaires
  - boucliers
weapon_proficiencies:
  - courantes
  - guerre
tool_proficiencies: []
skill_choices: 3
skill_options:
  - Athletisme
  - Discretion
  - Dressage
  - Intuition
  - Investigation
  - Nature
  - Perception
  - Survie
spellcasting_ability: sag
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Ennemi juré"
      - "Explorateur-né"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Style de combat"
      - "Incantation"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "Archétype de rôdeur"
      - "Vigilance primitive"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
      - "Attaque supplémentaire"
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "Amélioration d'ennemi juré et terrain"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
      - "Capacité d'archétype"
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "Amélioration de caractéristiques"
      - "Foulée tellurique"
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "Camouflage naturel"
      - "Amélioration de terrain"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "Capacité d'archétype"
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
      - "Amélioration d'ennemi juré"
      - "Disparition"
  - type: ClassLevelEntry
    level: 15
    proficiency_bonus: 5
    features:
      - "Capacité d'archétype"
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
      - "Sens sauvages"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Tueur implacable"
starting_equipment_draft: "- Une armure d'écailles OU une armure de cuir - Deux épées courtes OU deux armes courantes de corps à corps - Un sac de donjon OU un sac d'explorateur - Un arc long et un carquois de 20 flèches"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Armure d'écailles]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Armure de cuir]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Épée courte]]"
        quantity: 2
      - type: CategoryItem
        category: "Arme courante de corps à corps"
        quantity: 2
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Sac d'exploration souterraine]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'explorateur]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        item: "[[Arc long]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Carquois]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Flèches]]"
        quantity: 20
---



# Rôdeur

Les rôdeurs sont des guerriers des étendues sauvages spécialisés dans la traque des monstres menaçant la civilisation. Ils combinent compétences martiales, discrétion et magie naturelle pour protéger les zones frontalières.

## Tableau de progression

| Niveau | Bonus | Capacités | Sorts connus |
|--------|-------|-----------|--------------|
| 1 | +2 | Ennemi juré, Explorateur-né | - |
| 2 | +2 | Style de combat, Incantation | 2 |
| 3 | +2 | Archétype de rôdeur, Vigilance primitive | 3 |
| 4 | +2 | Amélioration de caractéristiques | 3 |
| 5 | +3 | Attaque supplémentaire | 4 |
| 6 | +3 | Amélioration d'ennemi juré et terrain | 4 |
| 7 | +3 | Capacité d'archétype | 5 |
| 8 | +3 | Amélioration de caractéristiques, Foulée tellurique | 5 |
| 9 | +4 | - | 6 |
| 10 | +4 | Camouflage naturel, Amélioration de terrain | 6 |
| 11 | +4 | Capacité d'archétype | 7 |
| 12 | +4 | Amélioration de caractéristiques | 7 |
| 13 | +5 | - | 8 |
| 14 | +5 | Amélioration d'ennemi juré, Disparition | 8 |
| 15 | +5 | Capacité d'archétype | 9 |
| 16 | +5 | Amélioration de caractéristiques | 9 |
| 17 | +6 | - | 10 |
| 18 | +6 | Sens sauvages | 10 |
| 19 | +6 | Amélioration de caractéristiques | 11 |
| 20 | +6 | Tueur implacable | 11 |

## Tableau de Mana (Demi-lanceur)

| Niveau | Niveau de sort max. | Mana |
|--------|---------------------|------|
| 1 | - | - |
| 2 | 1er | 2 |
| 3 | 1er | 4 |
| 4 | 1er | 4 |
| 5 | 2e | 8 |
| 6 | 2e | 8 |
| 7 | 2e | 10 |
| 8 | 2e | 10 |
| 9 | 3e | 16 |
| 10 | 3e | 16 |
| 11 | 3e | 18 |
| 12 | 3e | 18 |
| 13 | 4e | 22 |
| 14 | 4e | 22 |
| 15 | 4e | 24 |
| 16 | 4e | 24 |
| 17 | 5e | 30 |
| 18 | 5e | 30 |
| 19 | 5e | 36 |
| 20 | 5e | 42 |

> Voir [[Mana]] pour les règles complètes du système de mana.

## Caractéristiques de classe

**Dés de vie** : 1d10 par niveau de rôdeur
**Points de vie au niveau 1** : 10 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d10 (ou 6) + modificateur de Constitution

### Maîtrises

- **Armures** : Armures légères, armures intermédiaires, boucliers
- **Armes** : Armes courantes, armes de guerre
- **Outils** : Aucun
- **Jets de sauvegarde** : Force, Dextérité
- **Compétences** : Choisissez 3 parmi Athlétisme, Discrétion, Dressage, Intuition, Investigation, Nature, Perception, Survie

### Équipement de départ

- Une armure d'écailles OU une armure de cuir
- Deux épées courtes OU deux armes courantes de corps à corps
- Un sac de donjon OU un sac d'explorateur
- Un arc long et un carquois de 20 flèches

---

## Capacités de classe

### Ennemi juré (niveau 1)

Choisissez un type d'ennemi favori : aberrations, bêtes, célestes, créatures artificielles, dragons, élémentaires, fées, fiélons, géants, monstruosités, morts-vivants, plantes, ou vases. Vous pouvez également choisir deux races d'humanoïdes (comme les gnolls et les orques).

Vous avez l'avantage aux jets de Sagesse (Survie) pour pister vos ennemis jurés et aux jets d'Intelligence pour vous rappeler des informations les concernant. Vous apprenez une langue parlée par vos ennemis jurés s'ils en parlent une.

Vous choisissez un ennemi juré supplémentaire aux niveaux 6 et 14.

### Explorateur-né (niveau 1)

Choisissez un terrain favori : arctique, désert, forêt, littoral, marais, montagne, outreterres ou plaine.

En terrain favori :
- Votre bonus de maîtrise est doublé pour les jets d'Intelligence et de Sagesse liés à ce terrain
- Le terrain difficile ne ralentit pas le voyage de votre groupe
- Votre groupe ne peut pas se perdre sauf par magie
- Même en effectuant une autre activité de voyage, vous restez alerte
- En vous déplaçant seul, vous pouvez vous déplacer furtivement à un rythme normal
- Vous trouvez deux fois plus de nourriture en fourrage
- En pistant, vous savez combien de créatures, leur taille et depuis combien de temps elles sont passées

Vous choisissez un terrain favori supplémentaire aux niveaux 6 et 10.

### Style de combat (niveau 2)

Choisissez un style de combat :

- **Archerie** : +2 aux jets d'attaque avec des armes à distance
- **Combat à deux armes** : Ajoutez votre modificateur de caractéristique aux dégâts de la seconde attaque
- **Défense** : +1 à la CA tant que vous portez une armure
- **Duel** : +2 aux dégâts quand vous maniez une arme de corps à corps à une main et aucune autre arme

### Incantation (niveau 2)

Le rôdeur connaît ses sorts de manière innée.

**Caractéristique d'incantation** : Sagesse
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Sagesse
**Modificateur d'attaque** : bonus de maîtrise + modificateur de Sagesse
**Focaliseur** : Aucun (composantes uniquement)

### Vigilance primitive (niveau 3)

Par une action, vous pouvez dépenser un emplacement de sort (ou du mana) pour concentrer votre conscience sur la région autour de vous. Pendant 1 minute par niveau de sort dépensé, vous pouvez sentir si les types de créatures suivants sont présents dans un rayon de 1,5 km (ou 9 km en terrain favori) : aberrations, célestes, dragons, élémentaires, fées, fiélons, morts-vivants.

Cette capacité ne révèle pas leur emplacement ni leur nombre.

### Archétype de rôdeur (niveau 3)

Choisissez un archétype qui vous confère des capacités aux niveaux 3, 7, 11 et 15.

### Attaque supplémentaire (niveau 5)

Vous pouvez attaquer deux fois au lieu d'une quand vous utilisez l'action Attaquer pendant votre tour.

### Foulée tellurique (niveau 8)

Vous déplacer dans un terrain difficile non magique ne vous coûte pas de déplacement supplémentaire. Vous pouvez aussi traverser les plantes non magiques sans être ralenti et sans subir de dégâts de leurs épines ou dangers similaires.

De plus, vous avez l'avantage aux jets de sauvegarde contre les plantes qui sont magiquement créées ou manipulées pour entraver le mouvement.

### Camouflage naturel (niveau 10)

Vous pouvez passer 1 minute à créer un camouflage pour vous-même. Vous devez avoir accès à de la boue, de la terre, des plantes, de la suie et d'autres matériaux naturels.

Une fois camouflé, vous pouvez tenter de vous cacher en vous pressant contre une surface solide d'au moins votre hauteur et largeur. Vous gagnez un bonus de +10 aux jets de Dextérité (Discrétion) tant que vous restez immobile.

### Disparition (niveau 14)

Vous pouvez utiliser l'action Se cacher en action bonus pendant votre tour. De plus, vous ne pouvez pas être pisté par des moyens non magiques, sauf si vous choisissez de laisser une piste.

### Sens sauvages (niveau 18)

Vous gagnez des sens surnaturels qui vous aident à combattre les créatures que vous ne voyez pas. Quand vous attaquez une créature que vous ne voyez pas, votre incapacité à la voir ne vous impose pas un désavantage aux jets d'attaque contre elle.

Vous avez également conscience de l'emplacement de toute créature invisible à 9 mètres de vous, si cette créature n'est pas cachée de vous et que vous n'êtes pas aveugle ou assourdi.

### Tueur implacable (niveau 20)

Vous devenez un chasseur sans pareil de vos ennemis. Une fois par tour, vous pouvez ajouter votre modificateur de Sagesse au jet d'attaque ou de dégâts d'une attaque contre un de vos ennemis jurés.

---

## Archétypes de rôdeur

### Chasseur

Le chasseur accepte son rôle de rempart entre la civilisation et les terreurs des étendues sauvages.

#### Proie du chasseur (niveau 3)

Choisissez une des options suivantes :

**Tueur de colosses** : Votre ténacité peut user les ennemis les plus puissants. Quand vous touchez une créature avec une attaque d'arme, elle subit 1d8 dégâts supplémentaires si elle à moins que son maximum de points de vie.

**Tueur de géants** : Quand une créature de taille G ou plus grande à 1,5 m de vous vous touche ou vous rate avec une attaque, vous pouvez utiliser votre réaction pour attaquer cette créature immédiatement après son attaque, si vous pouvez la voir.

**Briseur de hordes** : Une fois par tour, quand vous effectuez une attaque d'arme, vous pouvez effectuer une autre attaque avec la même arme contre une créature différente se trouvant à 1,5 m de la cible originale et à portée de votre arme.

#### Tactiques défensives (niveau 7)

Choisissez une des options suivantes :

**Échapper à la horde** : Les attaques d'opportunité contre vous sont effectuées avec un désavantage.

**Défense contre les attaques multiples** : Quand une créature vous touche avec une attaque, vous gagnez un bonus de +4 à la CA contre toutes les attaques subséquentes effectuées par cette créature jusqu'à la fin du tour.

**Moral d'acier** : Vous avez l'avantage aux jets de sauvegarde contre la condition effrayé.

#### Attaques multiples (niveau 11)

Choisissez une des options suivantes :

**Volée** : Vous pouvez utiliser votre action pour effectuer une attaque à distance contre n'importe quel nombre de créatures à 3 mètres d'un point que vous pouvez voir à portée de votre arme. Vous devez avoir des munitions pour chaque cible et effectuez un jet d'attaque séparé pour chaque cible.

**Attaque tourbillonnante** : Vous pouvez utiliser votre action pour effectuer une attaque de corps à corps contre n'importe quel nombre de créatures à 1,5 m de vous, avec un jet d'attaque séparé pour chaque cible.

#### Défense supérieure du chasseur (niveau 15)

Choisissez une des options suivantes :

**Esquive totale** : Quand vous êtes soumis à un effet qui vous permet de faire un jet de sauvegarde de Dextérité pour ne subir que la moitié des dégâts, vous ne subissez aucun dégât en cas de réussite et la moitié en cas d'échec.

**Retour du bâton** : Quand une créature hostile rate une attaque de corps à corps contre vous, vous pouvez utiliser votre réaction pour l'obliger à répéter la même attaque contre une autre créature (autre que vous) de votre choix.

**Esquive instinctive** : Quand un attaquant que vous pouvez voir vous touche avec une attaque, vous pouvez utiliser votre réaction pour réduire de moitié les dégâts.

---

### Maître des bêtes

Le maître des bêtes forme un lien mystique avec un compagnon animal.

#### Compagnon du rôdeur (niveau 3)

Vous obtenez un compagnon animal qui vous accompagne dans vos aventures. Choisissez une bête de taille M ou moins avec un FP de 1/4 ou moins.

Le compagnon utilise votre bonus de maîtrise pour sa CA, ses jets d'attaque et ses jets de dégâts, ainsi que pour ses jets de sauvegarde et compétences qu'il maîtrise. Son maximum de points de vie est égal à son maximum normal ou à quatre fois votre niveau de rôdeur, selon le plus élevé.

Le compagnon obéit à vos ordres. À votre tour, vous pouvez verbalement ordonner à la bête de se déplacer (pas d'action requise). Vous pouvez utiliser votre action pour lui ordonner d'effectuer l'action Attaquer, Foncer, Se désengager, Esquiver ou Aider.

Si vous êtes neutralisé, le compagnon peut agir de lui-même.

Si le compagnon meurt, vous pouvez en obtenir un autre en passant 8 heures à vous lier à une bête appropriée.

#### Entraînement exceptionnel (niveau 7)

À votre tour, si votre compagnon n'attaque pas, vous pouvez utiliser une action bonus pour lui ordonner d'effectuer l'action Foncer, Se désengager ou Aider.

De plus, les attaques du compagnon comptent comme magiques pour surmonter les résistances et immunités.

#### Fureur bestiale (niveau 11)

Quand vous ordonnez à votre compagnon d'utiliser l'action Attaquer, il peut effectuer deux attaques ou utiliser Attaques multiples s'il en dispose.

#### Partage de sorts (niveau 15)

Quand vous lancez un sort qui vous cible, vous pouvez aussi affecter votre compagnon animal s'il est à 9 mètres de vous.

---

### Gardien de Drake

Le gardien de Drake a formé un lien avec un drake, une créature draconique qui sert de compagnon fidèle.

#### Don draconique (niveau 3)

Vous apprenez à parler, lire et écrire le draconique. De plus, vous apprenez le sort mineur *thaumaturgie*.

#### Compagnon drake (niveau 3)

Par une action, vous pouvez invoquer votre drake, qui apparaît dans un espace inoccupé à 9 mètres de vous.

**Statistiques du drake** :
- **PV** : 5 + 5 x votre niveau de rôdeur
- **CA** : 14 + votre bonus de maîtrise
- **Vitesse** : 12 m
- **Immunité** : type de dégâts correspondant à son Essence draconique

**Essence draconique** : Choisissez acide, froid, feu, foudre ou poison. Le drake est immunisé à ce type de dégâts et peut l'infliger.

**Actions** : À votre tour, le drake peut se déplacer et utiliser sa réaction. Il agit lors de votre initiative. Par défaut, il esquive. Vous pouvez utiliser une action bonus pour lui ordonner d'effectuer une autre action (Attaquer, Foncer, Se désengager, Aider).

**Morsure** : +votre bonus de maîtrise + modificateur de Sagesse, portée 1,5 m, 1d6 + bonus de maîtrise dégâts perçants.

**Réaction - Souffle infusant** : Quand vous ou un allié à 9 m touchez avec une attaque, le drake peut ajouter 1d6 dégâts de son Essence (2d6 au niveau 15).

Le drake disparaît s'il tombe à 0 PV, si vous le renvoyez (pas d'action), ou si vous mourez. Vous pouvez l'invoquer un nombre de fois égal à votre bonus de maîtrise par repos long.

#### Lien du croc et de l'écaille (niveau 7)

**Améliorations du drake** :
- Le drake devient de taille M et peut servir de monture
- Il gagne une vitesse de vol de 12 m
- Ses attaques de morsure infligent 1d6 dégâts supplémentaires de son Essence

**Votre bénéfice** : Vous gagnez la résistance au type de dégâts de l'Essence de votre drake.

#### Souffle du drake (niveau 11)

Par une action, vous canalisez une énergie destructrice dans votre drake. Il exhale un cône de 9 mètres. Chaque créature dans la zone doit effectuer un jet de sauvegarde de Dextérité (DD = votre DD de sort) et subit 8d6 dégâts du type de l'Essence (moitié en cas de réussite).

Les dégâts passent à 10d6 au niveau 15.

**Utilisations** : 1 par repos long, ou en dépensant un emplacement de sort de niveau 3+

#### Lien parfait (niveau 15)

**Améliorations du drake** :
- Le drake devient de taille G et peut être monté en vol
- Les attaques de morsure infligent 2d6 dégâts supplémentaires de son Essence
- Ses PV augmentent de 40

**Résistance réflexive** : Par une réaction, quand vous ou le drake subissez des dégâts, vous pouvez donner la résistance à ces dégâts à la cible (vous ou le drake).

**Utilisations de Résistance réflexive** : bonus de maîtrise par repos long

---

### Traqueur glissant

Le traqueur glissant excelle dans les environnements urbains et la traque discrète.

#### Ruse urbaine (niveau 3)

Vous gagnez la maîtrise de deux compétences parmi Intuition, Investigation, Représentation, Escamotage et Tromperie.

De plus, vous pouvez appliquer votre capacité Terrain favori aux environnements urbains.

#### Ruse de combat (niveau 3)

Vous pouvez utiliser l'action Se cacher en action bonus. De plus, vous ne subissez pas de pénalité aux jets de Discrétion quand vous vous déplacez jusqu'à la moitié de votre vitesse.

#### Pisteur implacable (niveau 7)

Quand vous désignez une créature comme cible de votre sort *marque du chasseur*, vous pouvez la localiser tant qu'elle est sur le même plan que vous.

#### Frappe inattendue (niveau 11)

Si vous attaquez une créature surprise, elle subit des dégâts supplémentaires égaux à votre niveau de rôdeur sur la première attaque.

#### Glisseur des ombres (niveau 15)

Quand vous êtes dans la pénombre ou les ténèbres, vous pouvez utiliser une action bonus pour vous téléporter jusqu'à 18 mètres dans un espace que vous pouvez voir qui est également dans la pénombre ou les ténèbres.
