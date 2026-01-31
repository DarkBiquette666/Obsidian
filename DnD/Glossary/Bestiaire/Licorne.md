---
aliases:
  - Licorne
tags:
  - monstre
  - bestiaire
type: Céleste
facteur_puissance: 5 (1800 PX)
---

# Licorne

```dnd-monstre
name: Licorne
type: Céleste
taille: Grand
alignement: loyal bon
ca: 12
pv: 67 (9d10 + 18)
vitesse: 15 m
for: 18
dex: 14
con: 15
int: 11
sag: 17
cha: 16
sens: vision dans le noir 18 m, Perception passive 13
langues: céleste, elfique, sylvestre, télépathie 18 m
facteur_puissance: 5 (1800 PX)
immunites_etats: charmé, paralysé, empoisonné
source: Monster Manual (SRD)
immunites:
  - poison
traits:
  - name: Charge
    description: "Si la licorne se déplace d'au moins 6 mètres en ligne droite vers une cible, puis la touche lors d'une attaque avec sa corne dans le même tour, la cible subit 9 (2d8) dégâts supplémentaires de type perforant. Si la cible est une créature, elle doit réussir un jet de sauvegarde de Force DD 15 ou tomber à terre."
  - name: Incantation innée
    description: "La caractéristique d'incantation innée de la licorne est le Charisme (jet de sauvegarde contre ses sorts DD 14). La licorne peut lancer les sorts suivants de manière innée, sans avoir besoin d'aucune composante :"
  - name: Résistance à la magie
    description: La licorne a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
  - name: Armes magiques
    description: Les attaques avec une arme de la licorne sont magiques.
actions:
  - name: Attaques multiples
    description: "La licorne effectue deux attaques : une avec ses sabots et une avec sa corne."
  - name: Sabots
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 11 (2d6 + 4) dégâts contondants."
    attaque: +7 au toucher
  - name: Corne
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 8 (1d8 + 4) dégâts perforants."
    attaque: +7 au toucher
  - name: Contact guérisseur (3/jour)
    description: La licorne touche une autre créature avec sa corne. La cible récupère magiquement 11 (2d8 + 2) points de vie. De plus, le toucher soigne toutes les maladies et neutralise tous les poisons affectant la cible.
  - name: Téléportation (1/jour)
    description: "La licorne se téléporte magiquement ainsi que jusqu'à trois créatures consentantes qu'elle peut voir à 1,50 mètre d'elle, y compris tous les équipements qu'ils revêtent ou transportent, dans un lieu dont la licorne est familière, à une distance maximale de 1,5 kilomètre."
legendaires:
  - name: Sabots
    description: La licorne effectue une attaque avec ses sabots.
  - name: Boucliers scintillant (coûte 2 actions)
    description: "La licorne crée un champ magique scintillant autour d'elle ou d'une autre créature qu'elle peut voir à 18 m d'elle. La cible gagne un bonus de +2 à sa CA jusqu'à la fin du prochain tour de la licorne."
  - name: Soin personnel (coûte 3 actions)
    description: La licorne récupère magiquement 11 (2d8 + 2) points de vie.
```
