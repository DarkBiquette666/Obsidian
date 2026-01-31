---
name: LootTable
is_abstract: false
icon: box
properties:
  description:
    type: string
    multiline: true
    description: "Description de la table (ex: Trésor de gobelin, Coffre rare)"
  dice:
    type: string
    default: "1d100"
    description: "Dé à lancer (ex: 1d100, 1d20, 2d6)"
  entries:
    type: array
    item_type: LootEntry
    description: "Liste des entrées de loot avec leurs plages"
---
# Blueprint LootTable
Table de génération de loot. Chaque table définit un dé à lancer et des entrées avec des plages de résultats.
