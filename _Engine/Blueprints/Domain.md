---
name: Domain
icon: sun
properties:
  parent_class:
    type: link
    target_folder: "Glossary/Classes"
    description: "Classe à laquelle appartient ce domaine (ex: Clerc)"
  domain_spells:
    type: array
    item_type: DomainSpellEntry
    description: "Liste des sorts accordés par le domaine"
---
# Blueprint Domain
Définit un domaine divin ou une spécialisation de classe.
