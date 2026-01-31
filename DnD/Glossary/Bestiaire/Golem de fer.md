---
aliases:
  - Golem de fer
tags:
  - monstre
  - bestiaire
type: Artificiel
facteur_puissance: 16 (15000 PX)
---

# Golem de fer

```dnd-monstre
name: Golem de fer
type: Artificiel
taille: Grand
alignement: sans alignement
ca: 20 (armure naturelle)
pv: 210 (20d10 + 100)
vitesse: 9 m
for: 24
dex: 9
con: 20
int: 3
sag: 11
cha: 1
sens: vision dans le noir 36 m, Perception passive 10
langues: comprend les langues de son créateur mais ne peut pas parler
facteur_puissance: 16 (15000 PX)
immunites_etats: charmé, épuisement, effrayé, paralysé, pétrifié, empoisonné
source: Monster Manual (SRD)
immunites:
  - feu
  - poison
  - psychique ; contondant
  - "perforant et tranchant d'attaques non magiques qui ne sont pas en adamantium"
traits:
  - name: Absorption du feu
    description: Chaque fois que le golem est soumis à des dégâts de feu, il ne subit aucun dégât et récupère un nombre de points de vie égal aux dégâts de feu infligés.
  - name: Forme immuable
    description: Le golem est immunisé aux sorts et effets qui altèreraient son apparence.
  - name: Résistance à la magie
    description: Le golem a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Armes magiques
    description: Les attaques avec une arme du golem sont magiques.
actions:
  - name: Attaques multiples
    description: Le golem effectue deux attaques au corps à corps.
  - name: Coup
    description: "Attaque au corps à corps avec une arme : +13 au toucher, allonge 1,50 m, une cible. Touché : 20 (3d8 + 7) dégâts contondants."
    attaque: +13 au toucher
  - name: Épée
    description: "Attaque au corps à corps avec une arme : +13 au toucher, allonge 3 m, une cible. Touché : 23 (3d10 + 7) dégâts tranchants."
    attaque: +13 au toucher
  - name: Souffle empoisonné (Recharge 6)
    description: "Le golem crache un gaz empoisonné dans un cône de 4,50 mètres. Chaque créature dans cette zone doit effectuer un jet de sauvegarde de Constitution DD 19, subissant 45 (10d8) dégâts de poison en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
```
