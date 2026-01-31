# Instructions d'Installation et de Compilation

## Probleme: Google Drive Partagé

Le vault Obsidian est situe sur un Google Drive partage (`y:\Shared drives\`), ce qui cause des problemes avec `npm install` et la compilation TypeScript.

Les erreurs typiques incluent:
- `npm warn tar TAR_ENTRY_ERROR UNKNOWN: unknown error, write`
- Modules npm installes incompletement
- `tsc` et `esbuild` ne s'executent pas correctement

## Solutions

### Solution 1: Compiler depuis un Emplacement Local (Recommandé)

1. Copier le dossier du plugin vers un emplacement local:
   ```bash
   cd C:\Users\[votre-nom]\Documents
   git clone [ou copier] le dossier obsidian-dnd-content
   cd obsidian-dnd-content
   ```

2. Installer les dependances:
   ```bash
   npm install
   ```

3. Compiler le plugin:
   ```bash
   npm run build
   ```

4. Copier le fichier compile vers le vault:
   ```bash
   copy main.js "y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\.obsidian\plugins\obsidian-dnd-content\"
   ```

### Solution 2: Utiliser un Symlink

1. Creer le plugin dans un dossier local:
   ```bash
   cd C:\Users\[votre-nom]\dev
   mkdir obsidian-dnd-content
   cd obsidian-dnd-content
   ```

2. Copier les fichiers sources (main.ts, src/, etc.)

3. Installer et compiler:
   ```bash
   npm install
   npm run build
   ```

4. Creer un symlink depuis le vault vers le dossier local:
   ```bash
   mklink /D "y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\.obsidian\plugins\obsidian-dnd-content" "C:\Users\[votre-nom]\dev\obsidian-dnd-content"
   ```

### Solution 3: Mode Developpement avec Watcher

Si vous developpez activement:

1. Compiler en mode watch depuis un emplacement local:
   ```bash
   cd C:\Users\[votre-nom]\dev\obsidian-dnd-content
   npm run dev
   ```

2. Utiliser un script pour copier automatiquement main.js:
   ```bash
   # Creer watch-and-copy.bat
   :loop
   xcopy /Y main.js "y:\Shared drives\Ubiquity\Perso\Obsidian\D&D\.obsidian\plugins\obsidian-dnd-content\"
   timeout /t 2
   goto loop
   ```

### Solution 4: Version Pre-compilee (Temporaire)

Pour tester rapidement le plugin sans compiler, j'ai cree une version JavaScript simplifiee.

Voir le fichier `main-simple.js` qui peut etre renomme en `main.js` pour tester le plugin sans compilation TypeScript.

## Structure Minimale Requise

Pour que le plugin fonctionne dans Obsidian, vous avez besoin de:

```
obsidian-dnd-content/
├── manifest.json      (requis)
├── main.js           (requis - fichier compile)
├── styles.css        (requis)
└── versions.json     (optionnel mais recommande)
```

Les fichiers sources TypeScript (main.ts, src/) ne sont necessaires que pour le developpement.

## Verification

Apres avoir compile et copie main.js:

1. Ouvrir Obsidian
2. Aller dans Parametres > Plugins communautaires
3. Activer le "Mode sans echec" si necessaire
4. Chercher "D&D Content Renderer" dans la liste
5. Activer le plugin
6. Ouvrir le fichier de test: `Glossary/Bestiaire/Mephit de Vapeur - Test.md`
7. Verifier que le bloc `dnd-monstre` s'affiche correctement

## Developpement

Pour developper le plugin:

1. Travaillez toujours dans un dossier local (C:\Users\...)
2. Compilez avec `npm run dev` pour le mode watch
3. Testez dans Obsidian
4. Copiez main.js vers le vault uniquement quand tout fonctionne

## Support

En cas de probleme:
- Verifier que Node.js est installe (v16 ou superieur)
- Verifier que npm fonctionne: `npm --version`
- Verifier la console developpeur d'Obsidian (Ctrl+Shift+I)
- Lire les logs du plugin dans la console
