---
aliases:
  - Vrock
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 6 (2300 PX)
---

# Vrock

```dnd-monstre
name: Vrock
type: Fiélon
taille: Grand
alignement: chaotique mauvais
ca: 15 (armure naturelle)
pv: 104 (11d10 + 44)
vitesse: 12 m, vol 18 m
for: 17
dex: 15
con: 18
int: 8
sag: 13
cha: 8
sauvegardes: Dex +5, Sag +4, Cha +2
sens: vision dans le noir 36 m, Perception passive 11
langues: abyssal, télépathie 36 m
facteur_puissance: 6 (2300 PX)
immunites_etats: empoisonné
source: Monster Manual (SRD)
immunites:
  - poison
résistances:
  - froid
  - feu
  - foudre ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Résistance à la magie
    description: Le vrock a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
actions:
  - name: Attaques multiples
    description: "Le vrock effectue deux attaques : une avec son bec et une avec ses serres."
  - name: Bec
    description: "Attaque au corps à corps avec une arme : +6 au toucher, allonge 1,50 m, une cible. Touché : 10 (2d6 + 3) dégâts perforants"
    attaque: +6 au toucher
  - name: Serres
    description: "Attaque au corps à corps avec une arme : +6 au toucher, allonge 1,50 m, une cible. Touché : 14 (2d10 + 3) dégâts tranchants."
    attaque: +6 au toucher
  - name: Spores (Recharge 6)
    description: "Un nuage de spores toxiques se répand du vrock dans un rayon de 4,50 mètres. Les spores contournent les angles de murs. Chaque créature qui se trouve dans la zone d'effet doit réussir un jet de sauvegarde de Constitution DD 14 ou être empoisonnée. Tant qu'elle est empoisonnée de la sorte, la cible subit 5 (1d10) dégâts de poison au début de chacun de ses tours. Une cible peut retenter un jet de sauvegarde à la fin de chacun de ses tours, mettant ainsi fin à son empoisonnement en cas de réussite. Vider une fiole d'eau bénite sur la cible met également fin à cet effet d'empoisonnement."
  - name: Cri étourdissant (1/jour)
    description: "Le vrock émet un cri horrible. Chaque créature dans un rayon de 6 mètres autour du vrock, qui peut l'entendre et n'est pas un démon, doit réussir un jet de sauvegarde de Constitution DD 14 ou être étourdie jusqu'à la fin du prochain tour du vrock."
```
