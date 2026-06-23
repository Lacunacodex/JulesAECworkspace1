# ÆTHERIUM CODEX — SESSION HANDOFF DOCUMENT
## Batch Processing Guide for Alpha Assembly

*This document is the continuity bridge between Claude sessions. Upload it to the Claude project. Each batch section should be updated with findings after its pass is complete.*

---

## HOW TO USE THIS DOCUMENT

When starting a new session, tell Claude: "Read the handoff document first." Claude should search project knowledge for this file before doing anything else. Each batch has a status field — update it after completing work. The FINDINGS section under each batch is where results go so the next session inherits them.

---

## PROJECT STATE AS OF APRIL 27, 2026

Alex is the sole creator of Ætherium Codex (ÆC), an original TTRPG system set in Tessera. The project has extensive source material across Google Drive, Claude project files, and uploaded session documents. A comprehensive inventory was completed identifying ~200+ documents across all locations. The project is approaching alpha-publishable state with most content existing but scattered and unreconciled.

### Document Locations
- **Claude Project Files:** ~37 files. Primary retrieval via project_knowledge_search.
- **Google Drive — Claude Specific / Book folder:** ~100+ files across 15+ subfolders. Accessible via Google Drive tools (search by parentId or keyword).
- **Google Drive — Unified Engine folder (parentId: 1jEyTEvQZwG26k433FPgQadAz-nCTje_v):** Complete 21-doc Narrative Engine spec in both .md and .docx.
- **Google Drive — Untitled folder (parentId: 16roZY5IOlscX2ZyWH88jpc_7O_e6NxZj):** Unified Architecture component documents including Doc 6B Worked Examples.
- **Session uploads:** Player Introduction/Quick Start, Player Survey, Player's Guide v4.1, Nomos PDF — these may or may not persist between sessions.

### Key Google Drive Folder IDs
- Claude Specific root: `1CvhYc2ka0h0Va8TY-hhQ-X-IdS2vFeA8`
- Book folder: `136az9-uHyiXwrBhzj8JbkEz-QxDu0sVw`
- Setting Lore & Gods Claude: `1OgJXWjgl0JCjcoWk743vRFHQyJ9CFOQt`
- Location subfolder: `1uoRoSX3N_m01AneiCfevIu93guFypb7C`
- Narrative Engine Alpha v1: `1jEyTEvQZwG26k433FPgQadAz-nCTje_v`
- Untitled folder (UA components): `16roZY5IOlscX2ZyWH88jpc_7O_e6NxZj`
- Talents folder: `1dpwfqvNykcJlD_E_N-zQ7mXqpVrNEL9F`
- Items & Materia: `1Wpsm_0Jap6tFUpS4wV4vjqzYlgZAN6g2`
- ÆC Complete Gamebook (chapter structure): `1wTw3Hs3X985GUT7fTIgYulsEAHdqWeg0`

### Open Decisions (unresolved — do not assume answers)
1. XP cost formula for talents — flat 6 vs BEL/FEL×3 vs ((2×Level)-1)×2
2. First-dot skill cost — 3 XP special case vs New Rating × 2
3. Crafting EML cap — hard cap at wielder Mastery vs caveman-grenade model
4. Daredevil Engine — promote to 9th Foundational Style or keep in General Pool
5. Ancestries in alpha — placeholder or exclude

### Confirmed Decisions (propagate, do not re-debate)
- Starting XP: 120 (not 100)
- Resolution: d20 (not 2d20)
- HP formula: Vigor×3 + Might×3 + Mastery×5
- ÆP/Construction Pool: Book of Shadows formula canonical; character sheet OUTDATED
- Skills: 16-skill 4-pillar grid (not 12-skill mundane/magical pairs)
- "Insight" renamed to "Instinct" (Metaphysical skill)
- Week = 8 days; Recharge base interval = 10 minutes
- Anchor cap: ceil(Base EML/2)
- Effects list: 23+Variable canonical
- Five-degree critical system

### Recurring Errors to Watch For
- Importing external framework affect (Spenglerian decline, "dark fantasy") onto a setting that is ongoing, not declining
- Guessing at setting content instead of reading source files first
- Conflating Palimpsest functions with Synod functions
- Reducing the Legacy system to forward-facing achievement triggers
- Importing 5e or Pathfinder aesthetics into setting design
- Making design recommendations that flatten cognitive complexity

---

## BATCH 1: CORE ARCHITECTURE

**Status:** NOT STARTED

**Purpose:** Confirm which version of overlapping content is canonical. Identify what the Compiled Alpha already reconciles. Establish the single source of truth for the system's spine.

### Documents to Review

**In Claude Project Files:**
- ÆC Operating Philosophy (Document 0) — `0__ÆC_Operating_Philosophy_Final_1.docx`
- AC Unified Architecture — `AC_Unified_Architecture.md`
- SRD v3 Combined — `1__SRD_v3_Combined.md`

**On Google Drive (fetch via Drive tools):**
- ÆC Operating System Compiled Alpha v1 (448KB, fileId: `1HRI0kxuJH5V5JNREWchtMzy82Rr3ql0p`)
- AC Errata Documents 1 and 2 (fileId: `1xpcCRWHOXrAnmfTE6M1pVhSlV_v-UaFJ`)
- AC Skill Effect Matrix (fileId: `1h4QN1eTgBtGwCFD6glFHQmACAsgPMN3s`)
- AEC_Alpha_Build_Order (fileId: `17csQb9-ES-4db83hLMiRH5knXImLnQkc`)
- AEC_Master_Catalog (fileId: `16IfsEDVpTGxHoHWRoiIv_bL2WuwQQ3nt`)
- AEC_Battle_Plan (fileId: `1pDmb6PhYGfSfcmpZmgbn1_RUGzxGm5kf`)
- AEC_Strategy_Sanity (fileId: `1bOBJqCxnMjlMA6GgC8Wx1tpPy2v05N66` — 43KB version)

### What to Look For
1. Does the Compiled Alpha v1 already contain reconciled versions of systems that are in conflict across individual files?
2. What does the Errata document correct? Does it resolve any of the open decisions?
3. Does the Skill Effect Matrix map the 16-skill grid to the effects list? This would close the petal-to-skill crosswalk gap.
4. What does the Master Catalog list as canonical versus deprecated?
5. Does the Battle Plan or Strategy Sanity contain timeline or priority decisions that affect batch ordering?

### Specific Conflicts to Check
- Construction Pool formula: character sheet vs Book of Shadows (believed resolved — BoS canonical per SRD v3 Amendment 8B, but verify in Compiled Alpha)
- XP cost formula: check if the Compiled Alpha or Errata locks one of the three options
- Skill architecture: confirm 16-skill grid is reflected throughout, no 12-skill remnants

### FINDINGS
*(Fill this section after completing the batch pass)*

---

## BATCH 2: NARRATIVE ENGINE

**Status:** NOT STARTED

**Purpose:** Verify all 21 docs of the Unified Engine spec for internal consistency. The set is confirmed complete (Doc 6B found in Untitled folder).

### Documents
All in Drive folder parentId: `1jEyTEvQZwG26k433FPgQadAz-nCTje_v`
- Docs 0, 1A, 1A Addendum, 1B, 2A, 2B, 3A, 3B, 3C, 4A, 4B, 4C, 5A, 5B, 5C, 6A, 7A, 7B, C1, R1
- Doc 6B in Untitled folder (fileId: `1m-4uRVAe3jKynH81pjGZ5cvlmzqHo8ax`)
- Also compare Psyche Schema v2 (project files) against v4 (Drive, fileId: `1Hg9ekta8FX09CJ5HeceU5qwJZ-oQkr0_`)

### FINDINGS
*(Fill after pass)*

---

## BATCH 3: MAGIC SYSTEM

**Status:** NOT STARTED

**Purpose:** Confirm full magic chain from cosmology → isotopes → Spell Sentence → Construction Pool → casting philosophies → alchemy.

### Documents
**Project files:** SRD v3 Combined, AC Unified Architecture (Docs 4c sections), ÆC Isotopes Combined, Turbulent/Laminar Flow
**Drive:** Book of Shadows v6 (fileId: `1oNL57Eu5xvPmEqSGTAGYKbc7q8ElrHf3`), Five Ways Framework (fileId: `1-JNMYbH0tkaR4aABo4EVFuj2u4n__GmqmNCSEditje0`), Way 1-5 individual docs, Social combat PDF (fileId: `117A3GVs7Tr5TM_HLVOlrVYjNOKWNXpmg`), Dual sources of magic (fileId: `1aVxbML0baf_6jXkPIuOG6FZ7hTzdrfoUlyWuuYnVuLo`)

### FINDINGS
*(Fill after pass)*

---

## BATCH 4: ITEM CREATION

**Status:** NOT STARTED

### Documents
**Drive:** Item Creation Rewrite v3 (fileId: `1cvT6yZGZ9HK5XvF3LzC7WtQUwKVN56V3`), Item Creation Reader Guide 16MB (fileId: `1zQ772tu0Dx1g1PZZdwxGG_NlZBJbfNYf`), Cross-Planar Forge library (13 numbered docs in Book folder), Planar Subtype Codex (fileId: `1jikQ6JO3vhkwchMwtjyuZ_PQnDLgGpe3VwkkdR5AGbI`)
**Project files:** SRD v3 (value curve), AC Unified Architecture (Artifice paths)

### FINDINGS
*(Fill after pass)*

---

## BATCH 5: CHARACTER CREATION

**Status:** NOT STARTED

### Documents
**Session uploads:** Player Introduction/Quick Start, Player Survey, Player's Guide v4.1 (parts donor)
**Project files:** Character Profile, AC Unified Architecture (talent trees, XP)
**Drive:** Character creation guide v1 (fileId: `1TydunVfRxY3IM0PvxHLGJNhCq9Nk7TeXZmcludLu8ng`), Player's Guide Alpha v1 537KB (fileId: `1e6qCXDEPFXoA_mL92UmLkMgXhZfgCfwa`), Character Creation v3.0 (fileId: `1pJFi2-HNnJokw0C3PQwfCX9klQKXoTIz`), Master Talent Catalogue v1 (fileId: `1vmDOJzPBZAqLi6F2x6sabkxV4LxKCCLN`), AE Stamina wip part 5 (fileId: `10nLs9QBr9aepgwlUBekfmhwGry3ck_xW8s-YojJV6Eg`)

### FINDINGS
*(Fill after pass)*

---

## BATCH 6: GODS AND COSMOLOGY

**Status:** NOT STARTED

### Documents
**Project files:** All 16 god documents, Synod of Endings, Lacuna Notes
**Drive:** Complete Pantheon Merge v1 (fileId: `1Vsg0_sZMvfpHEdOGW-q2vHt5cJQ3_pIy`), Kintsugi Cosmology (fileId: `1SVuPMLQgf4w7Y66EJJmKBpGGcToHG3giKUneT85hzm4`), Divine Comedies v1+v3, Merged Planes 55KB (fileId: `1d6yQz-g0MQ-W2cM7PtwMuZI2vsnslxVa`), Palimpsest.md (fileId: `1UMNTguhVoX4gQBsnRG12xn6yOBcT0J31`), individual plane files, Dominion of Dragons (fileId: `1e0eKfOxVUaaegV2PjM8iRbdgHAb_875A`)

### FINDINGS
*(Fill after pass)*

---

## BATCH 7: INSTITUTIONS AND POLITICS

**Status:** NOT STARTED

### Documents
**Project files:** Merged Colleges v1, Political Zoetrope v2, Society & Technology
**Drive:** Political Zoetrope v3 (fileId: `1Z-OiUhpcgP0ePIDDf67nIym-XzLvQgfkZd24-QCt9Dk`) — SUPERSEDES v2, Political Alloys series (5 docs), Sounds of the Zoetrope raw+compiled, Location notes (fileId: `1r83OfIz4iTo6Ep9ZhwlXsDQwkygxjuTf`), World refinement v1+v2

### FINDINGS
*(Fill after pass)*

---

## BATCH 8: CREATURES, COMPANIONS, GUILDS

**Status:** NOT STARTED

### Documents
**Project files:** Combined Companion Archetype & Creature Types, Aetheric pet system (contains guild system), Fey notes
**Drive:** Part 3 The Profession & Guilds (fileId: `1bNoQc2M57w4zVQPjxSUIt0vs_2DtvI-tyfHcowur5Go`), Pet System (fileId: `1zc3k2v8mAWMK48qDm2REJvVmhTkptV25abpHyHjcZV8`), Doc 4d Crafting & Companions (fileId: `1X0SDrOHPcnf4fEZHI_H_VGT6GubF-Ub_`)

### FINDINGS
*(Fill after pass)*

---

## BATCH 9: ISOTOPE CONTENT LIBRARY

**Status:** NOT STARTED

### Documents
**Project files:** ÆC Isotopes Combined, Elemental Cards Alpha
**Drive:** Cross-Planar Forge library (13 docs), Reality Paradox Borderlands+Palimpsest Primary (2.5MB each), Biotic Paradox Verdant+Synod Primary (1.8MB each)

### FINDINGS
*(Fill after pass)*

---

## BATCH 10: ADVENTURE AND GM TOOLS

**Status:** NOT STARTED

### Documents
Previously uploaded adventure generator compilations + Narrative Engine Docs 5B and 3C from Batch 2

### FINDINGS
*(Fill after pass)*

---

## BATCH 11: TALENT DEVELOPMENT ARCHIVE

**Status:** NOT STARTED

### Documents
**Drive (Talents folder, parentId: 1dpwfqvNykcJlD_E_N-zQ7mXqpVrNEL9F):**
Complete Talent System Inventory v2 (fileId: `1UxaDz_U9rtY5MgmUu8l_52Gr25_yNrm2`), Missing Talents v22 (fileId: `1zIrxiQPASM8-LJbo0jTBQO2b0vkiCXGcH2PT4exuzhw`), Martial Talents Final Archive (fileId: `1oF7Ji2UnvYqfEmsFxUAarApwyE0Im8aT8BL6DxJVxxo`), General & Utility v3 (fileId: `1lxF3wLc4UPSD27tnGllVWRS0RxCwxhIr`), Talents copy doc 168KB (fileId: `1gQvFHh6sj8imM8STXiS5MywUEOYEFCDDNUeD6hM4YA4`), ÆStamina extraction pipeline

### FINDINGS
*(Fill after pass)*

---

## GAPS CONFIRMED REMAINING (genuine writing needed)

These are items where no existing document was found during the deep dive:

1. Equipment/weapon stat block catalogue — no document found anywhere
2. Heritage State generation algorithm — conceptual only, no procedural document
3. Remaining ESL scaling tables — Summon, Transform, Mind Link, Affliction, Illusion, Create, Nullify, Senses (narrowed from original list; Damage, Weaken/Enhanced Trait, Protection, Movement, Panacea, Chronos are DONE in SRD v3)
4. Petal-to-skill crosswalk table (may be in Skill Effect Matrix — check in Batch 1)
5. Fey alpha-ready writeup (notes exist, not formatted)
6. Insight→Instinct propagation across all documents
7. "Influence" terminology collision resolution

## GAPS CLOSED BY DEEP DIVE

- Psyche Schema v4 — EXISTS on Drive
- Character creation procedure — EXISTS on Drive (early version)
- Guild system — EXISTS in Aetheric Pet System + Part 3 document
- Crafting system — EXISTS and resolved (Item Creation Rewrite v3)
- Five Ways alchemy framework — EXISTS on Drive
- Palimpsest-as-place description — EXISTS on Drive
- Geography/location reference — EXISTS on Drive
- Construction Pool formula — DECIDED (BoS canonical per Amendment 8B)
- Doc 6B Worked Examples — EXISTS in Untitled folder
- All 21 Narrative Engine docs — EXIST and COMPLETE on Drive
- Social combat notes — EXISTS on Drive
- Oracle Tables — EXISTS as Doc 5B
- Faction Turn Procedures — EXISTS as Doc 3C
