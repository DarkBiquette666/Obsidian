---
aliases:
  - Épouvantail
tags:
  - monstre
  - bestiaire
type: Artificiel
facteur_puissance: 1 (200 PX)
---

# Épouvantail

```dnd-monstre
name: Épouvantail
type: Artificiel
taille: Moyen
alignement: chaotique mauvais
ca: 11
pv: 36 (8d8)
vitesse: 9 m
for: 11
dex: 13
con: 11
int: 10
sag: 10
cha: 13
sens: vision dans le noir 18 m, Perception passive 10
langues: comprend les langues de son créateur mais ne peut pas parler
facteur_puissance: 1 (200 PX)
immunites_etats: charmé, épuisement, effrayé, paralysé, empoisonné, inconscient
source: Monster Manual
immunites:
  - poison
résistances:
  - contondant
  - "perforant et tranchant d'attaques non magiques"
vulnérabilités:
  - feu
traits:
  - name: Apparence trompeuse
    description: "Tant que l'épouvantail reste immobile, il ne peut pas être distingué d'un épouvantail ordinaire et inanimé."
actions:
  - name: Attaques multiples
    description: "L'épouvantail effectue deux attaques avec ses griffes."
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +3 au toucher, allonge 1,50 m, une cible. Touché : 6 (2d4 + 1) dégâts tranchants. Si la cible est une créature, elle doit réussir un jet de sauvegarde de Sagesse DD 11 ou être effrayée jusqu'à la fin du prochain tour de l'épouvantail."
    attaque: +3 au toucher
  - name: Regard terrifiant
    description: "L'épouvantail cible une créature qu'il peut voir et située à 9 mètres ou moins de lui. Si la cible peut voir l'épouvantail, elle doit réussir un jet de sauvegarde de Sagesse DD 11 ou être effrayée par magie jusqu'à la fin du prochain tour de l'épouvantail. La cible effrayée est également paralysée."
```
