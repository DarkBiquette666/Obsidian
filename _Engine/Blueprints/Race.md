---
name: Race
icon: user
properties:
  augmentations:
    type: array
    item_type: AbilityBonus
    description: "Augmentations de caractéristiques raciales"
  speed:
    type: number
    default: 9
    description: "Vitesse de déplacement en mètres"
  size:
    type: select
    options: ["TP", "P", "M", "G", "TG"]
    default: "M"
    description: "Taille de la créature"
  languages:
    type: array
    item_type: link
    target_folder: "Glossary/Langues"
    description: "Langues parlées"
  traits:
    type: array
    item_type: link
    target_folder: "Glossary/Traits"
    description: "Traits raciaux spéciaux (Vision dans le noir, etc.)"
  weapon_proficiencies:
    type: array
    item_type: string
    description: "Armes maîtrisées (ex: 'Épée longue')"
  armor_proficiencies:
    type: array
    item_type: string
    description: "Armures maîtrisées (ex: 'Légère')"
  tool_proficiencies:
    type: array
    item_type: link
    target_folder: "Glossary/Objets/Equipement/Outils"
    description: "Outils maîtrisés"
---
# Blueprint Race
Définit une race jouable avec ses maîtrises et traits.