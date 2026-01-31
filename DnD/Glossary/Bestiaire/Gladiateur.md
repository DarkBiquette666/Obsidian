---
aliases:
  - Gladiateur
tags:
  - monstre
  - bestiaire
type: Humanoïde
facteur_puissance: 5 (1800 PX)
---

# Gladiateur

```dnd-monstre
name: Gladiateur
type: Humanoïde
taille: Moyen
alignement: tout alignement
ca: 16 (armure de cuir clouté, bouclier)
pv: 112 (15d8 + 45)
vitesse: 9 m
for: 18
dex: 15
con: 16
int: 10
sag: 12
cha: 15
sauvegardes: For +7, Dex +5, Con +6
sens: Perception passive 11
langues: une langue au choix (généralement le commun)
facteur_puissance: 5 (1800 PX)
source: Monster Manual (SRD)
compétences:
  - Athlétisme +10
  - Intimidation +5
traits:
  - name: Brave
    description: Le gladiateur a un avantage aux jets de sauvegarde pour ne pas être effrayé.
  - name: Brutal
    description: "Une arme de corps à corps inflige un dé extra de ses dégâts si le gladiateur touche avec celle-ci (inclus dans l'attaque ci-dessous)."
actions:
  - name: Attaques multiples
    description: Le gladiateur effectue trois attaques au corps à corps ou deux attaques à distance.
  - name: Lance
    description: "Attaque au corps à corps ou à distance avec une arme : +7 au toucher, allonge 1,50 m ou portée 6/18 m, une cible. Touché : 11 (2d6 + 4) dégâts perforants, ou 13 (2d8 + 4) dégâts perforants si utilisée avec les deux mains pour une attaque au corps à corps."
    attaque: +7 au toucher
  - name: Coup de bouclier
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une créature. Touché : 9 (2d4 + 4) dégâts contondants. Si la cible est une créature de taille M ou inférieure, elle doit réussir un jet de sauvegarde de Force DD 15 pour ne pas tomber à terre."
    attaque: +7 au toucher
reactions:
  - name: Parade
    description: "Le gladiateur ajoute 3 à sa CA contre une attaque au corps à corps qui le toucherait. Pour ce faire, il doit voir l'attaquant et avoir en main une arme de corps à corps."
```
