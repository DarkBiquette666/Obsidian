---
Class: Class

aliases:
  - Barde
  - barde
  - Bard
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d8
saving_throws:
  - dex
  - cha
armor_proficiencies:
  - legeres
weapon proficiencies:
  - courantes
  - arbalete de poing
  - epee courte
  - epee longue
  - rapiere
tool_proficiencies:
  - trois instruments de musique
skill_choices: 3
skill_options: []
spellcasting_ability: cha
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Incantation"
      - "Inspiration bardique"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Touche-à-tout"
      - "Chant reposant"
  - type: ClassLevelEntry
    level: 3
    proficiency_bonus: 2
    features:
      - "Collège bardique"
      - "Expertise"
  - type: ClassLevelEntry
    level: 4
    proficiency_bonus: 2
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 5
    proficiency_bonus: 3
    features:
      - "Source d'inspiration"
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "Contre-charme"
      - "Capacité de collège"
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
      - "Chant reposant (d8)"
  - type: ClassLevelEntry
    level: 10
    proficiency_bonus: 4
    features:
      - "Secrets magiques"
      - "Expertise"
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
      - "Chant reposant (d10)"
  - type: ClassLevelEntry
    level: 14
    proficiency_bonus: 5
    features:
      - "Secrets magiques"
      - "Capacité de collège"
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
      - "Chant reposant (d12)"
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "Secrets magiques"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Inspiration supérieure"
starting_equipment_draft: "- Une rapière, une épée longue, OU une arme courante - Un sac de diplomate OU un sac d'artiste - Un luth OU un autre instrument de musique - Une armure de cuir et une dague"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Rapière]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Épée longue]]"
        quantity: 1
      - type: CategoryItem
        category: "Arme courante"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Sac de diplomate]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Sac d'artiste]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Luth]]"
        quantity: 1
      - type: CategoryItem
        category: "Instrument de musique"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        item: "[[Armure de cuir]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Dague]]"
        quantity: 1
---



# Barde

Le barde est un maître des mots, de la musique et de la magie. Ces artistes polyvalents utilisent leur art pour inspirer leurs alliés, démoraliser leurs ennemis et tisser des sortilèges puissants.

## Tableau de progression

| Niveau | Bonus | Capacités | Inspiration | Sorts mineurs | Sorts connus |
|--------|-------|-----------|-------------|---------------|--------------|
| 1 | +2 | Incantation, Inspiration bardique | d6 | 2 | 4 |
| 2 | +2 | Touche-à-tout, Chant reposant | d6 | 2 | 5 |
| 3 | +2 | Collège bardique, Expertise | d6 | 2 | 6 |
| 4 | +2 | Amélioration de caractéristiques | d6 | 3 | 7 |
| 5 | +3 | Source d'inspiration | d8 | 3 | 8 |
| 6 | +3 | Contre-charme, Capacité de collège | d8 | 3 | 9 |
| 7 | +3 | - | d8 | 3 | 10 |
| 8 | +3 | Amélioration de caractéristiques | d8 | 3 | 11 |
| 9 | +4 | Chant reposant (d8) | d8 | 3 | 12 |
| 10 | +4 | Secrets magiques, Expertise | d10 | 4 | 14 |
| 11 | +4 | - | d10 | 4 | 15 |
| 12 | +4 | Amélioration de caractéristiques | d10 | 4 | 15 |
| 13 | +5 | Chant reposant (d10) | d10 | 4 | 16 |
| 14 | +5 | Secrets magiques, Capacité de collège | d10 | 4 | 18 |
| 15 | +5 | - | d12 | 4 | 19 |
| 16 | +5 | Amélioration de caractéristiques | d12 | 4 | 19 |
| 17 | +6 | Chant reposant (d12) | d12 | 4 | 20 |
| 18 | +6 | Secrets magiques | d12 | 4 | 22 |
| 19 | +6 | Amélioration de caractéristiques | d12 | 4 | 22 |
| 20 | +6 | Inspiration supérieure | d12 | 4 | 22 |

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

**Dés de vie** : 1d8 par niveau de barde
**Points de vie au niveau 1** : 8 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d8 (ou 5) + modificateur de Constitution

### Maîtrises

- **Armures** : Armures légères
- **Armes** : Armes courantes, arbalètes de poing, épées courtes, épées longues, rapières
- **Outils** : Trois instruments de musique de votre choix
- **Jets de sauvegarde** : Dextérité, Charisme
- **Compétences** : Choisissez 3 compétences de votre choix

### Équipement de départ

- Une rapière, une épée longue, OU une arme courante
- Un sac de diplomate OU un sac d'artiste
- Un luth OU un autre instrument de musique
- Une armure de cuir et une dague

---

## Capacités de classe

### Incantation (niveau 1)

Vous avez appris à démêler et remodeler le tissu de la réalité grâce à la musique et à l'art oratoire.

**Caractéristique d'incantation** : Charisme
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur de Charisme
**Modificateur d'attaque** : bonus de maîtrise + modificateur de Charisme
**Focaliseur** : Instrument de musique
**Sorts préparés** : modificateur de Charisme + niveau de barde

### Inspiration bardique (niveau 1)

Par une action bonus, vous pouvez inspirer une créature autre que vous à 18 mètres qui peut vous entendre. Elle gagne un dé d'Inspiration bardique qu'elle peut ajouter à un jet d'attaque, de caractéristique ou de sauvegarde dans les 10 prochaines minutes. Le dé peut être lancé après le jet mais avant de connaître le résultat.

Nombre d'utilisations : modificateur de Charisme (minimum 1)
Récupération : repos long (repos court à partir du niveau 5)

Le dé augmente avec le niveau :
- d6 (niveaux 1-4)
- d8 (niveaux 5-9)
- d10 (niveaux 10-14)
- d12 (niveaux 15-20)

### Touche-à-tout (niveau 2)

Vous pouvez ajouter la moitié de votre bonus de maîtrise (arrondi à l'inférieur) à tous les jets de caractéristique qui n'incluent pas déjà votre bonus de maîtrise.

### Chant reposant (niveau 2)

Pendant un repos court, vous pouvez jouer de la musique apaisante. Les créatures qui récupèrent des points de vie en dépensant des dés de vie regagnent des PV supplémentaires :
- d6 (niveaux 2-8)
- d8 (niveaux 9-12)
- d10 (niveaux 13-16)
- d12 (niveaux 17-20)

### Collège bardique (niveau 3)

Choisissez un collège bardique qui vous confère des capacités aux niveaux 3, 6 et 14.

### Expertise (niveau 3, 10)

Choisissez deux de vos maîtrises de compétences (ou une compétence et les outils de voleur). Votre bonus de maîtrise est doublé pour tout jet de caractéristique utilisant ces maîtrises.

Au niveau 10, choisissez deux maîtrises supplémentaires.

### Source d'inspiration (niveau 5)

Vous récupérez vos utilisations d'Inspiration bardique après un repos court ou long.

### Contre-charme (niveau 6)

Par une action, vous pouvez jouer de la musique pour rompre les effets de charme et de terreur. Vous et les créatures amies dans un rayon de 9 mètres qui peuvent vous entendre ont l'avantage aux jets de sauvegarde contre les effets de charme et de terreur tant que vous jouez (concentration, jusqu'à 1 minute).

### Secrets magiques (niveau 10, 14, 18)

Choisissez deux sorts de n'importe quelle liste de sorts. Ces sorts comptent comme des sorts de barde pour vous.

### Inspiration supérieure (niveau 20)

Lorsque vous faites un jet d'initiative et n'avez aucune utilisation d'Inspiration bardique restante, vous en récupérez une.

---

## Collèges bardiques

### Collège du Savoir

Les bardes du Collège du Savoir collectent des connaissances de toutes sources, expertises et techniques diverses.

#### Maîtrises supplémentaires (niveau 3)
Vous gagnez la maîtrise de trois compétences de votre choix.

#### Mots cinglants (niveau 3)
Lorsqu'une créature que vous pouvez voir dans un rayon de 18 mètres fait un jet d'attaque, de caractéristique ou de dégâts, vous pouvez utiliser votre réaction pour dépenser un dé d'Inspiration bardique et soustraire le résultat du jet de la créature. Vous pouvez choisir d'utiliser cette capacité après le jet mais avant de connaître si elle réussit ou échoue.

#### Secrets magiques supplémentaires (niveau 6)
Vous apprenez deux sorts de n'importe quelle classe. Ces sorts doivent être d'un niveau que vous pouvez lancer.

#### Talent hors pair (niveau 14)
Lorsque vous faites un jet de caractéristique, vous pouvez dépenser une utilisation d'Inspiration bardique et ajouter le résultat à votre propre jet. Vous pouvez choisir après le jet mais avant de connaître le résultat.

---

### Collège de la Vaillance

Les bardes du Collège de la Vaillance sont des guerriers-poètes qui chantent les exploits héroïques et inspirent le courage sur le champ de bataille.

#### Maîtrises supplémentaires (niveau 3)
Vous gagnez la maîtrise des armures intermédiaires, des boucliers et des armes de guerre.

#### Inspiration martiale (niveau 3)
Une créature qui utilise votre dé d'Inspiration bardique peut l'ajouter à un jet de dégâts d'arme ou l'ajouter à sa CA en réaction contre une attaque qui la touche (avant de savoir si l'attaque touche).

#### Attaque supplémentaire (niveau 6)
Vous pouvez attaquer deux fois au lieu d'une lorsque vous utilisez l'action Attaquer.

#### Magie de combat (niveau 14)
Lorsque vous utilisez votre action pour lancer un sort de barde, vous pouvez effectuer une attaque d'arme en action bonus.

---

### Collège des Épées

Les bardes du Collège des Épées sont des artistes martiaux qui mélangent l'art du combat à leurs performances.

#### Maîtrises supplémentaires (niveau 3)
Vous gagnez la maîtrise des armures intermédiaires et du cimeterre. Si vous maîtrisez une arme de corps à corps, vous pouvez l'utiliser comme focaliseur.

#### Style de combat (niveau 3)
Choisissez un style de combat :
- **Duel** : +2 aux dégâts avec une arme de corps à corps tenue à une main
- **Combat à deux armes** : Ajoutez votre modificateur aux dégâts de la seconde attaque

#### Floriture de lame (niveau 3)
Lorsque vous touchez avec une attaque d'arme, vous pouvez dépenser une utilisation d'Inspiration bardique pour effectuer une floriture :
- **Floriture défensive** : Ajoutez le dé aux dégâts et à votre CA jusqu'au début de votre prochain tour
- **Floriture tranchante** : Ajoutez le dé aux dégâts et infligez le même montant à une autre créature à 1,5 m
- **Floriture mobile** : Ajoutez le dé aux dégâts et déplacez-vous sans provoquer d'attaque d'opportunité de la cible

#### Attaque supplémentaire (niveau 6)
Vous pouvez attaquer deux fois au lieu d'une lorsque vous utilisez l'action Attaquer.

#### Floriture de maître (niveau 14)
Lorsque vous utilisez une Floriture de lame, vous pouvez lancer un d6 au lieu de dépenser un dé d'Inspiration bardique.

---

### Collège des Murmures

Les bardes du Collège des Murmures utilisent leur art pour semer la peur, manipuler et extraire des secrets.

#### Lames psychiques (niveau 3)
Lorsque vous touchez une créature avec une attaque d'arme, vous pouvez dépenser une utilisation d'Inspiration bardique pour infliger 2d6 dégâts psychiques supplémentaires. Les dégâts augmentent : 3d6 (niveau 5), 5d6 (niveau 10), 8d6 (niveau 15).

#### Mots de terreur (niveau 3)
Si vous parlez seul à seul avec une créature humanoïde pendant au moins 1 minute, vous pouvez tenter de semer des graines de peur. Elle doit réussir un jet de sauvegarde de Sagesse ou être effrayée par vous ou une créature de votre choix pendant 1 heure.

#### Cape d'ombres (niveau 6)
Lorsque vous tuez une créature humanoïde, vous pouvez capturer son ombre avec votre magie. Pendant 1 heure, vous pouvez utiliser votre action pour prendre son apparence et accéder à ses souvenirs généraux. DD de sauvegarde d'Intuition contre votre DD de sorts pour percer le déguisement.

#### Maîtrise de la manipulation (niveau 14)
Vous pouvez lancer *domination de personne* une fois sans dépenser de mana. Vous devez terminer un repos long avant de réutiliser cette capacité.

---

### Collège de l'Éloquence

Les bardes du Collège de l'Éloquence sont des maîtres de l'art oratoire et de la persuasion.

#### Langue d'argent (niveau 3)
Lorsque vous faites un jet de Persuasion ou de Tromperie, vous pouvez traiter un résultat de 9 ou moins sur le dé comme un 10.

#### Mots démoralisants (niveau 3)
Par une action bonus, vous pouvez dépenser une utilisation d'Inspiration bardique pour murmurer des mots déstabilisants. Une créature à 18 mètres doit réussir un jet de sauvegarde de Sagesse ou subir un désavantage à son prochain jet de sauvegarde avant la fin de votre prochain tour.

#### Inspiration irrépressible (niveau 6)
Lorsqu'une créature ajoute votre dé d'Inspiration bardique à un jet et échoue, elle peut conserver le dé.

#### Inspiration universelle (niveau 6)
Lorsque vous utilisez Inspiration bardique, vous pouvez cibler deux créatures au lieu d'une. Chacune gagne un dé.

#### Cape d'éloquence (niveau 14)
Par une action bonus, vous pouvez vous envelopper d'une cape magique qui vous confère des avantages pendant 1 minute :
- Avantage aux jets de Persuasion
- Les créatures qui vous attaquent font un jet de sauvegarde de Sagesse ou ont un désavantage
