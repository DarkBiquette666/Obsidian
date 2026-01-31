---
name: Class
icon: sword
properties:
  hit_dice:
    type: string
    default: "d8"
  subclasses:
    type: array
    item_type: link
    target_folder: "Glossary/Domaines"
    description: "Domaines ou sous-classes disponibles"
  saving_throws:
    type: array
    item_type: string
  armor_proficiencies:
    type: array
    item_type: string
  weapon_proficiencies:
    type: array
    item_type: string
  spellcasting_ability:
    type: select
    options: ["force", "dexterite", "constitution", "intelligence", "sagesse", "charisme", "aucune"]
    default: "aucune"

  starting_equipment:
    type: array
    item_type: EquipmentGroup
    description: "Équipement de départ (Groupes)"
  progression:
    type: array
    item_type: ClassLevelEntry
    description: "Tableau de progression par niveau"
---
# Blueprint Class
Définit une classe de personnage.
