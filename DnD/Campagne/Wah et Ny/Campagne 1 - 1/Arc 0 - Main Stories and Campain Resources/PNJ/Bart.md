---
type: pnj
role: antagoniste
faction: Village de Trépied
status: vivant
tags:
  - pnj
  - mineur
  - barbare
  - mutant
aliases:
  - Bart le Faible
  - Bart l'Enragé
---

# Bart (Le Junkie de Puissance)

> **Identité :** Humain (25 ans) - Ouvrier agricole / Barbare (sous influence)
> **Trait Marquant :**
> *   *Normal :* Squelettique, tremblements incontrôlables, yeux injectés de sang.
> *   *Enragé :* Veines noires saillantes, muscles qui déchirent ses vêtements et sa peau, bave violette.
> **Désir Immédiat :** Retrouver sa "gloire" (la force surhumaine) à n'importe quel prix.

## 🎭 Roleplay Rapide
*   **Attitude :** [Désespéré / Paranoïaque / Ultraviolent]. Il alterne entre supplications larmoyantes et accès de rage meurtrière.
*   **Ce qu'il sait :** Il y a encore un tonneau "du bon jus" dans la vieille remise du forgeron.
*   **Ce qu'il ignore :** La potion le tue à petit feu. Son cœur est au bord de l'explosion.

## ⚔️ Statblock : Bart (Sous Elixir)

> [!warning] Condition Spéciale : Overdose
> Bart perd **5 points de vie temporaires** à la fin de chaque tour. Une fois ses PV temporaires épuisés, il perd **1d6 PV réels** à la fin de chaque tour. Son corps se brise littéralement sous le poids de sa propre force.

```dnd-monstre
name: Bart (Enragé)
type: Humanoïde (Humain)
taille: Moyen
alignement: Chaotique Mauvais
ca: 15 (Peau pétrifiée)
pv: 9 (1d12 - 3)
pv_temporaires: 20
vitesse: 6 m
for: 20 (+5)
dex: 5 (-3)
con: 5 (-3)
int: 6 (-2)
sag: 8 (-1)
cha: 6 (-2)
sens: Perception passive 9
langues: Commun (hurlements)
facteur_puissance: 1 (200 PX)
traits:
  - name: Peau Pétrifiée
    description: "L'élixir a calcifié la peau de Bart, lui conférant une CA fixe de 15. Il possède une résistance aux dégâts tranchants et perforants non-magiques, mais une vulnérabilité aux dégâts de tonnerre."
  - name: Rage Chimique (2/jour)
    description: "Par une action bonus, Bart entre en rage. Il a un avantage aux tests et jets de sauvegarde de Force, un bonus de +2 aux dégâts de corps à corps (inclus), et la résistance aux dégâts contondants, perforants et tranchants."
  - name: Masse Incontrôlable
    description: "Bart a un avantage sur les jets de Force. Cependant, il a un désavantage sur tous les jets de Sagesse et d'Intelligence."
  - name: Raideur Cadavérique
    description: "Bart a un désavantage permanent sur les jets de sauvegarde de Dextérité."
actions:
  - name: Coup de Poing Brise-Os
    description: "Attaque au corps à corps avec une arme : +7 au toucher, allonge 1,50 m, une cible. Touché : 12 (1d10 + 7) dégâts contondants. Bart subit lui-même 3 (1d6) dégâts de contrecoup (déduits de ses PV temporaires en priorité)."
  - name: Étreinte du Mort
    description: "Bart tente de broyer une cible. +7 au toucher. La cible est agrippée (DD 15 FOR pour s'échapper). Au début de chaque tour de Bart, la cible agrippée subit 10 (1d6 + 7) dégâts contondants automatiquement (DD 15 Const+For pour reduire de 1/2) mais les os de bart se brise et il subit également 10 point de dégat (déduits de ses PV temporaires en priorité)."
```