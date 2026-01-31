---
aliases:
  - Kraken
tags:
  - monstre
  - bestiaire
type: Monstruosité
facteur_puissance: 23 (50000 PX)
---

# Kraken

```dnd-monstre
name: Kraken
type: Monstruosité
taille: Grand
alignement: chaotique mauvais
ca: 18 (armure naturelle)
pv: 472 (27d20 + 189)
vitesse: 6 m, nage 18 m
for: 30
dex: 11
con: 25
int: 22
sag: 18
cha: 20
sauvegardes: For +17, Dex +7, Con +14, Int +13, Sag +11
sens: vision véritable 36 m, Perception passive 14
langues: "comprend l'abyssal, le céleste, l'infernal et le primordial mais ne peut pas parler, télépathie 36 m"
facteur_puissance: 23 (50000 PX)
immunites_etats: effrayé, paralysé
source: Monster Manual (SRD)
immunites:
  - foudre ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Amphibien
    description: "Le kraken peut respirer aussi bien dans l'air que sous l'eau."
  - name: Liberté de mouvement
    description: "Le kraken ignore les terrains difficiles, et les effets magiques ne peuvent pas réduire sa vitesse de déplacement ou l'entraver. Il peut dépenser 1,50 mètre de son déplacement pour s'échapper des entraves non magiques ou se libérer de l'état agrippé."
  - name: Monstre de siège
    description: "Le kraken inflige le double des dégâts aux objets et structures qu'il attaque."
actions:
  - name: Attaques multiples
    description: "Le kraken effectue trois attaques avec ses tentacules, il peut remplacer chacune d'elles par une action Catapultage."
  - name: Morsure
    description: "Attaque au corps à corps avec une arme : +17 au toucher, allonge 1,50 m, une cible. Touché : 23 (3d8 + 10) dégâts perforants. Si la cible est une créature de taille G ou inférieure agrippée par le kraken, la créature est engloutie, et n'est plus considérée comme agrippée. Tant qu'elle est engloutie par le kraken, la créature est aveuglée et entravée, elle possède un abri total contre les attaques et tout autre effet provenant de l'extérieur du kraken, et elle subit 42 (12d6) dégâts d'acide au début de chacun des tours du kraken. Si le kraken subit 50 dégâts ou plus en un seul tour de la part d'une créature qu'il a engloutie, le kraken doit réussir un jet de sauvegarde de Constitution DD 25 à la fin de ce tour ou régurgiter toutes les créatures qu'il a avalées, lesquelles se retrouvent à terre dans un rayon de 3 mètres autour du kraken. Si le kraken meurt, une créature avalée n'est plus considérée comme entravée par le kraken et peut s'échapper de son cadavre en utilisant 4,50 mètres de déplacement, sortant à plat ventre."
    attaque: +17 au toucher
  - name: Tentacule
    description: "Attaque au corps à corps avec une arme : +17 au toucher, allonge 9 m, une cible. Touché : 20 (3d6 + 10) dégâts contondants, et la cible est agrippée (DD 18 pour s'échapper). Tant qu'elle est agrippée, la cible est entravée. Le kraken possède 10 tentacules, chacune d'entre elles pouvant agripper une cible."
    attaque: +17 au toucher
  - name: Catapultage
    description: Une créature agrippée ou un objet tenu, de taille G ou inférieure, par le kraken est lancé à 18 mètres dans une direction aléatoire et jeté à terre. Si une cible lancée percute une surface solide, la cible subit 3 (1d6) dégâts contondants tous les 3 mètres parcourus dans les airs. Si la cible est lancée sur une autre créature, cette créature doit réussir un jet de sauvegarde de Dextérité DD 18 ou subir la même quantité de dégâts et être jetée à terre.
  - name: "Tempête d'éclairs"
    description: "Le kraken peut créer par magie trois éclairs, chacun d'entre eux pouvant frapper une cible que le kraken peut voir dans un rayon de 36 mètres autour de lui. Une cible doit effectuer un jet de sauvegarde de Dextérité DD 23, subissant 22 (4d10) dégâts de foudre en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
legendaires:
  - name: Attaque de tentacule ou Catapultage
    description: Le kraken effectue une attaque avec ses tentacules ou utilise son Catapultage.
  - name: "Tempête d'éclairs (coûte 2 actions)"
    description: "Le kraken utilise sa Tempête d'éclairs."
  - name: "Nuage d'encre (coûte 3 actions)"
    description: "Tant qu'il se trouve sous l'eau, le kraken expulse un nuage d'encre dans un rayon de 18 mètres. Le nuage contourne les angles des murs, et cette zone est fortement obscurcie pour toute créature à l'exception du kraken. Chaque créature, à l'exception du kraken, qui termine son tour dans le nuage doit effectuer un jet de sauvegarde de Constitution DD 23, subissant 16 (3d10) dégâts de poison en cas d'échec, ou la moitié de ces dégâts en cas de réussite. Un courant fort disperse le nuage d'encre, qui disparaît de toute façon à la fin du prochain tour du kraken."
```
