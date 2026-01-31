---
aliases:
  - Chevalier de la mort
tags:
  - monstre
  - bestiaire
type: Mort-vivant
facteur_puissance: 17 (18000 PX)
---

# Chevalier de la mort

```dnd-monstre
name: Chevalier de la mort
type: Mort-vivant
taille: Moyen
alignement: chaotique mauvais
ca: 20 (harnois, bouclier)
pv: 180 (19d8 + 95)
vitesse: 9 m
for: 20
dex: 11
con: 20
int: 12
sag: 16
cha: 18
sauvegardes: Dex +6, Sag +9, Cha +10
sens: vision dans le noir 36 m, Perception passive 13
langues: abyssal, commun
facteur_puissance: 17 (18000 PX)
immunites_etats: effrayé, épuisement, empoisonné
source: Monster Manual
immunites:
  - nécrotique
  - poison
traits:
  - name: Résistance à la magie
    description: Le chevalier de la mort a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Général des Morts
    description: "À moins que le chevalier de la mort soit incapable d'agir, les morts-vivants de son choix à 18 mètres ou moins de lui (lui y comprit) bénéficient d'un avantage à leurs jets de sauvegarde contre les capacités qui repoussent les morts-vivants."
  - name: Incantation
    description: "Le chevalier de la mort est un lanceur de sorts de niveau 19. Sa caractéristique d'incantation est le Charisme (jet de sauvegarde contre ses sorts DD 18, +10 au toucher pour les attaques avec un sort). Il a préparé les sorts de paladin suivants :"
actions:
  - name: Attaques multiples
    description: Le chevalier de la mort effectue trois attaques avec son épée longue.
  - name: Épée longue
    description: "Attaque au corps à corps avec une arme : +11 au toucher, allonge 1,50 m, une cible. Touché : 9 (1d8 + 5) dégâts tranchants, ou 10 (1d10 + 5) dégâts tranchants si utilisée à deux mains, plus 18 (4d8) dégâts nécrotiques."
    attaque: +11 au toucher
  - name: Orbe de feu infernal (1/jour)
    description: "Le chevalier de la mort projette une boule de feu magique qui explose en un point qu'il peut voir situé dans un rayon de 36 mètres autour de lui. Chaque créature dans un rayon de 6 mètres autour du point d'impact doit lancer un jet de sauvegarde de Dextérité DD 18. La sphère se propage au-delà des coins. Une créature subit 35 (10d6) dégâts de feu et 35 (10d6) dégâts nécrotiques si le jet de sauvegarde est raté, ou la moitié en cas de réussite."
reactions:
  - name: Parade
    description: "Le chevalier de la mort ajoute 6 à sa CA contre une attaque au corps à corps qui le toucherait. Pour ce faire, il doit voir l'attaquant et avoir en main une arme de corps à corps."
```
