# Claude Integration pour Obsidian

Une intégration complète de Claude AI pour Obsidian, permettant d'utiliser l'intelligence artificielle d'Anthropic directement dans votre environnement de prise de notes.

## 🚀 Fonctionnalités

- **Assistant IA intégré** : Interagissez avec Claude directement dans Obsidian
- **Analyse de notes** : Obtenez des analyses détaillées de vos notes
- **Amélioration automatique** : Améliorez la qualité de vos notes avec l'IA
- **Génération d'idées** : Générez des idées créatives sur n'importe quel sujet
- **Interface intuitive** : Interface utilisateur moderne et responsive
- **Historique de conversation** : Gardez le contexte de vos conversations
- **Actions rapides** : Boutons d'action rapide pour les tâches courantes

## 📦 Installation

### Installation manuelle

1. Téléchargez le dernier release depuis GitHub
2. Extrayez le contenu dans votre dossier de plugins Obsidian : `{vault}/.obsidian/plugins/obsidian-claude-integration/`
3. Activez le plugin dans les paramètres d'Obsidian

### Installation via Community Plugins (recommandé)

1. Ouvrez les paramètres d'Obsidian
2. Allez dans "Community plugins"
3. Désactivez "Safe mode"
4. Cliquez sur "Browse" et recherchez "Claude Integration"
5. Installez et activez le plugin

## ⚙️ Configuration

### 1. Obtenir une clé API Claude

1. Visitez [console.anthropic.com](https://console.anthropic.com)
2. Créez un compte ou connectez-vous
3. Générez une nouvelle clé API
4. Copiez la clé API

### 2. Configurer le plugin

1. Ouvrez les paramètres d'Obsidian
2. Allez dans "Community plugins" > "Claude Integration"
3. Entrez votre clé API Claude
4. Configurez les autres paramètres selon vos préférences

## 🎯 Utilisation

### Interface principale

- **Icône Claude** : Cliquez sur l'icône cerveau dans la barre latérale pour ouvrir l'assistant
- **Raccourcis clavier** : Utilisez `Ctrl/Cmd + Shift + P` et recherchez "Claude"

### Actions rapides

- **Analyser la note** : Obtenez une analyse complète de la note active
- **Améliorer la note** : Améliorez automatiquement la qualité de votre note
- **Générer des idées** : Générez des idées créatives basées sur le contenu

### Menu contextuel

Clic droit dans l'éditeur pour accéder aux options Claude :
- Demander à Claude
- Améliorer avec Claude

## 🔧 Paramètres

### Modèles disponibles

- **Claude 3 Sonnet** (recommandé) : Équilibré entre vitesse et qualité
- **Claude 3 Opus** : Le plus puissant, idéal pour des tâches complexes
- **Claude 3 Haiku** : Le plus rapide, parfait pour des réponses courtes

### Température

Contrôle la créativité des réponses :
- **0.0** : Réponses très focalisées et cohérentes
- **0.7** : Équilibré (recommandé)
- **1.0** : Réponses très créatives et variées

## 💡 Exemples d'utilisation

### Analyser une note

```
Analyse cette note sur la productivité et suggère des améliorations
```

### Améliorer du contenu

```
Améliore cette note en corrigeant la grammaire et en améliorant la structure
```

### Générer des idées

```
Génère des idées pour un projet de développement web
```

### Résumer du contenu

```
Résume ce texte en 200 mots maximum
```

## 🛠️ Développement

### Prérequis

- Node.js 16+
- npm ou yarn

### Installation des dépendances

```bash
npm install
```

### Développement

```bash
npm run dev
```

### Build de production

```bash
npm run build
```

## 📁 Structure du projet

```
obsidian-claude-integration/
├── src/
│   ├── main.ts              # Point d'entrée principal
│   ├── claude-api.ts        # Wrapper API Claude
│   ├── claude-modal.ts      # Interface utilisateur
│   └── settings.ts          # Configuration
├── styles.css               # Styles CSS
├── manifest.json            # Manifeste Obsidian
├── package.json             # Dépendances
└── README.md               # Documentation
```

## 🔒 Sécurité

- Votre clé API est stockée localement et n'est jamais transmise à des tiers
- Toutes les communications avec l'API Claude sont chiffrées
- Le plugin ne collecte aucune donnée personnelle

## 🐛 Dépannage

### Erreurs courantes

**"Clé API Claude invalide"**
- Vérifiez que votre clé API est correcte
- Assurez-vous que votre compte Anthropic est actif

**"Limite de taux dépassée"**
- Attendez quelques minutes avant de réessayer
- Vérifiez votre quota d'utilisation sur console.anthropic.com

**"Erreur de connexion"**
- Vérifiez votre connexion internet
- Assurez-vous que l'API Claude est accessible

### Support

Si vous rencontrez des problèmes :

1. Vérifiez que vous utilisez la dernière version du plugin
2. Consultez les logs dans la console développeur d'Obsidian
3. Ouvrez une issue sur GitHub avec les détails du problème

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Signaler des bugs
2. Proposer de nouvelles fonctionnalités
3. Soumettre des pull requests
4. Améliorer la documentation

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🙏 Remerciements

- [Obsidian](https://obsidian.md) pour l'excellent environnement de développement
- [Anthropic](https://anthropic.com) pour l'API Claude
- La communauté Obsidian pour l'inspiration et le support

---

**Note** : Ce plugin n'est pas affilié à Anthropic ou Obsidian. Il s'agit d'un projet communautaire indépendant. 