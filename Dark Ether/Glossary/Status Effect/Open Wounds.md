---
type: status_effect
category: Physical
tags:
  - dot
  - physical
  - bleed_synergy
  - severe
status: concept
---

# Open Wounds

## Description
**Open Wounds** is a severe form of physical trauma, deeper and more vicious than a standard [[Bleed]]. It represents a laceration so deep that it cannot easily close, causing continuous blood loss that worsens with movement.

## Mechanics

### Effects
1.  **Unstoppable Drain (Consume & Condense):** Upon application, **Open Wounds** consumes all active [[Bleed]] stacks on the target. It calculates the total remaining damage of these consumed bleeds, multiply it by 2 (100% more), and deals this total amount as Physical Damage over the duration of the Open Wounds effect.
2.  **Movement Penalty:** Enemies with Open Wounds take **10% increased damage** from all sources while moving.

### Duration
- Base Duration: 5.0 seconds.
- **Refresh Rule:** Open Wounds **cannot stack**. Applying Open Wounds to a target already affected by it calculates a new damage value based **only** on the currently active [[Bleed]] stacks.
    - If New Damage > Current Remaining Damage: The old effect is **replaced** by the new one.
    - If New Damage < Current Remaining Damage: The old effect continues and duration is refreshed
    - **Crucial:** The remaining damage of the previous Open Wounds effect is **never added** to the new calculation, preventing exponential scaling.

## Comparison to Bleed
| Feature          | Bleed              | Open Wounds                        |
| :--------------- | :----------------- | :--------------------------------- |
| **Stacking**     | Stacks infinitely  | Single "Super-Instance" by default |
| **Damage**       | Moderate DoT       | Massive Condensed DoT              |
| Default Duration | 5                  | 5                                  |
| **Mechanic**     | Basic health drain | Consumes Bleeds for Burst-DoT      |

## Sources
- **Critical Strikes** with specialized Blood skills.
- **[[Laceration Support]]**.
- **Certain Unique Items** (e.g., *The Flayed God's Edge*).

## Related
- [[Bleed]]
- [[Physical Damage]]
- [[Laceration Support]]
