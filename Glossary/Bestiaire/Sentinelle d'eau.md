---
aliases:
  - Sentinelle d'eau
tags:
  - monstre
  - bestiaire
type: Créature
facteur_puissance: 3 (700 PX)
---

# Sentinelle d'eau

```dnd-monstre
name: "Sentinelle d'eau"
taille: Grand
alignement: neutre
ca: 13
pv: 58 (9d10 + 9)
vitesse: 0 m, nage 18 m
for: 17
dex: 16
con: 13
int: 11
sag: 10
cha: 10
sens: vision aveugle 9 m, Perception passive 10
langues: "comprend l'aquatique mais ne peut pas parler"
facteur_puissance: 3 (700 PX)
immunites_etats: épuisement, agrippé, paralysé, empoisonné, entravé, à terre, inconscient
source: Monster Manual (BR+)
immunites:
  - poison
résistances:
  - feu ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: "Invisible dans l'eau"
    description: "La sentinelle d'eau est invisible tant qu'elle est complètement immergée dans l'eau."
  - name: "Connexion à l'eau"
    description: "La sentinelle d'eau meurt si elle quitte l'eau à laquelle elle est unie ou si cette eau est détruite."
actions:
  - name: Constriction
    description: "Attaque au corps à corps avec une arme : +5 au toucher, allonge 3 m, une créature. Touché : 13 (3d6 + 3) dégâts contondants. Si la cible est de taille M ou inférieure, elle est agrippée (évasion DD 13) et attirée de 1,50 mètre vers la sentinelle d'eau. Tant qu'elle est agrippée, la cible est entravée, la sentinelle d'eau tente de la noyer et ne peut pas étreindre une autre cible."
    attaque: +5 au toucher
```
