---
aliases:
  - Ettercap
tags:
  - monstre
  - bestiaire
type: Monstruosité
facteur_puissance: 2 (450 PX)
---

# Ettercap

```dnd-monstre
name: Ettercap
type: Monstruosité
taille: Moyen
alignement: neutre mauvais
ca: 13 (armure naturelle)
pv: 44 (8d8 + 8)
vitesse: 9 m, escalade 9 m
for: 14
dex: 15
con: 13
int: 7
sag: 12
cha: 8
sens: vision dans le noir 18 m, Perception passive 13
langues: —
facteur_puissance: 2 (450 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +4
  - Perception +3
  - Survie +3
traits:
  - name: "Pattes d'araignée"
    description: "L'ettercap peut escalader des surfaces difficiles et être au plafond la tête en bas sans avoir besoin d'effectuer un jet de caractéristique."
  - name: Sens de la toile
    description: "Lorsqu'il est en contact avec une toile, l'ettercap connait l'emplacement exact de toutes les créatures qui sont en contact avec cette toile."
  - name: Déplacement sur la toile
    description: "L'ettercap ignore les restrictions de mouvement causées par une toile d'araignée."
actions:
  - name: Attaques multiples
    description: "L'ettercap effectue deux attaques : une de morsure et une avec ses griffes."
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +4 au toucher, allonge 1,50 m, une cible. Touché : 7 (2d4 + 2) dégâts tranchants."
    attaque: +4 au toucher
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +4 au toucher, allonge 1,50 m, une créature. Touché : 6 (1d8 + 2) dégâts perforants + 4 (1d8) dégâts de poison. La cible doit réussir un jet de sauvegarde de Constitution DD 11 ou être empoisonnée pendant 1 minute. La créature peut recommencer ce jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite."
    attaque: +4 au toucher
  - name: "Toile d'araignée (Recharge 5-6)"
    description: "Attaque à distance avec une arme : +4 au toucher, portée 9/18 m, une créature de taille G ou inférieure. Touché : la créature est entravée par la toile. Par une action, la créature entravée peut effectuer un jet de Force DD 11, s'échappant de la toile en cas de réussite. L'effet se termine si la toile est détruite. La toile a une CA de 10, 5 points de vie, est vulnérable aux dégâts de feu et immunisée contre les dégâts contondants, de poison et psychiques."
    attaque: +4 au toucher
```
