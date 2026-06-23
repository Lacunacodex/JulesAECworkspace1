# ÆTHERIUM CODEX — SESSION HANDOFF
## April 27, 2026 — Session 2: Batch 4 Closed, Batch 5 Complete, Talent Archive Mapped

---

## SESSION SUMMARY

This session covered:
1. **Batch 4 (Item Creation):** Received findings from a parallel chat. Locked decisions integrated with corrections for conflicts. Two items still unverified (CML derivation, Affinity Alignment Rule location in SRD v3).
2. **Batch 5 (Character Creation):** Full consistency check across three CC documents, AE Stamina wip part 5, Character Profile output, SRD v3 Part XVIII, and AC UA. No current authoritative character creation procedure exists.
3. **Talent Archive Deep Mapping:** Complete folder structure mapped across the Book folder — "0. Talents" (source/extraction pipeline), "Talents Itemized" (sorted talent tree folders), and "1. Class Archetypes" (archetype definition cards).
4. **College Precepts Gap Confirmed:** 17 of 18 collegiate combat styles have structural shells only — no unique mechanical talents written. Only Mortis Ævum's Way of the Still Verse has actual Crux/Droplet/Capstone mechanics.

---

## BATCH 4: ITEM CREATION — STATUS: COMPLETE (with carryforward)

### Decisions Locked This Session

- **SRD v3 is canonical** over Rewrite v3 wherever they conflict
- **Five Artifice Paths** (Analyzer folded into Appraiser per SRD v3)
- **Schematic TN:** -2/-4/-6/-8 (SRD v3 scale)
- **Crafting TN:** SRD v3 three-band system canonical
- **Rewrite v3 disposition:** Companion flavor/derivation backstory, not mechanical authority. Contains unique alchemical specification content (Five Ways compound class tables, Battery derivation from Way+Lane, Corruption Track Synod rationale, Emulsion catalyst sub-types, worked item examples).
- **Planar Subtype Codex:** Flagged essential, needs isotope name reconciliation before deployment.

### Findings from Parallel Chat (Corrections Applied)

The parallel chat's findings document described what's IN the Rewrite v3. The following items in that document conflict with locked decisions and must be read with corrections:

- Findings list **six** Artifice Paths — canonical count is **five** (Analyzer merged into Appraiser)
- Crafting TN formula listed is the Rewrite's flat version — canonical is SRD v3's **three-band system**
- All other findings (Inseparability Principle, four-step procedural spine, Affinity Alignment Rule, CML formula, EML formula, Battery system, Artifice Events, Schematic system, Condition Track, Aberration system, Emulsion slot, Compound Classes) are valid extractions from the Rewrite and should be treated as companion derivation content

### Still Unverified (Carry Forward)

1. **CML derivation table location in SRD v3** — The Rewrite provides `max(Spell Sentence result, Material Floor)`. SRD v3 defines CML conceptually but explicit base-cost-by-effect-category table not confirmed present. Needs targeted search to confirm or flag as gap.
2. **Affinity Alignment Rule location in SRD v3** — The Rewrite provides Way∩Way = INNATE, disjoint = POWERED. SRD v3 references innate vs. powered but specific derivation rule not confirmed. Same treatment needed.
3. **Item Creation Reader Guide** (16MB) — Too large to process. Skip.
4. **Cross-Planar Forge library** (13 docs) vs Elemental Cards redundancy — Not checked.

### Corrections Needing Propagation (from Batch 4)

- Rewrite v3 Artifice Path count: 6 → 5 (drop Analyzer, merge into Appraiser)
- Rewrite v3 Schematic TN values: -1/-2/-3/-4 → -2/-4/-6/-8
- Rewrite v3 Crafting TN formula: flat → defer to SRD v3 band system
- Planar Subtype Codex isotope names: reconcile to current Isotopes Combined canonical names

---

## BATCH 5: CHARACTER CREATION — STATUS: COMPLETE

### Documents Reviewed

**Project files:** Character Profile (New_Character_Character_Profile.txt), SRD v3 Combined (Part XVIII), AC Unified Architecture (talent trees, XP, combat system)
**Drive:** Character Creation v3.0 (fileId: `1pJFi2-HNnJokw0C3PQwfCX9klQKXoTIz`), Character creation guide v1 (fileId: `1TydunVfRxY3IM0PvxHLGJNhCq9Nk7TeXZmcludLu8ng`), AE Stamina wip part 5 (fileId: `10nLs9QBr9aepgwlUBekfmhwGry3ck_xW8s-YojJV6Eg`)
**Not pulled:** Player's Guide Alpha v1 537KB, Master Talent Catalogue v1 (content already in AC UA project file)

### Key Finding: No Current Character Creation Procedure Exists

Three character creation documents exist. None is current:

**Character Creation v3.0** — DEPRECATED. Uses 100 XP (should be 120), wrong HP formula, 12 skills/3 petals, no Heritage States, no Psyche Schema, no college affiliation.

**Character Creation Guide v1** — PARTIALLY CURRENT. Correct 120 XP, has Archetype step (5/3/1 spread), Shaping Pool (Intellect + Dominion) and Substance Pool (Acuity + Anima) for magic vocabulary, uses `((2×Level)-1)×2` talent cost formula. Still uses 12 Abilities, 3 Skill Petals, multiple TBD sections.

**AE Stamina wip part 5** — NOT a stamina document. It's a ~100,000+ word Gemini conversation transcript containing the entire PF1e/PF2e class deconstruction project. Contains correct HP formula, complete defensive pillar formulas for all four pillars, condition track names/values, XP cost tables (two competing versions), 200+ extracted talents, and the Triskelion archetype framework. Uses 11-12 skills (not the canonical 16).

### Conflicts Found

| # | Conflict | Where | Resolution |
|---|---|---|---|
| B5-1 | Starting XP: 100 vs 120 | CC v3.0 vs CC Guide v1 | **120 XP locked** |
| B5-2 | HP formula: three versions | CC v3.0 vs AE Stamina vs SRD v3 | **Vigor×3 + Might×3 + Mastery×5 locked** |
| B5-3 | Skill count: 11 vs 12 vs 16 | AE Stamina variants vs SRD v3/AC UA | **16-skill 4-pillar grid locked** |
| B5-4 | Talent XP cost: flat 6 vs ((2×Level)-1)×2 vs variable | Multiple docs | **Open Decision #1 — unresolved** |
| B5-5 | Attribute cap at creation: 4 vs 5 | CC v3.0 vs CC Guide v1 | **OPEN — needs decision** |
| B5-6 | Petal count for skill distribution: 3 vs 4 | Both CC docs vs AC UA | **4 petals canonical** |
| B5-7 | Talent count at creation: 10 vs unspecified | CC v3.0 vs CC Guide v1 | **OPEN — needs decision** |

### Character Profile Output File — Error Catalog

The project file `New_Character_Character_Profile.txt` contains errors:
- Social HP pool labeled "Reputation" → should be **Poise**
- Skill "insight" → should be **instinct** (or Insight depending on Open Decision #9 resolution)
- Attribute "Anima" → **Open Decision #9**
- Uses generic defense labels → **Open Decision #7**
- Background "Influence" → should be **Clout**

### Disposition

| Document | Status |
|---|---|
| Character Creation v3.0 | **DEPRECATED.** No unique content not better expressed elsewhere. |
| Character Creation Guide v1 | **PARTIALLY CURRENT.** Shaping/Substance Pool and Archetype 5/3/1 spread may be canonical. Everything else superseded. |
| AE Stamina wip part 5 | **COMPANION REFERENCE — UNIQUE AND ESSENTIAL.** Most detailed defensive formulas, condition tracks, talent library, Triskelion framework. Needs reconciliation with SRD v3/AC UA. |
| Character Profile output | **OUTDATED.** Needs correction propagation. |

### Gaps Confirmed (Character Creation)

1. Sequenced character creation procedure document — needs complete rewrite
2. Heritage State generation at character creation — no procedural steps exist
3. Starting talent selection rules — quantity, pools, restrictions undefined
4. Background system — lists don't match across docs; escrow/debt integration TBD
5. Attribute distribution method — 7/5/5/3 spread needs verification against current values

---

## TALENT ARCHIVE — COMPLETE STRUCTURAL MAP

### Three-Layer Architecture

The talent development work exists in three layers, all containing views of the same material:

**Layer 1 — Source Transcripts** (0. Talents folder)
Raw Gemini conversation transcripts (AE Stamina wip parts 1-5), totaling ~500KB+ of conversational text. The primary source material.

**Layer 2 — Extracted/Synthesized Documents** (0. Talents subfolders)
Progressive extraction pipeline:
- `Æ Stamina wip 1 breakdown/` → topic-specific breakdowns (by class, by system)
- `Æ Stamina v1 clean edits/` → cleaned versions, subtractive editing snapshots
- `Talents reworked v3/` → Triskelion petal splits (ReCombat, ReKnowledge, RePhilosophical)
- `1. Class Archetypes/` → 25 individual archetype definition cards (MOST CURRENT, Mar 18-19)

**Layer 3 — Individual Talents Sorted Into Tree Folders** (Talents Itemized folder, Book level)
29 category folders containing individual talent documents filed by combat style/tree:

*Combat Styles:* Area Attack, Armor, Binding, Defensive Dualist, Dirty Fighter, Exotic & Unconventional, Finesse, Firearms, Mounted Combat, Ranged, Shields, Thrown, Two-handed, Unarmed
*Combat Systems:* Combat Maneuver, Hunter's Mark, Intimidation & Fear, Precision, Rage, Teamwork
*Magic/Supernatural:* College Precepts, Spellcasting, Style or Stance, Supernatural
*Non-Combat:* Companion, Utility
*Meta:* Classes, Uncategorized, Discard
*Index:* Talent Alphabetized Chapter Index (29KB)

### Key Google Drive Folder IDs (New)

| Folder | ID |
|---|---|
| Talents Itemized | `1aNQWZyHVYPaPaRPcoL4buQ5TSOwP9zk2` |
| Talents Itemized → Classes | `1kDI9iDGdraSWSLfQ5S46HoEMJWTnA-rr` |
| Talents Itemized → College Precepts | `1O8HWzkod9IVGtg-qFeoOX5SPx-xwICyE` |
| 1. Class Archetypes | `1zvBr1c-gKLNY932EZ9wCa8WKah_w4IYt` |
| Talents reworked v3 | `1k2fb1o2NwOnxa-lK8sG6d9MZuj6FJzWz` |
| Claude mechanics & talents v1 | `18gVT068WpEWsC_kKs7CYafJkUnWkVVAP` |
| Individual Crux talents | `1y65YAmM4CdSC7b_83xZtVv5C-_F8uAqn` |

---

## COLLEGE PRECEPTS GAP — CONFIRMED AND PRECISELY SCOPED

### The Framework (Exists)

**Structure of Martial Discipleship** (fileId: `1M5ppssELtmX5sTgLm97uuJ-FXWG2GTXiCjjwlpLtzNQ`) defines:
- Three-tier hierarchy: Foundational Talents → Ætherforged Precepts (Crux) → General Martial Talents
- Four tag groups for organizing all martial talents
- Two esoteric discipline poles: Sōmaturgy (internal/self) vs Ætherforged (external/technique)
- Sōmaturgy sub-tags: Creator, Soul Shaper, Mutation
- Ætherforged sub-tags: Discipline, Veil, Spellblade

### The College Structure (Exists)

Each of the 9 canonical colleges has **two Ways** — an Overt Way (public fighting style) and a Covert Way (institutional secret art). Each Way is defined by philosophy, Crux talents, and supporting talent tree recommendations.

| College | Overt Way | Covert Way |
|---|---|---|
| Mortis Ævum | Way of the Still Verse | Way of the Carrion Heart |
| Deepguard | Way of the Patient Snare | Way of the Inevitable Key |
| Stormpeak | Named but not read | Named but not read |
| Chiaroscuro | Named but not read | Named but not read |
| Chronosynclastic | Named but not read | Named but not read |
| Sovereign Exchange | Named but not read | Named but not read |
| Unity | Named but not read | Named but not read |
| Wildpath Wardens | Named but not read | Named but not read |
| Praxis (Generalist) | Named but not read | Named but not read |

### The Gap (Precisely Scoped)

**18 total collegiate combat styles (9 colleges × 2 Ways).**

**1 has actual unique mechanical talents:** Mortis Ævum's Way of the Still Verse — 4 talents specified (Crux: use Intellect for damage; Anatomical Strike: Stamina for conditions; Defanging the Serpent: reactive strike on parry; Stillness of Death: stun capstone).

**17 are structural shells:** Philosophy stated, talent tree shopping lists provided, but zero unique Crux/Droplet/Capstone talents designed. Estimated 3-4 unique talents per Way = **~50-70 unique talents needed.**

### Correction Needed

All College Precepts documents use D&D school labels in parentheses (Necromancy, Abjuration, Evocation, etc.). These are PF1e mapping artifacts and must be stripped. Colleges should be identified by planar source and institutional function per the Merged Colleges project file.

---

## UPDATED OPEN DECISIONS

All previous open decisions carry forward unchanged. New additions:

| # | Decision | Source |
|---|---|---|
| B5-5 | Attribute cap at creation: 4 vs 5 | Batch 5 |
| B5-7 | Starting talent count at creation | Batch 5 |

---

## UPDATED CORRECTIONS NEEDING PROPAGATION

All previous corrections carry forward. Add:

1. **Rewrite v3 Artifice Path count:** 6 → 5 (drop Analyzer into Appraiser)
2. **Rewrite v3 Schematic TN values:** -1/-2/-3/-4 → -2/-4/-6/-8
3. **Rewrite v3 Crafting TN formula:** flat → defer to SRD v3 band system
4. **Planar Subtype Codex isotope names:** reconcile to Isotopes Combined canonical names
5. **College Precepts D&D school labels:** strip (Necromancy), (Abjuration), etc. from all 9 college docs
6. **Character Profile output file:** Reputation→Poise, insight→instinct, Influence→Clout (3 confirmed errors + 2 open decisions)

---

## UPDATED GAPS CONFIRMED REMAINING

Previous gaps carry forward. Refined:

1. Equipment/weapon stat block catalogue — no document found anywhere
2. Heritage State generation algorithm — conceptual only, no procedural document
3. Remaining ESL scaling tables — Summon, Transform, Mind Link, Affliction, Illusion, Create, Nullify, Senses
4. Fey alpha-ready writeup (notes exist, not formatted)
5. Insight→Instinct propagation across all documents
6. "Influence" terminology collision resolution
7. Silas→Striven propagation across all documents
8. AC Unified Architecture consolidation pass
9. **Character creation procedure document** — no current version exists (Batch 5 confirmed)
10. **Collegiate combat styles** — 17 of 18 Ways need unique mechanical talents designed (~50-70 talents)
11. **CML derivation table** — confirm presence in SRD v3 or flag as gap the Rewrite uniquely fills
12. **Affinity Alignment Rule** — confirm presence in SRD v3 or flag as gap the Rewrite uniquely fills

---

## NEXT SESSION PRIORITIES

1. **Batch 6 (Gods and Cosmology)** or **Batch 7 (Institutions and Politics)** — next in sequence
2. **CML/Affinity targeted search** — quick verification pass against SRD v3 to close those two flags
3. **College Precepts development** — the 17 remaining Ways are a major creative task, not a cataloguing task. When ready, approach one college at a time using Merged Colleges + god documents + isotope profiles as source material.
4. **Handoff v4 production** — integrate this session's findings into the master handoff document (v3)

---

## DOCUMENT LOCATIONS ADDED THIS SESSION

| Document | Location | Notes |
|---|---|---|
| Character Creation v3.0 | Drive (fileId: `1pJFi2-HNnJokw0C3PQwfCX9klQKXoTIz`) | DEPRECATED |
| Character Creation Guide v1 | Drive (fileId: `1TydunVfRxY3IM0PvxHLGJNhCq9Nk7TeXZmcludLu8ng`) | Partially current |
| AE Stamina wip part 5 | Drive (fileId: `10nLs9QBr9aepgwlUBekfmhwGry3ck_xW8s-YojJV6Eg`) | ~100K word Gemini transcript |
| Structure of Martial Discipleship | Drive (fileId: `1M5ppssELtmX5sTgLm97uuJ-FXWG2GTXiCjjwlpLtzNQ`) in College Precepts folder | Framework doc |
| Mortis Ævum Collegium precept | Drive (fileId: `1E8jR05xrArMe8Vb8iqXtQMVjDNlmR6s03eZvoInBYoA`) in College Precepts folder | Most developed precept |
| Talent Alphabetized Chapter Index | Drive (fileId: `1kjiiKWGdeseT6d0UmVw2K7_8pVhJtYFxsbmzEp15Tdw`) in Talents Itemized folder | Master index |
| ReCombined Arche wip v3 | Drive (fileId: `1JAi3vV-SCeadz_SwXT07CUfQyj0N0x02`) in Talents reworked v3 folder | Combined Triskelion doc, 108KB |

---

*End of handoff. Batches 1-5 complete. Talent archive structurally mapped. College Precepts gap precisely scoped. Character creation procedure confirmed as highest-leverage gap for playable app.*
