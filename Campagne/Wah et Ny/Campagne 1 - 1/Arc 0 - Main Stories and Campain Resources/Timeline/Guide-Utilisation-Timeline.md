# Guide: Système de Timeline à Embranchements

## Vue d Ensemble

Ce système vous permet de gérer une histoire complexe avec de multiples embranchements narratifs, comme dans Baldur s Gate.

## Structure des Fichiers

### Dossiers Principaux

```
Timeline/
├── Events/          # Événements individuels
├── Decisions/       # Points de choix critiques
├── Outcomes/        # Résultats possibles
├── World-States/    # États du monde
└── Canvas/          # Visualisations
```

### Fichiers Clés

1. **Etat-Actuel-Campagne** - Tableau de bord principal
2. **Timeline-Master.canvas** - Vue macro complète
3. **Timeline-Arc1.canvas** - Vue détaillée Arc 1

## Comment Utiliser

### Avant Chaque Session

1. Ouvrir Etat-Actuel-Campagne
2. Consulter le Canvas de l arc actuel
3. Relire les Events à venir

### Pendant la Session

1. Noter les décisions importantes
2. Tracker les flags modifiés
3. Improviser et adapter

### Après Chaque Session (CRUCIAL!)

1. METTRE À JOUR Etat-Actuel-Campagne
2. Créer un nouveau World-State si nécessaire
3. Créer nouveaux Events/Outcomes si chemins inattendus

## Travailler avec les Embranchements

### Point de Décision

1. Ouvrir le fichier Decision
2. Présenter les choix organiquement
3. Noter quel choix est pris
4. Appliquer les conséquences

### Si Joueurs Font Quelque Chose d Inattendu

C est NORMAL et BON!

1. Improviser la réponse immédiate
2. Après session: créer nouveau Outcome
3. Le lier aux Events existants

**Le système est flexible, pas rigide!**

## Utiliser les Canvas

### Timeline-Master.canvas

- PASSÉ (rouge) = backstory Aldric
- PRÉSENT (bleu) = 5 arcs
- FUTURS (vert) = endings possibles

### Timeline-Arc1.canvas

- Événements = bleu
- Décisions = jaune
- Outcomes = vert
- Sidequests = orange

Suivre les flèches pour voir connexions causales.

## Flags et Variables

### Flags (true/false)
- aldric_rencontre
- pacte_decouvert
- village_sauve

### Variables (nombres)
- reputation: -100 à +100
- corruption: 0 à 100
- niveau: 1-20

Trouvables dans Etat-Actuel-Campagne.

## Best Practices

### DO
- Mettre à jour après CHAQUE session
- Créer nouveaux Outcomes quand surpris
- Utiliser canvas pour visualiser
- Tracker flags consciencieusement

### DON T
- Forcer joueurs sur un path
- Oublier de noter décisions
- Avoir peur de modifier système

### REMEMBER

**Le système sert l histoire, pas l inverse!**

## Checklist Après Session

- [ ] Mettre à jour résumé session
- [ ] Noter décisions majeures
- [ ] Modifier flags actifs
- [ ] Modifier variables
- [ ] Cocher événements accomplis
- [ ] Créer nouveaux Outcomes si besoin
- [ ] Noter préparation prochaine session

## Prochaines Étapes

1. Familiarisez-vous avec Etat-Actuel-Campagne
2. Ouvrez Timeline-Master.canvas
3. Explorez Timeline-Arc1.canvas
4. Préparez Session 1
5. Jouez et amusez-vous!

**Bonne aventure!**
