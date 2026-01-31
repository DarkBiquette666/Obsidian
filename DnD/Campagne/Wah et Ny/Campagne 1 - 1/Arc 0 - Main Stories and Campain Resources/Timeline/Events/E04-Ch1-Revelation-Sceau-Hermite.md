---
type: event
arc: "Ch1 - Puits Trépied"
chronologie: accompli
status: accompli
date_jeu: Séance 1
session: 1
dependencies:
  - "[[E03-Ch1-Incident-Chaussette-Mephit]]"
  - "[[E04-Ch1-Sortie-Galerie-Secrete]]"
triggers:
  - "[[D04-Ch1-Confronter-Hermite]]"
tags:
  - timeline
  - event
  - ch1
  - revelation
  - hermite
  - indice-majeur
---

## Evenement: La Révélation du Sceau de l'Hermite

### Prerequis

- Simon est revenu au village
- A raconté son aventure à Maître Renard
- Les villageois ont récupéré des fioles du puits

### Description

De retour au [[Trépied|village]], Simon explique en détail toute son aventure à [[Maître Renard]]. Le maire, comprenant la gravité de la situation, envoie immédiatement des villageois récupérer les fioles restantes dans le puits.

**La Découverte Majeure:**

En examinant les fioles récupérées de l'eau du puits, Maître Renard reconnaît le **symbole gravé dessus**.

**C'est le sceau de l'hermite de la forêt.**

**Implications:**
- L'hermite est impliqué dans la contamination du puits
- L'hermite a créé ces potions alchimiques
- L'hermite a refusé de parler probablement par culpabilité
- Les fioles sont d'origine alchimique, pas naturelle

**Questions ouvertes:**
- Pourquoi l'hermite a-t-il créé ces potions?
- Quel était l'objectif de contaminer le puits?
- Le Mephit était-il son serviteur ou une victime?
- L'hermite est-il dangereux?

### Personnages Impliques

- [[Simon-Fiche-Personnage|Simon]] - Rapporte l'aventure
- [[Maître Renard]] - Reconnaît le sceau, envoie récupérer les fioles
- L'Hermite - Identifié comme source (absent)
- Villageois - Récupèrent les fioles

### Lieux

- [[Trépied]] - Lieu de la révélation
- [[Le Puits]] - Où les fioles sont récupérées
- Forêt - Où vit l'hermite

### Choix Possibles

**Prochaine décision:** [[D04-Ch1-Confronter-Hermite]]

**Options:**
1. Retourner confronter l'hermite immédiatement avec les preuves
2. Informer l'Église de Heaum (Aldric)
3. Enquêter davantage avant d'agir
4. Attendre la Séance 2

### Consequences Directes

**Immédiates:**
- Le mystère du puits est partiellement résolu
- Source identifiée: l'hermite
- Fioles récupérées comme preuves
- Nouveau suspect principal

**Relations:**
- Confiance de Maître Renard envers Simon augmente (il a résolu le mystère)
- Villageois reconnaissants
- L'hermite devient suspect #1

### Impact a Long Terme

- Court terme: Prochaine session = confrontation avec l'hermite probable
- Moyen terme: Découverte des vraies motivations de l'hermite
- Long terme: Ce mystère local pourrait-il avoir des liens avec quelque chose de plus grand?

### Etat du Monde Apres

**Flags modifiés:**
```yaml
flags:
  hermite_identifie_comme_source: true
  sceau_hermite_reconnu: true
  fioles_recuperees_par_villageois: true
  mystere_partiellement_resolu: true
  preuves_obtenues: true
```

**Variables modifiées:**
```yaml
variables:
  confiance_maitre_renard: +15
  reputation_village: +20
  fioles_recuperees: 3  # Celles dans l'eau
  suspicion_hermite: 100
```

### Notes MJ

**RÉVÉLATION MAJEURE de la Séance 1!**

Cette découverte transforme totalement la quête:
- Ce n'était pas un phénomène naturel
- Ce n'était pas juste le Mephit qui jouait
- C'est délibéré, créé par quelqu'un

**Le refus initial de l'hermite** prend maintenant tout son sens:
- Il savait ce que Simon allait découvrir
- Il a refusé de parler par culpabilité
- Son hostilité était de la honte

**Setup pour Séance 2:**
Parfait cliffhanger! Les joueurs veulent maintenant:
1. Confronter l'hermite
2. Comprendre ses motivations
3. Découvrir le lien avec le Mephit

**Questions narratives fascinantes:**
- L'hermite est-il méchant ou a-t-il eu un accident?
- Pourquoi contaminer le puits de son propre village?
- Le Mephit était-il contrôlé ou libre?
- Y a-t-il un lien avec quelque chose de plus grand? (Aldric?)

### Ressources

- Voir [[Résumé#Le Retour et la Révélation]]
- Voir [[Résumé#Indices Découverts]]
- Lier à [[00-Synopsis#Conclusion]]
