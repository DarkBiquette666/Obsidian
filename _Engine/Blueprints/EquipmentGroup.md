---
name: EquipmentGroup
properties:
  selection_mode:
    type: select
    options: ["AND", "OR"]
    default: "AND"
    description: "AND = On reçoit tout. OR = On doit choisir UN élément."
  items:
    type: array
    item_type: EquipmentReference
    description: "Les objets du groupe"
---
# Blueprint EquipmentGroup
Un groupe d'objets qui sont soit tous donnés (AND), soit soumis à un choix (OR).
