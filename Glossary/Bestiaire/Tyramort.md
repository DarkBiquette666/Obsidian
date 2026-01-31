---
aliases:
  - Tyramort
tags:
  - monstre
  - bestiaire
type: Mort-vivant
facteur_puissance: 14 (11500 PX)
---

# Tyramort

```dnd-monstre
name: Tyramort
type: Mort-vivant
taille: Grand
alignement: loyal mauvais
ca: 19 (armure naturelle)
pv: 187 (25d10 + 50)
vitesse: 0 m, vol 6 m (stationnaire)
for: 10
dex: 14
con: 14
int: 19
sag: 15
cha: 19
sauvegardes: For +5, Con +7, Int +9, Sag +7, Cha +9
sens: vision dans le noir 36 m, Perception passive 22
langues: profond, commun des profondeurs
facteur_puissance: 14 (11500 PX)
immunites_etats: charmé, épuisement, paralysé, pétrifié, empoisonné, à terre
source: Monster Manual
compétences:
  - Perception +12
immunites:
  - poison
traits:
  - name: "Cône d'énergie négative"
    description: "L'œil central du tyramort émet de l'énergie négative dans un invisible cône magique de 45 mètres. Au début de chacun de ses tours, le tyramort décide de quel côté il tourne ce cône et s'il active ce cône. Aucune créature dans la zone ne peut récupérer de points de vie. Tout humanoïde qui meurt dans la zone devient un zombi sous le contrôle du tyramort. Un humanoïde mort conserve son tour dans l'ordre d'initiative et s'anime au début de son tour suivant, à condition que son corps n'ait pas été complètement détruit."
actions:
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +5 au toucher, allonge 1,50 m, une cible. Touché : 14 (4d6) dégâts perforants."
    attaque: +5 au toucher
  - name: Rayons oculaires
    description: "Le tyramort tire aléatoirement trois des rayons oculaires magiques suivants (relancez les jets identiques) sur une à trois cibles qu'il peut voir dans un rayon de 36 mètres : 1- Rayon de charme. La créature ciblée doit réussir un jet de sauvegarde de Sagesse DD 17 ou être charmée par le tyramort pendant 1 heure, ou jusqu'à ce que le tyramort nuise à la créature."
  - name: 2- Rayon paralysant
    description: "La créature ciblée doit réussir un jet de sauvegarde de Constitution DD 17 ou être paralysée pendant 1 minute. La cible peut retenter ce jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite."
  - name: 3- Rayon de peur
    description: "La créature ciblée doit réussir un jet de sauvegarde de Sagesse DD 17 ou être effrayée pendant 1 minute. La cible peut retenter ce jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite."
  - name: 4- Rayon de lenteur
    description: "La créature ciblée doit réussir un jet de sauvegarde de Dextérité DD 17. En cas d'échec, la vitesse de déplacement de la cible est diminuée de moitié pendant 1 minute. De plus, la créature ne peut pas utiliser de réaction, ne peut utiliser qu'une action ou qu'une action bonus pendant son tour, mais pas les deux. La créature peut retenter ce jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite."
  - name: 5- Rayon affaiblissant
    description: "La créature ciblée doit effectuer un jet de sauvegarde de Constitution DD 17, subissant 36 (8d8) dégâts nécrotiques en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: 6- Rayon télékinésique
    description: "Si la cible est une créature, elle doit réussir un jet de sauvegarde de Force DD 17 ou être déplacée par le tyramort sur 9 mètres dans n'importe quelle direction. Elle est entravée par la prise du rayon télékinésique jusqu'au début du prochain tour du tyramort ou jusqu'à ce que le tyramort soit incapable d'agir. Si la cible est un objet, pesant 150 kg ou moins, qui n'est pas tenu ni porté, il est déplacé de 9 mètres dans n'importe quelle direction. Le tyramort peut également exercer un contrôle très fin sur les objets grâce à ce rayon, comme manipuler un simple outil ou ouvrir une porte ou un contenant."
  - name: 7- Rayon de sommeil
    description: "La créature ciblée doit réussir un jet de sauvegarde de Sagesse DD 17 ou être endormie et rester inconsciente pendant 1 minute. La cible se réveille si elle subit des dégâts ou si une autre créature utilise une action pour la réveiller. Ce rayon n'a pas d'effet sur les morts-vivants et les artificiels."
  - name: 8- Rayon de pétrification
    description: "La créature ciblée doit effectuer un jet de sauvegarde de Dextérité DD 17. En cas d'échec au jet, la créature commence à se transformer en pierre et est entravée. Elle doit retenter ce jet de sauvegarde à la fin de son prochain tour. En cas de réussite, l'effet prend fin. En cas d'échec, la créature est pétrifiée jusqu'à ce qu'elle soit libérée par un sort de restauration supérieure ou une autre magie."
  - name: 9- Rayon de désintégration
    description: "Si la cible est une créature, elle doit réussir un jet de sauvegarde de Dextérité DD 17 ou subir 45 (10d8) dégâts de force. Si les dégâts font tomber les points de vie d'une créature à 0, son corps se transforme en un petit monticule de fine poussière grise. Si la cible est un objet non magique, ou la création d'une force magique, de taille G ou inférieure, il est désintégré sans jet de sauvegarde. Si la cible est un objet, ou la création d'une force magique, de taille TG ou supérieure, le rayon en désintègre un cube de 3 mètres d'arête."
  - name: 10- Rayon de mort
    description: La créature ciblée doit réussir un jet de sauvegarde de Dextérité DD 17 ou subir 55 (10d10) dégâts nécrotiques. La créature meurt si le rayon la fait tomber à 0 points de vie.
legendaires:
  - name: Rayon oculaire
    description: Le tyramort utilise un rayon oculaire aléatoire.
```
