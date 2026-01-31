---
aliases:
  - Argent
tags:
  - monstre
  - bestiaire
  - homebrew
type: Bête
---

# Argent (Lévrier du Nord)

*Basé sur Chien de Guerre (Niveau 3)*

```dnd-monstre
name: Argent
type: Bête
taille: Moyen
alignement: Neutre
ca: 11
pv: Niveau Inquisiteur x 3
vitesse: 15 m (Bonus Race)
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
  - name: Acrobatie
    description: ": +5 (Bonus Race)"
traits:
  - name: Description
    description: "Un lévrier svelte au poil gris orage. Elle possède des yeux vairons (un bleu glace, un ambre) particulièrement frappants."
  - name: Personnalité
    description: "Observatrice et silencieuse, elle communique beaucoup par le regard. Elle est très liée à son partenaire mais garde son indépendance."
  - name: Odorat aiguisé
    description: "Avantage aux jets de perception basés sur l'odorat."
  - name: Repos rapide
    description: "Récupère la moitié des PV max après un repos court."
  - name: Tactique de Meute
    description: "Avantage aux jets d'attaque contre une créature si un allié est à 1,50m d'elle."
actions:
  - name: Morsure Rapide
    description: "Attaque d'arme au corps à corps : +3 au toucher, allonge 1,50 m. Touché : 6 (1d6 + 1 + Bonus Maîtrise) dégâts perforants. JS Force DD 13 ou à terre."
    attaque: +3 au toucher
```