---
Class: Class

aliases:
  - Paladin
  - paladin
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d10
saving_throws:
  - sag
  - cha
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
  - Athletisme
  - Intimidation
  - Intuition
  - Medecine
  - Persuasion
  - Religion
spellcasting_ability: cha
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Sens divin"
      - "Imposition des mains"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Style de combat"
      - "Incantation"
      - "Châtiment divin"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "Santé divine"
      - "Serment sacré"
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
      - "Aura de protection (3 m)"
  - type: ClassLevelEntry
    level: 7
    proficiency_bonus: 3
    features:
      - "Capacité de serment"
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
      - "Aura de courage"
  - type: ClassLevelEntry
    level: 11
    proficiency_bonus: 4
    features:
      - "Châtiment divin amélioré"
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
      - "Contact purifiant"
  - type: ClassLevelEntry
    level: 15
    proficiency_bonus: 5
    features:
      - "Capacité de serment"
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
      - "Amélioration des auras (9 m)"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Capacité de serment"
starting_equipment_draft: "- Une arme de guerre et un bouclier OU deux armes de guerre - Cinq javelines OU une arme courante de corps à corps - Un sac d'ecclésiastique OU un sac d'explorateur - Une cotte de mailles et un symbole sacré"
starting_equipment:
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
      - type: SpecificItem
        item: "[[Javeline]]"
        quantity: 5
      - type: CategoryItem
        category: "Arme courante de corps à corps"
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
        item: "[[Cotte de mailles]]"
        quantity: 1
      - type: CategoryItem
        category: "Symbole sacré"
        quantity: 1
---



# Paladin

Les paladins sont des guerriers bénis qui ont prêté un serment solennel de combattre le mal. Guidés par une puissance divine issue de leur conviction plutôt que d'un dieu spécifique, ils combinent compétences martiales et magie divine pour incarner la justice et la vertu.

## Tableau de progression

| Niveau | Bonus | Capacités | Sorts préparés |
|--------|-------|-----------|----------------|
| 1 | +2 | Sens divin, Imposition des mains | - |
| 2 | +2 | Style de combat, Incantation, Châtiment divin | Niv + CHA |
| 3 | +2 | Santé divine, Serment sacré | Niv + CHA |
| 4 | +2 | Amélioration de caractéristiques | Niv + CHA |
| 5 | +3 | Attaque supplémentaire | Niv + CHA |
| 6 | +3 | Aura de protection (3 m) | Niv + CHA |
| 7 | +3 | Capacité de serment | Niv + CHA |
| 8 | +3 | Amélioration de caractéristiques | Niv + CHA |
| 9 | +4 | - | Niv + CHA |
| 10 | +4 | Aura de courage | Niv + CHA |
| 11 | +4 | Châtiment divin amélioré | Niv + CHA |
| 12 | +4 | Amélioration de caractéristiques | Niv + CHA |
| 13 | +5 | - | Niv + CHA |
| 14 | +5 | Contact purifiant | Niv + CHA |
| 15 | +5 | Capacité de serment | Niv + CHA |
| 16 | +5 | Amélioration de caractéristiques | Niv + CHA |
| 17 | +6 | - | Niv + CHA |
| 18 | +6 | Amélioration des auras (9 m) | Niv + CHA |
| 19 | +6 | Amélioration de caractéristiques | Niv + CHA |
| 20 | +6 | Capacité de serment | Niv + CHA |

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

**Dés de vie** : 1d10 par niveau de paladin
**Points de vie au niveau 1** : 10 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d10 (ou 6) + modificateur de Constitution

### Maîtrises

- **Armures** : Toutes les armures, boucliers
- **Armes** : Armes courantes, armes de guerre
- **Outils** : Aucun
- **Jets de sauvegarde** : Sagesse, Charisme
- **Compétences** : Choisissez 2 parmi Athlétisme, Intimidation, Intuition, Médecine, Persuasion, Religion

### Équipement de départ

- Une arme de guerre et un bouclier OU deux armes de guerre
- Cinq javelines OU une arme courante de corps à corps
- Un sac d'ecclésiastique OU un sac d'explorateur
- Une cotte de mailles et un symbole sacré

---

## Capacités de classe

### Sens divin (niveau 1)

Par une action, vous pouvez ouvrir votre conscience pour détecter les forces du bien et du mal. Jusqu'à la fin de votre prochain tour, vous connaissez l'emplacement de tout céleste, fiélon ou mort-vivant dans un rayon de 18 mètres qui n'est pas derrière un abri total. Vous connaissez le type de créature mais pas son identité.

**Utilisations** : 1 + modificateur de Charisme par repos long

### Imposition des mains (niveau 1)

Votre contact béni peut soigner les blessures. Vous avez une réserve de points de vie à soigner égale à 5 x votre niveau de paladin. Par une action, vous pouvez toucher une créature et puiser dans cette réserve pour lui rendre des points de vie.

Vous pouvez également dépenser 5 points de la réserve pour guérir une maladie ou neutraliser un poison affectant la cible. Vous pouvez guérir plusieurs maladies et poisons avec une seule utilisation, en dépensant les points séparément.

### Style de combat (niveau 2)

Choisissez un style de combat :

- **Arme à deux mains** : Relancez les 1 et 2 sur les dés de dégâts des armes à deux mains
- **Défense** : +1 à la CA tant que vous portez une armure
- **Duel** : +2 aux dégâts quand vous maniez une arme de corps à corps à une main et aucune autre arme
- **Protection** : Quand une créature attaque une cible autre que vous à 1,5 m, utilisez votre réaction pour imposer un désavantage (nécessite un bouclier)

### Incantation (niveau 2)

Le paladin prépare ses sorts chaque jour parmi la liste complète des sorts de paladin.

**Caractéristique d'incantation** : Charisme
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Charisme
**Modificateur d'attaque** : bonus de maîtrise + modificateur de Charisme
**Focaliseur** : Symbole sacré
**Sorts préparés** : niveau de paladin / 2 (arrondi à l'inférieur, minimum 1) + modificateur de Charisme

### Châtiment divin (niveau 2)

Quand vous touchez une créature avec une attaque de corps à corps, vous pouvez dépenser un emplacement de sort (ou du mana) pour infliger des dégâts radiants supplémentaires à la cible. Les dégâts supplémentaires sont de 2d8 pour un sort de niveau 1, plus 1d8 pour chaque niveau de sort au-dessus du 1er, jusqu'à un maximum de 5d8.

Les dégâts augmentent de 1d8 si la cible est un mort-vivant ou un fiélon.

### Santé divine (niveau 3)

La magie divine qui coule en vous vous immunise contre les maladies.

### Serment sacré (niveau 3)

Vous prêtez le serment qui vous lie en tant que paladin pour toujours. Votre serment vous confère des capacités aux niveaux 3, 7, 15 et 20.

### Attaque supplémentaire (niveau 5)

Vous pouvez attaquer deux fois au lieu d'une quand vous utilisez l'action Attaquer pendant votre tour.

### Aura de protection (niveau 6)

Chaque fois que vous ou une créature amicale située à 3 mètres de vous doit effectuer un jet de sauvegarde, elle gagne un bonus au jet égal à votre modificateur de Charisme (minimum +1). Vous devez être conscient pour accorder ce bonus.

Au niveau 18, la portée de cette aura passe à 9 mètres.

### Aura de courage (niveau 10)

Vous et les créatures amicales situées à 3 mètres de vous ne pouvez pas être effrayés tant que vous êtes conscient.

Au niveau 18, la portée de cette aura passe à 9 mètres.

### Châtiment divin amélioré (niveau 11)

Vous êtes tellement imbu de justice que toutes vos attaques avec des armes de corps à corps infligent 1d8 dégâts radiants supplémentaires.

### Contact purifiant (niveau 14)

Vous pouvez utiliser votre action pour mettre fin à un sort sur vous-même ou sur une créature consentante que vous touchez.

**Utilisations** : modificateur de Charisme (minimum 1) par repos long

---

## Serments sacrés

### Serment de Dévotion

Le serment de Dévotion lie un paladin aux idéaux les plus élevés de justice, de vertu et d'ordre. Ces paladins rencontrent des anges et des pouvoirs du bien.

#### Sorts de serment

| Niveau de paladin | Sorts |
|-------------------|-------|
| 3 | Protection contre le mal et le bien, Sanctuaire |
| 5 | Restauration partielle, Zone de vérité |
| 9 | Phare d'espoir, Dissipation de la magie |
| 13 | Liberté de mouvement, Gardien de la foi |
| 17 | Communion, Colonne de flamme |

#### Conduite divine (niveau 3)

Vous gagnez les deux options de Conduite divine suivantes :

**Arme sacrée** : Par une action, vous pouvez insuffler une arme avec de l'énergie positive. Pendant 1 minute, vous ajoutez votre modificateur de Charisme aux jets d'attaque avec cette arme (minimum +1). L'arme émet une lumière vive sur 6 mètres et une lumière faible sur 6 mètres supplémentaires. Vous pouvez terminer cet effet par une action bonus.

**Renvoi des impies** : Par une action, vous présentez votre symbole sacré et prononcez une prière contre les morts-vivants et les fiélons. Chaque mort-vivant ou fiélon à 9 mètres doit effectuer un jet de sauvegarde de Sagesse. En cas d'échec, la créature est renvoyée pendant 1 minute ou jusqu'à ce qu'elle subisse des dégâts.

#### Aura de dévotion (niveau 7)

Vous et les créatures amicales situées à 3 mètres de vous ne pouvez pas être charmés tant que vous êtes conscient.

Au niveau 18, la portée de cette aura passe à 9 mètres.

#### Pureté de l'esprit (niveau 15)

Vous êtes toujours sous l'effet du sort *protection contre le mal et le bien*.

#### Halo sacré (niveau 20)

Par une action, vous pouvez émaner une aura de lumière solaire. Pendant 1 minute :

- Vous émettez une lumière vive sur 9 mètres et une lumière faible sur 9 mètres supplémentaires
- Vous avez l'avantage aux jets de sauvegarde contre les sorts de fiélons et de morts-vivants
- Les ennemis dans la lumière vive subissent 10 dégâts radiants au début de leur tour

**Utilisations** : 1 par repos long

---

### Serment des Anciens

Le serment des Anciens est aussi vieux que les fées et les druides. Les paladins qui prêtent ce serment protègent la lumière contre les ténèbres.

#### Sorts de serment

| Niveau de paladin | Sorts |
|-------------------|-------|
| 3 | Communication avec les animaux, Collet |
| 5 | Rayon de lune, Pas brumeux |
| 9 | Croissance végétale, Protection contre une énergie |
| 13 | Tempête de grêle, Peau de pierre |
| 17 | Communion avec la nature, Passage par les arbres |

#### Conduite divine (niveau 3)

**Courroux de la nature** : Par une action, vous pouvez invoquer des vignes spectrales pour immobiliser un ennemi. Une créature à 3 mètres doit réussir un jet de sauvegarde de Force ou de Dextérité (son choix) ou être entravée. Elle peut répéter le jet à la fin de chacun de ses tours.

**Renvoi des infidèles** : Par une action, vous présentez votre symbole sacré et prononcez une prière contre les fées et les fiélons. Chaque fée ou fiélon à 9 mètres doit effectuer un jet de sauvegarde de Sagesse. En cas d'échec, la créature est renvoyée pendant 1 minute ou jusqu'à ce qu'elle subisse des dégâts.

#### Aura de garde (niveau 7)

Vous et les créatures amicales situées à 3 mètres de vous avez la résistance aux dégâts des sorts.

Au niveau 18, la portée de cette aura passe à 9 mètres.

#### Sentinelle immortelle (niveau 15)

Quand vous êtes réduit à 0 points de vie et n'êtes pas tué sur le coup, vous pouvez choisir de tomber à 1 point de vie à la place.

**Utilisations** : 1 par repos long

De plus, vous ne souffrez d'aucun des inconvénients de la vieillesse et vous ne pouvez pas être vieilli magiquement.

#### Champion de la nature (niveau 20)

Par une action, vous pouvez vous transformer en une force ancienne de la nature. Pendant 1 minute :

- Au début de chacun de vos tours, vous regagnez 10 points de vie
- Vous pouvez lancer des sorts de paladin avec un temps d'incantation d'une action en action bonus à la place
- Les ennemis à 3 mètres de vous ont un désavantage aux jets de sauvegarde contre vos sorts et capacités de Conduite divine

**Utilisations** : 1 par repos long

---

### Serment de Vengeance

Le serment de Vengeance est un engagement solennel de punir ceux qui ont commis un péché grave. Ces paladins mettent leur propre pureté de côté pour rendre justice.

#### Sorts de serment

| Niveau de paladin | Sorts |
|-------------------|-------|
| 3 | Malédiction, Marque du chasseur |
| 5 | Immobilisation de personne, Pas brumeux |
| 9 | Hâte, Protection contre une énergie |
| 13 | Bannissement, Porte dimensionnelle |
| 17 | Immobilisation de monstre, Scrutation |

#### Conduite divine (niveau 3)

**Conspuer l'ennemi** : Par une action, vous présentez votre symbole sacré et désignez une créature à 18 mètres. Elle doit effectuer un jet de sauvegarde de Sagesse. En cas d'échec, elle est effrayée pendant 1 minute ou jusqu'à ce qu'elle subisse des dégâts. Sa vitesse est de 0 pendant qu'elle est effrayée. En cas de réussite, sa vitesse est réduite de moitié pendant 1 minute.

**Voeu d'hostilité** : Par une action bonus, vous prononcez un voeu d'hostilité contre une créature à 3 mètres. Vous avez l'avantage aux jets d'attaque contre cette créature pendant 1 minute ou jusqu'à ce qu'elle tombe à 0 points de vie ou qu'elle soit inconsciente.

#### Représailles implacables (niveau 7)

Quand vous ou une créature à 3 mètres de vous est touchée par une attaque, vous pouvez utiliser votre réaction pour effectuer une attaque d'arme de corps à corps contre l'attaquant s'il est à votre portée.

#### Âme de vengeance (niveau 15)

Quand vous utilisez Voeu d'hostilité, vous gagnez également des attaques d'opportunité gratuites contre la cible qui ne consomment pas votre réaction.

#### Ange vengeur (niveau 20)

Par une action, vous vous transformez en avatar de la vengeance. Pendant 1 heure :

- Des ailes vous poussent, vous donnant une vitesse de vol de 18 mètres
- Vous émanez une aura de menace de 9 mètres. Quand un ennemi entre dans l'aura pour la première fois ou y commence son tour, il doit réussir un jet de sauvegarde de Sagesse ou être effrayé pendant 1 minute
- Une fois par tour, quand vous touchez une créature effrayée avec une attaque, vous infligez 1d8 dégâts psychiques supplémentaires

**Utilisations** : 1 par repos long

---

### Serment de Conquête

Les paladins du serment de Conquête cherchent la gloire au combat et la subjugation de leurs ennemis.

#### Sorts de serment

| Niveau de paladin | Sorts |
|-------------------|-------|
| 3 | Armure d'Agathys, Injonction |
| 5 | Immobilisation de personne, Arme spirituelle |
| 9 | Maléfice, Peur |
| 13 | Domination de bête, Peau de pierre |
| 17 | Nuage mortel, Domination de personne |

#### Conduite divine (niveau 3)

**Présence conquérante** : Par une action, vous forcez les créatures à 9 mètres à effectuer un jet de sauvegarde de Sagesse. En cas d'échec, elles sont effrayées pendant 1 minute. Une créature peut répéter le jet à la fin de chacun de ses tours.

**Frappe guidée** : Quand vous effectuez un jet d'attaque, vous pouvez utiliser votre Conduite divine pour gagner un bonus de +10 au jet. Vous faites ce choix après avoir vu le jet, mais avant de savoir s'il touche.

#### Aura de conquête (niveau 7)

Les créatures effrayées par vous et situées à 3 mètres ont une vitesse de 0 et subissent des dégâts psychiques égaux à la moitié de votre niveau de paladin au début de leur tour.

Au niveau 18, la portée de cette aura passe à 9 mètres.

#### Représailles méprisantes (niveau 15)

Quand une créature vous touche avec une attaque, vous pouvez utiliser votre réaction pour effectuer une attaque de corps à corps contre elle si elle est à votre portée.

#### Conquérant invincible (niveau 20)

Par une action, vous gagnez les bénéfices suivants pendant 1 minute :

- Vous avez la résistance à tous les dégâts
- Quand vous utilisez l'action Attaquer, vous pouvez effectuer une attaque supplémentaire en action bonus
- Vos attaques de corps à corps infligent un coup critique sur un 19 ou un 20

**Utilisations** : 1 par repos long

---

### Serment de Gloire

Les paladins du serment de Gloire croient que leur destinée est de s'inscrire dans la légende par des exploits héroïques.

#### Sorts de serment

| Niveau de paladin | Sorts |
|-------------------|-------|
| 3 | Héroïsme, Athlète incroyable |
| 5 | Amélioration de caractéristique, Arme magique |
| 9 | Hâte, Protection contre une énergie |
| 13 | Contrainte, Liberté de mouvement |
| 17 | Communion, Colonne de flamme |

#### Conduite divine (niveau 3)

**Prouesse inspirante** : Par une action bonus, vous pouvez distribuer des points de vie temporaires égaux à 2d8 + votre niveau de paladin, répartis comme vous le souhaitez entre les créatures à 9 mètres.

**Prouesse glorieuse** : Par une action bonus, vous pouvez vous et les alliés à 9 mètres ajouter un bonus aux dégâts égal à votre modificateur de Charisme pendant 1 minute.

#### Aura de vivacité (niveau 7)

Vous et les alliés à 3 mètres gagnez un bonus à la vitesse de déplacement égal à 3 mètres.

Au niveau 18, la portée de cette aura passe à 9 mètres.

#### Défiance glorieuse (niveau 15)

Quand vous ou un allié à 9 mètres subit des dégâts, vous pouvez utiliser votre réaction pour vous déplacer vers l'attaquant et effectuer une attaque de corps à corps contre lui.

#### Légende vivante (niveau 20)

Par une action bonus, vous devenez une légende vivante pendant 1 minute :

- Vous avez l'avantage aux jets de Charisme
- Une fois par tour, quand vous ratez un jet d'attaque ou une sauvegarde, vous pouvez utiliser votre réaction pour réussir à la place

**Utilisations** : 1 par repos long

---

### Serment de Rédemption

Les paladins du serment de Rédemption croient que toute créature peut être rachetée et cherchent la paix avant tout.

#### Sorts de serment

| Niveau de paladin | Sorts |
|-------------------|-------|
| 3 | Sanctuaire, Sommeil |
| 5 | Apaisement des émotions, Immobilisation de personne |
| 9 | Contre-sort, Lenteur |
| 13 | Résilience d'Otiluke, Peau de pierre |
| 17 | Immobilisation de monstre, Mur de force |

#### Conduite divine (niveau 3)

**Émissaire de la paix** : Par une action bonus, vous gagnez un bonus de +5 aux jets de Charisme (Persuasion) pendant 10 minutes.

**Réprimande des violents** : Quand un ennemi à 9 mètres inflige des dégâts à vous ou une créature autre que lui, vous pouvez utiliser votre réaction pour lui infliger des dégâts radiants égaux aux dégâts infligés.

#### Aura du gardien (niveau 7)

Quand une créature à 3 mètres subit des dégâts, vous pouvez utiliser votre réaction pour transférer ces dégâts à vous-même (les dégâts ne sont pas réduits).

Au niveau 18, la portée de cette aura passe à 9 mètres.

#### Esprit protecteur (niveau 15)

Vous gagnez la résistance aux dégâts contondants, perçants et tranchants des attaques non magiques.

#### Émissaire de rédemption (niveau 20)

Par une action bonus pendant 1 minute, vous gagnez :

- Résistance à tous les dégâts infligés par d'autres créatures (les attaques, sorts et effets)
- Chaque fois qu'une créature vous inflige des dégâts, elle subit des dégâts radiants égaux à la moitié de ce qu'elle vous a infligé

**Utilisations** : 1 par repos long
