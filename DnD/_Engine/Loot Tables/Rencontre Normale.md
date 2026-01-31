---
rpg_class: LootTable
description: "Loot pour rencontres normales (CR moyen)"
dice: "1d100"
entries:
  - range_min: 1
    range_max: 20
    entry_type: currency
    currency: "2d6 pa"
  - range_min: 21
    range_max: 40
    entry_type: currency
    currency: "2d6 po"
  - range_min: 41
    range_max: 55
    entry_type: table
    table: "[[Consommables]]"
  - range_min: 56
    range_max: 70
    entry_type: table
    table: "[[Objets Divers]]"
  - range_min: 71
    range_max: 82
    entry_type: table
    table: "[[Armes Courantes]]"
  - range_min: 83
    range_max: 92
    entry_type: table
    table: "[[Armures]]"
  - range_min: 93
    range_max: 98
    entry_type: table
    table: "[[Objets Magiques Communs]]"
  - range_min: 99
    range_max: 100
    entry_type: table
    table: "[[Objets Magiques Uncommon]]"
---
# Rencontre Normale

Table de loot pour les rencontres normales. Mix équilibré avec une petite chance d'objet magique.

| Plage | Résultat |
|-------|----------|
| 1-20 | 2d6 pa |
| 21-40 | 2d6 po |
| 41-55 | Consommable |
| 56-70 | Objet divers |
| 71-82 | Arme courante |
| 83-92 | Armure |
| 93-98 | Objet magique commun (6%) |
| 99-100 | Objet magique uncommon (2%) |
