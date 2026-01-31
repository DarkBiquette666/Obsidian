---
aliases:
  - Pollux
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Pollux (Berger de Heaum)

*Basé sur Chien de Guerre (Niveau 3)*

```dnd-monstre
name: Pollux
type: Bête
taille: Moyen
alignement: Loyal Bon
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
  - name: Intimidation
    description: ": +5 (Bonus Race)"
traits:
  - name: Description
    description: "Physiquement identique à Castor (noir et feu), ce qui trouble souvent les ennemis. Ses oreilles sont droites et toujours attentives."
  - name: Personnalité
    description: "Aussi sérieux et protecteur que son frère. Il est particulièrement vigilant lors des phases de garde et de surveillance."
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Fureur Fraternelle
    description: "Si son jumeau tombe à 0 PV ou crit, Rage (1 min) : Résistance dégâts physiques +2 dégâts."
actions:
  - name: Morsure
    description: "Attaque d'arme au corps à corps : +3 au toucher, allonge 1,50 m. Touché : 6 (1d6 + 1 + Bonus Maîtrise) dégâts perforants (+2 si Rage). JS Force DD 13 ou à terre."
    attaque: +3 au toucher
réactions:
  - name: Garde du Corps
    description: ": Si créature adjacente attaque une cible autre que lui, impose Désavantage."
```
