---
name: ProficiencyRequirement
extends: Requirement
properties:
  proficiency_type:
    type: select
    options: ["armor", "weapon", "tool", "skill"]
  target:
    type: string
    description: "Nom de la maîtrise (ex: 'armures lourdes', 'discrétion')"
---
# Blueprint ProficiencyRequirement
Prérequis de maîtrise.
