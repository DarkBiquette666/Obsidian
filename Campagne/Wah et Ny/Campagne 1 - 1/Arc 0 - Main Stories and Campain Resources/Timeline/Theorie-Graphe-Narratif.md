# Theorie: Construire un Graphe Narratif avec Outcomes Multiples

## Inspiration: Baldur's Gate et RPG a Choix

Les jeux comme Baldur's Gate 3, The Witcher, Mass Effect utilisent des **graphes narratifs** pour gerer les histoires a embranchements.

## Concepts Fondamentaux

### 1. Nodes (Noeuds)

Chaque point dans l histoire:
- **Event Node** = Evenement qui se produit
- **Decision Node** = Point de choix pour joueurs
- **State Node** = Etat du monde a un moment donne

### 2. Edges (Liens)

Connexions entre nodes:
- **Causal Edge** = X cause Y
- **Conditional Edge** = Si condition, alors Y
- **Temporal Edge** = X puis Y dans le temps

### 3. Variables d Etat

Tracking de l etat du monde:
- **Flags** = Boolean (true/false)
- **Variables** = Nombres (reputation, temps, etc.)
- **Lists** = Collections (alles, ennemis, items)

## Architecture Typique

```
EVENT → DECISION → OUTCOME → NEW STATE → NEW EVENTS
```

### Exemple Concret

```
[Village attaque]
      ↓
[Sauver village ou poursuivre ennemi?]
      ├─→ Sauver
      │     ↓
      │   [Village sauve, ennemi s echappe]
      │     ↓
      │   flag: village_saved = true
      │   flag: enemy_escaped = true
      │     ↓
      │   Deverrouille: [Quete gratitude villageois]
      │   Annule: [Quete capturer ennemi]
      │
      └─→ Poursuivre
            ↓
          [Ennemi capture, village detruit]
            ↓
          flag: village_saved = false
          flag: enemy_captured = true
            ↓
          Deverrouille: [Quete vengeance]
          Annule: [Quete gratitude villageois]
```

## Strategies de Design

### A. Le Chemin Critique

**Definition:** La ligne narrative principale qui doit toujours etre possible

**Dans votre campagne:**
Pacte → Arc 1 → Arc 2 → Arc 3 → Arc 4 → Arc 5 → Fin

**Regle:** Meme si PJ font choix terribles, campagne continue
**Comment:** Aldric ne peut pas mourir avant Arc 5

### B. Les Branches Optionnelles

**Definition:** Sidequests et contenus qui peuvent etre rates

**Dans votre campagne:**
- Puits Maudit
- Fermier Disparu
- Autres sidequests

**Regle:** Donnent bonus mais pas essentielles
**Comment:** Recompenses: XP, items, info, alles

### C. Les Points de Convergence

**Definition:** Moments ou toutes les branches reviennent ensemble

**Dans votre campagne:**
- Fin de chaque Arc converge vers debut Arc suivant
- Meme si approches differentes, tous arrivent a Arc 5

**Regle:** Evite explosion combinatoire
**Comment:** "Tous les chemins menent a Rome"

### D. Les Variables Cachees

**Definition:** Valeurs que joueurs ne voient pas mais qui affectent l histoire

**Dans votre campagne:**
- corruption_aldric
- jours_avant_expiration
- aldric_confiance (cache)

**Regle:** Cree emergence et surprise
**Comment:** Joueurs voient resultats sans voir mecanique

## Patterns Narratifs Communs

### Pattern 1: Le Dilemme Moral

```
Situation ethiquement ambigue
    ├─→ Choix "bon" → Consequences negatives inattendues
    └─→ Choix "mauvais" → Consequences positives inattendues
```

**Exemple campagne:**
Tuer Aldric (bon?) → Asmodee libere ame, pire menace
Allier Aldric (mauvais?) → Meilleure chance arreter Asmodee

### Pattern 2: L Information Cachee

```
Decision avec info incomplete
    ├─→ Choix A sans savoir X → Regret plus tard
    └─→ Choix B sans savoir Y → Surprise plus tard

Plus tard: Revelation de X ou Y
```

**Exemple campagne:**
Confronter Aldric sans savoir qu il etait paladin de Heaum
vs
Confronter apres avoir decouvert son passe

### Pattern 3: Les Consequences Retardees

```
Choix en Arc 1 → Pas d effet visible
...
...
Arc 4 → Consequence majeure apparait
```

**Exemple:**
Epargner membre Assemblee Arc 1
→ Il revele secret critique Arc 4

### Pattern 4: Les Effets Cumulatifs

```
Petit choix 1 + Petit choix 2 + Petit choix 3
→ Threshold atteint
→ Evenement majeur se declenche
```

**Exemple:**
Decisions mauvaises s accumulent
→ karma_groupe < -5
→ PNJ bon refuse d aider
→ Quete principale plus difficile

## Gestion de la Complexite

### Probleme: Explosion Combinatoire

Si chaque decision a 3 options:
- Arc 1: 3 branches
- Arc 2: 3 × 3 = 9 branches
- Arc 3: 9 × 3 = 27 branches
- Arc 4: 27 × 3 = 81 branches
**= INGERABLE!**

### Solution 1: Convergence Forcee

Apres chaque arc, branches convergent:

```
Arc 1: [A] [B] [C]
       ↓   ↓   ↓
       Convergence
            ↓
Arc 2: [D] [E] [F]
       ↓   ↓   ↓
       Convergence
```

### Solution 2: Variables au Lieu de Branches

Au lieu de creer branches separees:

```
Choix A → flag_x = true, var_y = +5
Choix B → flag_x = false, var_y = -3

Arc suit meme chemin mais:
- Si flag_x: dialogue different
- Si var_y > 0: PNJ amical
```

### Solution 3: Branches qui Meurent

Certaines branches menent a impasses:

```
[Choix Stupide]
    ↓
[Consequence Terrible]
    ↓
[Fin Prematuree / TPK]
```

C est OK! Choix ont consequences.

## Implementation dans Obsidian

### Niveau Macro (Canvas Master)

Vue 10,000 pieds:
- Arcs principaux
- Fins possibles
- Pas de details

### Niveau Meso (Canvas par Arc)

Vue 1,000 pieds:
- Evenements de l arc
- Decisions principales
- Outcomes majeurs

### Niveau Micro (Notes individuelles)

Vue 100 pieds:
- Details exacts
- Tous les embranchements
- Variables precises

## Exemple: Baldur's Gate 3

### Structure Reelle BG3

**Acte 1:**
- Chemin critique: Trouver guerisseuse
- Branches: 3-4 zones optionnelles
- Convergence: Tous arrivent a Acte 2

**Acte 2:**
- Chemin critique: Affronter Ketheric
- Branches: Alliances possibles
- Variables: Qui vit, qui meurt
- Convergence: Ketheric tombe, Acte 3

**Acte 3:**
- Chemin critique: Cerveau Elder
- Branches: Multiples alliances
- Fins: ~17 fins differentes (mais structure similaire)

### Lecon BG3

- **~6-8 decisions vraiment critiques** dans tout le jeu
- **Centaines de petites decisions** qui changent dialogues
- **Convergence forte** entre actes
- **Variables cachees** (approval ratings) affectent options

## Application a Votre Campagne

### Decisions Critiques (6 max)

1. **Arc 1 - Fin:** Confronter/Negocier/Fuir Aldric
2. **Arc 2 - Milieu:** Infiltrer ou Detruire Assemblee
3. **Arc 3:** Allier avec Aldric ou pas
4. **Arc 4:** Liberer Asmodee ou pas
5. **Arc 5 - Finale:** Sort final d Aldric
6. **Arc 5 - Finale:** Que faire du pacte

### Variables Principales (8-10 max)

```yaml
# Relations
aldric_confiance: -10 a +10
reputation_eglise: -20 a +20

# Progression
corruption_aldric: 0-100
jours_restants: 365→0

# Moral
karma_groupe: -20 a +20
decisions_mauvaises: compteur

# Ressources
allies_obtenus: liste
info_critique: 0-100%
```

### Points de Convergence (5)

- Fin Arc 1 → Debut Arc 2
- Fin Arc 2 → Debut Arc 3
- Fin Arc 3 → Debut Arc 4
- Fin Arc 4 → Debut Arc 5
- Arc 5 → Une des 4 fins

## Checklist Design

Pour chaque decision importante:

- [ ] Definir 2-4 options claires
- [ ] Chaque option a avantages ET inconvenients
- [ ] Consequences a court terme (immediate)
- [ ] Consequences a moyen terme (cet arc)
- [ ] Consequences a long terme (arcs suivants)
- [ ] Quels flags/variables changent
- [ ] Quels evenements deverrouilles
- [ ] Quels evenements annules
- [ ] Comment ca affecte la fin

## Conseils Finaux

### DO:
- Creez convergence entre arcs
- Utilisez variables au lieu de branches infinies
- ~6 decisions vraiment critiques
- Centaines de petites variations (dialogues, etc.)
- Consequences retardees pour surprises

### DONT:
- Creer branches qui ne convergent jamais
- Donner 10 options par decision (trop!)
- Creer option "parfaite" sans inconvenients
- Faire exploser nombre de variables
- Tout planifier a l avance (restez flexible)

## Ressources

- Voir: Timeline-Master.canvas
- Voir: Timeline-Arc1-Detail.canvas
- Voir: Etat-Actuel-Campagne.md

Votre graphe narratif est maintenant pret!
