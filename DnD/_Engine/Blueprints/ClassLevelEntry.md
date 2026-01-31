---
name: ClassLevelEntry
properties:
  level:
    type: number
  proficiency_bonus:
    type: number
  features:
    type: array
    item_type: string
    description: "Capacités débloquées à ce niveau"
  mana:
    type: number
    description: "Points de mana (si applicable)"
---
# Blueprint ClassLevelEntry
Définit les bénéfices d'un niveau spécifique dans une classe.
