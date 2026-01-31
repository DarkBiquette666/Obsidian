---
aliases:
  - Marteau
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Marteau (Chien de Guerre)

*Basé sur Chien de Guerre (Niveau 3)*

```dnd-monstre
name: Marteau
type: Bête
taille: Moyen
alignement: Loyal Neutre
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
    description: "Un mâle massif au pelage brun bringé. Il a une tête énorme et une mâchoire carrée. Il porte un lourd collier de cuir clouté."
  - name: Personnalité
    description: "Placide et calme hors du combat, il aime se coucher sur les pieds de son maître. En combat, il devient une force implacable qui ne lâche jamais sa prise."
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Duo de Choc (Marteau)
    description: "Marteau possède une force d'attaque supérieure (+1 aux jets d'attaque et de dégâts, inclus)."
  - name: Charge Renversante (Duo)
    description: "Si Marteau et Enclume chargent en même temps (6m min) vers une cible et touchent, JS Force DD 13 ou à terre."
actions:
  - name: Morsure Broyeuse
    description: "Attaque d'arme au corps à corps : +4 au toucher, allonge 1,50 m. Touché : 7 (1d6 + 2 + Bonus Maîtrise) dégâts perforants. JS Force DD 13 ou à terre."
    attaque: +4 au toucher
```