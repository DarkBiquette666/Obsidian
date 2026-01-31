---
aliases:
  - Dragon d'ombre rouge, jeune
tags:
  - monstre
  - bestiaire
type: Dragon
facteur_puissance: 13 (10000 PX)
---

# Dragon d'ombre rouge, jeune

```dnd-monstre
name: "Dragon d'ombre rouge, jeune"
type: Dragon
taille: Grand
alignement: chaotique mauvais
ca: 18 (armure naturelle)
pv: 178 (17d10 + 85)
vitesse: 12 m, escalade 12 m, vol 24 m
for: 23
dex: 10
con: 21
int: 14
sag: 11
cha: 19
sauvegardes: Dex +4, Con +9, Sag +4, Cha +8
sens: vision aveugle 9 m, vision dans le noir 36 m, Perception passive 18
langues: commun, draconique
facteur_puissance: 13 (10000 PX)
source: Monster Manual
compétences:
  - Discrétion +8
  - Perception +8
immunites:
  - feu
résistances:
  - nécrotique
traits:
  - name: Ombre vivante
    description: "Tant qu'il se trouve dans une zone de lumière faible ou de ténèbres, le dragon a une résistance à tous les dégâts, exception faite des dégâts de force, psychiques, ou radiants."
  - name: Discrétion dans les ombres
    description: "Tant qu'il se trouve dans une zone de lumière faible ou de ténèbres, le dragon peut utiliser l'action Se cacher en dépensant une action bonus."
  - name: Sensibilité au soleil
    description: "S'il est exposé à la lumière du soleil, le dragon a un désavantage aux jets d'attaque et aux jets de Sagesse (Perception) basés sur la vue."
actions:
  - name: Attaques multiples
    description: "Le dragon effectue trois attaques : une de morsure et deux avec ses griffes."
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +10 au toucher, allonge 1,50 m, une cible. Touché : 13 (2d6 + 6) dégâts tranchants."
    attaque: +10 au toucher
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +10 au toucher, allonge 3 m, une cible. Touché : 17 (2d10 + 6) dégâts perforants + 3 (1d6) dégâts nécrotiques."
    attaque: +10 au toucher
  - name: "Souffle d'ombres (Recharge 5-6)"
    description: "Le dragon exhale des flammes d'ombre dans un cône de 9 mètres. Toutes les créatures dans la zone doivent effectuer un jet de sauvegarde de Dextérité DD 18, subissant 56 (16d6) dégâts nécrotiques en cas d'échec, ou la moitié de ces dégâts en cas de réussite. Un humanoïde dont les points de vie tombent à 0 suite à ces dégâts meurt sur le champ, et une ombre morte-vivante surgit de son corps et agit immédiatement après le dragon dans l'ordre d'initiative. L'ombre est sous le contrôle du dragon."
```
