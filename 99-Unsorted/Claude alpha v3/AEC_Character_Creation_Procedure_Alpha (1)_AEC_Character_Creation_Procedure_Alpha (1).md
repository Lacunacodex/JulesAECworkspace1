*Ætherium Codex — Character Creation Procedure*

**THE ÆTHERIUM CODEX**

Character Creation Procedure

State Machine Document — Alpha Build

April 30, 2026 — Phase 3 Output

*This document sequences every step of character creation with explicit inputs, constraints, and outputs. A developer can build a character generator from it. A player can build a character at a table with it.*


# **Propagation Notice**
The following canonical renames have been applied throughout this document. Source files (AC Unified Architecture, SRD v3 Combined, Character Profile, Book of Shadows v6) have not yet been updated to reflect these changes. When cross-referencing this document against source files, apply these mappings:

|**Old Term**|**New Term**|**Source**|
| :- | :- | :- |
|**Integrity (attribute)**|Moiety|CF-17|
|**Anima (attribute)**|Essence|OD-4, Session 10|
|**Insight (skill)**|Instinct|Correction #1, Session 2|
|**Acuity (Meta. Evade defense)**|Elusivity|This session|
|**Essence (Meta. Resist defense)**|Coherence|DEF-1, Session 11|
|**Reputation (Social HP pool)**|Poise|Session 10|
|**Petals (3-group model)**|Pillars (4-group, 9/7/5/3)|OD-5, Session 10|
|**Ki Pool**|Dissolved into FP pool|OD-12, Session 11|


# **The Zero State**
Every entity begins existence at this baseline before any priorities, vocabulary, or XP are applied.

|**Trait**|**Starting Value**|
| :- | :- |
|**Mastery Level**|3 (Passing Knowledge). Purchasable to 5 during creation.|
|**Attributes**|All 12 attributes start at 1 dot.|
|**Skills**|All 16 skills start at 0 ranks.|
|**Backgrounds**|0 dots.|
|**XP Pool**|120 XP (liquid assets for customization in Step 7).|
|**Heritage Attributes**|Separate track. Applied in Step 2. Capped at +2.|
|**Magical Vocabulary**|Universal Grammar (all 0 CP components) free. Three derived pools in Step 5.|


# **Step 1: Psyche Schema**
**Vertebra 1 of the Narrative Engine.** The Schema says WHAT you value. Everything else determines HOW you pursue it.

**Inputs:** Player answers the Character Discovery Guide questionnaire (24 questions from the v2 Player Discovery Guide or cold-administration instrument).

**Process:** GM uses the Translation Guide to map narrative answers onto Schema dimensions: god-name weights, aspect values, Core Philosophy alignment. The player does not need to know the divine names or cosmological structure.

**Outputs:** Psyche Schema profile, college affinity recommendation, Legacy starting seed, FP pressure point identification (outliers, splits, breaks).

**Design Notes**

The Schema is not a personality test in the conventional sense. It is a diagnostic instrument that maps the character’s values onto the setting’s divine coordinate system. Two characters with identical Schema scores but different college affiliations produce completely different fronts because the college determines HOW the profile expresses. The Schema is stored in the character’s soul stone — a physical object in the setting that can be read, queried, stolen, damaged, or transferred.


# **Step 2: Heritage**
**Inputs:** Player choice of ancestry/species.

**Process:** Select Heritage qualities. Each quality is priced at magnitude through Spell Sentence scaling tables (the same grammar that governs spells, items, and mutations). Calculate Heritage rating. Apply Heritage attribute bonuses on a separate track.

**Outputs:** Heritage qualities, Heritage rating, Heritage attribute bonuses (separate track, capped at +2).

**Heritage Rating Formula**

Heritage Rating = (Highest Effective Quality EML + floor((Count − 1) / 4)) × 0.75

**Heritage Attribute Rules**

Heritage attributes function as a separate track from base attributes, similar to the Prodigy/Inept system. Each Heritage attribute bonus is capped at +2. Each ÆC attribute point equals a 3.5e modifier, not a score — a +2 Heritage bonus is equivalent to a +4 ability score bonus in legacy systems.

**PLACEHOLDER:** *Heritage State generation algorithm (Gap #3). The Punnett-square isotope-pair mapping exists conceptually but is not generator-ready. For the alpha build, use pre-built Heritage packages. Full procedural Heritage generation is a future workstream.*


# **Step 3: Attribute Allocation**
**Inputs:** Heritage bonuses from Step 2.

**Process:** Assign pillar priority. Distribute bonus dots across the four attribute groups using the 7/5/5/3 spread. All attributes begin at 1 before the spread is applied.

**Outputs:** 12 attribute scores (base + spread). Heritage bonuses tracked separately.

**The 7/5/5/3 Spread**

Assign priority to the four attribute groups: Physical, Mental, Social, Metaphysical. The primary group receives 7 additional dots. Two secondary groups each receive 5. The quaternary group receives 3. No attribute may exceed Rank 5 during this step.

|**Pillar**|**Attributes**|**Spread Applied To**|
| :- | :- | :- |
|**Physical**|Vigor / Might / Finesse|Distribute assigned dots freely among the three.|
|**Mental**|Wits / Intellect / Acuity|Distribute assigned dots freely among the three.|
|**Social**|Presence / Composure / Guile|Distribute assigned dots freely among the three.|
|**Metaphysical**|Moiety / Dominion / Essence|Distribute assigned dots freely among the three.|

**Constraints**

Creation cap: no attribute above Rank 5 during this step. Attributes are not constrained by Mastery. Heritage bonuses are applied on a separate track and do not count against the creation cap. Additional attribute dots may be purchased in Step 7 using XP (cost: New Rating × 4).


# **Step 4: Skill Allocation**
**Inputs:** Attribute scores from Step 3 (some skills key off specific attributes for checks).

**Process:** Assign pillar priority for skills. Distribute ranks within each pillar’s four skills.

**Outputs:** 16 skill ranks.

**The 9/7/5/3 Skill Spread**

Assign priority to the four skill pillars. The primary pillar receives 9 ranks to distribute. Secondary receives 7. Tertiary receives 5. Quaternary receives 3. Skill ranks are capped by current Mastery (3 at creation unless Mastery is purchased higher in Step 7).

**Skill Grid (16 Skills, 4 Per Pillar)**

|**Physical**|**Mental**|**Social**|**Metaphysical**|
| :- | :- | :- | :- |
|**Athletics**|Lore|Streetwise|Metaphysics|
|**Skullduggery**|Medicine|Performance|Operate|
|**Conveyance**|Artifice|Influence|Instinct|
|**Survival**|Discovery|Valuation|Praxis|

**Design Note**

Pillars are identity labels, not talent access gates. A character’s pillar priority describes who they are, not what they can do. Any talent tree can draw from any pillar’s FP pool. Skill priority and attribute priority do not need to match.


# **Step 5: Magical Vocabulary**
**Every living being in Tessera is composed of planar materials. There is no purely mundane baseline.** This step establishes every character’s starting magical vocabulary before any XP is spent.

**Inputs:** Attribute scores from Step 3 (specifically Intellect, Dominion, Acuity, Essence).

**Process:** Calculate three derived pools. Spend each pool on its designated category. Apply Universal Grammar (free).

**Outputs:** Starting Effect ratings, starting Isotope access, unlocked CP geometry components.

**A. Universal Grammar (Free)**

Every character inherently knows all 0 CP components: Individual, Ray, Emanation, Burst (Small) for shapes. Touch/Self and Close for ranges. Instantaneous and Concentration for durations. No cost, no roll, no purchase required.

**B. Shaping Pool (Effect Vocabulary)**

**Formula:** Intellect + Dominion

Spend these points to purchase starting ratings in Effects (the “verbs” of the Spell Sentence). One point buys one dot in one Effect. No individual Effect rating may exceed current Mastery. The logic: Intellect provides the formula, Dominion provides the command.

**C. Substance Pool (Isotope Vocabulary)**

**Formula:** Acuity + Essence

Spend these points to purchase starting access to Isotopes (the “adjectives” of the Spell Sentence). One point buys one dot in one Isotope. No individual Isotope rating may exceed current Mastery. The logic: Acuity perceives the specific frequency, Essence provides the connection to it.

**D. Grammar Points (CP Geometry)**

**Formula:** Intellect + Dominion

Spend these points to unlock Common-tier Construction Pool components (shapes, ranges, and durations costing 1–4 CP). Components costing 5+ CP (Dialect and Treasure tier) cannot be selected at creation and must be learned through play.

**Note on Pool Separation**

The Shaping Pool and Grammar Points share the same formula (Intellect + Dominion) but are separate pools. A character with Intellect 3 and Dominion 2 receives 5 points for Effects AND 5 points for geometry, not 5 total. The Substance Pool uses a different formula (Acuity + Essence) and is fully independent.


# **Step 6: Background**
**Inputs:** Player choice from 27 backgrounds (SRD v3 Combined).

**Process:** Select one background. Apply its mechanical benefits.

**Outputs:** Starting Clout, skill bonuses, narrative hooks, starting equipment package, college affiliation context.

**The Prince Rule (Social-Background Cap)**

A character cannot purchase a Background rating higher than their highest Social attribute (Presence, Guile, or Composure). This represents the social infrastructure required to maintain external resources. A character with Presence 4 can have Resources 4. A character with all Social attributes at 2 is limited to Background ratings of 2, regardless of available XP.

**College Affiliation**

College affiliation is social membership, not a mechanical gate. A character’s background and Schema affinity recommend a starting college, which provides institutional context, training methodology, and initial talent access patterns. College affiliation can change through play — migration, multi-college training, and personal development expand access beyond origin. The college determines HOW the Psyche Schema profile expresses.


# **Step 7: Talent & XP Spend**
**The 120 XP pool.** This is the customization layer that creates divergent character archetypes from identical base templates. All purchases draw from this single pool.

**Inputs:** 120 XP. All values from Steps 1–6.

**Process:** Spend XP on any combination of the options below. Free starting talents are applied before XP spending.

**Outputs:** Final Mastery, additional attributes/skills, talent list, expanded magical vocabulary, mutation investments, background ratings.

**XP Cost Table**

|**Trait**|**Cost Formula**|**Notes**|
| :- | :- | :- |
|**Mastery**|New Rating × 8|ML 4 = 32 XP. ML 5 = 40 XP (72 XP total from base 3 to 5).|
|**Attribute**|New Rating × 4|Creation cap: Rank 5. Heritage bonuses are separate.|
|**Skill (1st dot)**|3 XP (flat)|Capped by current Mastery.|
|**Skill (2nd+ dot)**|New Rating × 2|Capped by current Mastery.|
|**Talent**|BEL × 3|Prerequisite chaining discount applies.|
|**Effect (1st dot)**|6 XP (flat buy-in)|Rated 1–10. Capped by Mastery.|
|**Effect (advance)**|Current Rating × 4|Advancing from 2 to 3 costs 8 XP.|
|**Isotope (1st dot)**|6 XP (flat buy-in)|Rated 1–10. Capped by Mastery.|
|**Isotope (advance)**|Current Rating × 4|Compounds require constituent pures.|
|**Mutation**|BEL × 3|Same 120 XP budget. Not a separate economy.|
|**Background**|New Rating × 1|Capped by highest Social attribute (Prince Rule).|

**Free Starting Talents**

**PLACEHOLDER:** *Free starting talent count and selection rules are TBD. The alpha build will define a curated starter talent list. These represent the character’s basic training and style prior to play — a specific martial art, a magical tradition, or institutional methodology.*

**Mastery Advancement at Creation**

Mastery purchased during character creation has its benefits apply retroactively. It is considered to be purchased first, before any other XP expenditure. Advancing Mastery raises the cap on skills, Effects, and Isotopes, and increases all derived statistics. The “Hollow Master” archetype (72 XP on Mastery alone, leaving 48 for everything else) and the “Inept Prince” archetype (keep Mastery at 3, invest heavily in Backgrounds) are both valid and intentional build paths.

**PLACEHOLDER:** *Talent system rebuild (BEL assignments) is incomplete. Most talent trees do not yet have finalized BEL values. For the alpha build, reference the curated starter talent list.*

**PLACEHOLDER:** *Spells/rote construction at creation needs further specification. Characters use their Effect ratings, Isotope access, and Grammar Point unlocks from Step 5 plus any XP-purchased vocabulary to compose starting rotes.*


# **Step 8: Derived Statistics**
Calculated after all XP is spent. All formulas reference final attribute values and final Mastery.

**Inputs:** All final values from Steps 1–7.

**Process:** Calculate all pools, defenses, thresholds, and derived values.

**Outputs:** Complete mechanical profile.

**HP Pools (One Per Pillar)**

|**Pillar**|**Pool Name**|**Formula**|
| :- | :- | :- |
|**Physical**|Vitality|(Vigor × 3) + (Might × 3) + (Mastery × 5)|
|**Mental**|Resolve|(Wits × 3) + (Intellect × 3) + (Mastery × 5)|
|**Social**|Poise|(Presence × 3) + (Composure × 3) + (Mastery × 5)|
|**Metaphysical**|Pattern|(Moiety × 3) + (Essence × 3) + (Mastery × 5)|

**Fulcrum Point Pools (One Per Pillar)**

|**Pillar**|**Driving Attribute**|**Formula**|**T Counts**|
| :- | :- | :- | :- |
|**Physical**|Vigor|(Vigor + Tc) × Mastery|Combat pillar talents|
|**Mental**|Acuity|(Acuity + Tk) × Mastery|Knowledge pillar talents|
|**Social**|Guile|(Guile + Ts) × Mastery|Social pillar talents|
|**Metaphysical (ÆP)**|Dominion|(Dominion + Tₘ) × Mastery|Philosophy pillar talents|

Some specific talent trees may override the default pillar draw, calling FP from their invested tree’s pool rather than the pillar default. The universal FP action cost is (ESL × 2) − 1.

**Composite Defense (Per Pillar, No Base 10)**

Composite Defense = Dodge + Deflection. Attack checks roll d20 + Attribute + Skill/Talent + Modifiers against the target’s Composite Defense.

|**Pillar**|**Dodge (Evade)**|**Deflection (Deflect)**|
| :- | :- | :- |
|**Physical**|Finesse + Wits + (Mastery/2)|Might + Armor + Shield + (Mastery/2)|
|**Mental**|Acuity + Dominion + (Mastery/2)|Intellect + Composure + (Mastery/2)|
|**Social**|Guile + Wits + (Mastery/2)|Presence + Intellect + (Mastery/2)|
|**Metaphysical**|Essence + Acuity + (Mastery/2)|Moiety + Vigor + (Mastery/2)|

**Soak (Absorb) and Threshold**

|**Pillar**|**Soak Formula**|**Threshold Formula**|
| :- | :- | :- |
|**Physical**|((Vigor + Mastery)/2) + Armor Soak|(Vigor + Mastery) × 2|
|**Mental**|((Wits + Mastery)/2) + Talent Bonuses|(Wits + Mastery) × 2|
|**Social**|((Composure + Mastery)/2) + Status/Title|(Composure + Mastery) × 2|
|**Metaphysical**|((Moiety + Mastery)/2) + Faith/Pact|(Moiety + Mastery) × 2|

**Defense Names (16 Unique)**

|**Function**|**Physical**|**Mental**|**Social**|**Metaphysical**|
| :- | :- | :- | :- | :- |
|**Evade**|Evasion|Willpower|Grace|Elusivity|
|**Deflect**|Guard|Control|Dignity|Integrity|
|**Absorb**|Toughness|Conviction|Composure|Resilience|
|**Resist**|Vigor|Courage|Discretion|Coherence|

**Other Derived Values**

|**Value**|**Formula**|
| :- | :- |
|**Construction Pool**|(½ Effect Tier) + (½ Isotope Tier) + Mastery + Moiety|
|**Complexity Pool**|Same formula as Construction Pool|
|**Mutation Threshold**|Moiety × 5|
|**Tempo Pool**|Wits + Mastery|
|**ÆP Cost (per rote)**|(ESL × 2) − 1|
|**Anchor Cap**|ceil(Base EML / 2)|
|**Mastery Capacity Pool**|Mastery × 4 (base). Max: Mastery × 34 (with Expanded Consciousness).|


# **Step 9: Equipment**
**Inputs:** Background starting package from Step 6. Any remaining XP from Step 7.

**Process:** Select or purchase starting gear. Background provides a base equipment package.

**Outputs:** Equipment list with stat blocks.

**PLACEHOLDER:** *No equipment stat block catalogue exists. For the alpha build, use narrative equipment descriptions tied to background packages. Full equipment catalogue is a future workstream requiring an estimated 4–6 hours of creation.*


# **Step 10: Legacy Initialization**
**This is NOT a player choice step.** It is what the system sees when it reads everything the player has already decided. Identity crystallizes from pattern recognition, not forward-facing milestone achievement.

**Inputs:** The complete character sheet from Steps 1–9: Psyche Schema profile, Heritage, attributes, skills, college affiliation, background, talent selections, magical vocabulary, equipment.

**Process:** The GM reads the accumulated pattern of choices backward. The Palimpsest has already been recording this soul’s history. The starting Legacy state is derived from what the character’s pre-play existence reveals about who they are.

**Outputs:** Starting Legacy traits. Each trait provides a mechanical bonus in situations that align with the pattern and a mechanical penalty in situations that contradict it. Legacy modifies how Schema scores are weighted — not the scores themselves, but their significance.

**The Backward-Facing Read**

The Legacy System does not ask “what did you accomplish?” It asks “what pattern do your accumulated choices reveal about who you are?” A character who prioritized Physical attributes, took combat talents, chose a military background, and affiliated with Stormpeak has a pattern. That pattern crystallizes into Legacy traits that were not planned or assigned — they emerged from the accumulated shape of the character.

**What a Legacy Trait IS**

A permanent modifier reflecting accumulated pattern. It may provide a mechanical bonus in situations that align with the pattern, a mechanical penalty in situations that contradict it, or both. The trait is the character’s identity crystallized into a rule. Legacy traits are descriptive, not prescriptive. They describe who the character HAS BEEN, not who they SHOULD BE. The character can act against their Legacy — doing so creates friction (the trait’s penalty applies), which is itself a story moment.

**How Legacy Interacts with the Schema**

The Legacy trait modifies how the Schema is read. A character with a Legacy trait of “Protector” has their Constantine (Duty) score read with that specificity — the duty is now defined by the pattern of protective action. The Schema numbers do not change. Their weight and significance shift based on what the Legacy reveals.

**During Play**

After every significant cycle (typically every 3–5 sessions, or at the end of a campaign arc), the GM and player review the character’s accumulated actions. When the backward read reveals a consistent pattern, the GM proposes a new Legacy trait. The trait is discussed collaboratively. If both agree the pattern is genuine, the trait is added to the character sheet. The soul stone carries all Legacy data in-setting.


# **Appendix A: Condition Tracks**
Each pillar has a five-step condition track. When the corresponding HP pool reaches 0, subsequent damage drives the character down the track. Penalties are cumulative with the track position, not with each other.

|**Track**|**Step 1 (−1)**|**Step 2 (−2)**|**Step 3 (−5)**|**Step 4 (−10)**|**Step 5**|
| :- | :- | :- | :- | :- | :- |
|**Vitality (Physical)**|Winded|Reeling|Wounded|Crippled|Incapacitated|
|**Clarity (Mental)**|Distracted|Shaken|Frightened|Befuddled|Catatonic|
|**Poise (Social)**|Flustered|Humbled|Disgraced|Rapt|Broken|
|**Pattern Integrity (Meta.)**|Frayed|Strained|Corrupted|Unraveling|Dissolving|


# **Appendix B: Five-Degree Critical Table**

|**Degree**|**Attacker Gets**|**Target Gets**|
| :- | :- | :- |
|**Critical Success**|Full effect + isotope expression + 1 FP refund|Nothing extra|
|**Success**|Full effect|Nothing extra|
|**Success with Flaw**|Full effect|Free reaction trigger (costs FP to exploit)|
|**Failure**|Nothing|Nothing|
|**Critical Failure**|Nothing|All engaged actors gain 1 bonus tempo (free)|


# **Appendix C: Placeholder Steps**
The following elements are identified as incomplete and flagged for future workstreams. They do not block the alpha build — each has a defined workaround.

|**#**|**Placeholder**|**Workaround**|**Estimated Effort**|
| :- | :- | :- | :- |
|**1**|Heritage State generation algorithm (Gap #3)|Pre-built Heritage packages|Requires Punnett-square mapping formalization|
|**2**|Free starting talent count and selection rules|Curated alpha starter list|Depends on talent rebuild|
|**3**|Talent system rebuild (BEL assignments)|Reference partial talent archive|Major workstream — all 24 trees|
|**4**|Spells/rote construction at creation|Use Step 5 vocabulary + XP purchases|Needs worked examples|
|**5**|Equipment stat block catalogue|Narrative descriptions per background|4–6 hours estimated|


# **Appendix D: Casting Philosophies**
Every character chooses a casting philosophy at creation. This is a character identity choice, not a talent purchase.

|**Philosophy**|**Primary Attribute**|**Advantage**|**Weakness**|
| :- | :- | :- | :- |
|**Architect (Studied)**|Intellect|Recipe Optimization: FR reduction by ESL band (−4/−3/−2). Complexity Mastery: bonus to Complexity Pool = ⌊Dominion ÷ 2⌋. Intellect-based Metamagic efficiency.|Tactical rigidity. Rotes are fixed once designed.|
|**Improviser (Innate)**|Essence|On-the-fly modification: swap Additives or primary Isotope mid-cast. Essence-based ÆP reduction: per-rote Base ÆP reduced by (Essence − 3), minimum 0.|No Final Rank reduction. Less efficient foundations.|
|**Polymath**|Both|Maintains separate repertoires of optimized and flexible forms. Most versatile.|Requires investment in both paths. Rarest practitioners.|


# **Document Provenance**

|**Field**|**Value**|
| :- | :- |
|**Document**|Character Creation Procedure — State Machine (Gap #5)|
|**Version**|Alpha 1.0|
|**Date**|April 30, 2026|
|**Session**|Phase 3 — Character Creation Procedure|
|**Canonical Sources**|AC Unified Architecture, SRD v3 Combined, Book of Shadows v6, CC Guide v1, CC v3.0, Operating Philosophy (Doc 0), Session Handoffs 1–11|
|**Placeholders**|5 (Heritage algorithm, starting talents, talent rebuild, spells, equipment)|
|**Open Propagation Items**|7 renames (see Propagation Notice)|
|**License**|ORC — mechanics are Licensed Material. All Tessera proper nouns, lore, art, and setting elements are Reserved Material.|

Page 
