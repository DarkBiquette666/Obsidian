---
aliases:
  - Dragon blanc, ancien
tags:
  - monstre
  - bestiaire
type: Dragon
facteur_puissance: 20 (25000 PX)
---

# Dragon blanc, ancien

```dnd-monstre
name: Dragon blanc, ancien
type: Dragon
taille: Grand
alignement: chaotique mauvais
ca: 20 (armure naturelle)
pv: 333 (18d20 + 144)
vitesse: 12 m, creusement 12 m, nage 12 m, vol 24 m
for: 26
dex: 10
con: 26
int: 10
sag: 13
cha: 14
sauvegardes: Dex +6, Con +14, Sag +7, Cha +8
sens: vision aveugle 18 m, vision dans le noir 36 m, Perception passive 23
langues: commun, draconique
facteur_puissance: 20 (25000 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +6
  - Perception +13
immunites:
  - froid
traits:
  - name: Marche sur la glace
    description: "Le dragon peut se déplacer sur les sols gelés ou escalader les surfaces glacées sans avoir besoin d'effectuer un jet de caractéristique. De plus, les terrains difficiles formés de glace ou de neige ne lui coûtent pas de mouvement supplémentaire."
  - name: Résistance légendaire (3/jour)
    description: Si le dragon échoue à un jet de sauvegarde, il peut décider de transformer cet échec en réussite.
actions:
  - name: Attaques multiples
    description: "Le dragon peut utiliser sa Présence terrifiante. Il effectue ensuite trois attaques : une de morsure et deux avec ses griffes."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 4,50 m, une cible. Touché : 19 (2d10 + 8) dégâts perforants + 9 (2d8) dégâts de froid."
    attaque: +14 au toucher
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 3 m, une cible. Touché : 15 (2d6 + 8) dégâts tranchants."
    attaque: +14 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 6 m, une cible. Touché : 17 (2d8 + 8) dégâts contondants."
    attaque: +14 au toucher
  - name: Présence terrifiante
    description: "Chaque créature que le dragon choisit, se trouvant à 36 mètres ou moins du dragon et consciente de sa présence, doit réussir un jet de sauvegarde de Sagesse DD 16 ou être effrayée pendant 1 minute. Une créature peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite. Si le jet de sauvegarde d'une créature est une réussite ou si l'effet prend fin pour elle, la créature est immunisée à la Présence terrifiante du dragon pour les prochaines 24 heures."
  - name: Souffle de froid (Recharge 5-6)
    description: "Le dragon crache une tempête de glace dans un cône de 27 mètres. Chaque créature dans la zone d'effet doit effectuer un jet de sauvegarde de Constitution DD 22, subissant 72 (16d8) dégâts de froid en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
legendaires:
  - name: Détection
    description: Le dragon effectue un jet de Sagesse (Perception).
  - name: Attaque avec la queue
    description: Le dragon effectue une attaque avec sa queue.
  - name: Attaque avec les ailes (coûte 2 actions)
    description: "Le dragon bat des ailes. Chaque créature située à 4,50 mètres ou moins du dragon doit réussir un jet de sauvegarde de Dextérité DD 22 ou subir 15 (2d6 + 8) dégâts contondants et être jetée à terre. Le dragon peut ensuite s'envoler de la moitié de sa vitesse de vol."
```
