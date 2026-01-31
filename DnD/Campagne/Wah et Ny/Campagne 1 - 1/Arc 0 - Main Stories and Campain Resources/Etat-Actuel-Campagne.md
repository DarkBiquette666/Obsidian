---
type: campagne-status
date_updated: 2026-01-04
session_actuelle: 1
arc_actuel: "Ch1 - Puits Trépied"
tags:
  - campagne
  - status
  - tracking
---

# État Actuel de la Campagne

> **Dernière mise à jour:** Session 1 - 02/01/2026
> **Arc actuel:** Ch1 - Le Secret du Puits de Trépied
> **Niveau du personnage:** 1

## Navigation Rapide

- [[Timeline-Master.canvas|Timeline Complète (Canvas)]]
- [[Timeline/Canvas/Timeline-Ch1.canvas|Ch1 Détaillé (Canvas)]]
- [[Résumé|Résumé Complet Séance 1]]
- [[00 - Main Story Line|Histoire Principale Complète (Arc Principal - Pour Plus Tard)]]

---

## Résumé Session Précédente

**Session #:** 1
**Date:** 02/01/2026
**Joueur:** Wah
**MJ:** Ny

**Ce qui s'est passé:**

1. **Réception de la mission** - Simon reçoit une lettre d'Aldric Forteguard lui ordonnant d'investiguer le puits contaminé de Trépied
2. **Tentative avec l'hermite** - Simon apporte des présents mais l'hermite refuse catégoriquement de lui parler
3. **Le puits mystérieux** - Pataud saute dans le puits, Simon descend pour le sauver
4. **Échec critique** - Test d'Athlétisme raté (4), Simon perd sa lanterne et avale de l'eau contaminée
5. **Rencontre du Mephit** - Créature joueuse qui présente des fioles de potion violette
6. **Incident de la chaussette** - Simon met une chaussette au Mephit qui trébuche et brise la dernière fiole, puis s'enfuit frustré
7. **Sortie secrète** - 20 minutes dans le noir, Simon trouve une galerie et sort (qu'il rebouche ensuite)
8. **RÉVÉLATION** - Les fioles récupérées portent le sceau de l'hermite!

**Décisions majeures prises:**
- Descendre dans le puits à la place du maire (héroïque)
- Ne pas prendre de décision claire avec le Mephit → toutes les fioles perdues
- Reboucher la sortie secrète (prudence)
- Raconter tout à Maître Renard (confiance)

**Cliffhanger:**
L'hermite est identifié comme la source de la contamination. Que faire maintenant?

---

## Statut du Personnage

### Composition
| Joueur | Personnage | Classe/Niveau         | Statut                        |
| ------ | ---------- | --------------------- | ----------------------------- |
| Wah    | Simon      | [[Inquisiteur]] Niv.1 | Vivant (légèrement contaminé) |

### Ressources
- **Or:** 0 po (quête non terminée)
- **Objets magiques:** Aucun
- **Équipement perdu:** Lanterne (dans le puits)
- **Alliés:** Pataud (chien compagnon fidèle)
- **Monture:** Otro (cheval)

### Localisation Actuelle
**Lieu:** Village de Trépied (chez Maître Renard)
**Peut voyager vers:** Eauprofonde, forêt (hermite), exploration de la galerie

### Compagnon
**Pataud** - Chien de garde du village
- PV: 11/11
- Fidélité: Reste le chien de [[Maître Renard]]

---

## Progression de l'Histoire

### Ch1: Le Secret du Puits de Trépied
**Statut:** En cours (Session 1 complétée, 70% fait)
**Objectif:** Découvrir la source de la contamination et protéger les villageois

**Événements accomplis:**
- [x] Réception de la mission d'Aldric [[E01-Ch1-Reception-Mission]]
- [x] Voyage jusqu'au village
- [x] Tentative de parler à l'hermite (échec)
- [x] Investigation au village, rencontre de Maître Renard
- [x] Descente dans le puits [[E02-Ch1-Descente-Puits]]
- [x] Exploration de la grotte souterraine
- [x] Rencontre avec le Mephit de Vapeur [[E03-Ch1-Incident-Chaussette-Mephit]]
- [x] Sortie par la galerie secrète
- [x] Révélation: les fioles portent le sceau de l'hermite [[E04-Ch1-Revelation-Sceau-Hermite]]

**Événements restants:**
- [ ] Confronter l'hermite avec les preuves
- [ ] Laisser 24h a l'hermite pour confectionner un contre elixir pour nettoyer [[Le Puits]]
- [ ] Constater que l'hermite s'est fait enlever
- [ ] Enqueter

**Mystère actuel:**
Pourquoi l'hermite a-t-il contaminé le puits? Est-ce délibéré ou accidentel? Est t'il seulement au courant??

### Arc Principal: La Vigilance Corrompue (Aldric/Asmodée)
**Statut:** Pas encore commencé (setup en cours)
**Lien actuel:** Aldric a envoyé Simon en mission (observe à distance)

**Ce que Simon sait:**
- Aldric est le Haut-Prêtre de Heaum à Eauprofonde
- C'est son supérieur qui lui donne des missions

**Ce que Simon ne sait PAS:**
- Aldric est un Oathbreaker lié à Asmodée
- Cette mission est peut-être un test
- Aldric cherche quelqu'un qui pourrait défaire son pacte avec Asmodée

---

## Flags et Variables Critiques

### Flags Actifs
```yaml
# Ch1 - Puits de Trépied
mission_recue: true
village_trepied_visite: true
hermite_visite: true
hermite_refuse_parler: true
puits_explore: true
grotte_decouverte: true
galerie_secrete_decouverte: true
galerie_secrete_rebouchee: true
mephit_rencontre: true
mephit_enfui: true
incident_chaussette: true
fioles_toutes_perdues: true
fioles_recuperees_par_villageois: true
sceau_hermite_reconnu: true
hermite_identifie_comme_source: true

# Simon
simon_contamine_legerement: true
lanterne_perdue: true
pataud_compagnon: true

# Arc Principal (pour plus tard)
aldric_rencontre: false  # Juste sa lettre
aldric_identite_connue: false
pacte_asmodee_decouvert: false
```

### Variables Numériques
```yaml
# Progression Simon
niveau: 1
sessions_completees: 1
temps_jeu_heures: 3-4

# Relations PNJ
confiance_maitre_renard: 25  # Élevée ⭐⭐⭐
loyaute_pataud: 100  # Maximale ⭐⭐⭐⭐⭐
relation_hermite: -50  # Hostile
relation_mephit: -20  # Frustré

# Réputation
reputation_village_trepied: 20  # Positive, a aidé
reputation_eglise_heaum: 0  # Neutre, mission en cours

# Progression Ch1
progression_mystere_puits: 70  # 70% résolu

# Aldric (Background, Simon ne sait pas)
aldric_corruption: 75
aldric_espoir: 25
aldric_temps_restant_jours: 90
aldric_observe_simon: true  # À distance

# Impact
villages_sauves: 0
innocents_sauves: 0
membres_assemblee_tues: 0
membres_assemblee_convertis: 0
```

---

## Connaissances des Joueurs

### Ce qu'ils savent
- Rien concernant l'intrigue principale encore

### Ce qu'ils soupçonnent
- Rien encore

### Ce qu'ils ignorent (mais découvriront)
- Existence d'Aldric Forteguard
- L'Assemblée de l'Éveil Vigilant
- Le pacte avec Asmodée
- L'échelle réelle du complot

---

## PNJ Importants

### Rencontrés
Aucun encore

### Non Rencontrés (mais importants)

#### Aldric Forteguard
**Statut:** Observateur distant (pas conscient des PJ)
**Attitude:** Neutre
**Localisation:** Inconnue (quelque part dans la région)
**Prochaine interaction possible:** Arc 2 ou 3

**Notes MJ:**
- Corruption à 75% et montant
- Temps restant: ~3 mois
- Cherche désespérément a ce que quelqu'un découvre son pacte et l'aide à s'en libérer
- Observera les PJ s'ils deviennent notables

---

## Prochaine Session

### Session #2 - À Préparer

**Cliffhanger de la Séance 1:**
Les fioles récupérées portent le sceau de l'hermite. Il a clairement l'air impliqué dans la contamination du puits. Que faire?

**Objectifs MJ:**
1. Permettre la confrontation avec l'hermite
2. Révéler ses motivations (accident? malveillance? manipulation?)
3. Résoudre le mystère du puits
4. Purifier l'eau ou trouver solution
5. Conclusion de Ch1 avec récompense
6. Hook vers prochaine aventure?

**Préparation requise:**
- [ ] Développer l'hermite: qui est-il? Que sait t'il de la contamination du puit?
- [ ] Préparer dialogue/confrontation hermite
- [ ] Décider: combat ou résolution pacifique possible?
- [ ] Préparer méthode de purification du puits
- [ ] Prévoir récompense: 20 po + chope de bière
- [ ] Penser à un hook pour Ch2 (L'hermite va etre enlever, partir sur sa trace?)

**Pistes possibles pour Séance 2:**

1. **Confrontation avec l'hermite:**
   - Retourner avec les preuves (fioles)
   - Exiger des explications
   - Options: combat, persuasion, intimidation, négociation
   - Découvrir qu'il ne sait rien

2. **Purification du puits:**
   - Récupérer toutes les fioles restantes
   - Attendre 24h que l'hermite prépare un elixir de purification
   - Participer au quete secondaire du village en attendant

3. **Exploration de la galerie:**
   - Simon peut rouvrir le passage qu'il a rebouché
   - Où mène-t-il vraiment?
   - Lié à l'hermite?

4. **Le Mephit:**
   - Pourrait revenir?
   - Était-il serviteur de l'hermite ou victime?

5. **Effets de la contamination:**
   - Des phénomènres étrange arrive dans le [[Trépied]] (quetes secondaires)

6. Enlèvement de l'hermite 
	- Investiguer et go vers act2 

**Événements prévus:**
- Confrontation hermite
- Résolution partiel du mystère
- Enlèvement de l'hermite 
- Transition vers Ch2

---

## Notes et Rappels MJ

### Ch1 - Points Importants
- L'hermite n'est probablement pas "méchant" → accident ou manipulation plus probable
- Le Mephit était innocent, jouait avec les fioles sans comprendre. Il a été crée secretement à la demande d'Aldric pour semet le chaos dans le village pour qu'Aldric puisse envoyer le joueur et le tester.
- Simon a montré des traits qu'Aldric recherche: courage, protection des innocents, sacrifice
- Ne pas forcer le combat, laisser Simon choisir son approche

### Aldric en Background
- Aldric observe à distance (peut-être par magie ou rapports)
- Il évalue Simon: est-il digne? pur? fort?
- N'intervient PAS encore
- Cette mission simple est un test initial

### Prochains Chapitres
- Ch2: Prochaine mission d'Aldric (possiblement plus dangereuse) -> le mettre sur la piste de l'Assemblée
- Progressivement augmenter difficulté et enjeux
- Révéler lentement la vraie nature d'Aldric (Arcs 3-4-5)

### Foreshadowing à intégrer
- Symbole de l'Assemblée (œil vigilant) vu en passant
- Mention d'un "protecteur" ou "gardien"
- Comportements suspects mais pas évidents
- Créer des questions, pas donner de réponses

### Ajustements Session par Session
**Difficulté:** Ajuster selon la performance du groupe
**Rythme:** Accélérer si joueurs s'ennuient, ralentir si dépassés
**Ton:** Observer ce qui engage le plus la table

---

## Chemins Narratifs Encore Ouverts

**Tous les chemins sont ouverts!**

La campagne n'a pas encore commencé, donc toutes les possibilités existent:
- 8 endings différents possibles
- Multiple chemins à travers chaque arc
- Nombreux choix moraux à venir
- Aldric peut être sauvé, tué, ou devenir allié

**La liberté totale règne!**

---

## Statistiques de Campagne

**Sessions jouées:** 1
**Heures de jeu total:** 0h
**Combats:** 0
**Morts de PJ:** 0
**Réussites critiques mémorables:** 0
**Échecs critiques mémorables:** 0
**Moments épiques:** 0
**Twists révélés:** 0 / 15+


