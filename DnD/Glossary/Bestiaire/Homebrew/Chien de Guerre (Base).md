---
aliases:
  - Chien de Guerre (Base)
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Chien de Guerre (Base)

*Statistiques évolutives selon le niveau de l'Inquisiteur.*

```dnd-monstre
name: Chien de Guerre
type: Céleste, Fée ou Fiélon
taille: Moyen
alignement: Loyal Neutre
ca: 11 (10 + Dex)
pv: Niveau Inquisiteur x 3
vitesse: 12 m
for: 13
dex: 12
con: 12
int: 3
sag: 12
cha: 7
sens: Perception passive 15 (13 + Bonus Maîtrise)
langues: Comprend celles de l'inquisiteur mais ne parle pas.
facteur_puissance: Évolutif
compétences:
  - name: Perception
    description: ": +5 (3 + Bonus Maîtrise)"
  - name: Athlétisme
    description: ": +5 (3 + Bonus Maîtrise)"
traits:
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Entraîné au combat
    description: "Maîtrise armures légères."
actions:
  - name: Morsure
    description: "Attaque d'arme au corps à corps : +3 au toucher (1 + Bonus Maîtrise), allonge 1,50 m, une cible. Touché : 6 (1d6 + 1 + Bonus Maîtrise) dégâts perforants. Si la cible est une créature, elle doit réussir un JS Force DD 13 (11 + Bonus Maîtrise) ou tomber à terre."
    attaque: +3 au toucher
```