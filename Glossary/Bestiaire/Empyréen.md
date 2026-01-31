---
aliases:
  - Empyréen
tags:
  - monstre
  - bestiaire
type: Céleste
facteur_puissance: 23 (50000 PX)
---

# Empyréen

```dnd-monstre
name: Empyréen
type: Céleste
taille: Tres grand
alignement: chaotique bon (75 %) ou neutre mauvais (25 %)
ca: 22 (armure naturelle)
pv: 313 (19d12 + 190)
vitesse: 15 m, nage 15 m, vol 15 m
for: 30
dex: 21
con: 30
int: 21
sag: 22
cha: 27
sauvegardes: For +17, Int +12, Sag +13, Cha +15
sens: vision véritable 36 m, Perception passive 16
langues: toutes
facteur_puissance: 23 (50000 PX)
source: Monster Manual
compétences:
  - Intuition +13
  - Persuasion +15
immunites:
  - contondant
  - perforant
  - "ou tranchant d'attaques non magiques"
traits:
  - name: Incantation innée
    description: "La caractéristique d'incantation innée de l'empyréen est le Charisme (jet de sauvegarde contre ses sorts DD 23, +15 au toucher pour les attaques avec un sort). Il peut lancer les sorts suivants de manière innée, sans avoir besoin des composantes matérielles :"
  - name: Résistance légendaire (3/jour)
    description: "Si l'empyréen échoue à un jet de sauvegarde, il peut décider de transformer cet échec en réussite."
  - name: Résistance à la magie
    description: "L'empyréen a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques."
  - name: Armes magiques
    description: "Les attaques avec une arme de l'empyréen sont magiques."
actions:
  - name: Maillet
    description: "Attaque au corps à corps avec une arme : +17 au toucher, allonge 3 m, une cible. Touché : 31 (6d6 +10) dégâts contondants. Si la cible est une créature, elle doit réussir un jet de sauvegarde de Constitution DD 15 ou être étourdie jusqu'à la fin du prochain tour de l'empyréen."
    attaque: +17 au toucher
  - name: Foudre
    description: "Attaque à distance avec un sort : +15 au toucher, portée 180 m, une cible. Touché : 24 (7d6) dégâts de l'un des types suivants (au choix de l'empyréen): acide, froid, feu, force, foudre, radiant, ou tonnerre."
    attaque: +15 au toucher
legendaires:
  - name: Attaque
    description: "L'empyréen effectue une attaque."
  - name: Soutien
    description: "L'empyréen soutient toutes les créatures non-hostiles dans un rayon de 36 mètres autour de lui jusqu'à la fin de son prochain tour. Les créatures soutenues ne peuvent pas être charmées ou effrayées, de plus elles gagnent un avantage à leurs jets de caractéristique et de sauvegarde, jusqu'à la fin du prochain tour de l'empyréen."
  - name: Secousse (coûte 2 actions)
    description: "L'empyréen frappe le sol avec son maillet, déclenchant un tremblement de terre. Toutes les autres créatures sur le sol dans un rayon de 18 mètres autour de l'empyréen doivent réussir un jet de sauvegarde de Force DD 25 ou être jetées à terre."
```
