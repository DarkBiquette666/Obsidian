---
rpg_class: LootTable
description: "Loot pour rencontres difficiles (CR élevé, boss mineurs)"
dice: "1d100"
entries:
  - range_min: 1
    range_max: 15
    entry_type: currency
    currency: "4d6 po"
  - range_min: 16
    range_max: 30
    entry_type: currency
    currency: "2d6 pp"
  - range_min: 31
    range_max: 40
    entry_type: table
    table: "[[Consommables]]"
  - range_min: 41
    range_max: 50
    entry_type: table
    table: "[[Objets Divers]]"
  - range_min: 51
    range_max: 60
    entry_type: table
    table: "[[Armes Courantes]]"
  - range_min: 61
    range_max: 70
    entry_type: table
    table: "[[Armures]]"
  - range_min: 71
    range_max: 82
    entry_type: table
    table: "[[Objets Magiques Communs]]"
  - range_min: 83
    range_max: 92
    entry_type: table
    table: "[[Objets Magiques Uncommon]]"
  - range_min: 93
    range_max: 98
    entry_type: table
    table: "[[Objets Magiques Rare]]"
  - range_min: 99
    range_max: 100
    entry_type: table
    table: "[[Objets Magiques Very Rare]]"
---
# Rencontre Difficile

Table de loot pour les rencontres difficiles. Bonne chance d'équipement et d'objets magiques.

| Plage | Résultat |
|-------|----------|
| 1-15 | 4d6 po |
| 16-30 | 2d6 pp |
| 31-40 | Consommable |
| 41-50 | Objet divers |
| 51-60 | Arme courante |
| 61-70 | Armure |
| 71-82 | Objet magique commun (12%) |
| 83-92 | Objet magique uncommon (10%) |
| 93-98 | Objet magique rare (6%) |
| 99-100 | Objet magique très rare (2%) |
