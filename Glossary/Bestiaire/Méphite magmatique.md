---
aliases:
  - Méphite magmatique
  - Méphite
  - méphite
tags:
  - monstre
  - bestiaire
type: Créature
facteur_puissance: 1/2 (100 PX)
---

# Méphite magmatique

```dnd-monstre
name: Méphite magmatique
taille: Petit
alignement: neutre mauvais
ca: 11
pv: 22 (5d6 + 5)
vitesse: 9 m, vol 9 m
for: 8
dex: 12
con: 12
int: 7
sag: 10
cha: 10
sens: vision dans le noir 18 m, Perception passive 10
langues: igné, terreux
facteur_puissance: 1/2 (100 PX)
immunites_etats: empoisonné
source: Monster Manual (SRD)
compétences:
  - Discrétion +3
immunites:
  - feu
  - poison
vulnérabilités:
  - froid
traits:
  - name: Mort explosive
    description: "Lorsque le méphite meurt, il éclate dans une explosion de lave. Chaque créature présente dans un rayon de 1,50 mètre autour du méphite doit effectuer un jet de sauvegarde de Dextérité DD 11, subissant 7 (2d6) dégâts de feu en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: Apparence trompeuse
    description: "Tant que le méphite reste immobile, il ne peut être distingué d'un monticule de lave ordinaire."
  - name: Incantation innée (1/jour)
    description: "Le méphite peut lancer de manière innée le sort métal brûlant (jet de sauvegarde contre ses sorts DD 10), sans avoir besoin de composantes matérielles. Le Charisme est sa caractéristique d'incantation innée."
actions:
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +3 au toucher, allonge 1,50 m, une créature. Touché : 3 (1d4 + 1) dégâts tranchants + 2 (1d4) dégâts de feu."
    attaque: +3 au toucher
  - name: Souffle de feu (Recharge 6)
    description: "Le méphite crache un cône de 4,50 mètres de flammes. Chaque créature dans la zone doit effectuer un jet de sauvegarde de Dextérité DD 11, subissant 7 (2d6) dégâts de feu en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
```
