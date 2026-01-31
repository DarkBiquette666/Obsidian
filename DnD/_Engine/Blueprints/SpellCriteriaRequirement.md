---
name: SpellCriteriaRequirement
extends: Requirement
properties:
  class:
    type: link
    target_folder: "Glossary/Classes"
    description: "Le sort doit appartenir à cette classe"
  spell:
    type: link
    target_folder: "Glossary/Liste des Sorts"
    default: "any"
    description: "Sort spécifique requis"
  level:
    type: number
    default: 0
    description: "Niveau du sort (0 pour mineur)"
  operator:
    type: select
    options: [">=", "==", "<="]
    default: ">="
  must_deal_damage:
    type: select
    options: ["any", "true", "false"]
    default: "any"
---
# Blueprint SpellCriteriaRequirement
Prérequis flexible 100% piloté par les valeurs par défaut du Blueprint.
