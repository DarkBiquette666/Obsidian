import { Plugin, WorkspaceLeaf, TFile } from 'obsidian';
import { InspectorView, VIEW_TYPE_INSPECTOR } from './src/InspectorView';

export interface BlueprintDefinition {
    name: string;
    is_abstract?: boolean;
    extends?: string;
    properties: Record<string, any>;
}

export default class RPGEnginePlugin extends Plugin {
    blueprints: Map<string, BlueprintDefinition> = new Map();

    async onload() {
        console.log('Loading RPG Engine (Blueprints)...');

        this.app.workspace.onLayoutReady(() => {
             this.loadBlueprints();
        });

        this.registerView(
            VIEW_TYPE_INSPECTOR,
            (leaf) => new InspectorView(leaf, this)
        );

        this.addRibbonIcon('pencil', 'Open RPG Inspector', () => {
            this.activateView();
        });

        this.addCommand({
            id: 'open-inspector',
            name: 'Open Inspector',
            callback: () => {
                this.activateView();
            }
        });
        
        this.addCommand({
            id: 'reload-blueprints',
            name: 'Reload Blueprints',
            callback: async () => {
                await this.loadBlueprints();
            }
        });
    }

    async loadBlueprints() {
        const folder = this.app.vault.getAbstractFileByPath('_Engine/Blueprints');
        if (!folder) return;

        this.blueprints.clear(); // Clear before reload

        // @ts-ignore
        if (folder.children) {
             // @ts-ignore
            for (const file of folder.children) {
                if (file instanceof TFile && file.extension === 'md') {
                    const cache = this.app.metadataCache.getFileCache(file);
                    if (cache && cache.frontmatter) {
                        if (cache.frontmatter.name && cache.frontmatter.properties) {
                            const bp = cache.frontmatter as unknown as BlueprintDefinition;
                            this.blueprints.set(bp.name, bp);
                        }
                    }
                }
            }
        }
        console.log(`RPG Engine: ${this.blueprints.size} blueprints loaded.`);
    }

    async activateView() {
        const { workspace } = this.app;
        let leaf: WorkspaceLeaf | null = null;
        const leaves = workspace.getLeavesOfType(VIEW_TYPE_INSPECTOR);

        if (leaves.length > 0) {
            leaf = leaves[0];
        } else {
            const rightLeaf = workspace.getRightLeaf(false);
            if (rightLeaf) {
                 leaf = rightLeaf;
                 await leaf.setViewState({ type: VIEW_TYPE_INSPECTOR, active: true });
            }
        }
        if (leaf) workspace.revealLeaf(leaf);
    }

    onunload() { }
}
