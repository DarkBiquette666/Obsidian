---
name: MagicItem
extends: Equipment
icon: sparkle
properties:
  rarity:
    type: select
    options: ["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact"]
    default: "Common"
    description: "Rareté de l'objet"
  type:
    type: string
    description: "Type d'objet (ex: Wondrous Item, Weapon (Sword))"
  requires_attunement:
    type: boolean
    default: false
    description: "Nécessite un lien (harmonisation)"
  attunement_conditions:
    type: string
    description: "Conditions de lien (ex: by a wizard)"
  damage_type:
    type: array
    item_type: string
    description: "Types de dégâts magiques supplémentaires"
  resistance:
    type: array
    item_type: string
    description: "Résistances conférées"
---
# Blueprint MagicItem
Objet enchanté avec des propriétés spéciales.
