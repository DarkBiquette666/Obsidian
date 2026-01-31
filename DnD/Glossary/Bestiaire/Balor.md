---
aliases:
  - Balor
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 19 (22000 PX)
---

# Balor

```dnd-monstre
name: Balor
type: Fiélon
taille: Tres grand
alignement: chaotique mauvais
ca: 19 (armure naturelle)
pv: 262 (21d12 + 126)
vitesse: 12 m, vol 24 m
for: 26
dex: 15
con: 22
int: 20
sag: 16
cha: 22
sauvegardes: For +14, Con +12, Sag +9, Cha +12
sens: vision véritable 36 m, Perception passive 13
langues: abyssal, télépathie 36 m
facteur_puissance: 19 (22000 PX)
immunites_etats: empoisonné
source: Monster Manual (SRD)
immunites:
  - feu
  - poison
résistances:
  - foudre
  - froid ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: "Spasmes d'agonie"
    description: "Le balor explose lorsqu'il meurt, et toutes les créatures situées à 9 mètres ou moins de lui doivent effectuer un jet de sauvegarde de Dextérité DD 20, subissant 70 (20d6) dégâts de feu en cas d'échec, ou la moitié de ces dégâts en cas de réussite. L'explosion embrase les objets inflammables qui ne sont pas tenus ou portés se trouvant dans la zone, et détruit les armes du balor."
  - name: Aura de feu
    description: "Au début de chaque tour du balor, toute créature située à 1,50 mètre ou moins de lui subit 10 (3d6) dégâts de feu, et les objets inflammables situés dans l'aura, qui ne sont pas tenus ou portés, s'embrasent. Une créature qui touche le balor ou le frappe avec une attaque au corps à corps tout en se trouvant à 1,50 mètre ou moins de lui subit 10 (3d6) dégâts de feu."
  - name: Résistance à la magie
    description: Le balor a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Armes magiques
    description: Les attaques avec une arme du balor sont magiques.
actions:
  - name: Attaques multiples
    description: "Le balor effectue deux attaques : une avec son épée longue et une avec son fouet."
  - name: Épée longue
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 3 m, une cible. Touché : 21 (3d8 + 8) dégâts tranchants + 13 (3d8) dégâts de foudre. Si le balor réalise un coup critique, il lance trois fois les dés de dégâts au lieu de deux fois."
    attaque: +14 au toucher
  - name: Fouet
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 9 m, une cible. Touché : 15 (2d6 + 8) dégâts tranchants + 10 (3d6) dégâts de feu, et la cible doit réussir un jet de sauvegarde de Force DD 20 ou être tirée de 7,50 mètres vers le balor."
    attaque: +14 au toucher
  - name: Téléportation
    description: "Le balor se téléporte magiquement, avec tout équipement qu'il porte ou transporte, vers un espace inoccupé qu'il peut voir et situé dans un rayon de 36 mètres autour de lui."
```
