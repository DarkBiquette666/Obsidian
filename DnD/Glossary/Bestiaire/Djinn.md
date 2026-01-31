---
aliases:
  - Djinn
tags:
  - monstre
  - bestiaire
type: Créature
facteur_puissance: 11 (7200 PX)
---

# Djinn

```dnd-monstre
name: Djinn
taille: Grand
alignement: chaotique bon
ca: 17 (armure naturelle)
pv: 161 (14d10 + 84)
vitesse: 9 m, vol 27 m
for: 21
dex: 15
con: 22
int: 15
sag: 16
cha: 20
sauvegardes: Dex +6, Sag +7, Cha +9
sens: vision dans le noir 36 m, Perception passive 13
langues: aérien
facteur_puissance: 11 (7200 PX)
source: Monster Manual (SRD)
immunites:
  - foudre
  - tonnerre
traits:
  - name: Disparition élémentaire
    description: "Si le djinn meurt, son corps se désintègre en une chaude brise, ne laissant derrière lui que l'équipement que le djinn portait ou transportait."
  - name: Incantation innée
    description: "La caractéristique d'incantation innée du djinn est le Charisme (jet de sauvegarde contre ses sorts DD 17, +9 au toucher pour les attaques avec un sort). Il peut lancer les sorts suivants de manière innée, sans avoir besoin de composantes matérielles :"
actions:
  - name: Attaques multiples
    description: Le djinn effectue trois attaques avec le cimeterre.
  - name: Cimeterre
    description: "Attaque au corps à corps avec une arme : +9 au toucher, allonge 1,50 m, une cible. Touché : 12 (2d6 + 5) dégâts tranchants + 3 (1d6) dégâts de foudre ou de tonnerre (au choix du djinn)."
    attaque: +9 au toucher
  - name: Création de tourbillon
    description: "Le djinn crée magiquement un tourbillon de vent de 1,50 mètre de rayon et de 9 mètres de haut, en un point situé dans un rayon de 36 mètres autour du djinn et qu'il peut voir. Le tourbillon reste tant que le djinn maintient sa concentration (comme s'il se concentrait sur un sort). Toute créature, à l'exception du djinn, qui pénètre dans le tourbillon doit réussir un jet de sauvegarde de Force DD 18 ou être entravée par les vents. Le djinn peut déplacer le tourbillon jusqu'à 18 mètres en utilisant une action, et les créatures entravées par le tourbillon se déplacent avec lui. Le tourbillon se termine si le djinn le perd de vue. Une créature peut utiliser son action pour libérer une créature entravée par le tourbillon (elle peut se libérer elle-même), en réussissant un jet de Force DD 18. En cas de réussite, la créature n'est plus entravée et se déplace à l'endroit le plus proche à l'extérieur du tourbillon."
```
