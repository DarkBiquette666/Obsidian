---
tags:
  - pnj
  - hobgobelin
  - combattant
---

# Krug le Casseur

**Race :** Hobgobelin
**Rôle :** Champion de l'arène "La Fosse aux Os".
**Localisation :** [[Le Camp du Fer Rouillé]].

## Description
Krug est une montagne de muscles, même pour un Hobgobelin. Il ne porte pas d'armure, juste un pantalon de cuir taché de sang et de poussière, exhibant fièrement un torse couvert de cicatrices rituelles. Son nez a été cassé tant de fois qu'il est complètement aplati.
Il passe ses journées à soulever des troncs d'arbres ou à briser des pierres avec son front pour amuser les gobelins.

*   **Personnalité :** Brutal mais sportif. Il ne déteste pas "les petits hommes" tant qu'ils savent se battre. Il parle peu, grogne beaucoup.
*   **Motivation :** Trouver un adversaire qui ne tombe pas au premier coup.

## Le Défi de la Fosse
Krug s'ennuie. Si Simon approche de l'arène, Krug le pointe du doigt et grogne : *"Toi. Viande fraîche. Tu te bats ?"*

*   **Règles :** Pas d'armes, pas de magie, pas d'armure lourde. Le premier qui ne peut plus se relever ou qui abandonne a perdu.
*   **Mise :** 10 pièces d'or (ou équivalent). Krug parie sa précieuse **Potion de Force de Géant** (qu'il croit être juste du "Jus de Bagarre").

## Statblock (Bagarreur)
*Hobgobelin spécialisé dans la lutte.*

```dnd-monstre
name: Krug le Casseur
type: Humanoïde (Gobelinoïde)
taille: Moyenne
alignement: Loyal Mauvais
ca: 14 (Défense sans armure)
pv: 45 (6d8 + 18)
vitesse: 9 m
for: 18 (+4)
dex: 14 (+2)
con: 16 (+3)
int: 8 (-1)
sag: 10 (+0)
cha: 9 (-1)
sens: Vision dans le noir 18 m, Perception passive 10
langues: Commun, Gobelin
facteur_puissance: 1 (200 PX)
traits:
  - name: Prise de Fer
    description: "Krug a un avantage aux jets de Force (Athlétisme) pour agripper une cible."
actions:
  - name: Attaques multiples
    description: "Krug effectue deux attaques à mains nues."
  - name: Coup de Poing
    description: "Attaque au corps à corps : +6 au toucher, allonge 1,50 m, une cible. Touché : 6 (1d4 + 4) dégâts contondants."
    attaque: +6 au toucher
  - name: Brise-Dos (Recharge 5-6)
    description: "Si Krug a agrippé une créature, il peut tenter de l'écraser. La cible doit réussir un JdS Constitution DD 14 ou subir 14 (3d6 + 4) dégâts contondants et être étourdie jusqu'à la fin de son prochain tour."
réactions:
  - name: Encaissement
    description: "Krug peut réduire les dégâts d'une attaque contondante qu'il voit de 1d10 + 3."
```
