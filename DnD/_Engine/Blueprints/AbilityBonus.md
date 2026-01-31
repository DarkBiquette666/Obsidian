---
name: AbilityBonus
properties:
  ability:
    type: select
    options: ["force", "dexterite", "constitution", "intelligence", "sagesse", "charisme"]
    default: "constitution"
    description: "Caractéristique augmentée"
  value:
    type: number
    default: 1
    description: "Valeur du bonus"
---
# Blueprint AbilityBonus
Représente un bonus à une caractéristique.
