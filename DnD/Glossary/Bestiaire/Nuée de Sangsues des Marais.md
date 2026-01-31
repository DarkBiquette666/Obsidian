---
aliases:
  - Nuée de Sangsues des Marais
  - Sangsues des marais
tags:
  - monstre
  - bestiaire
type: Nuée
facteur_puissance: 1 (200 PX)
---

# Nuée de Sangsues des Marais

```dnd-monstre
name: "Nuée de Sangsues des Marais"
type: Nuée de bêtes de taille TP
taille: Moyen
alignement: sans alignement
ca: 12 (naturelle)
pv: 10 (10d1)
vitesse: 1,50 m, nage 9 m
for: 1
dex: 14
con: 10
int: 1
sag: 7
cha: 1
sens: vision aveugle 3 m, Perception passive 8
langues: —
facteur_puissance: 1 (200 PX)
immunites_etats: à terre, agrippé, charmé, effrayé, entravé, étourdi, paralysé, pétrifié
résistances:
  - contondant
  - perforant
  - tranchant
traits:
  - name: Nuée
    description: "La nuée peut occuper l'espace d'une créature et vice versa, et peut passer par une ouverture suffisamment grande pour une bête de taille TP. La nuée ne peut pas regagner de points de vie ou gagner des points de vie temporaires."
  - name: Dix Sangsues
    description: "La nuée est composée de 10 sangsues géantes. Pour simplifier, on considère que chaque Point de Vie de la nuée représente une sangsue vivante."
  - name: Parasitisme Sanguin
    description: "Tant que la nuée est attachée à une créature vivante, elle lui draine 1 point de Constitution après chaque repos long (soit 1 par jour). Cette réduction ne peut pas dépasser un total de 4 points de Constitution perdus. La Constitution perdue est récupérée au rythme de 1 point par repos long une fois la nuée retirée."
  - name: Embuscade des marais
    description: "La nuée a un avantage aux tests de Dextérité (Discrétion) lorsqu'elle est immergée dans l'eau trouble."
  - name: Faiblesse à l'Eau Bénite
    description: "Si la nuée est aspergée d'une fiole d'eau bénite, toutes les sangsues meurent instantanément."
actions:
  - name: Attachement
    description: "Attaque au corps à corps avec une arme : +4 au toucher, allonge 0 m, une créature dans l'espace de la nuée. Touché : La nuée s'attache à la cible. Tant qu'elle est attachée, la nuée ne peut pas attaquer une autre cible, mais elle se déplace automatiquement avec la cible."
  - name: Retrait Brutal (Action spéciale)
    description: "Une créature peut utiliser son action pour arracher physiquement les sangsues. Elle lance **1d4** pour déterminer combien de sangsues elle parvient à saisir et arracher. Elle subit **1d4 dégâts perforants pour chaque sangsue ainsi retirée**, et la nuée perd autant de PV."
  - name: Cautérisation (Action spéciale)
    description: "Une créature peut utiliser son action et une source de feu (comme une torche) pour brûler les sangsues une par une. Le joueur doit effectuer un jet de sauvegarde de Dextérité DD 13 **pour chaque sangsue** attachée (soit un jet par PV restant de la nuée).
    - **En cas de réussite :** La sangsue est brûlée et se détache (la nuée perd 1 PV) sans dégât pour l'hôte.
    - **En cas d'échec :** La créature se brûle, subissant 1d4 dégâts de feu, et la sangsue reste attachée (la nuée ne perd pas le PV)."
```
