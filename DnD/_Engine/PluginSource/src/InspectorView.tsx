import { ItemView, WorkspaceLeaf, TFile, Notice, normalizePath, Modal, App } from "obsidian";
import * as React from "react";
import * as ReactDOM from "react-dom/client";
import RPGEnginePlugin, { BlueprintDefinition } from "../main";
import { LinkSuggest } from "./LinkSuggest";
import { DataResolver } from "./DataResolver";

export const VIEW_TYPE_INSPECTOR = "rpg-engine-inspector";

export class InspectorView extends ItemView {
    plugin: RPGEnginePlugin;
    root: ReactDOM.Root | null = null;
    resolver: DataResolver;

    constructor(leaf: WorkspaceLeaf, plugin: RPGEnginePlugin) {
        super(leaf);
        this.plugin = plugin;
        this.resolver = new DataResolver(plugin);
    }

    getViewType() { return VIEW_TYPE_INSPECTOR; }
    getDisplayText() { return "RPG Inspector"; }
    getIcon() { return "pencil"; }

    async onOpen() {
        const container = this.containerEl.children[1];
        container.empty();
        const reactRoot = container.createDiv();
        this.root = ReactDOM.createRoot(reactRoot);
        this.render();
        
        this.registerEvent(this.app.workspace.on('file-open', () => this.render()));
        this.registerEvent(this.app.metadataCache.on('changed', () => this.render()));
    }

    async onClose() { if (this.root) this.root.unmount(); }

    render() {
        const file = this.app.workspace.getActiveFile();
        if (!file) {
            this.root?.render(<div className="p-4">No file selected</div>);
            return;
        }
        const cache = this.app.metadataCache.getFileCache(file);
        let blueprintName = cache?.frontmatter?.['Class'] || cache?.frontmatter?.['fileClass'];
        if (!blueprintName) {
            this.root?.render(<BlueprintSetupView file={file} plugin={this.plugin} />);
            return;
        }
        const blueprint = this.plugin.blueprints.get(blueprintName);
        if (!blueprint) {
            this.root?.render(
                <div className="rpg-inspector">
                    <h3>Unknown Blueprint</h3>
                    <p>Blueprint <code>{blueprintName}</code> not found.</p>
                    <button onClick={() => this.plugin.app.fileManager.processFrontMatter(file, (fm: any) => { delete fm['Class']; delete fm['fileClass']; })}>Remove Class</button>
                </div>
            );
            return;
        }
        this.root?.render(<InspectorComponent file={file} blueprint={blueprint} plugin={this.plugin} frontmatter={cache?.frontmatter || {}} resolver={this.resolver} />);
    }
}

const BlueprintSetupView = ({ file, plugin }: { file: TFile, plugin: RPGEnginePlugin }) => {
    const [selected, setSelected] = React.useState("");
    const blueprints = Array.from(plugin.blueprints.keys()).sort();
    const handleAssign = async () => {
        if (!selected) return;
        await plugin.app.fileManager.processFrontMatter(file, (fm: any) => { fm['Class'] = selected; });
        new Notice("Assigned " + selected);
    };
    const handleCreateNew = async () => {
        const name = prompt("Enter new Blueprint name:");
        if (!name) return;
        const path = normalizePath("_Engine/Blueprints/" + name + ".md");
        try {
            await plugin.app.vault.create(path, "---\nname: " + name + "\nproperties:\n  description:\n    type: string\n    multiline: true\n---\n# Blueprint " + name + "\n");
            new Notice("Created Blueprint " + name);
            await plugin.loadBlueprints();
        } catch (e) { new Notice("Error: " + e); }
    };
    return (
        <div className="rpg-inspector" style={{textAlign: 'center', padding: '20px'}}>
            <h3>No Blueprint Attached</h3>
            <select value={selected} onChange={(e) => setSelected(e.target.value)} style={{width: '100%', marginBottom: '10px'}}>
                <option value="">-- Select --</option>
                {blueprints.map(bp => <option key={bp} value={bp}>{bp}</option>)}
            </select>
            <button className="mod-cta" onClick={handleAssign} disabled={!selected} style={{width: '100%'}}>Assign</button>
            <button onClick={handleCreateNew} style={{width: '100%', marginTop: '10px'}}>+ New Blueprint</button>
        </div>
    );
};

const InspectorComponent = ({ file, blueprint, plugin, frontmatter, resolver }: any) => {
    const getAllProps = (bpName: string): Record<string, any> => {
        const bp = plugin.blueprints.get(bpName);
        if (!bp) return {};
        let props = bp.properties || {};
        if (bp.extends) props = { ...getAllProps(bp.extends), ...props };
        return props;
    };

    const applyDefaults = (data: any, bpName: string) => {
        const props = getAllProps(bpName);
        Object.entries(props).forEach(([k, p]: [string, any]) => {
            if (data[k] === undefined) {
                if (p.default !== undefined) data[k] = p.default;
                else if (p.type === 'number') data[k] = 0;
                else if (p.type === 'boolean') data[k] = false;
                else if (p.type === 'string') data[k] = "";
                else if (p.type === 'array') data[k] = [];
            }
            if (p.type === 'array' && Array.isArray(data[k])) {
                data[k].forEach((item: any) => {
                    const itemBpName = item.type || p.item_type;
                    if (itemBpName && plugin.blueprints.has(itemBpName)) applyDefaults(item, itemBpName);
                });
            }
        });
    };

    const handleSync = async () => {
        await plugin.app.fileManager.processFrontMatter(file, (fm: any) => { applyDefaults(fm, blueprint.name); });
        new Notice("Synced defaults");
    };

    const handlePreview = async () => {
        const resolvedData = await resolver.resolveFile(file);
        const modal = new JSONModal(plugin.app, resolvedData);
        modal.open();
    };

    const updateProperty = async (path: string[], value: any) => {
        await plugin.app.fileManager.processFrontMatter(file, (fm: any) => {
            let current = fm;
            for (let i = 0; i < path.length - 1; i++) {
                if (!current[path[i]]) current[path[i]] = {};
                current = current[path[i]];
            }
            current[path[path.length - 1]] = value;
        });
    };

    return (
        <div className="rpg-inspector">
            <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--background-modifier-border)', paddingBottom: '8px'}}>
                <h2 style={{margin: 0}}>{blueprint.name}</h2>
                <div style={{display: 'flex', gap: '5px'}}>
                    <button style={{padding: '2px 6px', fontSize: '0.8em'}} onClick={handlePreview}>👁️ Preview</button>
                    <button style={{padding: '2px 6px', fontSize: '0.8em'}} onClick={handleSync}>Sync</button>
                    <button style={{padding: '2px 6px', fontSize: '0.8em'}} onClick={() => {
                        const bpFile = plugin.app.vault.getAbstractFileByPath("_Engine/Blueprints/" + blueprint.name + ".md");
                        if (bpFile instanceof TFile) plugin.app.workspace.getLeaf().openFile(bpFile);
                    }}>Edit</button>
                </div>
            </div>
            {Object.entries(getAllProps(blueprint.name)).map(([key, propDef]: [string, any]) => (
                <FieldRenderer key={key} label={key} propDef={propDef} value={frontmatter[key]} onChange={(val: any) => updateProperty([key], val)} plugin={plugin} />
            ))}
        </div>
    );
};

class JSONModal extends Modal {
    constructor(app: App, private data: any) { super(app); }
    onOpen() {
        const { contentEl } = this;
        contentEl.createEl('h2', { text: 'Resolved Data (Inherited)' });
        contentEl.createEl('pre', { text: JSON.stringify(this.data, null, 2) });
    }
    onClose() { this.contentEl.empty(); }
}

const LinkAutocompleteField = ({ value, onChange, plugin, targetFolder, filterTag, placeholder }: any) => {
    const inputRef = React.useRef<HTMLInputElement>(null);
    React.useEffect(() => {
        if (inputRef.current) new LinkSuggest(plugin.app, inputRef.current, targetFolder || "", filterTag);
    }, [plugin.app, targetFolder, filterTag]);
    return <input ref={inputRef} type="text" value={value || ''} onChange={(e) => onChange(e.target.value)} placeholder={placeholder || "[[Note]]"} />;
};

const FieldRenderer = ({ label, propDef, value, onChange, plugin }: any) => {
    if (propDef.type === 'link') return (
        <div className="rpg-field-group">
            <label>{label}</label>
            <LinkAutocompleteField 
                value={value} 
                onChange={onChange} 
                plugin={plugin} 
                targetFolder={propDef.target_folder}
                filterTag={propDef.filter_tag}
                placeholder={propDef.default || "[[Note]]"} 
            />
        </div>
    );
    if (propDef.type === 'select') return (
        <div className="rpg-field-group">
            <label>{label}</label>
            <select value={value || propDef.default || ''} onChange={(e) => onChange(e.target.value)} style={{width: '100%', background: 'var(--background-modifier-form-field)'}}>
                {(propDef.options || []).map((opt: string) => <option key={opt} value={opt}>{opt}</option>)}
            </select>
        </div>
    );
    if (propDef.type === 'string') return (
        <div className="rpg-field-group">
            <label>{label}</label>
            {propDef.multiline ? <textarea value={value || ''} onChange={(e) => onChange(e.target.value)} style={{minHeight: '80px'}} /> : <input type="text" value={value || ''} onChange={(e) => onChange(e.target.value)} />}
        </div>
    );
    if (propDef.type === 'number') return (
        <div className="rpg-field-group">
            <label>{label}</label>
            <input type="number" value={value === undefined ? (propDef.default ?? 0) : value} onChange={(e) => onChange(parseFloat(e.target.value))} />
        </div>
    );
    if (propDef.type === 'boolean') return (
        <div className="rpg-field-group" style={{flexDirection: 'row', alignItems: 'center', gap: '8px'}}>
            <input type="checkbox" checked={value === undefined ? (propDef.default ?? false) : value} onChange={(e) => onChange(e.target.checked)} />
            <label style={{marginBottom: 0}}>{label}</label>
        </div>
    );
    if (propDef.type === 'array') {
        const items = Array.isArray(value) ? value : [];
        const itemType = propDef.item_type;
        const availableTypes: any[] = [];
        plugin.blueprints.forEach((bp: any) => { if (bp.extends === itemType || bp.name === itemType) if (!bp.is_abstract) availableTypes.push(bp); });

        const handleAdd = (typeName: string) => {
            let newItem: any;
            const bp = plugin.blueprints.get(typeName);
            if (bp) {
                newItem = { type: typeName };
                const getProps = (n: string): any => {
                    const s = plugin.blueprints.get(n); if (!s) return {};
                    return { ...(s.extends ? getProps(s.extends) : {}), ...s.properties };
                };
                Object.entries(getProps(typeName)).forEach(([k, p]: [string, any]) => {
                    if (k !== 'type') {
                        if (p.default !== undefined) newItem[k] = p.default;
                        else if (p.type === 'number') newItem[k] = 0;
                        else if (p.type === 'boolean') newItem[k] = false;
                        else if (p.type === 'string') newItem[k] = "";
                    }
                });
            } else {
                if (typeName === 'number') newItem = 0;
                else if (typeName === 'boolean') newItem = false;
                else newItem = "";
            }
            onChange([...items, newItem]);
        };

        return (
            <div className="rpg-array-container">
                <div className="rpg-array-header"><b>{label}</b> <span>{items.length} items</span></div>
                <div className="rpg-array-items">
                    {items.map((item: any, idx: number) => {
                        const itName = item.type || itemType;
                        const itBp = plugin.blueprints.get(itName);
                        return (
                            <div key={idx} className="rpg-item-card">
                                <button className="rpg-item-remove-btn" onClick={() => { const n = [...items]; n.splice(idx, 1); onChange(n); }}>✕</button>
                                {itBp ? <> <div className="item-type-label">{itBp.name}</div> <ObjectRenderer blueprint={itBp} value={item} onChange={(v: any) => { const n = [...items]; n[idx] = v; onChange(n); }} plugin={plugin} /> </>
                                      : <FieldRenderer label={`Item ${idx + 1}`} propDef={{ ...propDef, type: itemType || 'string' }} value={item} onChange={(v: any) => { const n = [...items]; n[idx] = v; onChange(n); }} plugin={plugin} />}
                            </div>
                        );
                    })}
                </div>
                <div className="rpg-add-buttons">
                    {availableTypes.length > 0 ? availableTypes.map(bp => <button key={bp.name} onClick={() => handleAdd(bp.name)}>+ {bp.name}</button>) : <button onClick={() => handleAdd(itemType || 'string')}>+ Add Item</button>}
                </div>
            </div>
        );
    }
    return <div>Unknown type: {propDef.type}</div>;
};

const ObjectRenderer = ({ blueprint, value, onChange, plugin }: any) => {
    const getProps = (n: string): any => {
        const s = plugin.blueprints.get(n); if (!s) return {};
        return { ...(s.extends ? getProps(s.extends) : {}), ...s.properties };
    };
    return (
        <div style={{display: 'flex', flexDirection: 'column', gap: '12px'}}>
            {Object.entries(getProps(blueprint.name)).map(([key, propDef]: [string, any]) => {
                if (key === 'type') return null;
                return <FieldRenderer key={key} label={key} propDef={propDef} value={value?.[key]} onChange={(newVal: any) => onChange({ ...value, [key]: newVal })} plugin={plugin} />;
            })}
        </div>
    );
};
