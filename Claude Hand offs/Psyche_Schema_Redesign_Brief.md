# PSYCHE SCHEMA REDESIGN BRIEF
## Ætherium Codex — Vertebra 1 Ground-Up Rebuild
### Prepared: April 28, 2026 — For dedicated future session

---

## MANDATE

The Psyche Schema requires a ground-up redesign. Not a patch. Not an expanded questionnaire bolted onto the existing framework. A complete rebuild of the instrument that serves as Vertebra 1 of the Narrative Engine, the entry point of the character creation procedure, and a standalone marketable product.

**This work is blocked on Batch 11 (Talents).** Talent architecture may also be reworked, and the Schema and talent systems are deeply interdependent — the Schema profiles *who you are*, talents define *what you can do*, and the two must interlock. Both should be redesigned with awareness of the other.

---

## WHY THE REDESIGN IS NEEDED

The current Schema (v2 guide / Doc 1A v4 spec) works as a GM tool. When you already know a character's personality — from history, design intent, or accumulated play — the dimensional framework maps it cleanly. This has been demonstrated repeatedly through profiling of historical figures (FDR), designed NPCs, and institutional entities.

It does NOT work as a cold-administration instrument for character creation. Three specific failures:

1. **Coverage gaps.** The 24-question Part I questionnaire leaves entire god dimensions unassessed (Aurelion, Moros, Thalassus have no dedicated questions). 8 of 9 Heart's Compass dimensions are inferred from 2 relationship questions. The GM fills the gaps through inference — a new player can't.

2. **No mechanical character output.** The Schema profiles personality. It doesn't produce a playable character. Attributes, skills, talents, heritage, equipment — none of these emerge from the current instrument. Character creation is a separate, unwritten procedure that happens *after* the Schema. The redesigned Schema should BE the character creation procedure, or at minimum, the first integrated phase of it.

3. **The standalone product must work without a GM.** The Psyche Schema as a marketable personality test needs to be self-administered, self-scored, and self-interpreting. The current system requires a trained operator (the GM) to translate player responses into scored dimensions using the Part III Translation Guide. That translation step needs to be either eliminated or made transparent enough for self-service.

---

## WHAT THE REDESIGNED SCHEMA MUST ACCOMPLISH

### As Vertebra 1 of the Narrative Engine:
- Profile any entity (PC, NPC, institution, territory, god) with enough resolution to generate Fulcrum Points from internal contradictions
- Produce the diagnostic outputs downstream vertebrae read: outlier scores, asymmetric splits, pattern breaks
- Map to the 10-band overlay (d4 through d12) for mechanical resolution
- Support the band-assignment shortcut for GM-generated entities

### As the character creation instrument:
- Take a player from zero to a playable character in one guided procedure
- Produce mechanical outputs: attribute scores, skill ranks, talent prerequisites, college affiliation, heritage traits, starting equipment profile
- Integrate with the 120 XP starting pool and the (still-unresolved) talent costing system
- Respect the unified grammar: Magic = Talents = Items = Heritage = Mutations

### As a standalone marketable product:
- Administrable cold without GM mediation
- Self-scoring or transparently scored
- Engaging enough to complete (target: 45-50 questions, comparable to established personality instruments)
- Produces a result the taker finds meaningful independent of the game (the personality profile has standalone value)
- Serves as a lead magnet / entry point to the broader Tessera IP

---

## CURRENT STATE OF THE SCHEMA

### Dimensional Structure (Doc 1A v4 / v2 Guide)

**Section I — Core Philosophy:** 11 paired dimensions, each anchored to a god's dual-aspect portfolio. 22 scored aspects.

| God | Aspect A | Aspect B |
|---|---|---|
| Aurelion | Luxos (The Ideal) | Ignislor (The Real) |
| Moros | Silas/Striven (The Struggle) | Dolor (The Stasis) |
| Daedalon | The Artificer (Process) | The Crucible (Result) |
| Nomos | Themis (Spirit of Law) | Lex (Letter of Law) |
| Bellum Hegemon | Kaelen (Productive Conflict) | Bellax (Suffering) |
| Valorin | Mercatus (Fair Trade) | Credo (Predatory) |
| Agora | The Architect (Collective) | The Tyranny (System) |
| Verdena | Fiora (The Garden) | Gorn (The Wild) |
| Rhapsodia | Jocan (Skillful Expression) | Malix (Unrestrained Will) |
| Vestus | Veritas (Lore/Context) | Gnosis (Raw Data) |
| Kanon/Anima | Kanon (The Science) | Anima (The Art) |

**Section II — The Selûnæ:** 3 paired dimensions. 6 scored aspects.

| Pair | Aspect A | Aspect B |
|---|---|---|
| Potential | Maiden (Inevitable) | Wench (Chosen Conquest) |
| Connection | Mother (Enduring) | Strumpet (Shifting) |
| Consequence | Crone (Understood) | Hag (Unending) |

**Section III — Heart's Compass:** 9 dimensions, each with 3 faces (Balanced/Unrestrained/Trauma). 9 scored dimensions + face state.

| Dimension | Chorus God |
|---|---|
| Isolde | Passion |
| Silas | Friendship |
| Aethel | Family |
| Eselle | Selflessness |
| Corin | Playfulness |
| Constantine | Duty |
| Kenna | Self-Love |
| Zeniel | Hospitality |
| Veyra | Unrequited Love |

**Additional assessed fields from v2 guide:**
- 6 archetype labels: Motivation, Mental Fortitude, Social Operation, Historicity, Self-Perception, Cognition
- 2 composite scores: Aíon (Cosmic Stability), Lacuna (Cosmic Instability)

**Total system footprint:** 24 questions + 45 data points = 69 touchpoints.

### Current Question-to-Dimension Mapping

The v2 guide's Part III Translation Guide maps specific questions to dimensions:

| Question | Dimension | Coverage Quality |
|---|---|---|
| Q9 (Justice & Law) | Nomos: Themis/Lex | Direct — clean |
| Q10 (Conflict & Growth) | Bellum: Kaelen/Bellax | Direct — clean |
| Q11 (Order & Chaos) | Rhapsodia: Jocan/Malix | Direct — clean |
| Q12 (Nature & Civilization) | Agora + Verdena | Direct — but conflates two gods |
| Q13 (Magic & Unknown) | Kanon/Anima | Direct — clean |
| Q14 (Knowledge & Truth) | Vestus: Veritas/Gnosis | Direct — clean |
| Q15 (Fate & Destiny) | Selûnæ (4 of 6 aspects) | Partial — Mother/Strumpet inferred |
| Q16 (Cornerstone of Connection) | Heart's Compass primary | 1 of 9 directly identified |
| Q17 (Defining Bond) | Heart's Compass + Mother/Strumpet | Heavy inference load |
| Q18 (The Ghost) | Heart's Compass + Mother/Strumpet | Heavy inference load |
| Q4 + Q21 (Driving Force + Skill) | Daedalon: Artificer/Crucible | Inferred from two unrelated questions |
| Q6 + morality (Social Strategy) | Valorin: Mercatus/Credo | Inferred loosely |

**Unassessed dimensions (no dedicated question):**
- Aurelion (Luxos/Ignislor) — idealism vs pragmatism in leadership
- Moros (Striven/Dolor) — generative struggle vs entropic weight
- Thalassus — dangerous labor, peril, sacrifice (not in v2 guide AT ALL)
- Heart's Compass dimensions 2-9 (only primary identified by Q16)
- Heart's Compass face states (no detection mechanism)
- Archetype labels (derivation procedure unspecified)
- Aíon/Lacuna composites (derivation procedure unspecified)

---

## ARCHITECTURAL CONSTRAINTS

The redesigned Schema must respect these locked decisions:

- The same unified grammar operates at every scale with no special cases
- Condition Tracks ARE clocks (identity statement)
- The Spell Sentence IS the symptom vocabulary at every scale
- The Legacy system reads accumulated choices backward (Palimpsest logic)
- The seven-vertebra spine is a cycle, not a line
- Narrative-first, not player-forward
- Starting XP pool: 120 XP
- Resolution system: d20
- HP formula: Vigor×3 + Might×3 + Mastery×5
- 23+Variable canonical effects list
- Five-degree critical system
- 16-skill 4-pillar grid
- 12 attributes across 4 pillars (3 per pillar)
- Heritage attributes as separate track, capped at +2
- Fulcrum Points generated from Schema contradictions (outliers, splits, breaks)
- The 10-band overlay (scores → die types) is the bridge between narrative and mechanical identity
- Schema co-completion: optimal specification leaves room for participant contribution

---

## SOURCE DOCUMENTS TO LOAD FOR THE REDESIGN SESSION

### Required:
1. **Psyche Schema v2 Guide** (project file) — the current instrument
2. **Operating Philosophy Doc 1A** (project knowledge, searchable) — the v4 spec
3. **Character Profile output file** (project file) — the mechanical character sheet
4. **SRD v3 Combined** (project file) — attribute/skill/talent structure, Spell Sentence, crafting
5. **AC Unified Architecture** (project file) — the master architecture document

### Highly Recommended:
6. **All god documents** (project files) — the 11 Core Philosophy dimensions are anchored to these gods. The redesign must assess each god's portfolio and ensure the questionnaire properly surfaces the philosophical tensions each god represents.
7. **Merged Colleges v1** (project file) — college affiliation is a companion element that shapes how the Schema expresses. The questionnaire may need to surface college alignment as part of character creation.
8. **Political Zoetrope v2** (project file) — the Zoetrope positions map to institutional methodologies. If the Schema is producing playable characters, their institutional context matters.

### Load After Batch 11:
9. **Whatever talent architecture emerges from Batch 11** — talents and the Schema must interlock. The Schema should either lead into talent selection or generate talent prerequisites as an output.

---

## DEPENDENCIES

| Dependency | Why | Status |
|---|---|---|
| **Batch 11 (Talents)** | Talent architecture may be reworked. Schema and talents are interdependent — can't finalize one without the other. | NOT STARTED |
| **XP cost formula (OD-1)** | If the Schema produces a character with 120 XP to spend, the talent pricing must be locked. | OPEN |
| **Heritage system** | Heritage attributes are a separate track. If heritage selection is part of character creation, the Schema needs to account for it or explicitly hand off to a heritage selection phase. | PARTIALLY DEVELOPED |
| **Daredevil Engine decision (OD-4)** | Whether Daredevil is a 9th Foundational Style affects the talent landscape the Schema must connect to. | OPEN |

---

## DESIGN QUESTIONS FOR THE REDESIGN SESSION

These are not pre-answered. They're the questions the dedicated session needs to resolve.

1. **Should the Schema produce mechanical outputs directly, or produce a profile that feeds a separate mechanical generation step?** (One integrated procedure vs. two-phase: profile then build.)

2. **How does college affiliation interact with the questionnaire?** Does the player choose a college, or does the Schema assign one based on responses? Or is it a recommendation the player can override?

3. **Should the standalone product version and the TTRPG character creation version be the same instrument, or two versions of the same instrument?** (The standalone product doesn't need to produce attributes and skills. The TTRPG version does.)

4. **How do the 9 Heart's Compass dimensions get properly assessed in a cold-administration instrument?** The current 2-question inference approach is insufficient. Forced ranking? Scenario-based? Direct self-assessment?

5. **What happens to the archetype labels (Motivation, Mental Fortitude, Social Operation, Historicity, Self-Perception, Cognition)?** Are they promoted to first-class scored dimensions, kept as qualitative labels, or eliminated?

6. **How do face states (Balanced/Unrestrained/Trauma) get detected?** The current instrument has no mechanism for this. Does each Heart's Compass dimension need a follow-up question, or is face state determined by the score itself (e.g., extreme scores = Unrestrained, moderate = Balanced)?

7. **Should contradiction detection be built into the questionnaire (dedicated cross-dimensional questions) or left as a diagnostic step the GM performs on the completed profile?** Building it in makes the standalone product more powerful. Leaving it out preserves the GM's creative territory.

8. **How does Thalassus get integrated?** It's the only major god with zero presence in the current v2 guide. Its portfolio (dangerous labor, peril, the value of sacrifice) is mechanically significant — it maps to the risk/reward economy that drives adventuring itself.

9. **What is the target question count?** 24 is insufficient. 90+ is too long. The sweet spot for engagement is probably 40-55. Each question must earn its place by either directly assessing a dimension, detecting a contradiction, or producing a mechanical output.

---

## WHAT SUCCESS LOOKS LIKE

A player sits down with no character concept. They take the redesigned Psyche Schema. When they finish:

- They have a personality profile mapped onto the god-anchored dimensional framework
- They have mechanical character outputs (attributes, skills, at minimum college affiliation and heritage direction)
- They have pre-identified contradiction points that will generate Fulcrum Points
- They have enough information to select talents and equipment with informed intent
- They feel like they *discovered* their character rather than *assembled* one
- The profile has standalone value as a personality assessment even if they never play the game

A GM sits down needing an NPC. They use the band-assignment shortcut. In 5 minutes they have a Schema profile that feeds the Ten Questions, produces pressure points, and drives front generation. The shortcut and the full instrument produce interchangeable outputs.

An institution, territory, or god is profiled using the Doc 1B companion guide. The same dimensional framework applies at every scale. The redesigned Schema doesn't break scale independence.

---

*End of brief. This document is the scope definition for a dedicated future session. The session should not begin until Batch 11 (Talents) is complete and the talent architecture's impact on the Schema is understood. Upload this brief alongside the source documents listed above when beginning the redesign work.*
