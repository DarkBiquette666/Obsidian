---
aliases:
  - Cambion
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 5 (1800 PX)
---

# Cambion

```dnd-monstre
name: Cambion
type: Fiélon
taille: Moyen
alignement: tout alignement mauvais
ca: "19 (armure d'écailles)"
pv: 82 (11d8 + 33)
vitesse: 9 m, vol 18 m
for: 18
dex: 18
con: 16
int: 14
sag: 12
cha: 16
sauvegardes: For +7, Con +6, Int +5, Cha +6
sens: vision dans le noir 18 m, Perception passive 14
langues: abyssal, commun, infernal
facteur_puissance: 5 (1800 PX)
source: Monster Manual
compétences:
  - Discrétion +7
  - Intimidation +6
  - Perception +4
  - Tromperie +6
résistances:
  - foudre
  - feu
  - froid
  - poison ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Faveur impie
    description: La CA du cambion prend en compte son bonus de Charisme.
  - name: Incantation innée
    description: "La caractéristique d'incantation innée du cambion est le Charisme (jet de sauvegarde contre ses sorts DD 14). Le cambion peut lancer les sorts suivants de manière innée, sans avoir besoin de composantes matérielles :"
actions:
  - name: Attaques multiples
    description: Le cambion effectue deux attaques au corps à corps, ou utilise deux fois son Rayon de feu.
  - name: Lance
    description: "Attaque au corps à corps ou à distance avec une arme : +7 au toucher, allonge 1,50 m ou portée 6/12 m, une cible. Touché : 7 (1d6 + 4) dégâts perforants, ou 8 (1d8 + 4) dégâts perforants si utilisée à deux mains pour faire une attaque au corps à corps, plus 3 (1d6) dégâts de feu."
    attaque: +7 au toucher
  - name: Rayon de feu
    description: "Attaque à distance avec un sort : +7 au toucher, portée 36 m, une cible. Touché : 10 (3d6) dégâts de feu."
    attaque: +7 au toucher
  - name: Charme satanique
    description: "Un humanoïde situé à 9 mètres ou moins du cambion et qu'il peut voir doit réussir un jet de sauvegarde de Sagesse DD 14 ou être charmé par magie pendant 1 journée. La cible charmée obéit aux paroles du cambion. Si la cible subit des dégâts de la part du cambion ou d'une autre créature, ou reçoit un ordre suicidaire de la part du cambion, elle peut retenter le jet de sauvegarde, mettant fin à l'effet en cas de réussite. Si le jet de sauvegarde d'une créature est réussi ou que l'effet qu'elle subit se termine, celle-ci devient immunisée au Charme satanique du cambion pendant les prochaines 24 heures."
```
