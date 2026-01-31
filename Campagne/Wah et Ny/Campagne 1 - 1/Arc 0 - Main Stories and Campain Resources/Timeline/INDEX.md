# INDEX - Systeme de Timeline Narrative

> Point d entree central pour le systeme de timeline avec embranchements multiples

---

## DEMARRAGE RAPIDE

### 1. Comprendre le Systeme
Lisez: [[README]]

### 2. Voir la Vue d Ensemble
Ouvrez: [[Timeline-Master.canvas]]

### 3. Preparer Votre Arc Actuel
Ouvrez: [[Canvas/Timeline-Arc1-Detail.canvas]]

### 4. Tracker Votre Campagne
Utilisez: [[Etat-Actuel-Campagne]]

---

## STRUCTURE COMPLETE

### Dossiers

```
Timeline/
├── Canvas/
│   ├── Timeline-Master.canvas
│   └── Timeline-Arc1-Detail.canvas
├── Events/
│   ├── E00-Pacte-Asmodee.md
│   └── E01-Arc1-Arrivee-Trepied.md
├── Decisions/
│   └── Decision-D01-Confrontation-Aldric-Arc1.md
├── Outcomes/
│   (vide - a remplir selon decisions PJ)
├── World-States/
│   (vide - a remplir apres sessions)
├── Etat-Actuel-Campagne.md
├── INDEX.md (ce fichier)
├── README.md
└── Theorie-Graphe-Narratif.md
```

### Templates (dans /Templates)

- Timeline-Event.md
- Timeline-Decision.md
- Timeline-Outcome.md
- Timeline-World-State.md

---

## FICHIERS PRINCIPAUX

### Documentation

| Fichier | Description |
|---------|-------------|
| [[README]] | Guide rapide utilisation |
| [[Theorie-Graphe-Narratif]] | Concepts design narratif |
| INDEX (ce fichier) | Point entree central |

### Canvas

| Fichier | Niveau | Description |
|---------|--------|-------------|
| [[Timeline-Master.canvas]] | Macro | Vue complete campagne |
| [[Canvas/Timeline-Arc1-Detail.canvas]] | Micro | Detail Arc 1 |

### Tracking

| Fichier | Description |
|---------|-------------|
| [[Etat-Actuel-Campagne]] | Etat actuel du monde, flags, variables |

### Exemples Crees

| Type | Fichier |
|------|---------|
| Event | [[E00-Pacte-Asmodee]] |
| Event | [[E01-Arc1-Arrivee-Trepied]] |
| Decision | [[Decisions/Decision-D01-Confrontation-Aldric-Arc1]] |

---

## WORKFLOWS

### Preparation Session

1. Ouvrir [[Etat-Actuel-Campagne]]
2. Consulter flags et variables actuels
3. Identifier evenements possibles
4. Ouvrir canvas de l arc actuel
5. Preparer notes Event si necessaire

### Pendant Session

- Noter decisions PJ
- Tracker interactions importantes
- Marquer flags actives/desactives

### Apres Session

1. Mettre a jour [[Etat-Actuel-Campagne]]
2. Creer notes Outcome pour decisions prises
3. Creer notes World-State si changement majeur
4. Mettre a jour canvas si branches inattendues

---

## PROCHAINES ETAPES

### Pour Commencer

- [ ] Lire README
- [ ] Consulter Timeline-Master.canvas
- [ ] Personnaliser Etat-Actuel-Campagne
- [ ] Creer evenements manquants pour Arc 1

### Pour Chaque Arc

- [ ] Creer canvas Detail-ArcX
- [ ] Creer 5-10 notes Event
- [ ] Identifier 2-3 decisions critiques
- [ ] Creer notes Decision
- [ ] Definir outcomes possibles

### Maintenance Continue

- [ ] Mettre a jour Etat-Actuel apres chaque session
- [ ] Creer Outcomes selon choix PJ
- [ ] Ajuster canvas selon progression
- [ ] Documenter branches prises

---

## AIDE RAPIDE

### Creer un Evenement

1. Copier template: [[Timeline-Event]]
2. Remplir sections
3. Sauver dans Events/
4. Ajouter au canvas si important

### Creer une Decision

1. Copier template: [[Timeline-Decision]]
2. Definir 2-4 options
3. Lier aux outcomes possibles
4. Sauver dans Decisions/
5. Ajouter au canvas

### Creer un Outcome

1. Copier template: [[Timeline-Outcome]]
2. Decrire consequences
3. Lister flags/variables modifies
4. Lister evenements deverrouilles/annules
5. Sauver dans Outcomes/

### Mettre a Jour Etat

1. Ouvrir [[Etat-Actuel-Campagne]]
2. Section Flags: modifier true/false
3. Section Variables: ajuster nombres
4. Section Notes Session: resumer
5. Section To Track: preparer prochaine

---

## QUESTIONS FREQUENTES

### Dois-je tout creer a l avance?

NON! Creez arc par arc, session par session.

### Combien de decisions par arc?

2-3 decisions vraiment critiques suffisent.

### Que faire si PJ font choix imprevu?

Creez note Outcome rapidement, ajustez canvas, continuez!

### Comment gerer temps limite (pacte)?

Variable jours_avant_expiration dans Etat-Actuel.
Decrementez apres chaque jour en jeu.

### Les joueurs peuvent voir ces notes?

- OUI: Canvas des arcs termines (apres)
- OUI: Leurs propres choix et consequences
- NON: Arcs futurs, notes MJ secretes, branches non prises

---

## LIENS RAPIDES

### Externe
- [[00 - Main Story Line]] - Histoire complete originale
- [[Side Story -]] - Histoires secondaires

### Templates
- [[Timeline-Event]]
- [[Timeline-Decision]]
- [[Timeline-Outcome]]
- [[Timeline-World-State]]

### Tracking
- [[Etat-Actuel-Campagne]] - NOTE PRINCIPALE

---

Derniere mise a jour: 2026-01-04
