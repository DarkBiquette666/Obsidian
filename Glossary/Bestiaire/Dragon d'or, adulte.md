---
aliases:
  - Dragon d'or, adulte
tags:
  - monstre
  - bestiaire
type: Dragon
facteur_puissance: 17 (18000 PX)
---

# Dragon d'or, adulte

```dnd-monstre
name: "Dragon d'or, adulte"
type: Dragon
taille: Tres grand
alignement: loyal bon
ca: 19 (armure naturelle)
pv: 256 (19d12 + 133)
vitesse: 12 m, nage 12 m, vol 24 m
for: 27
dex: 14
con: 25
int: 16
sag: 15
cha: 24
sauvegardes: Dex +8, Con +13, Sag +8, Cha +13
sens: vision aveugle 18 m, vision dans le noir 36 m, Perception passive 24
langues: commun, draconique
facteur_puissance: 17 (18000 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +8
  - Intuition +8
  - Perception +14
  - Persuasion +13
immunites:
  - feu
traits:
  - name: Amphibien
    description: "Le dragon peut respirer aussi bien dans l'air que sous l'eau."
  - name: Résistance légendaire (3/jour)
    description: Si le dragon échoue à un jet de sauvegarde, il peut décider de transformer cet échec en réussite.
actions:
  - name: Attaques multiples
    description: "Le dragon peut utiliser sa Présence terrifiante. Il effectue ensuite trois attaques : une de morsure et deux avec ses griffes."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 3 m, une cible. Touché : 19 (2d10 + 8) dégâts perforants."
    attaque: +14 au toucher
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 1,50 m, une cible. Touché : 15 (2d6 + 8) dégâts tranchants."
    attaque: +14 au toucher
  - name: Queue
    description: "Attaque au corps à corps avec une arme : +14 au toucher, allonge 4,50 m, une cible. Touché : 17 (2d8 + 8) dégâts contondants."
    attaque: +14 au toucher
  - name: Présence terrifiante
    description: "Chaque créature que le dragon choisit, se trouvant à 36 mètres ou moins de lui et consciente de sa présence, doit réussir un jet de sauvegarde de Sagesse DD 21 ou être effrayée pendant 1 minute. Une créature peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite. Si le jet de sauvegarde d'une créature est une réussite ou si l'effet prend fin pour elle, la créature est immunisée à la Présence terrifiante du dragon pour les prochaines 24 heures."
  - name: Souffles (Recharge 5-6)
    description: "Le dragon utilise l'un des souffles de combat présentés ci-dessous."
  - name: Souffle de feu
    description: "Le dragon crache des flammes dans un cône de 18 mètres. Chaque créature présente dans la zone doit effectuer un jet de sauvegarde de Dextérité DD 21, subissant 66 (12d10) dégâts de feu en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: Souffle affaiblissant
    description: "Le dragon exhale un gaz dans un cône de 18 mètres. Chaque créature présente dans la zone doit réussir un jet de sauvegarde de Force DD 21 ou avoir un désavantage aux jets d'attaque basés sur la Force, aux jets de Force et aux jets de sauvegarde de Force. L'effet dure 1 minute. Une créature peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite à ce nouveau jet de sauvegarde."
  - name: Changement de forme
    description: "Le dragon se métamorphose magiquement en un humanoïde ou en une bête d'un FP inférieur ou égal au sien, ou bien retrouve sa forme véritable. Il retrouve également sa forme véritable lorsqu'il meurt. Tout l'équipement qu'il porte ou transporte est absorbé ou porté par sa nouvelle forme (au choix du dragon). Dans sa nouvelle forme, le dragon conserve son alignement, ses points de vie, ses dés de vie, sa capacité à parler, ses maîtrises, sa résistance légendaire, ses actions de repaire, ses valeurs de caractéristique d'Intelligence, de Sagesse et de Charisme, ainsi que cette action. Ses statistiques et ses capacités sont quant à elles remplacées par celles de sa nouvelle forme, à l'exception des compétences de classe ou des actions légendaires de cette forme."
legendaires:
  - name: Détection
    description: Le dragon effectue un jet de Sagesse (Perception).
  - name: Attaque avec la queue
    description: Le dragon effectue une attaque avec sa queue.
  - name: Attaque avec les ailes (coûte 2 actions)
    description: "Le dragon bat des ailes. Chaque créature située à 3 mètres ou moins du dragon doit réussir un jet de sauvegarde de Dextérité DD 22 ou subir 15 (2d6 + 8) dégâts contondants et être jetée à terre. Le dragon peut ensuite s'envoler de la moitié de sa vitesse de vol."
```
