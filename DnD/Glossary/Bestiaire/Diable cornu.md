---
aliases:
  - Diable cornu
tags:
  - monstre
  - bestiaire
type: Fiélon
facteur_puissance: 11 (7200 PX)
---

# Diable cornu

```dnd-monstre
name: Diable cornu
type: Fiélon
taille: Grand
alignement: loyal mauvais
ca: 18 (armure naturelle)
pv: 178 (17d10 + 85)
vitesse: 6 m, vol 18 m
for: 22
dex: 17
con: 21
int: 12
sag: 16
cha: 17
sauvegardes: For +10, Dex +7, Sag +7, Cha +7
sens: vision dans le noir 36 m, Perception passive 13
langues: infernal, télépathie 36 m
facteur_puissance: 11 (7200 PX)
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
    description: "Le diable effectue trois attaques au corps à corps : deux avec sa fourche et une avec sa queue. Il peut utiliser son Jet de flammes à la place n'importe quelle attaque au corps à corps."
  - name: Fourche
    description: "Attaque au corps à corps avec une arme : +10 au toucher, allonge 3 m, une cible. Touché : 15 (2d8 + 6) dégâts perforants."
    attaque: +10 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +10 au toucher, allonge 3 m, une cible. Touché : 10 (1d8 + 6) dégâts perforants. Si la cible n'est ni un mort-vivant, ni un artificiel, elle doit réussir un jet de sauvegarde de Constitution DD 17 ou perdre 10 (3d6) points de vie au début de chacun de ses tours suivants à cause de cette plaie infernale. Chaque fois que le diable frappe la créature blessée avec cette attaque, les dégâts infligés par la plaie augmentent de 10 (3d6). N'importe quelle créature peut utiliser une action pour endiguer l'hémorragie, à condition qu'elle réussisse un jet de Sagesse (Médecine) DD 12. La plaie se referme également si la cible reçoit des soins magiques."
    attaque: +10 au toucher
  - name: Jet de flammes
    description: "Attaque à distance avec un sort : +7 au toucher, portée 45 m, une cible. Touché : 14 (4d6) dégâts de feu. Si la cible est un objet inflammable qui n'est pas porté ni tenu, elle prend feu."
    attaque: +7 au toucher
```
