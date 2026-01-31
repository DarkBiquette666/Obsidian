---
aliases:
  - Liche
tags:
  - monstre
  - bestiaire
type: Mort-vivant
facteur_puissance: 21 (33000 PX)
---

# Liche

```dnd-monstre
name: Liche
type: Mort-vivant
taille: Moyen
alignement: tout alignement mauvais
ca: 17 (armure naturelle)
pv: 135 (18d8 + 54)
vitesse: 9 m
for: 11
dex: 16
con: 16
int: 20
sag: 14
cha: 16
sauvegardes: Con +10, Int +12, Sag +9
sens: vision véritable 36 m, Perception passive 19
langues: "commun et jusqu'à cinq autres langues"
facteur_puissance: 21 (33000 PX)
immunites_etats: charmé, épuisement, effrayé, paralysé, empoisonné
source: Monster Manual (SRD)
compétences:
  - Arcanes +19
  - Histoire +12
  - Intuition +9
  - Perception +9
immunites:
  - poison ; contondant
  - "perforant et tranchant d'attaques non magiques"
résistances:
  - froid
  - foudre
  - nécrotique
traits:
  - name: Résistance légendaire (3/jour)
    description: Si la liche échoue à un jet de sauvegarde, elle peut décider de transformer cet échec en réussite.
  - name: Reconstitution
    description: Si elle a un phylactère, une liche détruite récupère un nouveau corps au bout de 1d10 jours, regagnant ainsi tous ses points de vie et redevenant active. Le nouveau corps apparaît à 1,50 mètre autour du phylactère.
  - name: Incantation
    description: "La liche est un lanceur de sorts de niveau 18. Sa caractéristique d'incantation est l'Intelligence (jet de sauvegarde contre ses sorts DD 20, +12 au toucher pour les attaques avec un sort). La liche a préparé les sorts de magicien suivants :"
  - name: Résistance au renvoi
    description: La liche a un avantage aux jets de sauvegarde pour résister aux effets de renvoi des morts-vivants.
actions:
  - name: Contact paralysant
    description: "Attaque au corps à corps avec un sort : +12 au toucher, allonge 1,50 m, une créature. Touché : 10 (3d6) dégâts de froid. La cible doit réussir un jet de sauvegarde de Constitution DD 18 ou être paralysée pendant 1 minute. La cible peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à cet effet de paralysie qui l'affecte si elle le réussit."
    attaque: +12 au toucher
legendaires:
  - name: Sort mineur
    description: La liche lance un sort mineur.
  - name: Contact paralysant (coûte 2 actions)
    description: La liche utilise son Contact paralysant.
  - name: Regard effrayant (coûte 2 actions)
    description: "La liche fixe du regard une créature qu'elle peut voir dans un rayon de 3 mètres autour d'elle. La cible doit réussir un jet de sauvegarde de Sagesse DD 18 contre la magie ou être effrayée pendant 1 minute. La cible effrayée peut retenter son jet de sauvegarde à la fin de chacun de ses tours, mettant fin à l'effet qui l'affecte en cas de réussite. Si le jet de sauvegarde de la cible est une réussite, ou si l'effet se termine pour elle, la cible est immunisée au regard de la liche pour les prochaines 24 heures."
  - name: Perturbation de la vie (coûte 3 actions)
    description: "Toute créature non morte-vivante située dans un rayon de 6 mètres autour de la liche doit effectuer un jet de sauvegarde de Constitution DD 18 contre la magie, subissant 21 (6d6) dégâts nécrotiques en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
```
