---
aliases:
  - Dragon blanc, adulte
tags:
  - monstre
  - bestiaire
type: Dragon
facteur_puissance: 13 (10000 PX)
---

# Dragon blanc, adulte

```dnd-monstre
name: Dragon blanc, adulte
type: Dragon
taille: Tres grand
alignement: chaotique mauvais
ca: 18 (armure naturelle)
pv: 200 (16d12 + 96)
vitesse: 12 m, creusement 9 m, nage 12 m, vol 24 m
for: 22
dex: 10
con: 22
int: 8
sag: 12
cha: 12
sauvegardes: Dex +5, Con +11, Sag +6, Cha +6
sens: vision aveugle 18 m, vision dans le noir 36 m, Perception passive 21
langues: commun, draconique
facteur_puissance: 13 (10000 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +5
  - Perception +11
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
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +11 au toucher, allonge 1,50 m, une cible. Touché : 13 (2d6 + 6) dégâts tranchants."
    attaque: +11 au toucher
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +11 au toucher, allonge 3 m, une cible. Touché : 17 (2d10 + 6) dégâts perforants + 4 (1d8) dégâts de froid."
    attaque: +11 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +11 au toucher, allonge 4,50 m, une cible. Touché : 15 (2d8 + 6) dégâts contondants."
    attaque: +11 au toucher
  - name: Présence terrifiante
    description: "Chaque créature que le dragon choisit, se trouvant à 36 mètres ou moins du dragon et consciente de sa présence, doit réussir un jet de sauvegarde de Sagesse DD 14 ou être effrayée pendant 1 minute. Une créature peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite. Si le jet de sauvegarde d'une créature est une réussite ou si l'effet prend fin pour elle, la créature est immunisée à la Présence terrifiante du dragon pour les prochaines 24 heures."
  - name: Souffle de froid (Recharge 5-6)
    description: "Le dragon crache une tempête de glace dans un cône de 18 mètres. Chaque créature dans la zone d'effet doit effectuer un jet de sauvegarde de Constitution DD 19, subissant 54 (12d8) dégâts de froid en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
legendaires:
  - name: Détection
    description: Le dragon effectue un jet de Sagesse (Perception).
  - name: Attaque avec la queue
    description: Le dragon effectue une attaque avec sa queue.
  - name: Attaque avec les ailes (coûte 2 actions)
    description: "Le dragon bat des ailes. Chaque créature située à 3 mètres ou moins du dragon doit réussir un jet de sauvegarde de Dextérité DD 19 ou subir 13 (2d6 + 6) dégâts contondants et être jetée à terre. Le dragon peut ensuite s'envoler de la moitié de sa vitesse de vol."
```
