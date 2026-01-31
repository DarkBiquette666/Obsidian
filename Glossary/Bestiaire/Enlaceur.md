---
aliases:
  - Enlaceur
tags:
  - monstre
  - bestiaire
type: Monstruosité
facteur_puissance: 5 (1800 PX)
---

# Enlaceur

```dnd-monstre
name: Enlaceur
type: Monstruosité
taille: Grand
alignement: neutre mauvais
ca: 20 (armure naturelle)
pv: 93 (11d10 + 33)
vitesse: 3 m, escalade 3 m
for: 18
dex: 8
con: 17
int: 7
sag: 16
cha: 6
sens: vision dans le noir 18 m, Perception passive 16
langues: —
facteur_puissance: 5 (1800 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +5
  - Perception +6
traits:
  - name: Apparence trompeuse
    description: "Tant que l'enlaceur reste immobile, il ne peut être distingué d'une formation naturelle de caverne, comme une stalagmite."
  - name: Filaments agrippants
    description: "L'enlaceur peut avoir jusqu'à 6 filaments à la fois. Chaque filament peut être attaqué (CA 20 ; 10 points de vie ; immunité au poison et aux dégâts psychiques). Détruire un filament n'inflige aucun dégât à l'enlaceur, qui peut faire sortir un filament de remplacement à son prochain tour. Un filament peut également être rompu si une créature utilise son action pour effectuer un jet de Force DD 15 contre elle."
  - name: "Pattes d'araignée"
    description: "L'enlaceur peut escalader des surfaces difficiles et être au plafond la tête en bas sans avoir besoin d'effectuer un jet de caractéristique."
actions:
  - name: Attaques multiples
    description: "L'enlaceur effectue quatre attaques avec ses filaments, utilise Embobiner, et effectue une attaque de morsure."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 22 (4d8 + 4) dégâts perforants."
    attaque: +7 au toucher
  - name: Filament
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 15 m, une créature. Touché : La cible est agrippée (évasion DD 15). Tant qu'elle est agrippée, la cible est entravée et a un désavantage aux jets de Force et aux jets de sauvegarde de Force, et l'enlaceur ne peut plus utiliser le même filament sur une autre cible."
    attaque: +7 au toucher
  - name: Embobiner
    description: "L'enlaceur tire à lui sur 7,50 mètres chaque créature qu'il a agrippée."
```
