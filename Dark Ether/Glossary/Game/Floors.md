---
aliases:
  - floor
  - Floor
  - floors
---

# Floors

Floors are the levels within a [[Dungeons|Dungeon]]. Each Floor contains multiple [[Rooms]] and ends with a **Mini-Boss**.

---

## Structure

```
FLOOR
├── Anomaly revealed at start
├── Normal Rooms → Resources, consumables, stat-ups
├── Trial Rooms → Blessings
├── Corrupted Rooms → Corruptions
├── Merchant Room → Mutations, supplies
└── Mini-Boss
```

---

## Floor Components

### Anomaly
Each Floor has a unique [[Anomalies|Anomaly]] revealed at the start:
- Modifies the rules for that Floor
- Challenges the player's build
- Can be countered with [[Mutations]]

### Rooms
Multiple [[Rooms]] to clear:
- [[Normal Room]] - Standard combat, resources
- [[Trial Room]] - Challenge for [[Blessings]]
- [[Corrupted Room]] - Risk/reward for [[Corruptions]]
- [[Merchant Room]] - Buy [[Mutations]] before the boss
- [[Chamber of Lost Time]] - Rare, unique mechanics

### Mini-Boss
Each Floor ends with a Mini-Boss:
- Randomly chosen from the Dungeon's boss pool
- Rewards progression to next Floor
- Examples: [[Xarenthor, The Shadow Weaver]], [[Kyrektor, The Stormcaller]]

---

## Floor Flow

1. **Anomaly revealed** - See what you're up against
2. **Clear Rooms** - Earn resources, Blessings, Corruptions
3. **Merchant Room** - Buy Mutations to adapt
4. **Mini-Boss** - Defeat to proceed

---

## Design Notes

- Anomalies should encourage using different classes
- Merchant Room placement before boss allows last-minute adaptation
- Floor difficulty scales within a Dungeon

---

## Related

- [[Dungeons]]
- [[Rooms]]
- [[Anomalies]]
- [[Mutations]]
