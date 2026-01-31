---
name: LootEntry
is_abstract: false
icon: package
properties:
  range_min:
    type: number
    default: 1
    description: "Valeur minimale de la plage (incluse)"
  range_max:
    type: number
    default: 100
    description: "Valeur maximale de la plage (incluse)"
  entry_type:
    type: select
    options: ["item", "table", "currency", "nothing"]
    default: "item"
    description: "Type d'entrée: item direct, sous-table, monnaie, ou rien"
  item:
    type: link
    target_folder: "Glossary/Objets"
    description: "Lien vers l'item (si entry_type = item)"
  table:
    type: link
    target_folder: "_Engine/Loot Tables"
    description: "Lien vers une sous-table (si entry_type = table)"
  currency:
    type: string
    description: "Formule de monnaie (ex: 2d6*10 po, 1d4 pp)"
  quantity:
    type: string
    default: "1"
    description: "Quantité ou formule (ex: 1, 1d4, 2d6)"
---
# Blueprint LootEntry
Une entrée dans une table de loot. Définit une plage de résultats et ce qui est obtenu.
