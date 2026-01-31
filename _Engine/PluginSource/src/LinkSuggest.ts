import { AbstractInputSuggest, App, TFile } from "obsidian";

export class LinkSuggest extends AbstractInputSuggest<TFile> {
    private textInputEl: HTMLInputElement;

    constructor(
        app: App, 
        inputEl: HTMLInputElement, 
        private targetFolder: string,
        private filterTag?: string
    ) {
        super(app, inputEl);
        this.textInputEl = inputEl;
    }

    getSuggestions(query: string): TFile[] {
        const files = this.app.vault.getMarkdownFiles();
        const lowerQuery = query.toLowerCase().replace('[[', '').replace(']]', '');

        const filtered = files.filter(file => {
            // Folder check
            if (this.targetFolder && !file.path.startsWith(this.targetFolder)) {
                return false;
            }

            // Tag check
            if (this.filterTag) {
                const cache = this.app.metadataCache.getFileCache(file);
                const tags = cache?.tags?.map(t => t.tag) || [];
                const frontmatterTags = cache?.frontmatter?.tags || [];
                const allTags = [...tags, ...(Array.isArray(frontmatterTags) ? frontmatterTags : [])];
                const hasTag = allTags.some(t => t.toString().toLowerCase().includes(this.filterTag!.toLowerCase()));
                if (!hasTag) return false;
            }

            // Text search
            return file.basename.toLowerCase().includes(lowerQuery);
        });

        // Sort alphabetically by name
        filtered.sort((a, b) => a.basename.localeCompare(b.basename));

        // Limit results
        return filtered.slice(0, 1000); 
    }

    renderSuggestion(file: TFile, el: HTMLElement): void {
        el.setText(file.basename);
    }

    selectSuggestion(file: TFile): void {
        const newValue = `[[${file.basename}]]`;
        
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value")?.set;
        nativeInputValueSetter?.call(this.textInputEl, newValue);
        
        const event = new Event('input', { bubbles: true });
        this.textInputEl.dispatchEvent(event);
        
        this.close();
    }
}
