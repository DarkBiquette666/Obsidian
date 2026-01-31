---
alias:
  - Silas
tags:
  - pnj
  - sidekick
race: Humain
affiliation: "Église de Heaum (Ordre de l'Œil Vigilant)"
---

# Frère Silas

**Rôle :** Sidekick (Soutien Feu / Érudit)
**Race :** Humain
**Affiliation :** Église de Heaum (Ordre de l'Œil Vigilant)

> Un jeune homme à lunettes, aux cheveux en bataille et à la robe de bure tachée d'encre. Il porte un lourd sac à dos rempli de parchemins. Il semble nerveux hors d'une bibliothèque, mais il brûle (littéralement) d'une foi inébranlable en la vérité.

## Relations
*   **[[Haut-Prêtre Aldric Forteguard|Aldric Forteguard]] :** Son supérieur. Silas a peur de lui depuis qu'il a découvert certains textes.
*   **[[Simon]] :** Son protecteur. Silas se considère comme le "radar" et Simon comme le "missile".

## Fiche Technique

```dnd-monstre
name: Frère Silas
type: Humanoïde (Humain)
taille: Moyen
alignement: Loyal Neutre
ca: 16 (Cotte de mailles, Bouclier)
pv: 31 (4d8 + 8)
mana: 10
vitesse: 9 m
for: 10
dex: 12
con: 14
int: 16
sag: 16
cha: 10
sens: Perception Passive 13, Investigation Passive 13
langues: Commun, Céleste, Infernal, Elfique
facteur_puissance: 2
sauvegardes: Sagesse +5, Constitution +4
compétences:
  - name: Histoire
    description: " +5"
  - name: Religion
    description: " +5"
  - name: Médecine
    description: " +5"
  - name: Arcanes
    description: " +5"
traits:
  - name: "Incantation (Domaine de la Lumière - Niv 4)"
    description: "Silas est un clerc de niveau 4. Caractéristique d'incantation : Sagesse (DD 13, +5 au toucher). Emplacements : 4/3.\n- Tours de magie : Flamme sacrée, Stabilisation, Lumière.\n- Niveau 1 : Bénédiction, Mains brûlantes (D), Lueurs féeriques (D), Mot de guérison, Soin des blessures, Sanctuaire.\n- Niveau 2 : Rayon ardent (D), Sphère de feu (D)."
  - name: "Don : Mage de Guerre"
    description: "Silas a l'Avantage aux jets de sauvegarde de Constitution pour maintenir sa concentration sur un sort lorsqu'il subit des dégâts. Il peut aussi lancer un sort en réaction lors d'une attaque d'opportunité."
  - name: "Chercheur (Sage)"
    description: "Lorsqu'il ne connaît pas une information, Silas sait presque toujours où et auprès de qui l'obtenir (bibliothèque, archive, temple ou érudit)."
  - name: "Conduit Divin (1/Repos)"
    description: "Silas peut canaliser l'énergie divine pour alimenter des effets magiques. Il peut utiliser soit Radiance de l'Aube, soit Renvoi des morts-vivants."
actions:
  - name: "Bénédiction (Sort Niv 1)"
    description: "3 cibles à 9m. Ajoutent 1d4 aux jets d'attaque et de sauvegarde pendant 1 min (Concentration). (Niv sup: +1 cible). **[PRIORITÉ ABSOLUE]**"
  - name: "Radiance de l'Aube (Conduit Divin)"
    description: "Zone de 9m autour de lui. Chaque créature hostile doit réussir un JdS de Con DD 13 ou subir 15 (2d10 + 4) dégâts radieux (moitié si réussi). Dissipe l'obscurité magique."
  - name: "Renvoi des morts-vivants (Conduit Divin)"
    description: "Chaque mort-vivant à moins de 9m doit réussir un JdS de Sagesse DD 13 ou être repoussé pendant 1 minute (doit s'éloigner et ne peut pas utiliser de réactions)."
  - name: "Mot de Guérison (Sort Niv 1)"
    description: "Action Bonus. Portée 18m. Rend 5 (1d4 + 3) PV à une créature visible. (Niv sup: +1d4 soin). **[URGENCE]**"
  - name: "Rayon Ardent (Sort Niv 2)"
    description: "Crée 3 rayons. Attaque de sort : +5 au toucher, 36m. Chaque rayon inflige 7 (2d6) dégâts de feu. (Niv sup: +1 rayon)."
  - name: "Sphère de Feu (Sort Niv 2)"
    description: "Invoque une sphère à 18m (Concentration). DD 13 Dex ou 7 (2d6) feu pour toute créature finissant son tour à côté. Action bonus pour déplacer la sphère de 9m. (Niv sup: +1d6 dégâts)."
  - name: "Sanctuaire (Sort Niv 1)"
    description: "Action Bonus. Pendant 1 min, tout ennemi ciblant Silas doit réussir un JdS de Sagesse DD 13 ou attaquer une autre cible (ou perdre son attaque)."
  - name: "Lueurs Féeriques (Sort Niv 1)"
    description: "Cube de 6m à 18m (Concentration). DD 13 Dex ou les attaques contre les cibles ont l'Avantage. Empêche l'invisibilité."
  - name: "Flamme Sacrée (Tour de magie)"
    description: "Cible à 18m. DD 13 Dex ou 9 (2d8) dégâts radieux. Aucun bénéfice du couvert pour ce jet de sauvegarde."
  - name: "Mains Brûlantes (Sort Niv 1)"
    description: "Cône de 4,5m. DD 13 Dex ou 10 (3d6) dégâts de feu (moitié si réussi). (Niv sup: +1d6 dégâts)."
  - name: "Soin des Blessures (Sort Niv 1)"
    description: "Contact. Rend 7 (1d8 + 3) PV à une créature touchée. (Niv sup: +1d8 soin)."
  - name: "Stabilisation (Tour de magie)"
    description: "Contact. Stabilise instantanément une créature vivante à 0 PV."
  - name: "Lumière (Tour de magie)"
    description: "Objet touché émet une lumière vive sur 6m et faible sur 6m."
  - name: "Masse d'armes"
    description: "Attaque au corps à corps : +2 au toucher, 1,5m. Touché : 3 (1d6) contondant."
réactions:
  - name: "Illumination Protectrice"
    description: ": 3/Jour. Impose le Désavantage à une attaque contre Silas provenant d'une créature à moins de 9m."
```

## Inventaire

- **[[Dague de l'Inquisiteur]]** : Brille en présence de Fiélon (Diablo ou Démon) à moins de 30m même s'il est invisible ou déguisé. Elle ne révèle pas la position exacte, seulement la présence.

## ⚔️ Tactiques Rapides (Cheat Sheet)

*   **1. LE CLASSIQUE (Début de combat)**
    *   **Action :** *Bénédiction* (Niv 2 pour 4 cibles : Simon, Chien 1, Chien 2, Silas).
    *   **Résultat :** Tout le "Pack" touche plus souvent et résiste mieux. Avec *Mage de Guerre*, Silas perdra rarement ce bonus.

*   **2. LE NETTOYEUR (Contre une horde de faibles)**
    *   **Positionnement :** S'avancer au milieu (9m de portée).
    *   **Action :** *[[Radiance de l'Aube]]*.
    *   **Résultat :** 2d10+4 dégâts radiants de zone. **Important :** Ne touche QUE les ennemis hostiles (pas de tir ami).

*   **3. L'ARTILLEUR (Monocible / Boss)**
    *   **Action :** *Rayon Ardent* (3 attaques à 2d6).
    *   **Action Bonus :** *Mot de Guérison* (Si quelqu'un est à terre) OU *Sanctuaire* (Préventif).

*   **4. LA TORTUE (Silas est en danger)**
    *   **Action Bonus :** *Sanctuaire*.
    *   **Action :** *Esquive* (Dodge).
    *   **Résultat :** Intouchable. L'ennemi doit réussir un JdS Sagesse pour cibler, ET a désavantage sur l'attaque.

## Histoire & Secret
Silas était archiviste. Il a trouvé des incohérences dans les rapports de la "Purge de l'Assemblée" d'il y a 20 ans. Il a vu qu'Aldric était le seul survivant d'une unité d'élite, mais les rapports de l'époque parlent de "Morts au combat" alors que les registres des cimetières sont vides.
Il a été envoyé en mission pour l'éloigner de la bibliothèque.