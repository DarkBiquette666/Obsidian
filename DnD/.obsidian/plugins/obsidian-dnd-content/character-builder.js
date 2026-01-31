// ========================================
// D&D CHARACTER BUILDER - Style BG3
// ========================================

const { ItemView, Modal, Notice, parseYaml, stringifyYaml } = require('obsidian');

const VIEW_TYPE_CHARACTER_BUILDER = 'dnd-character-builder';

// ========================================
// CHARACTER DATA MODEL
// ========================================

class CharacterData {
	constructor() {
		// Identite
		this.name = '';
		this.race = null;        // { name, subrace, traits, augmentations, vitesse, langues }
		this.background = null;  // { name, skills, languages, tools, equipment, feature }
		this.alignment = 'Neutre';

		// Stats de base (avant racial)
		this.baseStats = { for: 10, dex: 10, con: 10, int: 10, sag: 10, cha: 10 };
		this.statMethod = 'standard'; // 'standard', 'pointbuy', '4d6', 'manual'

		// Progression multi-classe
		this.levels = []; // Array de { class: 'Guerrier', subclass: null, choices: {} }

		// Selections
		this.spellsKnown = [];      // [{ name, level, prepared }]
		this.equipment = [];         // [{ name, quantity, equipped }]
		this.feats = [];             // [{ name, source, level }]
		this.proficiencies = {
			skills: [],
			savingThrows: [],
			armor: [],
			weapons: [],
			tools: [],
			languages: ['Commun']
		};

		// Ressources
		this.money = { pp: 0, po: 0, pe: 0, pa: 0, pc: 0 };
		this.hitDiceUsed = 0;

		// Roleplay
		this.traits = '';
		this.ideals = '';
		this.bonds = '';
		this.flaws = '';
		this.backstory = '';
		this.appearance = { age: '', height: '', weight: '', eyes: '', hair: '', skin: '', description: '' };
	}

	// Getters calcules
	get totalLevel() {
		return this.levels.length;
	}

	get classes() {
		const counts = {};
		for (const level of this.levels) {
			counts[level.class] = (counts[level.class] || 0) + 1;
		}
		return counts;
	}

	get primaryClass() {
		return this.levels[0]?.class || null;
	}

	get proficiencyBonus() {
		return Math.ceil(this.totalLevel / 4) + 1;
	}

	// Stats finales (base + racial)
	getFinalStats() {
		const final = { ...this.baseStats };
		if (this.race?.augmentations) {
			for (const [stat, bonus] of Object.entries(this.race.augmentations)) {
				if (final[stat] !== undefined && typeof bonus === 'number') {
					final[stat] += bonus;
				}
			}
		}
		// Ajouter les ASI des niveaux
		for (const level of this.levels) {
			if (level.choices?.asi) {
				for (const [stat, bonus] of Object.entries(level.choices.asi)) {
					if (final[stat] !== undefined) {
						final[stat] += bonus;
					}
				}
			}
		}
		return final;
	}

	getModifier(stat) {
		const stats = this.getFinalStats();
		return Math.floor((stats[stat] - 10) / 2);
	}

	// Calculs derives
	getMaxHP(classData) {
		if (this.levels.length === 0) return 0;

		const conMod = this.getModifier('con');
		let hp = 0;

		for (let i = 0; i < this.levels.length; i++) {
			const level = this.levels[i];
			const classInfo = classData[level.class];
			const hitDie = parseInt(classInfo?.des_de_vie?.replace('d', '')) || 8;

			if (i === 0) {
				// Niveau 1: max du de
				hp = hitDie + conMod;
			} else {
				// Niveaux suivants: moyenne arrondie
				hp += Math.floor(hitDie / 2) + 1 + conMod;
			}
		}

		return Math.max(hp, 1);
	}

	getAC() {
		// CA de base sans armure
		return 10 + this.getModifier('dex');
	}

	getInitiative() {
		return this.getModifier('dex');
	}

	getSpeed() {
		return this.race?.vitesse || 9; // 9m par defaut
	}

	getPassivePerception() {
		const sagMod = this.getModifier('sag');
		const hasPerception = this.proficiencies.skills.includes('Perception');
		return 10 + sagMod + (hasPerception ? this.proficiencyBonus : 0);
	}

	// Export vers YAML
	toYaml(classData) {
		const stats = this.getFinalStats();
		return {
			name: this.name,
			race: this.race?.name || '',
			sous_race: this.race?.subrace || '',
			classes: this.classes,
			classe: this.primaryClass,
			niveau: this.totalLevel,
			historique: this.background?.name || '',
			alignement: this.alignment,
			for: stats.for,
			dex: stats.dex,
			con: stats.con,
			int: stats.int,
			sag: stats.sag,
			cha: stats.cha,
			pv_max: this.getMaxHP(classData),
			pv_actuels: this.getMaxHP(classData),
			ca: this.getAC(),
			vitesse: this.getSpeed(),
			initiative: this.getInitiative(),
			perception_passive: this.getPassivePerception(),
			bonus_maitrise: this.proficiencyBonus,
			sauvegardes: this.proficiencies.savingThrows,
			competences: this.proficiencies.skills.map(s => ({ name: s, maitrise: true })),
			langues: this.proficiencies.languages,
			outils: this.proficiencies.tools,
			armes: this.proficiencies.weapons,
			armures: this.proficiencies.armor,
			sorts_connus: this.spellsKnown.map(s => s.name),
			equipement: this.equipment,
			argent: this.money,
			dons: this.feats.map(f => f.name),
			traits_personnalite: this.traits,
			ideaux: this.ideals,
			liens: this.bonds,
			defauts: this.flaws,
			backstory: this.backstory,
			apparence: this.appearance
		};
	}
}

// ========================================
// VAULT DATA LOADER
// ========================================

class VaultDataLoader {
	static async load(app) {
		console.log('[DnD Builder] Chargement des donnees du vault...');
		return {
			races: await this.loadRaces(app),
			classes: await this.loadClasses(app),
			backgrounds: await this.loadBackgrounds(app),
			spells: await this.loadSpells(app),
			equipment: await this.loadEquipment(app),
			feats: await this.loadFeats(app)
		};
	}

	static async loadRaces(app) {
		const races = {};
		const files = app.vault.getFiles().filter(f =>
			f.path.startsWith('Glossary/Races/') && f.extension === 'md'
		);

		for (const file of files) {
			try {
				const content = await app.vault.read(file);
				const parsed = this.parseRaceBlock(content);
				if (parsed) {
					races[file.basename] = parsed;
				}
			} catch (e) {
				console.warn(`[DnD Builder] Erreur lecture race ${file.basename}:`, e);
			}
		}

		console.log(`[DnD Builder] ${Object.keys(races).length} races chargees`);
		return races;
	}

	static parseRaceBlock(content) {
		const match = content.match(/```dnd-race\r?\n([\s\S]*?)\r?\n```/);
		if (!match) return null;

		try {
			const data = parseYaml(match[1]);
			return {
				name: data.name,
				augmentations: data.augmentations || {},
				vitesse: this.parseSpeed(data.vitesse),
				taille: data.taille,
				langues: data.langues || [],
				traits: data.traits || [],
				sous_races: data.sous_races || []
			};
		} catch (e) {
			return null;
		}
	}

	static parseSpeed(vitesse) {
		if (typeof vitesse === 'number') return vitesse;
		if (typeof vitesse === 'string') {
			const match = vitesse.match(/(\d+)/);
			return match ? parseInt(match[1]) : 9;
		}
		return 9;
	}

	static async loadClasses(app) {
		const classes = {};
		const files = app.vault.getFiles().filter(f =>
			f.path.startsWith('Glossary/Classes/') && f.extension === 'md'
		);

		for (const file of files) {
			try {
				const content = await app.vault.read(file);
				const parsed = this.parseClassBlock(content);
				if (parsed) {
					classes[file.basename] = parsed;
				}
			} catch (e) {
				console.warn(`[DnD Builder] Erreur lecture classe ${file.basename}:`, e);
			}
		}

		console.log(`[DnD Builder] ${Object.keys(classes).length} classes chargees`);
		return classes;
	}

	static parseClassBlock(content) {
		const match = content.match(/```dnd-classe\r?\n([\s\S]*?)\r?\n```/);
		if (!match) return null;

		try {
			const data = parseYaml(match[1]);
			return {
				name: data.name,
				des_de_vie: data.des_de_vie,
				pv_niveau_1: data.pv_niveau_1,
				maitrises: data.maitrises || {},
				capacites: data.capacites || [],
				source: data.source
			};
		} catch (e) {
			return null;
		}
	}

	static async loadBackgrounds(app) {
		const backgrounds = {};
		const files = app.vault.getFiles().filter(f =>
			f.path.startsWith('Glossary/Historique/') && f.extension === 'md'
		);

		for (const file of files) {
			try {
				const content = await app.vault.read(file);
				const parsed = this.parseBackgroundContent(content, file.basename);
				if (parsed) {
					backgrounds[file.basename] = parsed;
				}
			} catch (e) {
				console.warn(`[DnD Builder] Erreur lecture historique ${file.basename}:`, e);
			}
		}

		console.log(`[DnD Builder] ${Object.keys(backgrounds).length} historiques charges`);
		return backgrounds;
	}

	static parseBackgroundContent(content, basename) {
		const afterFrontmatter = content.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, '');

		// Extraire competences
		const skillsMatch = afterFrontmatter.match(/\*\*Comp[ée]tences ma[îi]tris[ée]es?\s*[:\*]*\s*\*?\*?\s*:?\s*([^\n*]+)/i);
		const skills = skillsMatch ? skillsMatch[1].split(/[,;]/).map(s => s.trim()).filter(s => s) : [];

		// Extraire langues
		const langMatch = afterFrontmatter.match(/\*\*Langues?\s*[:\*]*\s*\*?\*?\s*:?\s*([^\n*]+)/i);
		const languages = langMatch ? langMatch[1] : '';

		// Extraire outils
		const toolsMatch = afterFrontmatter.match(/\*\*Outils? ma[îi]tris[ée]s?\s*[:\*]*\s*\*?\*?\s*:?\s*([^\n*]+)/i);
		const tools = toolsMatch ? toolsMatch[1].split(/[,;]/).map(s => s.trim()).filter(s => s) : [];

		// Extraire equipement
		const equipMatch = afterFrontmatter.match(/\*\*[ÉE]quipement\s*[:\*]*\s*\*?\*?\s*:?\s*([^\n]+)/i);
		const equipment = equipMatch ? equipMatch[1] : '';

		return {
			name: basename,
			skills,
			languages,
			tools,
			equipment
		};
	}

	static async loadSpells(app) {
		const spells = [];
		const files = app.vault.getFiles().filter(f =>
			f.path.startsWith('Glossary/Liste des Sorts/') && f.extension === 'md'
		);

		for (const file of files) {
			try {
				const content = await app.vault.read(file);
				const parsed = this.parseSpellFrontmatter(content, file.basename);
				if (parsed) {
					spells.push(parsed);
				}
			} catch (e) {
				// Ignore silencieusement
			}
		}

		console.log(`[DnD Builder] ${spells.length} sorts charges`);
		return spells;
	}

	static parseSpellFrontmatter(content, basename) {
		const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
		if (!fmMatch) return null;

		try {
			const fm = parseYaml(fmMatch[1]);
			return {
				name: basename,
				niveau: fm.Niveau ?? fm.niveau ?? 0,
				ecole: fm.Ecole || fm.ecole || '',
				temps: fm['Temps d\'incantation'] || fm.temps || '',
				duree: fm['Durée'] || fm.duree || '',
				portee: fm['Portée'] || fm.portee || '',
				composantes: fm.Composante || fm.composantes || '',
				rituel: fm.Rituel || fm.rituel || false,
				concentration: (fm['Durée'] || '').toLowerCase().includes('concentration')
			};
		} catch (e) {
			return null;
		}
	}

	static async loadEquipment(app) {
		const equipment = [];

		// Charger armes
		const weaponFiles = app.vault.getFiles().filter(f =>
			f.path.includes('Glossary/Objets/Equipmement/Armes/') && f.extension === 'md'
		);

		for (const file of weaponFiles) {
			try {
				const content = await app.vault.read(file);
				const parsed = this.parseEquipmentFrontmatter(content, file.basename, 'arme');
				if (parsed) equipment.push(parsed);
			} catch (e) {}
		}

		// Charger armures
		const armorFiles = app.vault.getFiles().filter(f =>
			f.path.includes('Glossary/Objets/Equipmement/Armures/') && f.extension === 'md'
		);

		for (const file of armorFiles) {
			try {
				const content = await app.vault.read(file);
				const parsed = this.parseEquipmentFrontmatter(content, file.basename, 'armure');
				if (parsed) equipment.push(parsed);
			} catch (e) {}
		}

		console.log(`[DnD Builder] ${equipment.length} equipements charges`);
		return equipment;
	}

	static parseEquipmentFrontmatter(content, basename, type) {
		const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
		if (!fmMatch) return null;

		try {
			const fm = parseYaml(fmMatch[1]);
			return {
				name: fm.Nom || basename,
				type,
				categorie: fm.Categorie || '',
				degats: fm.Degats || '',
				ca: fm.CA || '',
				prix: fm.Prix || '',
				poids: fm.Poids || 0,
				proprietes: fm.Proprietes || []
			};
		} catch (e) {
			return null;
		}
	}

	static async loadFeats(app) {
		const feats = [];
		const files = app.vault.getFiles().filter(f =>
			f.path.startsWith('Glossary/Dons/') && f.extension === 'md'
		);

		for (const file of files) {
			feats.push({
				name: file.basename,
				path: file.path
			});
		}

		console.log(`[DnD Builder] ${feats.length} dons charges`);
		return feats;
	}
}

// ========================================
// LIVE SHEET RENDERER
// ========================================

class LiveSheetRenderer {
	constructor(container, character, vaultData) {
		this.container = container;
		this.character = character;
		this.vaultData = vaultData;
	}

	render() {
		this.container.empty();
		this.container.addClass('dnd-live-sheet');

		this.renderHeader();
		this.renderStats();
		this.renderCombat();
		this.renderProficiencies();
		this.renderSkills();
		this.renderSpells();
	}

	renderHeader() {
		const header = this.container.createDiv({ cls: 'dnd-sheet-header' });
		header.createEl('h2', { text: this.character.name || '???' });

		const subtitle = [];
		if (this.character.race?.name) subtitle.push(this.character.race.name);
		if (this.character.race?.subrace) subtitle.push(`(${this.character.race.subrace})`);

		const classes = this.character.classes;
		if (Object.keys(classes).length > 0) {
			const classStr = Object.entries(classes).map(([c, l]) => `${c} ${l}`).join(' / ');
			subtitle.push(classStr);
		}

		if (subtitle.length > 0) {
			header.createEl('p', { text: subtitle.join(' '), cls: 'dnd-sheet-subtitle' });
		}

		if (this.character.background?.name) {
			header.createEl('p', { text: `Historique: ${this.character.background.name}`, cls: 'dnd-sheet-bg' });
		}
	}

	renderStats() {
		const section = this.container.createDiv({ cls: 'dnd-sheet-section' });
		section.createEl('h4', { text: 'Caracteristiques' });

		const grid = section.createDiv({ cls: 'dnd-stats-grid' });
		const stats = ['for', 'dex', 'con', 'int', 'sag', 'cha'];
		const labels = { for: 'FOR', dex: 'DEX', con: 'CON', int: 'INT', sag: 'SAG', cha: 'CHA' };
		const finalStats = this.character.getFinalStats();

		for (const stat of stats) {
			const val = finalStats[stat] || 10;
			const mod = Math.floor((val - 10) / 2);

			const cell = grid.createDiv({ cls: 'dnd-stat-cell' });
			cell.createEl('div', { text: labels[stat], cls: 'dnd-stat-label' });
			cell.createEl('div', { text: `${val}`, cls: 'dnd-stat-value' });
			cell.createEl('div', { text: mod >= 0 ? `+${mod}` : `${mod}`, cls: 'dnd-stat-mod' });
		}
	}

	renderCombat() {
		const section = this.container.createDiv({ cls: 'dnd-sheet-section' });
		section.createEl('h4', { text: 'Combat' });

		const grid = section.createDiv({ cls: 'dnd-combat-grid' });

		const maxHP = this.character.getMaxHP(this.vaultData.classes);
		const ac = this.character.getAC();
		const init = this.character.getInitiative();
		const speed = this.character.getSpeed();
		const profBonus = this.character.proficiencyBonus;

		const items = [
			{ label: 'CA', value: ac },
			{ label: 'PV', value: maxHP },
			{ label: 'Init', value: init >= 0 ? `+${init}` : init },
			{ label: 'Vitesse', value: `${speed}m` },
			{ label: 'Maitrise', value: `+${profBonus}` },
			{ label: 'Perception', value: this.character.getPassivePerception() }
		];

		for (const item of items) {
			const cell = grid.createDiv({ cls: 'dnd-combat-cell' });
			cell.createEl('span', { text: item.label, cls: 'dnd-combat-label' });
			cell.createEl('span', { text: `${item.value}`, cls: 'dnd-combat-value' });
		}
	}

	renderProficiencies() {
		const section = this.container.createDiv({ cls: 'dnd-sheet-section' });
		section.createEl('h4', { text: 'Maitrises' });

		const profs = this.character.proficiencies;

		if (profs.savingThrows.length > 0) {
			section.createEl('p').innerHTML = `<strong>Sauvegardes:</strong> ${profs.savingThrows.join(', ')}`;
		}
		if (profs.armor.length > 0) {
			section.createEl('p').innerHTML = `<strong>Armures:</strong> ${profs.armor.join(', ')}`;
		}
		if (profs.weapons.length > 0) {
			section.createEl('p').innerHTML = `<strong>Armes:</strong> ${profs.weapons.join(', ')}`;
		}
		if (profs.tools.length > 0) {
			section.createEl('p').innerHTML = `<strong>Outils:</strong> ${profs.tools.join(', ')}`;
		}
		if (profs.languages.length > 0) {
			section.createEl('p').innerHTML = `<strong>Langues:</strong> ${profs.languages.join(', ')}`;
		}
	}

	renderSkills() {
		if (this.character.proficiencies.skills.length === 0) return;

		const section = this.container.createDiv({ cls: 'dnd-sheet-section' });
		section.createEl('h4', { text: 'Competences' });

		const list = section.createDiv({ cls: 'dnd-skills-list' });
		const skillStats = {
			'Acrobaties': 'dex', 'Arcanes': 'int', 'Athletisme': 'for',
			'Discretion': 'dex', 'Dressage': 'sag', 'Escamotage': 'dex',
			'Histoire': 'int', 'Intimidation': 'cha', 'Investigation': 'int',
			'Medecine': 'sag', 'Nature': 'int', 'Perception': 'sag',
			'Perspicacite': 'sag', 'Persuasion': 'cha', 'Religion': 'int',
			'Representation': 'cha', 'Survie': 'sag', 'Tromperie': 'cha'
		};

		for (const skill of this.character.proficiencies.skills) {
			const stat = skillStats[skill] || 'int';
			const mod = this.character.getModifier(stat);
			const bonus = mod + this.character.proficiencyBonus;

			const line = list.createDiv({ cls: 'dnd-skill-line' });
			line.createEl('span', { text: bonus >= 0 ? `+${bonus}` : `${bonus}`, cls: 'dnd-skill-bonus' });
			line.createEl('span', { text: skill });
		}
	}

	renderSpells() {
		if (this.character.spellsKnown.length === 0) return;

		const section = this.container.createDiv({ cls: 'dnd-sheet-section' });
		section.createEl('h4', { text: `Sorts (${this.character.spellsKnown.length})` });

		const list = section.createEl('ul', { cls: 'dnd-spells-list' });
		for (const spell of this.character.spellsKnown) {
			list.createEl('li', { text: spell.name });
		}
	}
}

// ========================================
// CHARACTER BUILDER VIEW
// ========================================

class CharacterBuilderView extends ItemView {
	constructor(leaf, plugin) {
		super(leaf);
		this.plugin = plugin;
		this.character = new CharacterData();
		this.vaultData = null;
		this.currentTab = 'base';
	}

	getViewType() {
		return VIEW_TYPE_CHARACTER_BUILDER;
	}

	getDisplayText() {
		return 'D&D Character Builder';
	}

	getIcon() {
		return 'sword';
	}

	async onOpen() {
		const container = this.containerEl.children[1];
		container.empty();
		container.addClass('dnd-builder-container');

		// Afficher chargement
		container.createEl('p', { text: 'Chargement des donnees...' });

		// Charger les donnees du vault
		this.vaultData = await VaultDataLoader.load(this.app);

		// Rendre l'interface
		this.render();
	}

	render() {
		const container = this.containerEl.children[1];
		container.empty();
		container.addClass('dnd-builder-container');

		// Layout split: formulaire | fiche
		const mainLayout = container.createDiv({ cls: 'dnd-builder-main' });
		const formPanel = mainLayout.createDiv({ cls: 'dnd-builder-form' });
		const sheetPanel = mainLayout.createDiv({ cls: 'dnd-builder-sheet' });

		// Formulaire avec onglets
		this.renderTabs(formPanel);
		this.renderCurrentTab(formPanel);
		this.renderActions(formPanel);

		// Fiche live
		const sheetRenderer = new LiveSheetRenderer(sheetPanel, this.character, this.vaultData);
		sheetRenderer.render();
	}

	renderTabs(container) {
		const tabs = container.createDiv({ cls: 'dnd-builder-tabs' });
		const tabList = [
			{ id: 'base', label: 'Base' },
			{ id: 'levels', label: 'Niveaux' },
			{ id: 'spells', label: 'Sorts' },
			{ id: 'equipment', label: 'Equipement' },
			{ id: 'roleplay', label: 'Roleplay' }
		];

		for (const tab of tabList) {
			const tabBtn = tabs.createEl('button', {
				text: tab.label,
				cls: `dnd-tab-btn ${this.currentTab === tab.id ? 'active' : ''}`
			});
			tabBtn.onclick = () => {
				this.currentTab = tab.id;
				this.render();
			};
		}
	}

	renderCurrentTab(container) {
		const content = container.createDiv({ cls: 'dnd-builder-content' });

		switch (this.currentTab) {
			case 'base':
				this.renderBaseTab(content);
				break;
			case 'levels':
				this.renderLevelsTab(content);
				break;
			case 'spells':
				this.renderSpellsTab(content);
				break;
			case 'equipment':
				this.renderEquipmentTab(content);
				break;
			case 'roleplay':
				this.renderRoleplayTab(content);
				break;
		}
	}

	// ========================================
	// ONGLET BASE
	// ========================================

	renderBaseTab(container) {
		container.createEl('h3', { text: 'Identite du Personnage' });

		// Nom
		this.createTextInput(container, 'Nom', this.character.name, (v) => {
			this.character.name = v;
			this.updateSheet();
		});

		// Race
		const raceOptions = ['', ...Object.keys(this.vaultData.races)];
		this.createDropdown(container, 'Race', raceOptions, this.character.race?.name || '', (v) => {
			if (v) {
				this.character.race = { ...this.vaultData.races[v], name: v };
			} else {
				this.character.race = null;
			}
			this.updateSheet();
		});

		// Sous-race (si disponible)
		if (this.character.race?.sous_races?.length > 0) {
			const subOptions = ['', ...this.character.race.sous_races.map(sr => sr.name)];
			this.createDropdown(container, 'Sous-race', subOptions, this.character.race.subrace || '', (v) => {
				this.character.race.subrace = v;
				// Appliquer les bonus de sous-race
				const subrace = this.character.race.sous_races.find(sr => sr.name === v);
				if (subrace?.augmentations) {
					this.character.race.augmentations = {
						...this.vaultData.races[this.character.race.name]?.augmentations,
						...subrace.augmentations
					};
				}
				this.updateSheet();
			});
		}

		// Classe (niveau 1)
		const classOptions = ['', ...Object.keys(this.vaultData.classes)];
		this.createDropdown(container, 'Classe', classOptions, this.character.primaryClass || '', (v) => {
			if (v && this.character.levels.length === 0) {
				this.character.levels.push({ class: v, subclass: null, choices: {} });
				this.applyClassProficiencies(v, true);
			} else if (v && this.character.levels.length > 0) {
				const oldClass = this.character.levels[0].class;
				this.character.levels[0].class = v;
				if (oldClass !== v) {
					this.applyClassProficiencies(v, true);
				}
			} else if (!v) {
				this.character.levels = [];
			}
			this.updateSheet();
		});

		// Historique
		const bgOptions = ['', ...Object.keys(this.vaultData.backgrounds)];
		this.createDropdown(container, 'Historique', bgOptions, this.character.background?.name || '', (v) => {
			if (v) {
				this.character.background = { ...this.vaultData.backgrounds[v], name: v };
				// Ajouter les competences de l'historique
				for (const skill of this.character.background.skills || []) {
					if (!this.character.proficiencies.skills.includes(skill)) {
						this.character.proficiencies.skills.push(skill);
					}
				}
			} else {
				this.character.background = null;
			}
			this.updateSheet();
		});

		// Alignement
		const alignments = [
			'Loyal Bon', 'Neutre Bon', 'Chaotique Bon',
			'Loyal Neutre', 'Neutre', 'Chaotique Neutre',
			'Loyal Mauvais', 'Neutre Mauvais', 'Chaotique Mauvais'
		];
		this.createDropdown(container, 'Alignement', alignments, this.character.alignment, (v) => {
			this.character.alignment = v;
			this.updateSheet();
		});

		// Methode de stats
		container.createEl('h4', { text: 'Caracteristiques' });

		const methods = [
			{ id: 'standard', label: 'Standard Array (15,14,13,12,10,8)' },
			{ id: 'pointbuy', label: 'Point Buy (27 points)' },
			{ id: 'manual', label: 'Manuel' }
		];
		this.createDropdown(container, 'Methode', methods.map(m => m.label),
			methods.find(m => m.id === this.character.statMethod)?.label || methods[0].label,
			(v) => {
				const method = methods.find(m => m.label === v);
				this.character.statMethod = method?.id || 'manual';
				if (this.character.statMethod === 'standard') {
					this.applyStandardArray();
				}
				this.render();
			}
		);

		// Afficher les stats selon la methode
		this.renderStatInputs(container);
	}

	applyStandardArray() {
		// Standard array a assigner
		this.character.baseStats = { for: 15, dex: 14, con: 13, int: 12, sag: 10, cha: 8 };
	}

	renderStatInputs(container) {
		const statsDiv = container.createDiv({ cls: 'dnd-stats-inputs' });
		const stats = ['for', 'dex', 'con', 'int', 'sag', 'cha'];
		const labels = { for: 'Force', dex: 'Dexterite', con: 'Constitution', int: 'Intelligence', sag: 'Sagesse', cha: 'Charisme' };

		for (const stat of stats) {
			const row = statsDiv.createDiv({ cls: 'dnd-stat-input-row' });
			row.createEl('label', { text: labels[stat] });

			const input = row.createEl('input', {
				type: 'number',
				attr: { min: 1, max: 30, value: this.character.baseStats[stat] }
			});
			input.onchange = (e) => {
				this.character.baseStats[stat] = parseInt(e.target.value) || 10;
				this.updateSheet();
			};

			// Afficher le bonus racial
			const racialBonus = this.character.race?.augmentations?.[stat] || 0;
			if (racialBonus > 0) {
				row.createEl('span', { text: `+${racialBonus}`, cls: 'dnd-racial-bonus' });
			}
		}
	}

	applyClassProficiencies(className, isFirstLevel) {
		const classInfo = this.vaultData.classes[className];
		if (!classInfo?.maitrises) return;

		const m = classInfo.maitrises;

		if (isFirstLevel) {
			// Sauvegardes
			if (m.sauvegardes) {
				this.character.proficiencies.savingThrows = [...m.sauvegardes];
			}
			// Armures
			if (m.armures) {
				this.character.proficiencies.armor = [...m.armures];
			}
			// Armes
			if (m.armes) {
				this.character.proficiencies.weapons = [...m.armes];
			}
		}
	}

	// ========================================
	// ONGLET NIVEAUX
	// ========================================

	renderLevelsTab(container) {
		container.createEl('h3', { text: 'Progression Multi-classe' });

		if (this.character.levels.length === 0) {
			container.createEl('p', { text: 'Selectionnez d\'abord une classe dans l\'onglet Base.' });
			return;
		}

		// Timeline des niveaux
		const timeline = container.createDiv({ cls: 'dnd-level-timeline' });

		for (let i = 0; i < this.character.levels.length; i++) {
			const level = this.character.levels[i];
			const lvlNum = i + 1;

			const levelRow = timeline.createDiv({ cls: 'dnd-level-row' });

			// Numero
			levelRow.createEl('span', { text: `Niv. ${lvlNum}`, cls: 'dnd-level-num' });

			// Dropdown classe
			const classOptions = Object.keys(this.vaultData.classes);
			const classSelect = levelRow.createEl('select');
			for (const cls of classOptions) {
				const opt = classSelect.createEl('option', { text: cls, attr: { value: cls } });
				if (cls === level.class) opt.selected = true;
			}
			classSelect.onchange = (e) => {
				this.character.levels[i].class = e.target.value;
				this.updateSheet();
			};

			// Info sur ce niveau
			const classInfo = this.vaultData.classes[level.class];
			if (classInfo) {
				const abilities = classInfo.capacites?.filter(c => {
					const match = c.name.match(/niveau (\d+)/i);
					return match && parseInt(match[1]) === this.getClassLevel(level.class, i);
				});

				if (abilities?.length > 0) {
					const abilitySpan = levelRow.createEl('span', { cls: 'dnd-level-abilities' });
					abilitySpan.textContent = abilities.map(a => a.name.replace(/\s*\(niveau \d+\)/i, '')).join(', ');
				}
			}

			// ASI/Feat aux niveaux 4, 8, 12, 16, 19 de chaque classe
			const classLevel = this.getClassLevel(level.class, i);
			if ([4, 8, 12, 16, 19].includes(classLevel)) {
				const asiDiv = levelRow.createDiv({ cls: 'dnd-level-asi' });
				asiDiv.createEl('span', { text: 'ASI/Don disponible', cls: 'dnd-asi-badge' });
			}

			// Bouton supprimer (sauf niveau 1)
			if (i > 0) {
				const removeBtn = levelRow.createEl('button', { text: 'X', cls: 'dnd-remove-btn' });
				removeBtn.onclick = () => {
					this.character.levels.splice(i, 1);
					this.render();
				};
			}
		}

		// Bouton ajouter niveau
		if (this.character.levels.length < 20) {
			const addBtn = container.createEl('button', { text: '+ Ajouter un niveau', cls: 'dnd-add-level-btn' });
			addBtn.onclick = () => {
				const lastClass = this.character.levels[this.character.levels.length - 1].class;
				this.character.levels.push({ class: lastClass, subclass: null, choices: {} });
				this.render();
			};
		}

		// Resume multi-classe
		const summary = container.createDiv({ cls: 'dnd-class-summary' });
		summary.createEl('h4', { text: 'Resume' });
		const classes = this.character.classes;
		for (const [cls, lvl] of Object.entries(classes)) {
			summary.createEl('p', { text: `${cls}: niveau ${lvl}` });
		}
	}

	getClassLevel(className, upToIndex) {
		let count = 0;
		for (let i = 0; i <= upToIndex; i++) {
			if (this.character.levels[i]?.class === className) {
				count++;
			}
		}
		return count;
	}

	// ========================================
	// ONGLET SORTS
	// ========================================

	renderSpellsTab(container) {
		container.createEl('h3', { text: 'Sorts' });

		// Verifier si lanceur de sorts
		const spellcasters = ['Barde', 'Clerc', 'Druide', 'Ensorceleur', 'Magicien', 'Occultiste', 'Paladin', 'Rodeur'];
		const hasSpellcasting = Object.keys(this.character.classes).some(c => spellcasters.includes(c));

		if (!hasSpellcasting) {
			container.createEl('p', { text: 'Ce personnage ne peut pas lancer de sorts.' });
			return;
		}

		// Bouton ajouter sort
		const addBtn = container.createEl('button', { text: '+ Ajouter un sort', cls: 'dnd-add-spell-btn' });
		addBtn.onclick = () => this.openSpellBrowser();

		// Liste des sorts selectionnes
		const spellList = container.createDiv({ cls: 'dnd-spell-selection' });

		if (this.character.spellsKnown.length === 0) {
			spellList.createEl('p', { text: 'Aucun sort selectionne.' });
		} else {
			for (let i = 0; i < this.character.spellsKnown.length; i++) {
				const spell = this.character.spellsKnown[i];
				const spellRow = spellList.createDiv({ cls: 'dnd-spell-row' });
				spellRow.createEl('span', { text: spell.name });
				spellRow.createEl('span', { text: `Niv. ${spell.niveau}`, cls: 'dnd-spell-level' });

				const removeBtn = spellRow.createEl('button', { text: 'X', cls: 'dnd-remove-btn' });
				removeBtn.onclick = () => {
					this.character.spellsKnown.splice(i, 1);
					this.render();
				};
			}
		}
	}

	openSpellBrowser() {
		new SpellBrowserModal(this.app, this.vaultData.spells, (spell) => {
			this.character.spellsKnown.push(spell);
			this.render();
		}).open();
	}

	// ========================================
	// ONGLET EQUIPEMENT
	// ========================================

	renderEquipmentTab(container) {
		container.createEl('h3', { text: 'Equipement' });

		// Bouton ajouter
		const addBtn = container.createEl('button', { text: '+ Ajouter equipement', cls: 'dnd-add-btn' });
		addBtn.onclick = () => this.openEquipmentBrowser();

		// Liste
		const list = container.createDiv({ cls: 'dnd-equipment-list' });

		if (this.character.equipment.length === 0) {
			list.createEl('p', { text: 'Aucun equipement.' });
		} else {
			for (let i = 0; i < this.character.equipment.length; i++) {
				const item = this.character.equipment[i];
				const row = list.createDiv({ cls: 'dnd-equipment-row' });
				row.createEl('span', { text: item.name });

				const removeBtn = row.createEl('button', { text: 'X', cls: 'dnd-remove-btn' });
				removeBtn.onclick = () => {
					this.character.equipment.splice(i, 1);
					this.render();
				};
			}
		}

		// Argent
		container.createEl('h4', { text: 'Argent' });
		const moneyDiv = container.createDiv({ cls: 'dnd-money-inputs' });
		const currencies = ['pp', 'po', 'pe', 'pa', 'pc'];
		const labels = { pp: 'PP', po: 'PO', pe: 'PE', pa: 'PA', pc: 'PC' };

		for (const curr of currencies) {
			const row = moneyDiv.createDiv({ cls: 'dnd-money-row' });
			row.createEl('label', { text: labels[curr] });
			const input = row.createEl('input', {
				type: 'number',
				attr: { min: 0, value: this.character.money[curr] }
			});
			input.onchange = (e) => {
				this.character.money[curr] = parseInt(e.target.value) || 0;
			};
		}
	}

	openEquipmentBrowser() {
		new EquipmentBrowserModal(this.app, this.vaultData.equipment, (item) => {
			this.character.equipment.push({ name: item.name, quantity: 1 });
			this.render();
		}).open();
	}

	// ========================================
	// ONGLET ROLEPLAY
	// ========================================

	renderRoleplayTab(container) {
		container.createEl('h3', { text: 'Roleplay' });

		this.createTextArea(container, 'Traits de personnalite', this.character.traits, (v) => {
			this.character.traits = v;
		});

		this.createTextArea(container, 'Ideaux', this.character.ideals, (v) => {
			this.character.ideals = v;
		});

		this.createTextArea(container, 'Liens', this.character.bonds, (v) => {
			this.character.bonds = v;
		});

		this.createTextArea(container, 'Defauts', this.character.flaws, (v) => {
			this.character.flaws = v;
		});

		this.createTextArea(container, 'Histoire', this.character.backstory, (v) => {
			this.character.backstory = v;
		}, 6);

		// Apparence
		container.createEl('h4', { text: 'Apparence' });
		const appearanceGrid = container.createDiv({ cls: 'dnd-appearance-grid' });

		const fields = ['age', 'height', 'weight', 'eyes', 'hair', 'skin'];
		const labels = { age: 'Age', height: 'Taille', weight: 'Poids', eyes: 'Yeux', hair: 'Cheveux', skin: 'Peau' };

		for (const field of fields) {
			this.createTextInput(appearanceGrid, labels[field], this.character.appearance[field], (v) => {
				this.character.appearance[field] = v;
			});
		}
	}

	// ========================================
	// ACTIONS
	// ========================================

	renderActions(container) {
		const actions = container.createDiv({ cls: 'dnd-builder-actions' });

		const saveBtn = actions.createEl('button', { text: 'Sauvegarder en Note', cls: 'dnd-save-btn' });
		saveBtn.onclick = () => this.saveToNote();

		const resetBtn = actions.createEl('button', { text: 'Nouveau Personnage', cls: 'dnd-reset-btn' });
		resetBtn.onclick = () => {
			this.character = new CharacterData();
			this.render();
		};
	}

	async saveToNote() {
		if (!this.character.name) {
			new Notice('Veuillez donner un nom au personnage.');
			return;
		}

		const yamlData = this.character.toYaml(this.vaultData.classes);
		const yamlStr = stringifyYaml(yamlData);

		const content = `---
aliases:
  - ${this.character.name}
tags:
  - personnage
  - joueur
---

# ${this.character.name}

\`\`\`dnd-personnage
${yamlStr}\`\`\`
`;

		const fileName = `${this.character.name.replace(/[\\/:*?"<>|]/g, '_')}.md`;
		const path = `Glossary/Personnages/${fileName}`;

		try {
			// Verifier si le dossier existe
			const folder = this.app.vault.getAbstractFileByPath('Glossary/Personnages');
			if (!folder) {
				await this.app.vault.createFolder('Glossary/Personnages');
			}

			// Verifier si le fichier existe
			const existing = this.app.vault.getAbstractFileByPath(path);
			if (existing) {
				await this.app.vault.modify(existing, content);
				new Notice(`Personnage mis a jour: ${fileName}`);
			} else {
				await this.app.vault.create(path, content);
				new Notice(`Personnage cree: ${fileName}`);
			}

			// Ouvrir la note
			const file = this.app.vault.getAbstractFileByPath(path);
			if (file) {
				await this.app.workspace.openLinkText(path, '');
			}
		} catch (e) {
			new Notice(`Erreur: ${e.message}`);
			console.error('[DnD Builder] Erreur sauvegarde:', e);
		}
	}

	// ========================================
	// HELPERS UI
	// ========================================

	createTextInput(container, label, value, onChange) {
		const div = container.createDiv({ cls: 'dnd-field' });
		div.createEl('label', { text: label });
		const input = div.createEl('input', { type: 'text', attr: { value: value || '' } });
		input.onchange = (e) => onChange(e.target.value);
		return input;
	}

	createDropdown(container, label, options, selected, onChange) {
		const div = container.createDiv({ cls: 'dnd-field' });
		div.createEl('label', { text: label });
		const select = div.createEl('select');

		for (const opt of options) {
			const optEl = select.createEl('option', {
				text: opt || '-- Choisir --',
				attr: { value: opt }
			});
			if (opt === selected) optEl.selected = true;
		}

		select.onchange = (e) => onChange(e.target.value);
		return select;
	}

	createTextArea(container, label, value, onChange, rows = 3) {
		const div = container.createDiv({ cls: 'dnd-field' });
		div.createEl('label', { text: label });
		const textarea = div.createEl('textarea', { attr: { rows } });
		textarea.value = value || '';
		textarea.onchange = (e) => onChange(e.target.value);
		return textarea;
	}

	updateSheet() {
		// Re-render seulement la fiche
		const sheetPanel = this.containerEl.querySelector('.dnd-builder-sheet');
		if (sheetPanel) {
			const sheetRenderer = new LiveSheetRenderer(sheetPanel, this.character, this.vaultData);
			sheetRenderer.render();
		}
	}
}

// ========================================
// SPELL BROWSER MODAL
// ========================================

class SpellBrowserModal extends Modal {
	constructor(app, spells, onSelect) {
		super(app);
		this.allSpells = spells;
		this.onSelect = onSelect;
		this.filters = { level: 'all', school: 'all', search: '' };
	}

	onOpen() {
		this.modalEl.addClass('dnd-browser-modal');
		this.contentEl.createEl('h2', { text: 'Selectionner un Sort' });

		this.renderFilters();
		this.renderList();
	}

	renderFilters() {
		const filtersDiv = this.contentEl.createDiv({ cls: 'dnd-browser-filters' });

		// Recherche
		const searchInput = filtersDiv.createEl('input', {
			type: 'text',
			placeholder: 'Rechercher...',
			cls: 'dnd-search-input'
		});
		searchInput.oninput = (e) => {
			this.filters.search = e.target.value.toLowerCase();
			this.renderList();
		};

		// Filtre niveau
		const levelSelect = filtersDiv.createEl('select');
		levelSelect.createEl('option', { text: 'Tous niveaux', attr: { value: 'all' } });
		for (let i = 0; i <= 9; i++) {
			levelSelect.createEl('option', { text: `Niveau ${i}`, attr: { value: i } });
		}
		levelSelect.onchange = (e) => {
			this.filters.level = e.target.value;
			this.renderList();
		};

		// Filtre ecole
		const schools = ['all', 'Abjuration', 'Conjuration', 'Divination', 'Enchantement', 'Evocation', 'Illusion', 'Necromancie', 'Transmutation'];
		const schoolSelect = filtersDiv.createEl('select');
		for (const school of schools) {
			schoolSelect.createEl('option', {
				text: school === 'all' ? 'Toutes ecoles' : school,
				attr: { value: school }
			});
		}
		schoolSelect.onchange = (e) => {
			this.filters.school = e.target.value;
			this.renderList();
		};
	}

	renderList() {
		let listDiv = this.contentEl.querySelector('.dnd-browser-list');
		if (!listDiv) {
			listDiv = this.contentEl.createDiv({ cls: 'dnd-browser-list' });
		}
		listDiv.empty();

		const filtered = this.getFilteredSpells();

		if (filtered.length === 0) {
			listDiv.createEl('p', { text: 'Aucun sort trouve.' });
			return;
		}

		for (const spell of filtered.slice(0, 100)) {
			const item = listDiv.createDiv({ cls: 'dnd-browser-item' });
			item.createEl('span', { text: spell.name, cls: 'dnd-item-name' });
			item.createEl('span', { text: `Niv. ${spell.niveau}`, cls: 'dnd-item-level' });
			item.createEl('span', { text: spell.ecole || '', cls: 'dnd-item-school' });

			item.onclick = () => {
				this.onSelect(spell);
				this.close();
			};
		}

		if (filtered.length > 100) {
			listDiv.createEl('p', { text: `... et ${filtered.length - 100} autres. Utilisez la recherche.` });
		}
	}

	getFilteredSpells() {
		return this.allSpells.filter(spell => {
			// Filtre recherche
			if (this.filters.search && !spell.name.toLowerCase().includes(this.filters.search)) {
				return false;
			}
			// Filtre niveau
			if (this.filters.level !== 'all' && spell.niveau !== parseInt(this.filters.level)) {
				return false;
			}
			// Filtre ecole
			if (this.filters.school !== 'all' && spell.ecole?.toLowerCase() !== this.filters.school.toLowerCase()) {
				return false;
			}
			return true;
		});
	}
}

// ========================================
// EQUIPMENT BROWSER MODAL
// ========================================

class EquipmentBrowserModal extends Modal {
	constructor(app, equipment, onSelect) {
		super(app);
		this.allEquipment = equipment;
		this.onSelect = onSelect;
		this.filters = { type: 'all', search: '' };
	}

	onOpen() {
		this.modalEl.addClass('dnd-browser-modal');
		this.contentEl.createEl('h2', { text: 'Selectionner un Equipement' });

		this.renderFilters();
		this.renderList();
	}

	renderFilters() {
		const filtersDiv = this.contentEl.createDiv({ cls: 'dnd-browser-filters' });

		// Recherche
		const searchInput = filtersDiv.createEl('input', {
			type: 'text',
			placeholder: 'Rechercher...',
			cls: 'dnd-search-input'
		});
		searchInput.oninput = (e) => {
			this.filters.search = e.target.value.toLowerCase();
			this.renderList();
		};

		// Filtre type
		const typeSelect = filtersDiv.createEl('select');
		typeSelect.createEl('option', { text: 'Tous types', attr: { value: 'all' } });
		typeSelect.createEl('option', { text: 'Armes', attr: { value: 'arme' } });
		typeSelect.createEl('option', { text: 'Armures', attr: { value: 'armure' } });
		typeSelect.onchange = (e) => {
			this.filters.type = e.target.value;
			this.renderList();
		};
	}

	renderList() {
		let listDiv = this.contentEl.querySelector('.dnd-browser-list');
		if (!listDiv) {
			listDiv = this.contentEl.createDiv({ cls: 'dnd-browser-list' });
		}
		listDiv.empty();

		const filtered = this.getFilteredEquipment();

		if (filtered.length === 0) {
			listDiv.createEl('p', { text: 'Aucun equipement trouve.' });
			return;
		}

		for (const item of filtered) {
			const row = listDiv.createDiv({ cls: 'dnd-browser-item' });
			row.createEl('span', { text: item.name, cls: 'dnd-item-name' });
			row.createEl('span', { text: item.categorie || item.type || '', cls: 'dnd-item-cat' });

			row.onclick = () => {
				this.onSelect(item);
				this.close();
			};
		}
	}

	getFilteredEquipment() {
		return this.allEquipment.filter(item => {
			if (this.filters.search && !item.name.toLowerCase().includes(this.filters.search)) {
				return false;
			}
			if (this.filters.type !== 'all' && item.type !== this.filters.type) {
				return false;
			}
			return true;
		});
	}
}

// ========================================
// EXPORTS
// ========================================

module.exports = {
	VIEW_TYPE_CHARACTER_BUILDER,
	CharacterBuilderView,
	CharacterData,
	VaultDataLoader
};
