---
Class: Class

aliases:
  - Moine
  - moine
  - Monk
tags:
  - classe
  - creation-personnage
hit_dice: d8
saving_throws:
  - for
  - dex
armor_proficiencies: []
weapon_proficiencies:
  - courantes
  - epee courte
tool_proficiencies: []
skill_choices: 2
skill_options:
  - Acrobaties
  - Athletisme
  - Discretion
  - Histoire
  - Intuition
  - Religion
spellcasting_ability:
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "1d4"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "1d4"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "1d4"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "1d4"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "1d6"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "1d8"
  - type: ClassLevelEntry
    level: 12
    proficiency_bonus: 4
    features:
      - "1d8"
  - type: ClassLevelEntry
    level: 13
    proficiency_bonus: 5
    features:
      - "1d8"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 5
    features:
      - "1d8"
  - type: ClassLevelEntry
    level: 15
    proficiency_bonus: 5
    features:
      - "1d8"
  - type: ClassLevelEntry
    level: 16
    proficiency_bonus: 5
    features:
      - "1d8"
  - type: ClassLevelEntry
    level: 17
    proficiency_bonus: 6
    features:
      - "1d10"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "1d10"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "1d10"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "1d10"
starting_equipment_draft: "- Une épée courte OU une arme courante - Un sac de donjon OU un sac d'explorateur - 10 fléchettes"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Épée courte]]"
        quantity: 1
      - type: CategoryItem
        category: "Arme courante"
        quantity: 1
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
        item: "[[Fléchette]]"
        quantity: 10
---



# Moine

Les moines exploitent une énergie magique appelée ki pour accomplir des prouesses martiales exceptionnelles. Ils recherchent la perfection de l'être grâce à la contemplation et à un entraînement rigoureux dans des monastères disséminés à travers les mondes.

## Tableau de progression

| Niveau | Bonus | Arts martiaux | Ki | Déplacement | Capacités |
|--------|-------|---------------|-----|-------------|-----------|
| 1 | +2 | 1d4 | - | - | Défense sans armure, Arts martiaux |
| 2 | +2 | 1d4 | 2 | +3m | Ki, Déplacement sans armure |
| 3 | +2 | 1d4 | 3 | +3m | Tradition monastique, Parade de projectiles |
| 4 | +2 | 1d4 | 4 | +3m | Amélioration, Chute ralentie |
| 5 | +3 | 1d6 | 5 | +3m | Attaque supplémentaire, Frappe étourdissante |
| 6 | +3 | 1d6 | 6 | +4,5m | Frappes de ki, Capacité de tradition |
| 7 | +3 | 1d6 | 7 | +4,5m | Esquive totale, Sérénité |
| 8 | +3 | 1d6 | 8 | +4,5m | Amélioration de caractéristiques |
| 9 | +4 | 1d6 | 9 | +4,5m | Déplacement sans armure amélioré |
| 10 | +4 | 1d6 | 10 | +6m | Pureté physique |
| 11 | +4 | 1d8 | 11 | +6m | Capacité de tradition |
| 12 | +4 | 1d8 | 12 | +6m | Amélioration de caractéristiques |
| 13 | +5 | 1d8 | 13 | +6m | Langue du soleil et de la lune |
| 14 | +5 | 1d8 | 14 | +7,5m | Âme de diamant |
| 15 | +5 | 1d8 | 15 | +7,5m | Jeunesse éternelle |
| 16 | +5 | 1d8 | 16 | +7,5m | Amélioration de caractéristiques |
| 17 | +6 | 1d10 | 17 | +7,5m | Capacité de tradition |
| 18 | +6 | 1d10 | 18 | +9m | Désertion de l'âme |
| 19 | +6 | 1d10 | 19 | +9m | Amélioration de caractéristiques |
| 20 | +6 | 1d10 | 20 | +9m | Perfection de l'être |

## Caractéristiques de classe

**Dés de vie** : 1d8 par niveau de moine
**Points de vie au niveau 1** : 8 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d8 (ou 5) + modificateur de Constitution

### Maîtrises

- **Armures** : Aucune
- **Armes** : Armes courantes, épées courtes
- **Outils** : Un type d'outil d'artisan ou un instrument de musique
- **Jets de sauvegarde** : Force, Dextérité
- **Compétences** : Choisissez 2 parmi Acrobaties, Athlétisme, Discrétion, Histoire, Intuition, Religion

### Équipement de départ

- Une épée courte OU une arme courante
- Un sac de donjon OU un sac d'explorateur
- 10 fléchettes

---

## Capacités de classe

### Défense sans armure (niveau 1)

Tant que vous ne portez ni armure ni bouclier, votre CA = 10 + modificateur de Dextérité + modificateur de Sagesse.

### Arts martiaux (niveau 1)

Vous maîtrisez les techniques de combat à mains nues et avec les armes de moine (armes courantes sans propriété lourde ou à deux mains, plus l'épée courte).

- Vous pouvez utiliser la Dextérité au lieu de la Force pour les jets d'attaque et de dégâts à mains nues ou avec une arme de moine
- Vous pouvez lancer votre dé d'Arts martiaux (voir tableau) au lieu des dégâts normaux
- Lorsque vous utilisez l'action Attaquer avec une attaque à mains nues ou une arme de moine, vous pouvez effectuer une attaque à mains nues en action bonus

### Ki (niveau 2)

Vous avez accès à l'énergie mystique du ki. Votre nombre de points de ki est égal à votre niveau de moine. Vous récupérez tous vos points de ki après un repos court ou long.

**DD de sauvegarde du ki** : 8 + bonus de maîtrise + modificateur de Sagesse

#### Utilisations du ki

**Déluge de coups (1 ki)** : Immédiatement après avoir utilisé l'action Attaquer, vous pouvez effectuer deux attaques à mains nues en action bonus.

**Défense patiente (1 ki)** : Vous pouvez utiliser l'action Esquiver en action bonus.

**Déplacement aérien (1 ki)** : Vous pouvez utiliser l'action Se désengager ou Foncer en action bonus, et votre distance de saut est doublée pour ce tour.

### Déplacement sans armure (niveau 2)

Votre vitesse augmente tant que vous ne portez ni armure ni bouclier. L'augmentation est indiquée dans le tableau de progression.

À partir du niveau 9, vous pouvez vous déplacer sur les surfaces verticales et sur les liquides sans tomber pendant votre déplacement.

### Tradition monastique (niveau 3)

Choisissez une tradition monastique qui vous confère des capacités aux niveaux 3, 6, 11 et 17.

### Parade de projectiles (niveau 3)

Vous pouvez utiliser votre réaction pour dévier un projectile lorsque vous êtes touché par une attaque à distance. Les dégâts sont réduits de 1d10 + modificateur de Dextérité + niveau de moine.

Si les dégâts sont réduits à 0, vous pouvez attraper le projectile. Si vous l'attrapez et avez une main libre, vous pouvez dépenser 1 point de ki pour effectuer une attaque à distance (portée 6/18m) avec le projectile, en utilisant votre dé d'Arts martiaux.

### Chute ralentie (niveau 4)

Vous pouvez utiliser votre réaction pour réduire les dégâts de chute de 5 x niveau de moine.

### Attaque supplémentaire (niveau 5)

Vous pouvez attaquer deux fois au lieu d'une lorsque vous utilisez l'action Attaquer.

### Frappe étourdissante (niveau 5)

Lorsque vous touchez une créature avec une attaque d'arme de corps à corps, vous pouvez dépenser 1 point de ki pour tenter de l'étourdir. La cible doit réussir un jet de sauvegarde de Constitution ou être étourdie jusqu'à la fin de votre prochain tour.

### Frappes de ki (niveau 6)

Vos attaques à mains nues comptent comme magiques pour surmonter les résistances et immunités.

### Esquive totale (niveau 7)

Lorsque vous êtes soumis à un effet vous permettant de faire un jet de sauvegarde de Dextérité pour ne subir que la moitié des dégâts, vous ne subissez aucun dégât en cas de réussite et seulement la moitié en cas d'échec.

### Sérénité (niveau 7)

Vous pouvez utiliser votre action pour mettre fin à un effet vous infligeant l'état charmé ou effrayé.

### Pureté physique (niveau 10)

Vous êtes immunisé aux maladies et aux poisons.

### Langue du soleil et de la lune (niveau 13)

Vous apprenez à toucher le ki d'autres esprits et comprenez ainsi tous les langages parlés. De plus, toute créature comprenant un langage peut vous comprendre.

### Âme de diamant (niveau 14)

Votre maîtrise du ki vous accorde la maîtrise de tous les jets de sauvegarde. De plus, vous pouvez dépenser 1 point de ki pour relancer un jet de sauvegarde raté.

### Jeunesse éternelle (niveau 15)

Votre ki vous préserve des effets du vieillissement. Vous ne pouvez pas vieillir magiquement, et vous ne souffrez plus des infirmités de l'âge. Cependant, vous pouvez toujours mourir de vieillesse. De plus, vous n'avez plus besoin de nourriture ni d'eau.

### Désertion de l'âme (niveau 18)

Vous pouvez dépenser 4 points de ki pour devenir invisible pendant 1 minute. Pendant cette période, vous avez aussi la résistance à tous les types de dégâts sauf force.

### Perfection de l'être (niveau 20)

Lorsque vous faites un jet d'initiative et n'avez aucun point de ki restant, vous en regagnez 4.

---

## Traditions monastiques

### Voie de la Paume

Les moines de la Voie de la Paume sont des maîtres du combat à mains nues.

#### Technique de la paume (niveau 3)
Lorsque vous touchez une créature avec une attaque de Déluge de coups, vous pouvez lui imposer l'un des effets suivants :
- Elle doit réussir un jet de sauvegarde de Dextérité ou tomber à terre
- Elle doit réussir un jet de sauvegarde de Force ou être repoussée de 4,5 mètres
- Elle ne peut pas effectuer de réactions jusqu'à la fin de votre prochain tour

#### Plénitude physique (niveau 6)
Par une action, vous pouvez regagner un nombre de points de vie égal à 3 fois votre niveau de moine. Vous devez terminer un repos long avant de réutiliser cette capacité.

#### Tranquillité (niveau 11)
À la fin d'un repos long, vous gagnez l'effet du sort *sanctuaire* jusqu'au début de votre prochain repos long. Le DD de sauvegarde est égal à votre DD de sauvegarde du ki.

#### Paume frémissante (niveau 17)
Lorsque vous touchez une créature avec une attaque à mains nues, vous pouvez dépenser 3 points de ki pour déclencher des vibrations imperceptibles dans son corps pendant un nombre de jours égal à votre niveau de moine. À tout moment, vous pouvez utiliser une action pour mettre fin aux vibrations. La créature doit faire un jet de sauvegarde de Constitution, subissant 10d10 dégâts nécrotiques en cas d'échec, ou 0 en cas de réussite.

---

### Voie de l'Ombre

Les moines de la Voie de l'Ombre suivent une tradition qui valorise la discrétion et la subtilité.

#### Arts des ombres (niveau 3)
Vous pouvez dépenser 2 points de ki pour lancer [[Ténèbres]], [[Vision dans le noir]], Passage sans trace ou Silence sans [[composantes matérielles]].

#### Foulée d'ombre (niveau 6)
Lorsque vous êtes dans une zone de lumière faible ou de ténèbres, vous pouvez utiliser une action bonus pour vous téléporter jusqu'à 18 mètres dans une autre zone de lumière faible ou de ténèbres que vous pouvez voir. Vous avez alors l'avantage à la première attaque de corps à corps que vous effectuez avant la fin du tour.

#### Linceul d'ombre (niveau 11)
Lorsque vous êtes dans une zone de lumière faible ou de ténèbres, vous pouvez devenir invisible par une action. Vous restez invisible jusqu'à ce que vous attaquiez, lanciez un sort, ou vous trouviez dans une zone de lumière vive.

#### Opportuniste (niveau 17)
Lorsqu'une créature à 1,5 mètre de vous est touchée par une attaque effectuée par une créature autre que vous, vous pouvez utiliser votre réaction pour effectuer une attaque de corps à corps contre cette créature.

---

### Voie des Quatre Éléments

Les moines de la Voie des Quatre Éléments apprennent à canaliser les éléments à travers leur ki.

#### Disciple des éléments (niveau 3)
Vous apprenez des disciplines magiques qui exploitent le pouvoir des quatre éléments. Chaque discipline nécessite de dépenser des points de ki.

Vous apprenez **Harmonisation élémentaire** (sort mineur à volonté pour petits effets élémentaires) plus une discipline de votre choix. Vous en apprenez d'autres aux niveaux 6, 11 et 17.

#### Disciplines élémentaires

| Discipline | Ki | Effet |
|------------|-----|-------|
| Crocs du serpent de feu | 1+ | Portée 3m à vos attaques à mains nues, +1d10 dégâts de feu; +1d10 par ki supp. |
| Poing de l'air | 2 | Ligne de 9m, 3d10 dégâts contondants, repousse 3m (Sauv. FOR) |
| Poing des quatre tonnerres | 2 | Vague tonnante |
| Défense de la montagne éternelle | 5 | Peau de pierre sur vous-même |
| Étreinte du vent du nord | 3 | Immobilisation de personne |
| Vagues de flammes dévoratrices | 5 | Boule de feu |
| Souffle de l'hiver | 6 | Cône de froid |
| Chevauchée du vent | 4 | Vol sur vous-même |
| Gong du sommet | 3 | Fracassement |
| Frappe de cendres | 2 | Mains brûlantes |

**Incantation avec le ki** : Les sorts lancés via ces disciplines utilisent votre DD de sauvegarde du ki.

---

### Voie de la Miséricorde

Les moines de la Voie de la Miséricorde apprennent à manipuler la force vitale des autres.

#### Instruments de miséricorde (niveau 3)
Vous gagnez la maîtrise de Intuition et Médecine, et le kit d'herboriste.

#### Main de guérison (niveau 3)
Par une action, vous pouvez dépenser 1 point de ki pour toucher une créature et lui restaurer un nombre de PV égal à un lancer de votre dé d'Arts martiaux + modificateur de Sagesse. Vous pouvez aussi mettre fin à une maladie ou à un état parmi aveugle, assourdi, empoisonné, étourdi ou paralysé.

#### Main de mort (niveau 3)
Lorsque vous touchez une créature avec une attaque à mains nues, vous pouvez dépenser 1 point de ki pour infliger des dégâts nécrotiques supplémentaires égaux à un lancer de votre dé d'Arts martiaux + modificateur de Sagesse. Cette capacité ne peut être utilisée qu'une fois par tour.

#### Technique du médecin (niveau 6)
Lorsque vous utilisez Main de guérison ou Main de mort, vous pouvez remplacer une attaque de Déluge de coups par l'une de ces capacités sans dépenser de ki supplémentaire.

#### Soins en masse (niveau 11)
Lorsque vous utilisez Main de guérison, vous pouvez cibler un nombre de créatures égal à votre modificateur de Sagesse.

#### Main de l'harmonie ultime (niveau 17)
Par une action, vous pouvez dépenser 5 points de ki pour toucher le corps d'une créature morte dans les dernières 24 heures et la ramener à la vie avec 4d10 + modificateur de Sagesse PV.
