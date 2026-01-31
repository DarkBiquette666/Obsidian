---
rpg_class: LootTable
description: "Butin typique trouvé sur un gobelin ou dans leur repaire"
dice: "1d100"
entries:
  - range_min: 1
    range_max: 30
    entry_type: currency
    currency: "1d6 pc"
    quantity: "1"
  - range_min: 31
    range_max: 60
    entry_type: currency
    currency: "2d6 pa"
    quantity: "1"
  - range_min: 61
    range_max: 75
    entry_type: item
    item: "[[Dague]]"
    quantity: "1"
  - range_min: 76
    range_max: 85
    entry_type: item
    item: "[[Cimeterre]]"
    quantity: "1"
  - range_min: 86
    range_max: 95
    entry_type: item
    item: "[[Armure de cuir]]"
    quantity: "1"
  - range_min: 96
    range_max: 100
    entry_type: table
    table: "[[Objets Magiques Communs]]"
    quantity: "1"
---
# Trésor de Gobelin

Table de loot pour les gobelins. Lance 1d100 pour déterminer le butin.

| Plage | Résultat |
|-------|----------|
| 1-30 | 1d6 pièces de cuivre |
| 31-60 | 2d6 pièces d'argent |
| 61-75 | Dague |
| 76-85 | Cimeterre |
| 86-95 | Armure de cuir |
| 96-100 | Objet magique commun (sous-table) |
