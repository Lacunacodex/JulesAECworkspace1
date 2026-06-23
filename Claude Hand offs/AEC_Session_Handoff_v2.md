# ÆTHERIUM CODEX — SESSION HANDOFF DOCUMENT v2
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
3. Crafting EML cap — SRD v3 says Formation Stage hard-caps item EML (Material Tier = ceiling). The unresolved question is specifically: what happens when a low-Mastery character WIELDS a high-EML item? (The caveman-grenade model.) Check SRD v3 for whether this is addressed.
4. Daredevil Engine — promote to 9th Foundational Style or keep in General Pool
5. Ancestries in alpha — placeholder or exclude
6. FP unification — the (Attribute + Tc) × Mastery formula replacing old Stamina formula produces dramatically larger pools (18/65/152 vs 8/16/24 at starting/journeyman/master). Alex is reevaluating. Currently OPEN, do not carry as confirmed.
7. Pillar-specific defense axis names (Evasion/Guard/Toughness/Vigor etc.) vs generic Dodge/Deflect/Soak/Thresh — design decision needed
8. Success with Flaw in combat — five-degree system is canonical but the specific mechanical cost for combat SWF needs design work
9. Essence vs Anima — verify whether Document 1 renamed Anima to Essence. If the rename was NOT locked, revert to Anima.

### Confirmed Decisions (propagate, do not re-debate)
- Starting XP: 120 (not 100)
- Resolution: d20 (not 2d20)
- HP formula: Vigor×3 + Might×3 + Mastery×5 (all four pillars follow same structure with their respective attributes)
- ÆP/Construction Pool: Book of Shadows formula canonical; character sheet OUTDATED
- Skills: 16-skill 4-pillar grid (not 12-skill mundane/magical pairs)
- "Insight" renamed to "Instinct" (Metaphysical skill) — NOT YET FULLY PROPAGATED
- Week = 8 days; Recharge base interval = 10 minutes
- Anchor cap: ceil(Base EML/2)
- Effects list: 23+Variable canonical
- Five-degree critical system (applies to ALL checks including combat)
- Poise = Social HP pool (overrides Errata's "Reputation" designation)
- Moros Life aspect = Striven (renamed from Silas) — NOT YET FULLY PROPAGATED
- V11.4 crafting system is DEPRECATED — SRD v3 item creation system is canonical
- Crafting system source: SRD v3 Combined (Five Artifice Paths, Formation Stage quality table, material properties → Spell Sentence mapping, Legacy & Ascension)

### Corrections Needing Propagation
These are confirmed canonical answers that have not yet been applied across all documents:
1. **Insight → Instinct:** The fourth Metaphysical skill. Affects Iconic Talents doc (Unity, Chronosynclastic, Generalist sections), the Errata's skill table, and any other document referencing Metaphysical skills. The Compiled Alpha and SRD v3 may be clean; standalone talent/spell docs are not.
2. **Silas → Striven:** Moros Life aspect. The Compiled Alpha's Psyche Schema v4 section still shows "Silas (The Struggle)." Gods Section document is correct. Psyche Schema source file needs updating.
3. **Poise Pool standardization:** Social HP pool = Poise. Social condition track = Poise track (or needs a distinct track name). Any document using "Reputation Pool" for Social HP needs correction.
4. **HP formula in Character Creation v3.0:** That document has the wrong formula. Canonical is (Vigor×3 + Might×3 + Mastery×5). Character Creation v3.0 shows (Vigor + Might + Mastery × 2) producing 8 instead of 21.

### Recurring Errors to Watch For
- Importing external framework affect (Spenglerian decline, "dark fantasy") onto a setting that is ongoing, not declining
- Guessing at setting content instead of reading source files first
- Conflating Palimpsest functions with Synod functions
- Reducing the Legacy system to forward-facing achievement triggers
- Importing 5e or Pathfinder aesthetics into setting design
- Making design recommendations that flatten cognitive complexity
- Referencing V11.4 as canonical crafting system — it is DEPRECATED; SRD v3 is current

---

## BATCH 1: CORE ARCHITECTURE

**Status:** COMPLETE

**Purpose:** Confirm which version of overlapping content is canonical. Identify what the Compiled Alpha already reconciles. Establish the single source of truth for the system's spine.

### Documents Reviewed

**In Claude Project Files:**
- ÆC Operating Philosophy (Document 0) — `0__ÆC_Operating_Philosophy_Final_1.docx`
- AC Unified Architecture — `AC_Unified_Architecture.md`
- SRD v3 Combined — `1__SRD_v3_Combined.md`

**On Google Drive (fetched via Drive tools):**
- ÆC Operating System Compiled Alpha v1 (fileId: `1HRI0kxuJH5V5JNREWchtMzy82Rr3ql0p`) — READ IN FULL
- AC Errata Documents 1 and 2 (fileId: `1xpcCRWHOXrAnmfTE6M1pVhSlV_v-UaFJ`) — READ IN FULL
- AC Skill Effect Matrix (fileId: `1h4QN1eTgBtGwCFD6glFHQmACAsgPMN3s`) — READ IN FULL
- AEC_Alpha_Build_Order (fileId: `17csQb9-ES-4db83hLMiRH5knXImLnQkc`) — READ IN FULL
- AEC_Master_Catalog (fileId: `16IfsEDVpTGxHoHWRoiIv_bL2WuwQQ3nt`) — READ IN FULL
- AEC_Battle_Plan (fileId: `1pDmb6PhYGfSfcmpZmgbn1_RUGzxGm5kf`) — READ IN FULL
- AEC_Strategy_Sanity (fileId: `1bOBJqCxnMjlMA6GgC8Wx1tpPy2v05N66`) — READ IN FULL

### FINDINGS

**1. Single Source of Truth Established:**
- **Narrative Engine:** Compiled Alpha v1 (21 docs in one file: Doc 0 placeholder through 7B, R1, C1). This is the most complete single source for the Narrative Engine architecture. Note: its Doc 0 is self-labeled as placeholder; the project file `0__ÆC_Operating_Philosophy_Final_1.docx` appears to be the final version.
- **Game Mechanics:** SRD v3 Combined + AC Unified Architecture (both in project files). SRD v3 contains the current crafting system, amendments, isotope framework, spell sentence, item creation, mutation economy. AC UA contains talent trees (Docs 4a-4d), casting philosophies, combat styles, scope scale, the six-component engine.
- **Errata:** TRASHED. Its corrections were already embedded within the AC Unified Architecture project file. No unique content lost.

**2. Gaps Closed:**
- **Petal-to-skill crosswalk:** CLOSED. The Skill Effect Matrix (Drive) provides a full 16×24 compatibility grid mapping every skill against every canonical effect. Each cell indicates Tier 1-2 producibility. Outstanding work: ESL range, tempo commitment, and FP cost per cell need assignment.
- **Five-degree combat system:** CONFIRMED across Errata, AC UA, and SRD v3. Includes Success with Flaw for combat (mechanical cost still needs design work).
- **16-skill grid:** CONFIRMED clean across all Batch 1 sources. No 12-skill remnants found anywhere.
- **Crafting system canonical source:** CONFIRMED as SRD v3 Combined. V11.4 is deprecated.

**3. Conflicts Found and Resolved:**
- **Poise naming:** Errata said Social HP = "Reputation," Social track = "Poise." Build Order said Poise Pool was formally locked as Social HP. Alex confirmed: **Poise = Social HP pool.** Errata overridden.
- **Construction Pool formula:** BoS formula canonical per SRD v3 Amendment 8B. No contradicting source found.

**4. Conflicts Found and Still Open:**
- All five original open decisions remain unresolved — no Batch 1 document locked any of them.
- Three new open decisions added (FP unification, defense axis names, combat SWF mechanics).
- Essence vs Anima needs one verification check.

**5. AC Unified Architecture Needs Consolidation:**
The AC UA project file currently contains TWO contradictory defense systems:
- **Old (Part VII):** Base-10 formulas with pillar-specific names (Evasion/Guard/Toughness/Vigor, Willpower/Control/Conviction/Courage, Grace/Dignity/Composure/Discretion, Acuity/Integrity/Resilience/Essence)
- **Corrected (Document 3):** Composite Defense = Dodge + Deflection per pillar, no base 10, matching Player's Guide V4.1
Both versions live in the same file. The old system needs to be stripped during a consolidation pass. Which naming convention to keep (pillar-specific vs generic) is an open design decision.

**6. Document Triage:**

| Document | Status | Disposition |
|---|---|---|
| SRD v3 Combined (project) | Deployable as-is | KEEP — core mechanics spine |
| AC Unified Architecture (project) | Needs consolidation pass (contradictory defense systems) | KEEP — needs editing |
| ÆC Operating Philosophy (project) | Final version of Doc 0 | KEEP — supersedes Compiled Alpha's placeholder Doc 0 |
| Compiled Alpha v1 (Drive) | Contains full 21-doc Narrative Engine; some pre-correction terminology (Silas not Striven) | KEEP — primary Narrative Engine source |
| Skill Effect Matrix (Drive) | Complete, unique content | KEEP — not reproduced elsewhere |
| Alpha Build Order (Drive) | Stale completion statuses but useful chapter sequence and blocking decisions | KEEP for reference — update statuses |
| Errata (Drive) | Contents already in AC UA project file | TRASHED |
| Master Catalog (Drive) | Production/marketing document | KEEP — needs combining with Battle Plan and Strategy Sanity into one coherent production doc |
| Battle Plan (Drive) | Production/marketing document | KEEP — needs combining |
| Strategy Sanity (Drive) | Production/marketing document; contains unique tarot architecture and personality test design | KEEP — needs combining |

**7. Production Document Consolidation Needed:**
Master Catalog, Battle Plan, and Strategy Sanity are three overlapping marketing/production strategy documents that need combining into a single reference. Unique content per doc:
- **Master Catalog:** 10-line card product ecosystem, image anchor master list, accessibility standards, mobile toolstack, full distributable catalog
- **Battle Plan:** Dependency graph (Phase 0-8), USA manufacturer contacts, platform revenue/terms, operational pain points, backlog gates, release schedule
- **Strategy Sanity:** 9-college quick start party design, 78-card tarot architecture, personality test as product, parallel lore/mechanics distribution model, Zoetrope color theory, 10 marketing framework analyses
This consolidation is a separate work session outside the batch system.

---

## BATCH 2: NARRATIVE ENGINE

**Status:** NOT STARTED

**Purpose:** Verify all 21 docs of the Unified Engine spec for internal consistency. The set is confirmed complete (Doc 6B found in Untitled folder). The Compiled Alpha v1 contains all 21 docs — use it as primary source. Cross-reference the project file version of Doc 0 (Operating Philosophy) against the Compiled Alpha's placeholder version.

### Documents
All in Drive folder parentId: `1jEyTEvQZwG26k433FPgQadAz-nCTje_v`
- Docs 0, 1A, 1A Addendum, 1B, 2A, 2B, 3A, 3B, 3C, 4A, 4B, 4C, 5A, 5B, 5C, 6A, 7A, 7B, C1, R1
- Doc 6B in Untitled folder (fileId: `1m-4uRVAe3jKynH81pjGZ5cvlmzqHo8ax`)
- Also compare Psyche Schema v2 (project files) against v4 (in Compiled Alpha and on Drive, fileId: `1Hg9ekta8FX09CJ5HeceU5qwJZ-oQkr0_`)

### What Batch 1 Already Established About These Documents
- The Compiled Alpha contains all 21 docs in a single file. It was read in full during Batch 1.
- The Compiled Alpha's Doc 0 is a placeholder. The project file version is the final.
- The Compiled Alpha uses "Silas" for Moros Life aspect (should be "Striven").
- The Psyche Schema v4 within the Compiled Alpha is complete (three sections, 10-band overlay, FP generation, GM shortcut, Story Stack validation, 1A Addendum with five diagnostic resolutions).
- The Compiled Alpha appears to use "Instinct" correctly in the Schema section but this needs verification across all 21 docs.
- Regulatory systems count: Doc 0 project file lists 8 systems (adds Interaction Ritual). Compiled Alpha's Doc 0 lists 7. R1 lists 8. Verify which count is canonical.

### Specific Consistency Checks for Batch 2
1. Do all 21 docs use "Instinct" (not "Insight") for the Metaphysical skill?
2. Do all 21 docs use "Striven" (not "Silas") for Moros Life aspect?
3. Are the regulatory systems consistently counted as 7 or 8 across Doc 0, R1, and all cross-references?
4. Does the FP generation formula (outliers + splits + breaks) appear consistently across Docs 1A, 2A, 4B, and 1B?
5. Does the Distance model (0/1/2/3/∞ with costs 1/2/3/4/5 FP) appear consistently across Docs 4B, 6A, and all cross-references?
6. Does Doc 6B (Worked Examples) validate the architecture? Are there inconsistencies in its worked cycles?
7. Does the Psyche Schema v2 in project files contain anything NOT in v4? Or is v2 fully superseded?

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

**Purpose:** Confirm the SRD v3 crafting system is complete and internally consistent. V11.4 is DEPRECATED — do not reference it as canonical.

### Documents
**Drive:** Item Creation Rewrite v3 (fileId: `1cvT6yZGZ9HK5XvF3LzC7WtQUwKVN56V3`) — check if this is superseded by SRD v3 or contains unique content. Item Creation Reader Guide 16MB (fileId: `1zQ772tu0Dx1g1PZZdwxGG_NlZBJbfNYf`), Cross-Planar Forge library (13 numbered docs in Book folder), Planar Subtype Codex (fileId: `1jikQ6JO3vhkwchMwtjyuZ_PQnDLgGpe3VwkkdR5AGbI`)
**Project files:** SRD v3 (crafting system, value curve, Five Artifice Paths), AC Unified Architecture (Doc 4d crafting trees)

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
4. ~~Petal-to-skill crosswalk table~~ — **CLOSED by Skill Effect Matrix (Batch 1)**
5. Fey alpha-ready writeup (notes exist, not formatted)
6. Insight→Instinct propagation across all documents — identified, not yet executed
7. "Influence" terminology collision resolution
8. Silas→Striven propagation across all documents — identified, not yet executed
9. AC Unified Architecture consolidation pass — strip old Part VII defense system, resolve contradictory formulas within single file

## GAPS CLOSED BY DEEP DIVE

- Psyche Schema v4 — EXISTS on Drive and in Compiled Alpha
- Character creation procedure — EXISTS on Drive (early version)
- Guild system — EXISTS in Aetheric Pet System + Part 3 document
- Crafting system — EXISTS and resolved (SRD v3 Combined is canonical; V11.4 DEPRECATED)
- Five Ways alchemy framework — EXISTS on Drive
- Palimpsest-as-place description — EXISTS on Drive
- Geography/location reference — EXISTS on Drive
- Construction Pool formula — DECIDED (BoS canonical per Amendment 8B)
- Doc 6B Worked Examples — EXISTS in Untitled folder
- All 21 Narrative Engine docs — EXIST and COMPLETE on Drive (also in Compiled Alpha v1)
- Social combat notes — EXISTS on Drive
- Oracle Tables — EXISTS as Doc 5B
- Faction Turn Procedures — EXISTS as Doc 3C
- Petal-to-skill crosswalk — CLOSED (Skill Effect Matrix, Batch 1)
- Five-degree combat system — CONFIRMED canonical (Batch 1)
- 16-skill grid — CONFIRMED clean, no remnants (Batch 1)

## DOCUMENTS TRASHED
- AC Errata Documents 1 and 2 (Drive, fileId: `1xpcCRWHOXrAnmfTE6M1pVhSlV_v-UaFJ`) — contents already embedded in AC Unified Architecture project file. No unique content lost.

## PRODUCTION DOCUMENTS NEEDING CONSOLIDATION
The following three documents on Google Drive overlap heavily and need combining into a single coherent production reference in a separate work session:
- AEC_Master_Catalog (fileId: `16IfsEDVpTGxHoHWRoiIv_bL2WuwQQ3nt`)
- AEC_Battle_Plan (fileId: `1pDmb6PhYGfSfcmpZmgbn1_RUGzxGm5kf`)
- AEC_Strategy_Sanity (fileId: `1bOBJqCxnMjlMA6GgC8Wx1tpPy2v05N66`)
