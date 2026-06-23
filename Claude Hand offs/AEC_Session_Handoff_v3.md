# ÆTHERIUM CODEX — SESSION HANDOFF DOCUMENT v3
## Batch Processing Guide for Alpha Assembly
## Updated: April 27, 2026 — Batch 3 Complete, Batch 4 Ready

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
9. Essence vs Anima — verify whether Document 1 renamed Anima to Essence. If the rename was NOT locked, revert to Anima. **NARROWED (Batch 2):** The question is specifically about the ATTRIBUTE name. The GOD pair name "Kanon / Anima" is unaffected regardless.
10. **Mastery Capacity Pool (B3-5):** Is the MCP system from BoS v6 canonical? If yes, it needs to be added to SRD v3. If deprecated, the Tethered additive reference needs updating. **AWAITING ALEX DECISION.**
11. **Guild interface track count (B3-8):** AC UA references a three-track system (Renown/Liability/Leverage). Social Combat PDF develops a four-track system adding Gratis as a passive disposition threshold. Is the four-track system canonical? **AWAITING ALEX DECISION.**

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
- Grand Orrery of Ætherna is its own plane — the plane of raw destiny, Kanon's direct expression. The Structured Current is the exhaust/byproduct of this plane's primary function of producing Fate.

### Corrections Needing Propagation
These are confirmed canonical answers that have not yet been applied across all documents:
1. **Insight → Instinct:** The fourth Metaphysical skill. Affects Iconic Talents doc (Unity, Chronosynclastic, Generalist sections), the Errata's skill table, and any other document referencing Metaphysical skills.
2. **Silas → Striven:** Moros Life aspect. Psyche Schema v4 AND v2 both still show "Silas (The Struggle)." Gods Section document is correct.
3. **Poise Pool standardization:** Social HP pool = Poise. Any document using "Reputation Pool" for Social HP needs correction.
4. **HP formula in Character Creation v3.0:** That document has the wrong formula. Canonical is (Vigor×3 + Might×3 + Mastery×5).
5. **AC UA Doc 4c Architect bonus pool name:** "Construction Pool" → "Complexity Pool"
6. **AC UA Doc 4c Improviser benefit:** Replace flat Metamagic Affinity (-2) with Anima-Based ÆP Reduction per SRD v3
7. **Five Ways Framework Section VI:** Update five-item reading (base compounds, mutations, attachments, enchantments, insets) to match SRD v3's four-layer model (Expressions consolidates mutations+enchantments)
8. **Five Ways Framework cross-reference box:** Update reference from "ÆC_Stoichiometry_Thermal_Register.docx" to "ÆC_Way1_Borderlands_Revised.docx" — the thermal register was incorporated into Way 1, the standalone file was never created.

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

### FINDINGS

1. **Single Source of Truth Established:** Narrative Engine = Compiled Alpha v1 (21 docs). Game Mechanics = SRD v3 Combined + AC Unified Architecture (project files). Errata = TRASHED (contents already in AC UA).
2. **Gaps Closed:** Petal-to-skill crosswalk (Skill Effect Matrix), five-degree combat system confirmed, 16-skill grid confirmed clean, crafting canonical source confirmed (SRD v3).
3. **Conflicts Resolved:** Poise = Social HP pool (Errata overridden). Construction Pool formula = BoS canonical per Amendment 8B.
4. **AC UA Needs Consolidation:** Two contradictory defense systems (old Part VII vs Document 3). Old system needs stripping.
5. **Document Triage:** SRD v3 (deployable), AC UA (needs consolidation pass), Operating Philosophy (final Doc 0), Compiled Alpha (keep, primary Narrative Engine source), Skill Effect Matrix (keep, unique), Alpha Build Order (keep for reference), Errata (TRASHED), Master Catalog/Battle Plan/Strategy Sanity (need combining into single production doc).

---

## BATCH 2: NARRATIVE ENGINE

**Status:** COMPLETE (21 Unified Engine doc checks skipped per Alex's instruction; Psyche Schema v2 vs v4 comparison done)

### FINDINGS

1. **Psyche Schema v2 NOT fully superseded by v4.** v2 contains three unique deliverables: Player Discovery Guide, Fillable Dossier Template, GM Translation Guide. v4 is the canonical system reference.
2. **Silas → Striven:** Both v2 and v4 need the correction.
3. **Essence vs Anima (Open Decision #9) narrowed:** The question applies only to the ATTRIBUTE name, not the god pair.
4. **Disposition:** v4 = canonical system reference (needs Silas→Striven). v2 = companion implementation tool (needs same correction + companion header).
5. **21 Unified Engine doc consistency checks** were skipped. Carry forward if needed later.

---

## BATCH 3: MAGIC SYSTEM

**Status:** COMPLETE

**Purpose:** Confirm full magic chain from cosmology → isotopes → Spell Sentence → Construction Pool → casting philosophies → alchemy.

### Documents Reviewed
**Project files:** SRD v3 Combined, AC Unified Architecture, ÆC Isotopes Combined
**Drive:** Book of Shadows v6, Five Ways Framework, Social Combat PDF, Dual Sources of Magic, ÆC_Way1_Borderlands_Revised.docx
**Uploads:** ÆC_Magical_Stoichiometry.docx, Magical_Stoichiometry_System_v1.pdf

### FINDINGS

**Verified Consistent ✓**
1. Cosmology layer — Primal/Structured Current consistent across all sources
2. Construction Pool formula — consistent between SRD v3, BoS v6, AC UA (character sheet OUTDATED)
3. ÆP Pool formula — consistent across SRD v3, BoS v6, AC UA
4. Boost system — Permanent +2/+3, Temporary +2/+3, Combined +4/+6 — consistent
5. Geology-bleed resonance model — consistent across AC UA, Turbulent/Laminar Flow, SRD v3
6. Isotope architecture — five planes, 16 isotopes per plane, phase wheel, Formation Stage — consistent
7. Kanon/Anima god aspects — Theoria/Praxis (Kanon) and Epiphanes/Pathos (Anima) confirmed canonical
8. Five Ways Framework vs SRD v3 crafting — consistent at every structural joint (Formation Stage scale, Heritage State, antithetical pairs, Forge as universal catalyst, four behavioral outcomes, four Forge catalyst types)
9. Social Combat PDF guild mechanics vs AC UA S4 — consistent at structural level (S4 IS the guild layer, contract components match)
10. ÆC_Magical_Stoichiometry.docx — uses canonical terminology (C/K/V/I lanes, Aetheric Profiles), consistent with Five Ways and SRD v3
11. Five Way individual docs (Way 1-5) — all five located on Drive, all labeled "Companion to ÆC_Five_Ways_Framework.docx," all contain unique molecular/compound tables not in the Framework

**Conflicts Found**

| # | Conflict | Where | Canonical Answer | Needs Update |
|---|---|---|---|---|
| B3-1 | Effects list pre-consolidation (35+ vs 23+Variable) | BoS v6 | SRD v3 Amendments | BoS v6 |
| B3-2 | "Subtype" vs "Isotope" terminology | BoS v6 | SRD v3 ("Isotope") | BoS v6 |
| B3-3 | Improviser: flat Metamagic Affinity vs Anima-Based ÆP Reduction | AC UA Doc 4c | SRD v3 (Anima-Based) | AC UA Doc 4c |
| B3-4 | Architect bonus to wrong pool name ("Construction" vs "Complexity") | AC UA Doc 4c | SRD v3 / BoS v6 ("Complexity Pool") | AC UA Doc 4c |
| B3-5 | Mastery Capacity Pool defined only in BoS v6 | SRD v3 missing it | **OPEN — ask Alex** | Depends on answer |
| B3-6 | Five Ways §VI lists 5 item layers; SRD v3 consolidates to 4 (Expressions = mutations+enchantments) | Five Ways §VI vs SRD v3 | SRD v3 (consolidation is explicit) | Five Ways §VI |
| B3-7 | Five Ways cross-references "ÆC_Stoichiometry_Thermal_Register.docx" | Five Ways §II | File never created; content in ÆC_Way1_Borderlands_Revised.docx | Five Ways cross-ref box |
| B3-8 | AC UA names 3-track guild system; Social Combat PDF develops 4-track (adds Gratis) | AC UA vs Social Combat PDF | **OPEN — ask Alex** | Depends on answer |

**Dual Sources of Magic — Concept Extraction Complete**
Full extraction saved separately (Dual_Sources_Concept_Extraction.md). 15 unique concept clusters extracted and Alex-approved. Raw conversational doc archivable once Alex confirms extraction completeness.

---

## BATCH 4: ITEM CREATION

**Status:** READY TO START

**Purpose:** Confirm the SRD v3 crafting system is complete and internally consistent. Verify the Five Ways alchemy chain feeds correctly into item creation. V11.4 is DEPRECATED — do not reference it as canonical.

### Documents

**Project files:**
- SRD v3 Combined (crafting system, value curve, Five Artifice Paths, material quality table, four-layer item model, Legacy & Ascension)
- AC Unified Architecture (Doc 4d crafting & companion trees)

**Drive — Core item creation:**
- ÆC_Item_Creation_Rewrite v3 (fileId: `1cvT6yZGZ9HK5XvF3LzC7WtQUwKVN56V3`, 230KB) — **KEY DOCUMENT.** Self-described as "Complete Rewrite — Five Ways Integrated Edition — Supersedes all prior Item Creation documents." Uses the same four-step architecture (Material Identification → Processing → Slot Architecture → Legacy) as Five Ways §VI. Must be compared against SRD v3 to determine which is more current and where unique content lives.
- Item Creation Reader Guide 16MB (fileId: `1zQ772tu0Dx1g1PZZdwxGG_NlZBJbfNYf`)
- Planar Subtype Codex (fileId: `1jikQ6JO3vhkwchMwtjyuZ_PQnDLgGpe3VwkkdR5AGbI`)
- Cross-Planar Forge library (13 numbered docs in Book folder) — may overlap with Elemental Cards project file

**Drive — Five Ways alchemy chain (verified Batch 3, implementation detail here):**
- ÆC_Five_Ways_Framework (fileId: `1-JNMYbH0tkaR4aABo4EVFuj2u4n__GmqmNCSEditje0`) — architectural overview
- ÆC_Way1_Borderlands_Revised.docx (fileId: `1ldtp8NJYbzWxbsGlZSVQ1XUuP8DZntEL`) — molecular expression tables, thermal register, C/K/V/I matrices, precipitate forms
- ÆC_Way2_Verdant_Font (fileId: `1XYEnbQqe7T60yKUAm6IauGBhpIoRW4cjgNIDnL6eK0g`) — organic molecules, mutation chemistry, pharmacological lanes
- ÆC_Way3_Synod (fileId: `1lzgg6yZ6KA2QDf7z4oyOpbzDKX4qV1zQmrYQLcIC9j0`) — Synod compounds, radioactive decay, soul stone chemistry
- ÆC_Way4_Hidden_Forge.docx (fileId: `19ARLbEMU6A3zLzIxCKY5os80C_D_Mu45`) — 16-isotope Forge lane mapping, emulsion mediator mechanics
- ÆC_Way5_Palimpsest.docx (fileId: `1sHjQ0NleFz5Dr8vY3FV5SU2MeAPWwB5_`) — equilibrium/probability lanes, chirality, narrative logic as thermodynamic variable

**Uploaded (verified Batch 3):**
- ÆC_Magical_Stoichiometry.docx — Lane Reaction Matrix, Profile Interaction Matrix, precipitate forms, toxicity, refinement, item creation integration

### What Batch 3 Already Established About These Documents
- Five Ways Framework is architecturally consistent with SRD v3 at every joint
- The Five Ways four-step item creation model maps to SRD v3's crafting system
- SRD v3's four-layer item model (Base Material / Expressions / Attachments / Insets) is the current consolidation — Five Ways §VI uses older five-item reading
- All five individual Way docs contain unique molecular/compound tables not reproduced elsewhere
- The ÆC_Magical_Stoichiometry.docx is current (canonical terminology); the v1 PDF is DEPRECATED
- ÆC_Item_Creation_Rewrite v3 explicitly integrates the Five Ways and claims to supersede all prior item creation docs — this is the primary document to compare against SRD v3

### Specific Consistency Checks for Batch 4
1. Does ÆC_Item_Creation_Rewrite v3 supersede SRD v3's crafting sections, or does SRD v3 contain amendments/corrections not in the Rewrite?
2. Are the Five Artifice Path talent trees in SRD v3 consistent with AC UA Doc 4d's versions?
3. Does the Rewrite's four-step model use the same formulas (Artifice Check, PV, crafting TN) as SRD v3?
4. Is the Item Creation Reader Guide (16MB) a formatted version of existing content or does it contain unique material?
5. Does the Planar Subtype Codex contain content not already in ÆC Isotopes Combined or the Elemental Cards?
6. Do any of the five Way docs contain item creation integration content that contradicts or extends the Framework's §VI?
7. Are the Cross-Planar Forge library docs (13) redundant with the Elemental Cards Alpha project file?
8. What is the relationship between the Rewrite's Affinity Alignment Rule and SRD v3's innate/powered determination?

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
- Guild system — EXISTS in Aetheric Pet System + Part 3 document + Social Combat PDF (most detailed)
- Crafting system — EXISTS and resolved (SRD v3 Combined is canonical; V11.4 DEPRECATED)
- Five Ways alchemy framework — EXISTS on Drive (Framework + 5 individual Way docs + Stoichiometry doc)
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
- Thermal register — CLOSED (incorporated into ÆC_Way1_Borderlands_Revised.docx, Batch 3)
- Stoichiometry reference — CLOSED (ÆC_Magical_Stoichiometry.docx confirmed current, Batch 3)

## DOCUMENTS TRASHED
- AC Errata Documents 1 and 2 (Drive, fileId: `1xpcCRWHOXrAnmfTE6M1pVhSlV_v-UaFJ`) — contents already embedded in AC Unified Architecture project file. No unique content lost.
- Magical Stoichiometry System v1 (PDF + Drive Google Doc fileId: `1O0B2sXavPKUOHcRQcuDG591cLAjTwjvb6wc1UD3i71A`) — fully deprecated. Pre-current terminology ("Silent Athenaeum," "Concordance," "Crucible/Deception"). All content better expressed in ÆC_Magical_Stoichiometry.docx and Five Ways Framework.
- Turbulent/Laminar Flow PDF (project file) — "World Bible v2." Content fully captured in AC UA Parts I-III with greater precision. Deprioritized; first candidate for removal if project file slots needed.

## DOCUMENT TRIAGE — COMPLETE THROUGH BATCH 3

### Deployable As-Is

| Document | Location | Notes |
|---|---|---|
| SRD v3 Combined | Project file | Core mechanics spine. Current, carries all amendments. |
| ÆC Isotopes Combined | Project file | Complete isotope profiles. Consistent with SRD v3. |
| Psyche Schema v4 | Drive / Compiled Alpha Doc 1A | Canonical system reference. Needs Silas→Striven only. |
| Kanon & Anima, The Dual Gods of Magic | Project file | Complete, internally consistent. |
| ÆC_Magical_Stoichiometry.docx | Uploaded / to be filed on Drive | Current stoichiometry reference. Canonical terminology. |
| ÆC_Five_Ways_Framework | Drive | Architectural alchemy overview. Consistent with SRD v3. Needs two minor corrections (§VI layer count, cross-ref box). |

### Contains Unique Content — Not Yet Fully Verified

| Document | Location | Unique Content | Status |
|---|---|---|---|
| ÆC_Item_Creation_Rewrite v3 | Drive (fileId: `1cvT6yZGZ9HK5XvF3LzC7WtQUwKVN56V3`) | 230KB Five Ways-integrated item creation. Claims to supersede all prior item creation docs. | **BATCH 4 PRIMARY TARGET** |
| ÆC_Way1_Borderlands_Revised.docx | Drive (fileId: `1ldtp8NJYbzWxbsGlZSVQ1XUuP8DZntEL`) | Molecular expression tables, thermal register, C/K/V/I precipitate matrices | Verified consistent Batch 3 |
| ÆC_Way2_Verdant_Font | Drive (fileId: `1XYEnbQqe7T60yKUAm6IauGBhpIoRW4cjgNIDnL6eK0g`) | Organic molecules, mutation chemistry, pharmacological lanes | Located Batch 3, not yet verified |
| ÆC_Way3_Synod | Drive (fileId: `1lzgg6yZ6KA2QDf7z4oyOpbzDKX4qV1zQmrYQLcIC9j0`) | Synod compounds, radioactive decay, soul stone chemistry | Located Batch 3, not yet verified |
| ÆC_Way4_Hidden_Forge.docx | Drive (fileId: `19ARLbEMU6A3zLzIxCKY5os80C_D_Mu45`) | 16-isotope Forge lane mapping, emulsion mediator mechanics | Located Batch 3, not yet verified |
| ÆC_Way5_Palimpsest.docx | Drive (fileId: `1sHjQ0NleFz5Dr8vY3FV5SU2MeAPWwB5_`) | Equilibrium/probability lanes, chirality, narrative logic formulation | Located Batch 3, not yet verified |
| Book of Shadows v6 | Drive (fileId: `1oNL57Eu5xvPmEqSGTAGYKbc7q8ElrHf3`) | Mastery Capacity Pool system, most detailed Construction Menu tables | Effects list and "Subtype" terminology deprecated. MCP status OPEN. |
| AC Unified Architecture | Project file | Massive, essential. | Needs consolidation pass (contradictory defense systems, Doc 4c errors). |
| Psyche Schema v2 | Project file | Player questionnaire, fillable dossier, GM translation guide | Companion to v4. Needs Silas→Striven + companion header. |
| Social Combat PDF | Drive (fileId: `117A3GVs7Tr5TM_HLVOlrVYjNOKWNXpmg`) | Four-track guild interface (Renown/Liability/Gratis/Leverage), Chartered Company mechanics, Adventuring Insurance, Contract Generator Engine, three-tier guild hierarchy | Raw conversational format. Gratis track status OPEN. |
| Five Ways Framework | Drive (fileId: `1-JNMYbH0tkaR4aABo4EVFuj2u4n__GmqmNCSEditje0`) | Complete 5-plane alchemy architecture, 20 directional combinations, Forge internal matrix, four emulsions | Needs two minor corrections (§VI, cross-ref). |
| Dual Sources of Magic | Drive (fileId: `1aVxbML0baf_6jXkPIuOG6FZ7hTzdrfoUlyWuuYnVuLo`) | See Dual Sources Concept Extraction | Archivable once Alex confirms extraction complete. |

## PRODUCTION DOCUMENTS NEEDING CONSOLIDATION
The following three documents on Google Drive overlap heavily and need combining into a single coherent production reference in a separate work session:
- AEC_Master_Catalog (fileId: `16IfsEDVpTGxHoHWRoiIv_bL2WuwQQ3nt`)
- AEC_Battle_Plan (fileId: `1pDmb6PhYGfSfcmpZmgbn1_RUGzxGm5kf`)
- AEC_Strategy_Sanity (fileId: `1bOBJqCxnMjlMA6GgC8Wx1tpPy2v05N66`)

---

*End of handoff v3. Batch 4 (Item Creation) is the next session's primary target. The ÆC_Item_Creation_Rewrite v3 is the key document to pull and compare against SRD v3.*
