---
name: Armor
extends: Equipment
icon: shield
properties:
  category:
    type: select
    options: ["Arme légère", "Armure intermédiaire", "Armure lourde", "Bouclier"]
    default: "Arme légère"
  ac_base:
    type: number
    description: "CA de base"
  dex_bonus:
    type: boolean
    default: true
    description: "Ajoute le bonus de Dex ?"
  max_dex_bonus:
    type: number
    default: 99
    description: "Bonus de Dex max (2 pour intermédiaire, 0 pour lourde)"
  stealth_disadvantage:
    type: boolean
    default: false
  strength_requirement:
    type: number
    default: 0
---
# Blueprint Armor
Armure ou bouclier.
