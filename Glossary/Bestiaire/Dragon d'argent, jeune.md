---
aliases:
  - Dragon d'argent, jeune
tags:
  - monstre
  - bestiaire
type: Dragon
facteur_puissance: 9 (5000 PX)
---

# Dragon d'argent, jeune

```dnd-monstre
name: "Dragon d'argent, jeune"
type: Dragon
taille: Grand
alignement: loyal bon
ca: 18 (armure naturelle)
pv: 168 (16d10 + 80)
vitesse: 12 m, vol 24 m
for: 23
dex: 10
con: 21
int: 14
sag: 11
cha: 19
sauvegardes: Dex +4, Con +9, Sag +4, Cha +8
sens: vision aveugle 9 m, vision dans le noir 36 m, Perception passive 18
langues: commun, draconique
facteur_puissance: 9 (5000 PX)
source: Monster Manual (SRD)
compétences:
  - Arcanes +6
  - Discrétion +4
  - Histoire +6
  - Perception +8
immunites:
  - froid
actions:
  - name: Attaques multiples
    description: "Le dragon effectue trois attaques : une de morsure et deux avec ses griffes."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +10 au toucher, allonge 3 m, une cible. Touché : 17 (2d10 + 6) dégâts perforants."
    attaque: +10 au toucher
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +10 au toucher, allonge 1,50 m, une cible. Touché : 13 (2d6 + 6) dégâts tranchants."
    attaque: +10 au toucher
  - name: Souffles (Recharge 5-6)
    description: "Le dragon utilise l'un des souffles de combat présentés ci-dessous."
  - name: Souffle de froid
    description: "Le dragon crache une tempête de glace dans un cône de 9 mètres. Chaque créature présente dans la zone doit effectuer un jet de sauvegarde de Constitution DD 17, subissant 54 (12d8) dégâts de froid en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: Souffle paralysant
    description: "Le dragon exhale un gaz paralysant dans un cône de 9 mètres. Chaque créature présente dans la zone doit réussir un jet de sauvegarde de Constitution DD 17 ou être paralysée pendant 1 minute. Une créature peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite à ce nouveau jet de sauvegarde."
```
