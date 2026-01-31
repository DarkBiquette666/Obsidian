---
Class: Class

aliases:
  - Clerc
  - clerc
  - Cleric
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d8
saving_throws:
  - sag
  - cha
armor_proficiencies:
  - intermediaires
  - boucliers
  - legeres
weapon_proficiencies:
  - courantes
tool_proficiencies: []
skill_choices: 2
skill_options:
  - Histoire
  - Intuition
  - Medecine
  - Persuasion
  - Religion
spellcasting_ability: sag
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Incantation"
      - "Domaine divin"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Conduit divin (1/repos)"
      - "Capacité de domaine"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
      - "Destruction des morts-vivants (FP 1/2)"
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "Conduit divin (2/repos)"
      - "Capacité de domaine"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
  - type: ClassLevelEntry
    level: 8
    proficiency_bonus: 3
    features:
      - "Amélioration"
      - "Destruction (FP 1)"
      - "Capacité de domaine"
  - type: ClassLevelEntry
    level: 9
    proficiency_bonus: 4
    features:
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "Intervention divine"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "Destruction des morts-vivants (FP 2)"
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
      - "Destruction des morts-vivants (FP 3)"
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
      - "Destruction des morts-vivants (FP 4)"
      - "Capacité de domaine"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "Conduit divin (3/repos)"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Intervention divine améliorée"
subclasses:
  - "[[Vie]]"
  - "[[Guerre]]"
  - "[[Lumière]]"
  - "[[Tempête]]"
  - "[[Savoir]]"
  - "[[Duperie]]"
  - "[[Nature]]"
  - "[[Forge]]"
  - "[[Crépuscule]]"
starting_equipment_draft: "- Une masse d'armes OU un marteau de guerre (si maîtrise) - Une armure d'écailles, une armure de cuir OU une cotte de mailles (si maîtrise) - Une arbalète légère et 20 carreaux OU une arme courante - Un sac d'ecclésiastique OU un sac d'explorateur - Un bouclier et un symbole sacré"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Masse d'armes]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Marteau de guerre]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Armure d'écailles]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Armure de cuir]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Cotte de mailles]]"
        quantity: 1
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
            item: "[[Carreau]]"
            quantity: 20
      - type: CategoryItem
        category: "Arme courante"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Sac d'ecclésiastique]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'explorateur]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        item: "[[Bouclier]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Symbole sacré]]"
        quantity: 1
---



# Clerc

Le clerc est un intermédiaire entre le monde mortel et les plans divins. Ces champions de leur foi manient la magie sacrée au service de leur divinité, soignant les alliés, repoussant les morts-vivants et frappant les ennemis avec le pouvoir divin.

## Tableau de progression

| Niveau | Bonus | Capacités | Sorts mineurs |
|--------|-------|-----------|---------------|
| 1 | +2 | Incantation, Domaine divin | 3 |
| 2 | +2 | Conduit divin (1/repos), Capacité de domaine | 3 |
| 3 | +2 | - | 3 |
| 4 | +2 | Amélioration de caractéristiques | 4 |
| 5 | +3 | Destruction des morts-vivants (FP 1/2) | 4 |
| 6 | +3 | Conduit divin (2/repos), Capacité de domaine | 4 |
| 7 | +3 | - | 4 |
| 8 | +3 | Amélioration, Destruction (FP 1), Capacité de domaine | 4 |
| 9 | +4 | - | 4 |
| 10 | +4 | Intervention divine | 5 |
| 11 | +4 | Destruction des morts-vivants (FP 2) | 5 |
| 12 | +4 | Amélioration de caractéristiques | 5 |
| 13 | +5 | - | 5 |
| 14 | +5 | Destruction des morts-vivants (FP 3) | 5 |
| 15 | +5 | - | 5 |
| 16 | +5 | Amélioration de caractéristiques | 5 |
| 17 | +6 | Destruction des morts-vivants (FP 4), Capacité de domaine | 5 |
| 18 | +6 | Conduit divin (3/repos) | 5 |
| 19 | +6 | Amélioration de caractéristiques | 5 |
| 20 | +6 | Intervention divine améliorée | 5 |

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

**Dés de vie** : 1d8 par niveau de clerc
**Points de vie au niveau 1** : 8 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d8 (ou 5) + modificateur de Constitution

### Maîtrises

- **Armures** : Armures légères, armures intermédiaires, boucliers
- **Armes** : Armes courantes
- **Outils** : Aucun
- **Jets de sauvegarde** : Sagesse, Charisme
- **Compétences** : Choisissez 2 parmi Histoire, Intuition, Médecine, Persuasion, Religion

### Équipement de départ

- Une masse d'armes OU un marteau de guerre (si maîtrise)
- Une armure d'écailles, une armure de cuir OU une cotte de mailles (si maîtrise)
- Une arbalète légère et 20 carreaux OU une arme courante
- Un sac d'ecclésiastique OU un sac d'explorateur
- Un bouclier et un symbole sacré

---

## Capacités de classe

### Incantation (niveau 1)

Le clerc prépare ses sorts chaque jour parmi la liste complète des sorts de clerc.

**Caractéristique d'incantation** : Sagesse
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Sagesse
**Modificateur d'attaque** : bonus de maîtrise + modificateur de Sagesse
**Focaliseur** : Symbole sacré
**Sorts préparés** : niveau de clerc + modificateur de Sagesse

### Domaine divin (niveau 1)

Choisissez un domaine divin qui vous confère des sorts de domaine et des capacités aux niveaux 1, 2, 6, 8 et 17.

### Conduit divin (niveau 2, 6, 18)

Vous pouvez canaliser l'énergie divine pour alimenter des effets magiques.

**Renvoi des morts-vivants** : Par une action, présentez votre symbole sacré. Chaque mort-vivant dans un rayon de 9 mètres qui peut vous voir ou vous entendre doit réussir un jet de sauvegarde de Sagesse ou être renvoyé pendant 1 minute (fuit et ne peut pas s'approcher volontairement à moins de 9 m).

Nombre d'utilisations :
- 1/repos (niveaux 2-5)
- 2/repos (niveaux 6-17)
- 3/repos (niveaux 18-20)

### Destruction des morts-vivants (niveau 5)

Lorsqu'un mort-vivant rate son jet de sauvegarde contre Renvoi des morts-vivants et que son FP est égal ou inférieur à un certain seuil, il est instantanément détruit :
- FP 1/2 (niveau 5)
- FP 1 (niveau 8)
- FP 2 (niveau 11)
- FP 3 (niveau 14)
- FP 4 (niveau 17)

### Intervention divine (niveau 10)

Vous pouvez implorer votre divinité pour qu'elle intervienne. Lancez 1d100 : si le résultat est égal ou inférieur à votre niveau de clerc, votre divinité intervient (le MD choisit la nature de l'intervention). En cas de succès, vous ne pouvez pas réutiliser cette capacité pendant 7 jours.

Au niveau 20, l'intervention réussit automatiquement.

---

## Domaines divins

### Domaine de la Vie

Le domaine de la Vie se concentre sur l'énergie positive et la guérison.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Bénédiction, Soins |
| 3 | Arme spirituelle, Restauration partielle |
| 5 | Lueur d'espoir, Retour à la vie |
| 7 | Gardien de la foi, Protection contre la mort |
| 9 | Rappel à la vie, Soins de groupe |

#### Maîtrise supplémentaire (niveau 1)
Vous gagnez la maîtrise des armures lourdes.

#### Disciple de la vie (niveau 1)
Vos sorts de guérison sont plus efficaces. Lorsque vous utilisez un sort de niveau 1 ou plus pour restaurer des points de vie, la créature regagne des PV supplémentaires égaux à 2 + le niveau du sort.

#### Conduit divin : Préservation de la vie (niveau 2)
Par une action, vous présentez votre symbole sacré et invoquez l'énergie de guérison. Vous restaurez un nombre de points de vie égal à 5 fois votre niveau de clerc, répartis comme vous le souhaitez entre les créatures dans un rayon de 9 mètres. Vous ne pouvez pas utiliser cette capacité sur un mort-vivant ou un artifice, et vous ne pouvez pas restaurer plus de la moitié des PV max d'une créature.

#### Guérisseur béni (niveau 6)
Les sorts de guérison que vous lancez sur d'autres créatures vous soignent aussi. Vous regagnez un nombre de PV égal à 2 + le niveau du sort.

#### Frappe divine (niveau 8)
Une fois par tour, lorsque vous touchez une créature avec une attaque d'arme, vous pouvez infliger 1d8 dégâts radiants supplémentaires. À partir du niveau 14, les dégâts passent à 2d8.

#### Guérison suprême (niveau 17)
Lorsque vous lancez un sort qui restaure des points de vie, au lieu de lancer les dés, vous utilisez le maximum possible pour chaque dé.

---

### Domaine de la Guerre

Le domaine de la Guerre exalte les vertus du combat au nom d'une cause juste.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Bouclier de la foi, Faveur divine |
| 3 | Arme magique, Arme spirituelle |
| 5 | Aura du croisé, Esprits gardiens |
| 7 | Liberté de mouvement, Peau de pierre |
| 9 | Colonne de flamme, Immobilisation de monstre |

#### Maîtrise supplémentaire (niveau 1)
Vous gagnez la maîtrise des armes de guerre et des armures lourdes.

#### Prêtre de la guerre (niveau 1)
Lorsque vous utilisez l'action Attaquer, vous pouvez effectuer une attaque d'arme en action bonus. Vous pouvez utiliser cette capacité un nombre de fois égal à votre modificateur de Sagesse (minimum 1), et vous récupérez toutes les utilisations après un repos long.

#### Conduit divin : Frappe guidée (niveau 2)
Lorsque vous effectuez un jet d'attaque, vous pouvez utiliser votre Conduit divin pour gagner un bonus de +10 au jet. Vous faites ce choix après avoir vu le résultat mais avant que le MD annonce si l'attaque touche.

#### Conduit divin : Bénédiction du dieu de la guerre (niveau 6)
Lorsqu'une créature dans un rayon de 9 mètres effectue un jet d'attaque, vous pouvez utiliser votre réaction et votre Conduit divin pour lui accorder un bonus de +10 au jet.

#### Frappe divine (niveau 8)
Une fois par tour, lorsque vous touchez avec une attaque d'arme, vous pouvez infliger 1d8 dégâts supplémentaires du même type que l'arme. À partir du niveau 14, les dégâts passent à 2d8.

#### Avatar de la bataille (niveau 17)
Vous gagnez la résistance aux dégâts contondants, perçants et tranchants des attaques non magiques.

---

### Domaine de la Lumière

Le domaine de la Lumière met l'accent sur la vérité, la vigilance et la beauté rayonnante.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Lueurs féeriques, Mains brûlantes |
| 3 | Rayon ardent, Sphère de feu |
| 5 | Boule de feu, Lumière du jour |
| 7 | Gardien de la foi, Mur de feu |
| 9 | Colonne de flamme, Scrutation |

#### Sort mineur supplémentaire (niveau 1)
Vous gagnez le sort mineur *lumière* s'il ne fait pas déjà partie de vos sorts de clerc.

#### Illumination protectrice (niveau 1)
Lorsqu'une créature que vous pouvez voir dans un rayon de 9 mètres vous attaque ou attaque une créature alliée, vous pouvez utiliser votre réaction pour imposer un désavantage au jet d'attaque. Vous pouvez utiliser cette capacité un nombre de fois égal à votre modificateur de Sagesse, et vous récupérez toutes les utilisations après un repos long.

#### Conduit divin : Radiance de l'aube (niveau 2)
Par une action, vous présentez votre symbole sacré et toute obscurité magique dans un rayon de 9 mètres est dissipée. Chaque créature hostile dans ce rayon doit effectuer un jet de sauvegarde de Constitution, subissant 2d10 + votre niveau de clerc dégâts radiants en cas d'échec, ou la moitié en cas de réussite.

#### Illumination améliorée (niveau 6)
Vous pouvez utiliser Illumination protectrice sur une créature alliée dans un rayon de 9 mètres.

#### Incantation puissante (niveau 8)
Vous ajoutez votre modificateur de Sagesse aux dégâts infligés par vos sorts mineurs de clerc.

#### Halo de lumière (niveau 17)
Par une action, vous vous enveloppez d'un halo de lumière pendant 1 minute. Vous émettez une lumière vive sur 18 mètres et une lumière faible sur 9 mètres supplémentaires. Les créatures ennemies dans la lumière vive ont un désavantage aux jets de sauvegarde contre les sorts infligeant des dégâts de feu ou radiants.

---

### Domaine de la Tempête

Le domaine de la Tempête incarne la puissance destructrice des orages et de la mer.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Nappe de brouillard, Vague tonnante |
| 3 | Bourrasque, Fracassement |
| 5 | Appel de la foudre, Tempête de neige |
| 7 | Contrôle de l'eau, Tempête de grêle |
| 9 | Fléaux d'insectes, Vague destructrice |

#### Maîtrise supplémentaire (niveau 1)
Vous gagnez la maîtrise des armes de guerre et des armures lourdes.

#### Fureur de l'ouragan (niveau 1)
Lorsqu'une créature que vous pouvez voir dans un rayon de 1,5 mètre vous touche avec une attaque, vous pouvez utiliser votre réaction pour infliger 2d8 dégâts de foudre ou de tonnerre. Vous pouvez utiliser cette capacité un nombre de fois égal à votre modificateur de Sagesse, et vous récupérez toutes les utilisations après un repos long.

#### Conduit divin : Fureur destructrice (niveau 2)
Lorsque vous infligez des dégâts de foudre ou de tonnerre, vous pouvez utiliser votre Conduit divin pour infliger les dégâts maximum au lieu de lancer les dés.

#### Frappe de l'éclair (niveau 6)
Lorsque vous infligez des dégâts de foudre à une créature de taille G ou moins, vous pouvez aussi la repousser de 3 mètres.

#### Frappe divine (niveau 8)
Une fois par tour, lorsque vous touchez avec une attaque d'arme, vous infligez 1d8 dégâts de tonnerre supplémentaires. À partir du niveau 14, les dégâts passent à 2d8.

#### Enfant de la tempête (niveau 17)
Vous gagnez une vitesse de vol égale à votre vitesse de marche actuelle tant que vous n'êtes pas sous terre ou à l'intérieur.

---

### Domaine du Savoir

Le domaine du Savoir met en valeur l'apprentissage et la compréhension.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Identification, Injonction |
| 3 | Augure, Suggestion |
| 5 | Antidétection, Communication avec les morts |
| 7 | Confusion, Oeil magique |
| 9 | Mythes et légendes, Scrutation |

#### Bénédictions du savoir (niveau 1)
Vous apprenez deux langues de votre choix. Vous gagnez aussi la maîtrise de deux compétences parmi Arcanes, Histoire, Nature et Religion. Votre bonus de maîtrise est doublé pour ces compétences.

#### Conduit divin : Savoir ancestral (niveau 2)
Vous pouvez utiliser votre Conduit divin pour puiser dans le puits de la connaissance divine. Par une action, vous gagnez la maîtrise d'une compétence ou d'un outil de votre choix pendant 10 minutes.

#### Conduit divin : Lecture des pensées (niveau 6)
Vous pouvez utiliser votre Conduit divin pour lire les pensées d'une créature. Vous pouvez alors utiliser votre accès à son esprit pour la commander (comme le sort *suggestion*) sans dépenser de mana.

#### Incantation puissante (niveau 8)
Vous ajoutez votre modificateur de Sagesse aux dégâts infligés par vos sorts mineurs de clerc.

#### Visions du passé (niveau 17)
Vous pouvez invoquer des visions du passé liées à un objet que vous tenez ou à votre environnement immédiat. Vous méditez pendant 1 minute puis recevez des visions des événements passés (jusqu'à un nombre de jours égal à votre modificateur de Sagesse).

---

### Domaine de la Duperie

Le domaine de la Duperie valorise la ruse, l'illusion et la tromperie.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Charme-personne, Déguisement |
| 3 | Image miroir, Passage sans trace |
| 5 | Clignotement, Dissipation de la magie |
| 7 | Métamorphose, Porte dimensionnelle |
| 9 | Domination de personne, Modification de mémoire |

#### Bénédiction de l'escroc (niveau 1)
Vous pouvez utiliser votre action pour toucher une créature consentante (autre que vous) et lui accorder l'avantage aux jets de Discrétion pendant 1 heure ou jusqu'à ce que vous utilisiez à nouveau cette capacité.

#### Conduit divin : Invocation de réplique (niveau 2)
Vous créez une illusion parfaite de vous-même qui dure 1 minute. Par une action bonus, vous pouvez déplacer l'illusion jusqu'à 9 mètres. Vous pouvez lancer des sorts comme si vous étiez à la place de l'illusion.

#### Conduit divin : Linceul d'ombre (niveau 6)
Lorsque vous êtes dans une zone de lumière faible ou de ténèbres, vous pouvez utiliser votre action pour devenir invisible jusqu'à la fin de votre prochain tour.

#### Frappe divine (niveau 8)
Une fois par tour, lorsque vous touchez avec une attaque d'arme, vous infligez 1d8 dégâts de poison supplémentaires. À partir du niveau 14, les dégâts passent à 2d8.

#### Réplique améliorée (niveau 17)
Vous pouvez créer jusqu'à quatre répliques de vous-même avec Invocation de réplique. Vous pouvez déplacer n'importe quel nombre d'entre elles par une action bonus.

---

### Domaine de la Nature

Le domaine de la Nature incarne la connexion avec le monde naturel.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Amitié avec les animaux, Communication avec les animaux |
| 3 | Croissance d'épines, Peau d'écorce |
| 5 | Croissance végétale, Mur de vent |
| 7 | Domination de bête, Liane avide |
| 9 | Fléaux d'insectes, Passage par les arbres |

#### Acolyte de la nature (niveau 1)
Vous apprenez un sort mineur de druide de votre choix. Vous gagnez aussi la maîtrise d'une compétence parmi Dressage, Nature et Survie.

#### Maîtrise supplémentaire (niveau 1)
Vous gagnez la maîtrise des armures lourdes.

#### Conduit divin : Charme des animaux et plantes (niveau 2)
Vous pouvez utiliser votre Conduit divin pour charmer les animaux et les plantes. Chaque bête ou créature végétale dans un rayon de 9 mètres doit réussir un jet de sauvegarde de Sagesse ou être charmée pendant 1 minute.

#### Atténuation des éléments (niveau 6)
Lorsque vous ou une créature dans un rayon de 9 mètres subissez des dégâts d'acide, de froid, de feu, de foudre ou de tonnerre, vous pouvez utiliser votre réaction pour accorder la résistance à ce type de dégâts.

#### Frappe divine (niveau 8)
Une fois par tour, lorsque vous touchez avec une attaque d'arme, vous infligez 1d8 dégâts de froid, de feu ou de foudre supplémentaires (votre choix). À partir du niveau 14, les dégâts passent à 2d8.

#### Maître de la nature (niveau 17)
Vous gagnez la capacité de commander les créatures charmées par votre Charme des animaux et plantes. Par une action bonus, vous pouvez commander ces créatures.

---

### Domaine de la Forge

Le domaine de la Forge célèbre l'art de la création et le travail des métaux.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Châtiment calcinant, Identification |
| 3 | Arme magique, Métal brûlant |
| 5 | Arme élémentaire, Protection contre une énergie |
| 7 | Fabrication, Mur de feu |
| 9 | Animation d'objets, Création |

#### Maîtrise supplémentaire (niveau 1)
Vous gagnez la maîtrise des armures lourdes et des outils de forgeron.

#### Bénédiction de la forge (niveau 1)
À la fin d'un repos long, vous pouvez toucher une armure non magique ou une arme non magique. Jusqu'à votre prochain repos long, cet objet devient magique et confère +1 à la CA (armure) ou +1 aux jets d'attaque et de dégâts (arme).

#### Conduit divin : Bénédiction de l'artisan (niveau 2)
Vous pouvez utiliser votre Conduit divin pour créer un objet non magique en métal (valeur max 100 po). La création prend 1 heure et l'objet reste jusqu'à la fin de votre prochain repos long.

#### Âme de la forge (niveau 6)
Vous gagnez la résistance aux dégâts de feu. De plus, lorsque vous portez une armure lourde, vous gagnez +1 à la CA.

#### Frappe divine (niveau 8)
Une fois par tour, lorsque vous touchez avec une attaque d'arme, vous infligez 1d8 dégâts de feu supplémentaires. À partir du niveau 14, les dégâts passent à 2d8.

#### Saint de la forge (niveau 17)
Vous gagnez l'immunité aux dégâts de feu. De plus, lorsque vous portez une armure lourde, vous gagnez la résistance aux dégâts contondants, perçants et tranchants des attaques non magiques.

---

### Domaine du Crépuscule

Le domaine du Crépuscule gouverne la transition entre la lumière et l'obscurité.

#### Sorts de domaine

| Niveau de clerc | Sorts |
|-----------------|-------|
| 1 | Lueurs féeriques, Sommeil |
| 3 | Cécité/Surdité, Rayon de lune |
| 5 | Aura de vitalité, Petite hutte de Léomund |
| 7 | Aura de vie, Invisibilité supérieure |
| 9 | Cercle de téléportation, Illusion trompeuse |

#### Maîtrise supplémentaire (niveau 1)
Vous gagnez la maîtrise des armes de guerre et des armures lourdes.

#### Yeux de la nuit (niveau 1)
Vous gagnez la vision dans le noir jusqu'à 90 mètres. Par une action, vous pouvez partager cette vision avec des créatures consentantes dans un rayon de 3 mètres pendant 1 heure (nombre de créatures = modificateur de Sagesse).

#### Bénédiction du vigilant (niveau 1)
Par une action, vous accordez l'avantage au prochain jet d'initiative d'une créature à 9 mètres. Utilisations : bonus de maîtrise par repos long.

#### Conduit divin : Sanctuaire du crépuscule (niveau 2)
Par une action, vous invoquez une sphère de lumière tamisée de 9 mètres de rayon centrée sur vous. Elle dure 1 minute et se déplace avec vous. À la fin de chaque tour, vous et les alliés dans la sphère gagnez des PV temporaires égaux à 1d6 + niveau de clerc.

#### Pas du héros (niveau 6)
Par une action bonus, vous gagnez une vitesse de vol égale à votre vitesse de marche jusqu'à la fin de votre tour.

#### Linceul divin (niveau 8)
Vos PV temporaires accordés par Sanctuaire du crépuscule passent à 1d6 + moitié de votre niveau de clerc.

#### Demi-obscurité (niveau 17)
Vous et vos alliés dans votre Sanctuaire du crépuscule avez un abri partiel.
