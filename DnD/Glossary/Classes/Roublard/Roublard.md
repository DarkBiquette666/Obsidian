---
Class: Class

aliases:
  - Roublard
  - roublard
  - Rogue
tags:
  - classe
  - creation-personnage
hit_dice: d8
saving_throws:
  - dex
  - int
armor_proficiencies:
  - legeres
weapon_proficiencies:
  - courantes
  - arbalete de poing
  - epee courte
  - epee longue
  - rapiere
tool_proficiencies:
  - outils de voleur
skill_choices: 4
skill_options:
  - Acrobaties
  - Athletisme
  - Discretion
  - Escamotage
  - Intimidation
  - Intuition
  - Investigation
  - Perception
  - Persuasion
  - Representation
  - Tromperie
spellcasting_ability:
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "2d6"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "2d6"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
      - "3d6"
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "3d6"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
      - "4d6"
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "4d6"
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
      - "5d6"
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "5d6"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "6d6"
  - type: ClassLevelEntry
    level: 12
    proficiency_bonus: 4
    features:
      - "6d6"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 5
    features:
      - "7d6"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 5
    features:
      - "7d6"
  - type: ClassLevelEntry
    level: 15
    proficiency_bonus: 5
    features:
      - "8d6"
  - type: ClassLevelEntry
    level: 16
    proficiency_bonus: 5
    features:
      - "8d6"
  - type: ClassLevelEntry
    level: 17
    proficiency_bonus: 6
    features:
      - "9d6"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "9d6"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "10d6"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "10d6"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 3
    features:
      - "3"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 3
    features:
      - "4"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
      - "5"
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "6"
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "7"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "8"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 4
    features:
      - "9"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 4
    features:
      - "10"
  - type: ClassLevelEntry
    level: 16
    proficiency_bonus: 4
    features:
      - "11"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 4
    features:
      - "12"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 4
    features:
      - "13"
starting_equipment_draft: "- Une rapière OU une épée courte - Un arc court et un carquois de 20 flèches OU une épée courte - Un sac de cambrioleur OU un sac d'explorateur OU un sac de donjon - Une armure de cuir, deux dagues et des outils de voleur"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Rapière]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Épée courte]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: EquipmentGroup
        selection_mode: AND
        items:
          - type: SpecificItem
            item: "[[Arc court]]"
            quantity: 1
          - type: SpecificItem
            item: "[[Carquois]]"
            quantity: 1
          - type: SpecificItem
            item: "[[Flèches]]"
            quantity: 20
      - type: SpecificItem
        item: "[[Épée courte]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Sac de cambrioleur]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'explorateur]]"
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
      - type: SpecificItem
        item: "[[Dague]]"
        quantity: 2
      - type: SpecificItem
        item: "[[Outils de voleur]]"
        quantity: 1
---



# Roublard

Les roublards comptent sur leur compétence, leur discrétion et les faiblesses de leurs ennemis. Ces personnages polyvalents font preuve d'ingéniosité et d'adaptabilité qui sont la pierre angulaire de toute aventure réussie.

## Tableau de progression

| Niveau | Bonus | Attaque sournoise | Capacités |
|--------|-------|-------------------|-----------|
| 1 | +2 | 1d6 | Expertise, Attaque sournoise, Jargon des voleurs |
| 2 | +2 | 1d6 | Ruse |
| 3 | +2 | 2d6 | Archétype de roublard |
| 4 | +2 | 2d6 | Amélioration de caractéristiques |
| 5 | +3 | 3d6 | Esquive instinctive |
| 6 | +3 | 3d6 | Expertise |
| 7 | +3 | 4d6 | Esquive totale |
| 8 | +3 | 4d6 | Amélioration de caractéristiques |
| 9 | +4 | 5d6 | Capacité d'archétype |
| 10 | +4 | 5d6 | Amélioration de caractéristiques |
| 11 | +4 | 6d6 | Talent fiable |
| 12 | +4 | 6d6 | Amélioration de caractéristiques |
| 13 | +5 | 7d6 | Capacité d'archétype |
| 14 | +5 | 7d6 | Sens subtils |
| 15 | +5 | 8d6 | Esprit fuyant |
| 16 | +5 | 8d6 | Amélioration de caractéristiques |
| 17 | +6 | 9d6 | Capacité d'archétype |
| 18 | +6 | 9d6 | Insaisissable |
| 19 | +6 | 10d6 | Amélioration de caractéristiques |
| 20 | +6 | 10d6 | Coup de chance |

## Caractéristiques de classe

**Dés de vie** : 1d8 par niveau de roublard
**Points de vie au niveau 1** : 8 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d8 (ou 5) + modificateur de Constitution

### Maîtrises

- **Armures** : Armures légères
- **Armes** : Armes courantes, arbalète de poing, épée courte, épée longue, rapière
- **Outils** : Outils de voleur
- **Jets de sauvegarde** : Dextérité, Intelligence
- **Compétences** : Choisissez 4 parmi Acrobaties, Athlétisme, Discrétion, Escamotage, Intimidation, Intuition, Investigation, Perception, Persuasion, Représentation, Tromperie

### Équipement de départ

- Une rapière OU une épée courte
- Un arc court et un carquois de 20 flèches OU une épée courte
- Un sac de cambrioleur OU un sac d'explorateur OU un sac de donjon
- Une armure de cuir, deux dagues et des outils de voleur

---

## Capacités de classe

### Expertise (niveau 1)

Choisissez deux compétences que vous maîtrisez, ou une compétence que vous maîtrisez et les outils de voleur. Votre bonus de maîtrise est doublé pour tout jet de caractéristique que vous effectuez avec les choix sélectionnés.

Au niveau 6, vous pouvez choisir deux maîtrises supplémentaires (compétences ou outils de voleur) pour gagner ce bénéfice.

### Attaque sournoise (niveau 1)

Une fois par tour, vous pouvez infliger des dégâts supplémentaires à une créature que vous touchez avec une attaque si vous avez l'avantage au jet d'attaque. L'attaque doit utiliser une arme de finesse ou une arme à distance.

Vous n'avez pas besoin d'avoir l'avantage au jet d'attaque si un autre ennemi de la cible est à 1,5 mètre d'elle, si cet ennemi n'est pas neutralisé, et si vous n'avez pas un désavantage au jet d'attaque.

Les dégâts supplémentaires sont de 1d6 et augmentent selon votre niveau (voir tableau).

### Jargon des voleurs (niveau 1)

Au cours de votre formation de roublard, vous avez appris le jargon des voleurs, un mélange secret de dialecte, de jargon et de code qui vous permet de cacher des messages dans une conversation apparemment normale. Seule une autre créature qui connaît le jargon des voleurs comprend ces messages.

De plus, vous comprenez un ensemble de signes et de symboles secrets utilisés pour transmettre des messages courts et simples.

### Ruse (niveau 2)

Votre réflexion rapide et votre agilité vous permettent de vous déplacer et d'agir rapidement. Vous pouvez effectuer une action bonus à chacun de vos tours de combat. Cette action ne peut être utilisée que pour Se désengager, Se cacher ou Foncer.

### Archétype de roublard (niveau 3)

Choisissez un archétype qui vous confère des capacités aux niveaux 3, 9, 13 et 17.

### Amélioration de caractéristiques

Aux niveaux 4, 8, 10, 12, 16 et 19, vous pouvez augmenter une caractéristique de 2, ou deux caractéristiques de 1 chacune (maximum 20).

### Esquive instinctive (niveau 5)

Quand un attaquant que vous pouvez voir vous touche avec une attaque, vous pouvez utiliser votre réaction pour réduire de moitié les dégâts de cette attaque contre vous.

### Esquive totale (niveau 7)

Quand vous êtes soumis à un effet qui vous permet de faire un jet de sauvegarde de Dextérité pour ne subir que la moitié des dégâts, vous ne subissez aucun dégât en cas de réussite et la moitié en cas d'échec.

### Talent fiable (niveau 11)

Vous avez affiné vos compétences choisies jusqu'à la perfection. Chaque fois que vous effectuez un jet de caractéristique qui vous permet d'ajouter votre bonus de maîtrise, vous pouvez traiter un résultat de 9 ou moins sur le d20 comme un 10.

### Sens subtils (niveau 14)

Si vous pouvez entendre, vous êtes conscient de l'emplacement de toute créature invisible ou cachée à 3 mètres de vous.

### Esprit fuyant (niveau 15)

Vous gagnez la maîtrise des jets de sauvegarde de Sagesse.

### Insaisissable (niveau 18)

Vous êtes tellement évasif que les attaquants ont rarement le dessus sur vous. Aucun jet d'attaque n'a l'avantage contre vous tant que vous n'êtes pas neutralisé.

### Coup de chance (niveau 20)

Vous avez un talent étrange pour réussir quand vous en avez besoin. Si votre attaque rate une cible à portée, vous pouvez transformer le jet raté en un coup. Si vous échouez à un jet de caractéristique, vous pouvez traiter le résultat du d20 comme un 20.

**Utilisations** : 1 par repos court ou long

---

## Archétypes de roublard

### Voleur

Le voleur affine ses compétences dans les arts du larcin. Les cambrioleurs, les bandits, les coupeurs de bourse et autres criminels suivent généralement cet archétype.

#### Mains lestes (niveau 3)

Vous pouvez utiliser l'action bonus accordée par Ruse pour effectuer un jet de Dextérité (Escamotage), utiliser vos outils de voleur pour désarmer un piège ou crocheter une serrure, ou utiliser un objet.

#### Monte-en-l'air (niveau 3)

Vous gagnez la capacité d'escalader plus vite que la normale. L'escalade ne vous coûte plus de déplacement supplémentaire.

De plus, quand vous effectuez un saut en longueur avec élan, la distance que vous pouvez couvrir augmente d'un nombre de mètres égal à votre modificateur de Dextérité.

#### Discrétion suprême (niveau 9)

Vous avez l'avantage aux jets de Dextérité (Discrétion) si vous vous déplacez d'au plus la moitié de votre vitesse durant le même tour.

#### Utilisation des objets magiques (niveau 13)

Vous avez appris suffisamment de magie pour pouvoir utiliser des objets magiques que vous ne devriez normalement pas pouvoir utiliser. Vous ignorez toutes les conditions de classe, de race et de niveau pour l'utilisation des objets magiques.

#### Réflexes de voleur (niveau 17)

Vous êtes devenu adepte à tendre des embuscades et à vous échapper rapidement du danger. Vous pouvez effectuer deux tours pendant le premier round de tout combat. Vous effectuez votre premier tour à votre initiative normale et votre second tour à votre initiative moins 10.

Vous ne pouvez pas utiliser cette capacité si vous êtes surpris.

---

### Assassin

L'assassin se concentre sur l'art du meurtre. Les assassins incluent les tueurs à gages, les espions, les chasseurs de primes et même les prêtres spécialement consacrés.

#### Maîtrises supplémentaires (niveau 3)

Vous gagnez la maîtrise du kit de déguisement et du kit d'empoisonneur.

#### Assassinat (niveau 3)

Vous êtes plus mortel quand vous prenez vos ennemis par surprise. Vous avez l'avantage aux jets d'attaque contre toute créature qui n'a pas encore agi dans le combat.

De plus, tout coup que vous portez contre une créature surprise est un coup critique.

#### Expert en infiltration (niveau 9)

Vous pouvez créer de fausses identités de manière infaillible. Vous devez passer sept jours et 25 po pour établir l'histoire, la profession et les affiliations d'une identité. Vous ne pouvez pas établir une identité qui appartient à quelqu'un d'autre.

Ensuite, si vous adoptez la nouvelle identité comme déguisement, les autres créatures croient que vous êtes cette personne jusqu'à ce qu'elles aient une raison évidente de penser le contraire.

#### Imposteur (niveau 13)

Vous gagnez la capacité d'imiter de manière infaillible la parole, l'écriture et le comportement d'une autre personne. Vous devez passer au moins trois heures à étudier ces trois composantes du comportement de la personne, en l'écoutant parler, en examinant son écriture et en observant ses manières.

Votre ruse est indiscernable de la vraie personne. Pour discerner la supercherie, une créature doit réussir un jet de Sagesse (Intuition) contre votre DD de jet de caractéristique de Charisme (Tromperie).

#### Coup mortel (niveau 17)

Vous devenez un maître de la mort instantanée. Quand vous attaquez et touchez une créature qui est surprise, elle doit effectuer un jet de sauvegarde de Constitution (DD 8 + votre modificateur de Dextérité + votre bonus de maîtrise). En cas d'échec, doublez les dégâts de votre attaque contre la créature.

---

### Arnaqueur arcanique

L'arnaqueur arcanique améliore ses compétences de roublard avec de la magie, se spécialisant dans l'enchantement et l'illusion.

#### Incantation (niveau 3)

Vous gagnez la capacité de lancer des sorts de magicien.

**Caractéristique d'incantation** : Intelligence
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur d'Intelligence
**Modificateur d'attaque** : bonus de maîtrise + modificateur d'Intelligence

**Sorts mineurs** : Vous apprenez *main de mage* et deux autres sorts mineurs de magicien de votre choix.

**Sorts connus** : Vous apprenez trois sorts de magicien de niveau 1. Deux de ces sorts doivent être des sorts d'enchantement ou d'illusion. Vous apprenez des sorts supplémentaires selon le tableau ci-dessous.

| Niveau | Sorts mineurs | Sorts connus | Emplacements | Niveau max |
|--------|---------------|--------------|--------------|------------|
| 3 | 3 | 3 | 2 | 1er |
| 4 | 3 | 4 | 3 | 1er |
| 7 | 3 | 5 | 4/2 | 2e |
| 8 | 3 | 6 | 4/2 | 2e |
| 10 | 4 | 7 | 4/3 | 2e |
| 11 | 4 | 8 | 4/3 | 2e |
| 13 | 4 | 9 | 4/3/2 | 3e |
| 14 | 4 | 10 | 4/3/2 | 3e |
| 16 | 4 | 11 | 4/3/3 | 3e |
| 19 | 4 | 12 | 4/3/3/1 | 4e |
| 20 | 4 | 13 | 4/3/3/1 | 4e |

#### Main de mage améliorée (niveau 3)

Quand vous lancez *main de mage*, vous pouvez rendre la main spectrale invisible. Vous pouvez effectuer les tâches supplémentaires suivantes avec elle :

- Déposer un objet dans un conteneur porté ou tenu par une autre créature
- Récupérer un objet dans un conteneur porté ou tenu par une autre créature
- Utiliser des outils de voleur pour crocheter des serrures et désarmer des pièges à distance

Vous pouvez effectuer l'une de ces tâches sans être remarqué par une créature si vous réussissez un jet de Dextérité (Escamotage) contre le jet de Sagesse (Perception) de la créature.

De plus, vous pouvez utiliser l'action bonus accordée par Ruse pour contrôler la main.

#### Embuscade magique (niveau 9)

Si vous êtes caché d'une créature quand vous lancez un sort sur elle, la créature a un désavantage à tout jet de sauvegarde qu'elle effectue contre le sort ce tour.

#### Voleur de sorts polyvalent (niveau 13)

Vous gagnez la capacité de voler la connaissance de la manière de lancer un sort à une autre créature.

Immédiatement après qu'une créature lance un sort qui vous cible ou vous inclut dans sa zone d'effet, vous pouvez utiliser votre réaction pour forcer la créature à effectuer un jet de sauvegarde avec sa caractéristique d'incantation de sort contre votre DD de sauvegarde de sort. En cas d'échec, vous annulez l'effet du sort sur vous, et vous volez la connaissance du sort si c'est au moins un sort de niveau 1 et d'un niveau que vous pouvez lancer (pas nécessairement un sort de magicien).

Pendant les 8 heures suivantes, vous connaissez le sort et pouvez le lancer en utilisant vos emplacements de sorts. La créature ne peut pas lancer ce sort jusqu'à ce que les 8 heures soient passées.

**Utilisations** : 1 par repos long

#### Filou des sorts (niveau 17)

Vous gagnez la capacité d'effectuer des attaques sournoises avec vos sorts. Une fois par tour, quand vous lancez un sort qui nécessite un jet d'attaque et touchez une créature, vous pouvez infliger des dégâts d'Attaque sournoise supplémentaires à cette créature.

---

### Cerveau

Le cerveau excelle dans la manipulation et les tactiques de groupe, orchestrant les combats depuis l'arrière.

#### Maître tacticien (niveau 3)

Vous pouvez utiliser l'action Aider en action bonus. De plus, quand vous utilisez l'action Aider pour aider un allié à attaquer une créature, la cible de cette attaque peut être à 9 mètres de vous au lieu de 1,5 mètre, si la cible peut vous voir ou vous entendre.

#### Maître manipulateur (niveau 3)

Vous gagnez la maîtrise de deux langues de votre choix.

De plus, vous pouvez imiter infailliblement les accents et les modes de parole d'une créature que vous avez entendu parler pendant au moins 1 minute. Une créature peut discerner l'imitation en réussissant un jet de Sagesse (Intuition) contre votre jet de Charisme (Tromperie).

#### Perspicace (niveau 9)

Si vous passez au moins 1 minute à observer ou interagir avec une créature en dehors du combat, vous pouvez apprendre certaines informations sur ses capacités comparées aux vôtres. Le MD vous dit si la créature est supérieure, égale ou inférieure à vous concernant deux des caractéristiques suivantes de votre choix :

- Valeur d'Intelligence
- Valeur de Sagesse
- Valeur de Charisme
- Niveaux de classe (le cas échéant)

À la discrétion du MD, vous pouvez également réaliser un trait de personnalité, un idéal, un défaut ou un lien de la créature.

#### Mauvaise direction (niveau 13)

Quand vous êtes la cible d'une attaque par une créature que vous pouvez voir, vous pouvez utiliser votre réaction pour choisir une autre créature à 1,5 mètre de vous (autre que l'attaquant). Vous changez de place avec cette créature et elle devient la cible de l'attaque à la place.

#### Âme de la tromperie (niveau 17)

Vos pensées ne peuvent pas être lues par télépathie ou autres moyens, sauf si vous le permettez. Vous pouvez présenter de fausses pensées en effectuant un jet de Charisme (Tromperie) contre le jet de Sagesse (Intuition) du lecteur de pensées.

De plus, quel que soit ce que vous dites, la magie qui déterminerait si vous dites la vérité indique que vous dites la vérité si vous le choisissez, et vous ne pouvez pas être contraint de dire la vérité par la magie.

---

### Fantôme

Le fantôme se déplace entre la vie et la mort, puisant dans les énergies du néant.

#### Murmures des morts (niveau 3)

Vous pouvez parler aux esprits des morts. Quand vous terminez un repos court ou long, vous pouvez poser une question à un esprit et recevoir une réponse brève et cryptique.

#### Trait d'agonie (niveau 3)

Immédiatement après qu'une créature à 9 mètres de vous soit réduite à 0 points de vie, vous gagnez un certain nombre de capacités basées sur la créature morte. Cette capacité dure jusqu'à ce que vous utilisiez cette capacité à nouveau ou terminiez un repos court ou long.

Vous pouvez utiliser l'un des traits suivants :
- Une compétence ou un outil que la créature maîtrisait
- Une langue que la créature connaissait
- La vitesse de déplacement de la créature (si différente de la vôtre)

#### Marche des esprits (niveau 9)

Par une action bonus, vous pouvez prendre une forme spectrale. Dans cette forme, vous avez une vitesse de vol de 3 mètres, vous pouvez planer, et les jets d'attaque contre vous ont un désavantage. Vous pouvez également vous déplacer à travers les créatures et les objets comme s'ils étaient du terrain difficile.

**Durée** : 10 minutes ou jusqu'à ce que vous l'annuliez
**Utilisations** : bonus de maîtrise par repos long

#### Jeton de mort (niveau 13)

Quand une vie se termine en votre présence, vous pouvez capturer une partie de cette énergie. Quand une créature que vous pouvez voir meurt à 9 mètres de vous, vous gagnez un jeton (maximum égal à votre bonus de maîtrise).

Vous pouvez dépenser un jeton pour :
- Lancer *représentation mineure* ou *communication avec les morts* sans composantes
- Poser une question supplémentaire à un esprit
- Gagner l'avantage à un jet d'attaque ou de sauvegarde

#### Présence fantomale (niveau 17)

Vous pouvez vous projeter partiellement dans le plan des morts. Par une action, vous devenez intangible pendant 10 minutes :
- Résistance à tous les dégâts sauf force
- Vous pouvez vous déplacer à travers les créatures et objets solides
- Si vous terminez votre tour à l'intérieur d'un objet, vous êtes éjecté et subissez 1d10 dégâts de force

**Utilisations** : 1 par repos long
