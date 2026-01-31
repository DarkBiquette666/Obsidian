---
Class: Class

aliases:
  - Guerrier
  - guerrier
  - Fighter
tags:
  - classe
  - creation-personnage
hit_dice: d10
saving_throws:
  - for
  - con
armor_proficiencies:
  - legeres
  - intermediaires
  - lourdes
  - boucliers
weapon_proficiencies:
  - courantes
  - guerre
tool_proficiencies: []
skill_choices: 2
skill_options:
  - Acrobaties
  - Athletisme
  - Dressage
  - Histoire
  - Intimidation
  - Intuition
  - Perception
  - Survie
spellcasting_ability:
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Style de combat"
      - "Second souffle"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Fougue (1)"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "Archétype martial"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
      - "Attaque supplémentaire (1)"
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "Amélioration de caractéristiques"
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
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
      - "Inflexible (1)"
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "Capacité d'archétype"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "Attaque supplémentaire (2)"
  - type: ClassLevelEntry
    level: 12
    proficiency_bonus: 4
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 5
    features:
      - "Inflexible (2)"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 5
    features:
      - "Amélioration de caractéristiques"
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
      - "Fougue (2)"
      - "Inflexible (3)"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "Capacité d'archétype"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Attaque supplémentaire (3)"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "3"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "4"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 2
    features:
      - "5"
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 2
    features:
      - "6"
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 3
    features:
      - "7"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 3
    features:
      - "8"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 3
    features:
      - "9"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 3
    features:
      - "10"
  - type: ClassLevelEntry
    level: 16
    proficiency_bonus: 3
    features:
      - "11"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 3
    features:
      - "12"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 3
    features:
      - "13"
starting_equipment_draft: "- Une cotte de mailles OU une armure de cuir, un arc long et 20 flèches - Une arme de guerre et un bouclier OU deux armes de guerre - Une arbalète légère et 20 carreaux OU deux hachettes - Un sac d'explorateur OU un sac de donjon"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: EquipmentGroup
        selection_mode: AND
        items:
          - type: SpecificItem
            item: "[[Cotte de mailles]]"
            quantity: 1
          - type: SpecificItem
            item: "[[Arc long]]"
            quantity: 1
          - type: SpecificItem
            item: "[[Flèches]]"
            quantity: 20
      - type: EquipmentGroup
        selection_mode: AND
        items:
          - type: SpecificItem
            item: "[[Armure de cuir]]"
            quantity: 1
          - type: SpecificItem
            item: "[[Arc long]]"
            quantity: 1
          - type: SpecificItem
            item: "[[Flèches]]"
            quantity: 20
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: EquipmentGroup
        selection_mode: AND
        items:
          - type: CategoryItem
            category: "Arme de guerre"
            quantity: 1
          - type: SpecificItem
            item: "[[Bouclier]]"
            quantity: 1
      - type: CategoryItem
        category: "Arme de guerre"
        quantity: 2
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
      - type: SpecificItem
        item: "[[Hachette]]"
        quantity: 2
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Sac d'explorateur]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'exploration souterraine]]"
        quantity: 1
---



# Guerrier

Le guerrier est la classe de personnage la plus diversifiée avec une maîtrise des armes, armures et tactiques de combat. Les guerriers sont des combattants entraînés : vétérans militaires, chevaliers, gardes du corps et officiers qui excellent sur les champs de bataille.

## Tableau de progression

| Niveau | Bonus | Capacités | Attaques |
|--------|-------|-----------|----------|
| 1 | +2 | Style de combat, Second souffle | 1 |
| 2 | +2 | Fougue (1) | 1 |
| 3 | +2 | Archétype martial | 1 |
| 4 | +2 | Amélioration de caractéristiques | 1 |
| 5 | +3 | Attaque supplémentaire (1) | 2 |
| 6 | +3 | Amélioration de caractéristiques | 2 |
| 7 | +3 | Capacité d'archétype | 2 |
| 8 | +3 | Amélioration de caractéristiques | 2 |
| 9 | +4 | Inflexible (1) | 2 |
| 10 | +4 | Capacité d'archétype | 2 |
| 11 | +4 | Attaque supplémentaire (2) | 3 |
| 12 | +4 | Amélioration de caractéristiques | 3 |
| 13 | +5 | Inflexible (2) | 3 |
| 14 | +5 | Amélioration de caractéristiques | 3 |
| 15 | +5 | Capacité d'archétype | 3 |
| 16 | +5 | Amélioration de caractéristiques | 3 |
| 17 | +6 | Fougue (2), Inflexible (3) | 3 |
| 18 | +6 | Capacité d'archétype | 3 |
| 19 | +6 | Amélioration de caractéristiques | 3 |
| 20 | +6 | Attaque supplémentaire (3) | 4 |

## Caractéristiques de classe

**Dés de vie** : 1d10 par niveau de guerrier
**Points de vie au niveau 1** : 10 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d10 (ou 6) + modificateur de Constitution

### Maîtrises

- **Armures** : Toutes les armures, boucliers
- **Armes** : Armes courantes, armes de guerre
- **Outils** : Aucun
- **Jets de sauvegarde** : Force, Constitution
- **Compétences** : Choisissez 2 parmi Acrobaties, Athlétisme, Dressage, Histoire, Intimidation, Intuition, Perception, Survie

### Équipement de départ

- Une cotte de mailles OU une armure de cuir, un arc long et 20 flèches
- Une arme de guerre et un bouclier OU deux armes de guerre
- Une arbalète légère et 20 carreaux OU deux hachettes
- Un sac d'explorateur OU un sac de donjon

---

## Capacités de classe

### Style de combat (niveau 1)

Choisissez un style de combat :

- **Archerie** : +2 aux jets d'attaque avec des armes à distance
- **Arme à deux mains** : Relancez les 1 et 2 sur les dés de dégâts des armes à deux mains
- **Combat à deux armes** : Ajoutez votre modificateur de caractéristique aux dégâts de la seconde attaque
- **Défense** : +1 à la CA tant que vous portez une armure
- **Duel** : +2 aux dégâts quand vous maniez une arme de corps à corps à une main et aucune autre arme
- **Protection** : Quand une créature attaque une cible autre que vous à 1,5 m, utilisez votre réaction pour imposer un désavantage (nécessite un bouclier)

### Second souffle (niveau 1)

Vous possédez une réserve limitée d'endurance. À votre tour, vous pouvez utiliser une action bonus pour regagner un nombre de points de vie égal à 1d10 + votre niveau de guerrier.

**Utilisations** : 1 par repos court ou long

### Fougue (niveau 2)

À votre tour, vous pouvez effectuer une action supplémentaire en plus de votre action normale et de votre éventuelle action bonus. Une fois cette capacité utilisée, vous devez terminer un repos court ou long pour la réutiliser.

À partir du niveau 17, vous pouvez l'utiliser deux fois avant un repos, mais une seule fois par tour.

### Archétype martial (niveau 3)

Choisissez un archétype qui vous confère des capacités aux niveaux 3, 7, 10, 15 et 18.

### Amélioration de caractéristiques

Aux niveaux 4, 6, 8, 12, 14, 16 et 19, vous pouvez augmenter une caractéristique de 2, ou deux caractéristiques de 1 chacune (maximum 20).

### Attaque supplémentaire (niveau 5)

Vous pouvez attaquer deux fois au lieu d'une quand vous utilisez l'action Attaquer. Le nombre d'attaques passe à trois au niveau 11, et à quatre au niveau 20.

### Inflexible (niveau 9)

Vous pouvez relancer un jet de sauvegarde que vous avez raté. Si vous le faites, vous devez utiliser le nouveau résultat.

**Utilisations** : 1 par repos long (2 au niveau 13, 3 au niveau 17)

---

## Archétypes martiaux

### Champion

Le champion se concentre sur le développement de la puissance physique brute pour porter des coups dévastateurs.

#### Critique amélioré (niveau 3)

Vos attaques avec des armes infligent un coup critique sur un résultat de 19 ou 20.

#### Athlète accompli (niveau 7)

Vous pouvez ajouter la moitié de votre bonus de maîtrise (arrondi à l'inférieur) à tout jet de Force, de Dextérité ou de Constitution que vous effectuez et qui n'utilise pas déjà votre bonus de maîtrise.

De plus, quand vous effectuez un saut en longueur avec élan, la distance que vous pouvez couvrir augmente d'un nombre de mètres égal à votre modificateur de Force.

#### Style de combat supplémentaire (niveau 10)

Choisissez un second style de combat parmi ceux disponibles.

#### Critique supérieur (niveau 15)

Vos attaques avec des armes infligent un coup critique sur un résultat de 18, 19 ou 20.

#### Survivant (niveau 18)

Au début de chacun de vos tours, vous regagnez un nombre de points de vie égal à 5 + votre modificateur de Constitution si vous avez au plus la moitié de vos points de vie maximum. Vous ne gagnez pas ce bénéfice si vous avez 0 points de vie.

---

### Maître de bataille

Le maître de bataille est un expert tactique qui utilise des manoeuvres de supériorité pour dominer ses adversaires.

#### Supériorité martiale (niveau 3)

Vous apprenez des manoeuvres alimentées par des dés spéciaux appelés dés de supériorité.

**Dés de supériorité** : Vous avez quatre dés de supériorité (d8). Vous en gagnez un supplémentaire aux niveaux 7 et 15. Ils deviennent des d10 au niveau 10 et des d12 au niveau 18. Vous les récupérez après un repos court ou long.

**Manoeuvres** : Vous apprenez trois manoeuvres de votre choix. Vous en apprenez deux supplémentaires aux niveaux 7, 10 et 15.

**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Force ou de Dextérité (votre choix)

#### Liste des manoeuvres

| Manoeuvre | Description |
|-----------|-------------|
| **Attaque menaçante** | Quand vous touchez, ajoutez le dé aux dégâts. La cible doit réussir un jet de sauvegarde de Sagesse ou être effrayée jusqu'à la fin de votre prochain tour. |
| **Attaque de balayage** | Quand vous touchez, si une autre créature est à 1,5 m et à portée, elle subit les dégâts du dé de supériorité. |
| **Attaque de croc-en-jambe** | Quand vous touchez, ajoutez le dé aux dégâts. Si la cible est de taille G ou moins, elle doit réussir un jet de sauvegarde de Force ou être mise à terre. |
| **Attaque de désarmement** | Quand vous touchez, ajoutez le dé aux dégâts. La cible doit réussir un jet de sauvegarde de Force ou lâcher un objet de votre choix qui tombe à ses pieds. |
| **Attaque de diversion** | Quand vous touchez, ajoutez le dé aux dégâts. Le prochain jet d'attaque contre la cible avant le début de votre prochain tour a l'avantage. |
| **Attaque de feinte** | Par une action bonus, désignez une créature à 1,5 m. Vous avez l'avantage à votre prochain jet d'attaque ce tour. Si vous touchez, ajoutez le dé aux dégâts. |
| **Attaque de fente** | Quand vous attaquez avec une arme de corps à corps, augmentez votre allonge de 1,5 m pour cette attaque. Si vous touchez, ajoutez le dé aux dégâts. |
| **Attaque de provocation** | Quand vous touchez, ajoutez le dé aux dégâts. La cible doit réussir un jet de sauvegarde de Sagesse ou avoir un désavantage à tous les jets d'attaque contre des cibles autres que vous jusqu'à la fin de votre prochain tour. |
| **Attaque de repousser** | Quand vous touchez, ajoutez le dé aux dégâts. Si la cible est de taille G ou moins, elle doit réussir un jet de sauvegarde de Force ou être repoussée de 4,5 mètres. |
| **Attaque précisée** | Quand vous effectuez un jet d'attaque, ajoutez le dé de supériorité au résultat. Vous pouvez utiliser cette manoeuvre avant ou après avoir lancé le dé, mais avant de connaître le résultat. |
| **Instruction** | Renoncez à une de vos attaques pour permettre à un allié à 9 m d'utiliser sa réaction pour effectuer une attaque d'arme, en ajoutant le dé aux dégâts. |
| **Jeu de jambes défensif** | Quand vous vous déplacez, ajoutez le dé de supériorité à votre CA jusqu'à la fin du déplacement. |
| **Manoeuvre tactique** | Quand vous touchez, ajoutez le dé aux dégâts. Vous permettez à un allié de se déplacer de la moitié de sa vitesse par sa réaction sans provoquer d'attaque d'opportunité de la cible. |
| **Parade** | Quand vous êtes touché par une attaque de corps à corps, utilisez votre réaction pour réduire les dégâts du résultat du dé + votre modificateur de Dextérité. |
| **Regain** | Par une action bonus, un allié à 18 m gagne des points de vie temporaires égaux au dé + votre modificateur de Charisme. |
| **Riposte** | Quand une créature rate une attaque de corps à corps contre vous, utilisez votre réaction pour effectuer une attaque de corps à corps contre elle. Si vous touchez, ajoutez le dé aux dégâts. |

#### Étudiant de la guerre (niveau 3)

Vous gagnez la maîtrise d'un type d'outils d'artisan de votre choix.

#### Observation de l'ennemi (niveau 7)

Si vous passez au moins 1 minute à observer ou interagir avec une créature en dehors d'un combat, vous pouvez apprendre certaines informations sur ses capacités comparées aux vôtres. Le MD vous dit si la créature est supérieure, égale ou inférieure à vous concernant deux des caractéristiques suivantes de votre choix :

- Valeur de Force
- Valeur de Dextérité
- Valeur de Constitution
- Classe d'armure
- Points de vie actuels
- Niveaux de classe totaux (le cas échéant)
- Niveaux de guerrier (le cas échéant)

#### Supériorité martiale améliorée (niveau 10)

Vos dés de supériorité deviennent des d10.

#### Implacable (niveau 15)

Quand vous lancez l'initiative et n'avez plus de dés de supériorité, vous en regagnez un.

#### Supériorité martiale supérieure (niveau 18)

Vos dés de supériorité deviennent des d12.

---

### Chevalier occulte

Le chevalier occulte combine entraînement martial et magie arcanique, spécialisé dans l'abjuration et l'évocation.

#### Incantation (niveau 3)

Vous apprenez à lancer des sorts de magicien.

**Caractéristique d'incantation** : Intelligence
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur d'Intelligence
**Modificateur d'attaque** : bonus de maîtrise + modificateur d'Intelligence

**Sorts mineurs connus** : 2 (un 3e au niveau 10)
**Sorts connus** : Voir tableau ci-dessous. Les sorts de niveau 1-2 doivent être d'Abjuration ou d'Évocation, sauf un sort "libre" à chaque palier.

| Niveau | Sorts mineurs | Sorts connus | Emplacements | Niveau max |
|--------|---------------|--------------|--------------|------------|
| 3 | 2 | 3 | 2 | 1er |
| 4 | 2 | 4 | 3 | 1er |
| 7 | 2 | 5 | 4/2 | 2e |
| 8 | 2 | 6 | 4/2 | 2e |
| 10 | 3 | 7 | 4/3 | 2e |
| 11 | 3 | 8 | 4/3 | 2e |
| 13 | 3 | 9 | 4/3/2 | 3e |
| 14 | 3 | 10 | 4/3/2 | 3e |
| 16 | 3 | 11 | 4/3/3 | 3e |
| 19 | 3 | 12 | 4/3/3/1 | 4e |
| 20 | 3 | 13 | 4/3/3/1 | 4e |

#### Lien d'arme (niveau 3)

Après un rituel d'1 heure, vous pouvez lier une arme à vous. Vous ne pouvez pas être désarmé de cette arme et vous pouvez l'invoquer dans votre main par une action bonus. Vous pouvez avoir jusqu'à deux armes liées.

#### Magie de guerre (niveau 7)

Quand vous utilisez votre action pour lancer un sort mineur, vous pouvez effectuer une attaque d'arme en action bonus.

#### Frappe occulte (niveau 10)

Quand vous touchez une créature avec une attaque d'arme, cette créature a un désavantage au prochain jet de sauvegarde qu'elle effectue contre un sort que vous lancez avant la fin de votre prochain tour.

#### Charge arcanique (niveau 15)

Quand vous utilisez Fougue, vous pouvez vous téléporter de 9 mètres avant ou après l'action supplémentaire.

#### Magie de guerre améliorée (niveau 18)

Quand vous utilisez votre action pour lancer un sort (pas seulement un sort mineur), vous pouvez effectuer une attaque d'arme en action bonus.

---

### Cavalier

Le cavalier excelle dans le combat monté et la protection de ses alliés.

#### Don supplémentaire (niveau 3)

Vous gagnez la maîtrise d'une des compétences suivantes : Dressage, Histoire, Intuition, Représentation ou Persuasion. Vous pouvez également apprendre une langue de votre choix.

#### Marque indélébile (niveau 3)

Par une action bonus, vous pouvez marquer une créature à 1,5 m. Jusqu'à la fin de votre prochain tour, vous infligez 1d8 dégâts supplémentaires à la cible quand vous la touchez, et elle a un désavantage à tout jet d'attaque contre une cible autre que vous.

#### Protection montée (niveau 7)

Quand votre monture est ciblée par une attaque, vous pouvez la rediriger vers vous.

De plus, si votre monture est soumise à un effet qui lui permet un jet de sauvegarde pour subir seulement la moitié des dégâts, elle ne subit aucun dégât en cas de réussite.

#### Cavalier inflexible (niveau 10)

Vous pouvez choisir de descendre sur vos pieds si vous êtes mis à terre en étant monté. De plus, si vous tombez de moins de 3 mètres, vous atterrissez sur vos pieds.

#### Défenseur vigilant (niveau 15)

Vous avez l'avantage aux jets de sauvegarde contre le fait d'être charmé, effrayé, neutralisé, paralysé ou étourdi.

De plus, quand une créature à 1,5 m effectue un jet d'attaque contre une cible autre que vous, vous pouvez utiliser votre réaction pour imposer un désavantage au jet.

#### Gardien puissant (niveau 18)

Quand une créature à 1,5 m est touchée par une attaque, vous pouvez utiliser votre réaction pour échanger vos PV actuels avec ceux de cette créature.

---

### Samouraï

Le samouraï est un guerrier d'une discipline inégalée qui peut puiser dans une détermination sans faille.

#### Don supplémentaire (niveau 3)

Vous gagnez la maîtrise d'une des compétences suivantes : Histoire, Intuition, Représentation ou Persuasion. Vous pouvez également apprendre une langue de votre choix.

#### Esprit combatif (niveau 3)

Par une action bonus, vous gagnez l'avantage aux jets d'attaque d'arme jusqu'à la fin de votre tour. Vous gagnez également 5 points de vie temporaires (augmente à 10 au niveau 10, 15 au niveau 15).

**Utilisations** : 3 par repos long

#### Courtisan élégant (niveau 7)

Vous ajoutez votre modificateur de Sagesse aux jets de Charisme (Persuasion). Vous gagnez également la maîtrise des jets de sauvegarde de Sagesse. Si vous avez déjà cette maîtrise, vous gagnez la maîtrise des jets de sauvegarde d'Intelligence ou de Charisme (votre choix).

#### Esprit indomptable (niveau 10)

Quand vous effectuez un jet de sauvegarde d'Intelligence, de Sagesse ou de Charisme et échouez, vous pouvez le relancer et devez utiliser le nouveau résultat.

**Utilisations** : 1 par repos long (2 au niveau 15, 3 au niveau 18)

#### Frappe rapide (niveau 15)

Si vous utilisez Esprit combatif et effectuez l'action Attaquer durant votre tour, vous pouvez effectuer une attaque d'arme supplémentaire en action bonus.

#### Force avant la mort (niveau 18)

Si vous êtes réduit à 0 points de vie, vous pouvez retarder votre chute inconsciente et prendre immédiatement un tour supplémentaire. Si vous subissez des dégâts durant ce tour supplémentaire, vous subissez normalement les échecs de jet de sauvegarde contre la mort. Vous tombez inconscient à la fin de ce tour supplémentaire.

**Utilisations** : 1 par repos long
