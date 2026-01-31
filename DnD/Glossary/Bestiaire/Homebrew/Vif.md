---
aliases:
  - Vif
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Vif (Lévrier du Nord)

*Basé sur Chien de Guerre (Niveau 3)*

```dnd-monstre
name: Vif
type: Bête
taille: Moyen
alignement: Neutre
ca: 11
pv: Niveau Inquisiteur x 3
vitesse: 15 m (Bonus Race)
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
  - name: Acrobatie
    description: ": +5 (Bonus Race)"
traits:
  - name: Description
    description: "Un lévrier haut sur pattes au poil dur hirsute, couleur gris orage. Il a une oreille déchiquetée et une cicatrice sur le museau."
  - name: Personnalité
    description: "Nerveux et toujours aux aguets, il ne tient pas en place. Très indépendant, il préfère agir vite et rester mobile."
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Tactique de Meute
    description: "Avantage aux jets d'attaque contre une créature si un allié est à 1,50m d'elle."
actions:
  - name: Morsure Rapide
    description: "Attaque d'arme au corps à corps : +3 au toucher, allonge 1,50 m. Touché : 6 (1d6 + 1 + Bonus Maîtrise) dégâts perforants. JS Force DD 13 ou à terre."
    attaque: +3 au toucher
```