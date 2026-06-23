# THE ÆTHERIUM CODEX — System Reference Document
## Section: Item Creation — The Crafting System

*Alpha SRD Draft — Working Document*

---

### PREAMBLE

Item creation is the intersection of physical fabrication and alchemical manipulation. A crafter shapes matter and directs planar expressions simultaneously. Every crafting operation involves two categories of work performed in parallel: physical operations that change the material's form, and alchemical operations that change the material's composition. Both happen within the same weekly workflow, abstracted into a single Artifice check that represents the total effort applied to the project that week.

---

## PART I: THE TWO CATEGORIES OF OPERATION

### Physical Operations

Physical operations change the material's form without changing its chemical or alchemical composition. The iron is still iron after you forge it into a blade. The wood is still wood after you carve it into a staff.

| Operation | What It Does | Common Conditions Involved |
|---|---|---|
| **Shaping** | Forming raw material into a desired geometry through deformation — forging, hammering, pressing, bending | Temperature, Mechanical Force, Geometry |
| **Cutting** | Removing material to create geometry — carving, sawing, knapping, chiseling | Mechanical Force, Geometry |
| **Grinding** | Removing material through abrasion — sharpening, polishing, sanding, lapping | Geometry, Mechanical Force |
| **Joining** | Connecting separate pieces — welding, riveting, mortise and tenon, gluing, sewing, binding | Temperature (for welding), Geometry, Timing (for adhesives), Moisture (for glues) |
| **Finishing** | Surface treatment for protection or aesthetics — oiling, lacquering, glazing, burnishing | Medium, Timing, Moisture |
| **Assembly** | Combining finished sub-components into a complete item — mounting a blade in a hilt, setting a gem, stringing a bow | Geometry, Sequence |

Physical operations are the domain of the **Mundane Artisan** path. Their difficulty is driven by the material's physical properties — hardness determines how hard it is to shape, the Brittle flag means it fractures under impact rather than deforming, Malleable materials accept shaping readily.

### Alchemical Operations

Alchemical operations change the material's composition — its chemical structure, its planar expressions, or both. These are the three fundamental operations established in the Prima Materia framework, applied using magically-active reagents that interact with the target material on both the physical and alchemical axes simultaneously.

| Operation | What It Does | Common Conditions Involved |
|---|---|---|
| **Synthesis** | Combining two or more substances or expressions to produce a new combined state — smelting, alloying, introducing a mutation, combining reagents | Temperature, Atmosphere, Reagent Ratio, Reagent Physical Compatibility, Reagent Alchemical Compatibility, Timing, Containment |
| **Decomposition** | Breaking a combined state into simpler constituents — stripping a mutation, separating an alloy, distilling a compound, purification through removal of impurities | Temperature, Pressure, Medium, Reagent Ratio, Collection Medium, Stabilization, Timing |
| **Displacement** | Replacing one constituent with another — swapping a mutation for a different one, replacing one alchemical expression with a stronger one | Reagent Ratio, Reagent Physical Compatibility, Reagent Alchemical Compatibility, Planar Balance, Collection Medium, Stabilization |

Alchemical operations are the domain of the **Alchemist** path. Their difficulty is driven by the number and nature of conditions that must be simultaneously maintained, the tolerance width of each condition, and the dual-axis matching problem — the reagent must physically survive the processing conditions AND carry the correct alchemical profile.

### The Dual-Axis Reagent Matching Principle

Every alchemical operation requires reagents that satisfy two requirements simultaneously:

**Physical axis:** The reagent must physically participate in the processing conditions. A liquid reagent is useless in a high-temperature glass remelt — it evaporates before it can interact. The reagent's physical carrier must survive and function within the operation's physical environment.

**Alchemical axis:** The reagent must carry the correct planar profile to interact with the target expression. A thermally stable mineral powder is useless for extracting a Verdant Font mutation if it carries no alchemical signature that interacts with Verdant Font expressions.

The intersection of valid physical carriers and valid alchemical profiles may be a short list for any given operation. The master alchemist's expertise is knowing which materials sit at that intersection. The alchemist's reagent collection is indexed by both periodic tables simultaneously — real properties on one axis, planar profiles on the other.

### Combined Operations

Most crafting projects involve both physical and alchemical operations across their duration. A steel longsword requires smelting (alchemical — synthesis of iron and carbon), forging (physical — shaping), tempering (combined — physical thermal process creating an alchemical arrested heritage state), sharpening (physical — grinding), assembly (physical — joining blade to hilt), and potentially mutation introduction (alchemical — synthesis) and attachment treatment (alchemical — surface application).

The weekly Artifice check abstracts whatever combination of operations the crafter is performing that week. The crafter declares their intended work for the week. The GM determines which conditions apply based on the declared operations. The TN is calculated from those conditions. One roll covers the week's effort.

---

## PART II: TARGET NUMBER CONSTRUCTION

The Target Number for a crafting check is built from two concrete variables: the number of simultaneous conditions the crafter must maintain, and how narrow the acceptable range is for each condition.

### Base Formula

**Crafting TN = 10 + Conditions Modifier + Tolerance Modifier**

### The 19 Crafting Conditions

Each applicable condition contributes to the Conditions Modifier. The crafter and GM identify which conditions are active for the declared operation.

**Physical Conditions:**

| # | Condition | Description |
|---|---|---|
| 1 | **Temperature** | Maintaining working material at correct heat. Forging, smelting, glass work, firing, tempering. Can be a range or a precise point. |
| 2 | **Mechanical Force** | Applying physical shaping pressure. Hammering, pressing, drawing, rolling. Direction, intensity, and rhythm all relevant. |
| 3 | **Atmosphere** | Controlling the air/gas environment. Sealed crucibles, reducing atmospheres, inert gas environments. Ranges from open air to specific gas mixtures. |
| 4 | **Pressure** | Environmental compression or vacuum. Hydraulic pressing, steam containment, vacuum distillation. Distinct from Mechanical Force — this is ambient, not directed. |
| 5 | **Timing** | Operations requiring specific duration or moment. Quench timing, reaction duration, cooling rate control. Can be a window or a sustained duration. |
| 6 | **Geometry** | Maintaining specific dimensions, angles, or shapes. Blade taper, edge angle, wall thickness, joint alignment. Ranges from rough to precise. |
| 7 | **Medium** | The substance the work is performed in or through. Quench medium, solvent choice, flux selection. The medium participates in the process but is not the workpiece. |
| 8 | **Moisture** | Water content control. Drying wood, controlling humidity, preventing oxidation. Some processes require moisture; others require its absence. |

**Alchemical Conditions:**

| # | Condition | Description |
|---|---|---|
| 9 | **Reagent Ratio** | Proportion of reagent to target material. Too little: incomplete reaction. Too much: side reactions or waste. |
| 10 | **Reagent Physical Compatibility** | The reagent must physically survive and participate in the processing conditions. First axis of dual-axis matching. |
| 11 | **Reagent Alchemical Compatibility** | The reagent must carry the correct planar profile for the target expression. Second axis of dual-axis matching. |
| 12 | **Planar Balance** | Relative intensity of two or more planar expressions being combined. Too much of one constituent and it dominates. Relevant to catalyzed diagonals and emulsions. |
| 13 | **Catalyst Maintenance** | Sustaining the Forge catalyst throughout the operation. If it fails mid-process, competing or antithetical expressions contact directly. |
| 14 | **Collection Medium** | Prepared vessel or substrate for receiving separated or extracted expressions. Must be compatible with what's being collected. |
| 15 | **Stabilization** | Holding a newly created or separated expression in its intended state until it locks. Fresh compounds, new mutations, extracted distillates all require this. |
| 16 | **Containment** | Preventing the process from escaping its intended boundaries. Volatile materials, energetic reactions, projecting expressions, toxic processes. |

**Process Conditions:**

| # | Condition | Description |
|---|---|---|
| 17 | **Sequence** | Operations that must happen in a specific order. Some sequences are flexible; others are rigid. Violation produces wrong results or dangerous intermediates. |
| 18 | **Purity** | Workspace, tools, and inputs must be free of specific contaminants. Cross-contamination, environmental dust, biological contamination. Relevant to high-Formation-Stage and sensitive alchemical work. |
| 19 | **Continuity** | The process cannot be interrupted once started. Some operations must run to completion or they produce dangerous intermediates. Distinct from Timing — this is unbroken attention, not specific duration. |

### Conditions Modifier

| Active Conditions | Modifier |
|---|---|
| 1-2 conditions | +2 |
| 3-4 conditions | +4 |
| 5-6 conditions | +6 |
| 7+ conditions | +8 |

### Tolerance Modifier

Tolerance measures how much each condition can deviate before the operation fails or produces an unintended result. The GM assesses the overall tolerance width based on the nature of the operation.

| Tolerance | Description | Modifier |
|---|---|---|
| **Wide** | Significant deviation still produces a usable result. Cooperative combinations, simple physical shaping, forgiving processes. | +0 |
| **Moderate** | Meaningful deviation produces noticeable quality loss or minor side effects. Standard professional work, natural combinations with some precision required. | +2 |
| **Narrow** | Small deviation produces failure or unintended results. Catalyzed diagonals, high-precision physical work, sensitive alchemical operations. | +4 |
| **Razor** | Almost no margin for error. The system actively resists the intended outcome. Emulsion synthesis, antithetical combination, working at the extreme limits of material capability. | +6 |

### TN Examples

| Operation | Conditions | Tolerance | TN |
|---|---|---|---|
| Shaping iron into a blade | Temperature, Mechanical Force, Geometry (3) | Wide | 10 + 4 + 0 = **14** |
| Smelting ore to clean iron | Temperature, Atmosphere, Medium, Timing (4) | Moderate | 10 + 4 + 2 = **16** |
| Tempering steel (arrested state) | Temperature, Timing, Medium, Sequence (4) | Narrow | 10 + 4 + 4 = **18** |
| Cooperative alchemical synthesis | Temperature, Reagent Ratio, Reagent Phys., Reagent Alch., Stabilization (5) | Moderate | 10 + 6 + 2 = **18** |
| Catalyzed diagonal synthesis | Temperature, Reagent Ratio, Reagent Phys., Reagent Alch., Planar Balance, Catalyst Maintenance, Containment (7) | Narrow | 10 + 8 + 4 = **22** |
| Mutation extraction (dual-axis) | Reagent Ratio, Reagent Phys., Reagent Alch., Collection Medium, Stabilization, Containment (6) | Narrow | 10 + 6 + 4 = **20** |
| Emulsion synthesis | Temperature, Reagent Ratio, Reagent Phys., Reagent Alch., Planar Balance, Catalyst Maintenance, Containment, Stabilization, Purity, Continuity (10) | Razor | 10 + 8 + 6 = **24** |

### TN Modification by Schematics

Schematics reduce the TN by reducing the effective complexity of the operation. A schematic maps conditions and their acceptable ranges in advance, eliminating the discovery phase and documenting failure recovery. This is not a bonus to the practitioner — it is a reduction in the operation's inherent difficulty through documented knowledge.

| Authority Level | What It Provides | TN Reduction |
|---|---|---|
| **Practitioner** | The author's own documented process. Some conditions mapped, some tolerances identified. Limited failure recovery notes. Usable by the author and personally trained apprentices. | Reduces conditions band by 1 step (e.g., 5-6 → 3-4 = −2 TN) |
| **Guild Standard** | Peer-reviewed across multiple practitioners. Most conditions mapped, tolerances well-documented. Common failure recovery included. Usable by any Guild-certified practitioner. | Reduces conditions band by 1 step AND tolerance band by 1 step (−4 TN) |
| **Institutional** | Rigorously tested with controlled variables across many practitioners. All significant conditions mapped, tolerances precisely documented. Comprehensive failure recovery. Carries legal weight for product certification. | Reduces conditions band by 2 steps AND tolerance band by 1 step (−6 TN) |
| **Archival** | The definitive record. All conditions mapped, all tolerances documented, all failure modes cataloged. Reduces the operation to minimum possible complexity — what remains is purely execution. Sealed by the Synod Sepulchral as permanent record. Cannot be altered. | Reduces conditions band by 2 steps AND tolerance band by 2 steps (−8 TN) |

**Schematic Example:** An emulsion synthesis (TN 24) with a Guild Standard schematic:
- Base: 10 + 8 (7+ conditions) + 6 (razor tolerance) = 24
- Guild reduces conditions by 1 step: 7+ → 5-6 = +6 instead of +8
- Guild reduces tolerance by 1 step: razor → narrow = +4 instead of +6
- New TN: 10 + 6 + 4 = **20**

The operation is still complex and demanding, but documented knowledge has removed the most dangerous uncertainty.

---

## PART III: THE CRAFTING CHECK

### The Roll

**Artifice Check = d20 + (Artifice Rank × 2) + Relevant Attribute Bonus + Modifiers**

The relevant attribute depends on the operation being performed. Intellect for most alchemical work. Finesse for precision physical work. Wits for reactive decision-making during volatile processes. The GM determines which attribute applies based on the declared operation.

### Modifier Types

All modifiers fall into defined types. Modifiers of the **same type** do not stack — take the highest. Modifiers of **different types** always stack.

| Type | Stacks with itself? | What It Represents | Examples |
|---|---|---|---|
| **Competence** | No | Skill, training, specific expertise | Specialized training tradition, focused study, practiced technique |
| **Enhancement** | No | Magical amplification of existing qualities | Spells boosting attributes, enchanted tools, temporary magical augmentation. Subject to character boost caps (+2 temporary, +4 combined). |
| **Alchemical** | No | Applied alchemical preparations | Tinctures applied to tools, treated work surfaces, preparatory compounds applied to the practitioner |
| **Infrastructure** | No | Having the right tools for the job | Quality of tools, specialized equipment, workshop capabilities. Applies wherever a prepared tool is used for a task — crafting, combat, investigation, medicine. |
| **Insight** | No | Perfect information or analytical advantage | Analyzer readings, divination revealing hidden material properties, prior knowledge of the specific sample being worked |
| **Collaborative** | Special | Another practitioner contributing distinct expertise | See Collaborative Crafting rules below |
| **Circumstance** | Yes | Situational conditions at the point of work | Favorable environment, planar bleed alignment, unhurried pace, good lighting. Multiple distinct circumstances each contribute. |
| **Luck** | Yes | Probability manipulation, divine favor, Palimpsest influence | Supernatural fortune. Multiple distinct Luck sources accumulate. |

### Hazard Penalties

These are not modifier types. They are measured material properties (rated 1-10) that impose penalties on the roll unless mitigated.

**Volatility (1-10):** The material's tendency to change state, release energy, or behave unpredictably under working conditions. Penalty applied directly to the roll. Mitigated by appropriate containment infrastructure — proper containment reduces the effective Volatility rating. Full containment eliminates the penalty.

**Toxicity (1-10):** The material's biological hazard to the practitioner through exposure. Penalty applied directly to the roll and represents the practitioner's impaired ability to work freely while managing exposure risk. Mitigated by protective measures — sealed work environments, alchemical treatments, magical shielding. Full protection eliminates the penalty. Toxicity is NOT mitigated by crafting skill — a master alchemist working with mercury is still endangered by mercury.

Volatility and Toxicity are independent. A material can be highly volatile but non-toxic (nitroglycerin), highly toxic but stable (lead), both (white phosphorus), or neither (gold).

### Collaborative Crafting

When multiple practitioners contribute to the same project, each fills a distinct role managing specific conditions within the operation. The number of assistants who can meaningfully contribute is limited by the operation's complexity.

| Operation Complexity | Maximum Assistants |
|---|---|
| 1-2 conditions | 0 (too simple to subdivide) |
| 3-4 conditions | 1 |
| 5-6 conditions | 2 |
| 7+ conditions | 3 |

Each assistant makes their own check using their relevant skill and attribute against the same TN. On success, they contribute a **Collaborative** modifier to the primary crafter's check equal to half their Artifice Rank (rounded down, minimum +1). On failure, they contribute nothing (they didn't manage their assigned conditions, but they didn't make things worse). On critical failure, they impose a −2 penalty to the primary crafter's check — they actively disrupted the process.

Collaborative modifiers from different assistants stack with each other (each assistant is filling a distinct role), but multiple assistants cannot be assigned to the same condition.

For projects of sufficient scale — construction of buildings, ships, siege engines, or legendary artifacts — the work may be broken into discrete sub-projects, each with its own complexity, TN, and team. There is no theoretical cap on the number of practitioners contributing to a project of this scale, only on the number contributing to any single operation within it.

---

## PART IV: THE FIVE OUTCOME STATES

Compare the Artifice Check result to the Crafting TN. The degree of success determines the outcome state, which determines progress, events, and consequences.

| Result | Outcome State | PV Progress | Event |
|---|---|---|---|
| TN+10 or higher, OR natural 20 | **Critical Success** | Double normal progress | Major benefit, no flaw |
| TN to TN+9 | **Success** | Normal progress | Minor benefit, no flaw |
| TN−1 to TN−4 | **Success with Flaw** | Half normal progress | Minor benefit + minor flaw |
| TN−5 to TN−9 | **Failure** | No progress | Minor flaw, no benefit |
| TN−10 or lower, OR natural 1 | **Critical Failure** | Lose progress | Major flaw, no benefit |

**Normal Progress per week = (Artifice Rank × 10) + (Relevant Attribute Bonus × 5)**

### Critical Success

The process has produced an exceptional result. The crafter receives a major benefit with no associated flaw.

| Option | What Happens | Final State |
|---|---|---|
| Accept as-is | No action taken. | Major benefit. Clean. |
| Reckless overcharge | Voluntarily take a major flaw. Gain one additional major benefit. | Two major benefits + major flaw. Flaw subject to standard buyoff. |
| Minor push | Voluntarily take a minor flaw. Gain one additional minor benefit. | Major benefit + minor benefit + minor flaw. Flaw subject to standard buyoff. |

Only one voluntary addition may be taken — either reckless overcharge or minor push, not both.

### Success

The process has produced a clean result. The crafter receives a minor benefit with no flaw.

| Option | What Happens | Final State |
|---|---|---|
| Accept as-is | No action taken. | Minor benefit. Clean. |
| Overclock | Voluntarily take a minor flaw. The minor benefit upgrades to a major benefit. | Major benefit + minor flaw. Flaw subject to standard buyoff. |

### Success with Flaw

The process produced a result, but not a clean one. The item has both a minor benefit and a minor flaw simultaneously.

| Option | What Happens | Final State |
|---|---|---|
| Accept as-is | No action taken. | Minor benefit + minor flaw. Flaw subject to standard buyoff. |
| Escalate | Upgrade the minor flaw to major flaw. The minor benefit upgrades to major benefit automatically. | Major benefit + major flaw. Flaw subject to standard buyoff. |
| Sublimate | Cancel both the benefit and flaw entirely. Neither carried forward. | Net zero. No benefit, no flaw. The week was spent but cleanly. |

### Failure

The process fell short. The item accrues a minor flaw. No benefits.

| Option | What Happens | Final State |
|---|---|---|
| Full buyoff | 1 extra week OR 1 minor success + 12% of acquisition cost in materials | Minor flaw fully removed. |
| Accept | No action. | Minor flaw remains at completion. |

### Critical Failure

The process has gone significantly wrong. The item accrues a major flaw. No benefits.

| Option | Cost | Result |
|---|---|---|
| Full buyoff | 2 extra weeks OR 2 minor successes OR 1 major success + 25% acquisition cost | Major flaw fully removed. |
| Downgrade to minor | 1 extra week + 12% acquisition cost | Major flaw reduced to minor flaw. Minor flaw then subject to its own buyoff terms. |
| Accept | None | Major flaw remains at completion. |

### Buyoff Rules

All flaws at all states are subject to buyoff. No flaw is permanent unless the crafter chooses not to address it. Buyoff weeks carry no risk — no dice are rolled, no new outcomes are generated, no new flaws can accrue during buyoff work.

| Flaw Tier | Time Cost | Material Cost | Success Trade |
|---|---|---|---|
| Minor Flaw | 1 extra week | 12% of acquisition cost | 1 minor success from any future roll |
| Major Flaw | 2 extra weeks | 25% of acquisition cost | 2 minor successes OR 1 major success from future roll(s) |

**Non-Consecutive Application:** Future roll results and extra time do not need to be applied immediately or in sequence. A major flaw accrued in week one can be bought off with a critical success result earned in week seven. Time-based and success-based buyoff can be mixed. The crafting ledger remains open until the item is declared complete.

**Applying Future Successes:** A future roll result that would generate a benefit can instead be applied against an existing flaw in the crafting ledger. The benefit is consumed — it does not also apply to the current week's item. The applied result must match or exceed the flaw tier.

---

## PART V: BENEFITS AND FLAWS — CRAFTING MUTATIONS

Benefits and flaws produced during crafting are mutations in the item's expression — the same Adaptive lane logic that governs biological mutation in characters applies to objects. A flaw on a crafted item is a minor or major mutation in the item's planar expression, induced by the conditions of its creation. A benefit is the same — a positive mutation emerging from the crafting process.

All crafting mutations follow the same rules as any other mutation. They are part of the item's combined state. They contribute to the item's effective properties. They can potentially be addressed through alchemical operations (decomposition to strip, displacement to swap) if the crafter has the skill and reagents to do so — though this is a separate operation from the buyoff system and carries its own risks.

### Minor Benefits (Lesser Positive Mutations)

The following categories represent the types of positive mutations that can emerge during crafting. The specific mutation is determined by the GM and crafter based on what the item is, what materials are involved, and what operation was being performed when the benefit emerged.

**Cost Reduction**
- Channeling: Reduce Stamina/ÆP cost of item abilities by half EML.
- Resourceful Process: Reduce material cost for future maintenance by 10%.

**Combat Enhancement**
- Defensive Training: +EML bonus to perform and defend against a specific combat maneuver (disarm, trip, grapple, etc.).
- Vicious Edge: Increase critical threat range by 2. Apply damage-type-specific effects on critical hits.
- Foe-Specific: +1d6 damage per 2 EML against a specific creature type.
- Piercing Strikes: Ignore Soak equal to half EML.

**Action Economy**
- Rapid Action: A specific item action (deployment, reload, donning) becomes a free action.
- Swift Response: Change a standard action to a move action, or a move to a swift.

**Influence**
- Forceful Presence: +EML to Influence checks when item is visible.
- Soothing Presence: +half EML to fear resistance and animal calming.

**Duration & Range**
- Extended Duration: Item effects last 50% longer.
- Greater Reach: Item effect range increased by 25%.

**Awareness**
- Guardian Awareness: +half EML to perception against surprise.
- Mnemonic Aid: +EML bonus once per day on Lore checks.

**Durability**
- Perfected Form: Immune to Brittle/Fragile conditions.
- Reinforced Structure: +EML to item's Physical condition track.

**Elemental**
- Elemental Attunement: +EML damage of aligned type. Apply associated rider effect on critical hits.

**Resource Storage**
- Reservoir: Store EML points of Stamina/ÆP. Regenerate half EML per 10 minutes (standard drip rate).

### Minor Flaws (Lesser Negative Mutations)

**Burden**
- Awkward Design: −half EML penalty on a specific skill sphere when item is equipped.
- Excessive Weight: Item weighs two size categories more than expected.

**Cost Increase**
- Hungry: Increase Stamina/ÆP cost of item abilities by half EML.
- Leeching: Double the cost of item abilities.

**Durability**
- Brittle Expression: Reduce item Hardness by half EML.
- Fragile Structure: Reduce item Hardness by full EML.

**Identification**
- Faint Aura: +EML to the TN required to identify the item's magical properties.

**Sympathetic Damage**
- Minor Feedback: Wielder takes 25% of damage dealt to the item's condition track as metaphysical backlash.
- Major Feedback: Wielder takes 50% of damage dealt to the item's condition track as metaphysical backlash.

**Planar Dissonance**
- Minor Dissonance: −half EML on metaphysical defense checks for wielders whose planar profile is not aligned with the item.
- Major Dissonance: −full EML on metaphysical defense checks for non-aligned wielders.

**Maintenance**
- Demanding: −1 cumulative penalty per encounter without maintenance (max −5). Reset by spending 10 minutes on upkeep.
- Ravenous: −1 cumulative penalty per encounter (max −10). Reset requires full maintenance session.

**Resource Drain**
- Minor Thirst: Drain half EML Stamina/ÆP per day from wielder.
- Major Thirst: Drain full EML Stamina/ÆP per day from wielder.

### Major Benefits (Greater Positive Mutations — Breakthrough Exclusive)

These mutations only emerge from Critical Success results. They represent exceptional outcomes where the material's nature cooperated perfectly with the crafter's intent.

- **Font:** Reduce Stamina/ÆP cost of all item abilities by full EML. Can reach 0.
- **Effortless Invocation:** Item abilities at EML 1-4 can be activated at no cost.
- **Greater Reservoir:** Store EML × 2 points of Stamina/ÆP. Same regeneration rate as standard reservoir.
- **Damage Immunity:** Complete immunity to one chosen damage type.
- **Elemental Fury:** +EML × 2 elemental damage. Apply associated rider effect on every hit.
- **Executioner's Mark:** Critical hits cause target to become vulnerable to the item's damage type for EML rounds.
- **Critical Immunity (Armor):** Immune to critical hits.
- **Impenetrable Ward (Armor/Shield):** Reduce all incoming damage by EML.

### Major Flaws

Major flaws are severe mutations that significantly impact the item's function. They always have buyoff paths available.

Major flaws are generated by inverting or intensifying the categories from the Minor Flaw list. A Minor Brittle Expression (−half EML Hardness) becomes a Major Structural Failure (−full EML Hardness AND the item's Physical condition track is reduced by half). A Minor Feedback (25% sympathetic damage) becomes a Major Resonant Wound (50% sympathetic damage AND the feedback targets the wielder's Mental condition track).

The specific major flaw should reflect what went wrong during the process — a failed alchemical synthesis might produce a Major Planar Dissonance, while a failed physical shaping operation might produce a Major Structural Failure.

*Note: The mutation tables above are adapted from the V11.4 Artifice & Materia document. Terminology has been updated to reflect current system vocabulary (Soak for Damage Reduction, condition tracks for HP, EML scaling for level-dependent values). Further review is flagged to ensure all references use current system language and mechanics consistently.*

---

## PART VI: PROGRESS VALUE

Progress Value (PV) is the total complexity and time investment required to complete a crafting project. It is a direct measure of "how many weeks of work at standard output does this project require."

### PV Formula

**PV = Base Value × Size Multiplier × Quality Multiplier**

| Item Category | Base Value | Examples |
|---|---|---|
| Simple Mundane | 50 | Wooden staff, basic tools, simple clothes |
| Simple Weapon/Tool | 100 | Dagger, club, leather armor |
| Martial Weapon/Armor | 200 | Longsword, chainmail, heavy shield |
| Complex Weapon/Armor | 400 | Full plate armor, composite bow |
| Intricate Device | 600+ | Clockwork mechanisms, complex alchemical apparatus |

| Size | Multiplier |
|---|---|
| Tiny / Large | ×0.75 |
| Small / Medium | ×1.0 |
| Diminutive / Huge | ×1.5 |
| Fine / Colossal | ×2.0 |

| Quality | Multiplier | Description |
|---|---|---|
| Standard | ×0.5 | Mass-produced, functional, common. Quick to make, expected to be replaced. |
| Masterwork | ×1.0 | Refined, balanced, reliable. The baseline for adventuring equipment. Foundation for magical work. |

**Additional PV for Alchemical Operations:**

Each alchemical operation performed on the item during creation adds PV based on the operation's complexity:

| Operation Complexity (TN Band) | Additional PV |
|---|---|
| Simple (TN 14-15) | +50 PV |
| Standard (TN 16-18) | +100 PV |
| Complex (TN 19-22) | +250 PV |
| Expert (TN 23-26) | +500 PV |
| Master (TN 27+) | +1000 PV |

This means a Masterwork longsword (400 PV base) with a catalyzed diagonal synthesis (TN 22, +250 PV) has a total PV of 650.

### Weeks to Completion

**Weeks = Total PV ÷ Weekly Progress**

**Weekly Progress = (Artifice Rank × 10) + (Relevant Attribute Bonus × 5)**

| Band | Typical Progress/Week | 400 PV Item | 900 PV Item |
|---|---|---|---|
| Novice (Rank 3, Attr 2) | 40 PV/week | 10 weeks | 23 weeks |
| Journeyman (Rank 5, Attr 3) | 65 PV/week | ~6 weeks | ~14 weeks |
| Master (Rank 8, Attr 4) | 100 PV/week | 4 weeks | 9 weeks |

---

## PART VII: THE ITEM CONDITION TRACK

Every item possesses a condition track across each of the four pillars: Physical, Mental, Social, and Metaphysical. The condition track uses the same five-state progression and applies universally to all items — mundane and magical alike.

### The Four Pillar Condition Tracks

**Physical Condition** — The material integrity of the item. Rust, cracks, chips, edge degradation, structural fatigue. The state of the physical substance.

- Pristine: The item functions exactly as designed. No material degradation.
- Worn: Minor surface degradation. Functional but showing use. Cosmetic imperfection.
- Damaged: Meaningful structural compromise. Functional but impaired. Some capabilities reduced.
- Broken: Severe structural failure. Barely functional. Major capabilities lost or unreliable.
- Destroyed: The material has reached its final state. The item cannot function as designed. Physical reconstruction requires new materials at full PV.

**Mental Condition** — The item's information integrity. How much can be learned about it through research, analysis, or identification. How well its own nature, history, and properties are preserved as readable data.

- Pristine: The item's nature is clearly readable. Identification and analysis are straightforward. Records of its creation and history are accessible.
- Worn: Some information degraded. Identification requires effort. Minor details of history obscured.
- Damaged: Significant information lost. Identification requires specialized skill. History fragmented.
- Broken: Most information inaccessible. Only the most obvious properties are detectable. History nearly lost.
- Destroyed: The item's identity as an informational object is gone. No analysis can recover what it was. Only physical examination of the remains is possible.

The Mental condition track is the target for research and investigation. Contested Mental checks against the item whittle down its Mental condition — not to damage it, but to extract information from it. Each successful check reveals more about the item until the investigator has "solved" it. This is the same mechanic used for puzzles and contagion research — progressive revelation through contested checks.

**Social Condition** — The item's legend and reputation. How well-known it is, what cultural weight it carries, what reactions it provokes in those who recognize it.

- Pristine: The item is famous. People recognize it and respond — with reverence, fear, desire, or respect. Its name carries power. Influence checks involving the item gain significant benefit.
- Worn: The item is known in certain circles. Recognition is not automatic but knowledgeable individuals respond to it.
- Damaged: The item is obscure. Few know of it. Its history is largely forgotten. It carries little social weight.
- Broken: The item is unknown. No one recognizes it or responds to it. It is socially inert.
- Destroyed: The item's social identity has been erased. Even those who once knew it have forgotten. Any legend associated with it has been lost.

The Social condition track grows through the Legacy system. As an item accumulates AP through significant use, its Social condition improves — it develops a story, a reputation, a legend. A newly forged sword with no history starts at Social Broken or Damaged regardless of its physical quality. A legendary blade wielded by heroes for generations is Social Pristine.

**Metaphysical Condition** — The stability of the item's planar expressions. How well its mutations, enchantments, and magical architecture are functioning.

- Pristine: All expressions functioning as designed. Mutations stable, enchantments at full output, Forge mediation holding.
- Worn: Minor planar instability. Expressions functional but occasionally inconsistent. Catalyzed states may flicker.
- Damaged: Meaningful planar degradation. Some expressions weakened or intermittent. Catalyzed states under stress. Enchantments losing efficiency.
- Broken: Severe planar instability. Most expressions unreliable. Catalyzed states failing. Enchantments may activate erratically or not at all.
- Destroyed: All planar coherence lost. Mutations may have reverted or annihilated. Enchantments gone. The item is metaphysically inert. Recovery requires complete re-enchantment.

The Metaphysical condition track is where the Synod's ongoing claim expresses most directly. The Synod constantly pushes all planar expressions toward their most stable endpoint. Maintenance — the practitioner's periodic Forge work to sustain the item's mediated states — is what holds the Metaphysical track at Pristine or Worn. Without maintenance, catalyzed diagonals and emulsions degrade first (they require the most sustained input), followed by standard mutations, and finally the base material's own heritage expression.

### Damage Distribution

When an item takes undirected damage (a sword struck against stone, armor hit by a weapon, an item dropped from height), the damage distributes across all parts proportionally based on the proportion each part occupies relative to the whole.

When a specific part is targeted (a called shot against the grip, a Nullify effect targeting the enchantment, acid applied to the blade surface), the damage applies directly to the targeted layer or component.

### Repair

Repair follows the same logic as crafting — physical damage requires physical operations, metaphysical damage requires alchemical or enchantment operations. The practitioner makes Artifice checks against the appropriate TN. The cost in PV and materials scales with the severity of damage:

| Condition | Repair PV | Material Cost |
|---|---|---|
| Worn → Pristine | 10% of original PV | Maintenance materials only |
| Damaged → Worn | 25% of original PV | 12% of original acquisition cost |
| Broken → Damaged | 50% of original PV | 25% of original acquisition cost |
| Destroyed → Broken | Not possible through standard repair — requires reconstruction at full PV with new materials. The Synod Sepulchral can recover the item's record for reference during reconstruction. |

---

## PART VIII: SCHEMATICS

A Schematic is a documented crafting procedure that makes a process reproducible. It is the Ætheric Scrivener's primary output and every other Artifice Path's most valuable tool.

### What a Schematic Contains

**A conditions map.** Which of the 19 conditions apply to the specific operation, and what the acceptable ranges are for each. "Temperature must be between 1100-1200°C. Atmosphere must be reducing. Quench in oil, not water. Timing is 4 seconds."

**A sequence record.** The order of operations, including which steps are flexible and which are rigid. "Apply flux before introducing the reagent. The reagent must be added within 30 seconds of reaching target temperature."

**A failure map.** What goes wrong when specific conditions deviate, and what the recovery options are. "If temperature drops below 1100°C, crystalline structure becomes brittle. If quench is too rapid, surface cracking occurs. Surface cracking can be corrected by re-heating to 800°C and re-quenching at slower rate."

**Reproducibility documentation.** The isolation of critical variables that turns a one-time success into a reliable process.

### Authority Levels

| Level | Who Can Use | TN Reduction | Variance Control | Recognition |
|---|---|---|---|---|
| **Practitioner** | The author + personally trained apprentices | −2 (conditions reduced 1 step) | Some conditions mapped. Basic failure notes. | None — personal knowledge only |
| **Guild Standard** | Any Guild-certified practitioner | −4 (conditions 1 step + tolerance 1 step) | Most conditions mapped. Tolerances documented. Common failure recovery. | Guild recognition. Legally binding for product certification. |
| **Institutional** | Any practitioner holding institutional certification | −6 (conditions 2 steps + tolerance 1 step) | All significant conditions mapped. Precise tolerances. Comprehensive failure recovery. | Institutional recognition. Quality guarantee carries legal weight. |
| **Archival** | Any practitioner with archive access and clearance | −8 (conditions 2 steps + tolerance 2 steps) | All conditions mapped. All tolerances documented. All failure modes cataloged. Maximum possible complexity reduction. | Synod Sepulchral seal. Cannot be altered. Historical fact in legal proceedings. |

### Creating a Schematic

Schematics are created by the Ætheric Scrivener path. The process requires:

- Successful completion of the operation being documented (you must have done it at least once)
- PV investment: 500 + (100 × Item PV ÷ 1,000), rounded up
- Creation time: 1 week per 1,000 PV of the documented item
- Materials: Documentation medium appropriate to the setting (vellum, metal plate, printed specification sheet)

Higher authority levels require additional investment:
- **Guild Standard:** Requires Journeyman Scrivener rank minimum. Must be reviewed and validated by a Guild assessor.
- **Institutional:** Requires Master Scrivener rank. Must be tested across multiple practitioners under controlled conditions. Institutional certification required.
- **Archival:** Requires Master Scrivener Rank 10+. Must be sealed by Synod Sepulchral authority. The schematic becomes a permanent, unalterable record.

---

*End of Item Creation section. Next section: Staves — The Housing Architecture.*
