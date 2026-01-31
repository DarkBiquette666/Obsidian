---
rpg_class: LootTable
description: "Loot pour rencontres faciles (CR bas, ennemis mineurs)"
dice: "1d100"
entries:
  - range_min: 1
    range_max: 30
    entry_type: currency
    currency: "1d6 pc"
  - range_min: 31
    range_max: 55
    entry_type: currency
    currency: "2d6 pa"
  - range_min: 56
    range_max: 70
    entry_type: currency
    currency: "1d4 po"
  - range_min: 71
    range_max: 80
    entry_type: table
    table: "[[Consommables]]"
  - range_min: 81
    range_max: 90
    entry_type: table
    table: "[[Objets Divers]]"
  - range_min: 91
    range_max: 98
    entry_type: table
    table: "[[Armes Courantes]]"
  - range_min: 99
    range_max: 100
    entry_type: table
    table: "[[Objets Magiques Communs]]"
---
# Rencontre Facile

Table de loot pour les rencontres faciles. Principalement de l'argent et des consommables, rarement de l'équipement.

| Plage | Résultat |
|-------|----------|
| 1-30 | 1d6 pc |
| 31-55 | 2d6 pa |
| 56-70 | 1d4 po |
| 71-80 | Consommable |
| 81-90 | Objet divers |
| 91-98 | Arme courante |
| 99-100 | Objet magique commun (2%) |
