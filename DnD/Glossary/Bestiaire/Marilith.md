---
aliases:
  - Marilith
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 16 (15000 PX)
---

# Marilith

```dnd-monstre
name: Marilith
type: Fiélon
taille: Grand
alignement: chaotique mauvais
ca: 18 (armure naturelle)
pv: 189 (18d10 + 90)
vitesse: 12 m
for: 18
dex: 20
con: 20
int: 18
sag: 16
cha: 20
sauvegardes: For +9, Con +10, Sag +8, Cha +10
sens: vision véritable 36 m, Perception passive 13
langues: abyssal, télépathie 36 m
facteur_puissance: 16 (15000 PX)
immunites_etats: empoisonné
source: Monster Manual (SRD)
immunites:
  - poison
résistances:
  - froid
  - feu
  - foudre ; contondant
  - perforant et tranchant non magiques
traits:
  - name: Résistance à la magie
    description: La marilith a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Armes magiques
    description: Les attaques avec une arme de la marilith sont magiques.
  - name: Réactif
    description: La marilith peut utiliser une réaction par tour de combat.
actions:
  - name: Attaques multiples
    description: "La marilith effectue sept attaques : six avec ses épées longues et une avec sa queue."
  - name: Épée longue
    description: "Attaque au corps à corps avec une arme : +9 au toucher, allonge 1,50 m, une cible. Touché : 13 (2d8 + 4) dégâts tranchants."
    attaque: +9 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +9 au toucher, allonge 3 m, une créature. Touché : 15 (2d10 + 4) dégâts contondants. Si la cible est de taille M ou inférieure, elle est agrippée (DD 19 pour s'échapper). Tant qu'elle est agrippée, la cible est entravée, et la marilith peut toucher automatiquement sa cible avec sa queue, mais ne peut pas attaquer d'autres cibles."
    attaque: +9 au toucher
  - name: Téléportation
    description: "La marilith se téléporte magiquement, avec tout équipement qu'elle porte ou transporte, vers un espace inoccupé qu'elle peut voir et situé dans un rayon de 36 mètres autour d'elle."
reactions:
  - name: Parade
    description: "La marilith ajoute 5 à sa CA contre une attaque au corps à corps qui la toucherait. Pour ce faire, elle doit voir l'attaquant et avoir en main une arme de corps à corps."
```
