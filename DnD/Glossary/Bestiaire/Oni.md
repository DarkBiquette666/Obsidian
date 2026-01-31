---
aliases:
  - Oni
tags:
  - monstre
  - bestiaire
type: Géant
facteur_puissance: 7 (2900 PX)
---

# Oni

```dnd-monstre
name: Oni
type: Géant
taille: Grand
alignement: loyal mauvais
ca: 16 (cotte de mailles)
pv: 110 (13d10 + 39)
vitesse: 9 m, vol 9 m
for: 19
dex: 11
con: 16
int: 14
sag: 12
cha: 15
sauvegardes: Dex +3, Con +6, Sag +4, Cha +5
sens: vision dans le noir 18 m, Perception passive +4
langues: commun, géant
facteur_puissance: 7 (2900 PX)
source: Monster Manual (SRD)
compétences:
  - Arcanes +5
  - Perception +4
  - Tromperie +8
traits:
  - name: Incantation innée
    description: "La caractéristique d'incantation innée de l'oni est le Charisme (jet de sauvegarde contre ses sorts DD 13). L'oni peut lancer les sorts suivants de manière innée, sans avoir besoin de composantes matérielles :"
  - name: Armes magiques
    description: "Les attaques avec une arme de l'oni sont magiques."
  - name: Régénération
    description: "L'oni récupère 10 points de vie au début de son tour s'il possède au moins 1 point de vie."
actions:
  - name: Attaques multiples
    description: "L'oni effectue deux attaques, avec ses griffes ou avec sa coutille."
  - name: "Griffes (forme d'oni uniquement)"
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 8 (1d8 + 4) dégâts tranchants."
    attaque: +7 au toucher
  - name: Coutille
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 3 m, une cible. Touché : 15 (2d10 + 4) dégâts tranchants, ou 9 (1d10 + 4) dégâts tranchants sous forme de taille M ou P."
    attaque: +7 au toucher
  - name: Changement de forme
    description: "L'oni se métamorphose magiquement en un humanoïde de taille P ou M, en un géant de taille G, ou bien retrouve sa forme véritable. Mise à part sa taille, ses statistiques restent les mêmes quelle que soit sa forme. La seule partie de son équipement qui est également transformée est sa coutille, qui se rétrécit avec lui et peut donc lui servir sous forme humanoïde. Si l'oni meurt, il retrouve sa forme véritable, et sa coutille retrouve sa taille normale."
```
