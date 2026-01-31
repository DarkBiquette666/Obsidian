---
aliases:
  - Élémentaire de l'eau
tags:
  - monstre
  - bestiaire
type: Créature
facteur_puissance: 5 (1800 PX)
---

# Élémentaire de l'eau

```dnd-monstre
name: "Élémentaire de l'eau"
taille: Grand
alignement: neutre
ca: 14 (armure naturelle)
pv: 114 (12d10 + 48)
vitesse: 9 m, nage 27 m
for: 18
dex: 14
con: 18
int: 5
sag: 10
cha: 8
sens: vision dans le noir 18 m, Perception passive 10
langues: aquatique
facteur_puissance: 5 (1800 PX)
immunites_etats: épuisement, agrippé, paralysé, pétrifié, empoisonné, à terre, entravé, inconscient
source: Monster Manual (SRD)
immunites:
  - poison
résistances:
  - acide ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: "Forme d'eau"
    description: "L'élémentaire peut entrer dans l'espace d'une créature hostile et y rester. Il peut se déplacer à travers un espace aussi étroit que 2,50 cm de large sans être compressé."
  - name: Congelé
    description: "Si l'élémentaire subit des dégâts de froid, il gèle partiellement ; sa vitesse est réduite de 6 mètres jusqu'à la fin de son prochain tour."
actions:
  - name: Attaques multiples
    description: "L'élémentaire effectue deux attaques de coup."
  - name: Coup
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 13 (2d8 + 4) dégâts contondants."
    attaque: +7 au toucher
  - name: Submersion (Recharge 4-6)
    description: "Chaque créature dans l'espace de l'élémentaire doit faire un jet de sauvegarde de Force DD 15. En cas d'échec, une cible subit 13 (2d8 + 4) dégâts contondants. Si elle est de taille G ou plus petite, elle est également agrippée (évasion DD 14). Tant qu'elle est agrippée, la cible est entravée et incapable de respirer à moins qu'elle puisse respirer sous l'eau. Si le jet de sauvegarde est réussi, la cible est poussée hors de l'espace de l'élémentaire. L'élémentaire peut agripper une créature de taille G ou jusqu'à deux créatures de taille M ou plus petites à la fois. Au début de chaque tour de l'élémentaire, chaque cible agrippée par l'élémentaire prend 13 (2d8 + 4) dégâts contondants. Une créature dans un rayon de 1,50 mètre autour de l'élémentaire peut lui retirer une créature ou un objet en prenant une action pour faire un jet de Force DD 14 et en le réussissant."
```
