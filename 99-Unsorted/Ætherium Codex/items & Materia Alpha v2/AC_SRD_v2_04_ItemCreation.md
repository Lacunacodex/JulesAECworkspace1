# THE ÆTHERIUM CODEX — System Reference Document
## Item Creation — The Crafting System

*Alpha SRD — Second Draft*

---

## PREAMBLE

Item creation is the intersection of physical fabrication and alchemical manipulation. A crafter shapes matter and directs planar expressions simultaneously. Every crafting operation involves two categories of work: physical operations that change material form, and alchemical operations that change material composition. Both happen within the same weekly workflow, abstracted into a single Artifice check.

---

## PART I: THE TWO CATEGORIES OF OPERATION

### Physical Operations

Physical operations change form without changing composition. The iron is still iron after forging.

| Operation | What It Does | Common Conditions |
|---|---|---|
| **Shaping** | Forming through deformation — forging, hammering, pressing | Temperature, Mechanical Force, Geometry |
| **Cutting** | Removing material — carving, sawing, chiseling | Mechanical Force, Geometry |
| **Grinding** | Removing through abrasion — sharpening, polishing | Geometry, Mechanical Force |
| **Joining** | Connecting pieces — welding, riveting, binding | Temperature, Geometry, Timing |
| **Finishing** | Surface treatment — oiling, lacquering, burnishing | Medium, Timing, Moisture |
| **Assembly** | Combining sub-components — mounting, setting, stringing | Geometry, Sequence |

### Alchemical Operations

Alchemical operations change composition — chemical structure, planar expressions, or both.

| Operation | What It Does | Common Conditions |
|---|---|---|
| **Synthesis** | Combining substances or expressions into a new combined state | Temperature, Atmosphere, Reagent Ratio, Reagent Compatibility (both axes), Timing, Containment |
| **Decomposition** | Breaking a combined state into simpler constituents | Temperature, Pressure, Medium, Reagent Ratio, Collection Medium, Stabilization, Timing |
| **Displacement** | Replacing one constituent with another | Reagent Ratio, Reagent Compatibility (both axes), Planar Balance, Collection Medium, Stabilization |

### The Dual-Axis Reagent Matching Principle

Every alchemical operation requires reagents satisfying two requirements simultaneously:

**Physical axis:** The reagent must physically survive the processing conditions.

**Alchemical axis:** The reagent must carry the correct planar profile to interact with the target expression.

The intersection of valid physical carriers and valid alchemical profiles determines what reagents are available for any given operation.

---

## PART II: TARGET NUMBER CONSTRUCTION

### Base Formula

**Crafting TN = 10 + Conditions Modifier + Tolerance Modifier**

### The 19 Crafting Conditions

**Physical Conditions (8):**

| # | Condition | Description |
|---|---|---|
| 1 | **Temperature** | Maintaining correct working heat |
| 2 | **Mechanical Force** | Applying shaping pressure — direction, intensity, rhythm |
| 3 | **Atmosphere** | Controlling air/gas environment |
| 4 | **Pressure** | Ambient compression or vacuum (distinct from directed Mechanical Force) |
| 5 | **Timing** | Specific duration or moment — quench timing, reaction duration |
| 6 | **Geometry** | Specific dimensions, angles, shapes |
| 7 | **Medium** | Substance the work is performed in or through — quench medium, solvent, flux |
| 8 | **Moisture** | Water content control |

**Alchemical Conditions (8):**

| # | Condition | Description |
|---|---|---|
| 9 | **Reagent Ratio** | Proportion of reagent to target |
| 10 | **Reagent Physical Compatibility** | First axis — physical survival in processing conditions |
| 11 | **Reagent Alchemical Compatibility** | Second axis — correct planar profile |
| 12 | **Planar Balance** | Relative intensity of multiple planar expressions being combined |
| 13 | **Catalyst Maintenance** | Sustaining Forge catalyst throughout operation |
| 14 | **Collection Medium** | Prepared vessel for receiving separated expressions |
| 15 | **Stabilization** | Holding new expression until it locks |
| 16 | **Containment** | Preventing process from escaping boundaries |

**Process Conditions (3):**

| # | Condition | Description |
|---|---|---|
| 17 | **Sequence** | Operations in specific order — violation produces wrong results or dangerous intermediates |
| 18 | **Purity** | Workspace free of specific contaminants |
| 19 | **Continuity** | Process cannot be interrupted once started |

### Conditions Modifier

| Active Conditions | Modifier |
|---|---|
| 1-2 | +2 |
| 3-4 | +4 |
| 5-6 | +6 |
| 7+ | +8 |

### Tolerance Modifier

| Tolerance | Description | Modifier |
|---|---|---|
| **Wide** | Significant deviation still produces usable result | +0 |
| **Moderate** | Deviation produces noticeable quality loss | +2 |
| **Narrow** | Small deviation produces failure or unintended results | +4 |
| **Razor** | Almost no margin. System actively resists intended outcome | +6 |

### TN Examples

| Operation | Conditions | Tolerance | TN |
|---|---|---|---|
| Shaping iron into blade | Temperature, Force, Geometry (3) | Wide | **14** |
| Smelting ore | Temperature, Atmosphere, Medium, Timing (4) | Moderate | **16** |
| Tempering steel (arrested state) | Temperature, Timing, Medium, Sequence (4) | Narrow | **18** |
| Cooperative alchemical synthesis | Temp, Ratio, Phys., Alch., Stabilization (5) | Moderate | **18** |
| Catalyzed diagonal synthesis | Temp, Ratio, Phys., Alch., Balance, Catalyst, Containment (7) | Narrow | **22** |
| Emulsion synthesis | Temp, Ratio, Phys., Alch., Balance, Catalyst, Containment, Stab., Purity, Continuity (10) | Razor | **24** |

### Schematic TN Reduction

| Authority | What It Provides | TN Reduction |
|---|---|---|
| **Practitioner** | Author's documented process | −2 (conditions band reduced 1 step) |
| **Guild Standard** | Peer-reviewed, certified | −4 (conditions 1 step + tolerance 1 step) |
| **Institutional** | Rigorously tested, legally binding | −6 (conditions 2 steps + tolerance 1 step) |
| **Archival** | Definitive record, Synod Sepulchral sealed | −8 (conditions 2 steps + tolerance 2 steps) |

---

## PART III: THE CRAFTING CHECK

### The Roll

**Artifice Check = d20 + (Artifice Rank × 2) + Relevant Attribute + Modifiers**

Relevant attribute: Intellect (alchemical), Finesse (precision physical), Wits (reactive/volatile), Might (force operations).

### Modifier Types

Same type does not stack (take highest). Different types always stack.

| Type | Stacks? | Represents | Examples |
|---|---|---|---|
| **Competence** | No | Skill, training | Specialized tradition, focused study |
| **Enhancement** | No | Magical amplification | Enchanted tools, attribute buffs. Subject to +2 temp / +4 combined caps |
| **Alchemical** | No | Applied preparations | Tinctures on tools, treated surfaces |
| **Infrastructure** | No | Right tools for the job | Workshop quality, specialized equipment |
| **Insight** | No | Perfect information | Analyzer readings, divination |
| **Collaborative** | Special | Another practitioner's expertise | See collaborative rules |
| **Circumstance** | Yes | Situational conditions | Favorable environment, good lighting. Multiple distinct circumstances stack |
| **Luck** | Yes | Probability manipulation | Multiple distinct Luck sources stack |

### Hazard Penalties

Material hazard ratings impose penalties unless mitigated. These are not modifier types — they are measured material properties from the NFPA/GHS classification.

**Health Hazard (1-10):** Biological danger to the practitioner. Penalty applied to the roll representing impaired ability to work freely while managing exposure risk. Mitigated by protective measures (sealed environments, alchemical treatments, magical shielding). Full protection eliminates the penalty. NOT mitigated by crafting skill — a master alchemist working with mercury is still endangered by mercury.

Chronic exposure to materials with Health Hazard ratings while unprotected is tracked through the **Planar Strain system.** The material's planar expression applies Adaptation Pressure per the Strain mechanic. Accumulated Strain may produce mutations. See the Planar Strain & Mutation Economy section.

**Physical Hazard (1-10):** Flammability and thermal energy release. Penalty applied to the roll. Mitigated by appropriate containment infrastructure.

**Instability (1-10):** Tendency toward violent decomposition or detonation. Penalty applied to the roll. Mitigated by containment and stabilization.

**The Oxidizer Rule:** A material flagged as an Oxidizer increases the effective Physical Hazard rating of adjacent flammable materials by the oxidizer's own Instability rating. The oxidizer itself may not be flammable, but it makes everything around it burn more readily. Storage and workspace organization must account for this — keeping oxidizers separate from flammables is basic alchemist safety.

### Collaborative Crafting

Multiple practitioners fill distinct roles managing specific conditions.

| Operation Complexity | Max Assistants |
|---|---|
| 1-2 conditions | 0 |
| 3-4 conditions | 1 |
| 5-6 conditions | 2 |
| 7+ conditions | 3 |

Each assistant checks against the same TN using their relevant skill and attribute. On success: **Collaborative** modifier to primary crafter equal to half their Artifice Rank (minimum +1). On failure: no contribution. On critical failure: −2 penalty to primary crafter. Different assistants' Collaborative modifiers stack (distinct roles).

---

## PART IV: THE FIVE OUTCOME STATES

| Result | Outcome | PV Progress | Event |
|---|---|---|---|
| TN+10 or higher, OR natural 20 | **Critical Success** | Double progress | Major benefit, no flaw |
| TN to TN+9 | **Success** | Normal progress | Minor benefit, no flaw |
| TN−1 to TN−4 | **Success with Flaw** | Half progress | Minor benefit + minor flaw |
| TN−5 to TN−9 | **Failure** | No progress | Minor flaw, no benefit |
| TN−10 or lower, OR natural 1 | **Critical Failure** | Lose progress | Major flaw, no benefit |

**Normal Progress per week = (Artifice Rank × 10) + (Relevant Attribute × 5)**

### Outcome Options

**Critical Success:** Accept as-is (major benefit), OR reckless overcharge (take major flaw, gain additional major benefit), OR minor push (take minor flaw, gain additional minor benefit). One voluntary addition maximum.

**Success:** Accept as-is (minor benefit), OR overclock (take minor flaw, minor benefit upgrades to major).

**Success with Flaw:** Accept as-is (minor benefit + minor flaw), OR escalate (both upgrade to major), OR sublimate (cancel both — net zero, clean week).

**Failure:** Full buyoff (1 extra week OR 1 minor success + 12% acquisition cost), OR accept minor flaw.

**Critical Failure:** Full buyoff (2 extra weeks OR 2 minor successes OR 1 major success + 25% cost), OR downgrade to minor (1 extra week + 12% cost), OR accept major flaw.

### Buyoff Rules

All flaws are buyable. No flaw is permanent unless the crafter chooses. Buyoff weeks carry no risk — no rolls, no new flaws.

| Flaw | Time | Material | Success Trade |
|---|---|---|---|
| Minor | 1 week | 12% acquisition cost | 1 minor success from any future roll |
| Major | 2 weeks | 25% acquisition cost | 2 minor or 1 major success from future rolls |

Non-consecutive application permitted. Time-based and success-based buyoff can be mixed. The crafting ledger remains open until declared complete.

---

## PART V: BENEFITS AND FLAWS — CRAFTING MUTATIONS

Benefits and flaws are mutations in the item's expression — the same system that governs biological mutation applies to objects. A flaw is a negative mutation induced by crafting conditions. A benefit is a positive mutation emerging from the process.

### Minor Benefits (Lesser Positive Mutations)

| Category | Effect |
|---|---|
| **Cost Reduction** | Reduce Stamina/ÆP cost of item abilities by half EML. OR reduce maintenance material cost by 10%. |
| **Combat Enhancement** | +EML bonus to specific combat maneuver. OR increase critical threat range by 2. OR +1d6 per 2 EML vs specific creature type. OR ignore Soak equal to half EML. |
| **Action Economy** | Specific item action becomes free action. OR standard action becomes move, or move becomes swift. |
| **Influence** | +EML to Influence checks when item visible. OR +half EML to fear resistance. |
| **Duration & Range** | Item effects last 50% longer. OR effect range increased by 25%. |
| **Awareness** | +half EML to perception against surprise. OR +EML once per day on Lore checks. |
| **Durability** | Immune to Brittle/Fragile conditions. OR +EML to item's Physical condition track. |
| **Elemental** | +EML damage of aligned type. Apply isotope-appropriate rider on critical. |
| **Resource** | Store EML points of Stamina/ÆP. Regenerate half EML per interval (standard drip). |

### Minor Flaws (Lesser Negative Mutations)

| Category | Effect |
|---|---|
| **Burden** | −half EML penalty on specific skill when equipped. OR item weighs two size categories more. |
| **Cost Increase** | Increase ability cost by half EML. OR double ability costs. |
| **Durability** | Reduce item Hardness by half EML. OR reduce by full EML. |
| **Identification** | +EML to TN required to identify item properties. |
| **Sympathetic Damage** | Wielder takes 25% of item condition track damage as Metaphysical backlash. OR 50%. |
| **Planar Dissonance** | −half EML on Metaphysical defense for non-aligned wielders. OR −full EML. |
| **Maintenance** | −1 cumulative per encounter without maintenance (max −5, reset by 10 min upkeep). OR max −10 with full session needed. |
| **Resource Drain** | Drain half EML Stamina/ÆP per day from wielder. OR drain full EML. |

### Major Benefits (Critical Success Only)

| Effect | Description |
|---|---|
| **Font** | Reduce all item ability costs by full EML. Can reach 0. |
| **Effortless Invocation** | EML 1-4 abilities at no cost. |
| **Greater Reservoir** | Store EML × 2 Stamina/ÆP. Standard drip regeneration. |
| **Damage Immunity** | Complete immunity to one damage type. |
| **Elemental Fury** | +EML × 2 elemental damage. Isotope rider on every hit. |
| **Executioner's Mark** | Crits cause vulnerability to item's damage type for EML rounds. |
| **Critical Immunity** | Immune to critical hits (armor). |
| **Impenetrable Ward** | Reduce all incoming damage by EML (armor/shield). |

### Major Flaws

Generated by inverting or intensifying minor flaw categories. A minor Brittle Expression (−half EML Hardness) becomes Major Structural Failure (−full EML Hardness AND Physical condition track reduced by half). Specific flaw should reflect what went wrong during the process.

---

## PART VI: PROGRESS VALUE

### PV Formula

**PV = Base Value × Size Multiplier × Quality Multiplier**

| Category | Base Value | Examples |
|---|---|---|
| Simple Mundane | 50 | Wooden staff, basic tools |
| Simple Weapon/Tool | 100 | Dagger, club, leather armor |
| Martial Weapon/Armor | 200 | Longsword, chainmail |
| Complex Weapon/Armor | 400 | Full plate, composite bow |
| Intricate Device | 600+ | Clockwork, complex apparatus |

| Size | Multiplier |
|---|---|
| Tiny / Large | ×0.75 |
| Small / Medium | ×1.0 |
| Diminutive / Huge | ×1.5 |
| Fine / Colossal | ×2.0 |

| Quality | Multiplier |
|---|---|
| Standard | ×0.5 |
| Masterwork | ×1.0 |

### Additional PV for Alchemical Operations

| Operation TN Band | Additional PV |
|---|---|
| Simple (TN 14-15) | +50 |
| Standard (TN 16-18) | +100 |
| Complex (TN 19-22) | +250 |
| Expert (TN 23-26) | +500 |
| Master (TN 27+) | +1000 |

### Additional PV for Material Complexity

Materials with higher Formation Stage and hazard profiles are inherently more difficult to work. The material's contribution to PV reflects the additional challenge of handling dangerous or highly-expressed substances.

| Formation Stage | Additional PV |
|---|---|
| 1-4 | +0 |
| 5-6 | +100 |
| 7-8 | +250 |
| 9-10 | +500 |

| Highest Hazard Rating (of three) | Additional PV |
|---|---|
| 1-3 | +0 |
| 4-6 | +50 |
| 7-8 | +100 |
| 9-10 | +250 |

### Weeks to Completion

**Weeks = Total PV ÷ Weekly Progress**

| Band | Typical Progress/Week | 400 PV Item | 900 PV Item |
|---|---|---|---|
| Novice (Rank 3, Attr 2) | 40/week | 10 weeks | 23 weeks |
| Journeyman (Rank 5, Attr 3) | 65/week | ~6 weeks | ~14 weeks |
| Master (Rank 8, Attr 4) | 100/week | 4 weeks | 9 weeks |

---

## PART VII: THE ITEM CONDITION TRACK

Every item has a condition track across each of the four pillars.

### Physical Condition

Material integrity. Rust, cracks, edge degradation.
- **Pristine → Worn → Damaged → Broken → Destroyed**

### Mental Condition

Information integrity. How much can be learned through analysis.
- Pristine: clearly readable. Destroyed: no analysis recovers what it was.
- The Appraiser's contested Mental checks against the item progressively reveal history.

### Social Condition

Legend and reputation. Grows through the Legacy system.
- Pristine: famous, recognized, carries power. Destroyed: forgotten, socially inert.
- Provides tangible Influence bonuses when displayed.

### Metaphysical Condition

Stability of planar expressions.
- Pristine: all expressions functioning. Destroyed: all coherence lost, expressions gone.
- Degradation from Synod's ongoing claim. Maintenance holds it at Pristine/Worn.

### Repair

| Condition | Repair PV | Material Cost |
|---|---|---|
| Worn → Pristine | 10% original PV | Maintenance materials |
| Damaged → Worn | 25% original PV | 12% acquisition cost |
| Broken → Damaged | 50% original PV | 25% acquisition cost |
| Destroyed → Broken | Not possible through standard repair — requires reconstruction |

---

## PART VIII: SCHEMATICS

A Schematic is a documented crafting procedure making a process reproducible.

### Contents

- **Conditions map** — which of the 19 conditions apply, with acceptable ranges
- **Sequence record** — order of operations, rigid vs flexible steps
- **Failure map** — what goes wrong when conditions deviate, recovery options
- **Reproducibility documentation** — isolation of critical variables

### Authority Levels

| Level | Users | TN Reduction | Recognition |
|---|---|---|---|
| **Practitioner** | Author + apprentices | −2 | Personal knowledge |
| **Guild Standard** | Any Guild-certified practitioner | −4 | Guild legal recognition |
| **Institutional** | Any institutionally certified practitioner | −6 | Institutional quality guarantee |
| **Archival** | Any with archive access and clearance | −8 | Synod Sepulchral seal. Unalterable. |

### Creating a Schematic

Requires successful completion of the operation being documented.
- **PV:** 500 + (100 × Item PV ÷ 1,000)
- **Time:** 1 week per 1,000 PV of documented item
- Higher authority requires higher Scrivener rank, peer review, institutional certification, or Synod authorization as appropriate.

---

*End of Item Creation. Next section: The Housing Architecture.*
