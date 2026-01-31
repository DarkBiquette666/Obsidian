---
aliases:
  - Érinye
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 12 (8400 PX)
---

# Érinye

```dnd-monstre
name: Érinye
type: Fiélon
taille: Moyen
alignement: loyal mauvais
ca: 18 (harnois)
pv: 153 (18d8 + 72)
vitesse: 9 m, vol 18 m
for: 18
dex: 16
con: 18
int: 14
sag: 14
cha: 18
sauvegardes: Dex +7, Con +8, Sag +6, Cha +8
sens: vision véritable 36 m, Perception passive 12
langues: infernal, télépathie 36 m
facteur_puissance: 12 (8400 PX)
immunites_etats: empoisonné
source: Monster Manual (SRD)
immunites:
  - feu
  - poison
résistances:
  - froid ; contondant
  - "perforant et tranchant d'attaques non magiques qui ne sont pas en argent"
traits:
  - name: Armes infernales
    description: "Les attaques avec une arme de l'érinye sont magiques et infligent 13 (3d8) dégâts de poison supplémentaires si elles touchent (inclus dans les attaques ci-dessous)."
  - name: Résistance à la magie
    description: "L'érinye a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques."
actions:
  - name: Attaques multiples
    description: "L'érinye effectue trois attaques."
  - name: Épée longue
    description: "Attaque au corps à corps avec une arme : +8 au toucher, allonge 1,50 m, une cible. Touché : 8 (1d8 + 4) dégâts tranchants, ou 9 (1d10 + 4) dégâts tranchants si utilisée à deux mains, plus 13 (3d8) dégâts de poison."
    attaque: +8 au toucher
  - name: Arc long
    description: "Attaque à distance avec une arme : +7 au toucher, portée 45/180 m, une cible. Touché : 7 (1d8 + 3) dégâts perforants + 13 (3d8) dégâts de poison, et la cible doit réussir un jet de sauvegarde de Constitution DD 14 ou être empoisonnée. Le poison reste jusqu'à ce qu'il soit supprimé à l'aide d'un sort de restauration partielle ou toute autre magie similaire."
    attaque: +7 au toucher
reactions:
  - name: Parade
    description: "L'érinye ajoute 4 à sa CA contre une attaque au corps à corps qui le toucherait. Pour ce faire, il doit voir l'attaquant et avoir en main une arme de corps à corps."
```
