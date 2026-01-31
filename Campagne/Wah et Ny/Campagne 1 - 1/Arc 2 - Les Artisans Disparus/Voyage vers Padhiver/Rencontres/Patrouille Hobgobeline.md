---
tags:
  - rencontre
  - bestiaire
---

# Patrouille Hobgobeline

Une petite unité disciplinée de [[La Légion de Fer]], probablement des éclaireurs ou des collecteurs de taxes illégaux. Ils travaillent en équipe pour maximiser leur efficacité martiale.

## Tactiques
*   **Formation :** Ils restent à 1,5m les uns des autres pour activer leur *Avantage Martial*.
*   **Cible prioritaire :** Ils visent la cible la plus faible ou celle qui lance des sorts (Silas).
*   **Moral :** Ils ne fuient pas facilement, mais si le chef tombe, les autres peuvent se replier en bon ordre pour faire un rapport.

---

## Hobgoblin (Soldat)
*Soldat discipliné en cotte de mailles.*

```dnd-monstre
name: Hobgoblin
type: Humanoïde (Gobelinoïde)
taille: Moyenne
alignement: Loyal Mauvais
ca: 18 (Cotte de mailles + Bouclier)
pv: 11 (2d8 + 2)
vitesse: 9 m
for: 13 (+1)
dex: 12 (+1)
con: 12 (+1)
int: 10 (+0)
sag: 10 (+0)
cha: 9 (-1)
sens: Vision dans le noir 18 m, Perception passive 10
langues: Commun, Gobelin
facteur_puissance: 1/2 (100 PX)
traits:
  - name: Avantage martial
    description: "Une fois par tour, le hobgobelin peut infliger 7 (2d6) dégâts supplémentaires à une créature qu'il touche avec une attaque d'arme si cette créature est à 1,50 mètre ou moins d'un allié du hobgobelin qui n'est pas neutralisé."
actions:
  - name: Épée longue
    description: "Attaque au corps à corps : +3 au toucher, allonge 1,50 m, une cible. Touché : 5 (1d8 + 1) dégâts tranchants."
    attaque: +3 au toucher
  - name: Arc long
    description: "Attaque à distance : +3 au toucher, portée 45/180 m, une cible. Touché : 5 (1d8 + 1) dégâts perforants."
    attaque: +3 au toucher
```

---

## Hobgoblin (Sergent)
*Le chef de l'escouade, plus robuste et aboyant des ordres.*

```dnd-monstre
name: Sergent Hobgoblin
type: Humanoïde (Gobelinoïde)
taille: Moyenne
alignement: Loyal Mauvais
ca: 17 (Feuilletée + Bouclier)
pv: 27 (5d8 + 5)
vitesse: 9 m
for: 15 (+2)
dex: 14 (+2)
con: 13 (+1)
int: 12 (+1)
sag: 10 (+0)
cha: 13 (+1)
sens: Vision dans le noir 18 m, Perception passive 10
langues: Commun, Gobelin
facteur_puissance: 1 (200 PX)
traits:
  - name: Avantage martial
    description: "Une fois par tour, le hobgobelin peut infliger 10 (3d6) dégâts supplémentaires à une créature qu'il touche avec une attaque d'arme si cette créature est à 1,50 mètre ou moins d'un allié du hobgobelin qui n'est pas neutralisé."
actions:
  - name: Attaques multiples
    description: "Le sergent effectue deux attaques au corps à corps."
  - name: Épée longue
    description: "Attaque au corps à corps : +4 au toucher, allonge 1,50 m, une cible. Touché : 6 (1d8 + 2) dégâts tranchants."
    attaque: +4 au toucher
  - name: Javelot
    description: "Attaque à distance ou au corps à corps : +4 au toucher, portée 9/36 m, une cible. Touché : 5 (1d6 + 2) dégâts perforants."
    attaque: +4 au toucher
réactions:
  - name: Parade
    description: "Le sergent ajoute 2 à sa CA contre une attaque au corps à corps qui devrait le toucher. Il doit voir l'attaquant et manier une arme de corps à corps."
```
