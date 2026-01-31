---
aliases:
  - Golem de chair
tags:
  - monstre
  - bestiaire
type: Artificiel
facteur_puissance: 5 (1800 PX)
---

# Golem de chair

```dnd-monstre
name: Golem de chair
type: Artificiel
taille: Moyen
alignement: neutre
ca: 9
pv: 93 (11d8 + 44)
vitesse: 9 m
for: 19
dex: 9
con: 18
int: 6
sag: 10
cha: 5
sens: vision dans le noir 18 m, Perception passive 10
langues: comprend les langues de son créateur mais ne peut pas parler
facteur_puissance: 5 (1800 PX)
immunites_etats: charmé, empoisonné, épuisement, paralysé, pétrifié, effrayé
source: Monster Manual (SRD)
immunites:
  - foudre
  - poison ; contondant
  - "perforant et tranchant d'attaques non magiques qui ne sont pas en adamantium"
traits:
  - name: Fou furieux
    description: "Chaque fois que le golem débute son tour avec 40 points de vie ou moins, lancez un d6. Sur un résultat de 6, le golem devient fou furieux. À chacun de ses tours, s'il est dans cet état, le golem attaque la créature la plus proche qu'il peut voir. Si aucune créature n'est assez proche de lui pour qu'il puisse se déplacer et l'attaquer, il attaquera un objet, de préférence plus petit que lui. Une fois fou furieux, le golem demeure dans cet état jusqu'à ce qu'il soit détruit ou jusqu'à ce qu'il récupère tous ses points de vie. Le créateur du golem, s'il se trouve à 18 mètres ou moins de lui, peut tenter de le calmer en lui parlant fermement et de manière persuasive. Le golem doit pouvoir entendre son créateur, qui doit utiliser une action pour effectuer un jet de Charisme (Persuasion) DD 15. Si le jet est réussi, le golem se calme. S'il subit des dégâts alors que ses points de vie sont à 40 ou moins, le golem peut de nouveau devenir fou furieux."
  - name: Absorption de la foudre
    description: Lorsque le golem subit des dégâts de foudre, il ne subit aucun dommage et récupère un nombre de points de vie égal aux dégâts de foudre causés.
  - name: Aversion au feu
    description: "Si le golem subit des dégâts de feu, il subit un désavantage aux jets d'attaque et de caractéristiques jusqu'à la fin de son tour."
  - name: Forme immuable
    description: Le golem est immunisé aux sorts et effets qui altèreraient son apparence.
  - name: Armes magiques
    description: Les attaques avec une arme du golem sont magiques.
  - name: Résistance à la magie
    description: Le golem a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
actions:
  - name: Attaques multiples
    description: Le golem effectue deux attaques de coup.
  - name: Coup
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 13 (2d8 + 4) dégâts contondants."
    attaque: +7 au toucher
```
