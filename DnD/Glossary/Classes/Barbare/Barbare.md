---
Class: Class
aliases:
  - Barbare
  - barbare
  - Barbarian
tags:
  - classe
  - creation-personnage
hit_dice: d12
saving_throws:
  - for
  - con
armor_proficiencies:
  - legeres
  - intermediaires
  - boucliers
weapon_proficiencies:
  - courantes
  - guerre
tool_proficiencies: []
skill_choices: 2
skill_options:
  - Athlétisme
  - Dressage
  - Intimidation
  - Nature
  - Perception
  - Survie
spellcasting_ability:
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "2"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "2"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "3"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "3"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
      - "3"
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "4"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
      - "4"
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "4"
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
      - "4"
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "4"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "4"
  - type: ClassLevelEntry
    level: 12
    proficiency_bonus: 4
    features:
      - "5"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 5
    features:
      - "5"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 5
    features:
      - "5"
  - type: ClassLevelEntry
    level: 15
    proficiency_bonus: 5
    features:
      - "5"
  - type: ClassLevelEntry
    level: 16
    proficiency_bonus: 5
    features:
      - "5"
  - type: ClassLevelEntry
    level: 17
    proficiency_bonus: 6
    features:
      - "6"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "6"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "6"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - Illimité
starting_equipment_draft: "- Une hache à deux mains OU une [[arme de guerre de corps à corps]] - Deux hachettes OU une arme courante - Un sac d'explorateur et quatre javelines"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        quantity: 1
        item: "[[Hache à deux mains]]"
      - type: CategoryItem
        quantity: 1
        category: Arme de guerre de corps à corps
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        quantity: 2
        item: "[[Hachette]]"
      - type: CategoryItem
        quantity: 1
        category: Arme courante
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        quantity: 1
        item: "[[Sac d'explorateur]]"
      - type: SpecificItem
        quantity: 4
        item: "[[Javeline]]"
---



# Barbare

Le barbare incarne la fureur primale et l'instinct sauvage. Ces guerriers canalisent une rage implacable leur conférant des réflexes surhumains, une résistance et une puissance physique exceptionnelles.

## Tableau de progression

| Niveau | Bonus | Rages    | Dégâts Rage | Capacités                                  |
| ------ | ----- | -------- | ----------- | ------------------------------------------ |
| 1      | +2    | 2        | +2          | Rage, Défense sans armure                  |
| 2      | +2    | 2        | +2          | Attaque téméraire, Sens du danger          |
| 3      | +2    | 3        | +2          | Voie primitive                             |
| 4      | +2    | 3        | +2          | Amélioration de caractéristiques           |
| 5      | +3    | 3        | +2          | Attaque supplémentaire, Déplacement rapide |
| 6      | +3    | 4        | +2          | Capacité de voie                           |
| 7      | +3    | 4        | +2          | Instinct sauvage                           |
| 8      | +3    | 4        | +2          | Amélioration de caractéristiques           |
| 9      | +4    | 4        | +3          | Critique brutal (1 dé)                     |
| 10     | +4    | 4        | +3          | Capacité de voie                           |
| 11     | +4    | 4        | +3          | Rage implacable                            |
| 12     | +4    | 5        | +3          | Amélioration de caractéristiques           |
| 13     | +5    | 5        | +3          | Critique brutal (2 dés)                    |
| 14     | +5    | 5        | +3          | Capacité de voie                           |
| 15     | +5    | 5        | +3          | Rage persistante                           |
| 16     | +5    | 5        | +4          | Amélioration de caractéristiques           |
| 17     | +6    | 6        | +4          | Critique brutal (3 dés)                    |
| 18     | +6    | 6        | +4          | Puissance indomptable                      |
| 19     | +6    | 6        | +4          | Amélioration de caractéristiques           |
| 20     | +6    | Illimité | +4          | Champion primitif                          |

## Caractéristiques de classe

**Dés de vie** : 1d12 par niveau de barbare
**Points de vie au niveau 1** : 12 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d12 (ou 7) + modificateur de Constitution

### Maîtrises

- **Armures** : Armures légères, armures intermédiaires, boucliers
- **Armes** : Armes courantes, armes de guerre
- **Outils** : Aucun
- **Jets de sauvegarde** : Force, Constitution
- **Compétences** : Choisissez 2 parmi Athlétisme, Dressage, Intimidation, Nature, Perception, Survie

### Équipement de départ

- Une hache à deux mains OU une [[arme de guerre de corps à corps]]
- Deux hachettes OU une arme courante
- Un sac d'explorateur et quatre javelines

---

## Capacités de classe

### Rage (niveau 1)

En combat, vous pouvez entrer en rage par une action bonus. Pendant votre rage :
- Avantage aux jets de Force et aux jets de sauvegarde de Force
- Bonus aux dégâts de corps à corps selon le niveau (voir tableau)
- Résistance aux dégâts contondants, perçants et tranchants
- Vous ne pouvez pas lancer de sorts ni vous concentrer sur un sort

La rage dure 1 minute et se termine si :
- Vous êtes inconscient
- Vous n'avez pas attaqué ou subi de dégâts depuis votre dernier tour
- Vous choisissez de l'arrêter (action bonus)

### Défense sans armure (niveau 1)

Tant que vous ne portez pas d'armure, votre CA = 10 + modificateur de Dextérité + modificateur de Constitution. Vous pouvez utiliser un bouclier.

### Attaque téméraire (niveau 2)

Lors de votre première attaque du tour, vous pouvez décider d'attaquer de manière téméraire. Vous obtenez l'avantage à tous vos jets d'attaque de corps à corps ce tour, mais les attaques contre vous ont aussi l'avantage jusqu'à votre prochain tour.

### Sens du danger (niveau 2)

Vous avez l'avantage aux jets de sauvegarde de Dextérité contre les effets que vous pouvez voir (pièges, sorts) tant que vous n'êtes pas aveugle, assourdi ou neutralisé.

### Voie primitive (niveau 3)

Choisissez une voie primitive qui vous confère des capacités aux niveaux 3, 6, 10 et 14.

### Attaque supplémentaire (niveau 5)

Vous pouvez attaquer deux fois au lieu d'une lorsque vous utilisez l'action Attaquer.

### Déplacement rapide (niveau 5)

Votre vitesse augmente de 3 mètres tant que vous ne portez pas d'armure lourde.

### Instinct sauvage (niveau 7)

- Avantage aux jets d'initiative
- Si vous êtes surpris au début du combat et n'êtes pas neutralisé, vous pouvez agir normalement à votre premier tour si vous entrez en rage

### Critique brutal (niveau 9, 13, 17)

Vous lancez un dé de dégâts d'arme supplémentaire lors d'un coup critique :
- 1 dé au niveau 9
- 2 dés au niveau 13
- 3 dés au niveau 17

### Rage implacable (niveau 11)

Si vous tombez à 0 PV en rage sans être tué sur le coup, vous pouvez faire un jet de sauvegarde de Constitution DD 10 pour tomber à 1 PV à la place. Le DD augmente de 5 à chaque utilisation jusqu'à un repos long.

### Rage persistante (niveau 15)

Votre rage ne se termine que si vous êtes inconscient ou si vous choisissez de l'arrêter.

### Puissance indomptable (niveau 18)

Si votre total pour un jet de Force est inférieur à votre valeur de Force, vous pouvez utiliser cette valeur à la place.

### Champion primitif (niveau 20)

Votre Force et votre Constitution augmentent de 4. Votre maximum pour ces caractéristiques est désormais de 24. Vous pouvez entrer en rage un nombre illimité de fois.

---

## Sous-classes - Voies primitives

### Voie du Berserker

Le berserker canalise une rage brutale et dévastatrice, sacrifiant sa santé pour une puissance de combat accrue.

#### Frénésie (niveau 3)
Vous pouvez entrer en frénésie lorsque vous entrez en rage. Pendant votre frénésie, vous pouvez effectuer une attaque d'arme de corps à corps supplémentaire en action bonus à chaque tour. Quand la rage se termine, vous gagnez un niveau d'épuisement.

#### Rage aveugle (niveau 6)
Vous ne pouvez pas être charmé ou effrayé tant que vous êtes en rage. Si vous êtes déjà affecté par l'un de ces effets, il est suspendu pendant la rage.

#### Présence intimidante (niveau 10)
Vous pouvez utiliser votre action pour effrayer une créature à 9 mètres qui peut vous voir. Elle doit réussir un jet de sauvegarde de Sagesse (DD = 8 + bonus de maîtrise + modificateur de Charisme) ou être effrayée jusqu'à la fin de votre prochain tour. Vous pouvez prolonger l'effet à chaque tour suivant avec votre action.

#### Représailles (niveau 14)
Lorsqu'une créature à 1,5 mètre de vous vous inflige des dégâts, vous pouvez utiliser votre réaction pour effectuer une attaque d'arme de corps à corps contre elle.

---

### Voie du Guerrier totemique

Le guerrier totemique puise dans les esprits de la nature pour obtenir des pouvoirs surnaturels liés à des animaux totems.

#### Quêteur spirituel (niveau 3)
Vous gagnez la capacité de lancer [[Communication avec les animaux]] et [[Sens animal]] comme rituels.

#### Esprit totémique (niveau 3)
Choisissez un animal totem et gagnez sa capacité en rage :

**Aigle** : Les créatures ont un désavantage aux attaques d'opportunité contre vous. Vous pouvez utiliser l'action Foncer en action bonus.

**Loup** : Vos alliés ont l'avantage aux jets d'attaque de corps à corps contre les créatures à 1,5 mètre de vous.

**Ours** : Vous avez la résistance à tous les types de dégâts sauf psychiques.

#### Aspect de la bête (niveau 6)
Gagnez un avantage magique basé sur votre totem (actif en permanence) :

**Aigle** : Vous pouvez voir jusqu'à 1,5 km sans difficulté. La lumière faible n'impose pas de désavantage à vos jets de Perception.

**Loup** : Vous pouvez pister d'autres créatures pendant un voyage à rythme rapide, et vous pouvez vous déplacer discrètement à rythme normal.

**Ours** : Votre capacité de charge est doublée, et vous avez l'avantage aux jets de Force pour pousser, tirer, soulever ou briser des objets.

#### Marcheur spirituel (niveau 10)
Vous pouvez lancer [[Communion avec la nature]] comme rituel. Les esprits vous confèrent des informations sur le terrain environnant.

#### Lien totémique (niveau 14)
Capacités de combat améliorées selon votre totem :

**Aigle** : Vous gagnez une vitesse de vol égale à votre vitesse de marche en rage (vous tombez si vous terminez votre tour en l'air).

**Loup** : Vous pouvez utiliser une action bonus pour mettre à terre une créature de taille G ou moins lorsque vous la touchez avec une attaque de corps à corps.

**Ours** : En rage, toute créature à 1,5 mètre de vous hostile à vos alliés a un désavantage aux attaques contre d'autres cibles que vous.

---

### Voie de la Magie sauvage

Les barbares de la magie sauvage sont imprégnés de magie brute et chaotique qui se manifeste de façon imprévisible lorsqu'ils entrent en rage.

#### Perception magique (niveau 3)
Par une action, vous pouvez ouvrir votre conscience à la magie. Jusqu'à la fin de votre prochain tour, vous connaissez l'emplacement de tout sort ou objet magique dans un rayon de 18 mètres qui n'est pas derrière un abri total. Vous pouvez utiliser cette capacité un nombre de fois égal à votre bonus de maîtrise, et vous récupérez toutes les utilisations après un repos long.

#### Sursaut de magie sauvage (niveau 3)
Lorsque vous entrez en rage, lancez 1d8 sur la table des Sursauts de magie sauvage pour déterminer l'effet magique produit :

| d8 | Effet |
|----|-------|
| 1 | Des vrilles spectrales jaillissent de vous. Chaque créature de votre choix dans un rayon de 9 m doit réussir un jet de sauvegarde de Constitution ou subir 1d12 dégâts nécrotiques. Vous gagnez des PV temporaires égaux à 1d12 + niveau de barbare. |
| 2 | Vous vous téléportez jusqu'à 9 m dans un espace inoccupé visible. Jusqu'à la fin de votre rage, vous pouvez activer cet effet en action bonus à chaque tour. |
| 3 | Un esprit intangible apparaît dans un espace inoccupé à 1,5 m de vous. À la fin de ce tour et à chacun de vos tours suivants, l'esprit explose en une rafale de lumière. Chaque créature de votre choix dans un rayon de 1,5 m de l'esprit subit 1d6 dégâts radiants. |
| 4 | De la magie infuse votre arme. Jusqu'à la fin de votre rage, le type de dégâts de votre arme devient force, et elle gagne les propriétés lumière et lancer (portée 6/18 m). Elle revient dans votre main après l'attaque. |
| 5 | Chaque fois qu'une créature vous touche avec une attaque avant la fin de votre rage, elle subit 1d6 dégâts de force. |
| 6 | Jusqu'à la fin de votre rage, vous êtes entouré d'une lumière multicolore. Vous et toute créature de votre choix dans un rayon de 3 m avez un abri partiel. |
| 7 | Des fleurs et de la végétation poussent temporairement autour de vous. Le sol dans un rayon de 4,5 m devient un terrain difficile pour vos ennemis. |
| 8 | Un éclair de lumière jaillit de votre poitrine. Une créature de votre choix visible dans un rayon de 9 m doit réussir un jet de sauvegarde de Constitution ou subir 1d6 dégâts radiants et être aveugle jusqu'au début de votre prochain tour. |

#### Réserves magiques (niveau 6)
Par une action, vous pouvez toucher une créature (ou vous-même) et conférer l'un des bénéfices suivants :
- La créature peut lancer un dé et ajouter le résultat à son prochain jet d'attaque, de caractéristique ou de sauvegarde
- Lancez un dé. La créature regagne un emplacement de sort de niveau égal ou inférieur au résultat (max niveau 5)

Vous pouvez utiliser cette capacité un nombre de fois égal à votre bonus de maîtrise par repos long.

#### Réaction instable (niveau 10)
Lorsque vous subissez des dégâts en rage, vous pouvez utiliser votre réaction pour lancer sur la table des Sursauts de magie sauvage et produire immédiatement l'effet obtenu. Cet effet remplace l'effet en cours.

#### Sursaut contrôlé (niveau 14)
Lorsque vous lancez sur la table des Sursauts de magie sauvage, vous pouvez lancer deux fois et choisir le résultat. Si vous obtenez le même nombre sur les deux dés, vous pouvez ignorer le résultat et choisir n'importe quel effet de la table.
