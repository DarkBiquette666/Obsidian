---
aliases:
  - Dungeon
  - dungeon
  - dungeons
---

# Dungeons

Dungeons are the major areas of a run. Each run consists of **4 Dungeons**, each with its own theme, enemy pool, and Major Boss.

---

## Structure

```
DUNGEON
├── Floor 1 → Rooms → Mini-Boss
├── Floor 2 → Rooms → Mini-Boss
├── Floor N → Rooms → Mini-Boss
└── MAJOR BOSS → Key Fragment
```

---

## Dungeon Progression

| Dungeon | Reward |
|---------|--------|
| **Dungeon 1** | Key Fragment #1 |
| **Dungeon 2** | Key Fragment #2 |
| **Dungeon 3** | Key Fragment #3 |
| **Dungeon 4** | Access to Final Boss |

Collecting all 4 Key Fragments allows Vorathros to face [[The Supreme Void]].

---

## Components

### Floors
Each Dungeon contains multiple [[Floors]]:
- Each Floor has its own [[Anomalies|Anomaly]]
- Ends with a **Mini-Boss** from the Dungeon's boss pool

### Major Boss
Each Dungeon ends with a **Major Boss**:
- Unique boss encounter
- Rewards a **Key Fragment** (required for final boss)
- Examples: [[Syl'Korath, the Infamous]], [[Aeryn'Tor]], [[Nythra'Zal]]

---

## Design Notes

- Each Dungeon should have a distinct visual theme
- Enemy pools should be thematically consistent
- Difficulty scales across Dungeons (Dungeon 4 > Dungeon 1)
- Major Bosses are the "gatekeepers" of progression

---

## Related

- [[Floors]]
- [[Rooms]]
- [[Gameplay Loop]]
- [[The Supreme Void]]
