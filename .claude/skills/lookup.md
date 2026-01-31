# Skill: /lookup

## Description
Recherche précise d'une règle, d'un sort, d'un objet ou d'un monstre dans la base de données (Glossary).

## Usage
```
/lookup [Terme de recherche]
```

## Comportement
1.  **Cible**: Dossier `Glossary/` uniquement (et `Dons/` pour les dons).
2.  **Priorité**:
    - Cherche d'abord une correspondance exacte de nom de fichier.
    - Cherche ensuite dans les `aliases`.
    - Cherche enfin dans le contenu.
3.  **Résultat**: Affiche un résumé concis de la règle/objet avec un lien vers la fiche originale. Ne pas halluciner de règles.

## Exemple
> /lookup "Action Bonus"
> **Résultat**: Résumé de la règle d'Action Bonus (Fichier: `Glossary/Règles/Action Bonus.md`).
