---
aliases:
  - Golem d'argile
tags:
  - monstre
  - bestiaire
type: Artificiel
facteur_puissance: 9 (5000 PX)
---

# Golem d'argile

```dnd-monstre
name: "Golem d'argile"
type: Artificiel
taille: Grand
alignement: sans alignement
ca: 14 (armure naturelle)
pv: 133 (14d10 + 56)
vitesse: 6 m
for: 20
dex: 9
con: 18
int: 3
sag: 8
cha: 1
sens: vision dans le noir 18 m, Perception passive 9
langues: comprend les langues de son créateur mais ne peut pas parler
facteur_puissance: 9 (5000 PX)
immunites_etats: charmé, empoisonné, épuisement, paralysé, pétrifié, effrayé
source: Monster Manual (SRD)
immunites:
  - acide
  - poison
  - psychique ; contondant
  - "perforant et tranchant d'attaques non magiques qui ne sont pas en adamantium"
traits:
  - name: "Absorption de l'acide"
    description: "Lorsque le golem subit des dégâts d'acide, il ne subit aucun dommage et récupère un nombre de points de vie égal aux dégâts d'acide causés."
  - name: Fou furieux
    description: "Chaque fois que le golem débute son tour avec 60 points de vie ou moins, lancez un d6. Sur un résultat de 6, le golem devient fou furieux. À chacun de ses tours, s'il est dans cet état, le golem attaque la créature la plus proche qu'il peut voir. Si aucune créature n'est assez proche de lui pour qu'il puisse se déplacer et l'attaquer, il attaquera un objet, de préférence plus petit que lui. Une fois fou furieux, le golem demeure dans cet état jusqu'à ce qu'il soit détruit ou jusqu'à ce qu'il récupère tous ses points de vie."
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
    description: "Attaque au corps à corps avec une arme : +8 au toucher, allonge 1,50 m, une cible. Touché : 16 (2d10 + 5) dégâts contondants. Si la cible est une créature, celle-ci doit réussir un jet de sauvegarde de Constitution DD 15 pour ne pas subir une diminution de son maximum de points de vie égale aux dégâts subis. La cible meurt si cet effet réduit ses points de vie à 0. Cette diminution perdure jusqu'à ce que la cible bénéficie d'un sort de restauration supérieure ou d'une magie similaire."
    attaque: +8 au toucher
  - name: Hâte (Recharge 5-6)
    description: "Jusqu'à la fin de son prochain tour, le golem bénéficie par magie d'un bonus de +2 à sa CA, d'un avantage aux jets de sauvegarde de Dextérité, et peut utiliser une attaque de coup en action bonus."
```
