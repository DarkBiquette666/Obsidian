---
aliases:
  - Revenant
tags:
  - monstre
  - bestiaire
type: Mort-vivant
facteur_puissance: 5 (1800 PX)
---

# Revenant

```dnd-monstre
name: Revenant
type: Mort-vivant
taille: Moyen
alignement: neutre
ca: 13 (armure de cuir)
pv: 136 (16d8 + 64)
vitesse: 9 m
for: 18
dex: 14
con: 18
int: 13
sag: 16
cha: 18
sauvegardes: For +7, Con +7, Sag +6, Cha +7
sens: vision dans le noir 18 m, Perception passive 13
langues: "les langues qu'il connaissait de son vivant"
facteur_puissance: 5 (1800 PX)
immunites_etats: charmé, épuisement, effrayé, paralysé, empoisonné, étourdi
source: Monster Manual (BR+)
immunites:
  - poison
résistances:
  - nécrotique
  - psychique
traits:
  - name: Régénération
    description: "Le revenant récupère 10 points de vie au début de son tour. Si le revenant subit des dégâts de feu ou des dégâts radiants, ce trait ne fonctionne pas au début de son prochain tour. Le corps du revenant n'est détruit que s'il débute son tour avec 0 points de vie et qu'il ne se régénère pas."
  - name: Reconstitution
    description: "Lorsque le corps du revenant est détruit, son âme subsiste. Au bout de 24 heures, l'âme habite et anime un autre corps humanoïde sur le même plan d'existence et récupère tous ses points de vie. Tant que l'âme n'est pas dans son nouveau corps, un sort de souhait peut être utilisé pour la forcer à passer dans l'au-delà et ne pas en revenir."
  - name: Immunité au renvoi
    description: Le revenant est immunisé aux effets de renvoi des morts-vivants.
  - name: Traqueur rancunier
    description: "Le revenant connaît la direction et la distance qui le sépare de toutes les créatures contre lesquelles il est venu réclamer vengeance, même si la créature et le revenant sont sur des plans d'existence différents. Si la créature traquée par le revenant meurt, le revenant l'apprend."
actions:
  - name: Attaques multiples
    description: Le revenant effectue deux attaques avec ses poings.
  - name: Poing
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 11 (2d6 + 4) dégâts contondants. Si la cible est une créature contre laquelle le revenant a juré vengeance, la cible subit 14 (4d6) dégâts contondants supplémentaires. Plutôt que d'infliger des dégâts, le revenant peut agripper la cible (évasion DD 14) à condition que la cible soit de taille G ou inférieure."
    attaque: +7 au toucher
  - name: Éblouissement vengeur
    description: "Le revenant cible une créature qu'il peut voir et se trouvant à 9 mètres ou moins de lui et contre laquelle il a juré vengeance. La cible doit effectuer un jet de sauvegarde de Sagesse DD 15. En cas d'échec, la cible est paralysée jusqu'à ce que le revenant lui inflige des dégâts, ou jusqu'à la fin du prochain tour du revenant. Lorsque la paralysie se termine, la cible est effrayée par le revenant pendant 1 minute. La cible effrayée peut retenter son jet de sauvegarde à la fin de chacun de ses tours, avec un désavantage si elle peut voir le revenant, mettant fin à cet état en cas de réussite."
```
