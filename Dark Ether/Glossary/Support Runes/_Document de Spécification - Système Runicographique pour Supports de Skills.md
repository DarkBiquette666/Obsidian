
## 1. Objectif



Créer un alphabet runique logique pour identifier visuellement les runes de support d'un Action-RPG. Chaque icône doit être générée selon une grammaire visuelle permettant au joueur de "lire" l'effet de la rune sans texte.



## 2. Contraintes Esthétiques (Style Runique)



Pour garantir l'aspect "gravé" et ancien, l'IA doit respecter les règles suivantes lors de la conception des formes :



- **Traits Droits Uniquement :** Pas de courbes lisses, pas de cercles parfaits. Utiliser des segments pour simuler les courbes si nécessaire.

    

- **Pas d'Horizontales Pures :** Privilégier les diagonales pour éviter de "fendre le grain du bois" (logique historique des runes).

    

- **Épaisseur Hiérarchique :** Le trait principal (La Poutre) est plus épais que les traits secondaires (Les Glyphes).

    

- **Minimalisme :** Maximum 5 traits par rune pour garantir la lisibilité en petit format.

    



## 3. Système de Construction Modulaire



Chaque rune de support est composée de deux éléments : **La Poutre** (Catégorie) et **Le Glyphe** (Modificateur).



### A. Les Poutres (La Racine de l'Action)







Définit la famille mécanique du skill ou la "source" de la modification.







*   **FORCE (Impact / Dégâts)**



    *   *Forme :* Verticale `|`



    *   *Usage :* Dégâts bruts, Physique, DoT agressifs.







*   **FLUX (Projectiles / Mouvement)**



    *   *Forme :* Diagonale `/`



    *   *Usage :* Projectiles, Chaining, Homing, Vitesse.







*   **CHAMP (Zone / Environnement)**



    *   *Forme :* Forme en `V`



    *   *Usage :* AoE, Auras, Effets de sol.







*   **SYSTÈME (Arcane / Méta-Données)**



    *   *Forme :* Losange `◇`



    *   *Usage :* Cooldowns, Durée, Mana, Conversion.







*   **CORPS (Constitution / Défense)**



    *   *Forme :* Chevron inversé `^`



    *   *Usage :* Vie, Armure, Scaling Santé (Vitality), Fortify.







### B. Les Glyphes (Le Modificateur d'Effet)



Traits plus fins venant se greffer sur la Poutre pour préciser l'effet.



#### I. Manipulations Temporelles & Spatiales

- **Vitesse / Fréquence :** Double chevron `>>` sur le côté droit. (Ex: *Faster Attacks, Rapid Recharge*).

- **Durée / Extension :** Trait horizontal prolongeant la forme. (Ex: *Extended Duration*).

- **Portée / Taille :** Flèches pointant vers l'extérieur `< >`. (Ex: *Massive Area, Long Reach*).

- **Compression / Intensité :** Flèches pointant vers l'intérieur `> <`. (Ex: *Concentrated Effect*).



#### II. Comportement des Projectiles

- **Multiplication :** Deux traits parallèles courts traversant la poutre `||`. (Ex: *Multiple Projectiles*).

- **Bifurcation (Fork) :** La poutre se sépare en deux au sommet `Y`.

- **Enchaînement (Chain) :** Un motif en "Z" ou éclair reliant deux points.

- **Guidage (Homing) :** Un carré ou une cible stylisée autour du centre.



#### III. Transformation & Ressources

- **Conversion :** Un motif cyclique ou deux flèches inversées. (Ex: *Elemental Conversion*).

- **Coupe / Économie :** Une barre transversale nette qui "coupe" la forme. (Ex: *Efficiency*).

- **Vie / Sang :** Une croix `+` ou un trait vertical descendant (goutte). (Ex: *Vitality*).

- **Mana / Esprit :** Un point ou petit losange au centre de la poutre.



#### IV. Types de Dégâts & Ailments

- **Feu / Brûlure :** Un chevron `^` au sommet.

- **Froid / Gel :** Un trait croisé perpendiculaire `+` en haut.

- **Foudre / Choc :** Un trait en zigzag.

- **Saignement / Physique :** Des traits dentelés ou en scie sur le côté. (Ex: *Laceration*).

- **Poison / Chaos :** Un losange vide rattaché à la base ou des points épars. (Ex: *Vicious Ailments*).

## Directives de Création : Unicité des Runes

**Problème à résoudre :** Éviter que deux supports ayant des mots-clés similaires (ex: deux supports de vitesse) ne se ressemblent.

**Solution : La Mutation Géométrique.** Pour chaque support, l'IA doit générer une "Signature" en modifiant la structure même de la rune selon ces trois leviers :

### Levier 1 : La Morphologie de la Poutre (Base)

Ne pas se contenter d'un trait droit. Chaque support doit avoir un style de trait propre :

- **Trait plein** `|`
    
- **Trait segmenté** (pointillés ou brisés)
    
- **Trait double** (deux lignes parallèles très serrées)
    
- **Trait avec nœud** (un petit losange ou carré au milieu du trait)
    

### Levier 2 : La Position des Affixes

Si deux runes utilisent le glyphe "Vitesse" `>>` :

- Le support A place le glyphe **en haut à droite**.
    
- Le support B place le glyphe **au milieu à gauche**.
    
- Le support C intègre le glyphe **directement à l'intérieur** de la poutre.
    

### Levier 3 : Les "Points d'Ancrage" (Détails uniques)

Chaque rune doit recevoir un détail ornemental aléatoire mais fixe qui sert d'ID visuel :

- Un point (impact) à une extrémité.
    
- Une barre transversale asymétrique.
    
- Une terminaison en fourche ou en pointe.
    

**Exemple de différenciation pour l'IA :**

- **Support "Added Fire" :** Poutre verticale simple + Flamme en haut.
    
- **Support "Added Burning Damage" :** Poutre verticale **segmentée** + Flamme en haut + Point à la base.
    
- _Résultat :_ Le joueur voit le "Feu" et les "Dégâts", mais distingue deux formes distinctes.

## 4. Instructions pour la Génération



Lors de l'analyse d'un support, suivre cette logique de priorité :



1. **Identifier la Poutre :**

   - Est-ce un Projectile ? -> *FLUX*

   - Est-ce une AoE ? -> *CHAMP*

   - Est-ce lié à la Vie/Défense ? -> *CORPS*

   - Est-ce une modification de stat pure (Cooldown, Mana, Conversion) ? -> *SYSTÈME*

   - Sinon (Dégâts, DoT) -> *FORCE*



2. **Identifier le Glyphe :**

   - Chercher le mot-clé le plus fort (ex: "Fast", "Multi", "Fire", "Life").

   - Appliquer le glyphe correspondant.



### Exemples Corrigés :



- **Vitality Support** :

  - *Base :* Utilise la Vie pour les dégâts -> Poutre **CORPS**.

  - *Modif :* Ajout de dégâts/Vie -> Glyphe **VIE** (+).

  

- **Rapid Recharge** :

  - *Base :* Modifie le Cooldown (Temps) -> Poutre **SYSTÈME**.

  - *Modif :* Accélère -> Glyphe **VITESSE** (>>).



- **Elemental Conversion** :

  - *Base :* Change le type de dégâts -> Poutre **SYSTÈME**.

  - *Modif :* Cycle -> Glyphe **CONVERSION**.



## 5. Livrable Attendu

L'IA générera des fichiers SVG nommés `[SkillName]_Rune.svg` en **Blanc Pur (#FFFFFF)**, sans aucun effet de lueur (Glow) ni fond. Cela permet une recoloration dynamique (Tint/Modulate) et l'ajout d'effets post-process directement dans le moteur de jeu.
