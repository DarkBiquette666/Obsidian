---
aliases:
  - Matriarche Tisse-Ombre
tags:
  - monstre
  - bestiaire
type: monstruosité
facteur_puissance: 2 (450 PX)
---

# Matriarche Tisse-Ombre

```dnd-monstre
name: Matriarche Tisse-Ombre
type: Monstruosité
taille: Grande
alignement: neutre mauvais
ca: 14 (armure naturelle)
pv: 45 (6d10 + 12)
vitesse: 9 m, escalade 9 m
for: 16
dex: 16
con: 14
int: 6
sag: 12
cha: 6
sens: vision aveugle 6 m, vision dans le noir 18 m, Perception passive 11
langues: —
facteur_puissance: 2 (450 PX)
source: Custom
compétences:
  - Discrétion +5
traits:
  - name: Déplacement sur la toile
    description: "L'araignée ignore les restrictions de mouvement causées par une toile d'araignée."
  - name: "Pattes d'araignée"
    description: "L'araignée peut escalader des surfaces difficiles et être au plafond la tête en bas sans avoir besoin d'effectuer un jet de caractéristique."
actions:
  - name: Multiattaque
    description: "L'araignée effectue deux attaques : une avec sa morsure et une avec ses griffes."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +5 au toucher, allonge 1,50 m, une créature. Touché : 7 (1d8 + 3) dégâts perforants, et la cible doit faire un JS Constitution DD 12, subissant 7 (2d6) dégâts de poison en cas d'échec, ou la moitié en cas de réussite."
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +5 au toucher, allonge 1,50 m, une créature. Touché : 6 (1d6 + 3) dégâts tranchants."
  - name: "Jet de Toile (Recharge 5-6)"
    description: "Attaque à distance avec une arme : +5 au toucher, portée 9/18 m, une créature. Touché : La cible est entravée. Par une action, elle peut faire un jet de Force DD 12 pour se libérer. La toile a CA 10, 10 PV, vulnérable au feu."
  - name: "Appel de la Ruche (1/Jour)"
    description: "La matriarche émet un sifflement. 1d2 [[Araignée de la Ruche]] (CR 1/4) émergent pour la protéger."
reactions:
  - name: "Repli Tissé"
    description: "Lorsque l'araignée subit des dégâts, elle peut utiliser sa réaction pour se déplacer jusqu'à la moitié de sa vitesse sans provoquer d'attaques d'opportunité, si elle finit sur une toile."
```