---
name: CategoryItem
extends: EquipmentReference
properties:
  category:
    type: select
    options: ["Arme courante", "Arme de guerre", "Arme courante de corps à corps", "Arme de guerre de corps à corps", "Armure légère", "Armure intermédiaire", "Armure lourde", "Bouclier", "Focaliseur arcanique", "Focaliseur druidique", "Symbole sacré", "Instrument de musique", "Jeu", "Outil d'artisan"]
    default: "Arme courante"
    description: "Catégorie d'objet"
---
# Blueprint CategoryItem
Référence à une catégorie d'objets.
