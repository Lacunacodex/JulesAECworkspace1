# THE ÆTHERIUM CODEX — ERRATA
## Corrections to Documents 1 and 2 (Parts 1-3)
### Compiled April 16, 2026

---

## PURPOSE

This document catalogs every specific error, inconsistency, or outdated reference in the Document 1 (Unified Architecture) and Document 2 (Combat Engine, Parts 1-3) output files. Each entry identifies the error, cites the canonical source, and provides the correct value. A single consolidation pass will incorporate these corrections after Document 3 is complete.

The architectural decisions in these documents remain sound. These are formula-level, terminology-level, and mechanical-detail corrections — not structural redesigns.

---

# SECTION 1: HP POOL FORMULAS

## Error 1.1 — HP Formula (All Documents)

**Where it appears:** Document 1 (Section: Resource Pools), Document 2 Part 1 (Part V: Unified FP System — HP reference), Document 2 Part 3 (Part IV: Damage Application)

**What was written:** Various formulas used, including (Primary Attr × 3) + (Secondary Attr × 3) + (Mastery × 5) in some places, and inconsistent references elsewhere. Document 1 referenced a formula from the outdated Character Creation v3 document.

**Canonical source:** Player's Guide V4.1, Chapter 2

**Correct formulas:**

| Pillar | Pool Name | Formula |
|---|---|---|
| Physical | Health (Vitality) | (Vigor × 3) + (Might × 3) + (Mastery × 5) |
| Mental | Resolve (Clarity) | (Wits × 3) + (Intellect × 3) + (Mastery × 5) |
| Social | Reputation (Poise) | (Presence × 3) + (Composure × 3) + (Mastery × 5) |
| Metaphysical | Pattern (Pattern Integrity) | (Integrity × 3) + (Anima × 3) + (Mastery × 5) |

**Verification:** At starting state (all attributes 1, Mastery 3): (1×3)+(1×3)+(3×5) = 21. Matches character profile.

---

# SECTION 2: HP POOL NAMING

## Error 2.1 — Inconsistent Pool Names

**Where it appears:** Document 1 (multiple sections), Document 2 Parts 1-3 (throughout)

**What was written:** Mixed usage of Vitality/Resolve/Poise/Pattern (Document 1 and early Document 2) vs Health/Resolve/Reputation/Pattern (character profile).

**Canonical source:** Player's Guide V4.1 and Character Profile

**Correct names:**

| Pillar | HP Pool Name | Condition Track Name |
|---|---|---|
| Physical | Health | Vitality |
| Mental | Resolve | Clarity |
| Social | Reputation | Poise |
| Metaphysical | Pattern | Pattern Integrity |

The HP pool and the condition track have DIFFERENT names for the same pillar. Health is the pool; Vitality is the track. Reputation is the pool; Poise is the track. Documents should use the correct name for the correct context.

---

# SECTION 3: DEFENSE SYSTEM

## Error 3.1 — Defense TN Formula

**Where it appears:** Document 2 Part 3 (Part II: Static Defense Mechanics)

**What was written:** "Defense TN = 10 + Pillar Defense Modifier + Mastery + Talent Bonuses + Protection Effects" — a base-10 system.

**Canonical source:** Player's Guide V4.1, Chapter 2

**Correct formula:** Defense TN IS the Composite Defense score. No base 10.

**Composite Defense = Dodge Defense + Deflection Defense**

| Pillar | Dodge (Reflex) | Deflection (Fortitude) |
|---|---|---|
| Physical | Finesse + Wits + (Mastery / 2) | Might + Armor Bonus + Shield Bonus + (Mastery / 2) |
| Mental | Acuity + Dominion + (Mastery / 2) | Intellect + Composure + (Mastery / 2) |
| Social | Guile + Wits + (Mastery / 2) | Presence + Intellect + (Mastery / 2) |
| Metaphysical | Anima + Acuity + (Mastery / 2) | Integrity + Vigor + (Mastery / 2) |

Attack check = d20 + Attribute + Skill/Talent + Modifiers vs. Composite Defense.

## Error 3.2 — Soak Formula

**Where it appears:** Document 2 Part 3 (Part II: Static Defense Mechanics) — referenced but not specified correctly.

**Canonical source:** Player's Guide V4.1

**Correct Soak formulas:**

| Pillar | Soak |
|---|---|
| Physical | ((Vigor + Mastery) / 2) + Armor Soak |
| Mental | ((Wits + Mastery) / 2) + Talent Bonuses |
| Social | ((Composure + Mastery) / 2) + Status/Title Bonuses |
| Metaphysical | ((Integrity + Mastery) / 2) + Faith/Pact Bonuses |

## Error 3.3 — Damage Threshold Formula

**Where it appears:** Document 2 Part 3 (Part IV: Damage Application)

**What was written:** "Threshold = (Primary Attribute for that Pillar × 2) + Mastery + Threshold Bonus"

**Canonical source:** Player's Guide V4.1

**Correct Threshold formulas:**

| Pillar | Damage Threshold |
|---|---|
| Physical | (Vigor + Mastery) × 2 |
| Mental | (Wits + Mastery) × 2 |
| Social | (Composure + Mastery) × 2 |
| Metaphysical | (Integrity + Mastery) × 2 |

At starting state (attribute 1, Mastery 3): (1+3)×2 = 8. Matches character profile.

## Error 3.4 — The 4×4 Defense Matrix Labels

**Where it appears:** Document 1 (Section: Defense Architecture), Document 2 Part 3 (Part II)

**What was written:** Document 1 established pillar-specific defense axis names (Evasion/Guard/Toughness/Vigor for Physical, Willpower/Control/Conviction/Courage for Mental, Grace/Dignity/Composure/Discretion for Social, Acuity/Integrity/Resilience/Essence for Metaphysical).

**Canonical source:** Player's Guide V4.1 uses generic Dodge/Deflection/Soak/Threshold for all four pillars. The talent manual used a third naming scheme. The character profile uses Dodge/Deflect/Soak/Thresh.

**Resolution needed:** The pillar-specific defense axis names (Willpower/Control/Conviction/Courage etc.) are architecturally valid and provide richer mechanical identity. However, the canonical character profile uses the generic names. This is a DESIGN DECISION to be locked, not an error to be corrected — Alex should confirm whether to use the generic Dodge/Deflect/Soak/Thresh across all pillars or adopt pillar-specific names.

---

# SECTION 4: CONDITION TRACKS

## Error 4.1 — Condition Track Penalty Values

**Where it appears:** Document 2 Part 3 (Part IV: Damage Application and Condition Tracks)

**What was written:** Linear penalty ramp: -1 at step -1, -2 at step -2, etc. Also invented pillar-specific terminal states (Dying/Broken/Disgraced/Unmade).

**Canonical source:** Player's Guide V4.1, Chapter 2

**Correct penalties:**

| Step | Penalty | Physical | Mental | Social | Metaphysical |
|---|---|---|---|---|---|
| 0 | — | Normal | Normal | Normal | Normal |
| -1 | -1 | Winded | Distracted | Flustered | Frayed |
| -2 | -2 | Reeling | Shaken | Humbled | Strained |
| -3 | -5 | Wounded | Frightened | Disgraced | Corrupted |
| -4 | -10 | Crippled | Befuddled | Rapt | Unraveling |
| -5 | Incapacitated | Unconscious/Dying | Catatonic | Broken | Dissolving |

**Critical rules:**
- Steps REPLACE within a track (not cumulative with themselves)
- Steps across DIFFERENT tracks ARE cumulative
- 0 HP on any pool = immediate drop to Incapacitated (bottom)
- 0 Physical/Mental HP = Unconsciousness
- 0 Social/Metaphysical HP = Emotional Collapse (confusion effect)
- Metaphysical track steps produce temporary narrative detriments (not beneficial mutations)
- External afflictions (Cursed, Poisoned, etc.) are Layer 3, separate from track steps

## Error 4.2 — Track Recovery Rates

**Where it appears:** Document 2 Part 3 (Part IV) — invented Scope-based recovery rates per step.

**Status:** The Player's Guide does not specify per-step recovery rates. The rates I invented (S2 for -1, S3 for -2, etc.) are design proposals, not corrections of existing canon. They should be flagged as proposals pending confirmation rather than treated as established mechanics.

---

# SECTION 5: DEGREES OF SUCCESS

## Error 5.1 — Four vs Five Degrees in Combat

**Where it appears:** Document 2 Part 3 (Part III: The Critical System)

**What was written:** Four-state combat system: Critical Success / Hit / Miss / Critical Failure. "Success with Flaw" was explicitly dropped with the note "doesn't translate cleanly to combat."

**Canonical source:** Player's Guide V4.1, Section 1.2 and 1.3

**Correct:** Five degrees of success apply to ALL checks including attack rolls:

| Result | Degree | Combat Application |
|---|---|---|
| ≥ TN+10 OR natural 20 that succeeds | Critical Success | Full damage + isotope critical expression + 1 FP refund |
| ≥ TN | Success (Hit) | Normal damage |
| 1-4 below TN | Success with Flaw | Hit lands but at a cost — overextension, weapon stress, self-exposure |
| 5-9 below TN | Failure (Miss) | No damage |
| ≤ TN-10 OR natural 1 | Critical Failure | No damage + engaged actors gain bonus tempo |

**Design work needed:** Define what "Success with Flaw" means mechanically in combat. Suggestions from the Player's Guide examples: "you pick the lock but your tools break; you hit the enemy but overextend." Combat equivalents:
- You deal damage but provoke a free reaction from the target
- You deal damage but your weapon takes one step on its condition track
- You deal damage but end the action in a disadvantageous position (grant Flat-Footed to next attacker)
- You deal damage but the effort costs 1 additional FP from the relevant pool

This is a design decision, not a formula correction.

---

# SECTION 6: FP UNIFICATION

## Note 6.1 — Stamina Formula Change

**Where it appears:** Document 2 Part 1 (Part V: Unified FP System)

**What was written:** Physical FP = (Vigor + Tc) × Mastery. This REPLACES the canonical Stamina formula.

**Canonical Stamina formula (Player's Guide):** (Vigor + Mastery) × 2

**Canonical ÆP formula (SRD v3):** (Dominion + Tₘ) × Mastery

**Status:** The FP unification was an intentional design decision approved by Alex. The Physical FP formula deliberately changes the Stamina calculation to parallel the ÆP structure. This is NOT an error — it is a locked design change. However, the following should be verified:

**Verification needed:** Does (Vigor + Tc) × Mastery produce appropriate starting values compared to the old (Vigor + Mastery) × 2?

| | Old Stamina | New Physical FP |
|---|---|---|
| Starting (Vigor 1, Mastery 3, Tc=5) | (1+3)×2 = 8 | (1+5)×3 = 18 |
| Journeyman (Vigor 3, Mastery 5, Tc=10) | (3+5)×2 = 16 | (3+10)×5 = 65 |
| Master (Vigor 4, Mastery 8, Tc=15) | (4+8)×2 = 24 | (4+15)×8 = 152 |

The new formula produces significantly larger pools. This is intentional (pools naturally scale with character investment). But the universal cost formula (ESL × 2) − 1 and drip recharge rates need to be tuned against these larger pools during playtesting.

## Note 6.2 — Stamina Regeneration Rate

**Where it appears:** Document 2 Part 1 (Part V: Drip Recharge)

**What was written:** "Base rate is one FP per S2 interval per pool" with ×1/×2/×4 conditional multipliers.

**Canonical Stamina regeneration (Player's Guide):** Mastery Rating × 2 per 10 minutes.

**Status:** The canonical Stamina regen produces specific numbers (Mastery 3 = 6 per 10 min, Mastery 5 = 10 per 10 min, Mastery 8 = 16 per 10 min). The "1 FP per interval" generic drip produces much lower numbers. These need reconciliation.

**Possible resolution:** The drip rate should be Mastery × 2 per S2 interval per pool under stressful conditions, doubled to Mastery × 4 under calm conditions, quadrupled to Mastery × 8 during sleep/rest. This preserves the ×1/×2/×4 structure while matching canonical Stamina regen as the ×1 baseline.

---

# SECTION 7: TERMINOLOGY CORRECTIONS

## Error 7.1 — "Poise" as HP Pool Name

**Where it appears:** Document 1, Document 2 Parts 1-3 (multiple references)

**What was written:** Social HP pool called "Poise" throughout.

**Correct:** Social HP pool is "Reputation." The Social condition track is "Poise." These are different things.

## Error 7.2 — "Vitality" as HP Pool Name

**Where it appears:** Document 1, some Document 2 references

**What was written:** Physical HP pool called "Vitality."

**Correct:** Physical HP pool is "Health." The Physical condition track is "Vitality."

## Error 7.3 — "Pattern" Ambiguity

**Status:** "Pattern" is used for both the Metaphysical HP pool AND the condition track name (Pattern Integrity). The Player's Guide distinguishes them as "Pattern Pool" and "Pattern Integrity (Track)." This should be consistently disambiguated in all documents.

## Error 7.4 — "Composite Defense" vs "AC" vs "Combined Defense"

**Where it appears:** Document 2 Part 3 (Part II)

**What was written:** References to "Defense TN" with a base-10 structure.

**Correct term:** Composite Defense. The sum of Dodge + Deflection for the relevant pillar. No base 10. The Player's Guide explicitly defines this and uses it as the attack roll target.

---

# SECTION 8: SKILL SYSTEM

## Note 8.1 — Skill List Evolution

**Where it appears:** Document 2 Part 2 (S0 action atoms reference social skills)

**Status:** The Player's Guide V4.1 shows the legacy 12-skill system in 6 Mundane/Magical pairs. The character profile shows the current 16-skill system in 4-per-pillar groups. Documents should use the current 16-skill system:

| Physical | Mental | Social | Metaphysical |
|---|---|---|---|
| Athletics | Lore | Streetwise | Metaphysics |
| Skullduggery | Medicine | Performance | Operate |
| Conveyance | Artifice | Influence | Insight |
| Survival | Discovery | Valuation | Praxis |

The legacy Mundane/Magical pair concept is superseded. Skills are now grouped by pillar, not by domain pairs.

## Note 8.2 — Skill Petal Assignment at Character Creation

**Where it appears:** Document 2 Part 1 (FP formula references petal talent counts Tc/Tk/Ts/Tₘ)

**Status:** Character Creation v3 distributes skills across Combat/Knowledge/Philosophy (three petals). The current system has four skill groups matching the four pillars. The FP formula uses four talent counts (one per petal). The petal-to-pillar mapping needs explicit confirmation:

| Petal | Pillar | Skills in This Petal |
|---|---|---|
| Combat | Physical | Athletics, Skullduggery, Conveyance, Survival |
| Knowledge | Mental | Lore, Medicine, Artifice, Discovery |
| Social | Social | Streetwise, Performance, Influence, Valuation |
| Philosophy | Metaphysical | Metaphysics, Operate, Insight, Praxis |

Character Creation v3 uses a 9/7/5 spread across THREE petals (Combat/Knowledge/Philosophy) with Social absent. If Social is now a fourth petal, the creation spread needs updating to accommodate four groups.

---

# SECTION 9: DOCUMENT-SPECIFIC CORRECTIONS

## Document 1 — Unified Architecture

**9.1:** The Mastery tier labels (1-4 Novice, 5-7 Journeyman, 8-10 Master) are correct and match all canonical sources.

**9.2:** The Scope scale (S0-S9+S∞) is original architecture from this session and has no canonical conflict.

**9.3:** The "Essence replaces Anima" decision from Document 1 needs verification — the Player's Guide and character profile both still use "Anima" as the Metaphysical attribute. If Essence was locked as a rename, all canonical documents need updating. If it was NOT locked, Document 1 needs correction.

## Document 2 Part 1 — Combat Engine Foundations

**9.4:** Part I (19+Variable effects) correctly references SRD v3 Amendment 1. No corrections needed.

**9.5:** Part II (Four Tiers of Expression) is original architecture. No canonical conflicts.

**9.6:** Part III (S0 Baseline) lists "Push" as mapping to "Movement (forced)." SRD v3 has "Move Object" as the telekinesis/force-movement effect. Push should map to Move Object, not Movement.

**9.7:** Part VI (Scope-CP Geometry) correctly references SRD v3 Amendment 6. No corrections needed.

**9.8:** Part IX (Systemic Catalyst) correctly references SRD v3 Amendment 4. No corrections needed.

## Document 2 Part 2 — Resolution Mechanics

**9.9:** Part I (Engagement States) — architecturally sound, no corrections needed.

**9.10:** Part II (Reaction Economy) — architecturally sound, no corrections needed.

**9.11:** Part III (Multi-Pillar Combat) — references to "Poise" as Social HP should be "Reputation."

**9.12:** Part V-VII (Action Atoms) — FP costs and pillar references are architecturally correct but use the wrong HP pool names in places.

## Document 2 Part 3 — Resolution at the Dice Level

**9.13:** Part I (Initiative) — tempo-weighted initiative (Wits + Mastery) is correct and does not conflict with canonical sources.

**9.14:** Part II (Static Defense) — defense formula is WRONG (see Error 3.1). Needs full replacement with Composite Defense system.

**9.15:** Part III (Critical System) — needs expansion from 4 to 5 degrees (see Error 5.1). The isotope critical expression and FP refund/bonus tempo mechanics are new design work that doesn't conflict with canon — they extend the five-degree system.

**9.16:** Part IV (Damage Application) — threshold formula is WRONG (see Error 3.3). Condition track penalties are WRONG (see Error 4.1). 0 HP rule is MISSING (see Error 4.1). Aggregated damage per phrase is a new design decision — architecturally sound but needs the correct threshold formula applied.

**9.17:** Part V (Weapon/Item Mechanics) — references SRD v3 correctly. No corrections needed.

**9.18:** Part VI (Advanced Reaction Chains) — architecturally sound, no corrections needed.

**9.19:** Part VII (Multi-Scope Scenarios) — worked examples are architecturally sound. The 1-tempo transition cost was validated through scenarios. No corrections needed.

**9.20:** Part VIII (Systemic Catalyst Examples) — historically sourced examples are correct. No corrections needed.

**9.21:** Part IX (Pressure Point Engagement) — architecturally sound, no corrections needed.

**9.22:** Part X (Smoothing Effect) — correctly identifies Smoothing as structural rather than dice-level. No corrections needed.

---

# SECTION 10: DESIGN DECISIONS PENDING CONFIRMATION

The following items were proposed during Document 1-2 development and accepted in conversation, but may need re-examination against canonical sources:

**10.1:** Essence replacing Anima as attribute name — verify against current canonical usage.

**10.2:** The four-petal creation spread — if Social is now a fourth petal, the 9/7/5 creation spread from Character Creation v3 needs updating to a four-group distribution.

**10.3:** The FP unification (Physical/Mental/Social/Metaphysical pools all using (Attribute + T) × Mastery) — intentionally changes the Stamina formula. Drip recharge rates need recalibration against the larger pool sizes.

**10.4:** Success with Flaw in combat — the five-degree system is canonical. The specific mechanical cost of a combat Success with Flaw needs design work.

**10.5:** The pillar-specific defense axis names (Willpower/Control/Conviction/Courage etc. from Document 1) vs the generic Dodge/Deflect/Soak/Thresh from the character profile — choose one system.

---

*End of Errata. Apply corrections during the post-Document 3 consolidation pass.*
