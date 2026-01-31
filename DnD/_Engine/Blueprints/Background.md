---
name: Background
properties:
  feat:
    type: link
    target_folder: "Glossary/Dons"
    description: "Don accordé par l'historique"
  skill_proficiencies:
    type: array
    item_type: string
    description: "Compétences maîtrisées (ex: 'Discrétion', 'Tromperie')"
  tool_proficiencies:
    type: array
    item_type: string
    description: "Outils maîtrisés (ex: 'Outils de voleur', 'Jeu de cartes')"
  languages:
    type: array
    item_type: string
    description: "Langues apprises (ex: 'Elfique', '2 de votre choix')"
  equipment:
    type: array
    item_type: EquipmentGroup
    description: "Équipement de départ"
  feature:
    type: object
    properties:
      name:
        type: string
      description:
        type: string
    description: "Capacité spéciale de l'historique"
---
# Blueprint Background
Définit un historique de personnage (Background).
