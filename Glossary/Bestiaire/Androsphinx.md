---
aliases:
  - Androsphinx
tags:
  - monstre
  - bestiaire
type: Monstruosité
facteur_puissance: 17 (18000 PX)
---

# Androsphinx

```dnd-monstre
name: Androsphinx
type: Monstruosité
taille: Grand
alignement: loyal neutre
ca: 17 (armure naturelle)
pv: 199 (19d10 + 95)
vitesse: 12 m, vol 18 m
for: 22
dex: 10
con: 20
int: 16
sag: 18
cha: 23
sauvegardes: Dex +6, Con +11, Int +9, Sag +10
sens: vision véritable 36 m, Perception passive 20
langues: commun, sphinx
facteur_puissance: 17 (18000 PX)
immunites_etats: charmé, effrayé
source: Monster Manual (SRD)
compétences:
  - Arcanes +9
  - Perception +10
  - Religion +15
immunites:
  - psychique ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Inscrutable
    description: "Le sphinx est immunisé aux effets cherchant à ressentir ses émotions ou à lire ses pensées, ainsi qu'à n'importe quel sort de divination qu'il refuse. Les jets de Sagesse (Intuition) réalisés pour connaître les intentions ou la sincérité du sphinx subissent un désavantage."
  - name: Armes magiques
    description: Les attaques avec une arme du sphinx sont magiques.
  - name: Incantation
    description: "Le sphinx est un lanceur de sorts de niveau 12. Sa caractéristique d'incantation est la Sagesse (jet de sauvegarde contre ses sorts DD 18, +10 au toucher pour les attaques avec un sort). Il n'a pas besoin de composantes matérielles pour lancer ses sorts. Le sphinx a la liste de sorts de clerc préparée :"
actions:
  - name: Attaques multiples
    description: Le sphinx effectue deux attaques avec ses griffes.
  - name: Griffes
    description: "Attaque au corps à corps avec une arme : +12 au toucher, allonge 1,50 m, une cible. Touché : 17 (2d10 + 6) dégâts tranchants."
    attaque: +12 au toucher
  - name: Rugissement (3/jour)
    description: "Le sphinx pousse un rugissement magique. Chaque fois qu'il rugit avant d'avoir terminé un repos long, le rugissement est de plus en plus fort et son effet différent, comme détaillé ci-dessous. Chaque créature se trouvant à 150 mètres du sphinx et étant capable de l'entendre doivent effectuer un jet de sauvegarde."
  - name: Premier rugissement
    description: "Toutes les créatures qui échouent à un jet de sauvegarde de Sagesse DD 18 sont effrayées pendant 1 minute. Une créature peut retenter le jet de sauvegarde à la fin de chacun de ses tours, mettant fin l'effet qu'elle subit."
  - name: Second rugissement
    description: "Toutes les créatures qui échouent à un jet de sauvegarde de Sagesse DD 18 sont assourdies et effrayées pendant 1 minute. Une créature effrayée est paralysée et peut retenter le jet de sauvegarde à la fin de chacun de ses tours, mettant fin l'effet qu'elle subit."
  - name: Troisième rugissement
    description: "Chaque créature effectue un jet de sauvegarde de Constitution DD 18. En cas d'échec, elle subit 44 (8d10) dégâts de tonnerre et est jetée à terre. En cas de réussite, elle subit la moitié des dégâts et n'est pas jetée à terre."
legendaires:
  - name: Attaque avec les griffes
    description: Le sphinx effectue une attaque avec ses griffes.
  - name: Téléportation (coûte 2 actions)
    description: "Le sphinx se téléporte par magie, emportant avec lui l'équipement qu'il porte ou transporte, jusqu'à un espace inoccupé qu'il peut voir dans un rayon de 36 mètres."
  - name: Sort (coûte 3 actions)
    description: Le sphinx lance un sort choisi parmi sa liste de sorts préparés, en utilisant un emplacement de sort normalement.
```
