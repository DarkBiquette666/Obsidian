---
aliases:
  - Gardien animé
tags:
  - monstre
  - bestiaire
type: Artificiel
facteur_puissance: 7 (2900 PX)
---

# Gardien animé

```dnd-monstre
name: Gardien animé
type: Artificiel
taille: Grand
alignement: sans alignement
ca: 17 (armure naturelle)
pv: 142 (15d10 + 60)
vitesse: 9 m
for: 18
dex: 8
con: 18
int: 7
sag: 10
cha: 3
sens: vision aveugle 3 m, vision dans le noir 18 m, Perception passive 10
langues: comprend les ordres donnés dans toutes les langues mais ne peut pas parler
facteur_puissance: 7 (2900 PX)
immunites_etats: charmé, épuisement, effrayé, paralysé, empoisonné
source: Monster Manual (SRD)
immunites:
  - poison
traits:
  - name: Lien
    description: "Le gardien animé est connecté magiquement à une amulette. Tant que le gardien et son amulette sont dans le même plan d'existence, le porteur de l'amulette peut appeler télépathiquement le gardien animé à le rejoindre, et le gardien sait automatiquement à quelle distance et dans quelle direction se trouve l'amulette. Si le gardien se trouve à 18 mètres ou moins du porteur de l'amulette, la moitié des dégâts que le porteur subit (arrondis au supérieur) est transférée au gardien."
  - name: Régénération
    description: "Le gardien animé récupère 10 points de vie au début de son tour s'il possède au moins 1 point de vie."
  - name: Réservoir de sort
    description: "Un lanceur de sorts qui porte l'amulette du gardien animé peut faire en sorte que le garde animé emmagasine un sort de niveau 4 ou inférieur. Pour ce faire, le porteur de l'amulette doit lancer le sort sur le gardien. Le sort n'a pas d'effet mais il est stocké dans le gardien. Lorsque le porteur de l'amulette le lui ordonne, ou lorsqu'une situation définie à l'avance par le lanceur de sorts survient, le gardien animé lance le sort emmagasiné avec tous les paramètres établis par le lanceur de sorts originel, et sans avoir besoin de composantes. Lorsque le sort est lancé ou lorsqu'un nouveau sort est emmagasiné, tout sort précédemment stocké est perdu."
actions:
  - name: Attaques multiples
    description: Le gardien animé effectue deux attaques avec ses poings.
  - name: Poing
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 11 (2d6 + 4) dégâts contondants."
    attaque: +7 au toucher
reactions:
  - name: Bouclier
    description: "Lorsqu'une créature effectue une attaque contre le porteur de l'amulette, le gardien animé confère au porteur de l'amulette un bonus de +2 à la CA s'ils se trouvent à 1,50 mètre ou moins l'un de l'autre."
```
