---
aliases:
  - Slaad vert
tags:
  - monstre
  - bestiaire
type: Aberration
facteur_puissance: 8 (3900 PX)
---

# Slaad vert

```dnd-monstre
name: Slaad vert
type: Aberration
taille: Grand
alignement: chaotique neutre
ca: 16 (armure naturelle)
pv: 127 (15d10 + 45)
vitesse: 9 m
for: 18
dex: 15
con: 16
int: 11
sag: 8
cha: 12
sens: vision aveugle 9 m, vision dans le noir 18 m, Perception passive 12
langues: slaad, télépathie 18 m
facteur_puissance: 8 (3900 PX)
source: Monster Manual
compétences:
  - Arcanes + 3
  - Perception +2
résistances:
  - acide
  - froid
  - feu
  - foudre
  - tonnerre
traits:
  - name: Métamorphe
    description: "Le slaad peut utiliser son action pour se métamorphoser en un humanoïde de taille P ou M, ou pour reprendre sa forme véritable. Mise à part sa taille, ses statistiques sont les mêmes quelle que soit sa forme. L'équipement qu'il porte ou transporte ne se transforme pas. Il retrouve sa forme véritable s'il meurt."
  - name: Incantation innée
    description: "La caractéristique d'incantation innée du slaad est le Charisme (jet de sauvegarde contre ses sorts DD 12). Le slaad peut lancer les sorts suivants de manière innée, sans avoir besoin de composantes matérielles :"
  - name: Résistance à la magie
    description: Le slaad a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Régénération
    description: "Le slaad récupère 10 points de vie au début de son tour s'il possède au moins 1 point de vie."
actions:
  - name: Attaques multiples
    description: "Le slaad effectue trois attaques : une de morsure et deux avec ses griffes ou avec le bâton. Il peut sinon utiliser son Jet de flammes deux fois."
  - name: Morsure (forme de slaad uniquement)
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 11 (2d6 + 4) dégâts perforants."
    attaque: +7 au toucher
  - name: Griffes (forme de slaad uniquement)
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 7 (1d6 + 4) dégâts tranchants."
    attaque: +7 au toucher
  - name: Bâton
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 11 (2d6 + 4) dégâts contondants."
    attaque: +7 au toucher
  - name: Jet de flammes
    description: "Attaque à distance avec un sort : +4 au toucher, portée 18 m, une cible. Touché : 10 (3d6) dégâts de feu. Si la cible est un objet inflammable qui n'est ni porté ni transporté, il prend feu."
    attaque: +4 au toucher
```
