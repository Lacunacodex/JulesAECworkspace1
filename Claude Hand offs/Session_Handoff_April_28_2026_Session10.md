# ÆTHERIUM CODEX — SESSION HANDOFF
## April 28, 2026 — Session 10: Category 2 Verifications + Category 3 Design Decisions

---

## SESSION SUMMARY

This session onboarded a new Claude instance via all 10 prior handoff documents + Cross-Reference Index, then executed Category 2 formula verifications and Category 3 design decisions.

1. **Full session history ingested.** All 10 handoff documents (Sessions 1–9) read in sequence. Cross-Reference Index read. Complete project state absorbed.
2. **File Triage Checklist produced.** Actionable checklist with Google Drive file IDs — ~50 files to KEEP, ~30 to ARCHIVE, organized by category with checkboxes.
3. **Two pending decisions from Session 9 resolved:** HP-1 (keep HP) and FS-1 (ten-step Formation Stage).
4. **Category 2 formula verifications completed.** Five of seven items verified clean across project files. Two propagation tasks identified. One structural task remains.
5. **Five Category 3 design decisions locked.** OD-1 (XP costing), OD-19 (petals = identity), OD-5 (petals → pillars, 9/7/5/3), OD-8 (pillar-specific defenses), OD-20 (Weapon Focus/Spec → single scaling). One deferred (OD-6, FP pool sizing).

---

## DECISIONS LOCKED THIS SESSION

| # | Decision | Resolution | Impact |
|---|---|---|---|
| HP-1 | Keep "HP" as canonical abbreviation? | **YES — keep HP, define on first use per document.** | Removes ~66 AC UA + ~22 SRD v3 hits from terminology audit scope |
| FS-1 | Formation Stage scale? | **Ten-step (1-10) is canonical.** SRD v3's 1-4/5-7/8-10 bands are correct. | Isotopes Combined needs all 64 entries remapped from 1-5 to 1-10 |
| OD-1 | XP talent costing | **BEL×3 as base cost, prerequisite chaining discount as modifier.** Deep specialization gets cheaper. Requires BEL assignment for every talent (needed anyway for crosswalk). | THE domino. Unblocks session XP yield validation, character creation procedure, talent pricing for digital implementation. |
| OD-19 | Petal assignment model | **Petals = identity, not talent access gates.** Any petal can buy from any tree. | Removes organizational gatekeeping. Player-facing archetype labels remain meaningful as identity without restricting mechanical options. |
| OD-5 | Petal/pillar relationship | **Petals folded INTO the four pillars.** No separate petal layer. Physical/Mental/Social/Metaphysical serve that function directly. Skill distribution at creation: **9/7/5/3 across four pillars.** | Retires the old three-petal 9/7/5 system. Cross-Reference Index needs updating. Character creation procedure must use four-pillar skill distribution. |
| OD-8 | Defense axis names | **Pillar-specific (16 unique names).** Physical: Evasion/Guard/Toughness/Vigor. Mental: Willpower/Control/Conviction/Courage. Social: Grace/Dignity/Composure/Discretion. Metaphysical: Acuity/Integrity/Resilience/Essence. | Character Profile needs updating from generic Dodge/Deflect/Soak/Thresh. Old Part VII defense system is now canonical naming; Document 3 formula (Composite Defense = Dodge + Deflection, no base 10) is canonical math. **FLAG:** Name collisions between some defense names and attributes (Integrity, Composure, Essence) — may be intentional or may need disambiguation. |
| OD-20 | Weapon Focus/Specialization | **Single scaling talent.** One Crux that deepens through Droplets. Not two separate Crux talents. | AC UA Doc 4a needs updating. Aligns with BEL-based pricing and Crux/Droplet architecture. |

## DECISIONS DEFERRED THIS SESSION

| # | Decision | Reason |
|---|---|---|
| OD-6 | FP pool sizing / drip recalibration | Alex needs more time. The unified formula produces dramatically larger pools (18/65/152 vs 8/16/24). Fundamentally a playtesting question. |

---

## CATEGORY 2 VERIFICATION RESULTS

### Verified Clean — No Action Needed in Project Files

| Item | Formula | Status |
|---|---|---|
| Construction Pool formula | (½ Effect Tier) + (½ Isotope Tier) + Mastery + Integrity | Consistent in SRD v3 + AC UA |
| BER static model | BER is STATIC, base cost IS the BER, never scales with dots | Explicitly confirmed in SRD v3 Part IV |
| Pool formula | Same as Construction Pool | Consistent |
| ÆP cost formula | (ESL × 2) − 1 | Consistent in SRD v3 + AC UA |
| Starting XP = 120 | 120 XP | Confirmed in AC UA Unresolved Flags #13 + Part XII |

### Needs Propagation

| Item | Issue | Scope |
|---|---|---|
| S-09 Haunt → Wraith | SRD v3 already uses "The Wraith." ÆC Isotopes Combined still says "The Haunt." P-02 "The Haunt" (Palimpsest) stays. | Surgical — rename S-09 only in Isotopes Combined |
| Formation Stage scale | Isotopes Combined uses 1-2/3/4-5 (five-step). Canonical is now 1-4/5-7/8-10 (ten-step). | Bulk — all 64 isotope entries need Formation Stage band remapping |
| Character Profile output | Still has: Reputation→Poise, insight→Instinct, Influence→Clout, Anima→pending OD-9, generic defense names→pillar-specific | Read-only project file — needs source correction |

### Not Verifiable via Search

| Item | Issue |
|---|---|
| Companion doc v1/v2 merge | AC UA Flag #10: Lines 358-850 and 912-end concatenated. Structural dedup needed — manual pass required. |

---

## CORRECTIONS NEEDING PROPAGATION (Updated)

All previous corrections 1–21 carry forward. Add:

22. **Isotopes Combined S-09:** "The Haunt" → "The Wraith" (S-09 only; P-02 "The Haunt" stays)
23. **Isotopes Combined Formation Stage bands:** Remap all 64 entries from 1-5 scale to 1-10 scale (1-4/5-7/8-10)
24. **Cross-Reference Index petal section:** Retire "9/7/5 across Combat, Knowledge, Philosophy." Replace with "9/7/5/3 across Physical, Mental, Social, Metaphysical pillars"
25. **Cross-Reference Index Open Decisions:** Update to reflect current state (many resolved this session)
26. **AC UA Doc 4a Weapon Focus/Spec:** Merge into single scaling Crux talent with Droplet progression
27. **Character Profile defense names:** Replace generic Dodge/Deflect/Soak/Thresh with pillar-specific names from AC UA Part VII
28. **All documents using three-petal model:** Update to four-pillar model where petals are referenced

---

## UPDATED OPEN DECISIONS

### Resolved This Session
- OD-1: XP costing → BEL×3 + chaining discount
- OD-5: Four-pillar skill spread → 9/7/5/3
- OD-8: Defense names → pillar-specific (16 unique)
- OD-19: Petals = identity → LOCKED
- OD-20: Weapon Focus/Spec → single scaling talent
- HP-1: Keep HP → LOCKED
- FS-1: Formation Stage → ten-step (1-10)

### Still Open (carried forward)
- OD-2: First-dot skill cost — 3 XP special case vs New Rating × 2
- OD-3: Crafting EML cap — caveman-grenade model
- OD-4: Daredevil Engine — 9th Foundational Style or General Pool
- OD-6: FP pool sizing / drip recalibration — **DEFERRED, needs playtesting**
- OD-7: (absorbed into OD-8, now resolved)
- OD-9: Essence vs Anima (attribute name)
- OD-10: Mastery Capacity Pool — canonical or deprecated?
- OD-11: Guild interface track count — three or four tracks?
- OD-12: S-09 naming — **RESOLVED by propagation decision (Wraith canonical)**
- OD-13: Borderlands numbering — standardize to Solid-first?
- OD-14: (absorbed into FS-1, now resolved)
- OD-15: Effects vs Functions for the Forge — intentional or inconsistency?
- OD-18: Strategic doctrine model scope

### Net Open Decision Count: 10 (down from 18+2)

---

## UPDATED GAPS

Previous gaps 1–43 carry forward. No new gaps added this session. Gaps affected by this session's decisions:

- **Gap #5 (Character creation procedure):** Now partially unblocked. XP costing decided (OD-1). Skill distribution decided (9/7/5/3). Defense names decided. Still needs: Heritage State generation algorithm, starting talent selection rules, background system finalization.
- **Gap #38 (Archetype-to-Transmission crosswalk):** Now directly needed — BEL assignments for every talent require this crosswalk to exist.

---

## DOCUMENTS PRODUCED THIS SESSION

| Document | Location | Contents |
|---|---|---|
| AEC_File_Triage_Checklist.md | `/mnt/user-data/outputs/` | Complete file sort with Drive IDs: ~50 KEEP, ~30 ARCHIVE, checkboxes |
| Session_Handoff_April_28_2026_Session10.md | `/mnt/user-data/outputs/` | This handoff document |

---

## NEXT SESSION PRIORITIES (ORDERED)

### Immediate — Unblocked by This Session's Decisions

1. **Gap #5: Character creation procedure** — Now has: XP costing model, skill distribution (9/7/5/3), defense naming, starting XP (120), HP formula, attribute spread (7/5/5/3). Still needs: Heritage State generation, starting talent count/selection rules, background system. Highest-leverage output.
2. **Gap #38: Archetype-to-Transmission crosswalk** — Required for BEL assignments, which are required for talent pricing under the new OD-1 model.
3. **Correction #22-23: Isotopes Combined propagation** — S-09 rename + Formation Stage remapping (64 entries).

### Design Decisions Still Needed

4. **OD-9: Essence vs Anima** — attribute name. Affects Character Profile, defense name (Metaphysical defense "Essence" collides if attribute is also Essence).
5. **OD-6: FP pool sizing** — deferred, needs playtesting data or mathematical modeling.
6. **Remaining ODs (2, 3, 4, 10, 11, 13, 15, 18)** — lower priority, don't block critical path.

### Build Work

7. **Gap #40: Combat maneuver core resolution** — unblocks ~30 talents
8. **Gap #41: Rage state mechanics** — unblocks ~10 talents
9. **Gap #39: Remaining 14 Precept extractions**
10. **Gap #37: Talent deduplication pass**
11. **Correction #21: Full terminology audit on Talents copy doc**

---

## CUMULATIVE STATISTICS (Sessions 1–10)

| Metric | Count | Change |
|---|---|---|
| Batches complete | 11 of 11 | No change |
| Open decisions | **10** | −10 (7 resolved, 2 absorbed, 1 already resolved by propagation) |
| Corrections needing propagation | **28** | +7 |
| Confirmed gaps | 43 | No change |
| Conflicts awaiting Alex | 8 | −2 (OD-8 resolved, OD-12 resolved) |
| Category 2 items verified clean | 5 of 7 | New |
| Category 2 items needing propagation | 2 | New |

---

*End of handoff. Seven design decisions locked. Open decisions cut nearly in half (18+2 → 10). The XP costing domino (OD-1) is resolved — BEL×3 with chaining discount. Petals are retired as a separate layer; the four pillars now serve that function with 9/7/5/3 skill distribution. Character creation procedure is the highest-leverage next output, now partially unblocked. File triage checklist produced for Drive reorganization.*
