---
aliases:
  - Tonnerre
  - Cheval Mutant
  - cheval mutant
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---
facteur_puissance: 1 (200 PX)
---

# Cheval de Trait Mutant ("Tonnerre")

> Autrefois un cheval de trait paisible, "Tonnerre" a brouté l'herbe contaminée près de la rivière. C'est maintenant une montagne de muscles pulsants, dont la peau se déchire sous la pression interne. Il est fou de douleur et frappe tout ce qui bouge.

```dnd-monstre
name: Cheval de Trait Mutant
type: Bête (Mutant)
taille: Grand
alignement: Non aligné
ca: 9 (Peau déchirée)
pv: 22 (3d10 + 6)
vitesse: 12 m
for: 18 (+4)
dex: 9 (-1)
con: 15 (+2)
int: 2 (-4)
sag: 12 (+1)
cha: 7 (-2)
sens: Perception passive 11
langues: —
facteur_puissance: 1 (200 PX)
traits:
  - name: Spasmes de Douleur
    description: "Le cheval est fou de douleur et ne vise pas ses attaques. Il subit un malus de -4 à ses jets d'attaque (déjà calculé dans l'action Sabots)."
  - name: Charge
    description: "Si le cheval se déplace d'au moins 6 m en ligne droite vers une cible avant de la toucher avec une attaque de sabots, la cible subit 3 (1d6) dégâts contondants supplémentaires. La cible doit réussir un JS Force DD 14 ou tomber à terre."
  - name: Instabilité Musculaire
    description: "La musculature du cheval est incontrôlable. Si son attaque de Sabots rate, le cheval heurte une surface dure (mur, sol, poutre) et subit 3 (1d6) dégâts contondants."
actions:
  - name: Sabots
    description: "Attaque au corps à corps avec une arme : +2 au toucher, allonge 1,50 m, une cible. Touché : 8 (1d8 + 4) dégâts contondants."
    attaque: +2 au toucher
```