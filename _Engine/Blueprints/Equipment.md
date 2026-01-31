---
name: Equipment
is_abstract: true
properties:
  cost:
    type: string
    description: "Prix (ex: 15 po)"
  weight:
    type: number
    description: "Poids en kg"
  description:
    type: string
    multiline: true
---
# Blueprint Equipment
Objet de base pouvant être acheté et transporté.
