---
Class: Class

aliases:
  - Magicien
  - magicien
  - Wizard
tags:
  - classe
  - creation-personnage
  - lanceur-de-sorts
hit_dice: d6
saving_throws:
  - int
  - sag
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
  - Histoire
  - Intuition
  - Investigation
  - Medecine
  - Religion
spellcasting_ability: int
progression:
  - type: ClassLevelEntry
    level: 1
    proficiency_bonus: 2
    features:
      - "Incantation"
      - "Restauration arcanique"
  - type: ClassLevelEntry
    level: 2
    proficiency_bonus: 2
    features:
      - "Tradition arcanique"
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
  - type: ClassLevelEntry
    level: 6
    proficiency_bonus: 3
    features:
      - "Capacité de tradition"
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
      - "Capacité de tradition"
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
      - "Capacité de tradition"
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
  - type: ClassLevelEntry
    level: 18
    proficiency_bonus: 6
    features:
      - "Maîtrise des sorts"
  - type: ClassLevelEntry
    level: 19
    proficiency_bonus: 6
    features:
      - "Amélioration de caractéristiques"
  - type: ClassLevelEntry
    level: 20
    proficiency_bonus: 6
    features:
      - "Sorts de prédilection"
starting_equipment_draft: "- Un bâton OU une dague - Une sacoche à composantes OU un focaliseur arcanique - Un sac d'érudit OU un sac d'explorateur - Un grimoire"
starting_equipment:
  - type: EquipmentGroup
    selection_mode: OR
    items:
      - type: SpecificItem
        item: "[[Bâton]]"
        quantity: 1
      - type: SpecificItem
        item: "[[Dague]]"
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
        item: "[[Sac d'explorateur]]"
        quantity: 1
  - type: EquipmentGroup
    selection_mode: AND
    items:
      - type: SpecificItem
        item: "[[Livre de Sorts (Vide)]]"
        quantity: 1
---



# Magicien

Les magiciens sont des utilisateurs puissants de la magie arcanique. Ils lancent des sorts de feu, de foudre, d'illusion et de contrôle des esprits. Leur magie est fondée sur l'étude et l'apprentissage plutôt que sur l'intuition naturelle.

## Tableau de progression

| Niveau | Bonus | Capacités | Sorts mineurs |
|--------|-------|-----------|---------------|
| 1 | +2 | Incantation, Restauration arcanique | 3 |
| 2 | +2 | Tradition arcanique | 3 |
| 3 | +2 | - | 3 |
| 4 | +2 | Amélioration de caractéristiques | 4 |
| 5 | +3 | - | 4 |
| 6 | +3 | Capacité de tradition | 4 |
| 7 | +3 | - | 4 |
| 8 | +3 | Amélioration de caractéristiques | 4 |
| 9 | +4 | - | 4 |
| 10 | +4 | Capacité de tradition | 5 |
| 11 | +4 | - | 5 |
| 12 | +4 | Amélioration de caractéristiques | 5 |
| 13 | +5 | - | 5 |
| 14 | +5 | Capacité de tradition | 5 |
| 15 | +5 | - | 5 |
| 16 | +5 | Amélioration de caractéristiques | 5 |
| 17 | +6 | - | 5 |
| 18 | +6 | Maîtrise des sorts | 5 |
| 19 | +6 | Amélioration de caractéristiques | 5 |
| 20 | +6 | Sorts de prédilection | 5 |

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

**Dés de vie** : 1d6 par niveau de magicien
**Points de vie au niveau 1** : 6 + modificateur de Constitution
**Points de vie aux niveaux suivants** : 1d6 (ou 4) + modificateur de Constitution

### Maîtrises

- **Armures** : Aucune
- **Armes** : Dague, fléchette, fronde, bâton, arbalète légère
- **Outils** : Aucun
- **Jets de sauvegarde** : Intelligence, Sagesse
- **Compétences** : Choisissez 2 parmi Arcanes, Histoire, Intuition, Investigation, Médecine, Religion

### Équipement de départ

- Un bâton OU une dague
- Une sacoche à composantes OU un focaliseur arcanique
- Un sac d'érudit OU un sac d'explorateur
- Un grimoire

---

## Capacités de classe

### Incantation (niveau 1)

Le magicien utilise un grimoire et prépare ses sorts chaque jour.

**Caractéristique d'incantation** : Intelligence
**DD de sauvegarde** : 8 + bonus de maîtrise + modificateur d'Intelligence
**Modificateur d'attaque** : bonus de maîtrise + modificateur d'Intelligence
**Focaliseur** : Focaliseur arcanique ou grimoire
**Sorts préparés** : niveau de magicien + modificateur d'Intelligence

#### Grimoire
Votre grimoire contient 6 sorts de niveau 1 au niveau 1. À chaque montée de niveau, vous ajoutez 2 sorts de magicien de votre choix d'un niveau que vous pouvez lancer.

**Copier des sorts** : Vous pouvez copier des sorts de magicien trouvés dans d'autres grimoires ou parchemins. Le coût est de 50 po et 2 heures par niveau de sort.

**Remplacer le grimoire** : Si vous perdez votre grimoire, vous pouvez en créer un nouveau et y transcrire vos sorts préparés (10 po et 1 heure par niveau de sort).

### Restauration arcanique (niveau 1)

Une fois par jour lorsque vous terminez un repos court, vous pouvez récupérer des emplacements de sorts dépensés. La somme des niveaux des emplacements ne peut pas excéder la moitié de votre niveau de magicien (arrondi à l'inférieur), et aucun emplacement ne peut être de niveau 6 ou plus.

### Tradition arcanique (niveau 2)

Choisissez une tradition arcanique parmi les 8 écoles de magie. Elle vous confère des capacités aux niveaux 2, 6, 10 et 14.

### Maîtrise des sorts (niveau 18)

Choisissez un sort de magicien de niveau 1 et un de niveau 2 dans votre grimoire. Vous pouvez lancer ces sorts à leur niveau le plus bas sans dépenser de mana tant qu'ils sont préparés.

### Sorts de prédilection (niveau 20)

Choisissez deux sorts de magicien de niveau 3 dans votre grimoire. Ces sorts sont toujours préparés et ne comptent pas dans le nombre de sorts préparés. Vous pouvez lancer chacun une fois sans dépenser de mana. Vous devez terminer un repos court ou long pour réutiliser cette capacité.

---

## Traditions arcaniques

### École d'Abjuration

Les abjurateurs excellent dans les sorts de protection et de bannissement.

#### Érudit en abjuration (niveau 2)
Le temps et l'argent nécessaires pour copier un sort d'abjuration sont réduits de moitié.

#### Protection arcanique (niveau 2)
Lorsque vous lancez un sort d'abjuration de niveau 1 ou plus, vous créez un sceau magique protecteur. Le sceau a un nombre de points de vie égal à 2 fois votre niveau de magicien + votre modificateur d'Intelligence. Lorsque vous subissez des dégâts, le sceau absorbe les dégâts en premier.

Le sceau ne peut pas avoir plus de PV que ce maximum. Lancer un sort d'abjuration de niveau 1 ou plus restaure 2 x niveau du sort PV au sceau.

#### Protection projetée (niveau 6)
Lorsqu'une créature à 9 mètres de vous subit des dégâts, vous pouvez utiliser votre réaction pour faire absorber ces dégâts par votre sceau.

#### Abjuration améliorée (niveau 10)
Lorsque vous lancez un sort d'abjuration qui nécessite un jet de caractéristique (comme *dissipation de la magie*), vous ajoutez votre bonus de maîtrise au jet.

#### Résistance aux sorts (niveau 14)
Vous avez l'avantage aux jets de sauvegarde contre les sorts. De plus, vous avez la résistance aux dégâts des sorts.

---

### École de Conjuration

Les invocateurs excellent à téléporter des créatures et des objets.

#### Érudit en conjuration (niveau 2)
Le temps et l'argent nécessaires pour copier un sort de conjuration sont réduits de moitié.

#### Invocation mineure (niveau 2)
Par une action, vous pouvez invoquer un objet inanimé non magique dans votre main ou au sol. L'objet doit faire au maximum 1 mètre de côté et peser 5 kg ou moins, et sa forme doit être celle d'un objet non magique que vous avez déjà vu. L'objet dure 1 heure avant de disparaître.

#### Permutation (niveau 6)
Par une action, vous pouvez vous téléporter jusqu'à 9 mètres dans un espace inoccupé visible. Alternativement, vous pouvez choisir un espace à portée occupé par une créature de taille P ou M consentante et échanger de place avec elle.

#### Invocation consciencieuse (niveau 10)
Votre concentration ne peut pas être brisée par des dégâts tant que vous vous concentrez sur un sort de conjuration.

#### Convocations coriaces (niveau 14)
Les créatures que vous invoquez ou créez avec un sort de conjuration ont 30 PV temporaires.

---

### École de Divination

Les devins spécialisent dans la perception du futur et des vérités cachées.

#### Érudit en divination (niveau 2)
Le temps et l'argent nécessaires pour copier un sort de divination sont réduits de moitié.

#### Présage (niveau 2)
Lorsque vous terminez un repos long, lancez 2d20 et notez les résultats. Avant votre prochain repos long, vous pouvez remplacer n'importe quel jet d'attaque, de sauvegarde ou de caractéristique fait par vous ou une créature visible par l'un de ces résultats. Ce remplacement doit être déclaré avant le jet.

#### Divination experte (niveau 6)
Lancer des sorts de divination devient plus facile. Lorsque vous lancez un sort de divination de niveau 2 ou plus, vous récupérez un emplacement de sort de niveau inférieur au sort lancé.

#### Troisième oeil (niveau 10)
Par une action, vous gagnez l'un des bénéfices suivants jusqu'à ce que vous soyez neutralisé ou que vous preniez un repos court/long :
- **Vision dans le noir** : 18 mètres
- **Vision éthérée** : 18 mètres dans le Plan Éthéré
- **Compréhension des langues** : lisez toutes les langues
- **Détection de l'invisibilité** : voyez les créatures et objets invisibles à 3 mètres

#### Présage supérieur (niveau 14)
Vous lancez 3d20 au lieu de 2 pour votre capacité Présage.

---

### École d'Enchantement

Les enchanteurs manipulent les esprits et les émotions.

#### Érudit en enchantement (niveau 2)
Le temps et l'argent nécessaires pour copier un sort d'enchantement sont réduits de moitié.

#### Regard hypnotique (niveau 2)
Par une action, vous pouvez charmer une créature humanoïde à 1,5 mètre. Jusqu'à la fin de votre prochain tour, elle est charmée, a une vitesse de 0 et est neutralisée. L'effet se termine si vous vous éloignez à plus de 1,5 mètre ou si la créature subit des dégâts.

#### Charme instinctif (niveau 6)
Lorsqu'une créature vous attaque, vous pouvez utiliser votre réaction pour rediriger l'attaque vers une autre créature à portée (sauf l'attaquant). L'attaquant doit faire un jet de sauvegarde de Sagesse contre votre DD de sorts.

#### Partage d'enchantement (niveau 10)
Lorsque vous lancez un sort d'enchantement de niveau 1 ou plus qui cible une seule créature, vous pouvez cibler une deuxième créature à portée.

#### Altération mémorielle (niveau 14)
Lorsqu'un effet de charme que vous avez créé se termine, la créature n'a aucun souvenir d'avoir été charmée par vous.

---

### École d'Évocation

Les évocateurs maîtrisent les sorts de dégâts élémentaires.

#### Érudit en évocation (niveau 2)
Le temps et l'argent nécessaires pour copier un sort d'évocation sont réduits de moitié.

#### Façonneur de sorts (niveau 2)
Lorsque vous lancez un sort d'évocation qui affecte d'autres créatures visibles, vous pouvez choisir un nombre de créatures égal à 1 + le niveau du sort. Ces créatures réussissent automatiquement leur jet de sauvegarde et ne subissent aucun dégât.

#### Sort mineur puissant (niveau 6)
Vos sorts mineurs qui infligent des dégâts affectent même les créatures qui réussissent leur jet de sauvegarde. Elles subissent la moitié des dégâts du sort mineur.

#### Évocation améliorée (niveau 10)
Vous pouvez ajouter votre modificateur d'Intelligence aux dégâts d'un jet de dégâts de vos sorts d'évocation de magicien.

#### Surcharge magique (niveau 14)
Lorsque vous lancez un sort de magicien de niveau 1 à 5 qui inflige des dégâts, vous pouvez infliger les dégâts maximaux au lieu de lancer les dés. Une fois utilisé, vous subissez 2d12 dégâts nécrotiques par niveau de sort (ces dégâts ignorent les résistances et immunités). Cette capacité ne peut être réutilisée avant un repos long.

---

### École d'Illusion

Les illusionnistes tissent des tromperies magiques.

#### Érudit en illusion (niveau 2)
Le temps et l'argent nécessaires pour copier un sort d'illusion sont réduits de moitié.

#### Illusion mineure améliorée (niveau 2)
Vous apprenez le sort mineur *illusion mineure* s'il ne fait pas partie de vos sorts. Lorsque vous le lancez, vous pouvez créer à la fois un son et une image.

#### Illusions malléables (niveau 6)
Lorsque vous lancez un sort d'illusion avec une durée de 1 minute ou plus, vous pouvez utiliser votre action pour modifier la nature de l'illusion.

#### Double illusoire (niveau 10)
Par une réaction quand une créature vous attaque, vous pouvez interposer un double illusoire entre vous et l'attaquant. L'attaque rate automatiquement et votre double se dissipe.

#### Réalité illusoire (niveau 14)
Lorsque vous lancez un sort d'illusion de niveau 1 ou plus, vous pouvez choisir un objet inanimé non magique faisant partie de l'illusion et le rendre réel pendant 1 minute. L'objet ne peut pas infliger de dégâts ni blesser directement.

---

### École de Nécromancie

Les nécromanciens manipulent les forces de la vie et de la mort.

#### Érudit en nécromancie (niveau 2)
Le temps et l'argent nécessaires pour copier un sort de nécromancie sont réduits de moitié.

#### Sinistre moisson (niveau 2)
Une fois par tour, lorsque vous tuez une ou plusieurs créatures avec un sort de niveau 1 ou plus, vous regagnez des PV égaux à 2 x le niveau du sort (3 x le niveau pour les sorts de nécromancie). Ce bénéfice ne fonctionne pas sur les artificiels et les morts-vivants.

#### Serviteurs morts-vivants (niveau 6)
Lorsque vous lancez *animation des morts*, vous pouvez cibler un cadavre ou un tas d'os supplémentaire. De plus, les morts-vivants créés ont les bonus suivants :
- PV max augmentés de votre niveau de magicien
- Ajoutez votre bonus de maîtrise à leurs jets de dégâts

#### Insensibilité à la non-vie (niveau 10)
Vous gagnez la résistance aux dégâts nécrotiques et votre maximum de PV ne peut pas être réduit.

#### Contrôle des morts-vivants (niveau 14)
Par une action, vous pouvez cibler un mort-vivant que vous pouvez voir dans un rayon de 18 mètres. Il doit réussir un jet de sauvegarde de Charisme contre votre DD de sorts ou devenir charmé par vous pendant 24 heures. Vous pouvez lui donner des ordres télépathiquement.

---

### École de Transmutation

Les transmutateurs changent la forme et la substance de la matière.

#### Érudit en transmutation (niveau 2)
Le temps et l'argent nécessaires pour copier un sort de transmutation sont réduits de moitié.

#### Alchimie mineure (niveau 2)
Vous pouvez temporairement modifier les propriétés physiques d'un objet non magique. Pendant 1 heure (ou jusqu'à la perte de concentration), vous pouvez transformer le bois en pierre, le métal en bois, etc.

#### Pierre du transmutateur (niveau 6)
Vous pouvez créer une pierre magique conférant l'un des bénéfices suivants à son porteur :
- Vision dans le noir (18 mètres)
- +3 mètres de vitesse
- Maîtrise des jets de sauvegarde de Constitution
- Résistance à un type de dégâts élémentaires

Vous pouvez changer le bénéfice chaque fois que vous lancez un sort de transmutation de niveau 1 ou plus.

#### Métamorphe (niveau 10)
Vous pouvez lancer *métamorphose* sur vous-même sans dépenser de mana (maximum FP 1). Vous ne pouvez pas réutiliser cette capacité avant un repos court ou long.

#### Maître transmutateur (niveau 14)
Par une action, vous pouvez détruire votre Pierre du transmutateur pour produire l'un des effets suivants :
- **Jouvence** : rajeunir une créature de 3d10 ans
- **Panacée** : guérir toutes maladies, poisons et afflictions
- **Résurrection** : lancer *rappel à la vie* sans composantes
- **Transmutation majeure** : transformer un objet non magique de taille jusqu'à 1,5 mètre cube
