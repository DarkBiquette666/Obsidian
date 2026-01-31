---
aliases:
  - Vampire
tags:
  - monstre
  - bestiaire
type: Mort-vivant
facteur_puissance: 13 (10000 PX)
---

# Vampire

```dnd-monstre
name: Vampire
type: Mort-vivant
taille: Moyen
alignement: loyal mauvais
ca: 16 (armure naturelle)
pv: 144 (17d8 + 68)
vitesse: 9 m
for: 18
dex: 18
con: 18
int: 17
sag: 15
cha: 18
sauvegardes: Dex +9, Sag +7, Cha +9
sens: vision dans le noir 36 m, Perception passive 17
langues: "les langues qu'il connaissait de son vivant"
facteur_puissance: 13 (10000 PX)
source: Monster Manual (SRD)
compétences:
  - Discrétion +9
  - Perception +7
résistances:
  - nécrotique ; contondant
  - "perforant et tranchant d'attaques non magiques"
traits:
  - name: Métamorphe
    description: "Si le vampire n'est pas exposé à la lumière du soleil ou dans une étendue d'eau courante, il peut utiliser son action pour se métamorphoser en une chauve-souris de taille TP ou en un nuage de brouillard de taille M, ou pour reprendre sa forme véritable. Tant qu'il est sous forme de chauve-souris, le vampire ne peut pas parler, sa vitesse de déplacement au sol tombe à 1,50 m, mais il obtient une vitesse de vol de 9 mètres. Mises à part sa taille et sa vitesse, ses statistiques sont les mêmes quelle que soit sa forme. Tout ce qu'il porte sur lui est transformé avec lui, contrairement à ce qu'il transporte. Il retrouve sa forme véritable s'il meurt. Tant qu'il est sous forme brumeuse, le vampire ne peut effectuer aucune action, parler ou manipuler un objet. Il est en apesanteur, obtient une vitesse de vol de 6 mètres, peut rester en vol stationnaire, pénétrer dans l'espace d'une créature hostile et s'y arrêter. De plus, si de l'air peut passer par un petit espace, le nuage de brume le peut également sans être considéré comme passant dans un espace étroit. Le nuage ne peut pas pénétrer dans l'eau. Il a un avantage aux jets de sauvegarde de Force, Dextérité et Constitution, et est immunisé contre tous les dégâts non magiques, à l'exception des dégâts qu'il subit du soleil."
  - name: Résistance légendaire (3/jour)
    description: Si le vampire échoue à un jet de sauvegarde, il peut décider de transformer cet échec en réussite.
  - name: Échappatoire brumeuse
    description: "Lorsqu'il tombe à 0 points de vie en dehors de sa tombe, le vampire se transforme en un nuage de brume (comme avec le trait Métamorphe) plutôt que de tomber inconscient, à condition qu'il ne soit pas exposé à la lumière du soleil ou dans une étendue d'eau courante. S'il ne peut pas se transformer, il est détruit. Tant qu'il est à 0 points de vie sous forme brumeuse, il ne peut pas retrouver sa forme de vampire, il doit impérativement atteindre sa tombe dans les 2 heures, ou être détruit. Dès qu'il atteint sa tombe, il retrouve sa forme vampirique. Il est alors paralysé jusqu'à ce qu'il récupère au moins 1 point de vie. Après être resté 1 heure dans sa tombe avec 0 points de vie, le vampire récupère 1 point de vie."
  - name: Régénération
    description: "Le vampire récupère 20 points de vie au début de son tour s'il possède au moins 1 point de vie et qu'il n'est ni exposé à la lumière du soleil ou dans une étendue d'eau courante. Si le vampire subit des dégâts radiants ou des dégâts via de l'eau bénite, ce trait ne fonctionne pas au début de son prochain tour."
  - name: "Pattes d'araignée"
    description: "Le vampire peut escalader des surfaces difficiles et être au plafond la tête en bas sans avoir besoin d'effectuer un jet de caractéristique."
  - name: Faiblesses de vampire
    description: "Le vampire a les faiblesses suivantes : Interdiction. Le vampire ne peut pas entrer dans une résidence sans y avoir été invité par l'un de ses occupants."
  - name: "Détruit par les étendues d'eau courante"
    description: "Le vampire subit 20 dégâts d'acide lorsqu'il termine son tour au sein d'une étendue d'eau courante."
  - name: Un pieu dans le cœur
    description: "Si une arme perforante faite de bois est enfoncée dans son cœur alors qu'il est incapable d'agir dans sa tombe, le vampire devient paralysé jusqu'à ce que ce pieu soit retiré."
  - name: Hypersensibilité au soleil
    description: "Le vampire subit 20 dégâts radiants lorsqu'il débute son tour à la lumière du soleil. S'il est exposé à la lumière du soleil, il a un désavantage aux jets d'attaque et de caractéristique."
actions:
  - name: Attaques multiples (forme de vampire uniquement)
    description: "Le vampire effectue deux attaques, mais seule l'une des deux peut être une attaque de morsure."
  - name: Attaque à mains nues (forme de vampire uniquement)
    description: "Attaque au corps à corps avec une arme : +9 au toucher, allonge 1,50 m, une créature. Touché : 8 (1d8 + 4) dégâts contondants. Plutôt que d'infliger des dégâts, le vampire peut agripper la cible (évasion DD 18)"
    attaque: +9 au toucher
  - name: Morsure (forme de vampire ou de chauve-souris uniquement)
    description: "Attaque au corps à corps avec une arme : +9 au toucher, allonge 1,50 m, une créature consentante ou une créature agrippée par le vampire, incapable d'agir ou entravée. Touché : 7 (1d6 + 4) dégâts perforants + 10 (3d6) dégâts nécrotiques. Le maximum de points de vie de la cible est réduit d'un montant égal à la quantité de dégâts nécrotiques subis, et le vampire récupère un nombre de points de vie équivalent. Cette réduction perdure jusqu'à ce que la cible termine un repos long. La cible meurt si cet effet réduit son maximum de points de vie à 0. Un humanoïde abattu de la sorte puis enterré se relève la nuit suivante en tant que vampirien sous le contrôle du vampire."
    attaque: +9 au toucher
  - name: Charme
    description: "Le vampire cible un humanoïde qu'il peut voir et à 9 mètres maximum de lui. Si la cible peut voir le vampire, elle doit réussir un jet de sauvegarde de Sagesse DD 17 contre cette capacité magique ou être charmée par le vampire. Une fois charmée, la cible voit le vampire comme un véritable ami qu'elle doit écouter et protéger. Bien que la cible ne soit pas sous le contrôle du vampire, elle prend les requêtes et les actions du vampire de la façon la plus favorable qui soit, et elle est une cible consentante pour l'attaque de morsure du vampire. Chaque fois que le vampire ou un compagnon du vampire fait quelque chose de nuisible à la cible, elle peut retenter un jet de sauvegarde, mettant fin à l'effet qui l'affecte en cas de réussite. Sinon l'effet dure 24 heures ou jusqu'à ce que le vampire soit détruit, sur un autre plan d'existence que celui de la cible, ou utilise une action bonus pour mettre fin à l'effet."
  - name: Enfants de la nuit (1/jour)
    description: "Le vampire appelle magiquement à lui 2d4 nuées de chauves-souris ou de rats, à condition que le soleil ne soit pas encore levé. S'il est à l'extérieur, le vampire peut choisir d'appeler à la place 3d6 loups. Les créatures appelées arrivent en 1d4 tours, agissant tels des alliés du vampire et obéissant à ses commandes verbales. Les bêtes restent 1 heure, jusqu'à ce que le vampire meure, ou jusqu'à ce que le vampire utilise une action bonus pour les congédier."
legendaires:
  - name: Déplacement
    description: "Le vampire se déplace de sa vitesse sans provoquer d'attaque d'opportunité."
  - name: Attaque à mains nues
    description: Le vampire effectue une attaque à mains nues.
  - name: Morsure (coûte 2 actions)
    description: Le vampire effectue une attaque de morsure.
```
