---
aliases:
  - Pouding noir
tags:
  - monstre
  - bestiaire
type: Vase
facteur_puissance: 4 (1100 PX)
---

# Pouding noir

```dnd-monstre
name: Pouding noir
type: Vase
taille: Grand
alignement: sans alignement
ca: 7
pv: 85 (10d10 + 30)
vitesse: 6 m, escalade 6 m
for: 16
dex: 5
con: 16
int: 1
sag: 6
cha: 1
sens: vision aveugle 18 m (aveugle au-delà de ce rayon), Perception passive 8
langues: —
facteur_puissance: 4 (1100 PX)
immunites_etats: aveuglé, charmé, assourdi, épuisement, effrayé, à terre
source: Monster Manual (SRD)
immunites:
  - acide
  - froid
  - foudre
  - tranchant
traits:
  - name: Informe
    description: "Le pouding peut se déplacer au travers d'espaces larges de 2,50 cm sans être considéré comme passant dans un espace étroit."
  - name: Forme corrosive
    description: "Une créature qui touche le pouding ou le frappe au corps à corps, et se trouvant à 1,50 mètre ou moins de lui, subit 4 (1d8) dégâts d'acide. Toute arme non magique faite de métal ou de bois qui touche le pouding se corrode. Après avoir infligé ses dégâts, l'arme subit une diminution permanente et cumulable de -1 aux dégâts. Si sa diminution atteint -5, l'arme est détruite. Une munition non magique faite de métal ou de bois et qui touche le pouding est détruite après avoir infligé ses dégâts. Le pouding peut absorber jusqu'à 5 cm d'épaisseur de bois ou de métal non magique en 1 tour."
  - name: "Pattes d'araignée"
    description: "Le pouding peut escalader des surfaces difficiles et être au plafond la tête en bas sans avoir besoin d'effectuer un jet de caractéristique."
actions:
  - name: Pseudopode
    description: "Attaque au corps à corps avec une arme : +5 au toucher, allonge 1,50 m, une cible. Touché : 6 (1d6 + 3) dégâts contondants + 18 (4d8) dégâts d'acide. De plus, une armure non magique portée par la cible est en partie dissoute et subit une diminution permanente et cumulable de -1 à la CA qu'elle confère. L'armure est détruite si la diminution de CA fait tomber la CA de l'armure à 10."
    attaque: +5 au toucher
reactions:
  - name: Division
    description: "Lorsqu'un pouding de taille M ou supérieure subit des dégâts de foudre ou des dégâts tranchants, il se divise en 2 nouveaux poudings s'il lui reste au moins 10 points de vie. Chaque nouveau pouding possède la moitié des points de vie de l'original, arrondis à l'entier inférieur. Les nouveaux poudings font une taille de moins que le pouding original."
```
