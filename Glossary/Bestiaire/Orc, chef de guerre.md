---
aliases:
  - Orc, chef de guerre
tags:
  - monstre
  - bestiaire
type: Humanoïde
facteur_puissance: 4 (1100 PX)
---

# Orc, chef de guerre

```dnd-monstre
name: Orc, chef de guerre
type: Humanoïde
taille: Moyen
alignement: chaotique mauvais
ca: 16 (cotte de mailles)
pv: 93 (11d8 + 44)
vitesse: 9 m
for: 18
dex: 12
con: 18
int: 11
sag: 11
cha: 16
sauvegardes: For +6, Con +6, Sag +2
sens: vision dans le noir 18 m, Perception passive 10
langues: commun, orc
facteur_puissance: 4 (1100 PX)
source: Monster Manual
compétences:
  - Intimidation +5
traits:
  - name: Agressif
    description: "Par une action bonus, l'orc peut se déplacer de sa vitesse vers une créature hostile qu'il peut voir."
  - name: Furie de Gruumsh
    description: "L'orc inflige 4 (1d8) dégâts supplémentaires lorsqu'il touche une cible lors d'une attaque avec une arme (ce bonus est inclus ci-dessous)."
actions:
  - name: Attaques multiples
    description: "L'orc effectue deux attaques avec la hache à deux mains ou la lance."
  - name: Hache à deux mains
    description: "Attaque au corps à corps avec une arme : +6 au toucher, allonge 1,50 m, une cible. Touché : 15 (1d12 + 4 plus 1d8) dégâts tranchants."
    attaque: +6 au toucher
  - name: Lance
    description: "Attaque au corps à corps ou à distance avec une arme : +6 au toucher, allonge 1,50 m ou portée 6/18 m une cible. Touché : 12 (1d6 + 4 plus 1d8) dégâts perforants, ou 13 (2d8 + 4) dégâts perforants si utilisée à deux mains pour effectuer une attaque au corps à corps."
    attaque: +6 au toucher
  - name: Cri de guerre (1/jour)
    description: "Chaque créature que le chef de guerre choisie et qui se trouve à 9 mètres ou moins de lui, qui peut l'entendre, et qui n'est pas déjà affectée par un Cri de guerre, gagne un avantage aux jets d'attaque jusqu'au début du prochain tour du chef de guerre. Le chef de guerre peut ensuite effectuer une attaque en utilisant son action bonus."
```
