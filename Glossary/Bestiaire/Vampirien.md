---
aliases:
  - Vampirien
tags:
  - monstre
  - bestiaire
type: Mort-vivant
facteur_puissance: 5 (1800 PX)
---

# Vampirien

```dnd-monstre
name: Vampirien
type: Mort-vivant
taille: Moyen
alignement: neutre mauvais
ca: 15 (armure naturelle)
pv: 82 (11d8 + 33)
vitesse: 9 m
for: 16
dex: 16
con: 16
int: 11
sag: 10
cha: 12
sauvegardes: Dex +6, Sag +3
sens: vision dans le noir 18 m, Perception passive 13
langues: "les langues qu'il connaissait de son vivant"
facteur_puissance: 5 (1800 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +6
  - Perception +3
résistances:
  - nécrotique ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Régénération
    description: "Le vampirien récupère 10 points de vie au début de son tour s'il possède au moins 1 point de vie et qu'il n'est pas exposé à la lumière du soleil ou dans une étendue d'eau courante. Si le vampirien subit des dégâts radiants ou des dégâts via de l'eau bénite, ce trait ne fonctionne pas au début de son prochain tour."
  - name: "Pattes d'araignée"
    description: "Le vampirien peut escalader des surfaces difficiles et être au plafond la tête en bas sans avoir besoin d'effectuer un jet de caractéristique."
  - name: Faiblesses de vampire
    description: "Le vampirien a les faiblesses suivantes : Interdiction. Le vampirien ne peut pas entrer dans une résidence sans y avoir été invité par l'un de ses occupants."
  - name: "Détruit par les étendues d'eau courante"
    description: "Le vampirien subit 20 dégâts d'acide lorsqu'il termine son tour au sein d'une étendue d'eau courante."
  - name: Un pieu dans le cœur
    description: "Le vampirien est détruit si une arme perforante faite de bois est enfoncée dans son cœur alors qu'il est incapable d'agir dans sa tombe."
  - name: Hypersensibilité au soleil
    description: "Le vampirien subit 20 dégâts radiants lorsqu'il débute son tour à la lumière du soleil. S'il est exposé à la lumière du soleil, il a un désavantage aux jets d'attaque et de caractéristique."
actions:
  - name: Attaques multiples
    description: "Le vampirien effectue deux attaques, mais seule l'une des deux peut être une attaque de morsure."
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +6 au toucher, allonge 1,50 m, une créature. Touché : 8 (2d4 + 3) dégâts tranchants. Plutôt que d'infliger des dégâts, le vampirien peut agripper la cible (évasion DD 13)"
    attaque: +6 au toucher
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +6 au toucher, allonge 1,50 m, une créature consentante ou une créature agrippée par le vampirien, incapable d'agir ou entravée. Touché : 6 (1d6 + 3) dégâts perforants + 7 (2d6) dégâts nécrotiques. Le maximum de points de vie de la cible est réduit d'un montant égal à la quantité de dégâts nécrotiques subis, et le vampirien récupère un nombre de points de vie équivalent. Cette réduction perdure jusqu'à ce que la cible termine un repos long. La cible meurt si cet effet réduit son maximum de points de vie à 0."
    attaque: +6 au toucher
```
