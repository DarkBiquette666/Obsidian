# Dark Ether - Game Design Document

---

## 1. Game Overview

**Title:** Dark Ether

**Genre:** Hack'n'Slash / Roguelite with deep RPG progression

**Engine:** Godot v4.3

**Inspirations:** Path of Exile (build depth), Hades (run structure), Ravenswatch (class versatility)

### Pitch

Dark Ether is a hack'n'slash roguelite where you play as Vorathros, a polymorphic Titan who can switch between 6 classes in real-time. Unlike traditional roguelites where your build is at the mercy of RNG, Dark Ether separates **build identity** (permanent) from **tactical adaptation** (per-run), giving players the depth of an ARPG with the replayability of a roguelite.

### Core Design Philosophy

The game solves two common player frustrations:

| Frustration | Dark Ether's Solution |
|-------------|----------------------|
| **PoE:** Locked into one build, can't experiment | Play 6 classes simultaneously, switch in real-time |
| **Roguelite:** RNG dictates your build each run | Your build is permanent; only tactical adaptations are per-run |

**The mantra:** *Your build identity is permanent. Your tactical adaptation is per-run.*

---

## 2. Narrative

### Universe

The story takes place in a universe corrupted by the Dark Ether, an ancient force that transformed the Titans—once guardians of cosmic balance—into monstrous entities. Only Vorathros, the Polymorphic Titan, resisted this corruption.

### Context

Vorathros was once the most powerful Titan, but was severely weakened during a cataclysmic battle against the Supreme Void. This justifies his weak starting state and drives the core progression: restoring his lost power to confront the Supreme Void and free his corrupted brothers.

### Objective

Progress through the prison's levels, defeat corrupted creatures and bosses, purify the fallen Titans, and collect fragments of the Cosmic Key to ultimately face the Supreme Void.

### Plot Twist

Upon reaching the final boss, the screen fades like an eye closing. A deep voice speaks: *"I've been watching you this whole time, Vorathros. Now it is time..."*

The player realizes everything was seen through the Supreme Void's eye. For this final fight, the player controls the Supreme Void against an AI-controlled Vorathros. To truly win, the player must let Vorathros defeat them.

---

## 3. Core Mechanics

### 3.1 Polymorphism (Class Switching)

Vorathros can adopt 6 different forms, each inspired by an ancient race:

| Class | Identity | Playstyles |
|-------|----------|------------|
| **Lesharii** | Nomadic hunters | Feral Hunter (ranged), Venom Hunter (poison), Primal Hunter (melee speed) |
| **Astralians** | Ethereal cosmic beings | Cosmic Mage (elemental), Abyssal Necromancer (summons), Occultist (curses) |
| **Torin** | Stone giants | Ether Berserker (rage), Blood Warrior (blood magic), Iron Wall (tank) |
| **Umbrathi** | Shadow assassins | Frost Shadow (cold), Abyssal Kraken (tentacles), Bounty Hunter (precision) |
| **Voidborn** | Prophets of the abyss | Parasite Matriarch (corruption), Cursed Mantle (curses), Cosmic Inquisitor (debuffs) |
| **Fortunians** | Fortune seekers | Master of Cards (luck), Techno-Magic Engineer (gadgets), Artisan Tinkerer (crafting) |

**Key feature:** Switch class in real-time during combat via radial menu or hotkey. The skillbar dynamically updates to show the active class's abilities.

### 3.2 Ability System

- Each class has **7 skill slots**
- **Dash** is universal across all classes (limited charges, rechargeable)
- Skills are unlocked permanently and customized before runs

### 3.3 Shield & Parry

**Passive Blocking:** Shields grant a % chance to auto-block attacks.

**Active Blocking:**
- **Perfect Parry:** Block at the exact moment → full absorption, fills parry gauge significantly
- **Imperfect Parry:** Block early → partial absorption, fills parry gauge less

**Parry Gauge:** Fills with each parry. When full, causes stun. Can be improved via:
- Increased gauge capacity
- Faster gauge recovery
- Shorter stun duration
- Longer perfect parry window

---

## 4. Progression System

### Design Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│                     PERMANENT (Your Identity)                   │
├─────────────────────────────────────────────────────────────────┤
│  Stuff      │  Equipment that defines your stats                │
│  Supports   │  Runes that modify how your skills work           │
│  Stat-ups   │  Your personal passive tree                       │
│  Perks      │  Major, build-defining skill modifications        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    TEMPORARY (Per-Run Adaptation)               │
├─────────────────────────────────────────────────────────────────┤
│  Anomalies  │  Floor modifiers that challenge your build        │
│  Mutations  │  DNA adaptations purchased in Merchant Rooms      │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4.1 Permanent Progression (Meta)

#### A. Stuff (Equipment)

- Weapons, armor, accessories
- Defines your base stats
- Crafted and collected throughout the game
- **Never lost between runs**
- Rarity tiers: Common → Magic → Rare → Unique

#### B. Skill Supports

- Runes that modify skill behavior (like PoE support gems)
- Slotted into skills permanently
- Examples: "Added Fire Damage", "Chain", "Increased AoE"
- Considered equipment → permanent once obtained

#### C. Stat-ups

- Your personal "passive tree"
- Permanent stat investments
- Unlocked via meta-progression (Account Level 0-100)
- Compensate for gaps in your equipment

#### D. Perks

**Major, build-defining modifications to your skills.**

- Unlocked through meta-progression
- Equipped before starting a run
- Define HOW your skills fundamentally work
- These are your theorycrafted choices

**Examples:**
- "Bloodblades amount is increased by x"
- "Call of the Colony summons Ether Flies instead of Spiders"
- "Dash leaves a trail of fire"
- "Your curses spread to nearby enemies on death"

**Key principle:** Perks are permanent choices. You unlock them, you equip them, they're YOUR build.

---

### 4.2 Run Progression (Temporary)

The roguelite variance comes from **adapting to challenges**, not rebuilding your identity.

#### A. Floor Anomalies

Each floor reveals an **Anomaly**—a temporal distortion that changes the rules of this timeline.

**Narrative context:** Each run is a different timeline. Anomalies represent the unique distortions of that particular timeline.

**Design rule:** Anomalies **challenge** your build without **hard-countering** it.

**Examples:**
- "Physical Resistance +50% on all enemies"
- "Enemies explode on death (Fire damage)"
- "No natural healing, but Lifesteal +30%"
- "Elite enemies have Frost Aura"
- "Lightning damage +100%, Movement speed -20%"
- "Enemies regenerate HP, but have -30% max HP"

Your Torin Blood Warrior might struggle against physical resistance—but that's when your Astralian Cosmic Mage shines. Anomalies encourage using all 6 classes.

#### B. Mutations

**DNA adaptations purchased in the Merchant Room.**

**Narrative context:** Vorathros is a shapeshifter who manipulates his own DNA. Mutations represent temporary genetic modifications he applies to adapt to the current timeline's anomalies.

| Property | Detail |
|----------|--------|
| **Slots** | 6 maximum (mirrors your 6 classes) |
| **Weight** | Lighter than Perks—tactical, not build-defining |
| **Purpose** | Patch weaknesses against current anomalies |
| **Acquisition** | Purchased with gold in Merchant Rooms |

**Examples:**
- "Convert 30% Physical damage to Fire"
- "Your Bloodblades inflict Bleed even on immune enemies"
- "+20% damage against the dominant enemy type"
- "Gain 5% of damage dealt as Energy Shield"
- "Your summons taunt enemies for 2 seconds on spawn"
- "Lightning Resistance +30%"

**Strategic depth:**
- Spread 6 Mutations across 6 classes (1 each to cover weaknesses)
- Or stack all 6 on one class to hyper-specialize
- Gold becomes crucial: Mutations vs healing vs consumables

#### C. Room Rewards

Different rooms provide different rewards:

| Room Type                | Rewards                                       |
| ------------------------ | --------------------------------------------- |
| **Normal Room**          | Resources, consumables, minor stats up        |
| **Trial Room**           | Blessings (scaled to objective performance)   |
| **Corrupted Room**       | Corruptions (bonus + malus)                   |
| **Boss Room**            | Meta-loot, equipment, story progression       |
| **Merchant Room**        | Spend gold on Mutations, consumables, healing |
| **Chamber of Lost Time** | Unique random rewards                         |

See **Section 5: Dungeon Structure** for detailed room mechanics.

---

### 4.3 The Run Flow

A complete run consists of **4 Dungeons**. Each Dungeon contains multiple **Floors**. Each Floor contains multiple **Rooms**.

```
RUN STRUCTURE
├── DUNGEON 1
│   ├── Floor 1 → Rooms → Mini-Boss
│   ├── Floor 2 → Rooms → Mini-Boss
│   ├── Floor N → Rooms → Mini-Boss
│   └── MAJOR BOSS → Key Fragment #1
├── DUNGEON 2
│   ├── Floors...
│   └── MAJOR BOSS → Key Fragment #2
├── DUNGEON 3
│   ├── Floors...
│   └── MAJOR BOSS → Key Fragment #3
└── DUNGEON 4
    ├── Floors...
    └── FINAL BOSS (The Supreme Void)
```

### Detailed Flow

```
LOBBY
├── Equip your Stuff, Supports, Perks
├── Your 6 classes are ready with their permanent builds
└── Start Run

DUNGEON 1
│
├── FLOOR 1
│   ├── Anomaly revealed: "Physical Resistance +50%"
│   ├── Normal Rooms → Resources, consumables, stat-ups
│   ├── Trial/Corrupted Rooms → Blessings or Corruptions
│   ├── Merchant Room: Buy Mutations to adapt
│   │   └── "Convert 30% Physical → Fire"
│   └── Mini-Boss
│
├── FLOOR 2
│   ├── New Anomaly: "Enemies explode on death (Fire)"
│   ├── Your previous Mutation might hurt you now!
│   ├── Rooms...
│   ├── Merchant Room: Swap/add Mutations (6 slots total)
│   │   └── "Fire Resistance +30%"
│   └── Mini-Boss
│
├── FLOOR N...
│
└── MAJOR BOSS
    └── Reward: Key Fragment + Major loot

DUNGEON 2, 3, 4...
└── Same structure, increasing difficulty

END OF RUN
├── Success: All 4 Key Fragments, face The Supreme Void
└── Failure: Keep resources, return to Lobby
```

---

### 4.4 Meta-Progression (Global Level)

**Global Level 0-100** tracks overall progression:

- Unlocks new Perks
- Unlocks Stat-up nodes
- Unlocks new equipment tiers
- Unlocks new Mutations in Merchant pool
- Story/lore unlocks

Experience gained at end of each run, proportional to difficulty reached.

---

## 5. Dungeon Structure

### 5.1 Hierarchy

```
RUN
└── 4 DUNGEONS
    └── Multiple FLOORS per dungeon
        └── Multiple ROOMS per floor
```

### 5.2 Dungeons

Each run consists of **4 Dungeons**:
- Each Dungeon has a unique theme and enemy pool
- Multiple **Floors** per Dungeon
- Ends with a **Major Boss**
- Defeating the Major Boss rewards a **Key Fragment**
- Collecting all 4 Key Fragments unlocks the Final Boss

### 5.3 Floors

Each Floor contains:
- A revealed **Anomaly** at the start
- Multiple **Rooms** to clear
- A **Merchant Room** before the boss
- A **Mini-Boss** at the end (from the Dungeon's boss pool)

### 5.4 Room Types

| Room | Description | Reward |
|------|-------------|--------|
| **Normal Room** | Standard combat encounter | Gold, resources, consumables |
| **Trial Room** | Challenge with graded objectives | Blessings (scaled to performance) |
| **Corrupted Room** | Choose corruption first, then survive | Corruptions (bonus + malus) |
| **Boss Room** | Floor boss encounter | Meta-loot, story progression |
| **Merchant Room** | Shop | Mutations, consumables, healing |
| **Chamber of Lost Time** | Rare, unique mechanics | Random special reward |

---

### 5.5 Room Details

#### Normal Room
Standard combat encounter. Clear all enemies to receive:
- Gold (for Merchant purchases)
- Resources (for meta-progression/crafting)
- Consumables (potions, temporary items)

#### Trial Room
A room with a **graded objective** system to minimize frustration:

**Flow:**
1. Enter room, objective is revealed (e.g., "Clear without taking damage", "Kill all enemies within 60s")
2. Complete the room
3. Reward scales based on performance:
   - **Failed objective** → Minor Blessing
   - **Partial success** → Standard Blessing
   - **Full success** → Major Blessing

**Rewards:** Blessings (pure buffs, no downside)

#### Corrupted Room
A risk/reward room where you commit before fighting:

**Flow:**
1. Enter room, see available **Corruptions** (bonus + malus combinations)
2. **Choose your Corruption first** (commit to the deal)
3. Enemies spawn
4. **Survive** to keep the Corruption; die and lose everything

**Rewards:** Corruptions (powerful bonuses with drawbacks)

#### Boss Room
End-of-floor encounter:
- Defeat the floor boss
- Rewards: Equipment, resources, meta-progression items, story elements

#### Merchant Room
Shop to prepare for upcoming challenges:
- **Mutations** (DNA adaptations, 6 slots max)
- Consumables
- Healing
- Occasionally rare items

#### Chamber of Lost Time
A rare room with **unique, random mechanics** each time:

**Spawn conditions:**
- Random chance per floor (rare)
- **Guaranteed** if specific condition met (e.g., clear Floor 1 under X minutes)

**Possible variants:**
- Single chest guaranteeing a **Unique item**
- Room full of treasure chests
- Choice of **3 Blessings**
- **Perk unlock** (meta-progression during run)
- Special merchant with rare Mutations
- One-shot crafting station
- Narrative event with meaningful choice
- Healing fountain with a trade-off

---

### 5.6 Purity/Corruption Balance System

A dynamic system inspired by Binding of Isaac's Angel/Devil room duality.

#### The Balance Gauge

```
[PURITY] ◄━━━━━━━━━━━━━●━━━━━━━━━━━━━► [CORRUPTION]
  100%              50/50              100%
```

#### Rules

1. **Start of run:** Gauge at 50/50 (neutral)

2. **Each choice shifts the balance:**
   - Complete a Trial Room → Gauge shifts toward **Purity**
   - Complete a Corrupted Room → Gauge shifts toward **Corruption**

3. **Spawn probability:**
   - Gauge position = % chance for each room type to appear
   - At 70% Purity: 70% chance Trial Room, 30% chance Corrupted Room

4. **Point of no return (Lock):**
   - Reaching **100%** on either side = **Locked**
   - Cannot return to neutral
   - Only that room type will spawn for the rest of the run

#### Reward Pools by State

| State | Available Pool |
|-------|----------------|
| **Neutral (0-99%)** | Standard Blessings / Standard Corruptions |
| **Locked Purity (100%)** | Standard + **Sacred Blessings** (exclusive) |
| **Locked Corruption (100%)** | Standard + **Abyssal Corruptions** (exclusive) |

**Sacred Blessings:** Extremely powerful pure buffs, only accessible to those fully committed to Purity.

**Abyssal Corruptions:** Extremely powerful bonus/malus combinations, only accessible to those fully committed to Corruption.

#### Strategic Implications

- **Stay neutral:** Flexibility, access to both room types, but no exclusive rewards
- **Commit to one side:** Lose flexibility, gain access to exclusive powerful rewards
- **The choice matters:** Early rooms influence late-game options

---

### 5.7 Blessings & Corruptions

#### Blessings (Trial Room Rewards)

Pure buffs with no downside. Themed around light, order, and purity.

| Tier | Source | Power Level |
|------|--------|-------------|
| **Minor** | Trial (failed objective) | Small buff |
| **Standard** | Trial (partial success) | Moderate buff |
| **Major** | Trial (full success) | Strong buff |
| **Sacred** | Trial (Locked Purity only) | Exclusive, very powerful |

#### Corruptions (Corrupted Room Rewards)

Powerful bonuses paired with meaningful drawbacks. Themed around darkness, chaos, and corruption.

| Tier | Source | Power Level |
|------|--------|-------------|
| **Standard** | Corrupted Room | Bonus + Malus |
| **Abyssal** | Corrupted Room (Locked Corruption only) | Exclusive, extreme bonus + extreme malus |

---

### 5.8 Timed Runs

- Each run has a **countdown timer**
- **Time rewards:** Completing objectives quickly unlocks bonuses (hidden bosses, rare items, Chamber of Lost Time guarantee)
- **Run failure:** If timer expires before killing final boss, run fails → return to Lobby with collected resources

---

## 6. Skills System

### 6.1 Skill Acquisition

Skills are unlocked permanently through meta-progression:
- Defeating bosses
- Finding skill runes in dungeons
- Account level milestones

Each class has:
- **General skill pool** (available to all specializations)
- **Specialization skills** (unlocked when choosing a sub-class)

### 6.2 Skill Customization Layers

```
SKILL (e.g., "Bloodblade")
│
├── Base behavior (inherent to the skill)
│
├── Supports (slotted gems that modify behavior)
│   └── "Added Fire", "Chain", "Faster Casting"
│
└── Perks (major modifications, 1-2 per skill)
    └── "Bloodblades chain to 3 enemies"
```

### 6.3 Universal Skills

Some special skills can be used by any class, enabling cross-class synergies.

---

## 7. Equipment System

### 7.1 Rarity Tiers

| Rarity | Affixes | Notes |
|--------|---------|-------|
| **Common** | 0 | Base stats only |
| **Magic** | 1-2 | Minor bonuses |
| **Rare** | 3-4 | Significant build impact |
| **Unique** | Special | Fixed affixes, may grant skills or unique effects |

### 7.2 Crafting

Players can craft equipment using resources collected during runs:
- Reroll affixes
- Upgrade rarity
- Target specific stat types

---

## 8. User Interface

### 8.1 Lobby UI

- Class selection and loadout
- Equipment management
- Perk and Support assignment
- Stat-up allocation
- Run initiation

### 8.2 In-Run UI

- **Skillbar:** 7 slots, dynamically updates on class switch
- **Class switcher:** Radial menu or hotkeys (1-6)
- **Mutation display:** Show active Mutations (6 slots)
- **Anomaly indicator:** Current floor's anomaly always visible
- **Timer:** Run countdown

### 8.3 Merchant Room UI

- Available Mutations for purchase
- Current Mutation loadout (6 slots)
- Ability to swap/replace Mutations
- Other purchasables (consumables, healing)

---

## 9. Why This Design Works

| Player Want | How It's Solved |
|-------------|-----------------|
| "I want to build MY Torin" | Perks, Stuff, Supports, Stats are all permanent |
| "I want variety each run" | Anomalies force different approaches |
| "I don't want RNG to ruin my build" | Mutations are purchased, not random |
| "I want to use all 6 classes" | Anomalies make different classes shine |
| "I want meaningful in-run choices" | 6 Mutation slots = real trade-offs |
| "I want long-term progression" | Account level, equipment, Perks persist |
| "I want each run to feel different" | Anomaly combinations create unique challenges |

---

## 10. Future Sections (To Be Developed)

- Level Design
- Art Direction
- Sound Design
- Technical Architecture
- Monetization Strategy
- Team & Resources
