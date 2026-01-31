---
aliases:
  - Zombi tyrannoeil
tags:
  - monstre
  - bestiaire
type: Mort-vivant
facteur_puissance: 5 (1800 PX)
---

# Zombi tyrannoeil

```dnd-monstre
name: Zombi tyrannoeil
type: Mort-vivant
taille: Grand
alignement: neutre mauvais
ca: 15 (armure naturelle)
pv: 93 (11d10 + 33)
vitesse: 0 m, vol 6 m (stationnaire)
for: 10
dex: 8
con: 16
int: 3
sag: 8
cha: 5
sauvegardes: Sag +2
sens: vision dans le noir 18 m, Perception passive 9
langues: comprend le profond et le commun des profondeurs mais ne peut pas parler
facteur_puissance: 5 (1800 PX)
immunites_etats: à terre, empoisonné
source: Monster Manual
immunites:
  - poison
traits:
  - name: Tenacité de mort-vivant
    description: Si des dégâts font tomber le zombi à 0 points de vie, celui-ci doit effectuer un jet de sauvegarde de Constitution DD 5 + les dégâts subis, sauf en cas de dégâts radiants ou coup critique. En cas de réussite, il tombe à 1 point de vie à la place.
actions:
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +3 au toucher, allonge 1,50 m, une cible. Touché : 14 (4d6) dégâts perforants."
    attaque: +3 au toucher
  - name: Rayons oculaires
    description: "Le zombi tire aléatoirement un des rayons oculaires magiques suivants sur une cible qu'il peut voir dans un rayon de 18 mètres : 1- Rayon paralysant. La créature ciblée doit réussir un jet de sauvegarde de Constitution DD 14 ou être paralysée pendant 1 minute. La cible peut retenter ce jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite."
  - name: 2- Rayon de peur
    description: "La créature ciblée doit réussir un jet de sauvegarde de Sagesse DD 14 ou être effrayée pendant 1 minute. La cible peut retenter ce jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite."
  - name: 3- Rayon affaiblissant
    description: "La créature ciblée doit effectuer un jet de sauvegarde de Constitution DD 14, subissant 36 (8d8) dégâts nécrotiques en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: 4- Rayon de désintégration
    description: "Si la cible est une créature, elle doit réussir un jet de sauvegarde de Dextérité DD 14 ou subir 45 (10d8) dégâts de force. Si les dégâts font tomber les points de vie d'une créature à 0, son corps se transforme en un petit monticule de fine poussière grise. Si la cible est un objet non magique, ou la création d'une force magique, de taille G ou inférieure, il est désintégré sans jet de sauvegarde. Si la cible est un objet, ou la création d'une force magique, de taille TG ou supérieure, le rayon en désintègre un cube de 3 mètres d'arête."
```
