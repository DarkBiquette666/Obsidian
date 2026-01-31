---
aliases:
  - Spectre
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Spectre (Doberman de l'Ombre)

*Basé sur Chien de Guerre (Niveau 3)*

```dnd-monstre
name: Spectre
type: Bête
taille: Moyen
alignement: Neutre
ca: 11
pv: Niveau Inquisiteur x 3
vitesse: 12 m
for: 13
dex: 12
con: 12
int: 3
sag: 12
cha: 7
sens: Perception passive 15
langues: Comprend celles de l'inquisiteur
facteur_puissance: Évolutif
compétences:
  - name: Perception
    description: ": +5"
  - name: Athlétisme
    description: ": +5"
  - name: Discrétion
    description: ": +5 (Bonus Race)"
traits:
  - name: Description
    description: "Semblable à Ombre, il se déplace comme un fantôme dans l'obscurité. Son pelage mat absorbe la lumière."
  - name: Personnalité
    description: "Aussi furtif et discipliné que son partenaire. Il excelle dans les approches détournées et les attaques surprises."
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Frappe de l'Ombre
    description: "Avantage attaque si caché/surprise. Critique sur 18-20 dans ces conditions."
actions:
  - name: Morsure Silencieuse
    description: "Attaque d'arme au corps à corps : +3 au toucher, allonge 1,50 m. Touché : 6 (1d6 + 1 + Bonus Maîtrise) dégâts perforants. JS Force DD 13 ou à terre."
    attaque: +3 au toucher
actions_bonus:
  - name: Manteau d'Ombre
    description: ": Action Bonus : Se Cacher (si lumière faible/ténèbres)."
```
