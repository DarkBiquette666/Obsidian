import { App, TFile } from "obsidian";
import RPGEnginePlugin, { BlueprintDefinition } from "../main";

export class DataResolver {
    plugin: RPGEnginePlugin;
    app: App;

    constructor(plugin: RPGEnginePlugin) {
        this.plugin = plugin;
        this.app = plugin.app;
    }

    /**
     * Resolves the final data for a file by merging it with its parents (inheritance).
     */
    async resolveFile(file: TFile): Promise<any> {
        const cache = this.app.metadataCache.getFileCache(file);
        const data = cache?.frontmatter ? { ...cache.frontmatter } : {};
        
        // Identify Blueprint
        let blueprintName = data['Class'] || data['fileClass'];
        if (!blueprintName) return data; // No blueprint, raw data

        const blueprint = this.plugin.blueprints.get(blueprintName);
        if (!blueprint) return data;

        // Check for Parent Field defined in Blueprint
        // We look for a field of type 'link' that represents the parent (e.g. 'parent_race')
        // Convention: The field name might be defined in the blueprint, or we look for standard names
        // But better: look at the data. Is there a link to a parent?
        
        // Actually, we need to know WHICH field holds the parent link.
        // In SubRace blueprint, we have `parent_race`.
        // Let's hardcode a lookup or add 'is_parent: true' to the blueprint property later.
        // For now, let's look for common parent keys: 'parent_race', 'parent_class', 'parent'.
        
        let parentLink: string | null = null;
        if (data['parent_race']) parentLink = data['parent_race'];
        else if (data['parent_class']) parentLink = data['parent_class'];
        else if (data['parent']) parentLink = data['parent'];

        if (parentLink) {
            const parentPath = this.resolveLinkPath(parentLink, file.path);
            if (parentPath) {
                const parentFile = this.app.vault.getAbstractFileByPath(parentPath);
                if (parentFile instanceof TFile) {
                    const parentData = await this.resolveFile(parentFile); // Recursive !
                    return this.mergeData(parentData, data, blueprint);
                }
            }
        }

        return data;
    }

    private resolveLinkPath(link: string, sourcePath: string): string | null {
        // Extract [[Link]] or plain Link
        const cleanLink = link.replace(/\[\[|\]\]/g, "");
        const file = this.app.metadataCache.getFirstLinkpathDest(cleanLink, sourcePath);
        return file ? file.path : null;
    }

    private mergeData(parent: any, child: any, blueprint: BlueprintDefinition): any {
        const result = { ...parent };

        // Iterate over child keys to merge
        for (const key in child) {
            // Skip system keys
            if (key === 'Class' || key === 'fileClass' || key.startsWith('parent_')) {
                result[key] = child[key];
                continue;
            }

            const propDef = blueprint.properties[key] || this.getInheritedPropertyDef(blueprint, key);
            
            // If property is defined in blueprint and is array -> check merge strategy
            if (propDef && propDef.type === 'array') {
                const strategy = propDef.merge_strategy || 'append';
                
                if (strategy === 'append') {
                    // Append child items to parent items
                    const parentArray = Array.isArray(parent[key]) ? parent[key] : [];
                    const childArray = Array.isArray(child[key]) ? child[key] : [];
                    result[key] = [...parentArray, ...childArray];
                } else {
                    // Override
                    result[key] = child[key];
                }
            } else {
                // Simple Override for non-arrays
                result[key] = child[key];
            }
        }
        
        return result;
    }

    private getInheritedPropertyDef(bp: BlueprintDefinition, key: string): any {
        if (bp.properties[key]) return bp.properties[key];
        if (bp.extends) {
            const parentBp = this.plugin.blueprints.get(bp.extends);
            if (parentBp) return this.getInheritedPropertyDef(parentBp, key);
        }
        return null;
    }
}
