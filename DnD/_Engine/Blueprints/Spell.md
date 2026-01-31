---
name: Spell
icon: flame
properties:
  level:
    type: number
    default: 0
    description: "Niveau du sort (0 pour sort mineur)"
  school:
    type: string
    description: "École de magie"
  classes:
    type: array
    item_type: string
    description: "Classes pouvant apprendre ce sort"
  deals_damage:
    type: boolean
    default: false
    description: "Est-ce que ce sort inflige des dégâts ?"
  domain_spells:
    type: array
    item_type: link
    target_folder: "Glossary/Domaines"
    description: "Domaines divins utilisant ce sort"
---
# Blueprint Spell
Définit la structure de base d'un sort de magie.