---
Class: Class

aliases:
  - Ensorceleur
  - ensorceleur
  - Sorcerer
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d6
saving_throws:
  - con
  - cha
armor_proficiencies: []
weapon_proficiencies:
  - dague
  - flechette
  - fronde
  - baton
  - arbalete legere
tool_proficiencies: []
skill_choices: 2
skill_options:
  - Arcanes
  - Intimidation
  - Intuition
  - Persuasion
  - Religion
  - Tromperie
spellcasting_ability: cha
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Incantation"
      - "Origine magique"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Source de magie"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "Métamagie (2 options)"
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
      - "Capacité d'origine"
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
      - "Métamagie (3e option)"
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
      - "Capacité d'origine"
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
      - "Métamagie (4e option)"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "Capacité d'origine"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Restauration magique"
starting_equipment_draft: "- Une arbalète légère et 20 carreaux OU une arme courante - Une sacoche à composantes OU un focaliseur arcanique - Un sac de donjon OU un sac d'explorateur - Deux dagues"
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
        item: "[[Sac d'exploration souterraine]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'explorateur]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        item: "[[Dague]]"
        quantity: 2
---



# Ensorceleur

Les ensorceleurs possèdent une magie innée qui prend sa source dans un lignage exotique, une quelconque influence d'Outremonde ou une exposition à une force cosmique inouïe. Contrairement aux magiciens, ils ne dépendent pas de grimoires ni de patrons.

## Tableau de progression

| Niveau | Bonus | Capacités | Pts Sorcellerie | Sorts mineurs | Sorts connus |
|--------|-------|-----------|-----------------|---------------|--------------|
| 1 | +2 | Incantation, Origine magique | - | 4 | 2 |
| 2 | +2 | Source de magie | 2 | 4 | 3 |
| 3 | +2 | Métamagie (2 options) | 3 | 4 | 4 |
| 4 | +2 | Amélioration de caractéristiques | 4 | 5 | 5 |
| 5 | +3 | - | 5 | 5 | 6 |
| 6 | +3 | Capacité d'origine | 6 | 5 | 7 |
| 7 | +3 | - | 7 | 5 | 8 |
| 8 | +3 | Amélioration de caractéristiques | 8 | 5 | 9 |
| 9 | +4 | - | 9 | 5 | 10 |
| 10 | +4 | Métamagie (3e option) | 10 | 6 | 11 |
| 11 | +4 | - | 11 | 6 | 12 |
| 12 | +4 | Amélioration de caractéristiques | 12 | 6 | 12 |
| 13 | +5 | - | 13 | 6 | 13 |
| 14 | +5 | Capacité d'origine | 14 | 6 | 13 |
| 15 | +5 | - | 15 | 6 | 14 |
| 16 | +5 | Amélioration de caractéristiques | 16 | 6 | 14 |
| 17 | +6 | Métamagie (4e option) | 17 | 6 | 15 |
| 18 | +6 | Capacité d'origine | 18 | 6 | 15 |
| 19 | +6 | Amélioration de caractéristiques | 19 | 6 | 15 |
| 20 | +6 | Restauration magique | 20 | 6 | 15 |

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

**Dés de vie** : 1d6 par niveau d'ensorceleur
**Points de vie au niveau 1** : 6 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d6 (ou 4) + modificateur de Constitution

### Maîtrises

- **Armures**: Aucune
- **Armes**: Dague, fléchette, fronde, bâton, arbalète légère
- **Outils**: Aucun
- **Jets de sauvegarde**: Constitution, Charisme
- **Compétences**: Choisissez 2 parmi Arcanes, Intimidation, Intuition, Persuasion, Religion, Tromperie

### Équipement de départ

- Une arbalète légère et 20 carreaux OU une arme courante
- Une sacoche à composantes OU un focaliseur arcanique
- Un sac de donjon OU un sac d'explorateur
- Deux dagues

---

## Capacités de classe

### Incantation (niveau 1)

L'ensorceleur connaît ses sorts de manière innée et ne les prépare pas.

**Caractéristique d'incantation** : Charisme
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Charisme
**Modificateur d'attaque** : bonus de maîtrise + modificateur de Charisme
**Focaliseur** : Focaliseur arcanique

### Origine magique (niveau 1)

Choisissez une origine magique qui vous confère des capacités aux niveaux 1, 6, 14 et 18.

### Source de magie (niveau 2)

Vous gagnez des points de sorcellerie que vous pouvez utiliser pour :

**Flexibilité des emplacements** : Vous pouvez transformer des points de sorcellerie en emplacements de sorts ou vice versa :

| Niveau d'emplacement | Coût en points |
|---------------------|----------------|
| 1er | 2 |
| 2e | 3 |
| 3e | 5 |
| 4e | 6 |
| 5e | 7 |

Vous ne pouvez pas créer d'emplacements au-dessus du niveau 5. Les emplacements créés disparaissent après un repos long.

### Métamagie (niveau 3, 10, 17)

Vous gagnez la capacité de modifier vos sorts. Choisissez 2 options au niveau 3, une 3e au niveau 10, et une 4e au niveau 17.

#### Sort accéléré (2 points)
Lorsque vous lancez un sort avec un temps d'incantation d'1 action, vous pouvez dépenser 2 points de sorcellerie pour le lancer en action bonus à la place.

#### Sort ample (1 point)
Lorsque vous lancez un sort avec une portée de 1,5 mètre ou plus, vous pouvez dépenser 1 point de sorcellerie pour doubler la portée du sort. Pour les sorts de contact, la portée devient 9 mètres.

#### Sort étendu (1 point)
Lorsque vous lancez un sort avec une durée d'1 minute ou plus, vous pouvez dépenser 1 point de sorcellerie pour doubler sa durée (maximum 24 heures).

#### Sort intensifié (3 points)
Lorsque vous lancez un sort qui oblige une créature à faire un jet de sauvegarde, vous pouvez dépenser 3 points de sorcellerie pour imposer à une cible un désavantage à son premier jet de sauvegarde contre le sort.

#### Sort jumelé (coût variable)
Lorsque vous lancez un sort qui cible une seule créature et n'a pas une portée personnelle, vous pouvez dépenser un nombre de points égal au niveau du sort (minimum 1) pour cibler une deuxième créature à portée.

#### Sort prévenant (1 point)
Lorsque vous lancez un sort qui oblige d'autres créatures à faire un jet de sauvegarde, vous pouvez protéger certaines d'entre elles. Dépensez 1 point et choisissez un nombre de créatures égal à votre modificateur de Charisme (minimum 1). Ces créatures réussissent automatiquement leur sauvegarde et ne subissent aucun dégât.

#### Sort renforcé (1 point)
Lorsque vous lancez les dés de dégâts d'un sort, vous pouvez dépenser 1 point de sorcellerie pour relancer un nombre de dés égal à votre modificateur de Charisme (minimum 1). Vous devez utiliser les nouveaux résultats.

#### Sort subtil (1 point)
Lorsque vous lancez un sort, vous pouvez dépenser 1 point de sorcellerie pour le lancer sans composante verbale ni somatique.

### Restauration magique (niveau 20)

Vous récupérez 4 points de sorcellerie dépensés lorsque vous terminez un repos court.

---

## Origines magiques

### Lignée draconique

Votre magie innée provient de l'influence draconique dans votre lignée.

#### Ancêtre draconique (niveau 1)
Choisissez un type de dragon parmi la liste. Ce choix détermine votre type de dégâts associé et les capacités futures.

| Dragon | Type de dégâts |
|--------|---------------|
| Blanc, Argent | Froid |
| Bleu, Bronze | Foudre |
| Noir, Cuivre | Acide |
| Or, Laiton, Rouge | Feu |
| Vert | Poison |

Vous parlez, lisez et écrivez le draconique. De plus, lorsque vous interagissez avec des dragons, votre bonus de maîtrise est doublé pour les jets de Charisme.

#### Résistance draconique (niveau 1)
Votre maximum de points de vie augmente de 1 par niveau d'ensorceleur. De plus, lorsque vous ne portez pas d'armure, votre CA = 13 + modificateur de Dextérité.

#### Affinité élémentaire (niveau 6)
Lorsque vous lancez un sort qui inflige des dégâts du type associé à votre ancêtre, vous pouvez ajouter votre modificateur de Charisme aux dégâts. De plus, vous pouvez dépenser 1 point de sorcellerie pour gagner la résistance à ce type de dégâts pendant 1 heure.

#### Ailes draconiques (niveau 14)
Par une action bonus, vous pouvez faire apparaître des ailes spectrales dans votre dos. Vous gagnez une vitesse de vol égale à votre vitesse de marche actuelle. Les ailes durent jusqu'à ce que vous les renvoyiez (action bonus), que vous soyez neutralisé, ou que vous mouriez.

#### Présence draconique (niveau 18)
Par une action, vous pouvez dépenser 5 points de sorcellerie pour dégager une aura de terreur ou de fascination dans un rayon de 18 mètres. Pendant 1 minute (concentration), les créatures hostiles qui commencent leur tour dans l'aura doivent réussir un jet de sauvegarde de Sagesse ou être charmées (fascination) ou effrayées (terreur) jusqu'à la fin de leur prochain tour.

---

### Magie sauvage

Votre magie innée provient des forces brutes du chaos.

#### Pic de magie sauvage (niveau 1)
Après avoir lancé un sort d'ensorceleur de niveau 1 ou plus, le MD peut vous demander de lancer 1d20. Sur un 1, lancez sur la table des Pics de magie sauvage pour déterminer un effet aléatoire.

#### Marée du chaos (niveau 1)
Vous pouvez manipuler les forces du hasard. Une fois avant de terminer un repos long, immédiatement après avoir lancé un d20 pour un jet d'attaque, de caractéristique ou de sauvegarde, vous pouvez lancer 1d4 et l'appliquer comme bonus ou malus au résultat.

#### Chance forcée (niveau 6)
Lorsqu'une créature que vous pouvez voir dans un rayon de 18 mètres fait un jet d'attaque, de caractéristique ou de sauvegarde, vous pouvez utiliser votre réaction et dépenser 2 points de sorcellerie pour lancer 1d4 et l'appliquer comme bonus ou malus au résultat. Vous pouvez le faire après le jet mais avant de connaître le résultat.

#### Chaos contrôlé (niveau 14)
Lorsque vous lancez sur la table des Pics de magie sauvage, vous pouvez lancer deux fois et utiliser l'un ou l'autre des résultats.

#### Bombardement de sort (niveau 18)
Une fois par tour, lorsque vous lancez les dés de dégâts d'un sort et obtenez le maximum sur au moins un dé, vous pouvez relancer ce dé une fois et ajouter le résultat aux dégâts.

---

### Âme divine

Votre magie provient d'un lien avec le divin.

#### Magie divine (niveau 1)
Vous pouvez apprendre des sorts de la liste de clerc en plus de celle d'ensorceleur. Ces sorts comptent comme des sorts d'ensorceleur pour vous.

#### Faveur des dieux (niveau 1)
Si vous échouez un jet de sauvegarde ou ratez une attaque, vous pouvez lancer 2d4 et ajouter le résultat. Une fois utilisé, vous devez terminer un repos court ou long avant de réutiliser cette capacité.

#### Soin renforcé (niveau 6)
Lorsque vous ou un allié dans un rayon de 1,5 mètre lancez les dés pour récupérer des points de vie, vous pouvez dépenser 1 point de sorcellerie pour relancer n'importe quels dés une fois.

#### Ailes d'Outremonde (niveau 14)
Par une action bonus, vous pouvez faire apparaître des ailes spectrales (semblables à celles d'un ange ou d'un démon selon votre nature). Vous gagnez une vitesse de vol de 9 mètres.

#### Récupération surnaturelle (niveau 18)
Quand vous avez moins de la moitié de vos PV max et n'êtes pas neutralisé, vous pouvez utiliser une action bonus pour regagner un nombre de PV égal à la moitié de votre maximum. Une fois utilisé, vous devez terminer un repos long.

---

### Esprit aberrant

Votre magie provient d'une connexion avec des entités d'outre-monde.

#### Sorts psioniques (niveau 1)
Vous apprenez des sorts bonus et pouvez les lancer en dépensant des points de sorcellerie au lieu de mana.

#### Parole télépathique (niveau 1)
Par une action bonus, vous pouvez établir un lien télépathique avec une créature à 9 mètres. Le lien dure un nombre de minutes égal à votre niveau d'ensorceleur.

#### Prana psionique (niveau 6)
Lorsque vous lancez un sort de 1er niveau ou plus de votre liste de sorts psioniques, vous pouvez le lancer en dépensant des points de sorcellerie égaux au niveau du sort. Vous n'avez besoin d'aucune composante.

#### Défenses psychiques (niveau 6)
Vous gagnez la résistance aux dégâts psychiques et l'avantage aux jets de sauvegarde contre les effets de charme et de terreur.

#### Révélation de l'esprit (niveau 14)
Si vous n'êtes pas neutralisé, les créatures subissent un désavantage à leurs jets d'attaque contre vous.

#### Forme de distorsion (niveau 18)
Par une action bonus, vous pouvez dépenser 5 points de sorcellerie pour vous transformer en une forme aberrante pendant 10 minutes. Vous gagnez une vitesse de vol de 12 mètres, résistance à tous les dégâts sauf force et psychiques, et pouvez vous déplacer à travers les créatures et objets.
