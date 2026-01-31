---
name: LevelRequirement
extends: Requirement
properties:
  level:
    type: number
    default: 1
    description: "Niveau global du personnage"
  operator:
    type: select
    options: [">=", "==", "<="]
    default: ">="
---
# Blueprint LevelRequirement
Prérequis de niveau global du personnage.
