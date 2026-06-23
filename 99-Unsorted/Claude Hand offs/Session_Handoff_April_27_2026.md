# ÆTHERIUM CODEX — SESSION HANDOFF
## April 27, 2026 — Batch 2 (Complete), Batch 3 (Partial), Document Triage, Dual Sources Extraction

---

## SESSION SUMMARY

This session covered:
1. Batch 2: Psyche Schema v2 vs v4 comparison (the 21 Unified Engine docs were skipped per Alex's instruction)
2. Batch 3: Partial magic system chain verification (cosmology → isotopes → Spell Sentence → Construction Pool → casting philosophies)
3. Document triage across Batches 2-3: deployable, unique-but-outdated, and disposal candidates
4. Deep dive and concept extraction from the Dual Sources of Magic conversational document

---

## BATCH 2 FINDINGS — COMPLETE

### Check #7: Psyche Schema v2 vs v4

**Verdict: v2 is NOT fully superseded.** Contains three unique deliverables v4 does not replicate.

**Unique content in v2 not in v4:**
1. Part I — Player Discovery Guide (natural-language questionnaire, 5 sections, ~20 questions for players who don't know the system)
2. Part II — Fillable Dossier Template (literal form with blank fields for all Schema dimensions)
3. Part III — GM Translation Guide (question-by-question scoring instructions mapping each player answer to Schema dimensions)

**Content in v4 not in v2:** The entire theoretical/mechanical framework (10-Band Overlay, Companion Elements, Active Properties, FP Generation, Composite Scores, Story Stack Validation, Expression Guidance, Known Limitations).

**Propagation errors in BOTH versions:**
- Silas → Striven (Moros Life aspect): Neither v2 nor v4 has been corrected. Both still use "Silas (The Struggle)" in Core Philosophy tables.
- Naming collision resolved by the rename: Heart's Compass "Silas (Friendship)" is a DIFFERENT entity from Moros "Silas (The Struggle)." The rename to "Striven" applies only to Moros. Once propagated, no collision.
- Essence vs Anima (Open Decision #9): v4 uses "Kanon / Anima" as the god PAIR — this is the deity name, not the attribute. The AC UA renames the ATTRIBUTE from Anima to Essence. These are separate uses. The open decision should be narrowed to the attribute only.

**Disposition:**
- Psyche Schema v4 → canonical system reference, needs Silas→Striven correction
- Psyche Schema v2 → companion implementation tool, needs same correction + header noting it's a companion to v4

**Add to Corrections Needing Propagation:** "Silas → Striven in Psyche Schema v4 Core Philosophy table" (both versions need the fix).

### Remaining Batch 2 Items (skipped, carry forward)
- 21 Unified Engine doc consistency checks (Items 1-6 from the handoff's Batch 2 checklist) were skipped per Alex's instruction. These remain NOT STARTED if needed later.

---

## BATCH 3 FINDINGS — PARTIAL

**Status:** Cosmology, Spell Sentence core, Construction Pool, ÆP, casting philosophies, isotope architecture, and boost system verified. Five Ways Framework, individual Way docs, and Social Combat PDF read but categorized under document triage rather than full consistency verification.

### Verified Consistent ✓

1. **Cosmology layer** — Primal/Structured Current consistent across all sources
2. **Construction Pool formula** — `(½ Effect Tier) + (½ Isotope Tier) + Overall Mastery + Integrity` — consistent between SRD v3, BoS v6, AC UA. Known discrepancy with character sheet (already flagged in SRD v3 gap #21; character sheet is OUTDATED)
3. **ÆP Pool formula** — `(Dominion + Tₘ) × Mastery` — consistent across SRD v3, BoS v6, AC UA
4. **Boost system** — Permanent +2/+3, Temporary +2/+3, Combined +4/+6 — consistent
5. **Geology-bleed resonance model** — consistent across AC UA, Turbulent/Laminar Flow, SRD v3
6. **Isotope architecture** — five planes, 16 isotopes per plane, phase wheel, Formation Stage — consistent
7. **Kanon/Anima god aspects** — Theoria/Praxis (Kanon) and Epiphanes/Pathos (Anima) confirmed in canonical god document. Psyche Schema's "Kanon (The Science) / Anima (The Art)" is intentional scale compression, not a conflict.

### Conflicts Found

| # | Conflict | Where | Canonical Answer | Needs Update |
|---|---|---|---|---|
| B3-1 | Effects list pre-consolidation (35+ vs 23+Variable) | BoS v6 | SRD v3 Amendments | BoS v6 |
| B3-2 | "Subtype" vs "Isotope" terminology | BoS v6 | SRD v3 ("Isotope") | BoS v6 |
| B3-3 | Improviser: flat Metamagic Affinity vs Anima-Based ÆP Reduction | AC UA Doc 4c | SRD v3 (Anima-Based) | AC UA Doc 4c |
| B3-4 | Architect bonus to wrong pool name ("Construction" vs "Complexity") | AC UA Doc 4c | SRD v3 / BoS v6 ("Complexity Pool") | AC UA Doc 4c |
| B3-5 | Mastery Capacity Pool defined only in BoS v6 | SRD v3 missing it | OPEN — is MCP canonical? Ask Alex | Depends on answer |

### Not Yet Verified (carry to next session)
- Five Ways Framework internal consistency against SRD v3 crafting system
- Social Combat PDF guild mechanics against AC UA references
- Individual Way 1-5 docs (not pulled)

---

## DOCUMENT TRIAGE — BATCHES 2-3

### Deployable As-Is

| Document | Location | Notes |
|---|---|---|
| SRD v3 Combined | Project file | Core mechanics spine. Current, carries all amendments. |
| ÆC Isotopes Combined | Project file | Complete isotope profiles. Consistent with SRD v3. |
| Psyche Schema v4 | Drive / Compiled Alpha Doc 1A | Canonical system reference. Needs Silas→Striven only. |
| Kanon & Anima, The Dual Gods of Magic | Project file | Complete, internally consistent. |

### Not Up To Date But Contains Unique Content

| Document | Location | Unique Content | Update Needed |
|---|---|---|---|
| Book of Shadows v6 | Drive (fileId: `1oNL57Eu5xvPmEqSGTAGYKbc7q8ElrHf3`) | Mastery Capacity Pool system (formula, Expanded Consciousness talent, XP costs). Most detailed Construction Menu tables. | Extract MCP into SRD v3. Effects list and "Subtype" terminology are deprecated. |
| AC Unified Architecture | Project file | Massive, essential. | Wrong pool name for Architect bonus, pre-Addendum Improviser benefit in Doc 4c, contradictory defense systems (old Part VII vs Document 3). Needs consolidation pass. |
| Psyche Schema v2 | Project file | Player questionnaire, fillable dossier template, GM translation guide. | Silas→Striven correction. Add header noting companion status to v4. |
| Social Combat PDF | Drive (fileId: `117A3GVs7Tr5TM_HLVOlrVYjNOKWNXpmg`) | Renown/Liability/Leverage guild standing (3-track). Gratis economy. Adventuring insurance. Chartered Company mechanics. Contract anatomy. Guildhall ecosystem. Background mechanical definitions (~129 occurrences). | Raw conversational format. AC UA references these systems by name at S4 but doesn't contain specifications. |
| Five Ways Framework | Drive (fileId: `1-JNMYbH0tkaR4aABo4EVFuj2u4n__GmqmNCSEditje0`) | Complete 5-plane alchemy system. Three language registers. Four-lane specs per plane. All 20 directional two-plane combinations. Forge internal 16-combination matrix. Four Forge-mediated emulsions with inverses. Item creation integration. | Unique and irreplaceable. Needs formatting cleanup. |
| Dual Sources of Magic | Drive (fileId: `1aVxbML0baf_6jXkPIuOG6FZ7hTzdrfoUlyWuuYnVuLo`) | See extraction below. 15 unique concept clusters identified and extracted. | Raw conversational. Archivable once extraction confirmed complete. |

### Deprecated (deprioritize)

| Document | Location | Notes |
|---|---|---|
| Turbulent/Laminar Flow PDF | Project file | "World Bible v2." Content fully captured in AC UA Parts I-III with greater precision. If project file slots needed, this is the one to remove. |

---

## DUAL SOURCES CONCEPT EXTRACTION — SUMMARY

Full extraction saved to: `/mnt/user-data/outputs/Dual_Sources_Concept_Extraction.md`

### What Was Extracted (Alex-approved)

- **1A — Aetheric Silt / Magical Decay Cycle:** Structured Current has a half-life, decays to silt, accumulates in geological sinks, ignites into Primal Loci. The Grand Orrery of Ætherna is its OWN PLANE (plane of raw destiny). The Structured Current blanketing the world is the EXHAUST of fate's engine, not the plane itself. Needs modification but provides mutation-mechanics flavor.
- **1C — Planar-specific materials:** Palimpsest Dust, Heartwood Seed, Athenaeum Salt, Generative Cores, Concordance Vellum (reassigned to Synod). All flagged as pre-Isotope-system designs.
- **1D — Animus Geodes:** Ioun stone analogue — symbiotic crystals that merge with the body. Pre-Isotope concept.
- **2C — Cognitive Dissonance triggers:** Full trigger list (3 cosmic + 6 mundane). Gnosis milestone table (Peripheral → Transcendent). Explicitly NOT established triggers flagged.
- **Group 3 — Cold War structure:** Three-Front Framework (Physical/Informational/Conceptual). Generalist College operational structure (Church of Aíon, college leverage matrix, Nexus Spire overlay). Five Operating Doctrines (Tapestry Imperative, Cost of Silence, Containment Imperative, Protocol of Veiled Contact, Unspoken Sanction).
- **Group 4 — College extremist factions:** Planar Cartel (Sovereign Exchange), Argent Coil (Chiaroscuro), Aegis of Purity/Restorationists (Stormpeak+broad), Keepers of Still Verse (Mortis Ævum), Three-Way Schism (Wildpath), Arbiters (Deepguard), Unifiers (Unity), Oracular Covenant (Chronosynclastic).
- **Group 5 — Fey, Daedalon, design philosophy:** Three Generations of Fey (Elder/Lost/Newborn; cryptids = modern fey). Daedalon's realm in the Palimpsest (two-tier: Artisan's Canton + hidden Artificer's Demiplane). Alex's design philosophy meta-notes (Eberron benchmark, mysteries over exposition, everyman perspective, cold war is perceptual).

### What Was Cut

- **1B — Primal Loci three-tier framework:** Superseded by 5-stage elevation map later in same conversation.
- **2A — Gods as sanitized Lacuna concepts:** Nice enrichment but not essential. Gods already systematically built.
- **2B — Entropics vs Architects:** Don't fit current architecture. Cut entirely.

### What Was NOT Extracted (unresolved markers only)

- Dragons (Lacunae-status, Dragonlance merge not designed)
- Far East snake-like people (Lacunae-status)
- Vecna analogue (no design exists)
- Sōmaturgy and Ætherforged Precepts (confirmed already integrated, need polish)

---

## UPDATED OPEN DECISIONS

All original open decisions from Batch 1 remain. No new ones were resolved this session. One clarification added:

**Open Decision #9 (Essence vs Anima) — NARROWED:** The question is specifically whether the ATTRIBUTE was renamed from Anima to Essence. The GOD pair name "Kanon / Anima" is unaffected regardless.

**New confirmed fact:** The Grand Orrery of Ætherna is its own plane — the plane of raw destiny, Kanon's direct expression. The Structured Current is the exhaust/byproduct of this plane's primary function of producing Fate.

---

## CORRECTIONS NEEDING PROPAGATION (updated)

All previous corrections carry forward. Add:
1. **Silas → Striven in Psyche Schema v4** Core Philosophy table (both v2 and v4 need the fix — this was only listed for v2 previously)
2. **AC UA Doc 4c Architect bonus pool name:** "Construction Pool" → "Complexity Pool"
3. **AC UA Doc 4c Improviser benefit:** Replace flat Metamagic Affinity (-2) with Anima-Based ÆP Reduction per SRD v3

---

## NEXT SESSION PRIORITIES

1. **Finish Batch 3:** Pull and verify Five Ways Framework against SRD v3 crafting system. Verify Social Combat guild mechanics against AC UA S4 references.
2. **Batch 4 (Item Creation):** Ready to start once Batch 3 is closed.
3. **Dual Sources extraction review:** Alex should review the full extraction file and confirm completeness before archiving the raw doc.
4. **Mastery Capacity Pool decision:** Is the MCP system from BoS v6 canonical? If yes, it needs to be added to SRD v3. If deprecated, the Tethered additive reference needs updating.

---

*End of handoff. The Dual Sources Concept Extraction is a separate file in the same outputs directory.*
