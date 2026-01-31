import os

OUTPUT_DIR = r"Y:\\Shared drives\\Ubiquity\\Perso\\Obsidian\\D&D\\Glossary\\Liste des Sorts"

# Données extraites de Glossary/Classes/Clerc/Clerc.md
features = [
    {
        "name": "Renvoi des morts-vivants",
        "source": "Clerc (Base)",
        "aliases": ["Turn Undead"],
        "time": "1 action",
        "range": "9 mètres (30 feet)",
        "duration": "1 minute",
        "desc": "Vous présentez votre symbole sacré. Chaque mort-vivant dans un rayon de 9 mètres qui peut vous voir ou vous entendre doit réussir un jet de sauvegarde de Sagesse ou être renvoyé pendant 1 minute (fuit et ne peut pas s'approcher volontairement à moins de 9 m)."
    },
    {
        "name": "Préservation de la vie",
        "source": "Clerc (Domaine de la Vie)",
        "aliases": ["Preserve Life"],
        "time": "1 action",
        "range": "9 mètres (30 feet)",
        "duration": "Instantanée",
        "desc": "Vous présentez votre symbole sacré et invoquez l'énergie de guérison. Vous restaurez un nombre de points de vie égal à **5 fois votre niveau de clerc**, répartis comme vous le souhaitez entre les créatures dans un rayon de 9 mètres.\n\nVous ne pouvez pas utiliser cette capacité sur un mort-vivant ou un artifice, et vous ne pouvez pas restaurer plus de la moitié des PV max d'une créature."
    },
    {
        "name": "Frappe guidée",
        "source": "Clerc (Domaine de la Guerre)",
        "aliases": ["Guided Strike"],
        "time": "Aucune (Lors d'une attaque)",
        "range": "Personnelle",
        "duration": "Instantanée",
        "desc": "Lorsque vous effectuez un jet d'attaque, vous pouvez utiliser votre Conduit divin pour gagner un **bonus de +10 au jet**. Vous faites ce choix après avoir vu le résultat mais avant que le MD annonce si l'attaque touche."
    },
    {
        "name": "Bénédiction du dieu de la guerre",
        "source": "Clerc (Domaine de la Guerre)",
        "aliases": ["War God's Blessing"],
        "time": "Réaction",
        "range": "9 mètres (30 feet)",
        "duration": "Instantanée",
        "desc": "Lorsqu'une créature dans un rayon de 9 mètres effectue un jet d'attaque, vous pouvez utiliser votre réaction et votre Conduit divin pour lui accorder un **bonus de +10 au jet**."
    },
    {
        "name": "Fureur destructrice",
        "source": "Clerc (Domaine de la Tempête)",
        "aliases": ["Destructive Wrath"],
        "time": "Aucune (Lors des dégâts)",
        "range": "Personnelle",
        "duration": "Instantanée",
        "desc": "Lorsque vous infligez des dégâts de **foudre** ou de **tonnerre**, vous pouvez utiliser votre Conduit divin pour infliger les dégâts maximum au lieu de lancer les dés."
    },
    {
        "name": "Savoir ancestral",
        "source": "Clerc (Domaine du Savoir)",
        "aliases": ["Knowledge of the Ages"],
        "time": "1 action",
        "range": "Personnelle",
        "duration": "10 minutes",
        "desc": "Vous pouvez utiliser votre Conduit divin pour puiser dans le puits de la connaissance divine. Vous gagnez la **maîtrise d'une compétence ou d'un outil de votre choix** pendant 10 minutes."
    },
    {
        "name": "Lecture des pensées",
        "source": "Clerc (Domaine du Savoir)",
        "aliases": ["Read Thoughts"],
        "time": "1 action",
        "range": "18 mètres (60 feet)",
        "duration": "1 minute",
        "desc": "Vous pouvez utiliser votre Conduit divin pour lire les pensées d'une créature. Vous pouvez alors utiliser votre accès à son esprit pour la commander (comme le sort *Suggestion*) sans dépenser de mana."
    },
    {
        "name": "Invocation de réplique",
        "source": "Clerc (Domaine de la Duperie)",
        "aliases": ["Invoke Duplicity"],
        "time": "1 action",
        "range": "9 mètres (30 feet)",
        "duration": "Concentration, jusqu'à 1 minute",
        "desc": "Vous créez une illusion parfaite de vous-même qui dure 1 minute. Par une action bonus, vous pouvez déplacer l'illusion jusqu'à 9 mètres.\n\nVous pouvez lancer des sorts comme si vous étiez à la place de l'illusion, mais vous devez utiliser vos propres sens."
    },
    {
        "name": "Linceul d'ombre",
        "source": "Clerc (Domaine de la Duperie)",
        "aliases": ["Cloak of Shadows"],
        "time": "1 action",
        "range": "Personnelle",
        "duration": "Jusqu'à la fin du prochain tour",
        "desc": "Lorsque vous êtes dans une zone de lumière faible ou de ténèbres, vous pouvez utiliser votre action pour devenir **invisible** jusqu'à la fin de votre prochain tour."
    },
    {
        "name": "Charme des animaux et plantes",
        "source": "Clerc (Domaine de la Nature)",
        "aliases": ["Charm Animals and Plants"],
        "time": "1 action",
        "range": "9 mètres (30 feet)",
        "duration": "1 minute",
        "desc": "Chaque bête ou créature végétale dans un rayon de 9 mètres doit réussir un jet de sauvegarde de Sagesse ou être **charmée** pendant 1 minute."
    },
    {
        "name": "Bénédiction de l'artisan",
        "source": "Clerc (Domaine de la Forge)",
        "aliases": ["Artisan's Blessing"],
        "time": "1 heure (Rituel)",
        "range": "Toucher",
        "duration": "Instantanée",
        "desc": "Vous conduisez un rituel pour créer un objet non magique en métal (valeur max 100 po). La création prend 1 heure et l'objet apparaît à la fin."
    },
    {
        "name": "Sanctuaire du crépuscule",
        "source": "Clerc (Domaine du Crépuscule)",
        "aliases": ["Twilight Sanctuary"],
        "time": "1 action",
        "range": "Personnelle (Rayon de 9m)",
        "duration": "1 minute",
        "desc": "Vous invoquez une sphère de lumière tamisée de 9 mètres de rayon centrée sur vous. Elle se déplace avec vous.\n\nÀ la fin de chaque tour, vous et les alliés dans la sphère gagnez (au choix) :\n*   Des **PV temporaires** égaux à 1d6 + niveau de clerc.\n*   La fin d'un effet qui rend charmé ou effrayé."
    }
]

for feat in features:
    filename = f"{feat['name']}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Construction du YAML
    aliases_yaml = "\n".join([f'  - "{a}"' for a in feat['aliases']])
    
    content = f"""---
Class: Feature
type: Conduit Divin
source: {feat['source']}
alias:
{aliases_yaml}
---

# **{feat['name']}**

*Conduit Divin - {feat['source']}*

**Temps d'incantation** : {feat['time']}
**Portée** : {feat['range']}
**Durée** : {feat['duration']}

{feat['desc']}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filename}")
