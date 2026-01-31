---
Class: PNJ
tags:
  - pnj
  - boss
  - hobgobelin
  - mage
  - légion
aliases:
  - Moloch
---

# Lieutenant Moloch
![[Pasted image 20260120230421.png]]
**Race :** Hobgobelin
**Rôle :** Commandant de l'Avant-Poste de la Roche-Fendue / Mage de Conjuration
**Affiliation :** [[La Légion de Fer]]

## 👤 Description
Moloch est un mage de guerre calculateur. Il porte une robe de mage en cuir renforcé par-dessus une cotte de mailles, et son visage est marqué par une brûlure magique.
*   **Personnalité :** Cruel et pragmatique. Il voit la magie comme l'outil ultime de domination.

## Statblock (Boss Mage)

```dnd-monstre
name: Lieutenant Moloch
type: Humanoïde (hobgobelin)
taille: Moyen
alignement: loyal mauvais
ca: 16 (cotte de mailles)
pv: 65 (10d8 + 20)
mana: 20
vitesse: 9 m
for: 12 (+1)
dex: 10 (+0)
con: 14 (+2)
int: 18 (+4)
sag: 12 (+1)
cha: 14 (+2)
js: Int +7, Sag +4
sens: vision dans le noir 18 m, Perception passive 11
langues: commun, gobelin
facteur_puissance: 5 (1800 PX)
traits:
  - name: Avantage Tactique
    description: "Une fois par tour, lorsque Moloch inflige des dégâts à une créature avec un sort, il inflige 7 (2d6) dégâts supplémentaires si la cible est à 1,50 m d'un allié de Moloch."
  - name: Invocation consciencieuse (Conjuration)
    description: "La concentration de Moloch ne peut pas être brisée par des dégâts tant qu'il se concentre sur un sort de conjuration."
  - name: Incantation
    description: "Moloch est un mage de niveau 6. Intelligence (DD 15, +7 au toucher). Emplacements : 4/3/3.\n- Tours de magie : Rayon de givre, Trait de feu, Main magique, Prestidigitation.\n- Niveau 1 : Bouclier, Projectile magique, Onde de choc, Graisse (Conj).\n- Niveau 2 : Rayon ardent, Foulée brumeuse (Conj), Toile d'araignée (Conj).\n- Niveau 3 : Boule de feu, Nuage nauséabond (Conj)."
actions:
  - name: Bâton de Magie de Guerre
    description: "Attaque au corps à corps : +4 au toucher, 1,50 m. Touché : 4 (1d6 + 1) contondant."
  - name: "Boule de Feu (Sort Niv 3)"
    description: "Zone de 6m de rayon à 45m. DD 15 Dex ou 28 (8d6) feu (moitié si réussi)."
  - name: "Nuage Nauséabond (Sort Niv 3 - Conjuration)"
    description: "Sphère de 6m de rayon à 27m (Concentration). DD 15 Con ou la créature perd son action à son tour à cause des nausées. (Concentration protégée par Invocation Consciencieuse)."
  - name: "Rayon Ardent (Sort Niv 2)"
    description: "Crée 3 rayons. Attaque de sort : +7 au toucher, 36m. Chaque rayon inflige 7 (2d6) feu."
  - name: "Toile d'Araignée (Sort Niv 2 - Conjuration)"
    description: "Cube de 6m à 18m (Concentration). DD 15 Dex ou entravé. (Concentration protégée)."
  - name: "Projectile Magique (Sort Niv 1)"
    description: "Crée 3 projectiles (touchent d'office). 1d4+1 force par projectile (Total: 3d4+3)."
  - name: "Onde de Choc (Sort Niv 1)"
    description: "Cube de 4,5m. DD 15 Con ou 9 (2d8) tonnerre et repoussé de 3m (moitié si réussi)."
  - name: "Graisse (Sort Niv 1 - Conjuration)"
    description: "Zone de 3m à 18m. DD 15 Dex ou tombe à terre (Prone)."
  - name: "Trait de Feu (Tour de magie)"
    description: "Attaque de sort : +7 au toucher, 36m. Touché : 11 (2d10) feu."
  - name: "Rayon de Givre (Tour de magie)"
    description: "Attaque de sort : +7 au toucher, 18m. Touché : 9 (2d8) froid et vitesse réduite de 3m."
  - name: Permutation (Conjuration - Recharge 5-6)
    description: "Moloch se téléporte magiquement jusqu'à 9 mètres. Alternativement, il peut échanger sa place avec une créature de taille M ou P consentante à 9 mètres."
  - name: Invocation Mineure
    description: "Moloch crée un objet inanimé non magique (max 1m de côté, 5kg) dans sa main ou au sol."
  - name: "Foulée Brumeuse (Sort Niv 2 - Conjuration)"
    description: "Action Bonus. Se téléporte jusqu'à 9 mètres dans un espace inoccupé visible."
réactions:
  - name: "Bouclier (Sort Niv 1)"
    description: "En cas d'attaque ou projectile magique. Gagne +5 à la CA jusqu'au début de son prochain tour et annule les projectiles magiques."
```

## 🗣️ Dialogues
*   *"La ville meurt de faim pendant que nous nous engraissons. C'est la loi naturelle."*
*   *"Ne me forcez pas à vous recycler en cendres."*

## 💎 Butin
*   **Grimoire de Moloch** : Contient tous ses sorts de conjuration.
*   **[[Le Monocle de Moloch]]** : Trouvé dans son coffre (ou sur lui).
*   **[[Pierre de Faille de Moloch]]** : Posée sur son bureau.