---
aliases:
  - Dragon d'airain, adulte
tags:
  - monstre
  - bestiaire
type: Dragon
facteur_puissance: 13 (10000 PX)
---

# Dragon d'airain, adulte

```dnd-monstre
name: "Dragon d'airain, adulte"
type: Dragon
taille: Tres grand
alignement: chaotique bon
ca: 18 (armure naturelle)
pv: 172 (15d12 + 75)
vitesse: 12 m, creusement 9 m, vol 24 m
for: 23
dex: 10
con: 21
int: 14
sag: 13
cha: 17
sauvegardes: Dex +5, Con +10, Sag +6, Cha +8
sens: vision aveugle 18 m, vision dans le noir 36 m, Perception passive 21
langues: commun, draconique
facteur_puissance: 13 (10000 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +5
  - Histoire +7
  - Perception +11
  - Persuasion +8
immunites:
  - feu
traits:
  - name: Résistance légendaire (3/jour)
    description: Si le dragon échoue à un jet de sauvegarde, il peut décider de transformer cet échec en réussite.
actions:
  - name: Attaques multiples
    description: "Le dragon peut utiliser sa Présence terrifiante. Il effectue ensuite trois attaques : une de morsure et deux avec ses griffes."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +11 au toucher, allonge 3 m, une cible. Touché : 17 (2d10 + 6) dégâts perforants."
    attaque: +11 au toucher
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +11 au toucher, allonge 1,50 m, une cible. Touché : 13 (2d6 + 6) dégâts tranchants."
    attaque: +11 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +11 au toucher, allonge 4,50 m, une cible. Touché : 15 (2d8 + 6) dégâts contondants."
    attaque: +11 au toucher
  - name: Présence terrifiante
    description: "Chaque créature que le dragon choisit, se trouvant à 36 mètres ou moins de lui et consciente de sa présence, doit réussir un jet de sauvegarde de Sagesse DD 16 ou être effrayée pendant 1 minute. Une créature peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite. Si le jet de sauvegarde d'une créature est une réussite ou si l'effet prend fin pour elle, la créature est immunisée à la Présence terrifiante du dragon pour les prochaines 24 heures."
  - name: Souffles (Recharge 5-6)
    description: "Le dragon utilise l'un des souffles de combat présentés ci-dessous."
  - name: Souffle de feu
    description: "Le dragon exhale des flammes sur une ligne de 18 mètres de long et de 1,50 mètre de large. Chaque créature présente dans la zone doit effectuer un jet de sauvegarde de Dextérité DD 18, subissant 45 (13d6) dégâts de feu en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: Souffle de sommeil
    description: "Le dragon exhale un gaz soporifique dans un cône de 18 mètres. Chaque créature dans cette zone doit réussir un jet de sauvegarde de Constitution DD 18 ou tomber inconsciente pendant 10 minutes. Cet effet prend fin pour une créature si elle subit des dégâts ou si quelqu'un utilise son action pour la réveiller."
legendaires:
  - name: Détection
    description: Le dragon effectue un jet de Sagesse (Perception).
  - name: Attaque avec la queue
    description: Le dragon effectue une attaque avec sa queue.
  - name: Attaque avec les ailes (coûte 2 actions)
    description: "Le dragon bat des ailes. Chaque créature située à 3 mètres ou moins du dragon doit réussir un jet de sauvegarde de Dextérité DD 19 ou subir 13 (2d6 + 6) dégâts contondants et être jetée à terre. Le dragon peut ensuite s'envoler de la moitié de sa vitesse de vol."
```
