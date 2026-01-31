---
name: Weapon
extends: Equipment
icon: sword
properties:
  category:
    type: select
    options: ["Arme courante", "Arme de guerre"]
    default: "Arme courante"
  range_type:
    type: select
    options: ["Corps à corps", "A distance"]
    default: "Corps à corps"
  damage:
    type: string
    description: "Dés de dégâts (ex: 1d8)"
  damage_type:
    type: select
    options: ["contondant", "perforant", "tranchant"]
    default: "contondant"
  properties:
    type: array
    item_type: link
    target_folder: "Glossary/Objets/Equipement/Armes/Proprietes"
    description: "Propriétés spéciales (Légère, Finesse...)"
  weapon_mastery:
    type: link
    target_folder: "Glossary/Objets/Equipement/Armes/Botte d'arme"
    description: "Botte d'arme associée"
  ammunition:
    type: link
    target_folder: "Glossary/Objets/Equipement/Matériel d'aventurier"
    filter_tag: "munitions"
    description: "Type de munition requis"
  range:
    type: string
    description: "Portée (ex: 6/18)"
---
# Blueprint Weapon
Arme offensive.
