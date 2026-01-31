# D&D Content Renderer

Plugin Obsidian pour afficher des fiches D&D 5e (monstres, personnages, classes, races) avec le style visuel d'aidedd.org.

## Fonctionnalites

- Rendu de fiches avec style aidedd.org (rouge fonce, orange, creme)
- 4 types de blocs de code YAML supportes
- Wizard de creation de personnage en 5 etapes
- Import de stat blocks Markdown depuis aidedd.org
- Architecture SOLID, extensible

## Blocs de code supportes

| Type | Description |
|------|-------------|
| `dnd-monstre` | Fiches de creatures/monstres |
| `dnd-personnage` | Fiches de personnages (PJ/PNJ) |
| `dnd-classe` | Fiches de classes |
| `dnd-race` | Fiches de races |

## Commandes

- **Import Markdown Stat Block (Homebrew)** - Importe un stat block depuis aidedd.org/dnd-statblock
- **Creer un nouveau personnage** - Wizard en 5 etapes

## Installation

1. Copiez le dossier `obsidian-dnd-content` dans `.obsidian/plugins/`
2. Activez le plugin dans Parametres > Plugins communautaires
3. Rechargez Obsidian

## Utilisation

### Monstre

```yaml
```dnd-monstre
name: Gobelin
type: Humanoide
taille: P
alignement: neutre mauvais
classe_armure: 15 (armure de cuir, bouclier)
points_de_vie: 7 (2d6)
vitesse: 9 m
for: 8
dex: 14
con: 10
int: 10
sag: 8
cha: 8
competences: Discretion +6
sens: vision dans le noir 18 m
langues: commun, gobelin
facteur_puissance: 1/4
traits:
  - name: Fuite agile
    description: Le gobelin peut se desengager ou se cacher par une action bonus.
actions:
  - name: Cimeterre
    attaque: Attaque d'arme au corps a corps
    description: +4 au toucher, 1d6+2 degats tranchants.
`` `
```

### Personnage

```yaml
```dnd-personnage
name: Thorin
race: Nain (Nain des montagnes)
classe: Guerrier
niveau: 5
historique: Soldat
alignement: Loyal Bon
for: 16
dex: 12
con: 16
int: 10
sag: 12
cha: 8
ca: 18
pv_max: 52
pv_actuels: 52
vitesse: 7.5 m
bonus_maitrise: 3
sauvegardes:
  - Force
  - Constitution
competences:
  - name: Athletisme
    maitrise: true
  - name: Intimidation
    maitrise: true
langues:
  - Commun
  - Nain
armures:
  - armures lourdes
armes:
  - armes de guerre
equipement:
  - name: Hache d'armes
    quantite: 1
argent:
  po: 50
traits_personnalite: Je suis toujours poli et respectueux.
ideaux: La protection des innocents est mon devoir.
liens: Ma famille compte plus que tout.
defauts: Je fais confiance trop facilement.
`` `
```

### Classe

```yaml
```dnd-classe
name: Guerrier
des_de_vie: d10
pv_niveau_1: 10 + Con
pv_niveaux_suivants: 1d10 (ou 6) + Con
maitrises:
  armures:
    - armures legeres
    - armures lourdes
    - boucliers
  armes:
    - armes courantes
    - armes de guerre
  sauvegardes:
    - Force
    - Constitution
  competences:
    choix: 2
    liste:
      - Athletisme
      - Intimidation
      - Perception
      - Survie
capacites:
  - name: Second souffle
    description: Recuperez 1d10 + niveau PV par une action bonus.
archetypes:
  - name: Champion
  - name: Maitre de guerre
`` `
```

### Race

```yaml
```dnd-race
name: Elfe
taille: M
vitesse: 9 m
augmentations:
  dex: 2
langues:
  - Commun
  - Elfique
traits:
  - name: Vision dans le noir
    description: Vous pouvez voir a 18 metres dans une lumiere faible.
  - name: Ascendance feerique
    description: Avantage contre les effets de charme.
sous_races:
  - name: Haut-elfe
    augmentations:
      int: 1
    traits:
      - name: Tour de magie
        description: Vous connaissez un tour de magie du magicien.
`` `
```

## Architecture

Le plugin utilise une architecture SOLID:

```
DnDContentPlugin          # Orchestration
├── BlockProcessor        # Factory pattern
│   ├── MonsterRenderer   # extends BaseRenderer
│   ├── CharacterRenderer
│   ├── ClasseRenderer
│   └── RaceRenderer
├── CharacterWizardModal  # Wizard 5 etapes
│   └── CharacterFileGenerator
├── ImportStatBlockModal
│   ├── MarkdownParser
│   ├── YamlGenerator
│   └── FileGenerator
└── DnDUtils              # Fonctions utilitaires
```

## Style

Palette de couleurs aidedd.org:
- Rouge fonce: #6D0000
- Rouge vif: #B80000
- Orange: #e69a28
- Creme: #fdf1dc

## Changelog

### v4.0.0
- Architecture SOLID complete
- Renderer pour les classes (dnd-classe)
- Renderer pour les races (dnd-race)
- Wizard de creation de personnage

### v3.0.0
- Renderer pour les personnages (dnd-personnage)
- Support equipement, incantation, roleplay

### v2.0.0
- Import de stat blocks Markdown

### v1.0.0
- Renderer de base pour les monstres

## Licence

MIT License - voir [LICENSE](LICENSE)

## Credits

- Style base sur aidedd.org
- Donnees D&D 5e de Wizards of the Coast
