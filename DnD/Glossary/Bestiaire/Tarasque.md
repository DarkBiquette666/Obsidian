---
aliases:
  - Tarasque
tags:
  - monstre
  - bestiaire
type: Monstruosité
facteur_puissance: 30 (155000 PX)
---

# Tarasque

```dnd-monstre
name: Tarasque
type: Monstruosité
taille: Grand
alignement: sans alignement
ca: 25 (armure naturelle)
pv: 676 (33d20 + 330)
vitesse: 12 m
for: 30
dex: 11
con: 30
int: 3
sag: 11
cha: 11
sauvegardes: Int +5, Sag +9, Cha +9
sens: vision aveugle 36 m, Perception passive 10
langues: —
facteur_puissance: 30 (155000 PX)
immunites_etats: charmé, effrayé, empoisonné, paralysé
source: Monster Manual (SRD)
immunites:
  - feu
  - poison ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Résistance légendaire (3/jour)
    description: Si la tarasque échoue à un jet de sauvegarde, elle peut décider de transformer cet échec en réussite.
  - name: Résistance à la magie
    description: La tarasque a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Carapace réfléchissante
    description: "Chaque fois que la tarasque est ciblée par un sort de projectile magique, un sort dont la zone d'effet est une ligne, ou un sort requérant un jet d'attaque à distance, lancez un d6. De 1 à 5, la tarasque n'est pas affectée. Sur un 6, la tarasque n'est pas affectée, et l'effet est renvoyé vers le lanceur de sorts comme s'il provenait de la tarasque, le lanceur devenant donc la cible."
  - name: Monstre de siège
    description: "La tarasque inflige le double des dégâts aux objets et structures qu'elle attaque."
actions:
  - name: Attaques multiples
    description: "La tarasque peut utiliser sa Présence terrifiante. Elle effectue ensuite cinq attaques : une de morsure, deux avec ses griffes, une avec ses cornes, et une avec sa queue. Elle peut utiliser Engloutissement à la place de sa morsure."
  - name: Cornes
    description: "Attaque au corps à corps avec une arme : +19 au toucher, allonge 3 m, une cible. Touché : 32 (4d10 + 10) dégâts perforants."
    attaque: +19 au toucher
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +19 au toucher, allonge 4,50 m, une cible. Touché : 28 (4d8 + 10) dégâts tranchants."
    attaque: +19 au toucher
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +19 au toucher, allonge 3 m, une cible. Touché : 36 (4d12 + 10) dégâts perforants. Si la cible est une créature, elle est agrippée (évasion DD 20). Tant qu'elle est agrippée, la créature est entravée, et la tarasque ne peut pas mordre une autre cible."
    attaque: +19 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +19 au toucher, allonge 6 m, une cible. Touché : 24 (4d6 + 10) dégâts contondants. Si la cible est une créature, elle doit réussir un jet de sauvegarde de Force DD 20 ou tomber à terre."
    attaque: +19 au toucher
  - name: Présence terrifiante
    description: "Chaque créature choisie par la tarasque, se trouvant à 36 mètres d'elle et consciente de sa présence, doit réussir un jet de sauvegarde de Sagesse DD 17 ou être effrayée pendant 1 minute. Une créature peut retenter le jet de sauvegarde à la fin de chacun de ses tours, avec un désavantage si la tarasque est dans la ligne de vue, mettant fin à l'effet qui l'affecte en cas de réussite. Si le jet de sauvegarde d'une créature est réussi ou que l'effet qu'elle subit prend fin, celle-ci devient immunisée à la Présence terrifiante de la tarasque pendant les prochaines 24 heures."
  - name: Engloutissement
    description: "La tarasque effectue une attaque de morsure contre une créature de taille G ou inférieure qu'elle agrippe. Si l'attaque réussit, la créature subit les dégâts de la morsure et est avalée, et elle n'est plus agrippée. Une fois avalée, la créature est aveuglée et entravée, bénéficie d'un abri total contre les attaques et effets provenant de l'extérieur de la tarasque, et subit 56 (16d6) dégâts d'acide au début de chaque tour de la tarasque. Si la tarasque subit 60 points de dégâts ou plus en un seul tour de la part d'une créature avalée, la tarasque doit réussir un jet de sauvegarde de Constitution DD 20 à la fin de ce tour ou régurgiter toutes les créatures qu'elle a avalées, qui se retrouveront alors à terre, à 3 mètres ou moins de la tarasque. Si la tarasque meurt, une créature avalée n'est plus entravée et peut s'échapper du cadavre en utilisant 9 mètres de mouvement pour se retrouver à l'extérieur et à terre."
legendaires:
  - name: Attaque
    description: La tarasque effectue une attaque avec ses griffes ou avec sa queue.
  - name: Déplacement
    description: La tarasque se déplace de la moitié de sa vitesse.
  - name: Mastication (coûte 2 actions)
    description: La tarasque effectue une attaque de morsure ou utilise Engloutissement.
```
