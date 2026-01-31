---
aliases:
  - Roc
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Roc (Dogue de Terre)

*Basé sur Chien de Guerre (Niveau 3)*

```dnd-monstre
name: Roc
type: Bête
taille: Moyen
alignement: Neutre
ca: 11
pv: Niveau Inquisiteur x 3
vitesse: 12 m
for: 13
dex: 12
con: 12
int: 3
sag: 12
cha: 7
sens: Perception passive 15
langues: Comprend celles de l'inquisiteur
facteur_puissance: Évolutif
compétences:
  - name: Perception
    description: ": +5"
  - name: Athlétisme
    description: ": +5"
traits:
  - name: Description
    description: "Une peau épaisse comme du cuir bouilli et une ossature massive. Il possède une plaque de métal greffée sur le crâne."
  - name: Personnalité
    description: "Têtu et incroyablement courageux, il ignore la douleur. Rien ne semble pouvoir le détourner de sa charge."
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Ténacité de la Pierre Brisée
    description: "Si 0 PV -> 1 PV (Max 3/RL). Ajoute 1 Fissure par usage : -2 CA cumulatif + Test Dressage (DD10+5/Fissure) sinon attaque random."
  - name: Rempart de Granit (Duo)
    description: "Tant que Roc et Ruine sont à 1,50m ou moins l'un de l'autre, ils bénéficient d'un bonus de +2 à la CA et ne peuvent pas être mis à terre."
actions:
  - name: Morsure Lourde
    description: "Attaque d'arme au corps à corps : +3 au toucher, allonge 1,50 m. Touché : 6 (1d6 + 1 + Bonus Maîtrise) dégâts perforants. JS Force DD 13 ou à terre."
    attaque: +3 au toucher
```
