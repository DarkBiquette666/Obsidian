---
type: event
arc: "Ch1 - Puits Trépied"
chronologie: accompli
status: accompli
date_jeu: Séance 1
session: 1
dependencies:
  - "[[E02-Ch1-Descente-Puits]]"
triggers:
  - "[[E04-Ch1-Sortie-Galerie-Secrete]]"
  - "[[O01-Ch1-Toutes-Fioles-Deversees]]"
tags:
  - timeline
  - event
  - ch1
  - mephit
  - moment-memorable
  - humour
---

## Evenement: L'Incident de la Chaussette et du Mephit

### Prerequis

- Simon est dans la grotte, dans le noir
- A rejoint Pataud sur la rive
- Le Mephit de Vapeur est présent

### Description

Dans la pénombre de la grotte, Simon fait la rencontre du **[[Mephit de Vapeur]]**. Il adopte une approche amicale avec la créature.

**La Présentation des Fioles:**
Le Mephit présente des fioles de potion violette à Simon. Face à l'indécision de Simon sur quoi faire avec ces fioles, le Mephit déverse **trois fioles** dans l'eau du puits.

**L'Incident de la Chaussette:**
Voulant jouer avec le Mephit, Simon lui enfile une **chaussette sur le pied**.

Le Mephit, désorienté comme un chat à qui on met des vêtements, perd complètement l'équilibre. Il trébuche et tombe sur la **dernière fiole restante**, la brisant accidentellement.

**Réaction du Mephit:**
Extrêmement frustré par ce qui vient de se passer, le Mephit s'échappe précipitamment et disparaît dans les profondeurs de la grotte.

**Résultat final:**
- 3 fioles déversées volontairement par le Mephit
- 1 fiole brisée accidentellement (incident chaussette)
- **Toutes les fioles perdues**
- Simon ne prend aucune fiole avec lui

### Personnages Impliques

- [[Simon-Fiche-Personnage|Simon]] - Approche ludique mais indécision
- [[Mephit de Vapeur]] - Créature joueuse mais frustrée
- [[Pataud]] - Regarde la scene silencieux

### Lieux

- [[La Grotte]] - Rive sombre de la caverne souterraine

### Choix Possibles

**Décision critique:** [[D03-Ch1-Que-Faire-Fioles]]

**Options disponibles:**
1. Prendre les fioles (non choisie)
2. Détruire les fioles (non choisie)
3. Négocier avec le Mephit (tentée mais indécision)
4. Ne rien faire de clair → **CHOIX PAR DÉFAUT**

**Conséquence de l'indécision:**
Le Mephit prend l'initiative et déverse les fioles lui-même

### Consequences Directes

**Immédiates:**
- Toutes les fioles perdues (déversées ou brisées)
- Mephit s'enfuit, frustré
- Plus de preuves physiques dans la grotte
- Simon reste seul avec Pataud dans le noir

**Narratives:**
- Moment comique mémorable (chaussette)
- Démonstration que l'indécision a des conséquences
- Fin de la menace du Mephit (parti)

### Impact a Long Terme

- Court terme: Pas de fioles à rapporter comme preuve
- Moyen terme: Les villageois devront fouiller le puits pour récupérer les fioles déversées
- Long terme: Le Mephit pourrait revenir? Ou rester caché?

### Etat du Monde Apres

**Flags modifiés:**
```yaml
flags:
  mephit_rencontre: true
  mephit_enfui: true
  fioles_toutes_perdues: true
  incident_chaussette: true
  negociation_mephit_echec: true
```

**Variables modifiées:**
```yaml
variables:
  fioles_en_possession: 0
  fioles_dans_eau_puits: 3
  fioles_brisees: 1
  relation_mephit: -20  # Frustré
```

### Notes MJ

**Moment le plus drôle de la session!**

L'incident de la chaussette est devenu LE moment mémorable. Le Mephit désorienté comme un chat est une image hilarante.

**Leçon narrative:**
L'indécision a des conséquences. Simon n'a pas pris de décision claire, donc le Mephit a agi de son propre chef.

**Improvisation:**
Le joueur a montré une belle créativité avec la chaussette. Cet acte ludique a créé une conséquence imprévue (fiole brisée).

**Nature du Mephit:**
Confirmée comme créature joueuse et innocente, pas vraiment méchante. Il manipulait les fioles sans comprendre les conséquences.

**Impact futur:**
Bien que toutes les fioles soient perdues pour Simon, certaines peuvent être récupérées du puits par les villageois plus tard.

### Ressources

- Voir [[Résumé#La Rencontre avec le Mephit]]
- Voir [[Résumé#L'Incident de la Chaussette]]
- Voir [[Mephit de Vapeur]]
