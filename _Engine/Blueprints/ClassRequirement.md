---
name: ClassRequirement
extends: Requirement
properties:
  class:
    type: link
    target_folder: "Glossary/Classes"
  level:
    type: number
    default: 1
  operator:
    type: select
    options: [">=", "==", "<="]
    default: ">="
---
# Blueprint ClassRequirement
Prérequis basé sur le niveau d'une classe avec opérateur de comparaison.