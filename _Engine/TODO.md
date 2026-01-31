# RPG Engine - Plan de Route

## État des lieux (Session précédente)
Le moteur est fonctionnel. L'équipement, les sorts, les races et les classes ont été migrés vers le nouveau système.

## À Faire (Priorité Haute)

- [x] **Vérification Équipement de départ** :
    - [x] Barbare (Fait).
    - [x] Barde.
    - [x] Clerc.
    - [x] Druide.
    - [x] Ensorceleur.
    - [x] Guerrier.
    - [x] Magicien.
    - [x] Moine.
    - [x] Occultiste.
    - [x] Paladin.
    - [x] Rôdeur.
    - [x] Roublard.
    *Note : Utiliser le champ `starting_equipment_draft` comme référence dans l'Inspecteur.*

- [x] **Historiques (Backgrounds)** :
    - [x] Créer le Blueprint `Background.md`.
    - [x] Migrer les données (Extraire Compétences, Outils, Équipement).

- [x] **Compétences (Skills)** :
    - [x] Créer le Blueprint `Skill.md` (Caractéristique liée).
    - [x] Migrer les données.

- [x] **Dons (Feats)** :
    - [x] Créer le Blueprint `Feat.md`.
    - [x] Créer les Blueprints de prérequis (`Requirement`, `Ability`, `Proficiency`, `Race`, `CastSpell`, `Composite`).
    - [x] Migrer les prérequis vers le système `Requirement` polymorphe.

## Améliorations Futures

- [ ] **Blueprint Builder** : Créer une interface pour créer et éditer les Blueprints graphiquement (éviter l'édition manuelle du YAML).
- [ ] **Bestiaire** : Migrer les monstres (actuellement en codeblock) vers le système de Blueprints.
- [ ] **Sous-Classes** : Lier formellement les sous-classes aux classes (actuellement fait pour le Clerc uniquement).
- [ ] **Character Builder** : Créer une vue qui assemble toutes ces données pour créer un personnage.
