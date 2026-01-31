---
aliases:
  - Solar
tags:
  - monstre
  - bestiaire
type: Céleste
facteur_puissance: 21 (33000 PX)
---

# Solar

```dnd-monstre
name: Solar
type: Céleste
taille: Grand
alignement: loyal bon
ca: 21 (armure naturelle)
pv: 243 (18d10 + 144)
vitesse: 15 m, vol 45 m
for: 26
dex: 22
con: 26
int: 25
sag: 25
cha: 30
sauvegardes: Int +14, Sag +14, Cha +17
sens: vision véritable 36 m, Perception passive 24
langues: toutes, télépathie 36 m
facteur_puissance: 21 (33000 PX)
immunites_etats: charmé, effrayé, empoisonné, épuisement
source: Monster Manual (SRD)
compétences:
  - Perception +14
immunites:
  - nécrotique
  - poison
résistances:
  - radiant ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Armes angéliques
    description: "Les attaques avec une arme du solar sont magiques. Lorsque le solar touche avec n'importe quelle arme, l'arme inflige 6d8 dégâts radiants supplémentaires (inclus dans l'attaque ci-dessous)."
  - name: Conscience divine
    description: Le solar sait quand il entend un mensonge.
  - name: Incantation innée
    description: "La caractéristique d'incantation innée du solar est le Charisme (jet de sauvegarde contre ses sorts DD 25). Le solar peut lancer les sorts suivants de manière innée, sans avoir besoin de composantes matérielles :"
  - name: Résistance à la magie
    description: Le solar a un avantage aux jets de sauvegarde contre les sorts et autres effets magiques.
actions:
  - name: Attaques multiples
    description: "Le solar effectue deux attaques d'épée à deux mains."
  - name: Épée à deux mains
    description: "Attaque au corps à corps avec une arme : +15 au toucher, allonge 1,50 m, une cible. Touché : 22 (4d6 + 8) dégâts tranchants + 27 (6d8) dégâts radiants."
    attaque: +15 au toucher
  - name: Arc long Tueur
    description: "Attaque à distance avec une arme : +13 au toucher, portée 45/180 m, une cible. Touché : 15 (2d8 + 6) dégâts perforants + 27 (6d8) dégâts radiants. Si la cible est une créature qui a 100 points de vie ou moins, elle doit réussir un jet de sauvegarde de Constitution DD 15 ou mourir."
    attaque: +13 au toucher
  - name: Épée volante
    description: "Le solar lâche son épée à deux mains pour qu'elle flotte dans un espace inoccupé à 1,50 mètre de lui. Si le solar peut voir l'épée, il peut la commander mentalement en utilisant une action bonus pour qu'elle vole jusqu'à une distance de 15 mètres et effectue une attaque contre une cible ou retourne dans la main du solar. Si l'épée volante est ciblée par un effet, le solar est considéré comme étant en train de la tenir. L'épée volante tombe au sol si le solar meurt."
  - name: Contact guérisseur (4/jour)
    description: Le solar touche une autre créature. La cible récupère par magie 40 (8d8 + 4) points de vie et est guérie de toutes malédictions, maladies, poisons, aveuglement ou assourdissement.
legendaires:
  - name: Téléportation
    description: "Le solar se téléporte magiquement, avec tout l'équipement qu'il porte ou transporte, vers un espace inoccupé qu'il peut voir et situé dans un rayon de 36 mètres autour de lui."
  - name: Explosion brûlante (coûte 2 actions)
    description: "Le solar émet une énergie magique et divine. Toutes les créatures de son choix dans un rayon de 3 mètres doivent effectuer un jet de sauvegarde de Dextérité DD 23, subissant 14 (4d6) dégâts de feu plus 14 (4d6) dégâts radiants en cas d'échec, ou la moitié de ces dégâts en cas de réussite."
  - name: Regard aveuglant (coûte 3 actions)
    description: "Le solar prend pour cible une créature qu'il peut voir et qui se trouve à 9 mètres ou moins de lui. Si la cible peut voir, celle-ci doit réussir un jet de sauvegarde de Constitution DD 15 ou être aveuglée, jusqu'à ce qu'une magie, comme un sort de restauration partielle, lui restaure la vue."
```
