---
aliases:
  - Golem de pierre
tags:
  - monstre
  - bestiaire
type: Artificiel
facteur_puissance: 10 (5900 PX)
---

# Golem de pierre

```dnd-monstre
name: Golem de pierre
type: Artificiel
taille: Grand
alignement: sans alignement
ca: 17 (armure naturelle)
pv: 178 (17d10 + 85)
vitesse: 9 m
for: 22
dex: 9
con: 20
int: 3
sag: 11
cha: 1
sens: vision dans le noir 36 m, Perception passive 10
langues: comprend les langues de son créateur mais ne peut pas parler
facteur_puissance: 10 (5900 PX)
immunites_etats: charmé, épuisement, effrayé, paralysé, pétrifié, empoisonné
source: Monster Manual (SRD)
immunites:
  - poison
  - psychique ; contondant
  - "perforant et tranchant d'attaques non magiques qui ne sont pas en adamantium"
traits:
  - name: Forme immuable
    description: Le golem est immunisé aux sorts et effets qui altèreraient son apparence.
  - name: Résistance à la magie
    description: Le golem a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Armes magiques
    description: Les attaques avec une arme du golem sont magiques.
actions:
  - name: Attaques multiples
    description: Le golem effectue deux attaques de coup.
  - name: Coup
    description: "Attaque au corps à corps avec une arme : +10 au toucher, allonge 1,50 m, une cible. Touché : 19 (3d8 + 6) dégâts contondants."
    attaque: +10 au toucher
  - name: Lenteur (Recharge 5-6)
    description: "Le golem cible une ou plusieurs créatures qu'il peut voir dans un rayon de 3 mètres autour de lui. Chaque cible doit faire un jet de sauvegarde de Sagesse DD 17 contre cette magie. En cas d'échec, une cible ne peut pas utiliser de réaction, sa vitesse est réduite de moitié, et elle ne peut pas faire plus d'une attaque à son tour. En outre, la cible peut à son tour prendre une action normale ou une action bonus, mais pas les deux. Ces effets durent pendant 1 minute. Une cible peut répéter le jet de sauvegarde à la fin de chacun de ses tours, l'effet se terminant en cas de réussite."
```
