# THE ÆTHERIUM CODEX — UNIFIED ARCHITECTURE
## Document 1: One Engine, Different Scales, Same Dials
### Alpha Draft — April 15, 2026

---

# PART I: DESIGN PRINCIPLES

## The Core Assertion

Every system in the Ætherium Codex is an implementation of one underlying engine. Combat, social interaction, crafting, institutional operations, environmental phenomena, civilizational drift, and cosmological maintenance all use the same structural components operating at different scales. No system is an exception. No system requires its own rules. The components are:

1. **Scope** — the scale at which an action operates
2. **Pillars** — the axes along which health, damage, and consequence are tracked
3. **Petals** — the domains of trained capability that characters use to act
4. **Tempo** — the unit of action within a given Scope level
5. **Clocks** — the mechanism by which accumulated small changes produce large-scale state transitions
6. **Debt** — the universal cost model for carrying conditions, adaptations, and consequences

These six components combine to describe any interaction at any scale. A sword fight and a trade war use the same components — different content, same architecture.

## The Relationship Between Components

Scope determines WHAT you're affecting and at what temporal resolution.
Pillars determine WHICH axis of the target is being tested.
Petals determine WHAT training the actor brings to the action.
Tempo determines HOW MUCH the actor can do within a single phrase at their operating Scope.
Clocks determine HOW accumulated actions at one Scope propagate to adjacent Scopes.
Debt determines HOW conditions are carried, integrated, or failed.

No component operates in isolation. Every action involves all six simultaneously. A Wildpath Warden sealing a Reality Seam is: operating at Scope 4-5 (regional/operational), testing the Metaphysical pillar of the environment, using Philosophy and Knowledge petal talents, spending tempos on channeling actions, advancing or retarding the local ley line clock, and carrying Mental debt from the college initiation that made them capable of the work.

---

# PART II: THE SCOPE SCALE

## Definition

Scope measures two independent variables that are normally locked together but can be decoupled through infrastructure:

**Scope of Effect:** How large is the entity, area, or concept being affected? This is fixed by the target.

**Dissemination Time:** How long do effects take to propagate through the affected scope? This is variable based on communication and coordination infrastructure.

An army of 10,000 with runner communication has Scope 6 effect with Scope 6 dissemination — orders take days to propagate across the force. The same army with Forge-linked ward communication has Scope 6 effect with Scope 3 dissemination — orders arrive in minutes. The Forge infrastructure did not change what the army can affect. It changed how fast effects propagate.

## The Scale

| Scope | Temporal Resolution | Spatial/Conceptual Reach | What Operates Here |
|---|---|---|---|
| **S0** | Seconds | Personal / arm's reach | Individual exchange: sword fight, psychic duel, face-to-face negotiation |
| **S1** | Seconds to minutes | Fireteam / voice range (~30ft) | Small group coordination: covering fire, squad argument, fireteam tactics |
| **S2** | Minutes | Engagement zone (~150ft) | Skirmish, archery field, courtroom trial, item drip recharge (10-minute interval) |
| **S3** | Minutes to tens of minutes | Company / building complex | Battle command, siege section, institutional meeting, complex channeling |
| **S4** | Tens of minutes to hours | Battlefield / district | Full battle, district operation, public address, guild deployment |
| **S5** | Hours to days | Fortress / town / operation | Siege, extended operation, political crisis, faction action |
| **S6** | Days to weeks | Region / campaign | Military campaign, trade route management, faction turn |
| **S7** | Weeks to months | Territory / institution | Institutional strategy, economic policy, seasonal planning |
| **S8** | Months to years | Civilization / multi-territory | Trade wars, alliances, Zoetrope pressure, cultural shifts |
| **S9** | Years to decades | Epoch / setting-scale | Civilizational drift, Smoothing maintenance, planar boundary shifts |
| **S∞** | Cosmological | The architecture itself | Aíon-level operations, Smoothing override, regulatory system manipulation |

The scale matches the 1-10 system used by Mastery, Formation Stage, and isotope ranks. Everything in the system runs on the same spine.

## Scope and Mastery

Mastery does NOT limit which Scope levels a character can access. A Mastery 3 militia captain IS operating at Scope 3-4 when they direct troops. They're not good at it, but they're doing it.

Mastery determines how EFFECTIVELY a character operates at a given Scope — their tempo budget, their action options, their ability to manage information flow across Scope boundaries. A Mastery 3 captain issuing orders at Scope 4 is slower, less precise, and more prone to information loss than a Mastery 8 general doing the same thing.

## Scope and the Drip Recharge System

The drip recharge system's 10-minute base interval places it at Scope 2. This is not arbitrary — item charges, Stamina recovery, and short rest mechanics all operate at the engagement/skirmish temporal resolution. The recharge rate scales with item tier through the existing formula, but the BASE interval is anchored to Scope 2's temporal resolution.

| Item Tier | Tick Interval | Scope Anchor |
|---|---|---|
| 0 (Mundane) | 1 minute | S1 (fireteam) |
| 1-4 (Novice) | 10 minutes | S2 (engagement) |
| 5-7 (Journeyman) | 1 hour | S3-4 (company/battlefield) |
| 8-10 (Master) | 12-24 hours | S5-7 (operation/territorial) |

Mastery 10 is the absolute peak of mortal expression and performance. Beyond 10 enters the Legendary/Monstrous scale (attribute × 2) and the Divine scale (attribute × 10) — these are separate attribute tracks similar to Mega Attributes, not extensions of the mortal 1-10 scale.

Higher-tier items recharge at higher Scope temporal resolutions. A Novice item refills during a skirmish break. A Master item refills overnight or across a full day depending on Formation Stage.

---

# PART III: THE FOUR PILLARS

## Definition

The four pillars are the axes along which any entity's health, Moiety, and functional capacity are measured. They operate at EVERY Scope level. The content changes with scale. The diagnostic function is identical: how healthy is this entity along this axis?

## Physical (Structural Integrity [structural])

The physical composition, structural soundness, and material functionality of the entity.

| Scope | What It Tracks                                                           | Example Threats                                           |
| ----- | ------------------------------------------------------------------------ | --------------------------------------------------------- |
| S0    | Body: bones, organs, blood, tissue                                       | Sword wound, blunt force, burns, falling                  |
| S1    | Squad effectiveness: casualties, exhaustion, ammunition                  | Ambush, suppressive fire, booby traps                     |
| S2    | Engagement infrastructure: fortifications, equipment, positions          | Siege engines, sappers, engineering operations            |
| S3-4  | Operational infrastructure: supply depots, roads, facilities             | Sabotage, targeted destruction, logistics disruption      |
| S5-6  | Regional infrastructure: trade routes, production, agriculture           | Blockade, sanctions, scorched earth                       |
| S7-8  | Civilizational infrastructure: cities, industry, transportation networks | Strategic bombing, territorial conquest, economic warfare |
| S9+   | Setting-scale physical integrity [structural]                            | Planar boundary rupture, cosmological structural failure  |

## Metaphysical (Elemental/Chemical/Biological Integrity [structural])

The isotope composition, planar coherence, and fundamental chemical-biological health of the entity. This is NOT limited to "magic." It encompasses the full spectrum of the five alchemy layers: inorganic chemistry (Borderlands), organic chemistry and biology (Verdant Font), thermodynamics and entropy (Synod), catalysis and process chemistry (Hidden Forge), and statistical mechanics and probability (Palimpsest).

Agent Orange is a Metaphysical attack — Borderlands + Verdant Font compound isotope weaponized at Scope 7-8, poisoning the chemical and biological substrate of an entire territory for generations.

| Scope | What It Tracks                                                                                                                  | Example Threats                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| S0    | Personal biochemistry: Strain, poison, disease, radiation                                                                       | Toxic exposure, disease vector, isotope contamination                         |
| S1    | Local environmental quality: water, air, soil, ambient isotope levels                                                           | Localized contamination, bleed zone expansion                                 |
| S2    | Engagement-zone hazards: ward stability, tactical isotope use                                                                   | Ward sabotage, chemical weapon deployment                                     |
| S3-4  | Operational magical infrastructure: communication networks, ritual sites, Kan-tech systems                                      | Infrastructure disruption, communication ward collapse                        |
| S5-6  | Regional elemental health: ley line stability, agricultural soil quality, water table purity                                    | Resource extraction damage, ley line destabilization, industrial pollution    |
| S7-8  | Civilizational elemental health: territorial isotope balance, genetic health of populations, Smoothing Effect regional strength | Weaponized isotope contamination, genetic damage, territorial planar collapse |
| S9+   | Cosmological coherence: the Smoothing Effect, planar boundary integrity [structural]                                            | Reality Seam catastrophe, Coherence Clock failure                             |

## Mental (Identity Coherence)

The psychological integrity [structural], cognitive function, and identity coherence of the entity. At personal Scope, this is the individual's composure, conviction, and sense of self. At institutional Scope, this is the organization's ideological alignment and internal trust. At civilizational Scope, this is cultural identity and collective will.

| Scope | What It Tracks | Example Threats |
|---|---|---|
| S0 | Personal composure: will, conviction, courage, self-control | Intimidation, psychic assault, traumatic experience, belief failure |
| S1 | Squad morale: unit cohesion, trust, willingness to fight | Casualties, leadership loss, betrayal within unit |
| S2 | Force morale: operational belief that victory is possible | Heavy losses, failed operations, propaganda targeting troops |
| S3-4 | Institutional ideology: organizational belief in mission and methods | Internal schism, revealed hypocrisy, infiltration |
| S5-6 | Regional identity: community sense of shared purpose | Cultural displacement, imposed ideology, institutional collapse |
| S7-8 | Civilizational identity: cultural will to exist as coherent entity | Cultural genocide, forced assimilation, narrative replacement |
| S9+ | Cosmological narrative coherence: the Great Lie's stability | Mass Cognitive Dissonance, exposure of the Great Truth at population scale |

## Social (Legitimacy / Standing)

The reputation, credibility, and relational standing of the entity within its social context. At personal Scope, this is face-to-face credibility. At institutional Scope, this is political standing and alliance reliability. At civilizational Scope, this is sovereignty and international legitimacy.

| Scope | What It Tracks | Example Threats |
|---|---|---|
| S0 | Personal credibility: Poise, composure under social pressure | Accusation, exposure, insult, evidence of wrongdoing |
| S1 | Local standing: group trust, authority within immediate community | Public accusation, witnessed failure, gossip |
| S2 | Operational credibility: reputation among those you interact with | Atrocities, broken promises, collateral damage |
| S3-4 | Institutional standing: political influence, alliance reliability | Broken agreements, diplomatic scandals, revealed operations |
| S5-6 | Regional legitimacy: authority recognized across a territory | Failed governance, popular uprising, rival claimant |
| S7-8 | Civilizational legitimacy: right to exist as a sovereign entity | War of aggression, humanitarian violations, state failure |
| S9+ | Cosmological legitimacy: divine mandate, positional divinity | Loss of divine portfolio, Zoetrope transition, theological crisis |

---

# PART IV: THE FOUR PETALS

## Definition

The four petals are domains of trained capability. Each petal has a system it modifies — a mechanical engine that the petal's talents operate on. The petals describe WHAT YOU TRAINED IN. The pillars describe WHAT YOU'RE AFFECTING. Any petal can target any pillar. There are no restrictions on petal-to-pillar crossing.

| Petal | What It Governs | System It Modifies | Infrastructure It Uses |
|---|---|---|---|
| **Combat** | How you fight, physically and tactically | Physical combat engine (tempo, engagement states, action atoms) | Weapons, armor, physical condition tracks |
| **Knowledge** | What you know, analyze, and create | Crafting/analysis engine (item creation, schematics, material science) | Materials, tools, schematics, item architecture |
| **Philosophy** | How you channel metaphysical force | Spell Sentence system (isotopes, effects, Construction Pool, ÆP) | Isotope ranks, effect tiers, ÆP pool, Mastery Capacity |
| **Social** | How you interact with people and institutions | Background system (Poise, Clout, Rank, Title, Standing Track) | Backgrounds, contacts, reputation, institutional position |

## Free Crossing

Petals are actions. Pillars are defenses. They cross freely.

A Combat petal talent can target any pillar:
- Combat → Physical: a Power Strike targeting Guard
- Combat → Mental: an Intimidation check mid-combat targeting Courage
- Combat → Social: a dramatic victory affecting the enemy commander's Standing
- Combat → Metaphysical: a weapon strike disrupting an opponent's isotope expression

A Social petal talent can target any pillar:
- Social → Social: a diplomatic argument targeting Dignity
- Social → Mental: a psychological manipulation targeting Conviction
- Social → Physical: a Commander ordering a charge (Social talent producing Physical consequence through institutional authority)
- Social → Metaphysical: a political decision to contaminate a region's water supply (Social action producing Metaphysical consequence)

The petal determines the actor's training and approach. The pillar determines which of the target's defenses responds. The Scope determines the scale and temporal resolution.

---

# PART V: THE UNIVERSAL DEBT MODEL

## The Core Mechanism

Every lasting condition — physical injury, psychological transformation, isotope mutation, social disgrace — is tracked through a single universal debt system. The architecture is identical across all four pillars. The content differs. The thresholds, zones, repayment mechanics, and failure states are the same.

## The Thresholds

The thresholds are calculated from the character's **total lifetime XP** — including the equivalent XP value of creation choices (starting dots, backgrounds, Heritage States, etc.).

| Zone | Debt Range | Status | Consequences |
|---|---|---|---|
| **Safe** | Debt ≤ Lifetime XP × 2 | Clean integration | Benefits/adaptation only. No penalties. The condition exists but doesn't impair. The character has grown around it. |
| **Stressed** | Debt > Lifetime XP × 2, ≤ Lifetime XP × 8 | Strained integration | Detriments manifest alongside benefits/adaptations. The character is carrying more than their development cleanly supports. Triggers fire. Reactions manifest. But the person is present and processing. |
| **Overwhelmed** | Debt > Lifetime XP × 8 | Irrecoverable failure | The pillar is in catastrophic failure. Normal integration cannot recover this. Requires REMAKING, not repairing. |

## The Origin of ×2 and ×8

**The ×2 threshold** derives from Adaptation Pressure = Source Formation Stage × 2. It is the baseline calculation for how much pressure a single exposure event creates. Below ×2, the character's total development can absorb the condition without distortion — the adaptation is proportionally small relative to who they are.

**The ×8 threshold** is 4× the Safe threshold. The Stressed zone between ×2 and ×8 is the working zone — the character is struggling with detriments but remains present, functional, and capable of growth. Past ×8, the process has consumed the pilot.

## Automatic Repayment

When any pillar's debt exceeds the ×2 Safe threshold:

**25% of all XP gained is automatically deducted and applied to that pillar's debt.** The character's growth is being consumed by integration pressure. This is not optional — the body, mind, social context, or metaphysical composition is directing resources toward integrating the change.

**If multiple pillars are in debt simultaneously,** each draws its 25% independently. A character Stressed on both Physical and Mental has 50% of incoming XP consumed by auto-repayment. This creates meaningful pressure to manage debt across pillars rather than accumulating conditions freely.

**Minimum floor:** There is a guaranteed minimum XP the player receives per session regardless of total debt across all pillars. The player always has some agency over their character's development. Adaptation pressure cannot consume everything. The pilot always gets fuel.

## Natural Threshold Growth

Because the thresholds are based on **current lifetime XP**, simply gaining XP over time moves the ×2 and ×8 lines upward. A condition that pushed you into the Stressed zone at Mastery 3 might fall into the Safe zone by Mastery 5 — not because you paid anything toward it, but because your total development grew enough that the condition is proportionally smaller relative to who you are now.

**You grew around it.** The fire adaptation that was destabilizing at Mastery 3 is just part of you at Mastery 6. The trauma that was overwhelming at Mastery 4 is integrated background at Mastery 7. The social disgrace that consumed your identity at Mastery 3 is an old scar at Mastery 8.

This means time and experience are themselves healing mechanisms. Not because the condition changed, but because the PERSON grew.

## Voluntary Investment

A character can voluntarily invest XP into any pillar's debt at any time. This accelerates integration beyond the 25% automatic deduction.

## Detriments

Each detriment that manifests in the Stressed zone has its own XP cost. Detriments are tracked separately in the debt ledger.

**Paying off a detriment ELIMINATES it.** Unlike the condition itself (which stays when paid), the negative expression disappears when its debt is cleared. You outgrew the problem.

The person who "no longer flinches" has paid off the detriment of their trauma. The trauma is still THERE — the experience is part of them, the scar exists. But the flinch — the involuntary reaction, the avoidance behavior, the triggered response — is gone because they invested the growth required to overcome it. The momentary flicker of recognition still fires. The reaction that follows is managed so smoothly it never reaches the surface.

Detriments can be bought down independently. A character might choose to pay off a specific detriment first (eliminating the most disruptive penalty) while still carrying debt on the condition overall.

## Calcification (Integration Complete)

When all debt on a specific condition is cleared — both the condition and all its detriments — the condition **Calcifies.** The Heritage State shifts from Active to Settled.

The condition is permanent baseline. It costs nothing ongoing. It's just what you are. You don't maintain it. You don't pay for it. It's integrated.

**Calcification does NOT remove the condition.** The power, adaptation, or scar stays. The obligation goes. The Wildpath Warden's biological adaptations are permanent. The SERE graduate's stress inoculation is permanent. The social Title's settled connotation is permanent. The isotope mutation is permanent. These are who you ARE, not what happened TO you.

## Irrecoverable Failure (>×8)

Past the ×8 threshold, normal integration cannot recover the pillar. The condition has exceeded the character's capacity to grow around it. The process consumed the pilot.

| Pillar | What >×8 Looks Like | What Remaking Requires |
|---|---|---|
| **Physical** | Accumulated structural damage exceeding integration capacity. The body is failing systemically. | Full biological reconstruction: Panacea ESL 9-10. Not healing — REBUILDING from the body's pattern. The body that emerges is not the body that went in. |
| **Mental** | Identity coherence gone. Functioning without presence. The college failure states: clinical machine without empathy, cognitive engine without a pilot, ecosystem without direction. | Identity reconstruction. Not therapy — BUILDING a new self from whatever fragments remain. The person that emerges is not the person that went in. This is cognitive resurrection. |
| **Social** | Total social death. Vilified at a scale that normal social effort cannot reach. No community will accept the entity as it currently exists. | New identity (Constructed Identity), institutional rehabilitation at college scale, or relocation to a community where the damage hasn't propagated. The old social self is dead. A new one must be built. |
| **Metaphysical** | Monstrous transformation. Mutations expressing uncontrollably. The body has become something inhuman. The biological engine without a pilot. | Alchemical reconstruction: Decomposition + Displacement of overwhelming mutations. Strip the expressions and rebuild from substrate. The creature that emerges is not what went in. |

All four follow the same principle: past ×8, you cannot FIX it. You REMAKE it. And the remade version is not the original restored. It is something new built from what survived.

## Applied to Each Pillar — Content Summary

**Physical Debt:**
Conditions: Lasting injuries (Scarred through Terminal). Debt is the structural damage's integration cost. Detriments: functional limitations, pain, reduced capability in specific contexts. Calcification: the injury is permanent but fully adapted to. The blind swordsman. The one-armed smith. The person who no longer flinches from the old wound.

**Mental Debt:**
Conditions: Psychological transformations (trauma, college initiation, Cognitive Dissonance, belief failure). Debt is the identity integration cost. Detriments: triggers, avoidance behaviors, Schema distortion, reduced function in contexts related to the source. Calcification: the experience is permanent but fully integrated. The SERE graduate. The Wildpath diamond identity. The person who carries the weight and still tastes the coffee.

**Social Debt:**
Conditions: Standing damage (reputation destruction, institutional disgrace, Title mutation). Debt is the social recovery cost. Detriments: closed doors, withheld trust, denied opportunities, mutated Titles. Calcification: the reputation is settled — whether redeemed or accepted in its mutated form. The Title stabilizes.

**Metaphysical Debt:**
Conditions: Isotope mutations (Strain → Nascent → Calcification pipeline). Debt is the adaptation cost. Detriments: negative expressions of the same isotope (vulnerability, uncontrolled expression, biological side effects). Calcification: the mutation is permanent baseline. Heritage State shifts to Settled. Just what you are.

---

# PART VI: SCENE-LEVEL CONDITION TRACKS

## Definition

Each pillar has a 5-step condition track that represents moment-to-moment degradation DURING an encounter. Scene-level conditions recover with rest. They are NOT the lasting track — they are the immediate combat consequences that the lasting track's debt system sits behind.

## Trigger

A character moves one step down the relevant track when a single hit's post-Soak damage exceeds the **Damage Threshold** for that pillar.

**Damage Threshold = (Primary Attribute + Mastery) × 2**

| Pillar       | Primary Attribute | Threshold Formula         |
| ------------ | ----------------- | ------------------------- |
| Physical     | Vigor             | (Vigor + Mastery) × 2     |
| Mental       | Wits              | (Wits + Mastery) × 2      |
| Social       | Composure         | (Composure + Mastery) × 2 |
| Metaphysical | Moiety            | (Moiety + Mastery) × 2    |

## The Four Tracks

### Physical Scene Track

| Step | Name | Mechanical Effect |
|---|---|---|
| 0 | Unharmed | No effect |
| −1 | Winded | −1 to physical checks |
| −2 | Reeling | −2 to physical checks, −10ft movement |
| −3 | Wounded | −5 to physical checks, −20ft movement |
| −4 | Crippled | −10 to physical checks, movement halved |
| −5 | Incapacitated | Cannot act. Unconscious or helpless. |

### Mental Scene Track

| Step | Name | Mechanical Effect |
|---|---|---|
| 0 | Composed | No effect |
| −1 | Distracted | −1 to mental checks |
| −2 | Shaken | −2 to mental checks, disadvantage on Initiative |
| −3 | Frightened | −5 to mental checks, aggressive actions require Courage check TN 15 |
| −4 | Befuddled | −10 to mental checks, Confused behavior |
| −5 | Incapacitated | Catatonic. Cannot act or respond. |

### Social Scene Track

| Step | Name | Mechanical Effect |
|---|---|---|
| 0 | Poised | No effect |
| −1 | Flustered | −1 to social checks |
| −2 | Humbled | −2 to social checks, disadvantage on Presence checks |
| −3 | Disgraced | −5 to social checks, lose active status/reputation benefits |
| −4 | Rapt | −10 to ALL checks, Flat-Footed (social defenses compromised) |
| −5 | Incapacitated | Broken. Flee, surrender, or comply. Cannot resist. |

### Metaphysical Scene Track

| Step | Name | Mechanical Effect |
|---|---|---|
| 0 | Stable | No effect |
| −1 | Frayed | −1 to metaphysical checks |
| −2 | Strained | −2 to metaphysical checks |
| −3 | Corrupted | −5 to metaphysical checks, cosmetic mutation manifests |
| −4 | Unraveling | −10 to metaphysical checks, Staggered |
| −5 | Incapacitated | Metaphysical collapse. Pattern destabilizing. |

## Recovery

| Method | Effect |
|---|---|
| Short rest (10 minutes of safety, Scope 2 interval) | Move one step up on any ONE track |
| Full rest (8 hours) | Reset ALL tracks to Step 0 |

## Scene Track to Lasting Track Transition

Reaching specific scene track steps may trigger entry onto the lasting debt ledger. This is NOT automatic — it depends on the nature and source of the damage. A sword wound that reaches Wounded (Step −3) MAY create a lasting Physical debt entry. A momentary fright that reaches Frightened (Step −3) MAY NOT create a lasting Mental debt entry if the source was transient.

The determining factor is whether the event produced STRUCTURAL change (Physical: tissue/bone damage beyond surface), PERCEPTUAL change (Mental: belief challenged, identity altered, Schema pressure point activated), STANDING change (Social: public witnesses, institutional consequences), or COMPOSITIONAL change (Metaphysical: isotope Strain exceeding threshold).

The Spell Sentence's ESL calibration provides the severity benchmark for lasting entries. An effect equivalent to ESL 3+ is sufficient to create a lasting debt entry. Below ESL 3, the damage is scene-level only.

---

# PART VII: DEFENSE ARCHITECTURE

## Structure

Each pillar has four defenses that parallel each other functionally. The defense names reflect their pillar's vocabulary. The mechanical function is identical across pillars.

| Function | Physical | Mental | Social | Metaphysical |
|---|---|---|---|---|
| **Evade** (avoid entirely) | Evasion | Willpower | Grace | Acuity |
| **Deflect** (redirect/block) | Guard | Control | Dignity | Integrity |
| **Absorb** (reduce damage) | Toughness | Conviction | Composure | Resilience |
| **Resist** (internal/systemic) | Vigor | Courage | Discretion | Essence |

## Defense Derivation Formulas

### Physical Defenses

| Defense | Formula | Defends Against |
|---|---|---|
| **Evasion** | 10 + Finesse mod + Mastery bonus + [Mobility tag talent count] | Ranged attacks, area effects |
| **Guard** | 10 + Finesse mod + Mastery bonus + [Weapon Style tag talent count] | Melee attacks, combat maneuvers |
| **Toughness** | Might mod + Armor bonus + [Durability tag talent count] | Damage reduction (Soak). Subtracted from incoming Physical damage. |
| **Vigor** | 10 + Vigor attribute mod + Mastery bonus | Poison, disease, exhaustion, internal physical threats |

### Mental Defenses

| Defense | Formula | Defends Against |
|---|---|---|
| **Willpower** | 10 + Acuity mod + Dominion mod + Mastery/2 | Direct psychic intrusion, mind reading, telepathic probes |
| **Control** | 10 + Intellect mod + Composure mod + Mastery/2 | Emotional manipulation, compelled rage/panic, overwhelming impulses |
| **Conviction** | Wits mod + Mastery/2 + talent bonuses | Identity challenges, forced moral violations, belief testing. Functions as Mental Soak. |
| **Courage** | 10 + Courage attribute equivalent + Mastery bonus | Fear, terror, intimidation, existential dread |

### Social Defenses

| Defense | Formula | Defends Against |
|---|---|---|
| **Grace** | 10 + Guile mod + Wits mod + Mastery/2 | Verbal traps, public embarrassment, being pinned in argument |
| **Dignity** | 10 + Presence mod + Intellect mod + Mastery/2 | Direct accusation, confrontation, challenges to authority |
| **Composure** | (Composure attr + Mastery)/2 + Title/Status bonuses | Social damage absorption. Functions as Social Soak. |
| **Discretion** | 10 + Composure attr mod + Mastery bonus | Persistent rumors, smear campaigns, blackmail, long-term reputation poisoning |

### Metaphysical Defenses

| Defense        | Formula                                           | Defends Against                                                      |
| -------------- | ------------------------------------------------- | -------------------------------------------------------------------- |
| **Acuity**     | 10 + Essence mod + Acuity mod + Mastery/2         | Incoming planar effects, ambient isotope exposure, magical targeting |
| **Integrity**  | 10 + Integrity attr mod + Vigor mod + Mastery/2   | Identity-altering metaphysical effects, Schema overwrite, possession |
| **Resilience** | (Integrity attr + Mastery)/2 + Faith/Pact bonuses | Metaphysical damage absorption. Functions as Metaphysical Soak.      |
| **Essence**    | 10 + Essence attr mod + Mastery bonus             | Internal corruption, isotope contamination, planar identity drift    |

*Note: The attribute previously called "Anima" has been renamed to **Essence** to avoid collision with Anima the god. Essence is the Metaphysical attribute governing raw planar connection and internal coherence. It feeds into Acuity (Metaphysical Evade), Essence defense (Metaphysical Resist), and the Pattern pool formula.*

*Note: Specific attribute mappings are subject to final attribute list confirmation in the Character Creation document. The structural parallel (four defenses per pillar, consistent function) is locked. Specific derivation formulas are calibration targets.*

---

# PART VIII: RESOURCE POOLS

## HP Pools (One Per Pillar)

Each pool is a buffer of points that absorb damage before the character moves down the scene-level condition track. When the pool reaches 0, subsequent damage drives the character down the track directly.

| Pool | Name | Formula |
|---|---|---|
| Physical | **Vitality** | (Vigor × 3) + (Might × 3) + (Mastery × 5) |
| Mental | **Resolve** | (Wits × 3) + (Intellect × 3) + (Mastery × 5) |
| Social | **Poise** | (Presence × 3) + (Composure × 3) + (Mastery × 5) |
| Metaphysical | **Pattern** | (Integrity × 3) + (Essence × 3) + (Mastery × 5) |

All four pools follow the same formula structure: (Primary Attribute × 3) + (Secondary Attribute × 3) + (Mastery × 5).

## Operational Pools

| Pool | Name | Formula | Function |
|---|---|---|---|
| Physical fuel | **Stamina** | (Vigor + Mastery) × 2 | Fuels physical talents, push turns, special actions. Recovers at Scope 2 intervals (10 min). Does NOT recover during combat without specific talent investment. |
| Metaphysical fuel | **ÆP (Æther Points)** | (Dominion + Tₘ) × Mastery | Fuels all Spell Sentence expressions. Tₘ = total Magical + Supernatural talents. Recovers with full rest. |
| Sustained expression capacity | **Mastery Capacity Pool** | Base: OMT × 4. Max: OMT × 34 (with Expanded Consciousness talent investment) | Tracks how many simultaneous sustained metaphysical effects the character can maintain. |

---

# PART IX: THE FULCRUM POINT ECONOMY

## Generation

Fulcrum Points are generated by internal complexity. The more contradictory the entity's Psyche Schema, the more narrative energy it produces.

**FP per session = (count of outlier scores) + (count of asymmetric splits) + (count of pattern breaks)**

This is the same pressure point count produced by the Schema extraction procedure at Vertebra 2 of the Operating Philosophy. Character depth IS mechanical power.

| Entity Type | Typical FP Range |
|---|---|
| Player Characters | 4-8 FP |
| Minor NPCs | 1-2 FP (flat, do not track) |
| Notable NPCs | 4-8 FP (from personal Schema) |
| Major NPCs | 8-15+ FP (personal + positional + institutional pools) |
| Institutions | Generated from institutional Schema tensions |
| Territories | Generated from territorial complexity (high-FP territories produce more unpredictable events) |

## Cost Table (10-Point Scope Scale)

| S0 | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S∞ |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 7 | 9 | 15 |

FP cost represents the narrative energy required to reach across Scope boundaries. Low-Scope spends (S0-2 at 1 FP each) are cheap and frequent — personal-scale observation collapses. High-Scope spends (S7+ at 5-9 FP) are expensive and rare — institutional or civilizational-scale interventions.

S∞ at 15 FP requires either an extremely complex Schema (15+ pressure points) or institutional FP pooling from a major organization.

## Institutional Pooling

Individual characters cannot normally reach S7+ alone. Institutions can — by pooling FP from multiple actors through communication infrastructure.

| Infrastructure Level | Pooling Capacity | Scope Reach | Analog |
|---|---|---|---|
| None | No pooling | Individual Scope only | Lone operative |
| Basic (voice, runners) | Up to 3 actors' FP, co-located | +1-2 Scope | Squad with a sergeant |
| Standard (institutional comms) | Up to 10 actors' FP, same region | +2-3 Scope | Company with signal corps |
| Advanced (Forge ward networks) | Up to 50 actors' FP, multi-region | +3-4 Scope | College with communication infrastructure |
| Exceptional (Palimpsest links) | Unlimited pooling, cross-territorial | +5+ Scope | Aíon's continuous maintenance |

Communication infrastructure is a strategic asset because it determines the maximum Scope at which an institution can concentrate narrative energy. The Forge doesn't just make items. It makes institutions capable of operating at higher Scope levels.

## Recovery

FP refreshes each session (the Schema's internal tensions continuously produce narrative energy).

Mid-session recovery is generated mechanically through Schema × situation intersection:

**Procedure:** The Psyche Schema's pressure points are tagged by dimension. Adventure situations are tagged by which dimensions they test. When a tagged situation activates and a character whose pressure points include that dimension ENGAGES with it (makes a choice, takes an action, accepts a consequence), they generate 1 FP. The engagement is binary (engaged or avoided), not qualitative.

This is a mechanical comparison, not a GM judgment call. The pressure points are pre-identified. The situations are pre-tagged. The intersection is a lookup operation. Implementation details are specified in the Adventure Generator coupling document (future build).

## Destiny Points

Destiny Points are a SEPARATE treasure currency from FP. They are not generated by the Schema. They are awarded by the GM for campaign-defining moments — the dramatic peaks where player agency and GM agency converge into something neither planned.

Destiny Points are NOT spent through the Scope cost table. They have their own spend mechanics (to be defined in the combat engine document). They represent the BIG moments, not the continuous narrative energy that FP provides.

---

# PART X: CASCADE MECHANICS

## Definition

Events at one Scope level propagate to adjacent Scope levels. Downward cascade (higher Scope affecting lower) carries LATENCY. Upward cascade (lower Scope affecting higher) carries INFORMATION LOSS.

## Downward Cascade (High Scope → Low Scope)

When a higher-Scope action produces effects at a lower Scope, those effects arrive with a delay measured in lower-Scope phrases. The delay is determined by the communication infrastructure connecting the two Scope levels.

**Example:** A Scope 4 order (battlefield command) propagates to Scope 0 (individual soldiers). Without infrastructure enhancement, the order takes approximately 5-10 Scope 0 phrases (exchanges) to reach the front line. During that time, the soldiers act on PREVIOUS orders. With Forge-linked communication, the same order arrives in 1-2 Scope 0 phrases.

Talents and resources that reduce cascade latency are strategically valuable. Telepathic links, ward communication networks, trained signal corps — these compress the gap between decision and execution across Scope boundaries.

## Upward Cascade (Low Scope → High Scope)

When lower-Scope events accumulate, they eventually tick a higher-Scope clock. The number of lower-Scope ticks required to advance a higher-Scope clock is determined by the situation.

**Example:** Individual tactical victories (Scope 0-1) accumulate to affect operational morale (Scope 3-4). But the information flowing upward DEGRADES — the general doesn't know exactly what happened at every Scope 0 exchange. They receive reports, summaries, assessments — each stage of upward transmission strips detail and introduces interpretation.

The information that reaches the higher Scope is a COMPRESSED version of what happened at the lower Scope. Critical details may be lost. The general's picture of the battle is always slightly behind and slightly simplified compared to reality.

Talents and resources that improve upward information flow are equally valuable. Scrying, familiar networks, trained scouts, institutional reporting chains — these reduce the information degradation across Scope boundaries.

## Bidirectional FP Spending

Fulcrum Points can be spent in EITHER direction across Scope boundaries (already defined in the Operating Philosophy). A Scope 0 character can spend FP to affect Scope 3 (reaching UP — a soldier's personal action has operational consequences). A Scope 4 character can spend FP to affect Scope 0 (reaching DOWN — a general intervenes in a specific tactical moment).

The FP cost is the same regardless of direction. The SIDE EFFECTS differ:
- Reaching UP: the deferred consequences involve Scope levels the character doesn't normally perceive. They may not know what their action triggered.
- Reaching DOWN: the deferred consequences involve attention drawn away from the character's operating Scope. The general who micro-manages one fight loses awareness of the broader battle.

---

# PART XI: THE ZOETROPE CONNECTION

## Three Distribution Functions

The Political Zoetrope serves as the setting's talent, mutation, and training distribution map. Each of the 16 Zoetrope positions (plus buffer zones) determines three things for characters originating from that position:

### Territorial Planar → Mutations (What the Land Does to You)

The territorial isotope expression determines which Heritage States develop in the local population through the Strain → Nascent → Calcification → Heritage State pipeline. This is involuntary. The land shapes organisms whether they want it or not.

Stormpeak (Position 12, B-OMNI): Population develops Borderlands adaptations — heat resistance, electrical tolerance, geological bone density.

Wildpath (Position 10, V-OMNI primary): Population develops Verdant Font adaptations — biological communion, accelerated healing, ecological sensitivity.

### Institutional Planar → Magical Talents (What the College Teaches You)

The institutional planar expression determines which Philosophy petal talents are available for training. This is voluntary — the character apprentices to an institution and learns their methods.

Deepguard (F-13 Spire): Teaches Abjuration methodology — Nullify-focused, Protection-focused talents.

Chronosynclastic (P-01 Oracle): Teaches Divination methodology — Detect-focused, predictive talents.

### Governance + Economics + Ethos → Mundane Talents and Backgrounds (What Society Trains You For)

The political alloy determines which Combat, Knowledge, and Social petal talents the civilization invests in.

Stormpeak (Stratocracy + Capability Export + Agonism): Full military talent access. Limited social and crafting access.

Sovereign Exchange (Corporatocracy + Platform Arbitrage + Exchange): Full mercantile and social talent access. Limited military access.

## Character Origin as Talent Access

A character's Zoetrope origin determines their starting talent ACCESS — which talents were available for training, which Heritage States they carry, and which institutional magical traditions they could learn. Migration, multi-college training, and personal development expand access beyond origin, but the origin establishes the baseline.

---

# PART XII: SYSTEM CROSS-REFERENCE MAP

## How Each Existing Document Implements the Architecture

| Document | Architecture Region | What It Defines |
|---|---|---|
| **Operating Philosophy** | The spine itself | Seven vertebrae, FP system, clocks, fronts, feedback loop, campfire principle. The meta-structure that this document systematizes. |
| **SRD v2 Prima Materia** | Metaphysical pillar mechanics | Isotopes, dual periodic table, Formation Stage, item creation, housing architecture, Legacy/Ascension. The Metaphysical debt system (Strain → Calcification) is defined here. |
| **Book of Shadows** | Philosophy petal system | Spell Sentence grammar, Construction Pool, ÆP formula, Metamagic/Focus talents, Architect/Improviser philosophies. |
| **Character Creation v3** | Starting state specification | Attributes, skills, derived stats, starting XP (120), talent costs, Heritage States at creation. |
| **Political Zoetrope v2** | Scope 7-9 civilizational mechanics | The alloy system, 16-position lifecycle clock, governance/economics/ethos/planar source. Also serves as talent/mutation/training distribution map. |
| **Elemental Cards** | Metaphysical pillar content library | 104+ isotope combination cards with physical character, emission, and material use. Applies to biological substrates for ancestry generation, not just crafted items. |
| **Companion System docs** | Companion mechanics | Acquisition paths, creature types, bonding. Creature traits generated through the same Punnett square system as racial Heritage States. |
| **College Initiations** | Mental lasting track content | Each initiation is a deliberate Mental debt event. Persistent tests are the ongoing integration work. Failure states define the >×8 Overwhelmed outcome per college. |
| **World Bible (Turbulent/Laminar)** | Environmental weather system | Ley line states, Reality Seams, planar bleed zones, the Three Fronts, the Cold War structure. These become Scope 5-9 clocks and fronts within the Operating Philosophy's spine. |
| **Psyche Schema** | FP generation engine, Mental pillar diagnostic | Pressure point identification, Schema dimensions, FP generation formula. The diagnostic instrument that the Mental lasting track operates through. |

## Documents That Need To Be Written (This Architecture's Downstream)

| Document | What It Defines | Dependencies |
|---|---|---|
| **Document 2: Combat Engine** | Tempo model, action atoms per Scope level, engagement states, Stamina integration, spell tempo costs | This document (architecture) |
| **Document 3: Environmental Weather** | Ley line clocks, Reality Seam clocks, rift lifecycle, seasonal cycle, Coherence Clock, forecast system | This document + Operating Philosophy |
| **Document 4: Ancestry & Creatures** | Isotope-to-adaptation tables, Punnett square inheritance, Heritage State formation, sample populations | This document + SRD v2 + Elemental Cards |
| **Document 5: Talent Architecture** | Talent organization by Scope/petal/category, Crux/droplet model, sphere grid structure | This document + Document 2 |
| **Document 6: Social & Mental Combat** | Background mechanical definitions, social/mental action atoms, cross-pillar interaction | This document + Document 2 |
| **Document 7: Master Talent Catalogue v2** | Every talent tagged, placed, and mechanically specified | Documents 2, 5, and 6 |

---

# PART XIII: CANONICAL TERMINOLOGY

## Confirmed Terms (Use These)

| Term | Meaning | Replaces |
|---|---|---|
| **Scope** (S0-S9, S∞) | The universal scale measuring effect reach and temporal resolution | "Distance" (retired — ambiguous with physical distance) |
| **Composite Defense** | The combined defensive value from applicable defenses | AC, Combined Defense Score |
| **Poise** | Social HP pool | Reputation Pool |
| **Clout** | Background: accumulated social weight | Influence (background) |
| **Soak** | Damage reduction value (Toughness/Conviction/Composure/Resilience) | DR |
| **TN** | Target Number for checks | DC |
| **Achieved ESL** | The effective power level of a spell/effect | Caster Level equivalent |
| **Shove** | Combat maneuver: push target | Bull Rush |
| **Archetypes** | Character build templates | Classes |
| **Psyche Schema** | Personality diagnostic instrument | "Personality quiz" |
| **Kan-tech** | Technology derived from Kanon's Structured Current | Magi-tech |
| **Essence** | Metaphysical attribute (raw planar connection) AND Metaphysical Resist defense | Anima (attribute and defense) — retired to avoid collision with Anima the god |

## Pool Names

| Pillar | HP Pool | Operational Pool |
|---|---|---|
| Physical | Vitality | Stamina |
| Mental | Resolve | — (uses Stamina for mental exertion, ÆP for mental expressions) |
| Social | Poise | — (uses backgrounds as social "resources") |
| Metaphysical | Pattern | ÆP (Æther Points) |

## Condition Track Step Names

| Step | Physical | Mental | Social | Metaphysical |
|---|---|---|---|---|
| 0 | Unharmed | Composed | Poised | Stable |
| −1 | Winded | Distracted | Flustered | Frayed |
| −2 | Reeling | Shaken | Humbled | Strained |
| −3 | Wounded | Frightened | Disgraced | Corrupted |
| −4 | Crippled | Befuddled | Rapt | Unraveling |
| −5 | Incapacitated | Catatonic | Broken | Collapsed |

## Defense Names

| Function | Physical | Mental | Social | Metaphysical |
|---|---|---|---|---|
| Evade | Evasion | Willpower | Grace | Acuity |
| Deflect | Guard | Control | Dignity | Integrity |
| Absorb (Soak) | Toughness | Conviction | Composure | Resilience |
| Resist | Vigor | Courage | Discretion | Essence |

---

*End of Document 1: Unified Architecture. This document is the architectural map. All mechanical implementations reference this structure. No downstream document should introduce systems that contradict the principles established here.*

# THE ÆTHERIUM CODEX — THE COMBAT ENGINE
## Document 2: Tempo, Scope, and the Universal Grammar of Action
### Canonical Draft — April 15, 2026 — Revision 3 (SRD v3 Integrated)

---

## PREAMBLE

This document specifies the combat engine layer that sits atop the SRD v3's material science, spell sentence, and item systems. The SRD v3 provides the physics — the 19+Variable effects, the scaling tables, the Construction Pool geometry, the Planar Strain mechanics. This document specifies the game: how those mechanics produce playable action resolution across every Scope of engagement, from personal combat at Scope 0 through institutional operations at Scope 7+ and cosmological action at Scope ∞.

The tempo model, nested clock architecture, and Fulcrum Point unification defined here are canonical, locked at SRD v3 compatibility level. Where this document references effect mechanics, the SRD v3 is authoritative. Where this document defines action resolution, it supersedes any earlier combat materials.

---

# PART I: THE 19+VARIABLE EFFECTS AS UNIVERSAL VERBS

## Core Principle

The SRD v3's canonical 19+Variable effects (Amendment 1) are not combat mechanics. They are not magic mechanics. They are the UNIVERSAL VERB LIST for all actions in the system. Every action at every Scope, through every petal, against every pillar, is expressible as one or more of these verbs.

A sword strike is a Damage effect delivered through the Combat petal against the Physical pillar at Scope 0. A trade embargo is a Nullify effect delivered through the Social petal against the Physical pillar at Scope 6. A propaganda campaign is an Illusion effect delivered through the Social petal against the Mental pillar at Scope 7. Same grammar. Different Scope. Different delivery. Different target.

## The Canonical Effect Table (SRD v3, Amendment 1)

| Category | Effect | BER | Combat-Relevant Notes |
|---|---|---|---|
| **Offensive** | Damage | 1 | Direct harm across any pillar. Isotope determines damage type and die band. |
| **Offensive** | Affliction | 1–5 | Discrete conditions (Trivial BER 1 → Critical BER 5) or directed track movement. |
| **Offensive** | Nullify | 3 | Counter-magic via neutralization reaction. Exothermic — energy release scales with target ESL. |
| **Offensive** | Weaken | 2/3/4 | Reduce attributes. Single (2), Pillar (3), Full Suite (4). Mirrors Enhanced Trait. |
| **Defensive** | Protection | 2 | Numeric defense (DB, Soak, ER, Threshold, Barrier HP). Never absolute. |
| **Defensive** | Immunity | 4 | Absolute negation. ESL determines breadth (single isotope → conceptual). |
| **Defensive** | Immortality | 5 | Permanent soul-body binding preventing death from completing. |
| **Movement** | Movement | 1 | ALL physical movement modes (walk, swim, burrow, climb, fly). Isotope determines medium. |
| **Movement** | Teleport | 3 | Same-plane translocation via Palimpsest skim. |
| **Movement** | Dimensional Travel | 4 | Interplanar transit through deep Palimpsest. |
| **Movement** | Time Travel | 5 | Temporal displacement via Synod navigation. |
| **Recovery** | Healing | 2 | HP restoration across all four pillars. Duration creates HoT. |
| **Recovery** | Panacea | 3 | Condition reversal. Inverse of Affliction. High-rank Panacea = resurrection. |
| **Sensory** | Senses | 2 | Information management (absorbs Communication, Comprehend, Remote Sensing). |
| **Sensory** | Mind Link | 3 | Bidirectional mental access. Low: read. Mid: charm. High: dominate. |
| **Support** | Feature | 0 | Cosmetic magical tell. Everyone in Tessera has one. Diagnostic. |
| **Support** | Chronos | 2 | Temporal flow manipulation. Haste/slow/age/preserve. Affects tempo directly. |
| **Support** | Create | 2 | Form solid non-living objects or Palimpsest folds. |
| **Support** | Move Object | 2 | Telekinesis. ESL determines weight capacity. |
| **Support** | Illusion | 2/3 | Palimpsest superposition collapse. Single sense (2) / multi-sensory (3). |
| **Support** | Enhanced Trait | 2/3/4 | Attribute enhancement. Mirrors Weaken. |
| **Support** | Summon | 3 | Condense prima æther into shaped magical expression. Universal shaping verb. |
| **Support** | Transform | 1/2 | Alter fundamental properties. Minor (1) / Significant (2). |
| **Meta** | Variable | Rank × 2 | Bounded replicator. Reproduces any known effect. |

Scaling tables for each effect are canonical in the SRD v3 (Session 2, Amendment 7). Combat engine references those tables — it does not redefine them.

## The Action Formula

**Effect + Isotope + ESL + Construction = Specific Observable Action**

- **Effect** — the verb
- **Isotope** — the adjective (subtype, one of 104 in the Elemental Cards)
- **ESL** — the power (capped by min(Effect Tier, Isotope Tier, Mastery))
- **Construction** — the geometry (CP purchases determining target/range/duration, which determines Scope reach)

Scope is not an independent variable. Scope EMERGES from Construction Pool choices. A spell's CP purchases determine the ceiling Scope it can reach. The caster's application within that ceiling determines actual Scope of effect.

## Effects Natural to All Five Planes

The six universal effects — available through any isotope, any plane — form the TRUE baseline vocabulary:

**Affliction, Damage, Movement, Protection, Senses, Transform**

Every character with any isotope training can produce these six. They are the shared grammar of the setting.

## College Signature Effects (SRD v3, Amendment 10)

| College | Signature Effect(s) | Planar Home |
|---|---|---|
| Chiaroscuro Institute | Illusion (superposition collapse) | Palimpsest |
| Chronosynclastic Institute | Chronos + Senses | Palimpsest/Synod interface |
| Deepguard Academy | Protection + Nullify | Hidden Forge |
| Mortis Ævum Collegium | Affliction + Weaken + Healing | Synod |
| Praxis Collegium | Variable | None (isotope-independent) |
| Sovereign Exchange | Create + Enhanced Trait | Borderlands/Hidden Forge |
| Stormpeak Academy | Damage | Borderlands |
| Unity Academy | Mind Link | Palimpsest boundary |
| Wildpath Wardens | Transform | Verdant Font |

---

# PART II: THE FOUR TIERS OF EXPRESSION

## Core Principle

Every living being in Tessera is composed of planar materials. There is no "purely mundane" baseline. The distinction between "martial" and "magical" is a gradient of how deliberately the character channels their isotope expression, not a binary category.

**Magic is technology in this setting.** Guns are ranged Damage effects delivered through Forge-crafted items with a bore. They can be modified with attachments and insets like any other magical item. The vocabulary between "item" and "weapon" blurs completely because they ARE the same thing — Forge-crafted expressions of effect, isotope, and geometry through a physical substrate.

## The Spectrum

### Tier 0 — Ambient Expression (Every Living Being)

No training. No deliberate channeling. The body's ambient isotope profile interacts with the environment and with wielded materials at negligible levels. A Borderlands Magma-adapted warrior's strikes are microscopically hotter than baseline. Undetectable, unmeasurable, but present. The seed is planted.

The Feature effect (SRD v3, BER 0) is the universal magical tell — cosmetic only, but every person in Tessera expresses one. The prima æther acknowledging you exist and you acknowledging it back. Trained observers read Features diagnostically to map magical aptitude.

### Tier 1 — Trained Technique (Mundane Talents, Combat Petal)

Physical training that makes actions more effective through biomechanics — better angles, timing, force application. No deliberate isotope channeling. Power Attack hits harder because of leverage and commitment, not directed expression.

### Tier 2 — Directed Expression (The Bridge)

Trained physical technique paired with directed isotope channeling. Channeled Strike routes isotope expression through the weapon. The strike hits with physical force (from training) AND isotope force (from directed expression). The technique is the VEHICLE. The expression is the PAYLOAD.

This is where Incarnum-style soulmeld mechanics live — deliberate shapings of isotope profile into functional constructs through Summon's universal shaping verb application.

### Tier 3 — Full Expression (Magical Talents, Philosophy Petal)

The Spell Sentence in its full form. Complete expression constructed from Effect + Isotope + Construction Pool geometry. The technique is entirely metaphysical.

**The Spell Sentence allows for skipping of friction.** At Tier 3, the expression bypasses the physical biomechanics of Tier 1 and the directed channeling of Tier 2 to construct the effect directly. This is the advantage of magical talents — they skip intermediate tiers. The trade-off is ÆP (Metaphysical FP) fuel cost and CP construction requirement.

## The Setting Baseline

Mastery bands (SRD v3):
- **Novice (1-4):** Raw potential, untrained capability, Formation Stage 1-4 crafting access
- **Journeyman (5-7):** Professional, trained efficiency, Formation Stage 5-7 access
- **Master (8-10):** Peak mortal capability, Formation Stage 8-10 access
- **Beyond Mortal (11+):** Monstrous (×2) and Divine (×10) attribute scales

## The Design Goal

**Tiers 1+2 paired must be COMPETITIVE with Tier 3 alone.** The trained warrior channeling heritage expression through physical technique should match the caster constructing full expressions. Different method, comparable output. This is the core fix for the 3.5e martial/caster divide.

The bridge: **everyone in this system has the potential for magic and magical effects regardless of their personal feelings for it.** The Tier 0 ambient expression exists whether the character acknowledges it or not. The biology of Tessera includes isotope channeling as a baseline condition.

---

# PART III: THE S0 COMBAT BASELINE (UNIVERSAL GRAMMAR)

## What Every Living Being Can Do (0 CP Equivalent)

### Physical Actions

| Action | What It Is | Effect Parallel |
|---|---|---|
| **Strike** | Extend limb to impact — punch, kick, shove, headbutt | Damage |
| **Block** | Interpose body part between attack and vital area | Protection |
| **Grab** | Close hands around something — grapple initiation | Affliction (restraint) |
| **Push** | Apply force to move something or someone | Move Object |
| **Move** | Walk, run, crawl, climb, swim, jump | Movement |
| **Dodge** | Shift weight to avoid incoming | Protection (evasive) |
| **Observe** | Look, listen, smell — all senses active | Senses |
| **Communicate** | Speak, shout, gesture | Senses (output mode) |

### Metaphysical Baseline

| Capability | What It Is | Implication |
|---|---|---|
| **Heritage expression** | Always-on racial adaptations from ancestral isotope profile | Passive Heritage State bonuses |
| **Ambient interaction** | Natural resonance with heritage-matched materials | Heritage-matched weapons feel right |
| **Isotope awareness** | Sensing strong local planar concentrations | The body resonates with heritage isotope |
| **Passive Strain processing** | Mutation system operates continuously | Body always adapting to ambient isotope pressure |
| **Weapon resonance** | Heritage-matched weapon carries faint isotope rider | SEED of Channeled Strike, no mechanical effect at baseline |
| **Feature** | Universal cosmetic magical tell | Diagnostic for trained observers |

## The Mapping to Effects

Every baseline physical action IS a universal effect delivered through the body at Scope 0. Strike = Damage. Block = Protection. Push = Move Object. Grab = Affliction. The effect vocabulary is not separate from combat — combat actions ARE effects. Training and channeling (Tiers 1-3) make those effects MORE POWERFUL, not fundamentally different.

---

# PART IV: THE TEMPO MODEL

## What Tempo Represents

Tempo is not "how fast you move." Tempo is COGNITIVE BANDWIDTH — how many decision cycles (OODA loops) you can process before the phrase resets.

Each tempo represents one complete Observe-Orient-Decide-Act cycle. The phrase is the chain of tempos strung together without resetting to neutral. A phrase ends when participants disengage from the current exchange and reorient.

## The Formula

**Tempo Pool = Wits + Mastery**

Two components. Nothing else.

- **Wits:** How fast each OODA cycle processes. Faster Wits = more cycles in the same elapsed time.
- **Mastery:** How compressed each cycle is through training. The master's parry-riposte is ONE cycle. The novice's parry is one cycle and the riposte is a SECOND cycle.

Physical speed determines how well you EXECUTE each act, not how many cycles you process. Strength determines how much FORCE each act delivers. These affect action QUALITY, not action QUANTITY.

## Range

| Level | Wits | Mastery | Tempo Pool | Character |
|---|---|---|---|---|
| Starting novice | 2-3 | 3 | 5-6 | Trained but inexperienced practitioner |
| Experienced journeyman | 3-4 | 5 | 8-9 | Seasoned professional |
| Peak master | 4-5 | 8-10 | 12-15 | Absolute elite of mortal capability |

## Commitment Spectrum

Actions cost tempo based on ESL:

| Commitment | Tempo Cost | ESL Band |
|---|---|---|
| **Light** | 1 tempo | ESL 1-2 |
| **Standard** | 2 tempos | ESL 3-4 |
| **Heavy** | 3 tempos | ESL 5+ |

## The Tempo/FP Relationship

Tempo and Fulcrum Points are SEPARATE CONSTRAINTS. Both must be available to execute an action.

- Tempo governs HOW MANY actions you can process per phrase (bandwidth)
- FP governs HOW MANY you can FUEL (cost)

The LESSER of available tempo and available FP governs actual output per phrase.

---

# PART V: THE UNIFIED FULCRUM POINT SYSTEM

## Core Principle

Every pillar has its own Fulcrum Point pool. All four pools use the same formula structure, the same universal action cost, the same recharge mechanics. FP is agnostic fuel — each point flavors to the pillar it came from (Physical FP functions as stamina, Metaphysical FP functions as ÆP, Social FP functions as influence/momentum, Mental FP functions as focus/composure), but the mechanical architecture is identical.

## The Four Pools

| Pillar | Pool Name | Formula | Talent Count (T) |
|---|---|---|---|
| **Physical** | Physical FP | (Vigor + Tc) × Mastery | Combat petal talents |
| **Mental** | Mental FP | (Acuity + Tk) × Mastery | Knowledge petal talents |
| **Social** | Social FP | (Guile + Ts) × Mastery | Social petal talents |
| **Metaphysical** | Metaphysical FP (ÆP) | (Dominion + Tₘ) × Mastery | Philosophy petal talents |

The Metaphysical pool IS ÆP. The formula is unchanged from the SRD v3. The other three pillars now use the same architecture.

## The Universal Action Cost

**FP Cost = (ESL × 2) − 1**

Universal across all pillars, all petals, all Scope levels, all action types.

| ESL | FP Cost | Typical Actions |
|---|---|---|
| 1 | 1 FP | Simple strike, basic argument, quick observation, minor spell |
| 2 | 3 FP | Trained technique, coordinated negotiation, standard spell |
| 3 | 5 FP | Complex maneuver, strategic play, significant spell |
| 5 | 9 FP | Master-level action in any pillar |
| 7 | 13 FP | Apex mortal action |
| 10 | 19 FP | Peak human capability |

## Scope Does Not Multiply Cost

Scope is not a cost modifier. The ESL of the action already encodes scope-appropriate complexity. An S0 personal action is inherently low ESL (1-4). An S7 institutional action is inherently high ESL (6-8) because that Scope's complexity requires that tier of expression.

The cost follows ESL, not Scope.

## FP Tagging

Every FP point carries two tags:

**Pillar tag** (at generation — which pool): Physical, Mental, Social, or Metaphysical.

**Scope tag** (at expenditure — what scale): S0 through S∞.

When spending FP, both tags are declared. The pillar tag determines the TYPE of effect. The Scope tag determines the REACH.

## Drip Recharge

All four FP pools recharge through drip mechanics anchored to Scope intervals. Base rate is one FP per S2 interval per pool.

| Condition | Rate | Represents |
|---|---|---|
| **Stressful** (combat, crisis) | ×1 | Standard drip under pressure |
| **Calm** (safe environment) | ×2 | Doubled rate when not under stress |
| **Sleep / bed rest** | ×4 | Quadrupled rate during restorative rest |

The drip accumulates regardless of circumstance. No "full rest" — all recovery through accumulated drip. Recharge is per-pool simultaneous.

## Recovery Through Schema Engagement

Beyond base drip, characters recover FP through Schema pressure point activation. When a situation tags a character's pressure point (outlier, split, or break) and the character ENGAGES with it, they recover FP into the pillar most aligned with that engagement.

Character depth = faster recovery = more total FP available across a session.

## Destiny Points Remain Separate

Destiny Points are treasure currency, GM-awarded. Not generated by Schema. Not recharged through drip. They represent dramatic peaks where player and GM agency converge. Mechanics defined separately.

---

# PART VI: SCOPE-CP GEOMETRY (SRD v3 AMENDMENT 6)

## Core Principle

Scope is embedded in the Construction Pool geometry system. The CP a caster invests in target shape, range, and duration determines the spatial and temporal reach of their expression — which IS the Scope they operate at.

## The Three Scale Tiers

| CP Range | Shapes Available | Scale Tier | Scope Range | Access |
|---|---|---|---|---|
| **0-3** | Individual, Ray, Emanation, Burst (small), Cone, Spread, Line, Wall (Standard) | **Encounter** | S0-S2 | Common |
| **4-6** | Burst (Large), Zone, Wall (Fortified) | **Battlefield** | S3-S4 | Dialect |
| **7-10** | District, Regional, Territorial, Vast | **Geographic** | S5-S7+ | Treasure |

## Access Tier Implications

**Common (CP 0-3, Encounter scale):** Known by default (0 CP) or purchasable at creation using Grammar Points. Every character has full access to Encounter-scale actions.

**Dialect (CP 4-6, Battlefield scale):** Must be learned through play. A character cannot start with Battlefield-scale geometry. They must encounter it and train.

**Treasure (CP 7-10, Geographic scale):** Must be acquired through exceptional circumstances. Cannot be learned at character creation. This is the mechanical constraint that makes institutional pooling necessary for high-Scope operations.

## Implications for Combat Engine

**An individual character, through personal training alone, can only operate up to Battlefield scale (S3-S4).** To reach Geographic scale (S5+), they need:

1. **Institutional pooling** — combining FP resources across many actors
2. **Exceptional circumstances** — treasure-tier resources acquired through play
3. **The Systemic Catalyst talent** — leveraging natural systems to multiply reach

This is why Scope 5+ operations are inherently institutional. The mechanical system enforces it. No individual, no matter how powerful, can achieve Geographic-scale effects through personal CP alone.

---

# PART VII: THE UNIFIED FULCRUM POINT SYSTEM AT SCALE

*(Institutional FP pooling mechanics — how characters reach beyond personal ceiling)*

## Pool Stacking (Operating Philosophy Composite Pools)

Per the Operating Philosophy, FP pools stack across five layers:

| Layer | Source | Available To |
|---|---|---|
| Personal | Character's own Schema + drip | The individual |
| Positional | Role within an institution | Whoever holds the position |
| Institutional | Institution's aggregate FP | Whoever operates the institution |
| Territorial | Territory's Zoetrope tension, isotope asymmetries, factional conflicts | Entities with territorial claim |
| Divine | God's aspect tension | Mortals whose actions resonate with portfolio |

A headmaster accessing Personal + Positional + Institutional + Territorial + Divine pools has dramatically more FP than an individual adventurer operating alone. This is why headmasters are the most narratively potent entities short of gods.

## Infrastructure Tiers

Communication infrastructure determines how many actors can pool FP:

| Infrastructure | Pooling Capacity | Institutional ESL Reach |
|---|---|---|
| None | Individual only | Limited to personal FP totals |
| Basic (voice, runners) | 3 actors, co-located | Moderate institutional ESL |
| Standard (institutional comms) | 10 actors, same region | Significant institutional ESL |
| Advanced (Forge ward networks) | 50 actors, multi-region | High institutional ESL |
| Exceptional (Palimpsest links) | Unlimited, cross-territorial | Civilizational ESL |

The Forge doesn't just build items. It builds institutions capable of operating at higher ESL through FP pooling.

---

# PART VIII: THE NESTED CLOCK ARCHITECTURE

## Core Principle

Higher-Scope actions are not separate from lower-Scope actions. They are COMPOSED of them. There is no special "S7 action." There are thousands of S0 actions — reading, talking, writing, thinking — that accumulate through nested clocks until one S7 tempo finally advances.

## S0 as Universal Processing Speed

Wits + Mastery governs S0 processing speed. S0 efficiency cascades UPWARD — a faster S0 processor fills higher-Scope clocks faster.

## The Cascade

| Activity | Scope | Feeds |
|---|---|---|
| Reads one page of a report | S0 | S1 "process this report" |
| Finishes the report, cross-references others | S1 | S2 "sector assessment" |
| Discusses assessment with staff | S2-3 | S4 "operational posture" |
| Approves posture after meetings and field visit | S4 | S5 "campaign allocation" |
| Finalizes allocation after weeks of assessments | S5 | S7 "institutional reorientation" |

## Movement as Temporal Calibration

Movement defines temporal resolution at each Scope:

| Scope | Movement Type | Time per Movement |
|---|---|---|
| S0 | Reaction — flinch, sidestep | Fraction of a second |
| S1 | Combat speed — sprint to cover | Seconds |
| S2 | Deployment — establish perimeter | Minutes |
| S3 | Forced march — company to objective | Tens of minutes |
| S4 | Operational redeployment — battalion shift | Hours |
| S5 | Campaign movement — army relocates | Days |
| S6 | Strategic repositioning — theater redeploy | Weeks |
| S7 | Institutional shift — college reallocates | Months |

## The Tempo-Fill Principle

To affect a target operating at Scope N, you must fill at least one tempo of time at Scope N. S0 events accumulate through nested clocks — enough S0 ticks fill an S1 tempo, enough S1 tempos fill an S2 tempo, and so on.

## The Smoothing Effect as Scope Resistance

The Smoothing Effect (from the Operating Philosophy) IS the mechanism requiring tempo-filling at each Scope. Not a separate system — the natural resistance preventing Scope jumping.

| Scope | Smoothing Resistance |
|---|---|
| S0-S2 | None — personal actions resolve freely |
| S3-S4 | Minor — operational inertia, communication latency |
| S5-S6 | Significant — political opposition, resource constraints |
| S7-S8 | Major — institutional inertia, civilizational complexity |
| S9-S∞ | Maximum — Aíon's continuous maintenance |

The Smoothing Effect manifests mechanically as the requirement that each clock be filled through accumulated lower-Scope ticks before the next advances. You cannot skip from S0 to S7. The time this takes IS the Smoothing Effect's operational expression.

## The S3+ Fault Line

| S0-S2 | S3+ |
|---|---|
| PARTICIPANT — body in action | DIRECTOR — body behind the line |
| Combat petal actions (Strike, Block, Grab, Channeled Strike) | Social petal (Command, Rally, Coordinate) and Knowledge petal (Analyze, Plan, Assess) |
| Sword arm matters | Signal corps matters |
| Physical movement | Organizational movement |

A character splitting across the fault line divides tempo and FP across competing activities. Every tempo spent on a personal Strike is a tempo NOT feeding the Command clock.

The Stormpeak Way of the Phalanx exists specifically to minimize S0 tempo expenditure on personal combat (shield wall = reactive, low tempo cost posture) so the officer can allocate tempo and FP to S3+ command actions instead.

---

# PART IX: THE SYSTEMIC CATALYST TALENT

*(The mechanical bridge enabling individual characters to operate at Scope levels normally requiring institutional pooling)*

## What It Is

The Systemic Catalyst talent (SRD v3, Amendment 4) allows a practitioner to target a natural system's leverage point rather than a direct target. The effect's reach multiplies based on the system's scale. The multiplier applies to AREA of consequence, not intensity. Precision is lost proportionally.

## The Multiplier Table

| System Scale | Multiplier | Leverage Point Example |
|---|---|---|
| Local (room/pond) | ×2 | Heating element in closed room |
| Site (building/grove) | ×5 | Structural keystone, root system hub |
| Block (street/stream) | ×10 | Water main, gas line, herd alpha |
| District (neighborhood/creek) | ×25 | Tributary junction, power grid node |
| Regional (valley/river) | ×100 | Pressure gradient, aquifer source |
| Territorial (weather front/ecosystem) | ×500 | Jet stream boundary, watershed divide |

**×2 = mostly controllable. ×500 = act of god pointed in a direction.**

## Prerequisites

- Minimum ranks in Discovery or Survival
- Knowledge of relevant isotope
- GM confirms valid leverage point exists

## Post-Trigger Behavior

Output becomes NON-MAGICAL after triggering. Natural processes take over. Nullify cannot reverse it. This is a critical property — you are not maintaining a magical effect at scale, you are initiating a physical cascade that proceeds under its own momentum.

## Combat Engine Implications

Systemic Catalyst is how individual characters produce the five validated attack vectors:

| Attack Vector | Systemic Catalyst Application |
|---|---|
| **Stealth Accumulation** (Dien Bien Phu) | Multiple low-intensity Movement/Growth applications at Site-District scale below detection threshold |
| **Parallel Relay Exploitation** (Tet) | Senses/Mind Link at District scale (media infrastructure leverage) |
| **Clock Starvation** (Malaya) | Nullify routed through Regional pressure gradient (supply chain/food/water node) |
| **Single Point of Failure** (Six-Day War) | Damage at Site or Block scale (structural keystone, command node) |
| **Analytical Poisoning** (Yom Kippur) | Illusion + Affliction at Regional/Territorial scale (doctrine/analytical framework node) |

The talent is the mechanical implementation. The five attack vectors are historical proof that this design produces real strategic thinking.

## Why This Matters

Without Systemic Catalyst, individual characters could only reach Battlefield scale (S3-S4) through personal training. With Systemic Catalyst, a single trained practitioner can produce Geographic-scale consequences (S5-S7+) by identifying and leveraging natural systems. The asymmetric warfare capability is now a player option, not just institutional fiction.

---

# PART X: THE COMMUNICATION INFRASTRUCTURE

## Two Separate Systems

**Information relay:** Observations flow UPWARD. Scouts → squad leaders → company commander → HQ. Each link adds latency and loses fidelity.

**Command relay:** Decisions flow DOWNWARD. General → staff → field commanders → squad leaders → troops. Each link adds latency and introduces interpretation.

Separate attack surfaces. You can have perfect intelligence and no command infrastructure. You can have perfect command infrastructure and no intelligence.

## Communication as Scope Compression

Every transition between Scope levels adds latency and loses fidelity. Reducing transitions is the fundamental operational advantage.

**Full chain (no enhancement):** Seven transitions, weeks of latency, catastrophic fidelity loss.

**Compressed chain (Forge communication):** Two transitions via Forge ward networks, hours of latency, recognizable fidelity.

**Maximally compressed (divine perception):** Zero transitions — Aíon perceives S0→S∞ directly. This is what godhood provides and what Lyra pursues.

## The Information Threshold

Events below a significance floor at each Scope transition don't generate reports. They're invisible to higher Scopes. An attacker keeping every action below that threshold accumulates force without triggering defender's higher-Scope clocks. This is the Dien Bien Phu vector — stealth accumulation.

## Analytical Poisoning

The information relay can fail at any transition, each differently. The most dangerous failure is at the ORIENT phase of the OODA loop — where institutional assumptions filter incoming intelligence. A corrupted analytical framework produces FALSE CONFIDENCE. Worse than destroyed relays (recognized absence of information). The Yom Kippur vector.

---

# PART XI: THE INTERACTION TYPE MODIFIERS

*(Cross-pillar and cross-planar combat calculation — SRD v3 Planar Strain system, applied universally)*

## Core Principle

The four interaction types from the Planar Strain system apply to all cross-pillar combat interactions, not just Strain calculation. When an effect from one pillar/plane interacts with a target defended by a different pillar/plane, the interaction type modifier applies.

## The Four Types

| Interaction | Modifier | Description |
|---|---|---|
| **Cooperative** | ×0.25 | The effect aligns with target's existing state. The body accepts it. Minimal resistance. |
| **Competing** | ×1.0 | The effect conflicts with target's current state. Standard resistance. |
| **Cancellation** | ×1.5 | Effects fight each other. The target is caught between. Higher stress. |
| **Emergent** | ×2.0 | Something new is being created. No template. Maximum demand. |

## Combat Applications

**Cooperative:** Healing an ally's existing biology with V-01 World Tree. Enhanced Trait applied to an attribute matching target's isotope profile. Aligned Mind Link establishing connection to a willing participant.

**Competing:** Standard damage — Borderlands Inferno attacking a non-aligned target. Most common combat interaction. Default calculation.

**Cancellation:** Synod entropic effect applied to a Font-mutated creature. Borderlands expression against a Palimpsest-warped construct. The effects fight rather than negotiate.

**Emergent:** Emulsion artifact interactions. Multiple strong planar expressions interacting in the same target simultaneously. Unpredictable outcomes — the target has no template for what they're becoming.

## Implications for Attack Vectors

Clock starvation (Malayan Emergency vector) leverages Cooperative interactions at Social pillar (aligning with target populations' existing state) to produce Cancellation effects at Physical pillar (guerrilla support network). Low-resistance infiltration at one pillar produces high-resistance crisis at another.

Analytical poisoning (Yom Kippur vector) leverages Cooperative Illusion (aligning with target's analytical framework) to produce Emergent Affliction (the framework itself becomes a disease). The target accepts the input as confirming existing assumptions — Cooperative. The accumulated corruption then produces unprecedented failure — Emergent.

---

# PART XII: SPECIAL EFFECT MECHANICS

## Chronos as Tempo Multiplier

Chronos directly affects the tempo economy. At ESL 7, the buff grants "two full rounds per one" — doubling the tempo pool for a phrase. At ESL 10, the character's relationship with time is fundamentally rewritten.

| ESL | Buff | Debuff |
|---|---|---|
| 1 | +1 initiative | −1 initiative |
| 3 | Haste — extra attack, +30 ft, +1 Dodge | Slow — lose action, −30 ft, −1 Dodge |
| 5 | Extra standard action per round | Only one action per round |
| 7 | Two full rounds per one | Near-stasis |
| 10 | Relationship with time fundamentally rewritten | Personal timeline ceases |

Chronos at ESL 5+ breaks normal tempo constraints. Under ESL 7 Chronos, a character gets two phrases per one shared phrase. This is the mechanical basis for why the Chronosynclastic Institute is feared — their signature effect directly multiplies action economy.

Combat engine note: characters under Chronos effects have independent tempo budgets that can diverge from the shared phrase structure. The GM tracks their tempo separately during the duration.

## Hyper-Real Illusion as Metaphysical Damage

Illusion at ESL 10 produces >100% collapse — hyper-real, MORE anchored than baseline reality. Succeeding on a save against >100% Illusion causes Metaphysical track damage.

This is mechanically significant for combat at high Scopes. Chiaroscuro Institute masters can produce realities that overwrite baseline reality. Observers who penetrate the illusion pay Metaphysical damage because they see behind reality's curtain. The Maestro is a permanently >100% collapsed superposition state — an entity maintained by collective belief that cannot be destroyed by conventional means.

Combat application: Chiaroscuro attacks against the Mental pillar can deal Metaphysical pillar damage when the target succeeds too well on their save. Over-performing on the defense IS the vulnerability.

## Nullify as Exothermic Neutralization

Nullify operates via acid-base chemistry model. Incompatible expression introduced to target's concordance structure. Reaction is exothermic — energy release scales with target ESL.

| ESL | Energy Release | Implication |
|---|---|---|
| 1-2 | Negligible to Minor | Counter-magic with no collateral |
| 3-4 | Noticeable to Significant | Counter-magic with area effect |
| 5-6 | Dangerous to Major containment | Active offensive action |
| 7-10 | Massive to cosmic hiccup | Structural damage to surroundings |

Combat engine note: Nullify at ESL 5+ is an OFFENSIVE action, not just defensive. Breaking Deepguard wards releases stored concordance energy as uncontrolled burst. A character countering a high-ESL spell with Nullify deals collateral damage to everything in the vicinity.

Against Structured Current (Architect) spells: introduce turbulence into the concordance lattice.

Against Primal Current (Improviser) spells: impose unwanted structure on chaotic flow, crystallize until it shatters.

Against natural phenomena: significantly harder — no caster maintaining the expression.

---

# PART XIII: THE FIVE VALIDATED ATTACK VECTORS

Historical cross-examination (mid-1940s through mid-1970s conflicts) validates five distinct attack vectors against the nested clock architecture. Each is mechanically implemented through Systemic Catalyst plus specific effect combinations.

## 1. Stealth Accumulation (Dien Bien Phu, 1954)

**Mechanism:** Thousands of S0 actions individually below information threshold accumulate to fill an S5 clock invisible to defender.

**Effects:** Movement → Growth (Transform) → Summon → Damage

**Systemic Catalyst:** Applied at Local or Site scale repeatedly. Each individual action too small to generate reports. The cascade fills higher Scope clocks through raw accumulation.

## 2. Parallel Relay Exploitation (Tet Offensive, 1968)

**Mechanism:** Two relay systems feed same clock with contradictory assessments. Lower-transition relay wins.

**Effects:** Damage (S0-2) + Senses (bypass primary relay) → Illusion (primary relay contradicted) → Weaken (institutional will)

**Systemic Catalyst:** Applied at District scale (media infrastructure). Not building the infrastructure — LEVERAGING it.

**Key Insight:** Communication infrastructure that compresses transitions works for EVERYONE, not just who built it.

## 3. Clock Starvation (Malayan Emergency, 1948-1960)

**Mechanism:** Cut off S0 actions that FEED clocks rather than attacking clocks directly. Clocks starve.

**Effects:** Protection + Healing (Social pillar at S5-6) → Nullify + Weaken (Physical pillar at S1-3 as cascade)

**Systemic Catalyst:** Applied at Regional scale — pressure gradient of a population's support network.

**Key Insight:** An S0 action that never happens can't cascade upward. Preventing input is as effective as defeating output.

## 4. Single Point of Failure (Six-Day War, 1967)

**Mechanism:** Critical infrastructure node destruction cascades DOWNWARD through all dependent Scopes.

**Effects:** Senses (identify node) → Damage (destroy it) → Weaken (cascading downward)

**Systemic Catalyst:** Applied at Site or Block scale — structural keystone, command node, communication hub.

**Key Insight:** Systems without redundancy at critical nodes are brittle regardless of strength elsewhere.

## 5. Analytical Poisoning (Yom Kippur War, 1973)

**Mechanism:** Corrupt ORIENT phase of target's OODA loop at S5-S7. Relay delivers accurate observations but analytical framework is wrong.

**Effects:** Illusion + Affliction (Mental pillar, S5-7) → Damage (Physical pillar, S2-4 enabled by corrupted orientation)

**Systemic Catalyst:** Applied at Regional or Territorial scale — doctrinal framework, institutional analytical lens.

**Key Insight:** Poisoned fidelity at analytical node is more dangerous than destroyed relay. False confidence worse than recognized ignorance.

---

# PART XIV: THE 18 ÆTHERFORGED PRECEPTS

## Structure

Nine colleges, each with a public-facing Overt Way and a secret Covert Way. Each Precept is a Crux talent defining a combat philosophy with supporting talent trees.

## Complete List

| College | Overt Way | Covert Way |
|---|---|---|
| **Wildpath** | Way of the Primal Form — beast emulation, unarmed/shapeshifting | Way of the Silent Hunt — ambush, stealth/ranged/poison |
| **Mortis Ævum** | Way of the Still Verse — surgical precision, paired blades | Way of the Carrion Heart — unstoppable juggernaut |
| **Deepguard** | Way of the Patient Snare — bodyguard, control, bind | Way of the Inevitable Key — infiltrator, defense-breaker |
| **Unity** | Way of the Adamant Heart — psychological warfare, elegant weapons | Way of the Shepherd and Flock — crowd control, pacification |
| **Chiaroscuro** | Way of the Inconstant Moon — deceptive, trick weapons | Way of the Silent Step — assassin, lethal efficiency |
| **Sovereign Exchange** | Way of the Unbroken Road — endurance, caravan defense | Way of the Binding Contract — corporate enforcer, firearms |
| **Stormpeak** | Way of the Phalanx — line-holder, shield wall | Way of the Vanguard — shock trooper, two-handed force |
| **Chronosynclastic** | Way of the Resonant Word — predictive counter, dueling | Way of the Severed Thread — causality enforcer, flurry |
| **Praxis** | Way of the Scholar's Gambit — versatile all-tool | Way of the Fulcrum — analytical, reactive, weakness exploitation |

## Setting Baseline Combat Themes

Frequency analysis across 18 styles reveals universal combat priorities:

| Talent Tree | Appearances | What This Tells Us |
|---|---|---|
| Finesse Style | 10/18 | Speed and precision — most universal approach |
| Agile Defense | 10/18 | Mobility-based defense — nearly universal |
| Durability | 10/18 | Endurance and resilience — almost every style |
| Mobility | 8/18 | Footwork and positioning — fundamental |
| Intimidation Style | 8/18 | Social petal crossing into combat — extremely common |
| Precision Damage | 8/18 | Exploiting vulnerabilities — widely trained |
| Finisher | 7/18 | Capitalizing on advantage — common |
| Teamwork | 6/18 | Coordinated action — a third of styles |
| Commander | 6/18 | Leadership in combat — a third of styles |

The top four — Finesse, Agile Defense, Durability, Mobility — define Tessera's combat philosophy: be fast, be evasive, be resilient, control your positioning. The setting's environmental selective pressure (Titanwood, Reality Seams, ley line weather) favors adaptive mobile fighters over static armored ones.

---

# PART XV: DOWNTIME AS STRUCTURED CLOCK ALLOCATION

## Core Principle

"Downtime" in the nested clock architecture is not dead air. It is where higher-Scope clocks advance. The adventure happens at S0-S2. The campaign happens at S3-S7. The campaign advances because characters spend S0 actions on mundane tasks that cascade upward.

## The Player's Choice

When a character has time between adventures, they are allocating their S0 processing speed (tempo) and their FP across competing clocks. The meaningful decision is: which clocks get my resources?

| Activity | Petal | Clock It Fills | What Advances |
|---|---|---|---|
| Crafting | Knowledge | Project completion | Item creation progress |
| Research/Analysis | Knowledge | Investigation | Understanding, schematic development |
| Training | Combat/Philosophy | Skill development | Talent acquisition, Mastery advancement |
| Medical treatment | Knowledge | Recovery | Physical lasting track integration |
| Therapy/counseling | Social | Integration | Mental lasting track integration |
| Social networking | Social | Relationship | Background advancement, Contact/Ally development |
| Reputation building | Social | Standing | Standing track recovery, Title development |
| Institutional duties | Social/Knowledge | Obligation | Rank maintenance |
| Intelligence gathering | Knowledge/Social | Information | Front awareness |
| Recovery/rest | — | Healing | Pool restoration, condition track reset |
| Personal reflection | — | Schema | FP recovery through pressure point engagement |

## Interrupts

A surprise attack during crafting time costs tempos and FP that would have fed the project clock. Time is zero-sum. Every tempo spent on one clock is a tempo NOT spent on another. Every FP spent on one action is a FP not spent on another. Interrupts during downtime are mechanically meaningful — the cost isn't just the fight, it's the lost progress on every other clock.

---

*End of Document 2, Part I (Revision 3, SRD v3 Integrated). Part II covers: Engagement States and Transitions, Reaction Economy, Multi-Pillar Combat, Multi-Scope Play Rules, and the S0-S2 Action Atom tables with exact ESL references.*
