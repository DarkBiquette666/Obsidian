---
name: AbilityRequirement
extends: Requirement
properties:
  ability:
    type: select
    options: ["force", "dexterite", "constitution", "intelligence", "sagesse", "charisme"]
  value:
    type: number
    default: 13
---
# Blueprint AbilityRequirement
Prérequis de caractéristique minimale.
