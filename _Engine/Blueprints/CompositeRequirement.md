---
name: CompositeRequirement
extends: Requirement
properties:
  operator:
    type: select
    options: ["AND", "OR"]
    default: "AND"
  requirements:
    type: array
    item_type: Requirement
---
# Blueprint CompositeRequirement
Permet de combiner plusieurs prérequis avec des opérateurs logiques (ET/OU).
