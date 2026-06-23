# THE ÆTHERIUM CODEX — THE COMBAT ENGINE
## Document 2, Part II: Resolution Mechanics
### Canonical Draft — April 15, 2026

---

## PREAMBLE

Part I established the architectural foundations — the 19+Variable effects as universal verbs, the four tiers of expression, the tempo model, the unified Fulcrum Point system, the Scope-CP geometry tiers, the nested clock architecture, and the Systemic Catalyst as mechanical bridge. Part II covers the resolution mechanics that produce playable combat at any Scope: engagement states, the reaction economy, multi-pillar combat calculation, multi-Scope play rules, and representative S0-S2 action atoms showing how the universal grammar produces specific observable actions.

---

# PART I: ENGAGEMENT STATES

## Core Principle

Combat does not have a binary "fight/no fight" state. It has a three-state model that applies identically at every Scope — what differs is the temporal resolution of each state transition and the consequences of shifting between them.

## The Three States

**Disengaged:** Not in active conflict. Normal action economy. Full access to all Scope levels simultaneously. No threat awareness occupying bandwidth. The baseline.

**Threatened:** Active conflict possible or imminent. A hostile actor is within reach but exchanges have not yet begun. Attention is forced onto the potential threat. Cross-Scope attention is constrained — you cannot fully engage with S7 strategic planning while someone is about to punch you.

**Engaged:** Active conflict in progress. Phrase structure applies. Tempo budget is consumed. Reactions are triggered by opponent actions. Participants cannot freely disengage without cost.

## State Transitions

### Entering Threatened (from Disengaged)

**Cost:** Free. You don't choose to be threatened — the situation imposes it. Any character becoming aware of a hostile actor within effective range automatically enters Threatened.

**Effect:** Character's attention is forced onto the threat. Any ongoing higher-Scope tempo allocation is interrupted by the threshold-of-relevance test (see Part IV).

### Entering Engaged (from Threatened)

**Cost:** 1 tempo for the character initiating engagement. The initiator "starts the phrase."

**Effect:** All characters in the engagement zone who were Threatened now shift to Engaged. The phrase begins. Tempo budgets activate. Reaction triggers go live.

### Exiting Engaged (back to Threatened)

**Cost:** 2 tempo for the disengaging character PLUS a Reaction trigger for every still-Engaged opponent (see Part II).

**Effect:** Character breaks contact. Phrase structure for that character ends. Opposing characters may still be Engaged with each other.

### Exiting Threatened (back to Disengaged)

**Cost:** Free but requires condition — opponent moves beyond effective range, situation resolves, third-party intervention removes the threat.

**Effect:** Character returns to baseline. Full Scope access restored.

## Universal Pattern Across Scopes

The same three-state model applies at every Scope. What changes is the temporal resolution:

| Scope | Threatened Lasts | Engaged Phrase Duration | Disengaging Requires |
|---|---|---|---|
| S0 | Seconds | Fraction of a second to minute | Breaking physical contact |
| S1 | Minutes | Seconds to minutes | Tactical withdrawal |
| S2 | Tens of minutes | Minutes | Squad-level reposition |
| S3 | Hours | Tens of minutes to hours | Operational retreat |
| S4 | Hours to days | Hours | Battlefield withdrawal |
| S5 | Days | Days | Campaign strategic shift |
| S6 | Weeks | Weeks | Theater-level retreat |
| S7 | Months | Months | Institutional withdrawal |

A character can be Engaged at S0 (currently fighting) AND Threatened at S7 (institutional conflict brewing) AND Disengaged at S3 (no operational fight in progress). Different Scopes have different states simultaneously.

## Asymmetric Cost Pattern

Moving INTO engagement is cheap. Moving OUT is expensive. This is universal across Scopes and matches real-world conflict physics.

- Starting a fight costs 1 tempo. Starting a war costs less than ending one.
- Breaking contact requires opponents to allow it. At higher Scopes, the costs become political, economic, and reputational rather than purely tempo-based, but the asymmetry persists.

Combat engine implication: players choosing to engage should understand the exit cost. A character committing to S0 combat is committing their tempo budget for the phrase and paying to break contact afterward. A character committing to S5 campaign conflict is committing weeks to months and cannot simply decide to stop.

---

# PART II: THE REACTION ECONOMY

## Core Principle

Reactions happen OUTSIDE a character's own phrase, triggered by specific events. They consume FP out of turn, not tempo. Tempo is bandwidth for YOUR phrase actions. FP is fuel for all actions, yours and reactive. The pool is the only limit.

This separation means tactical tension shifts from "should I save tempo for defense?" to "how much FP do I want to spend on offense vs. reserve for defense?" The FP pool is the battlefield resource.

## Trigger Events

Reactions can only be declared when triggered. Valid triggers:

**Physical triggers:**
- Incoming attack targeting you or an ally within reach
- Hostile movement into your threatened zone
- Spell or effect affecting an area you occupy
- Environmental hazard activating within reach

**Mental triggers:**
- Mental pillar attack targeting you
- Affliction effect attempting to impose a condition
- Senses effect probing your mind or information
- Mind Link attempting to establish connection

**Social triggers:**
- Social pillar attack targeting your standing
- Public accusation or challenge
- Attempt to manipulate your reputation
- Compel effect attempting to force behavior

**Metaphysical triggers:**
- Isotope expression contacting your body
- Planar bleed pressure exceeding threshold
- Spell effect targeting your Metaphysical pillar
- Nullify or Transform attempt on your active expressions

## Reaction Declaration

When triggered, a character may declare a reaction. The reaction:

1. Specifies an Effect + Isotope + ESL combination
2. Effective Spell Level capped by the reacting character's Mastery
3. Costs FP from the pillar pool matching the reaction's effect: (ESL × 2) − 1
4. Must be a reactive-appropriate effect (Protection, Nullify, Movement, Senses, Healing, Affliction counter, etc.)
5. Does NOT consume the reacting character's tempo from their own phrase

## Reaction-Appropriate Effects

Not all effects can be reactions. The reaction must respond to the trigger:

| Trigger Type | Appropriate Reaction Effects |
|---|---|
| Incoming Damage | Protection (parry/shield/ward), Movement (dodge), Nullify (counter-spell) |
| Incoming Affliction | Protection (resist), Nullify (cancel), Healing (immediate) |
| Incoming Illusion | Senses (pierce), Nullify (dispel) |
| Incoming Mind Link | Nullify (sever), Protection (mental ward) |
| Incoming Movement/Teleport | Protection (bind), Senses (tracking) |
| Incoming Transform | Nullify (prevent), Immunity (if available) |
| Detection of hidden threat | Senses (reveal), Damage (preemptive strike) |

The GM judges appropriateness. The rule of thumb: a reaction effect must plausibly respond to what's actually happening.

## Scaling Reactions

Mastery caps reaction ESL regardless of Scope. An EML 9 reaction at Scope 0 is still an EML 9 reaction — and high-EML effects tend to cascade across Scopes. A master's parry against an assassin's strike might produce S1-S2 consequences simply because the mechanical outcome is too significant to stay contained.

This is the mechanical basis for legendary defensive moments. A master's reaction isn't just blocking an attack — it's producing a reality-ripple that observers at higher Scopes register. The duelist whose parry is so perfect that it becomes strategic intelligence for the whole campaign.

## Pool Limits

You can only spend what you have. If your Physical FP is depleted, no physical reactions are possible. If your Metaphysical FP is depleted, no magical reactions. The FP pool IS the ceiling on total action quantity across the phrase — your own actions plus your reactive actions.

Characters who burn through their FP on offense have nothing left for defense. This is the meaningful resource tension the FP system produces.

## Exothermic Reactions — Nullify

Nullify reactions carry collateral damage scaling with target ESL (SRD v3, Amendment 8F).

| Target ESL Countered | Energy Release | Collateral |
|---|---|---|
| 1-2 | Negligible to Minor | No collateral |
| 3-4 | Noticeable to Significant | Adjacent squares may take 1d4 damage |
| 5-6 | Dangerous to Major | Area burst, 15 ft radius, 2d6 damage |
| 7-8 | Massive containment | Area burst, 30 ft radius, 4d6 damage, additional effects |
| 9-10 | Cosmic hiccup | GM arbitrates — reality may temporarily destabilize |

Nullify at ESL 5+ is an OFFENSIVE action that happens to neutralize incoming magic as a side effect. A character reactively countering a high-ESL spell with Nullify damages everything in the burst zone, including allies.

---

# PART III: MULTI-PILLAR COMBAT

## Core Principle

Combat in Tessera engages any combination of the four pillars — Physical, Mental, Social, Metaphysical — simultaneously. A fight can be Physical (sword strikes), Mental (psychic assault), Social (public challenge), and Metaphysical (isotope corruption) all at once. The system handles this through primary pillar focus with explicit crossing, modified by Interaction Type.

## Primary Pillar Focus

Every encounter has a primary pillar determined by the situation:

| Encounter Type | Primary Pillar | Typical Secondary |
|---|---|---|
| Sword fight | Physical | Mental (intimidation) |
| Courtroom duel | Social | Mental (rhetorical warfare) |
| Magical exchange | Metaphysical | Physical (collateral damage) |
| Interrogation | Mental | Social (authority) |
| Corporate takeover | Social | Knowledge-petal planning |
| Military campaign | Physical (aggregate) | Social (command) |
| Intelligence operation | Mental (analysis) | Social (agents) |

Actions default to the primary pillar. Defense checks default to the pillar's relevant defense stat. Damage applies to the pillar's HP pool. Condition tracks advance for the pillar being damaged.

## Explicit Pillar Crossing

A character may attack a different pillar than the encounter's primary focus. This is always available but always visible — the crossing declares itself.

**Example 1:** In a sword fight (Physical primary), a character uses a Demoralize action to target the opponent's Mental pillar. The fight continues Physical for everyone else, but the demoralized character takes Mental damage.

**Example 2:** In a courtroom duel (Social primary), a character uses a Channeled Strike through a concealed knife to target the opponent's Physical pillar. The social duel continues, but physical damage is now also in play.

Pillar crossing is mechanically valid but socially/narratively consequential. Using a lethal weapon in a courtroom duel is legally actionable. Demoralizing an opponent in a sword fight is considered dishonorable by some traditions.

## Interaction Type Modifiers

When an effect from one pillar or plane interacts with a target's defending pillar, the Interaction Type modifier applies (SRD v3 Planar Strain model, extended):

| Interaction | Modifier | Application |
|---|---|---|
| **Cooperative** | ×0.25 | Effect aligns with target's existing state |
| **Competing** | ×1.0 | Standard conflict — default calculation |
| **Cancellation** | ×1.5 | Effects actively fight each other |
| **Emergent** | ×2.0 | No template — unprecedented interaction |

## Determining Interaction Type

**Cooperative:** The incoming effect reinforces or aligns with the target's existing state. Healing an ally's biology with V-01 World Tree. Enhanced Trait applied to a matching attribute. Mind Link with a willing participant. Aligned isotope with aligned target.

**Competing:** Standard combat interaction. The effect conflicts with target's current state but isn't antithetical. Most combat falls here by default.

**Cancellation:** Antithetical expressions fight each other. Synod entropic effect against Font-mutated creature. Borderlands physical expression against Palimpsest-warped construct. The target is caught between — higher damage, higher defensive strain.

**Emergent:** No template for the interaction. Emulsion artifact exposures. Multiple strong planar expressions converging on the same target. Doubled damage but unpredictable side effects — the target has no framework for what's happening.

## Cross-Pillar Attack Calculation

When targeting a non-primary pillar:

1. Declare the effect and target pillar
2. Determine Interaction Type based on effect + target's current state
3. Calculate damage/effect using standard scaling tables
4. Multiply result by Interaction Modifier
5. Apply to target's pillar-specific HP pool and condition track

**Example:** A Unity practitioner uses Mind Link to attempt to charm a Wildpath Warden who is in partial beast form (actively Transformed).

- Effect: Mind Link (ESL 4)
- Target pillar: Mental (Warden's Mental defense)
- Interaction Type: Cancellation — the Warden's active Transform state fights the Mind Link's attempt to establish connection
- Damage multiplier: ×1.5 if successful
- The Warden takes 1.5× normal Mental effect, but the Unity practitioner also takes feedback from the Cancellation — their own Mental FP consumed at 1.5× rate for the attempt

The Interaction Type cuts both ways when it's Cancellation or Emergent. The attacker pays more too.

## Pillar Crossing in Practice

Most combat defaults to single-pillar focus for simplicity. Multi-pillar combat emerges when:

- A character's Schema produces cross-pillar attacks naturally
- An opponent's vulnerability is on a different pillar than their strength
- Environmental conditions engage non-primary pillars (a burning building deals Physical damage during a Social duel)
- Magical effects produce cross-pillar consequences (high-ESL Illusion dealing Metaphysical damage on successful saves)

The GM tracks pillar engagement as it emerges, not proactively. Most turns of combat will be single-pillar. Cross-pillar moments are when the system produces its most interesting outcomes.

---

# PART IV: MULTI-SCOPE PLAY

## Core Principle

Characters operate at multiple Scopes simultaneously, but each Scope has its own temporal resolution and its own threshold of relevance. An event that interrupts a character at S0 doesn't necessarily interrupt their S7 operations. The threshold of relevance determines whether an interrupt propagates upward.

This mechanic emerges from the nested clock architecture. You don't need special multi-Scope rules — the Scope system itself handles it.

## Independent Tempo Pools Per Scope

A character has Wits + Mastery tempo at every Scope level simultaneously. Most Scopes are idle most of the time — the character isn't actively engaged at S4 or S7 during a normal combat encounter.

When a character activates at a Scope (by engaging with that Scope's activity), their tempo pool for that Scope comes online. A general who starts reading an operational report activates their S3 tempo. A character who starts a campaign-level negotiation activates their S5 tempo. The tempo at each Scope is independent — spending tempo at S0 doesn't deplete tempo at S4.

**This is the mechanical reason higher-Scope figures can operate across multiple scales without burning out from "insufficient tempo."** They have tempo budgets at every Scope, activated by context, consumed by context.

## The Threshold of Relevance

When an event occurs at a lower Scope while a character is actively operating at a higher Scope, the event must pass a threshold of relevance to interrupt the higher Scope operation.

| Higher Scope Active | Lower Scope Event | Threshold to Interrupt |
|---|---|---|
| S3 (operational meeting) | S0 attack | Any direct physical threat to the character |
| S4 (strategic planning) | S1 fireteam engagement nearby | Sustained conflict exceeding 1 minute |
| S5 (campaign coordination) | S2 engagement at command post | Breach of security perimeter |
| S6 (regional strategy) | S3 operational setback | Failure cascading to campaign implications |
| S7 (institutional reorientation) | S4 battlefield loss | Casualties exceeding institutional tolerance |

Lower-scale events that fall below the threshold are handled at the appropriate Scope without interrupting higher operations. The general who is attacked by one assassin deals with it at S0 (spending S0 tempo on the fight) while their S7 operations continue uninterrupted. The general whose command post is overrun by enemy forces has their S7 operations interrupted because the event has crossed the relevance threshold.

## Interrupt Procedure

When an event crosses the relevance threshold:

1. The higher-Scope tempo is paused at its current position
2. The character shifts primary attention to the interrupting Scope
3. The interrupting event resolves at its own Scope's tempo pace
4. Once resolved, the character returns to the higher-Scope tempo where it paused
5. Time elapsed during the interrupt counts against the higher-Scope clock at its temporal resolution

**Example:** General Vasik is 4 tempos into an 8-tempo S7 phrase (weeks of institutional reorientation). An assassin attacks him at S0. The S0 event is clearly above threshold (direct physical threat).

- S7 tempo pauses at 4/8 used
- Vasik shifts to S0 — his Wits + Mastery = 9 S0 tempos come online
- The fight resolves in 30 seconds of real time (6 S0 tempos consumed)
- Vasik returns to S7 — the pause cost approximately zero S7 tempo because 30 seconds is immaterial at monthly resolution
- Vasik continues his S7 reorientation with 4/8 tempos still available

The assassination attempt mattered at S0. It barely registered at S7. This is correct system behavior.

## Cascade Interrupts

A single event may cross threshold at multiple Scopes simultaneously:

**Example:** A provincial governor is publicly assassinated.

- S0 event: the killing itself (seconds)
- S1 event: the security detail's response (minutes)
- S2 event: local authority response (tens of minutes)
- S3 event: regional investigation launches (hours to days)
- S5 event: political implications ripple through the province (days to weeks)
- S7 event: institutional succession crisis (weeks to months)

The governor's actual killer resolves S0 combat. The security detail resolves S1. The investigators resolve S2-S3. The political implications play out at S5-S7. All of these are happening simultaneously at their own temporal resolutions, driven by the single S0 cascade event.

This is how the nested clock architecture produces campaign-scale consequences from encounter-scale events.

## Splitting Attention Across Scopes

A character may deliberately split their active attention across Scopes — for example, fighting at S0 while commanding at S3. This is expensive:

- Both Scopes consume tempo simultaneously
- A 1-tempo transition cost applies each time the character shifts focus between Scopes within a phrase
- FP is split across the pillars serving each Scope (Physical for S0 combat, Social for S3 command)

This is the Stormpeak officer problem. The Way of the Phalanx exists specifically to minimize S0 tempo expenditure (defensive stance, low tempo cost) so that S3 command tempo remains available.

## Chronos and Multi-Scope Play

Chronos effects can modify tempo at specific Scopes. A character under ESL 5 Chronos (extra standard action per round) has enhanced S0 tempo but normal tempo at other Scopes. Chronos at ESL 7 (two full rounds per one) doubles S0 tempo while leaving higher Scopes unaffected.

This creates tactical patterns:

- Speedsters operate with Chronos-enhanced S0 tempo, but cannot command S5 campaigns any faster than unmodified characters
- Strategic planners using ESL 5 Chronos at S4 operate at doubled operational tempo — they can execute in days what competitors take weeks to complete
- The Chronosynclastic Institute's signature is precisely calibrated Chronos application at the appropriate Scope for any operation

---

# PART V: S0 ACTION ATOMS — ENCOUNTER SCALE

*(Representative examples demonstrating universal grammar application at Scope 0)*

## How to Read These Tables

Each action specifies:
- **Action name:** The combat term
- **Effect:** The universal verb from the 19+Variable list
- **BER:** Base Effect Rank (from SRD v3)
- **Typical ESL:** The level a competent practitioner produces
- **Tempo cost:** Light (1) / Standard (2) / Heavy (3)
- **FP cost:** (ESL × 2) − 1, from the relevant pillar pool
- **Geometry:** CP purchases (typically 0 CP at S0)
- **Pillar targeted:** Usually Physical at S0, but cross-pillar is available

## Physical Pillar Actions at S0

| Action | Effect | BER | Typical ESL | Tempo | FP | Geometry | Notes |
|---|---|---|---|---|---|---|---|
| Strike (light) | Damage | 1 | 1 | 1 | 1 | Individual, Touch | Basic jab, quick punch, light slash |
| Strike (standard) | Damage | 1 | 2 | 2 | 3 | Individual, Touch | Full committed blow |
| Strike (power) | Damage | 1 | 3-4 | 3 | 5-7 | Individual, Touch | Power Attack, Heavy weapon swing |
| Ranged shot | Damage | 1 | 1-3 | 1-2 | 1-5 | Individual, Close/Medium | Bow, firearm, thrown weapon |
| Channeled Strike | Damage | 1 | 2-3 | 2 | 3-5 | Individual, Touch | Strike + isotope rider |
| Parry | Protection | 2 | 2-3 | REACTION | 3-5 | Self | Interposing weapon against incoming |
| Block | Protection | 2 | 1-2 | REACTION | 1-3 | Self | Shield or armor catching attack |
| Dodge | Protection | 2 | 2-3 | REACTION | 3-5 | Self (Evasion) | Movement to avoid incoming |
| Grapple | Affliction | 1-5 | 2 | 2 | 3 | Individual, Touch | Restraint condition, Minor severity |
| Pin | Affliction | 1-5 | 3 | 3 | 5 | Individual, Touch | Immobilize, Moderate severity |
| Shove | Move Object | 2 | 2 | 2 | 3 | Individual, Touch | Forced movement of target |
| Disarm | Affliction | 1-5 | 2 | 2 | 3 | Individual, Touch | Removes weapon, Minor severity |
| Trip | Affliction | 1-5 | 2 | 2 | 3 | Individual, Touch | Prone condition |
| Intimidate (physical) | Affliction | 1-5 | 2 | 2 | 3 | Individual, Close | Minor Mental condition via Physical display |
| Move | Movement | 1 | 1-2 | 1-2 | 1-3 | Self | Walk, run, sprint, climb (land speed from ESL table) |
| Jump | Movement | 1 | 1-2 | 1 | 1-3 | Self | Leaping via Movement effect |

## Mental Pillar Actions at S0

| Action | Effect | BER | Typical ESL | Tempo | FP (Mental) | Notes |
|---|---|---|---|---|---|---|
| Observe/Analyze | Senses | 2 | 1 | 1 | 1 | Identify threats, read situation |
| Read emotion | Senses | 2 | 3 | 2 | 5 | Analytical overlay on social read |
| Resist Mental attack | Protection | 2 | 2-4 | REACTION | 3-7 | Defense against incoming Mental |
| Focus (ignore distraction) | Protection | 2 | 2 | 1 | 3 | Concentration maintenance |
| Intimidate (mental) | Affliction | 1-5 | 2-3 | 2 | 3-5 | Mental pressure, Minor/Moderate |
| Counter-argue | Nullify | 3 | 2-3 | 2 | 3-5 | Dismantle opponent's mental construct |

## Social Pillar Actions at S0

| Action | Effect | BER | Typical ESL | Tempo | FP (Social) | Notes |
|---|---|---|---|---|---|---|
| Demoralize | Affliction | 1-5 | 2-3 | 2 | 3-5 | Social pressure, affects Poise |
| Rally | Enhanced Trait | 2/3/4 | 2 | 2 | 3 | Boost ally social/mental state |
| Deception | Illusion | 2/3 | 2 | 2 | 3 | Single-sense social illusion (lying convincingly) |
| Command | Mind Link | 3 | 2-3 | 2 | 3-5 | Social compulsion via presence and authority |
| Truth-sense | Senses | 2 | 3 | 2 | 5 | Analytical read of Social truth |

## Metaphysical Pillar Actions at S0

These are Spell Sentence applications at 0 CP geometry — personal scale spellwork.

| Action | Effect | BER | Typical ESL | Tempo | FP (Metaphysical) | Notes |
|---|---|---|---|---|---|---|
| Spell bolt | Damage | 1 | 1-3 | 1-2 | 1-5 | Isotope-determined damage type |
| Shield | Protection | 2 | 2-3 | 1 | 3-5 | Self-Protection expression |
| Healing touch | Healing | 2 | 2 | 2 | 3 | Minor ally restoration |
| Detect | Senses | 2 | 2 | 1 | 3 | Magical perception enhancement |
| Counter-spell | Nullify | 3 | 3 | REACTION | 5 | Dispel targeted spell (exothermic) |
| Illusion | Illusion | 2/3 | 2 | 2 | 3 | Minor deceptive manifestation |

## S0 Geometry Examples (All 0 CP)

At Scope 0, geometry is the baseline universal grammar:

| Shape | What It Covers |
|---|---|
| Individual | Single target — a specific person or object |
| Touch/Close | Arm's reach to 25 feet |
| Instantaneous | Single moment — one tempo's duration |
| Concentration | Lasts while actively focused (1 tempo per round to maintain) |

These are free and known by every practitioner. No Grammar Points required.

---

# PART VI: S1 ACTION ATOMS — FIRETEAM SCALE

*(Scope 1: Fireteam to small unit engagement, seconds to minutes)*

## Representative Geometry Shifts

At S1, actions begin to engage multiple individuals and require higher geometry investment:

| Shape | CP | Covers |
|---|---|---|
| Burst (Small) | 0 | 10 ft + (5 ft / 2 ML) — reaches 35 ft at ML 10 |
| Cone | 1 | ~60 ft breath weapon / spray |
| Line (Area) | 2 | Beam hitting all in path |
| Spread | 2 | Cloud 10-20 ft radius, turns corners |
| Medium range | 1 | 100 ft + (10 ft / ML) |
| Minutes duration | 1 | 1 min per ML |

## Representative Physical Actions

| Action | Effect | Geometry | Typical ESL | Notes |
|---|---|---|---|---|
| Area attack (spray) | Damage | Cone (1 CP) | 2-3 | Sweeping strike, spray of thrown weapons |
| Suppressing fire | Affliction | Line Area (2 CP) | 2-3 | Pin down, Minor severity condition in the line |
| Area control | Protection | Emanation (0 CP) + Minutes (1 CP) | 3 | Persistent defensive aura for ally group |
| Fireteam coordination | Senses + Mind Link | Individual × 3-4 targets, Minutes | 3 | Linking fireteam awareness for duration |
| Tactical repositioning | Movement | Self + Medium range (1 CP) | 2-3 | Rapid relocation through threatened area |
| Difficult terrain creation | Transform | Spread (2 CP) | 3 | Modify ground conditions over small area |

## The S1 Tempo Calibration

At S1, a tempo represents seconds to a minute of coordinated action. The fireteam leader's "one tempo" is a complete observe-orient-decide-communicate-verify cycle. Faster Wits + higher Mastery = more cycles per engagement.

Communication is now a cost. At S0, you only decide for yourself. At S1, each decision must propagate to the team, which costs tempo or requires pre-established protocols (trained teamwork reducing the per-decision cost).

## Representative S1 Durations

| Duration | CP | What Fits |
|---|---|---|
| Instantaneous | 0 | A single fireteam action |
| Concentration | 0 | Sustained focus for a few exchanges |
| Minutes | 1 | A short engagement sequence |
| Hours | 2 | A sustained operational posture (bleeds into S2) |

---

# PART VII: S2 ACTION ATOMS — ENGAGEMENT SCALE

*(Scope 2: Squad to platoon engagement, minutes to tens of minutes)*

## Representative Geometry

At S2, actions engage the full engagement zone — entire squads, established positions, held territory during a fight:

| Shape | CP | Covers |
|---|---|---|
| Spread | 2 | Cloud or zone effect |
| Line (Area) | 2 | Beam across engagement |
| Wall (Standard) | 3 | 2 squares/ML barrier |
| Long range | 2 | 400 ft + (40 ft / ML) |
| Visual Sight range | 3 | Anything visible |
| Hours duration | 2 | Sustained engagement lasting |

## Representative Actions at S2

| Action | Effect | Geometry | Typical ESL | Notes |
|---|---|---|---|---|
| Barrage | Damage | Spread (2 CP) + Hours (2 CP) | 3-4 | Sustained fire over engagement zone |
| Zone denial | Affliction | Line Area (2 CP) + Minutes (1 CP) | 3 | Movement restriction across a line |
| Defensive line | Protection | Wall Standard (3 CP) + Hours (2 CP) | 3-4 | Established fortification for duration |
| Squad healing | Healing | Spread (2 CP) + Concentration (0 CP) | 3 | Sustained field medicine |
| Intelligence sweep | Senses | Visual Sight (3 CP) | 3-4 | Analytical overlay on engagement zone |
| Tactical concealment | Illusion | Spread (2 CP) + Minutes (1 CP) | 3 | Concealing squad movement or position |
| Coordinated assault | Enhanced Trait (Pillar BER 3) | Individual × squad | 4 | Boost squad capability for engagement |
| Terrain shaping | Transform | Spread (2 CP) + Hours (2 CP) | 3-4 | Reshape battlefield terrain |

## The S2 Tempo Calibration

At S2, a tempo represents minutes of coordinated squad action. The squad leader's "one tempo" encompasses reading squad reports, adjusting positions, committing reserves, coordinating with adjacent squads.

S2 is the critical transition zone. Below S2, action is direct. Above S2 (at S3+), action is mediated through institutional structures. S2 is where personal command meets organizational command.

## The Drip Recharge Anchor

S2 is where the FP drip recharge anchors (10-minute interval = 1 S2 tempo). Every S2 interval generates base recharge across all four pools. This makes S2 the natural breathing-room Scope — engagements at this scale produce recovery opportunities between actions.

## Engagement Duration Limits

Most S2 engagements resolve within a few tempos (tens of minutes to an hour). Sustained S2 engagements for hours begin cascading upward into S3 operational patterns. A prolonged S2 engagement IS an S3 operation.

---

# PART VIII: SCOPE MARGIN AND GEOMETRY ACCESS

## Encounter Scale (S0-S2) Geometry Summary

All Encounter-scale geometry is Common tier — known at character creation through Grammar Points. Every character can produce these effects with sufficient ESL and FP:

| CP | Targets | Ranges | Durations |
|---|---|---|---|
| 0 | Individual, Ray, Emanation, Burst (Small) | Touch/Self, Close | Instantaneous, Concentration |
| 1 | Cone | Medium, Line of Sight | Minutes |
| 2 | Spread, Line (Area) | Long | Hours |
| 3 | Wall (Standard) | Visual Sight | Day |

## Crossing Into Battlefield Scale (S3-S4)

Battlefield-scale geometry is Dialect tier — must be LEARNED THROUGH PLAY:

| CP | Shape/Range/Duration |
|---|---|
| 4 | Burst (Large): 100 ft + (10 ft/ML) |
| 5 | Zone: 500 ft + (50 ft/ML); Week duration |
| 6 | Wall (Fortified): 4 squares/ML, 1 inch/ML thick |

A character cannot start with Battlefield geometry. They must encounter it, study it, practice it. This constraint creates the mechanical reason why S3-S4 play is typically reserved for experienced characters.

## Geographic Scale (S5+) — Treasure Tier

Geographic geometry (CP 7-10) is Treasure tier — acquired only through exceptional circumstances:

| CP | Shape/Range/Duration |
|---|---|
| 7 | District (~1 mile radius); Unlimited same-plane range |
| 8 | Regional (~5 mile radius) |
| 9 | Territorial (~10 mile radius); Extraplanar range; Years duration |
| 10 | Vast (20 miles/ML = 200 miles at ML 10); Permanent duration |

For individual characters, the primary path to Geographic-scale effect is the Systemic Catalyst talent — leveraging natural systems to multiply reach without acquiring Treasure-tier geometry directly. For institutions, the path is aggregate FP pooling with Forge-tier communication infrastructure.

---

# PART IX: QUICK REFERENCE SUMMARY

## The Combat Loop

1. **Engagement State** — Disengaged / Threatened / Engaged
2. **Phrase Begins** — Initiator pays 1 tempo, all engaged actors activate
3. **Action Declaration** — Choose Effect + Isotope + ESL + Geometry; pay FP
4. **Resolution** — Attack check, defense check, damage/effect calculation
5. **Interaction Type Applied** — Cooperative/Competing/Cancellation/Emergent modifier
6. **Reactions Triggered** — Opponents may spend FP out of turn for appropriate reactions
7. **Consequences Applied** — HP damage, condition tracks, status effects
8. **Tempo Spent** — Light (1) / Standard (2) / Heavy (3)
9. **Phrase Continues** — Until all actors disengage, one side eliminated, or situation resolves
10. **Disengagement** — Pay exit cost; remaining actors may continue phrase

## The Resource Triangle

Three constraints govern action output per phrase:

- **Tempo Pool** (Wits + Mastery) — bandwidth ceiling
- **FP Pool** (pillar-specific formula) — fuel ceiling
- **Engagement Duration** — how long the phrase runs

Output = min(tempo available, FP fueled actions, engagement duration) at each moment.

## Scope Navigation Rules

- Every character has tempo at every Scope simultaneously
- Active Scopes consume tempo; idle Scopes do not
- Events must cross relevance threshold to propagate upward
- Splitting attention across Scopes costs 1 tempo per transition
- Chronos modifies tempo at specific Scopes, not universally

## The Four Interaction Modifiers

When effects cross pillars or planes:
- **Cooperative** ×0.25 — aligned with target state
- **Competing** ×1.0 — standard conflict (default)
- **Cancellation** ×1.5 — antithetical clash
- **Emergent** ×2.0 — unprecedented combination

## The Reaction Pattern

1. Trigger event occurs
2. Character may declare reaction (one per trigger)
3. Reaction specifies Effect + ESL (capped by Mastery)
4. FP cost: (ESL × 2) − 1 from appropriate pillar pool
5. Tempo NOT consumed (reactions are outside own phrase)
6. Nullify reactions at ESL 5+ produce exothermic collateral

---

*End of Document 2, Part II. Remaining combat engine materials (advanced reaction chains, complex multi-Scope scenarios, Systemic Catalyst combat application examples, and the complete ESL-to-observable-action atlas) continue in Part III and reference the SRD v3 scaling tables directly.*
