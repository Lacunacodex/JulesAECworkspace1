# TERMINOLOGY.md — Ætherium Codex Locked Terms & Renames

*Single source of truth for terminology changes. Referenced by `AGENTS.md` §8.*
*Last revised: 2026-06-22.*

> **STATUS — draft for reconciliation.** This table is compiled from the locked-decision set. Because **errata currently trails the decision log (conflict C3)**, some source documents still frame these renames as open or unapplied. Verify against the live decision log before treating any single row as final. Flag, do not silently update, where a document conflicts with this file.

---

## THE RULE

**Never blind find-replace.** Every row below has a defined scope. Several deprecated strings remain *correct* in specific contexts (the "Kept usages" column). A global swap will corrupt those usages.

---

## Locked renames

| Old string | Current | What changed | Kept usages — old string still correct when… | Decision |
| --- | --- | --- | --- | --- |
| **Anima** (attribute) | **Essence** | Metaphysical *attribute* renamed | "Anima" the **god**; "**Anima's Law**" / the Primal Current (cosmological term) | OD-4 |
| **Integrity** (attribute) | **Moiety** | Metaphysical *attribute* renamed | "Integrity" as the **Metaphysical Deflect defense name** (Part VII canonical) | CF-17 |
| **Metaphysical Resist** | **Coherence** | Defense renamed (resolves Essence collision) | — | DEF-1 |
| **Poise** (condition track) | **Reputation** | The Social **condition track** renamed | "Poise" as the **Social HP pool** (the HP pool keeps the name) | — |
| **Silas** (Moros aspect) | **Striven** | Moros aspect renamed | "Silas" as **Heart's Compass Silas** (Affectionate Love / Philia) — a different entity | — |
| **Thrallherd** | **Hyphena / MNI** | Renamed | — | OD-15 |
| **Petals** | **the four pillars** (Physical / Mental / Social / Metaphysical) | Restructured into pillars | — | OD-5 |

## Dissolved / restructured (not simple renames)

| Old | Disposition | Notes |
| --- | --- | --- |
| **Dolor** | **Dissolved** | Not renamed. Vestus absorbed its slot. Rework contextually; do not swap for a single word. |
| **Vestus** (standalone dimension) | **Folded into Moros** | The string survives, but its role changed: it is now the **second aspect of Moros** (Moros = Striven / Vestus). Core Philosophy moved **11 → 10** paired dimensions. |
| **Ki Pool** | **Dissolved into FP** | The unified Fulcrum Point pool absorbs it. | OD-12 |

---

## High-risk collisions — expanded

These four cause the most damage under a careless replace.

- **Anima.** KEEP for the god and for *Anima's Law* (Primal Current). The renamed **attribute** is **Essence**. Both are valid in their own contexts.
- **Integrity.** KEEP as the **Metaphysical Deflect** defense name. The renamed **attribute** is **Moiety**.
- **Poise.** KEEP as the **Social HP pool**. The renamed **Social condition track** is **Reputation**. *(Track steps, pending confirmation: Flustered → Humbled → Disgraced → Rapt → Broken.)*
- **Silas.** KEEP for **Heart's Compass Silas** (Affectionate Love / Philia). The former **Moros aspect** Silas is now **Striven**.

---

## Metaphysical attribute line + propagation

- **Full line:** **Moiety / Dominion / Essence.**
- This is the **least-propagated** rename (last count: Moiety appeared ~7 times against ~34 expected). Propagate **manually and contextually**, not by blind replace — Integrity (defense name), Anima (god), and Poise (HP pool) all have kept usages that a sweep would clobber.
- Formula references to update where they still show old attribute names:
  - **Pattern pool** = (Moiety × 3) + (Essence × 3) + (Mastery × 5)
  - **Construction Pool** includes Moiety
  - **Mutation threshold** = Moiety × 5
  - Metaphysical **Soak / Threshold / Deflect** formulas reference the **Moiety** attribute

---

## Not-yet-applied (a conflict, not an error)

- **C1 — Moros restructure.** If you find the Core Philosophy still showing the **old 11-pair model with standalone Vestus** (and/or a live "Dolor"), that is the known C1 conflict. **Flag it; do not silently update.**

---

*Maintenance: when the decision log advances, update this file first, then let `AEC Jules Compilation V# [date]` runs reference it. AGENTS.md carries only the never-blind-replace rule and the four high-risk callouts — this file holds the full set.*
