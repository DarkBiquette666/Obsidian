---
aliases:
  - Drake de Garde
  - Guard Drake
tags:
  - monstre
  - bestiaire
  - légion
type: Dragon
facteur_puissance: 2 (450 PX)
---

# Drake de Garde

Une créature reptilienne trapue et musclée, ressemblant à un dragon sans ailes. Créés par un rituel impliquant des écailles de dragon, ils sont utilisés comme chiens de garde ou montures de choc par la Légion de Fer.
Le rituel détermine la couleur et les résistances du drake. Celui-ci est une variante rouge (feu).

```dnd-monstre
name: Drake de Garde (Rouge)
type: Dragon
taille: Moyen
alignement: sans alignement
ca: 14 (armure naturelle)
pv: 52 (7d8 + 21)
vitesse: 9 m
for: 16 (+3)
dex: 11 (+0)
con: 16 (+3)
int: 4 (-3)
sag: 10 (+0)
cha: 7 (-2)
sens: vision dans le noir 18 m, Perception passive 12
langues: Comprend le Draconique mais ne parle pas
facteur_puissance: 2 (450 PX)
source: Volo's Guide to Monsters
compétences:
  - Perception +2
resistances:
  - Feu
traits:
  - name: Sensibilité Olfactive
    description: "Le drake a l'avantage aux tests de Sagesse (Perception) basés sur l'odorat."
actions:
  - name: Attaques multiples
    description: "Le drake effectue deux attaques : une avec sa morsure et une avec sa queue."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +5 au toucher, allonge 1,50 m, une cible. Touché : 7 (1d8 + 3) dégâts perforants + 3 (1d6) dégâts de Feu."
    attaque: +5 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +5 au toucher, allonge 1,50 m, une cible. Touché : 6 (1d6 + 3) dégâts contondants."
    attaque: +5 au toucher
```
