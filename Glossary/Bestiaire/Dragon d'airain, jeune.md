---
aliases:
  - Dragon d'airain, jeune
tags:
  - monstre
  - bestiaire
type: Dragon
facteur_puissance: 6 (2300 PX)
---

# Dragon d'airain, jeune

```dnd-monstre
name: "Dragon d'airain, jeune"
type: Dragon
taille: Grand
alignement: chaotique bon
ca: 17 (armure naturelle)
pv: 110 (13d10 + 39)
vitesse: 12 m, creusement 6 m, vol 24 m
for: 19
dex: 10
con: 17
int: 12
sag: 11
cha: 15
sauvegardes: Dex +3, Con +6, Sag +3, Cha +5
sens: vision aveugle 9 m, vision dans le noir 36 m, Perception passive 16
langues: commun, draconique
facteur_puissance: 6 (2300 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +3
  - Perception +6
  - Persuasion +5
immunites:
  - feu
actions:
  - name: Attaques multiples
    description: "Le dragon effectue trois attaques : une de morsure et deux avec ses griffes."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 3 m, une cible. Touché : 15 (2d10 + 4) dégâts perforants."
    attaque: +7 au toucher
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 11 (2d6 + 4) dégâts tranchants."
    attaque: +7 au toucher
  - name: Souffles (Recharge 5-6)
    description: "Le dragon utilise l'un des souffles de combat présentés ci-dessous."
  - name: Souffle de feu
    description: "Le dragon exhale des flammes sur une ligne de 12 mètres de long et de 1,50 mètre de large. Chaque créature présente dans la zone doit effectuer un jet de sauvegarde de Dextérité DD 14, subissant 42 (12d6) dégâts de feu en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: Souffle de sommeil
    description: "Le dragon exhale un gaz soporifique dans un cône de 9 mètres. Chaque créature dans cette zone doit réussir un jet de sauvegarde de Constitution DD 14 ou tomber inconsciente pendant 5 minutes. Cet effet prend fin pour une créature si elle subit des dégâts ou si quelqu'un utilise son action pour la réveiller."
```
