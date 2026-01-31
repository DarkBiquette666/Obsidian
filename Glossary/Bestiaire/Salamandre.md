---
aliases:
  - Salamandre
tags:
  - monstre
  - bestiaire
type: Créature
facteur_puissance: 5 (1800 PX)
---

# Salamandre

```dnd-monstre
name: Salamandre
taille: Grand
alignement: neutre mauvais
ca: 15 (armure naturelle)
pv: 90 (12d10 + 24)
vitesse: 9 m
for: 18
dex: 14
con: 15
int: 11
sag: 10
cha: 12
sens: vision dans le noir 18 m, Perception passive 10
langues: igné
facteur_puissance: 5 (1800 PX)
source: Monster Manual (SRD)
immunites:
  - feu
résistances:
  - contondant
  - "perforant et tranchant d'attaques non magiques"
vulnérabilités:
  - froid
traits:
  - name: Corps brûlant
    description: "Une créature qui touche la salamandre ou la frappe lors d'une attaque au corps à corps en étant à 1,50 mètre ou moins de la salamandre subit 7 (2d6) dégâts de feu."
  - name: Armes brûlantes
    description: "Toute arme de corps à corps en métal que brandit la salamandre inflige 3 (1d6) dégâts de feu supplémentaires (inclus dans l'attaque ci-dessous)."
actions:
  - name: Attaques multiples
    description: "La salamandre effectue deux attaques : une avec la lance et une avec sa queue."
  - name: Lance
    description: "Attaque au corps à corps ou à distance avec une arme : +7 au toucher, allonge 1,50 m ou portée 6/18 m, une cible. Touché : 11 (2d6 + 4) dégâts perforants, ou 13 (2d8 + 4) dégâts perforants si utilisée à deux mains pour faire une attaque au corps à corps, plus 3 (1d6) dégâts de feu."
    attaque: +7 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 3 m, une cible. Touché : 11 (2d6 + 4) dégâts contondants + 7 (2d6) dégâts de feu, et la cible est agrippée (évasion DD 14). Tant qu'elle est agrippée, la cible est entravée, la salamandre peut automatiquement toucher la cible avec sa queue, et la salamandre ne peut plus effectuer d'attaque avec sa queue contre d'autres cibles."
    attaque: +7 au toucher
```
