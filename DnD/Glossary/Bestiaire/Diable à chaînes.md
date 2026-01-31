---
aliases:
  - Diable à chaînes
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 8 (3900 PX)
---

# Diable à chaînes

```dnd-monstre
name: Diable à chaînes
type: Fiélon
taille: Moyen
alignement: loyal mauvais
ca: 16 (armure naturelle)
pv: 85 (10d8 + 40)
vitesse: 9 m
for: 18
dex: 15
con: 18
int: 11
sag: 12
cha: 14
sauvegardes: Con +7, Sag +4, Cha +5
sens: vision dans le noir 36 m, Perception passive 11
langues: infernal, télépathie 36 m
facteur_puissance: 8 (3900 PX)
immunites_etats: empoisonné
source: Monster Manual (SRD)
immunites:
  - feu
  - poison
résistances:
  - froid ; contondant
  - "perforant et tranchant d'attaques non magiques qui ne sont pas en argent"
traits:
  - name: Vision de diable
    description: Des ténèbres magiques ne gênent pas la vision dans le noir du diable.
  - name: Résistance à la magie
    description: Le diable a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
actions:
  - name: Attaques multiples
    description: Le diable effectue deux attaques avec ses chaînes.
  - name: Chaine
    description: "Attaque au corps à corps avec une arme : +8 au toucher, allonge 3 m, une cible. Touché : 11 (2d6 + 4) dégâts tranchants. La cible se retrouve agrippée (évasion DD 14) si le diable n'a pas déjà agrippé une créature. Tant qu'elle est agrippée, la cible est entravée et subit 7 (2d6) dégâts perforants au début de chacun de ses tours."
    attaque: +8 au toucher
  - name: Animation des chaînes (Recharge après un repos court ou long)
    description: "Le diable peut faire éclore des barbelées coupant sur 1 à 4 chaines qu'il voit et situées dans un rayon de 18 mètres autour de lui, les animant et les contrôlant, à condition qu'elles ne soient ni portées ni transportées par quelqu'un. Chaque chaine animée est un objet ayant une CA de 20, 20 pv, une résistance aux dégâts perforants et l'immunité aux dégâts psychiques et de tonnerre. Lorsque le diable utilise ses Attaques multiples durant son tour, il peut utiliser chaque chaîne animée pour faire une attaque supplémentaire. Une chaine animée peut agripper une créature de son choix, mais ne peut plus attaquer tant qu'elle agrippe. Une chaîne animée redevient inanimée si ses points de vie tombent à zéro ou si le diable est incapable d'agir ou meurt."
reactions:
  - name: Masque déstabilisant
    description: "Quand une créature débute son tour à 9 mètres ou moins du diable et que celui-ci peut la voir, le diable peut donner l'illusion d'être un être décédé, qui était très aimé ou dêtesté par cette créature. Si la créature peut voir le diable, elle doit réussir un jet de sauvegarde de Sagesse DD 14 ou être effrayée jusqu'à la fin de son tour."
```
