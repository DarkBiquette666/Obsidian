---
aliases:
  - Enclume
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Enclume (Chien de Guerre)

*Basé sur Chien de Guerre (Niveau 3)*

```dnd-monstre
name: Enclume
type: Bête
taille: Moyen
alignement: Loyal Neutre
ca: 12 (+1 Bonus Duo)
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
    description: "Une femelle gris fer, légèrement plus petite que Marteau mais plus large d'épaules. Elle porte un collier protecteur assorti."
  - name: Personnalité
    description: "Protectrice et attentive, elle surveille toujours les alentours. Elle est le bouclier du duo, encaissant les coups pour permettre à Marteau de frapper."
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Duo de Choc (Enclume)
    description: "Enclume possède une robustesse exceptionnelle (+1 CA)."
  - name: Charge Renversante (Duo)
    description: "Si Marteau et Enclume chargent en même temps (6m min) vers une cible et touchent, JS Force DD 13 ou à terre."
actions:
  - name: Morsure
    description: "Attaque d'arme au corps à corps : +3 au toucher, allonge 1,50 m. Touché : 6 (1d6 + 1 + Bonus Maîtrise) dégâts perforants. JS Force DD 13 ou à terre."
    attaque: +3 au toucher
```