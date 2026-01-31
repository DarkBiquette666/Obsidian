---
aliases:
  - Troll des marais
  - Troll bourbeux
tags:
  - monstre
  - bestiaire
  - homebrew
type: Geant
facteur_puissance: 3 (700 PX)
---

# Troll des Marais

*Plus petit et plus sournois que ses cousins des montagnes, le troll des marais a evolue pour chasser dans les eaux stagnantes et les tourbieres. Sa peau verdatre est couverte d'une mousse visqueuse qui lui permet de se fondre dans son environnement. Moins puissant qu'un troll adulte, il compense par sa ruse et sa capacite a surprendre ses proies.*

```dnd-monstre
name: Troll des Marais
type: Geant
taille: Grand
alignement: chaotique mauvais
ca: "13 (armure naturelle)"
pv: 52 (7d10 + 14)
vitesse: 9 m, nage 9 m
for: 16
dex: 12
con: 14
int: 6
sag: 10
cha: 5
competences: Discretion +3, Perception +2
sens: vision dans le noir 18 m, Perception passive 12
langues: geant
facteur_puissance: 3 (700 PX)
source: Homebrew
capacites:
  - name: Regeneration
    description: "Le troll des marais recupere 5 points de vie au debut de son tour. Si le troll subit des degats de feu ou d'acide, ce trait ne fonctionne pas au debut de son prochain tour. Le troll ne meurt que s'il commence son tour avec 0 point de vie et ne se regenere pas."
  - name: Odorat aiguise
    description: "Le troll a l'avantage aux jets de Sagesse (Perception) bases sur l'odorat."
  - name: Camouflage des marecages
    description: "Le troll a l'avantage aux jets de Dexterite (Discretion) effectues pour se cacher dans un terrain marecageux ou boueux."
  - name: Amphibie
    description: "Le troll peut respirer a l'air libre et sous l'eau."
  - name: Puanteur
    description: "Toute creature qui commence son tour dans un rayon de 3 metres du troll doit reussir un jet de sauvegarde de Constitution DD 12, ou etre empoisonnee jusqu'au debut de son prochain tour. En cas de reussite, la creature est immunisee contre la Puanteur du troll pendant 24 heures."
actions:
  - name: Attaques multiples
    description: "Le troll effectue deux attaques de griffe."
  - name: Griffe
    description: "Attaque au corps a corps avec une arme : +5 au toucher, allonge 1,50 m, une cible. Touche : 8 (1d10 + 3) degats tranchants."
    attaque: +5 au toucher
  - name: Morsure
    description: "Attaque au corps a corps avec une arme : +5 au toucher, allonge 1,50 m, une cible. Touche : 6 (1d6 + 3) degats perforants."
    attaque: +5 au toucher
```

## Notes de conception

**Difficulte estimee** : Rencontre difficile a mortelle pour 3 personnages de niveau 3-4.

**Ajustements par rapport au troll standard (CR 5)** :
- Points de vie reduits (52 vs 84)
- Regeneration reduite (5 vs 10)
- Une attaque de moins par tour (2 griffes vs 3 attaques)
- Degats legerement reduits

**Capacites thematiques ajoutees** :
- Nage et Amphibie pour le theme marecageux
- Camouflage des marecages pour les embuscades
- Puanteur pour le cote repugnant des marais

## Tactiques

Le troll des marais prefere tendre des embuscades depuis l'eau boueuse ou les roseaux. Il utilise son camouflage pour surprendre ses proies, puis compte sur sa regeneration pour user ses adversaires. Il fuit s'il est confronte au feu, sa terreur ancestrale.

## Indices pour les joueurs

- Odeur de pourriture dans les marais
- Traces de griffes sur les arbres
- Carcasses d'animaux a moitie devores
- Villageois mentionnant une "chose verte" dans les marais
