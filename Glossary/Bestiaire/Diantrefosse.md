---
aliases:
  - Diantrefosse
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 20 (25000 PX)
---

# Diantrefosse

```dnd-monstre
name: Diantrefosse
type: Fiélon
taille: Grand
alignement: loyal mauvais
ca: 19 (armure naturelle)
pv: 300 (24d10 + 168)
vitesse: 9 m, vol 18 m
for: 26
dex: 14
con: 24
int: 22
sag: 18
cha: 24
sauvegardes: Dex +8, Con +13, Sag +10
sens: vision véritable 36 m, Perception passive 14
langues: infernal, télépathie 36 m
facteur_puissance: 20 (25000 PX)
immunites_etats: empoisonné
source: Monster Manual (SRD)
immunites:
  - feu
  - poison
résistances:
  - froid ; contondant
  - "perforant et tranchant d'attaques non magiques qui ne sont pas en argent"
traits:
  - name: Aura de peur
    description: "Toute créature hostile au diantrefosse qui commence son tour à 6 mètres ou moins de lui doit effectuer un jet de sauvegarde de Sagesse DD 21, à moins que le diantrefosse ne soit incapable d'agir. En cas d'échec, la créature est effrayée jusqu'au début de son prochain tour. Si le jet de sauvegarde d'une créature est une réussite, la créature est immunisée contre l'Aura de peur du diantrefosse pour les prochaines 24 heures."
  - name: Résistance à la magie
    description: Le diantrefosse a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Armes magiques
    description: Les attaques avec une arme du diantrefosse sont magiques.
  - name: Incantation innée
    description: "La caractéristique d'incantation innée du diantrefosse est le Charisme (jet de sauvegarde contre ses sorts DD 21). Le diantrefosse peut lancer les sorts suivants de manière innée, sans avoir besoin de composantes matérielles :"
actions:
  - name: Attaques multiples
    description: "Le diantrefosse effectue quatre attaques : une de morsure, une avec ses griffes, une avec sa masse d'armes et une avec sa queue."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 1,50 m, une cible. Touché : 22 (4d6 + 8) dégâts perforants. La cible doit effectuer un jet de sauvegarde de Constitution DD 21 ou être empoisonnée. Tant qu'elle est empoisonnée de la sorte, la cible ne peut pas récupérer de points de vie, et elle subit 21 (6d6) dégâts de poison au début de chacun de ses tours suivants. La cible empoisonnée peut retenter ce jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite."
    attaque: +14 au toucher
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 3 m, une cible. Touché : 17 (2d8 + 8) dégâts tranchants."
    attaque: +14 au toucher
  - name: "Masse d'armes"
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 3 m, une cible. Touché : 15 (2d6 + 8) dégâts contondants + 21 (6d6) dégâts de feu."
    attaque: +14 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 3 m, une cible. Touché : 24 (3d10 + 8) dégâts contondants."
    attaque: +14 au toucher
```
