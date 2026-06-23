# ÆTHERIUM CODEX — Item Creation Reader Guide: Concept Extraction
## Extracted from: ÆC Item Creation Reader Guide 1.md (16 MB, 186,671 lines)
## Extraction Date: April 29, 2026

**Source disposition:** The original 16 MB file is a concatenated mega-document. 98% is templated enumeration data (isotope combination matrices, political alloy permutations). This extraction contains the ~2% unique concept payload — all design decisions, mechanical specifications, and analytical frameworks not captured elsewhere.

**Sections in this extraction:**
1. **Reader Guide (Parts I–VII)** — Complete player-facing crafting manual (lines 1–777)
2. **80-Isotope Card Set** — Five planes × 16 isotopes in card format with Tier Scaling (lines 778–1944)
3. **Forge as Emulsifier** — Complete catalyst-specified emulsion reference + analytical notes (lines 85020–85952)
4. **Political Alloy System Index** — Three-slot formula, complete menus, canonical Zoetrope positions (lines 182603–182808)

**Known conflicts with project knowledge (from Investigation Handoff):**
- C-1: Six Artifice Paths listed here vs five locked in SRD v3 (Analyzer split from Appraiser)
- C-2: Tier 12+ materials (SRD v3 caps at 10)
- C-3: Echo-Heart Battery (4th type, Palimpsest-sourced — SRD v3 lists 3)
- C-4: Crafting attribute "Intellect" vs canonical "Wits"
- C-5: Volatility Regulator as Enabling Component (not in SRD v3)
- C-6: Attunement Matrix slot economics clarification (not in SRD v3)

---
---

# How to Read This Document

### A Guide to the Ætherium Codex Item Creation System

 ---

You are holding a crafting system. Not a list of magic items — a system for making them from scratch, understanding what they are physically and cosmologically, watching them grow over the course of a campaign, and eventually turning them into something that carries the full history of everywhere they have been.

It is more involved than most crafting systems you have encountered. That is intentional. In this setting, an item is not a mechanical bundle of bonuses. It is simultaneously a physical substance, a cosmological expression, a political artifact, and a biography. This document gives you the tools to build and understand all four layers at once.

You do not need to know the setting to use this document. Everything you need is defined here.

 ---

## The Mental Model

Before you read anything else, understand the structure. Everything in this document follows four sequential steps, and the order is not arbitrary — each step builds directly on the one before it.

**Step 1** establishes what the material IS. Not just physically, but cosmologically. Where it comes from, what it naturally does, who controls access to it.

**Step 2** transforms that raw material into a shaped item. This is the crafting process itself — the dice rolls, the weekly progress, the decisions that give the item its first unique character.

**Step 3** installs the item's magical and technological components. This is where the item's power configuration is built: what effects it carries, how its power economy works, how much it can hold.

**Step 4** covers what happens after the item is finished. Over the course of a campaign, the item accumulates experience alongside its wielder, and that experience eventually changes the item in ways that no amount of money or materials can replicate.

Each step corresponds to a Part in the document. Parts II through VI map directly to Steps 1 through 4, with Part IV covering a sub-layer of Step 2 that is rich enough to deserve its own section.

 ---

## Part I — System Overview

Start here. It is short and it orients everything else.

You will find three things: the three foundational pillars that define how the system works at a structural level, the six Artifice Paths that tell you what kinds of crafting exist, and the principle that governs the entire Artifice Engine: you are a master artisan, not a dice-rolling victim. You make choices. You do not suffer mistakes.

Read the pillar table slowly. The Core Process (Layer 1) is mechanical and objective — time, materials, skill applied toward a goal. The Artifice Engine (Layer 2) is where crafting becomes interesting — events interrupt the work and force you to make decisions with real trade-offs. Item Ascension (Layer 3) is how the item grows after it exists. These three layers operate simultaneously and at different timescales. Understanding which layer you are in at any given moment is the first skill this system asks of you.

The six Artifice Paths tell you the specializations available. You do not need all six to build items. The Path of the Enchanter covers permanent magical items, which is what most of this document describes. The Path of the Alchemist handles consumables. The others are support functions. If you are new to this system, think of yourself as working the Enchanter path until you know where the others become relevant.

 ---

## Part II — Step 1: Material Identification

This is where every item begins. Before you shape anything, you need to know what you are working with.

The unusual feature of this system is the Two-Table Check. Every material is described by two different frameworks simultaneously. The real periodic table — the one that exists in the 1940s-era technology of this setting's second source world — tells you the physical properties: hardness, melting point, conductivity, chemical reactivity. The alchemical periodic table, derived from the setting's cosmology of five outer planes, tells you the material's magical identity: which plane produced it, what phase state it crystallized in, how stable it is, what it continuously radiates just by existing.

Neither table overrides the other. An acid material (from the Borderlands plane, Earth+Water forced into tension) is simultaneously a corrosive chemical with real pH characteristics AND an unstable planar expression that will try to assert its contradictory nature during shaping. Both problems are real. Both impose their own costs.

The Material Tiers table tells you what any given material can support: its Tier equals the number of magical slots available in the finished item. Tier 4 gives you four slots. Tier 10 gives you ten. This is the glass ceiling — no amount of skill or additional components can push an item's Tier above what its core material supports.

Material Grades (Flawed, Standard, Superior, Masterwork) describe the quality of a specific sample of a material, independent of its rarity. A Masterwork sample of common iron is harder to find than standard iron but dramatically easier to work with once you have it — the superior quality cooperates with the shaping process.

The Volatility table tells you how much the material's planar character will interfere with crafting. A material formed under calm, stable planar conditions (Stage 1–2) processes cooperatively. A material formed during a near-planar-breach event (Stage 5) is still actively expressing its planar identity during every step of the shaping process, adding significant difficulty to every Artifice Check.

The Political Alloy section is about access rather than material properties. Some materials are physically available in a location but institutionally restricted — controlled by one of the nine great colleges or a regional political faction. Acquiring them without proper standing requires either going through the Sovereign Exchange at premium cost, earning the credentials, or finding a way around the system entirely. The document distinguishes Physical TN (where is it, how dangerous to obtain) from Access TN (who owns it, how do I get permission). You can find a material and still not be able to take it.

The Material Sourcing as Quest Design table at the end of Part II is aimed at GMs. It maps Acquisition TN ranges to adventure lengths. If the material costs TN 10–12, a single session of roleplay probably gets you there. If it costs TN 24+, sourcing that material is a campaign arc. Use this when you want crafting to drive the story rather than sit alongside it.

 ---

## Part III — Step 2: Processing (The Core Process)

This is the Layer 1 mechanics: dice rolls, weekly progress, and the quantified difficulty of transforming raw material into a shaped item blank.

The Crafting TN formula combines everything from Step 1 into a single number you roll against each week. Your Physical Base TN comes from the real periodic table. Volatility adds on top. If your Artifice Rank is lower than the material's Tier, the Rank Penalty stacks on top of that.

The Artifice Check is the wording you roll each week: `d20 + (Artifice Rank × 2) + Intellect Bonus`. Your Normal Weekly Progress — how much you advance the project on a standard success — is `(Rank × 10) + (Intellect Bonus × 5)` PV. Progress Value is the quantified measure of how much work the project requires. A simple dagger needs about 100 PV of Masterwork work. A complex prosthetic device might need 2,550 PV. A legendary artifact could need 10,000 or more.

The Degrees of Success table tells you what happens at each outcome. Critical Success doubles your progress and triggers a Breakthrough event — good things happen. Standard Success gives normal progress and triggers a Fork in the Road — choices with trade-offs. Success with Cost gives half progress and triggers a Complication — something went wrong, you get a drawback. Failure gives nothing and triggers Stasis — a lost week. Critical Failure actually reverses progress and triggers a Setback.

The PV Formula is `(Base Value + Material Value) × Size Multiplier × Quality Multiplier`. This looks complex but it is straightforward once you run through it once. The Base Value is set by item category — a Martial Weapon is 200 PV base; an Intricate Device is 600+. The Material Value adds per archetype type: Mundane archetypes add 100 each, Elemental archetypes add 250 each, Conceptual archetypes add 500 each. The Multipliers adjust for the item's size and the quality of work you are putting in. Standard quality is ×0.5 — functional, disposable, mass-producible. Masterwork quality is ×1.0 — the baseline for adventuring equipment, what a character carries and maintains throughout a career.

The Three Material Layers explain how the physical construction of the item produces its magical architecture. The Base Component is the item's primary material — what sets its planar identity and Tier. The Additive Component is material worked into the item during construction (a grip wrapping, a pommel inlay) — it adds a secondary planar expression and produces a continuous field effect without costing any of the item's magical slots. The Innate Component is the rarest case: the item IS the magical material, rather than being made from it.

The Affinity table at the end of Part III covers a recurring strategic question: does the magical effect you want to install match the planar character of the material you are building from? If yes, the crafting is easier and the item sustains the effect without needing battery power at all. If no, the crafting is harder and the item burns battery continuously. If the material actively opposes the effect, the difficulty is highest and the drain is doubled for that component. This single table does a lot of the work for item design decisions.

 ---
## Part IV — The Artifice Engine (Layer 2)

This is the part that makes items distinctive rather than generic.

Every week of crafting, depending on your Degree of Success, one of five Artifice Events may trigger. The Breakthrough gives you a positive Mutation you can accept or decline. The Fork gives you a choice between two valid approaches with different trade-offs. The Complication forces a Lesser Negative Mutation — unless you spend extra resources to mitigate it into a Lesser Positive. The Stasis loses the week with no other consequence. The Setback loses progress.

Mutations are permanent. They are not accidents — they are the results of decisions you made during crafting. The system distinguishes Lesser and Greater versions of both Positive and Negative mutations, and allows a trade-off: you can downgrade a Greater Success to a Lesser Success by accepting a Lesser penalty, or push a Greater Success toward its full value by accepting a Greater penalty. This creates a dial you control at every event.

The worked example in this section — the Golem-Forged Arm — walks through 24 weeks of crafting week by week. You do not need to memorize it, but reading through it once gives you the rhythm of how these systems interact during actual play. You will see Breakthroughs, Complications, Stasis weeks, and a Critical Failure, and you will see how each one changed the final item rather than simply representing good or bad luck.

 ---

## Part V — Step 3: Slot Architecture

This is where you build the item's power configuration.

The core architecture is the same for every magical item regardless of type: a Core (the physical base, whose material quality determines Tier and therefore slot count), a Power Housing (the battery, which lives in its own dedicated slot and is never counted against the inset total), and Inset Slots (the configurable sockets that hold Active and Enabling Components).

Active Components are spell effects and magical properties. They consume inset slots and they count toward the EML formula. Enabling Components — things like the Attunement Matrix that makes a staff expandable, or the Volatility Regulator that reduces a difficult material's instability — also consume slots but do not affect EML.

The EML formula is the single most important mechanical formula in this section: `Highest Active CML + floor((Total Active Components − 1) ÷ 4)`. Read the example table slowly. It will show you that adding more low-level spells to a staff can push EML up even if you never increase the power of the strongest individual spell — the breadth of what the item can do contributes to how sophisticated it is. The Broad vs. Deep trade-off section unpacks the strategic implications of this.

The Battery section establishes the item's power economy. Four battery types exist. Organic batteries recharge quickly but hold little. Crystalline batteries hold a great deal but recharge slowly. Metallic batteries sit between the two. Echo-Heart batteries match Crystalline capacity with Organic recharge speed and are accordingly rare and expensive. The Drain and Recharge formulas are both in the document; the key thing to understand is that how fast your item ticks through its charges is determined by the host item's Tier, not the battery type — a Tier 10 item drains once every 24 hours per active effect; a Tier 2 item drains once every 10 minutes.

The Wand and Staff sections describe the two fundamental item architectures. Wands are closed systems — one spell, up to three add-ons, Tier 4 ceiling, fixed at creation. They are mass-producible consumer goods. Staves are open platforms — they grow, they expand, they carry the Attunement Matrix that lets you add spells post-construction. A staff is a limited spellbook that you add to over the course of a campaign. The fractal rule is simple: a Staff can hold Wands in its inset slots, but a Wand cannot hold a Staff. This prevents recursive complexity while letting you build sophisticated nested configurations.

The Carrier Effects section explains the NOUN/VERB principle as it applies to physical construction. The Core material is the NOUN — what the item IS, architecturally first, cannot be changed. The Additive Component is the VERB — how the item's nature expresses. A sword with a geological-permanence core and an electrical-storm grip wrapping IS permanence and ACTS through electricity. Compatible planes stack naturally. Antithetical combinations require a catalyst.

 ---

## Part VI — Step 4: Legacy

Everything in the previous parts was about building the item. This part is about what happens after.

The Core is the item's identity. This is the section's fundamental principle and it is worth stating clearly before you read anything else: Ascension Points (AP) belong to the Core material. If the Core survives, the legacy survives with it — you can re-spec every slot, replace every component, change the grip and the housing and the battery, and the item's accumulated history is intact. If the Core is replaced or destroyed, the AP history is gone. The analogy given elsewhere in this project is exact: the replacement rogue does not inherit the previous rogue's XP. The core is the character.

AP accumulates the same way character XP does. The same events that earn characters XP earn items AP for items that participated in those events. You and your GM both have the ability to designate which items earn AP from which events. Items that were central to an encounter earn full AP. Items present but not meaningfully engaged earn reduced AP.

The Three Legacy Tiers define what the AP actually unlocks. Unattuned (0–49 AP) is base spec — the item does what it was built to do, passively. Awakened (50–99 AP) means the item has accumulated enough experiential backing to express its planar character actively rather than passively — it wants to do what it does, and at 50 AP you can perform the first Ascension Ritual to unlock a new trait. Mastery (100+ AP) is full integration — and it is where the Emulsion slot becomes available, which is the most powerful thing an item can do.

The Legacy Trigger Skeleton defines what earns AP by breaking it into four components: Action (what the item must do), Subject (against or through what), Condition (where or when), and Scale (how much or how long). The worked example in this section — "the hero quenched the blade in the blood of a thousand fire-newts beneath the burning crystal caverns for a fortnight" — translates this legend into its mechanical skeleton and shows you that the same trigger can be fulfilled in multiple ways, with different side-effects depending on how it was done.

The Legacy Trigger Action Table is a d20 reference with twenty possible Action verbs, each shown with two examples (one Frost-themed, one Authority-themed) to demonstrate how the same mechanical action can express very different character depending on the item's identity. Use it for inspiration when designing legacy triggers, or roll on it if you need a trigger to emerge from play.

The Ascension Ritual section explains the process of spending AP to install a new trait. The critical piece is compatibility: if the proposed trait's conceptual character does not align with the item's AP history and planar identity, the ritual can fail — not because you rolled badly, but because the item's accumulated story does not support the development you are asking for. The item knows what it has been, and it cannot be talked out of that through mechanical optimization. Resolving an Aberration failure is always a narrative task: you create the story that makes the development coherent.

The three Aberration tables give you the range of possible failure (and occasional success) outcomes when using substitute components or mismatched materials. The Cosmetic table (d100) is gentle — visual and narrative effects with no mechanical impact. The Negative table (d20) imposes real costs. The Positive table (d20) triggers only on Critical Success with a substitute, and represents the rare case where an unexpected compatibility produces something better than what you planned.

 ---

## Part VII — Quick Reference

Everything is condensed here for table use.

The Item Creation Checklist runs all four steps as a numbered sequence. If you are mid-session and need to remember where you are in the process, start here.

The All Formulae block at the very end puts every mathematical formula in the system on one page, in one place, in monospace text. When you need a number and you do not remember which part of the document defines it, check here first.

 ---

## What You Are Building

When you finish working through this system for a specific item, what you have is not a stat block. It is a specification — a description of a physical object whose properties are fully derived from where it came from, who made it, what went into making it, and what the wielder has done with it since.

The code on the pommel of a finished item tells anyone who knows how to read it: which material produced it and at what formation conditions, what planar identity it carries, which civilization's stamp it wears, what the crafter chose during those twenty-something weeks of work, and what the wielder's history with it has been.

That is the system. Read it once through. Build one item. The second item will take half the time, and the tenth will feel like second nature.

 ---




**ÆTHERIUM CODEX**

**Item Creation System**

*The Four Steps from Raw Material to Legacy Artifact*

*Alpha Draft — Working Document*


# **PART I — SYSTEM OVERVIEW**
## **Three Foundational Pillars**
All item creation follows the same three-layered structure regardless of path.

|**Pillar**|**Layer**|**Purpose**|
| :- | :- | :- |
|1 — The Core Process|Component & Progress|Time, materials, and skill combined in a quantifiable pass/fail framework. Mechanical and objective.|
|2 — The Artifice Engine|Technique & Trade-offs|Interactive decision-making during creation. Unique items gain distinctive character through Artifice Events and Mutations.|
|3 — Item Ascension|Growth & Evolution|Long-term progression of permanent magical items. AP accumulates through use; Ascension Slots unlock new traits. Consumables do not qualify.|

|*PRINCIPLE: The character is a master artisan, not a dice-rolling victim. They make choices, not suffer mistakes. Negative mutations exist, but they never occur without a corresponding choice and opportunity for mitigation.*|
| :- |

## **The Six Artifice Paths**
The Artifice skill is divided into six distinct paths, each representing a specialized tradition. Each follows a three-tier progression: Novice → Journeyman → Master.

|**Path**|**Focus Domain**|**Produces**|
| :- | :- | :- |
|Path of the Mundane Artisan|Physical craftsmanship, masterwork items|Non-magical items of exceptional quality|
|Path of the Appraiser|Market analysis, provenance, rarity assessment|Economic and social valuation of items|
|Path of the Analyzer|Arcane analysis, component identification, diagnostics|Identification and deconstruction of magical properties|
|Path of the Ætheric Scrivener|Scrolls, schematics, runic wards, enchanted documents|Written and inscribed magic|
|Path of the Alchemist|Potions, elixirs, alchemical compounds, salves|Brewing and creation of consumable magic|
|Path of the Enchanter|Magic weapons, wondrous items, artifacts|Creation of permanent enchanted items|

|*Ætheric Essence is a specialized resource used by the Alchemist and Scrivener paths for consumable magic. Permanent magical items (Enchanter path) are fueled entirely by Progress Value and component quality.*|
| :- |


# **PART II — STEP 1: MATERIAL IDENTIFICATION**

|*Cross-reference both periodic tables simultaneously. Physical properties set the baseline difficulty; planar identity sets volatility, affinity, and tier potential.*|
| :- |

## **The Two-Table Check**
Every item begins with two simultaneous lookups describing the same substance from different directions.

### **Real Periodic Table — Physical Properties**
Sets the base physical behavior: hardness, melting point, conductivity, chemical reactivity, density. Setting B characters work from this table as standard institutional knowledge.

**•** Base Crafting TN — how physically difficult the material is to work

**•** Hardness and HP of the finished item

**•** Chemical interaction flags (corrosive, reactive, biologically active)

**•** Tool requirements

### **Alchemical Periodic Table — Planar Identity**
Sets the magical behavior: plane of origin, phase state, bleed-stage formation, cross-planar character, tier potential.

**•** Volatility modifier — added to Crafting TN based on formation stage

**•** Innate affinity — which effects the material sustains without battery drain

**•** Emission character — the continuous field the material radiates when installed

**•** Political ownership flags — which institutions control access

**•** Tier potential ceiling — maximum achievable Tier from this material

|*ALCHEMY AS INTERSTICE: Historical alchemy produced gunpowder, acids, and early metallurgy because it described real chemical interactions through a philosophical-symbolic lens before systematic chemistry existed to name them precisely. In Tessera, both systems operate simultaneously because both source worlds merged. The Deepguard chemist and the Setting A alchemist are reading the same substance from opposite directions. Neither is wrong. Together they are more complete than either alone.*|
| :- |

## **Material Tiers**

|**Tier**|**Slots**|**Grade**|**Crafting Rank Required**|**Examples**|
| :- | :- | :- | :- | :- |
|0|0|Mundane|1|Non-magical; cannot host insets|
|2|2|Awakened|1–2|Simple charms, hedge-wizard tools|
|4|4|Common|2–4|Standard adventuring gear; wand-grade|
|6|6|Uncommon|4–6|Superior gear; notable magical items|
|8|8|Rare|6–8|Regionally famous relics; major treasures|
|10|10|Legendary|8–10|Peak mortal craftsmanship; staff-grade|
|12+|12+|Mythic–Absolute|10+|Divine or monstrous origin; beyond mortal construction|

|*PENALTY FOR CRAFTING BEYOND RANK: If a crafter attempts to work with a material above their Artifice Rank, Crafting TN increases by +5 per rank of difference (stacking). At extreme differences, failure risks Setback effects. A crafter with Rank 4 attempting Tier 6 material: Crafting TN +10.*|
| :- |

|*CHARACTER LIMIT RULE (EDITOR NOTE): An item's EML should not exceed the wielder's Mastery Tier — not because it prevents use, but because a character wielding an item whose EML exceeds their Mastery is treated as a target for their own effects. Like a caveman trying to use a grenade.*|
| :- |

## **Material Grades**

|**Grade**|**Acquisition TN Mod**|**Crafting Modifier**|**Cost Mod**|**Effect**|
| :- | :- | :- | :- | :- |
|Flawed|−2|−2 to checks|×0.5|Damaged/incoherent sample; penalizes crafting; caps achievable Tier below potential|
|Standard|±0|±0|×1.0|Baseline; material performs as specified|
|Superior|+5|+1 to checks|×1.5|Pristine; crafting gains bonus; minor quality improvement to final item|
|Masterwork|+10|+2 to checks; −5 to final PV|×2.0|Exceptional; crafting significantly improved; named quality bonus on final item|

## **Volatility by Source**
Volatility adds to Crafting TN. A Volatility Regulator (Enabling Component, does not consume an inset slot) can reduce Volatility by its EML rating.

|**Source**|**Volatility**|**Example**|**Mitigation**|
| :- | :- | :- | :- |
|Standard mundane|0|Iron, wood, leather|None needed|
|Magically-touched naturally|+1|Items near ley lines|Basic stabilizer|
|Magically-harvested|+2|Dragon bone, fey material|Enabling Component|
|Planar-touched (weakly)|+2 to +3|Frost-infused ore|Specific material affinity|
|Planar essence (medium)|+3 to +4|Crystallized elemental|Specialized Enabling Component|
|Planar essence (pure)|+4 to +5|Raw elemental core|Specialized ritual required|
|Divine-touched|+5+|God-blessed material|Divine favor or artifact-level crafter|

|*ANTITHETICAL MATERIALS: Materials that are themselves the product of Forge catalyst (diagonal ⚙ states or Emulsion states) carry Volatility equal to the catalyst tier used, minimum +2. The material is holding a contradiction — that tension asserts during shaping.*|
| :- |

## **Material Grades and Hardness**

|**Item Type**|**Base Hardness**|**Base HP**|**Notes**|
| :- | :- | :- | :- |
|Wooden staff|5|8|Brittleness threshold at 3 HP|
|Longsword (standard steel)|8|15|Common adventuring item|
|Full plate armor (standard steel)|10|20|Typical protection baseline|
|Masterwork longsword|10|20|+2 vs. standard|
|Magical sword (EML 2)|12|22|Hardness benefits from magic|
|Magical sword (EML 4)|14|25|+2 per EML tier above 2|
|Artifact-grade (EML 8+)|18+|35+|Near-unbreakable|

|**Archetype Bonus**|**Bonus Hardness**|**Bonus HP**|
| :- | :- | :- |
|None (standard)|+0|+0|
|Single Resilience|+2|+3|
|Single Impact|+1|+2|
|Resilience + Impact|+3|+5|
|Reinforced property mutation|+2|+4|

## **Political Alloy and Acquisition**
Acquisition TN has two independent components resolved separately.

|**Component**|**Set By**|**Check**|**Failure Result**|
| :- | :- | :- | :- |
|Physical TN|Material rarity, location danger, harvesting difficulty|Exploration, Survival, or relevant skill|Material unavailable or only inferior grade|
|Access TN|Political alloy of controlling institution|Social check, credential, Sovereign Exchange purchase, or circumvention|Legal barrier — material present but not legally obtainable|

|*SUCCESS AT PHYSICAL TN WITHOUT ACCESS TN: The crafter can locate the material but cannot legally obtain it. This is an adventure scenario. The Sovereign Exchange converts access barriers into currency barriers via platform arbitrage — if the crafter can afford the premium, the institutional obstacle becomes a financial one.*|
| :- |

## **Material Sourcing as Quest Design**

|**Acquisition TN**|**Adventure Length**|**Campaign Role**|**Example**|
| :- | :- | :- | :- |
|10–12|Single session roleplay|Background detail|Common ore, nearby harvests, easily purchased materials|
|14–16|1–2 session quest|Filler arc|Regional materials — requires travel, trading contacts, hunting|
|18–20|3–5 session quest|Minor arc|Rare magical materials — legendary creature parts, planar materials|
|22–24|5–10 session arc|Major arc|Very rare — specific planar travel or legendary creature required|
|26+|10+ session campaign arc|Main plot|One-of-a-kind — dead god fragments, divine blessings, fate-tied materials|


# **PART III — STEP 2: PROCESSING (THE CORE PROCESS)**

|*Transform raw material into a shaped item. The Core Process (Layer 1) is mechanical and objective. The Artifice Engine (Layer 2) is the interactive layer where items gain distinctive character.*|
| :- |

## **Crafting TN**

|**Crafting TN = Physical Base TN + Volatility Modifier + Grade Modifier + Rank Penalty (if any)**|
| :- |

|**Factor**|**Source**|**Range**|
| :- | :- | :- |
|Physical Base TN|Real periodic table — material's physical workability|TN 10–26 (mundane to divine-touched)|
|Volatility Modifier|Alchemical table — planar formation stage|+0 (Stage 1–2) through +8 (Stage 5 Breach)|
|Grade Modifier|Sample quality|Flawed −2 / Standard ±0 / Superior +1 / Masterwork +2 (these are crafting check modifiers, not TN additions)|
|Rank Penalty|Crafter rank vs. material tier|+5 per rank of difference (stacking)|

## **The Artifice Check**

|**Artifice Check = d20 + (Artifice Rank × 2) + Intellect Bonus vs. Project TN**|
| :- |

|**Normal Weekly Progress = (Artifice Rank × 10) + (Intellect Bonus × 5) PV**|
| :- |

One Artifice Check is made per week of dedicated work. A character may work on two projects concurrently — each receives half progress. Focused crafting (one project, full progress) is the default.

## **Degrees of Success**

|**Result vs. TN**|**Degree**|**PV Completed**|**Artifice Engine Event**|
| :- | :- | :- | :- |
|+10 or higher|Critical Success|Double Normal Progress|Breakthrough — positive Mutation available|
|0 to +9|Success|Normal Progress|Fork in the Road — choice offered|
|−1 to −4|Success with Cost|Half Normal Progress|Complication — Lesser Negative Mutation (forced) or Lesser Positive (if mitigated)|
|−5 to −9|Failure|No Progress|Stasis — nothing happens, retry next week|
|−10 or lower|Critical Failure|Lose previous week's progress|Setback — go backward; may damage material or slots|

|*COMPLICATION vs. FAILURE: Complication (−1 to −4) means something went wrong but progress was made — you get a quirk as a side effect. Failure (−5 to −9) means nothing happened this week — you wasted time but nothing broke. Critical Failure (−10+) means something broke; you lose ground.*|
| :- |

## **The Progress Value (PV) Formula**

|**PV = (Base Value + Material Value) × Size Multiplier × Quality Multiplier**|
| :- |

### **Base Value by Item Category**

|**Item Category**|**Base Value**|**Examples**|
| :- | :- | :- |
|Simple Mundane|50|Wooden staff, basic tools, simple clothing|
|Simple Weapon/Tool|100|Dagger, club, leather armor|
|Martial Weapon/Armor|200|Longsword, chainmail, heavy shield|
|Complex Weapon/Armor|400|Full plate armor, composite bow|
|Intricate Device|600+|Clockwork mechanisms, siege engines, prosthetics|

### **Material Value by Archetype Type**

|**Archetype Type**|**PV Cost Per Archetype**|**Examples**|
| :- | :- | :- |
|Mundane Archetype|+100 PV|Resilience, Impact, Lightness, Velocity|
|Elemental Archetype|+250 PV|Flame, Frost, Current, Acid, Magma — any Borderlands element|
|Conceptual Archetype|+500 PV|Verdant (life), Forge (artifice), Palimpsest (fate), Synod (death)|

### **Size and Quality Multipliers**

|**Size**|**Multiplier**||**Quality**|**Multiplier**|
| :- | :- | :- | :- | :- |
|Large / Tiny|×0.75||Standard|×0.5 (mass-producible, functional, disposable)|
|Medium / Small|×1.0||Masterwork|×1.0 (signature equipment, refined, the adventuring baseline)|
|Huge / Diminutive|×1.5||||
|Colossal / Fine|×2.0||||

### **Complete PV Example**

|*Masterwork Longsword with Frost-Infused Iron + Dragon Fang: • Base Value: 200 (Martial Weapon) • Material Value: Resilience +100, Frost +250, Resilience +100, Flame +250 = 700 PV • Size Multiplier: ×1.0 (Medium) • Quality Multiplier: ×1.0 (Masterwork) • FINAL PV: (200 + 700) × 1.0 × 1.0 = 900 PV At Rank 5, Intellect +4: Normal Progress = (5×10) + (4×5) = 70 PV/week → ~13 weeks focused work.*|
| :- |

## **The Three Material Layers**

|**Layer**|**Role**|**Slot Cost**|**Key Property**|
| :- | :- | :- | :- |
|Base Component|Primary material; establishes planar identity and Tier|None — IS the core|Sets base affinity, Tier ceiling, slot count, PV requirement|
|Additive Component|Worked into item during forging (grip, pommel, inlay)|None at creation; one slot per addition post-creation|Secondary planar expression; continuous emission; no battery draw|
|Innate Component|The item IS the magical material (bone blade, crystal focus)|None — replaces Base Component|Strongest primary expression; formation conditions become origin story|

## **Affinity Advantage and Opposition**

|**Relationship**|**Crafting TN Modifier**|**Runtime Effect**|**Example**|
| :- | :- | :- | :- |
|Innate Alignment|−2 to Crafting TN|Effect operates without battery (Innate) — material sustains it|B-01 Inferno core + fire Active Component → fire is free|
|Secondary Alignment|±0|Normal drain; Efficiency Tick improves one step|B-09 Bedrock core + Current wrapping + lightning Active Component|
|Neutral|±0|Normal drain; standard Efficiency Tick|Mundane steel core + any magical effect|
|Opposition|+2 to Crafting TN|Drain increased one step; Volatility doubled for that component|B-01 Inferno core + frost Active Component|


# **PART IV — THE ARTIFICE ENGINE (LAYER 2)**

|*The interactive narrative layer. Artifice Events trigger during crafting. The crafter makes meaningful choices between trade-offs. Items gain permanent Mutations — unique quirks that shape final mechanics and flavor.*|
| :- |

## **Artifice Events**

|**Event Type**|**Trigger**|**What Happens**|
| :- | :- | :- |
|Breakthrough|Critical Success (+10 over TN)|A positive Mutation is available. The crafter may accept it or decline. Accepting costs nothing; declining loses the opportunity.|
|Fork in the Road|Success (0 to +9 over TN)|Two or more valid approaches are presented, each with clear trade-offs. The crafter chooses. Result shapes the item's character.|
|Complication|Success with Cost (−1 to −4)|Something went wrong but progress was made. A Lesser Negative Mutation is forced — OR the crafter may spend extra resources to mitigate it into a Lesser Positive.|
|Stasis|Failure (−5 to −9)|Nothing happened. The week was wasted. No mutation, no progress, no penalty beyond the lost time.|
|Setback|Critical Failure (−10+)|Progress is lost. Previous week's PV is reversed. Severe Setbacks may damage a component or a slot. No mutation.|

## **Mutation Types**

|**Category**|**Sub-type**|**Effect Scale**|
| :- | :- | :- |
|Positive|Lesser Positive|Minor bonus — +EML to a specific check, speed improvement, rider effect on a specific condition|
|Positive|Greater Positive|Significant bonus — major effect, unlocks new capability, substantial improvement to core function|
|Negative|Lesser Negative|Minor drawback — maintenance requirement, limited use condition, minor restriction|
|Negative|Greater Negative|Significant drawback — functional limitation, ongoing cost, compatibility restriction|
|Neutral|Cosmetic/Narrative|No mechanical impact. Visual trait, sound property, narrative characteristic. Always safe to take.|

|*TRADE-OFF SYSTEM: A greater success can be downgraded to a lesser success by accepting a lesser penalty. A greater penalty can be exchanged for a greater positive. This creates a risk/reward dial at every Artifice Event — the crafter decides how much they want to push the item toward power at the cost of drawbacks.*|
| :- |

## **Worked Example — Golem-Forged Arm (Summary)**

|*Item: Tier 4, Golem-Forged Arm (Complex Prosthetic) Base Value: 600 (Intricate Device) Components: Resilience (100) + Impact (100) + Forge (500) + Pattern (500) + Concordance (500) + Current (250) = 1,950 PV Size: ×1.0 | Quality: ×1.0 FINAL PV: (600 + 1950) × 1.0 = 2,550 PV Crafter: Rank 5, Intellect +4 → Normal Progress 70 PV/week; Check = d20 + 14 Project Duration: ~24 weeks focused work*|
| :- |

|**Week**|**Check Result**|**Event**|**Outcome**|
| :- | :- | :- | :- |
|1|d20+14 = 26 (Success)|Fork in the Road|Crafter chooses "cleaner joint tolerances" → Lesser Positive: Maneuvering Grip (+EML to Grapple)|
|2|d20+14 = 31 (Critical Success)|Breakthrough|Lesser Positive (or Greater Positive, editor note): Rapid Action (Deployment) — switching to Guard Mode is a free action once/round|
|3|d20+14 = 23 (Success with Cost)|Complication|Forced Lesser Negative: Minor Hog (Maintenance) — after 3 encounters without service, accumulates −1 penalty (max −5) on Active Component checks until cleaned|
|4–8|Mix of Successes|GMs mix events|5 × 70 = 350 PV. Weeks 4–5: Fork events with no new Mutations. Week 6: Complication resolves as half progress only. Weeks 7–8: Stasis.|
|9|d20+14 = 14 (Failure)|Stasis|No progress. Week wasted.|
|10–24|Mix|Push phase|~1,355 PV accumulated across 14 weeks. Project completes at 2,550+ PV with 2 Positives + 1 Negative.|


# **PART V — STEP 3: SLOT ARCHITECTURE**

|*Install Active and Enabling Components into the slot structure. Establish the power economy. Tier = Slots. Battery lives in a dedicated housing, never counted against inset total.*|
| :- |

## **Core Architecture**

|**Element**|**Location**|**Function**|
| :- | :- | :- |
|Core|IS the item (blade, shaft, chassis)|Material quality sets Tier; Tier sets slot count; planar identity sets base affinity|
|Power Housing (Battery)|Dedicated slot — NEVER counted against inset total|Stores and delivers energy for Active Components; modular and swappable|
|Inset Slots (= Tier count)|Tier number of binary sockets|Empty or occupied; holds Active and Enabling Components; modular post-creation|

## **Slot Types**

|**Type**|**Counts for EML?**|**Examples**|**Notes**|
| :- | :- | :- | :- |
|Active Component|YES|Spells, magical properties, mechanical effects|Primary content of item power. Each occupies one inset slot.|
|Enabling Component|NO|Attunement Matrix, Volatility Regulator, Daedalon's Catalyst|Makes other things possible. Consumes slots but does not affect EML.|
|Nested Item (Wand in Staff)|YES — as one entry at nested EML|A wand slotted into a staff|Staff may hold wands; wands may not hold staves. Internal components do not individually inflate host EML.|

## **EML Formula — Rule of Sums**

|**EML = Highest Active CML + floor((Total Active Components − 1) ÷ 4)**|
| :- |

Only Active Components count. Enabling Components (batteries, matrices, regulators) affect capability but NOT EML.

|**Configuration**|**Highest CML**|**Active Count**|**EML Calculation**|**Result**|
| :- | :- | :- | :- | :- |
|1 spell at CML 2|2|1|2 + floor(0/4)|EML 2|
|2 spells, highest CML 2|2|2|2 + floor(1/4)|EML 2|
|4 spells, highest CML 3|3|4|3 + floor(3/4)|EML 3|
|5 spells, highest CML 3|3|5|3 + floor(4/4)|EML 4|
|8 spells, highest CML 4|4|8|4 + floor(7/4)|EML 5|
|8 spells; raise 1 to CML 5|5|8|5 + floor(7/4)|EML 6|
|12 spells, highest CML 5|5|12|5 + floor(11/4)|EML 7|

## **Broad vs. Deep Trade-off**

|**Strategy**|**Configuration**|**EML Progression**|**Best For**|
| :- | :- | :- | :- |
|Deep|Few high-CML components (3 slots, all CML 3+)|EML rises slowly with component count; powerful individual effects|Swords, single-function items, specialist wands|
|Broad|Many low-CML components (6+ slots, mix CML 1–3)|EML rises faster once 4+ components present; maximum utility|Staves, armor, multi-function platforms|

|*DIMINISHING RETURNS EXAMPLE — Same EML, different capability: Focused Staff (4 spells): Fireball CML 4, Magic Missile CML 2, Light CML 1, Cure CML 2 → EML = 4+0 = 4. Strong offense. Versatile Staff (8 spells): Fireball CML 3, Lightning CML 3, Ice Storm CML 3, Magic Missile CML 2, Light CML 1, Cure CML 2, Detect CML 1, Shield CML 2 → EML = 3+floor(7/4) = 4. Same EML; much broader capability.*|
| :- |

## **CML Reference**

|**CML Range**|**Tier**|**Effect Scale**|
| :- | :- | :- |
|CML 1–2|Novice|Simple effects — basic damage, minor utility, condition triggers|
|CML 3–4|Journeyman entry|Intermediate — conditional bonuses, moderate utility, multiple targets|
|CML 5–6|Journeyman|Advanced — significant bonuses, complex mechanics, sustained effects|
|CML 7–8|Expert|Expert — powerful abilities, multiple interactions, area or persistent|
|CML 9–10|Master|Master — transformative abilities, reality-bending, domain-level effects|

## **The Battery System**
### **Battery Types**

|**Type**|**Capacity**|**Recharge Unit**|**Profile**|
| :- | :- | :- | :- |
|Organic (Verdant Font)|EML × 4 charges|Minutes|Small reservoir, fast recovery. Burst and combat use.|
|Metallic (Hidden Forge)|EML × 8 charges|10 Minutes|Medium reservoir, reliable. General adventuring standard.|
|Crystalline (Borderlands)|EML × 16 charges|Hours|Large reservoir, slow recovery. Sustained or long-duration use.|
|Echo-Heart (Palimpsest)|EML × 16 charges|Minutes|Large reservoir, fast recovery. Apex tier; expensive and rare.|

|**Capacity = EML × Multiplier Recharge Rate = (10 − (EML − 1)) × Base Unit Drain per Tick = floor(CML ÷ 2), minimum 1**|
| :- |

### **Efficiency Tick — Host Item Tier**

|**Item Tier**|**Efficiency Tick**|**Implication**|
| :- | :- | :- |
|Tier 0 (Mundane)|1 Minute|Bleeds energy; low-tier housing cannot maintain magical containment|
|Tier 1–4 (Novice/Wand-grade)|10 Minutes|Standard adventuring items; charges drain at normal rate|
|Tier 5–7 (Journeyman)|1 Hour|Professional equipment; stable drain over extended periods|
|Tier 8–9 (Master)|12 Hours|High-tier items maintain charge for full field operations|
|Tier 10 (Legendary)|24 Hours|Near-permanent stability; loses charge only over multiple days|

|*INNATE vs. POWERED: If an Active Component's planar identity matches the core material's affinity, the component operates without battery drain (Innate). An obsidian blade with a fire-damage Active Component does not need a battery for that component — the Inferno expression sustains it. Install a battery for the other components; the fire is free.*|
| :- |

## **Installing and Removing Components**

|**Operation**|**CML Range**|**Time Cost**|**Talent Required**|
| :- | :- | :- | :- |
|Install|CML 1–2|1 day per CML|Enchanter: Novice|
|Install|CML 3–4|2 days per CML|Enchanter: Novice|
|Install|CML 5+|3–5 days per CML|Enchanter: Journeyman|
|Remove (safe)|Any|1 day per CML|Enchanter: Journeyman|
|Remove (without talent)|Any|Immediate|Risk: component damaged on failure; critical failure breaks component AND slot|

|*SLOT REPAIR: A damaged slot requires a dedicated crafting ritual (500–1,000 PV minimum) or a specialized Enabling Component. High-level crafter work (Rank 8+) can repair slots in the field with appropriate materials.*|
| :- |

## **Wand Grade — Closed Systems**

|**Property**|**Value**|**Notes**|
| :- | :- | :- |
|Tier cap|Tier 4 (hard)|Consumer-grade; standard adventuring tool; mass-producible|
|Core spell|One Active Component|Fixed at creation; establishes primary affinity; cannot be changed|
|Remaining slots|Up to 3|Accuracy/range/duration mods; secondary Enabling Components; Additive Components|
|EML|Effectively the CML of core spell|Add-ons do not push EML unless they are high-CML Active Components themselves|
|Post-creation|No new spells|Once the core is set, the wand's character is locked|

|*AFFINITY LOCK: Post-creation Additive Components modify the expression but cannot change the fundamental character. A fire wand wrapped in Frost material produces fire with cold secondary expression — it does not become a cold wand.*|
| :- |

## **Staff Grade — Open Platforms**

|**Property**|**Value**|**Notes**|
| :- | :- | :- |
|Tier range|Tier 6–10 (mortal); Tier 12+ (monstrous/divine)|Open platform designed for expansion over campaign time|
|Attunement Matrix|Enabling Component; holds 4 spell slots per Matrix|Does not consume an inset slot; multiple Matrices can be installed in open slots|
|Post-creation spells|Via Attunement Ritual (1 day/inscription)|Each added spell becomes an Active Component for EML purposes|
|Fractal nesting|Staff may hold Wands; Wands may not hold Staves|Nested wand contributes its EML as a single Active Component value|
|EML growth|Grows over campaign as spells are inscribed|A staff's EML is its living history; each spell shifts the affinity balance|

|*STAFF AS BIOGRAPHY: A staff used over a campaign reflects the history of that use in its affinity architecture. Each installed spell shifts the affinity balance. A Verdant-core staff accumulating Synod-expression spells develops Biotic tension in its ambient field. The staff becomes what the caster does with it.*|
| :- |

## **Carrier Effects — Affinity Stacking**
The NOUN/VERB principle from the planar combination table applies directly to item construction:

**•** Primary material (Core) = NOUN — what the item IS. Architecturally prior. Cannot be changed post-construction.

**•** Additive Component (construction-time) = VERB modifier — free; no slot cost; continuous emission.

**•** Additive Component (post-creation) = Secondary VERB — consumes one inset slot.

**•** Compatible-plane Additives: Resonance (same plane) or Harmonic/Tensioned (adjacent/opposing phase) — all natural, no Forge catalyst.

**•** Antithetical Additives: Require a Daedalon's Catalyst Enabling Component in a dedicated slot.

|*EXAMPLE — Current-Wrapped Bedrock Blade: A Bedrock (B-09, Earth/Solid) core sword with a Current (B-14, Air+Fire/Gas) pommel wrapping is simultaneously structurally permanent (Bedrock noun) AND electrically expressive (Current verb). Both are Borderlands-origin — compatible planes, resonant emission field, no catalyst required. The blade IS permanence. It ACTS through electrical expression.*|
| :- |


# **PART VI — STEP 4: LEGACY (ITEM ASCENSION)**

|*The item accrues meaning through use. AP mirrors XP distribution. The Core is the character — its AP history belongs to it and travels with it. Replace the core: legacy resets. Replace everything else: legacy persists.*|
| :- |

## **The Three Legacy Tiers**

|**Tier**|**AP Threshold**|**Expression**|**Capability**|
| :- | :- | :- | :- |
|Unattuned|0–49 AP|Passive — material does what it does|Base spec only; no Ascension Slots; EML and component effects as installed|
|Awakened|50–99 AP|Active — material wants to do it|First Ascension Slot unlocked; Innate Alignment enhanced; item begins expressing intent|
|Mastery|100+ AP|Integrated — wielder and item are one system|Emulsion slot available with Daedalon's Catalyst; full planar character expressed|

|*AP ACCUMULATION: AP distribution mirrors XP distribution. The same events that earn character XP earn item AP for items that participated in those events. Both player and GM may designate items to receive AP. Items central to an encounter's resolution earn full AP. Items present but not meaningfully engaged earn reduced AP. Items performing actions directly relevant to their planar identity and legacy triggers may earn bonus AP at the GM's discretion.*|
| :- |

## **The Legacy Trigger Skeleton**
A Legacy Trigger defines what earns AP and shapes which Ascension Traits become available.

|**Element**|**Definition**|**Example**|
| :- | :- | :- |
|Action|What the item must DO|"Strike a killing blow" / "Absorb a magical effect" / "Seal a planar rift"|
|Subject|What material, creature, energy, or concept provides resonance|"Against Synod-domain entities" / "While channeling Borderlands electrical expression"|
|Condition|Where, when, or under what circumstances|"In a Stage 3+ bleed zone" / "While wielder is at full health" / "During a politically designated conflict"|
|Scale|How much, how many, or how long|"20 qualifying targets defeated" / "10 cumulative hours in bleed zone" / "3 consecutive encounters without rest"|

|*DESIGN EXAMPLE (canonical from V11.4): "The hero quenched the blade in the blood of a thousand fire-newts beneath the burning crystal caverns for a fortnight." Mechanical translation — Action: Quench/Bathe the weapon. Subject: Blood from 1,000 Fire-aspect salamander-type creatures (or fewer more potent substitutes). Condition: Immersed at a mid-power ley line at a planar rift to the Fire Borderlands. Scale: Duration 3–5 weeks + kill count. The same trigger can be fulfilled differently (1,000 minor vs. handful of powerful), with different side-effects per substitution.*|
| :- |

## **Legacy Trigger Action Table (d20)**

|**Roll**|**Action Verb**|**Frost Example**|**Authority Example**|
| :- | :- | :- | :- |
|1|Anoint / Bathe|Submerge in meltwater from a primordial glacier|Bathe the crown in the waters of a coronation spring|
|2|Slay / Vanquish|Slay a creature of pure summer fire|Vanquish a usurper sitting on a stolen throne|
|3|Expose / Endure|Expose to an unending blizzard for three nights|Have the item endure the oaths of 1,000 soldiers|
|4|Channel / Infuse|Channel a blizzard through the item to freeze a river solid|Infuse the item with the collective loyalty of a city|
|5|Shatter / Break|Shatter a vessel containing an eternal flame|Break the gates of a besieged capital|
|6|Re-forge / Alter|Re-forge the blade, quenching only in glacial melt|Rebuild the hilt from a broken royal sigil|
|7|Witness / Observe|Witness the birth of an ice-born leviathan|Be present at the signing of a world-shaping treaty|
|8|Placate / Appease|Placate an enraged winter spirit|Offer the item as tribute to a restless monarch's shade|
|9|Survive / Withstand|Survive being buried in an avalanche with the item in hand|Withstand a trial by combat for the right to rule|
|10|Seal / Bind|Seal a rift leaking summer-fire into a frozen region|Bind a chaotic entity that threatens civil order|
|11|Liberate / Free|Free a beast encased in ancient ice without killing it|Liberate a populace from an unjust law|
|12|Nurture / Plant|Nurture a frost-lotus to bloom on a volcano's flank|Consecrate the founding stone of a new just city|
|13|Inscribe / Carve|Inscribe the item with the true name of Winter's Heart|Carve the first law of a new dynasty into its haft|
|14|Sacrifice / Offer|Sacrifice a cherished warm memory to eternal cold|Relinquish a claim to title or inheritance in its name|
|15|Reclaim / Steal|Reclaim the stolen Heart of Winter from foreign hands|Steal a despot's scepter of rule|
|16|Create / Weave|Weave a permanent ice-bridge between two peaks|Use the item as a symbol to found a knightly order|
|17|Harmonize / Attune|Meditate with the item at a leyline convergence on solstice|Attune the item during the coronation ceremony of a new ruler|
|18|Defile / Corrupt|Corrupt a sacred flame with frost in a holy sanctuary|Defile an unjust law by using the item to break it publicly|
|19|Restore / Heal|Restore a frozen wasteland to temporary summer|Restore a fallen house to its rightful position|
|20|GM Custom|Design a trigger specific to this item and its history|Design a trigger specific to this item and its history|

## **The Ascension Ritual**
**•** 1. Define the desired trait. Establish its mechanical effect and conceptual character.

**•** 2. Set the AP cost (typically 25–50 AP per slot unlock, scaling with trait power).

**•** 3. Identify the required component (exact or substitute).

**•** 4. Check compatibility — does the proposed trait's conceptual character align with the item's AP history and planar identity?

**•** 5. Perform the ritual. Success: trait inscribed, Ascension Slot unlocked. Failure: roll on Aberration table.

Mechanical Ascension Traits count as Active Components for EML purposes. Cosmetic traits do not.

## **Component Substitution**

|**Substitution Type**|**Risk Level**|**Aberration Chance**|**Catalyst Required?**|
| :- | :- | :- | :- |
|Exact component|None|None|No|
|Same plane, different isotope|Minor|Roll on Cosmetic table (d100)|No|
|Adjacent plane, compatible affinity|Moderate|Roll on Negative table (d20) or Positive on Critical Success|No|
|Antithetical plane|High|Roll full Aberration table; Positive only on Critical Success|Yes — Daedalon's Catalyst required|

## **Aberration Tables**
### **Cosmetic Aberrations (d100) — Triggered on minor substitution**
Roll when using a same-plane substitute or in certain other low-risk conditions. All cosmetic effects are permanent but have no mechanical impact.

|**Roll**|**Aberration**|**Effect**|
| :- | :- | :- |
|1–10|Temperature Ghost|Item radiates illusory heat or cold (no actual thermal effect)|
|11–20|Mirrored Surface|Item develops a minor reflective quality (cosmetic only)|
|21–30|Gravelly Whisper|Item makes a deep, grinding sound when moved; otherworldly but not hostile|
|31–40|Bioluminescence|Item glows softly with the color of its primary archetype (Flame=red, Frost=blue, etc.)|
|41–50|Ethereal Trail|Item leaves a faint, quickly-fading wisp when moved quickly; purely visual|
|51–60|Harmonic Resonance|Item vibrates gently when near others with strong magical auras|
|61–70|Temporal Lag|Item appears to move a fraction of a second behind the wielder's hand; harmless|
|71–80|Planar Tether|Item occasionally phases slightly, becoming briefly translucent; no mechanical effect|
|81–90|Sympathetic Scar|Item develops a mark matching the component's defining feature|
|91–99|Resonant Scar|Item develops permanent marks in the pattern of its component's defining feature|
|100|GM's Choice|Create a custom cosmetic aberration fitting the component and item|

### **Negative Aberrations (d20) — Triggered on incompatible substitution**

|**Roll**|**Aberration**|**Mechanical Cost**|
| :- | :- | :- |
|1–2|Discordant Resonance|−1 penalty on all checks using the item until stabilized|
|3–4|Planar Misalignment|Item has difficulty functioning; 20% chance to fizzle on each use|
|5–6|Volatile Essence|After each use, item makes TN 15 save or suffers 1 Hardness damage|
|7–8|Leeching Drain|Wielder loses Half-EML Stamina per hour while carrying the item|
|9–10|Parasitic Bond|Wielder suffers −1 penalty on saves while item is dormant/stowed|
|11–12|Chaotic Mutation|Roll d4: 1 = property works only half the time; 2 = unpredictable side effects; 3 = stronger but costs more; 4 = swaps effects randomly|
|13–14|Planar Contamination|Item permanently detectable as magical; cannot be concealed from magical senses|
|15–16|Symbiotic Hunger|Each day wielding requires TN 10 Will save or −1 on all checks from emotional drain|
|17–18|Cascading Failure|10% chance on each use to trigger Setback-level malfunction (lose next week of use)|
|19–20|Planar Anchor|Item resists crossing planar boundaries; wielder slowed in extradimensional spaces|

### **Positive Aberrations (d20) — Triggered on Critical Success with substitute**

|**Roll**|**Aberration**|**Mechanical Benefit**|
| :- | :- | :- |
|1–2|Perfect Attunement|+1 bonus on one chosen Skill Sphere per day|
|3–4|Enhanced Affinity|+Half EML to damage/effect rolls involving primary archetype|
|5–6|Adaptive Essence|After 10 uses in a specific archetype, may swap item's secondary archetype once (resets)|
|7–8|Resonant Strength|+1 to item's EML (max +2 across lifetime)|
|9–10|Swift Attunement|Reduces activation time by 1 action category (standard→swift, swift→free) once per encounter|
|11–12|Sympathetic Echo|+2 bonus on attack/check rolls when using item's primary ability|
|13–14|Harmonic Binding|Item bonds strongly; +1 to saves while wielding|
|15–16|Resonant Memory|Item retains a perfect memory of a past wielder's expertise (+1 to a relevant skill)|
|17–18|Planar Harmony|Item's planar identity shifts to integrate the substitute — gains properties of both origins permanently|
|19–20|Awakened Spirit|Item gains a faint consciousness; can warn wielder of danger once per day as an instinct flash|

## **The Emulsion Capstone**
The Tier 3 (Mastery) Emulsion slot is the legacy system's capstone. It requires everything else simultaneously:

**•** Daedalon's Catalyst Enabling Component at Tier 6+ minimum (consumes one inset slot)

**•** 100+ AP on the Core material

**•** AP history demonstrating use consistent with the Emulsion's conceptual character

**•** Both antithetical materials available (separate acquisition arcs required)

The Emulsion installed at Mastery tier is not manufactured — it is earned. An item that has spent its Mastery tier operating at the boundary of two antithetical expressions, with AP history built from those interactions, develops the Emulsion as the only coherent outcome of its history.

|*A MASTERY-TIER ITEM IS: A physical substance. An alchemical compound. A political artifact. A divine resonance node. A biography. The code on the pommel tells anyone who knows how to read it: who made it, what conditions produced the material, what the wielder did with it, which gods have a stake in its existence, and why it ended up exactly this way.*|
| :- |


# **PART VII — QUICK REFERENCE**

## **Item Creation Checklist**

|**Step**|**Action**|**Result**|
| :- | :- | :- |
|1a|Identify base material on real periodic table|Physical Base TN; Hardness; chemical interactions|
|1b|Identify planar identity on alchemical table|Plane; phase; formation stage; tier potential; political access flags|
|1c|Resolve acquisition (Physical TN + Access TN if restricted)|Material in hand or adventure required|
|2a|Calculate combined Crafting TN|Physical Base + Volatility + Rank Penalty (Grade modifies the check, not TN)|
|2b|Calculate PV requirement|(Base Value + Material Value) × Size × Quality|
|2c|Accumulate PV via weekly Artifice Checks|Each check: d20 + (Rank×2) + Intellect vs. TN → Degree of Success → PV + Event|
|2d|Resolve Artifice Engine events|Breakthrough/Fork/Complication generate Mutations; Stasis/Setback are timelosses|
|2e|Establish material layers|Base Component + up to two Additive Components (free at construction)|
|3a|Install Active Components|One per inset slot; each contributes to EML calculation|
|3b|Install Enabling Components|Attunement Matrix, Catalyst, Volatility Regulator; consume slots but do not affect EML|
|3c|Install Power Housing (Battery)|Dedicated slot; not counted against inset total; select type for desired profile|
|3d|Calculate EML and verify Power Economy|EML = highest CML + floor((count−1)÷4); check drain vs. recharge sustainability|
|4|Establish Legacy Triggers|Action + Subject + Condition + Scale; written toward planar identity; set AP thresholds|

## **All Formulae**

|**ARTIFICE CHECK = d20 + (Artifice Rank × 2) + Intellect Bonus vs. Crafting TN NORMAL WEEKLY PROGRESS = (Artifice Rank × 10) + (Intellect Bonus × 5) PV PV = (Base Value + Material Value) × Size Multiplier × Quality Multiplier CRAFTING TN = Physical Base TN + Volatility + Rank Penalty EML = Highest Active CML + floor((Total Active Components − 1) ÷ 4) CAPACITY = EML × Multiplier (Organic ×4 / Metallic ×8 / Crystalline ×16 / Echo ×16) RECHARGE RATE = (10 − (EML − 1)) × Base Unit DRAIN PER TICK = floor(CML ÷ 2), minimum 1**|
| :- |

**ÆTHERIUM CODEX**

**Planar Element Reference — Complete Card Set**

104 Single-Plane States + 16 Cross-Planar Naturals + 8 Emulsions

*Alpha Draft | Working Document*
# **READING KEY**
• ◆ Natural combination — forms without catalyst under appropriate conditions

• ⚙ Catalyzed diagonal — requires Hidden Forge catalyst; forced/unnatural state

• ◆⚙ Emulsion — both antithetical planes forced together by Forge catalyst; cosmological event

• Tier Scaling: Each material exists at Tier 1 (Resonant), Tier 2 (True), or Tier 3 (Prime). Higher tiers emit more strongly and provide more powerful properties.

• Formation Conditions: The planar bleed stage at which the material crystallizes determines its purity and coherence. Stage 1–2 = clean; Stage 3 = volatile; Stage 4–5 = unstable/rare.

• Interaction Profile: How the material's phase state behaves with other phase states. Determines cross-planar compatibility.

• Emission Character: The continuous magical field the material generates — its contribution to the regional Primal Current.


-e 
---
---

# SECTION 2: 80-ISOTOPE CARD SET
## (Lines 778–1944 of original)

# **THE BORDERLANDS**
*The Engine of Matter. Dominant defines physical state. Recessive defines behavior.*

Phase Wheel: Earth (Solid) / Water (Liquid) / Air (Gas) / Fire (Plasma)

Diagonals: Earth ↔ Air / Water ↔ Fire

**B-01 — The Inferno**

|**Plane**|Borderlands|**Phase**|Plasma (Pure)|
| :- | :- | :- | :- |
|**Combination**|Fire (Pure)|**Type**|◆|
|**Base Physical Property**|Pure elemental fire. No ground, only flame. Consumes all available fuel without cessation. Self-sustaining as long as fuel exists anywhere in proximity.|||
|**Emission Character**|Consumption/transformation field. Actively draws on nearby fuel sources — organic, chemical, or magical. Accelerates entropy in adjacent materials.|||
|**Interaction Profile**|Consumes and transforms. Amplifies adjacent Plasma to destructive levels. Drives Liquid into volatility. Expands through Gas environments, consuming available fuel. Opposed by Solid — high tension at contact boundary; Forge mediation required for stable combination.|||
|**Formation Conditions**|Stage 4–5 bleed. Requires sustained planar pressure from a Fire-dominant Borderlands rift. Cannot form in Stage 1–2 environments — dissipates before crystallizing.|||
|**Tier Scaling**|Tier 1 — Mild persistent warmth. Material is noticeably hot to touch, ignites tinder on contact. Contributes minor heat emission to regional Primal Current. Tier 2 — Active flame property. Surface burns continuously without consuming the host material. Other combustibles in contact ignite. Soak against fire damage for the item itself. Tier 3 — Self-sustaining consumption field. Item radiates a 5-ft heat aura dealing fire damage. Adjacent materials of lower tier begin degrading on the item condition track from sustained exposure.|||

**B-02 — Steam**

|**Plane**|Borderlands|**Phase**|Plasma + Liquid|
| :- | :- | :- | :- |
|**Combination**|Fire + Water (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Scalding high-pressure vapor. Geothermal vent character. Expands violently under containment. Temperature exceeds boiling indefinitely without dissipating.|||
|**Emission Character**|Pressure and expansive heat combined. Forces outward expansion in adjacent materials. Degrades sealed containment structures over time.|||
|**Interaction Profile**|Plasma dominant with Liquid recessive. Retains Plasma's consuming character but the Liquid component forces the energy into an expanding, permeating form rather than a point-source burn. Inherently unstable — requires active Forge mediation to prevent rapid decompression.|||
|**Formation Conditions**|Stage 3–4, high geothermal pressure environments. Requires forcing Fire and Water resonance into the same material — natural formation only at major volcanic/aquatic seam intersections.|||
|**Tier Scaling**|Tier 1 — Material is always hot and damp. Water near it becomes uncomfortably warm. Prevents freezing conditions within 10 ft. Tier 2 — High-pressure steam emission. Exposed flesh takes ongoing scalding damage. Item provides immunity to cold-based damage thresholds. Tier 3 — Pressurized field. Item continuously emits a scalding vapor aura. Sealed armor worn near it suffers accelerated item condition degradation from internal pressure buildup.|||

**B-03 — Slag**

|**Plane**|Borderlands|**Phase**|Plasma + Solid|
| :- | :- | :- | :- |
|**Combination**|Fire + Earth|**Type**|◆|
|**Base Physical Property**|Superheated semi-liquid heavy matter. Sticky and slow-moving. Retains heat for extended periods after the source has withdrawn. Adheres to surfaces on contact.|||
|**Emission Character**|Persistent heat that also has mass. Does not dissipate like gaseous emissions — heat stays where the material is. Adhesive energy character.|||
|**Interaction Profile**|Plasma consuming a Solid substrate. The Solid component gives the Plasma mass and persistence. Results in a slow-moving, high-damage emission that lingers rather than flashing and fading.|||
|**Formation Conditions**|Stage 3–4 volcanic environments. Forms where Fire-dominant bleed permeates Earth-heavy geology and partially crystallizes before the flow cools.|||
|**Tier Scaling**|Tier 1 — Material retains heat. Stays warm hours after removal from heat source. Provides cold resistance through thermal mass. Tier 2 — Adhesive burn. On hit, the material adheres to target. Ongoing fire damage until actively removed. Counts as a persistent condition. Tier 3 — Flowing destruction. Material can reshape slowly under sustained heat (from itself). Item gains a self-sealing property against physical damage — Slag fills its own fractures, preventing item condition track deterioration below Damaged.|||

**B-04 — Scorch**

|**Plane**|Borderlands|**Phase**|Plasma + Gas|
| :- | :- | :- | :- |
|**Combination**|Fire + Air|**Type**|◆|
|**Base Physical Property**|Solar wind. Heat without fuel source. Flash-burns at distance without physical contact. Does not ignite — vaporizes. No smoke, no residue.|||
|**Emission Character**|Rapid energy transfer across distance without material contact. Bypasses physical barriers that would stop flame.|||
|**Interaction Profile**|Plasma and Gas both expanding. The combination amplifies range dramatically while reducing the burning/adhesive quality of pure Plasma. Think heat ray rather than flame.|||
|**Formation Conditions**|Stage 3–4 bleed, high-altitude or wide-open exposed environments where Air and Fire resonances intermingle without an Earth substrate to ground them.|||
|**Tier Scaling**|Tier 1 — Radiant heat. Item feels hot from a foot away. Melts soft materials — wax, light compounds — on extended contact. Tier 2 — Flash-burn delivery. Ranged attacks from weapons made with Scorch components deal fire damage at range without combustion. No saving throw against ignite — it doesn't ignite, it chars. Tier 3 — Solar intensity field. 10-ft radiant aura. Creatures in aura take ongoing fire damage. Armor worn by targets in the aura suffers accelerated item track degradation.|||

**B-05 — The Abyss**

|**Plane**|Borderlands|**Phase**|Liquid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Water (Pure)|**Type**|◆|
|**Base Physical Property**|Endless crushing ocean. No surface, no light. Pressure increases without limit. Total sensory deprivation. The weight of infinite depth made tangible.|||
|**Emission Character**|Pressure field. Increases the perceived weight and density of nearby materials. Slows movement through or near the material as though moving through deep water.|||
|**Interaction Profile**|Flows through and connects. Carries adjacent emissions as a medium, diluting and distributing them. Fills Solid-defined channels. Disperses into Gas environments, losing coherence. Energizes under Plasma contact, becoming volatile.|||
|**Formation Conditions**|Stage 3+ deep environments. Requires sustained Water-dominant bleed without Fire or Earth interference. Most commonly found in subterranean water systems or coastal cave formations near Abyss-adjacent Borderlands bleeds.|||
|**Tier Scaling**|Tier 1 — Hydrostatic weight. Item feels heavier than it is. Grants minor resistance to being moved involuntarily (Shove, reposition maneuvers). Tier 2 — Pressure field. 5-ft aura slows movement through the area. Creatures in aura treat movement as difficult terrain. Item grants immunity to crushing-type damage thresholds. Tier 3 — Abyssal depth. Item actively suppresses sound and light in a 10-ft radius. Creatures in the aura must make checks to avoid Disoriented condition. Provides total pressure immunity to wielder.|||

**B-06 — Vapor**

|**Plane**|Borderlands|**Phase**|Liquid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Water + Fire (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Choking white fog. Humidity that drowns on land. Visibility zero. Heat and water combined into an oppressive atmospheric presence rather than steam's violent pressure.|||
|**Emission Character**|Obscuring field. Reduces the clarity of magical emissions nearby — functions as interference for magical detection and targeting. Physical obscurement identical.|||
|**Interaction Profile**|Liquid dominant but forced toward Plasma temperature. The combination wants to either fully boil off (become Steam) or fully cool (become Rain). Requires Forge mediation to hold the intermediate choking-fog state.|||
|**Formation Conditions**|Requires forcing Water and Fire into proximity without the pressure differential that would produce Steam. Forms in magically active swamp or fen environments near convergent bleeds.|||
|**Tier Scaling**|Tier 1 — Perpetual dampness. Item is always slightly wet. Provides fire resistance (moisture). Hampers visibility in enclosed spaces when active. Tier 2 — Obscuring cloud. Activating item produces a 10-ft fog cloud. Targets within have obscured vision. Magical detection checks against targets in the fog are at disadvantage. Tier 3 — Blinding fog. Dense emission obscures 20-ft radius completely. All ranged attacks into or out of the area automatically miss. Item itself becomes difficult to locate magically.|||

**B-07 — Mire**

|**Plane**|Borderlands|**Phase**|Liquid + Solid|
| :- | :- | :- | :- |
|**Combination**|Water + Earth|**Type**|◆|
|**Base Physical Property**|The bog. Mud, quicksand, sucking earth. Neither fully liquid nor solid. Resists penetration while flowing to fill any gap. Immense cohesive strength.|||
|**Emission Character**|Cohesive field. Slows movement through the area around the material. Causes adhesion between surfaces in contact with each other near the source.|||
|**Interaction Profile**|Liquid flowing through Solid substrate. The Solid gives the Liquid resistance and mass. The result is something that moves but moves slowly, with tremendous drag.|||
|**Formation Conditions**|Stage 2–3 wetland environments. Forms where Water and Earth bleeds intermingle slowly over extended periods — geological timescales in laminar conditions.|||
|**Tier Scaling**|Tier 1 — Resistant material. Item surface is always slightly tacky. Grip never slips. Provides advantage on checks to maintain hold on anything. Tier 2 — Cohesive pull. Struck targets must make an Athletics check or have movement halved next turn as the adhesion pulls. Item resists Disarm attempts — treat item as one tier heavier for Sunder checks. Tier 3 — Immobilizing field. On hit, target must succeed on Might check or be Restrained for 1 round. Area around wielder becomes difficult terrain for opponents.|||

**B-08 — Hail**

|**Plane**|Borderlands|**Phase**|Liquid + Gas|
| :- | :- | :- | :- |
|**Combination**|Water + Air|**Type**|◆|
|**Base Physical Property**|Hardened water. Glaciers and relentless sleet. Flash-freezes on contact with anything warmer. Persistent cold that endures without dissipating.|||
|**Emission Character**|Thermal drain field. Actively pulls heat from the environment rather than generating cold directly. The absence of warmth rather than the presence of cold.|||
|**Interaction Profile**|Liquid carried by Gas mobility. The Air component gives this the penetrating, reaching quality of wind while the Water component provides the thermal drain. Reaches further than pure cold materials.|||
|**Formation Conditions**|Stage 2–3 cold environments. Forms where Air-dominant and Water-dominant bleeds interact in cold high-altitude or polar conditions.|||
|**Tier Scaling**|Tier 1 — Persistent chill. Item is always cold to touch. Provides immunity to heat-based discomfort. Preserves organic materials indefinitely from biological decay. Tier 2 — Thermal drain. Item slowly reduces ambient temperature in 10-ft radius. Creatures in area at end of their turn take cold damage. Extinguishes mundane and low-tier magical flames. Tier 3 — Flash-freeze field. On hit, target must succeed on Vigor check or suffer Slowed condition (cold crystallization in joints). Magical flames within 20 ft require maintenance checks each round or extinguish.|||

**B-09 — The Bedrock**

|**Plane**|Borderlands|**Phase**|Solid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Earth (Pure)|**Type**|◆|
|**Base Physical Property**|Infinite stone. Subterranean tunnels, geodes. Maximum structural density. The deepest, oldest expression of physical permanence — geology without time limit.|||
|**Emission Character**|Permanence field. Resists change and disruption in nearby materials. Adjacent items resist item condition track movement — Sunder checks against nearby items are at disadvantage.|||
|**Interaction Profile**|Persists and resists change. Reinforces adjacent Solid emissions (Resonance). Shapes Liquid flows into defined channels. Creates stable pockets that resist Gas dispersal. Opposes Plasma consumption — high tension, productive when mediated by Forge.|||
|**Formation Conditions**|Stage 1–2 geological stability zones. The cleanest formation condition in the Borderlands — long-duration laminar bleed with no competing resonances. Found in deep undisturbed geology, ancient mountain cores, and settled cave systems far from Reality Seams.|||
|**Tier Scaling**|Tier 1 — Dense material. Item is heavier than its size suggests. Gains +1 to item Soak calculation. Provides minor resistance to Knockback effects. Tier 2 — Structural permanence. Item cannot move down the condition track from a single hit unless that hit exceeds double the item's Damage Threshold. Provides full Knockback immunity to wielder. Tier 3 — Immovable object. Item actively resists every form of displacement, magical or physical. Wielder gains Might advantage on all checks to resist forced movement. Item condition track starts at Nicked only from weapons with Sunder advantage at Master tier or higher.|||

**B-10 — Magma**

|**Plane**|Borderlands|**Phase**|Solid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Earth + Fire|**Type**|◆|
|**Base Physical Property**|The volcano. Flowing, destructive rock. Has both the mass of stone and the consuming nature of fire. Moves slowly but nothing stops it.|||
|**Emission Character**|Destructive mass field. Combines density with consumption. Heat that also has structural weight — damages both the physical and the thermal.|||
|**Interaction Profile**|Solid channeling Plasma. The Earth substrate gives the Fire expression mass and persistence rather than rapid consumption. Slower but more thorough.|||
|**Formation Conditions**|Stage 3–4 volcanic environments. Forms in the transition zone between Fire-dominant bleed and Earth-heavy geology. The crystallization happens mid-flow.|||
|**Tier Scaling**|Tier 1 — Volcanic material. Always hot, heavier than stone of same size. Deals supplemental fire damage on contact. Naturally suppresses ice-type effects. Tier 2 — Flowing destruction. Item can reshape slowly under sustained heat applied to it. Self-sealing against damage — fills its own fractures. Deals fire damage type on successful hit. Tier 3 — Magma flow field. On Knockback, target location and path are treated as difficult terrain with ongoing fire damage for 2 rounds. Item itself cannot be destroyed by fire or cold — extremes neutralize each other.|||

**B-11 — Acid**

|**Plane**|Borderlands|**Phase**|Solid + Liquid|
| :- | :- | :- | :- |
|**Combination**|Earth + Water|**Type**|◆|
|**Base Physical Property**|Solvents and sludge. Rock dissolved into fluid. The earth becoming corrosive. Penetrates and dissolves structural materials while retaining some cohesion.|||
|**Emission Character**|Corrosive field. Degrades the structural integrity of adjacent materials over time. Items left near Acid-source materials for extended periods begin losing Tier.|||
|**Interaction Profile**|Liquid flowing through a Solid substrate that it is actively dissolving. The Solid component gives direction and mass to the corrosive action while being consumed by it.|||
|**Formation Conditions**|Stage 2–3 chemical-rich environments. Forms at intersections of Water-dominant bleeds with mineral-heavy geology, particularly where subsurface water contacts reactive Earth materials.|||
|**Tier Scaling**|Tier 1 — Mildly corrosive surface. Contact with vulnerable materials (leather, soft metals) causes slow degradation. Natural Sunder advantage against organic or low-tier items. Tier 2 — Active dissolution. On hit, target item (weapon or armor) moves one step down its condition track. Metal armors exposed to repeated hits degrade toward Compromised. Tier 3 — Deep corrosion. Armor-Piercing 3 — bypasses 3 points of Soak on hit. Creatures critically hit must succeed on Vigor check or suffer Weakened condition as structural tissue degrades.|||

**B-12 — Dust**

|**Plane**|Borderlands|**Phase**|Solid + Gas|
| :- | :- | :- | :- |
|**Combination**|Earth + Air (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Erosion. Sandstorms, dunes, floating islands. The Solid being broken down and carried by the Gas — Earth in the process of being dispersed into Air.|||
|**Emission Character**|Dispersal field. Gradually breaks down solid structures in proximity. The inverse of Bedrock's permanence field — everything near Dust is slowly being worn away.|||
|**Interaction Profile**|Forced tension between persistence (Earth/Solid) and dispersal (Air/Gas). Requires Forge mediation to hold this material from either settling as inert Solid or dispersing entirely as Gas.|||
|**Formation Conditions**|Requires forcing Earth and Air resonance together — natural formation only at desert environments with strong Borderlands bleeds, or at high altitudes where Stone formations are being eroded by Air-dominant bleed.|||
|**Tier Scaling**|Tier 1 — Abrasive coating. Exposed skin and eyes require protection. Provides camouflage in arid environments. Slight Sunder advantage against unprotected targets. Tier 2 — Erosion field. Objects near the item lose 1 point of effective Soak per hour of exposure. Opponents' armor degrades during extended encounters. Tier 3 — Sandstorm aura. 10-ft radius of blinding abrasion. All creatures in aura must spend movement to shield eyes or suffer Blinded. Item condition tracks of opponents degrade one step per round of aura exposure.|||

**B-13 — The Void Sky**

|**Plane**|Borderlands|**Phase**|Gas (Pure)|
| :- | :- | :- | :- |
|**Combination**|Air (Pure)|**Type**|◆|
|**Base Physical Property**|Endless sky. No gravity, no ground. Pure atmospheric presence without any physical anchoring. Movement in every direction simultaneously possible.|||
|**Emission Character**|Dispersal field. Spreads and diffuses other emissions in the area. Items near this material find their own emissions becoming gradually less intense but wider in range.|||
|**Interaction Profile**|Permeates and disperses. Distributes adjacent emissions widely at reduced intensity. Fills Solid voids, exerts outward pressure. Expands through Liquid, creating turbulence. Amplifies Plasma energy by providing fuel and range.|||
|**Formation Conditions**|Stage 3–4 high elevation or exposure. Forms at extreme altitudes or in locations where Air-dominant bleed has no Earth or Water to interact with — pure atmospheric zones near Borderlands tears.|||
|**Tier Scaling**|Tier 1 — Weight reduction. Item is lighter than material should allow. Encumbrance rating reduced by one category. Wielder moves slightly faster when carrying only this item. Tier 2 — Gravitational independence. Item can hover in place when released. Wielder gains advantage on checks to resist forced prone. Movement through air unimpeded. Tier 3 — Weightless field. Wielder ignores encumbrance penalties entirely. Jumps treat as though under Leaping effect. Opponents within 10 ft find their footing unreliable — movement costs doubled.|||

**B-14 — Current**

|**Plane**|Borderlands|**Phase**|Gas + Plasma|
| :- | :- | :- | :- |
|**Combination**|Air + Fire|**Type**|◆|
|**Base Physical Property**|Lightning and plasma. Storm without rain. Pure electrical-kinetic force expressed through atmospheric medium. The conductive atmosphere amplifies electrical discharge to enormous scale.|||
|**Emission Character**|Electrical/kinetic field. Arcs between conducting materials in proximity. Metal armor, weapons, and items within 30 ft are potential secondary targets for discharge.|||
|**Interaction Profile**|Gas providing the medium and range; Plasma providing the destructive energy. The most mobile form of destructive force in the Borderlands — reaches everywhere Air can reach.|||
|**Formation Conditions**|Stage 3–4 storm environments. Primary formation zone is the Stormpeak region (B-OMNI territory). Also forms at exposed ridgelines and high-altitude Borderlands rift zones.|||
|**Tier Scaling**|Tier 1 — Static charge. Item always has a mild electrical charge. Metal-armored opponents touching or being touched by item take 1 point of electrical supplemental damage. Tier 2 — Arc discharge. On critical hit, electrical arc jumps to nearest metal-wearing creature within 20 ft for secondary damage. Item grants wielder immunity to electrical Knockback. Tier 3 — Storm channel. Item becomes a lightning rod by choice — absorbs electrical damage directed at wielder, stores up to 3 charges, releases as single devastating discharge. Chain-lightning effect on release.|||

**B-15 — Frost**

|**Plane**|Borderlands|**Phase**|Gas + Liquid|
| :- | :- | :- | :- |
|**Combination**|Air + Water|**Type**|◆|
|**Base Physical Property**|Flash-freezing wind. Cold that snaps metal. Rapid crystallization on contact with anything containing moisture. The wind that kills not through force but through instantaneous temperature drop.|||
|**Emission Character**|Thermal drain at range. Where Hail drains locally, Frost's Gas component carries the cold across distance. Rapidly reduces heat in the environment at range.|||
|**Interaction Profile**|Liquid carried by Gas at low temperature. The cold persists because the Water component has crystallized but the Air component keeps spreading it. Mobile cold.|||
|**Formation Conditions**|Stage 2–3 cold exposure zones. Forms at high-altitude or polar environments where Air-dominant bleed interacts with moisture-heavy conditions.|||
|**Tier Scaling**|Tier 1 — Persistent chill at range. Cold radiates 5 ft. Liquids freeze on contact with item. Provides cold immunity to wielder. Tier 2 — Flash-freeze. On hit, target's joints crystallize — Slowed condition for 1 round. Wet or water-adjacent targets are frozen in place (Restrained) for same duration. Tier 3 — Ice field. 15-ft frost aura continuously. Surfaces in aura become difficult terrain. Creatures entering aura make Vigor check or suffer Slowed. Sustained exposure risks Restrained without saving throw.|||

**B-16 — Erosion**

|**Plane**|Borderlands|**Phase**|Gas + Solid|
| :- | :- | :- | :- |
|**Combination**|Air + Earth (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Abrasive wind. Grit that strips flesh. The Air carrying the Earth as an abrasive medium. Penetrates gaps in armor and protection that direct strikes cannot reach.|||
|**Emission Character**|Wearing field. Reduces item tier over time through continuous exposure. The most dangerous sustained material for equipment — not dramatic, just relentlessly wearing.|||
|**Interaction Profile**|Forced tension between Gas's dispersal and Solid's persistence. The Earth wants to settle; the Air won't let it. This unstable state is maintained by Forge mediation.|||
|**Formation Conditions**|Requires forcing Air and Earth resonance — forms in desert canyon environments where strong Borderlands bleed expresses through both elements simultaneously.|||
|**Tier Scaling**|Tier 1 — Abrasive coating. Deals bonus abrasion damage to unarmored or lightly armored targets. Natural Sunder advantage — bypasses aesthetic protection. Tier 2 — Penetrating grit. Armor Soak contribution reduced by 1 for each round of sustained combat. Resets outside combat. Gets between articulated joints — penalizes heavy armor movement. Tier 3 — Item-eating field. Opponent armor items make condition track checks each round of combat. Damage accumulates. Wielder's own items are immune — the Erosion recognizes its host.|||


# **THE VERDANT FONT**
*The Engine of Life. Dominant defines the organism. Recessive defines the behavior.*

Phase Wheel: Flora (Solid) / Myco (Liquid) / Viral (Gas) / Fauna (Plasma)

Diagonals: Flora ↔ Viral / Myco ↔ Fauna (catalyzed states are unnatural — require institutional or cosmological pressure)

**V-01 — The World Tree**

|**Plane**|Verdant Font|**Phase**|Solid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Flora (Pure)|**Type**|◆|
|**Base Physical Property**|Infinite canopy. Everything is wood and leaf. Living biological permanence — structure that grows rather than being built. Wood that is both architecture and organism.|||
|**Emission Character**|Growth field. Encourages biological development in adjacent materials. Organic materials in contact with World Tree expression repair themselves slowly over time.|||
|**Interaction Profile**|Persists and resists change. Reinforces adjacent Solid emissions (Resonance). Shapes Liquid flows into defined channels. Creates stable pockets that resist Gas dispersal. Opposes Plasma consumption — high tension, productive when mediated by Forge.|||
|**Formation Conditions**|Stage 1–3 deep forest environments with sustained Flora-dominant bleed. The Titanwood is the primary material-plane formation zone. Long-duration laminar bleed through existing forest produces the cleanest World Tree materials.|||
|**Tier Scaling**|Tier 1 — Living wood. Material continues to grow slowly — a weapon made from this wood gains the self-repair property (1 condition track step per 24 hours in sunlight). Naturally resistant to fire despite being wood — biological moisture content never drops. Tier 2 — Regenerative structure. Item repairs one condition track step per 10-minute rest period without external intervention. Dormant seeds occasionally sprout from the material. Grants wielder minor natural camouflage in forested environments. Tier 3 — World-tree node. Item actively grows root structures that anchor it against removal or theft. Wielder gains regeneration (1 HP per round) while in contact with natural earth or vegetation. Item becomes a Primal Current node for the World Tree expression.|||

**V-02 — Carnivorous**

|**Plane**|Verdant Font|**Phase**|Solid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Flora + Fauna|**Type**|◆|
|**Base Physical Property**|Venus flytraps, strangler vines, aggressive roots. Plants that hunt. Biological predation expressed through vegetation rather than animal form — the plant that does not wait for prey.|||
|**Emission Character**|Predatory biological field. Triggers threat responses and territorial instincts in nearby fauna. Animals near this material become anxious and aggressive.|||
|**Interaction Profile**|Solid growth given Plasma's predatory drive. The Flora wants to grow and persist; the Fauna wants to hunt and consume. Together they produce something that grows toward prey.|||
|**Formation Conditions**|Stage 3–4 Font bleed in carnivore-plant environments. The predatory vine systems of the Titanwood's interior zones are the primary formation source.|||
|**Tier Scaling**|Tier 1 — Aggressive reach. Weapon has a tendency to snag and grip. Disarm advantage property (natural vine-grip). Minor ongoing biological growth — trim regularly. Tier 2 — Predatory lunge. Once per encounter, item grants an extra attack as a free action triggered by a successful hit — the weapon hungers. Target of this extra attack suffers Grapple-compatible restraint for 1 round. Tier 3 — Apex predator field. Item projects a 10-ft predatory aura. All creatures in aura must succeed on Instinct check or be treated as Prey (item gains +2 to hit them for the encounter). Cannot be Disarmed by any means — item returns.|||

**V-03 — The Spore**

|**Plane**|Verdant Font|**Phase**|Solid + Liquid|
| :- | :- | :- | :- |
|**Combination**|Flora + Myco|**Type**|◆|
|**Base Physical Property**|Pollen-choked air. Trees that exhale poison. Hive-mind root networks. The plant and the fungus in communion — biological communication at the network scale.|||
|**Emission Character**|Network resonance. Creates sympathetic connections between items in proximity. Multiple items sharing Spore expression can share information about damage taken — if one item is hit, others in range 'know'.|||
|**Interaction Profile**|Solid structure carrying the network connectivity of Liquid. Flora defines the physical form; Myco provides the communication medium that flows through it.|||
|**Formation Conditions**|Stage 2–3 Font bleed where plant and fungal systems coexist in high density. Old-growth forest floors with visible mycelial networks are the primary formation zone.|||
|**Tier Scaling**|Tier 1 — Networked material. Item can serve as a Substance Delivery platform for spore-based compounds. Naturally produces a mild sedative compound on any open wound contact. Tier 2 — Hive awareness. Wielder gains advantage on Discovery checks relating to living networks, root systems, and underground structures. Item passively detects other Spore-expression items within 100 ft. Tier 3 — Network node. Item functions as an anchor for a 30-ft living network. Allies touching plant or fungal matter within the network area share a communication link. Wielder knows immediately if any anchor point is disturbed.|||

**V-04 — Overgrowth**

|**Plane**|Verdant Font|**Phase**|Solid + Gas|
| :- | :- | :- | :- |
|**Combination**|Flora + Viral (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Plants grow instantly to crush structures. Nature reclaiming cities in hours. Hyper-accelerated growth that bypasses normal biological timescales — the biological equivalent of Stage 5 Turbulent bleed.|||
|**Emission Character**|Accelerated growth field. Biological materials in proximity grow at abnormal rates. Unstable — living things near this material may grow incorrectly, producing cancerous or chaotic biological structures.|||
|**Interaction Profile**|Flora's Solid persistence forced into Viral's Gas acceleration. Inherently unstable — the growth drives conflict with its own structural integrity. Requires constant Forge mediation.|||
|**Formation Conditions**|Requires forcing Flora and Viral resonances — forms only at Reality Seams where Font bleed from two incompatible biological systems converges. Catalogued as Stage 4+ formation condition.|||
|**Tier Scaling**|Tier 1 — Growth trigger. Contact with organic material produces rapid minor growth — hair, nails, and plant matter grow visibly. Wounds seal fast but leave scarring. Unstable healing. Tier 2 — Structural reclamation. On hit, target's armor begins sprouting growth. Armor condition track degrades 1 step per round until growth removed (standard action). Wielder's wounds close at end of round. Tier 3 — Overgrowth field. 10-ft aura of explosive biological growth. Architecture in aura takes accelerated damage. Opponents must make Athletics checks each turn or be partially Restrained by growth. Wielder is immune.|||

**V-05 — The Hunt**

|**Plane**|Verdant Font|**Phase**|Plasma (Pure)|
| :- | :- | :- | :- |
|**Combination**|Fauna (Pure)|**Type**|◆|
|**Base Physical Property**|Pure Darwinism. A realm of alpha predators. The biological imperative without qualification — only the strongest continue. The Titanwood's organizing principle made material.|||
|**Emission Character**|Predatory imperative field. Heightens aggression and territorial instincts in nearby fauna. Animals near this material exhibit apex-predator behaviors regardless of species.|||
|**Interaction Profile**|Consumes and transforms. Amplifies adjacent Plasma to destructive levels. Drives Liquid into volatility. Expands through Gas environments, consuming available fuel. Opposed by Solid — high tension at contact boundary; Forge mediation required for stable combination.|||
|**Formation Conditions**|Stage 3–5 Font bleed in pure predator-dominant environments. The Hunt expression is most concentrated at Wildpath bleed zones. Also forms in the aftermath of large predator kills where biological intensity concentrations are highest.|||
|**Tier Scaling**|Tier 1 — Predator sense. Wielder gains Discovery advantage against living creatures within 30 ft — can detect heartbeats, breathing, movement through wall. Animals treat wielder as more dominant. Tier 2 — Apex expression. Weapon damage increases by one die step against biological targets. Wielder gains advantage on Initiative. Critical hit range expanded by 1 against biological targets. Tier 3 — Hunt field. 20-ft aura of predatory dominance. All biological creatures entering must make Instinct check or be Frightened. Prey-animal instincts activate even in sapient creatures. Wielder becomes the apex of the immediate ecosystem — nothing in range will willingly attack first.|||

**V-06 — Sylvan**

|**Plane**|Verdant Font|**Phase**|Plasma + Solid|
| :- | :- | :- | :- |
|**Combination**|Fauna + Flora|**Type**|◆|
|**Base Physical Property**|Symbiosis. Animals with bark-skin. Elves biologically bonded to mounts. Predation and growth in equilibrium — the biological balance point.|||
|**Emission Character**|Symbiotic field. Encourages biological cooperation rather than competition. Predator and prey relationships in the area shift toward mutualistic interactions.|||
|**Interaction Profile**|Plasma predation given Solid structure and permanence. The hunt is given roots. Fauna's consuming drive channeled through Flora's stability produces something that sustains rather than just kills.|||
|**Formation Conditions**|Stage 2–3 Font bleed in genuine symbiotic ecosystems — old-growth forests with stable predator-prey relationships maintained over geological time.|||
|**Tier Scaling**|Tier 1 — Bonded material. Item creates a sympathetic bond with its wielder over time — after 30 days of regular use, item responds to wielder's emotional state. Resists being used against the bonded wielder. Tier 2 — Symbiotic partner. Item grants wielder a passive bonus equal to half the item's EML on Athletics and Survival checks — the material 'wants' the wielder to thrive. Item cannot be intentionally used by anyone other than primary bond-holder. Tier 3 — Apex symbiosis. Wielder and item become a single biological system. Damage taken by item is split equally with wielder. HP restored to wielder also restores item condition. The bond grants both perfect awareness of the other's state at all times.|||

**V-07 — Cordyceps**

|**Plane**|Verdant Font|**Phase**|Plasma + Liquid|
| :- | :- | :- | :- |
|**Combination**|Fauna + Myco (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Bodies piloted by parasitic fungus. Animal autonomy surrendered to network control. The Myco forcing the Fauna into its network — not symbiosis but occupation.|||
|**Emission Character**|Override field. Disrupts autonomous biological control. Creatures near this material experience intrusive impulses and difficulty asserting their own intentions against the network.|||
|**Interaction Profile**|Fauna's predatory autonomy forced into Myco's network control. The Fauna fights the Myco's direction; the Myco contains the Fauna's drive and redirects it. Fundamentally unnatural and unstable.|||
|**Formation Conditions**|Requires forcing Fauna and Myco resonances at Stage 4+. Only forms in Font bleed zones where actual Cordyceps-type organisms have achieved genuine biological control over animal populations.|||
|**Tier Scaling**|Tier 1 — Network intrusion. Living creatures struck must make Instinct check or suffer a compelled minor action on their next turn (move toward a specific location, drop a held item). Does not override self-preservation. Tier 2 — Biological override. On critical hit, target must succeed on Instinct check (TN 15 + item tier) or be Charmed for 1 round — acts as directed by wielder on next turn only. Does not stack. Tier 3 — Network puppet. Once per encounter, on successful hit, wielder may attempt full Cordyceps control on biological target (Operate vs. Instinct). Success: target acts under wielder's direction for 1d3 rounds. The target is aware this is happening.|||

**V-08 — Chimera**

|**Plane**|Verdant Font|**Phase**|Plasma + Gas|
| :- | :- | :- | :- |
|**Combination**|Fauna + Viral|**Type**|◆|
|**Base Physical Property**|Rapid mutation. Creatures are mash-ups of species. Biological chaos without direction — the predatory drive married to unchecked change. The creature that becomes something else while hunting.|||
|**Emission Character**|Mutation catalyst field. Accelerates biological change in exposed organisms. Creatures struck by Chimera-expression items accumulate mutation faster than normal.|||
|**Interaction Profile**|Plasma consuming and Viral dispersing — both expansive, both transforming. The combination produces the fastest biological change in the Font's domain.|||
|**Formation Conditions**|Stage 3–5 Font bleed in environments where multiple predator species interact intensely — Reality Seam zones where different ecosystems from Settings A and B collide.|||
|**Tier Scaling**|Tier 1 — Adaptive surface. Item shifts minor properties based on what it strikes — after hitting fire-armored opponents, it gains minor fire resistance. After hitting armored opponents, it becomes slightly harder. Changes persist 1 hour. Tier 2 — Combat evolution. Each round of combat, item gains a small bonus to either attack or damage (wielder's choice) that accumulates up to +3. Resets between encounters. Represents the item 'adapting' to the current fight. Tier 3 — Living weapon. Item actively mutates in response to threats. Gains the ability to target any defense type (combined, Physical, Mental, Social) as a free action once per encounter — it finds the weakness.|||

**V-09 — The Mycelium**

|**Plane**|Verdant Font|**Phase**|Liquid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Myco (Pure)|**Type**|◆|
|**Base Physical Property**|A world of mushrooms. Everything connected underground. Pure network expression — the world as information system rather than physical structure. Every point is connected to every other point.|||
|**Emission Character**|Network resonance. Creates sympathetic connections between materials. Items made from Mycelium expression are aware of each other across distance.|||
|**Interaction Profile**|Flows through and connects. Carries adjacent emissions as a medium, diluting and distributing them. Fills Solid-defined channels. Disperses into Gas environments, losing coherence. Energizes under Plasma contact, becoming volatile.|||
|**Formation Conditions**|Stage 2–3 Font bleed where fungal systems dominate. Deep cave systems and ancient forest floors with millennia of fungal network accumulation.|||
|**Tier Scaling**|Tier 1 — Connected material. Item is aware of the general condition of its environment — wielder gains a sense of 'wrongness' when something nearby is concealed or hidden. Difficulty of Skullduggery to conceal items near this material increases by 2. Tier 2 — Network tap. Wielder can communicate silently with anyone touching fungal matter within 100 ft. Item passively maps underground and root-level structures within 30 ft. Tier 3 — Distributed consciousness. Item cannot be destroyed as long as any fragment exists. On apparent destruction, item reconstitutes from nearby biological matter within 24 hours. Wielder gains network sense of all living creatures within 50 ft as ambient awareness.|||

**V-10 — Rot-Garden**

|**Plane**|Verdant Font|**Phase**|Liquid + Solid|
| :- | :- | :- | :- |
|**Combination**|Myco + Flora|**Type**|◆|
|**Base Physical Property**|Slime molds and ooze. Decay that smells sweet. Everything dying and alive simultaneously. The most honest expression of the Font's death-as-growth principle.|||
|**Emission Character**|Decomposition field. Accelerates breakdown of organic structures. The material actively participates in the Font's cycle — consuming and contributing simultaneously.|||
|**Interaction Profile**|Myco network flowing through Flora structure it is also consuming. The Solid component provides the substrate; the Liquid component breaks it down. The item is its own ecosystem.|||
|**Formation Conditions**|Stage 2–4 Font bleed in environments with high organic turnover — forest floors, swamp margins, decomposition-rich cave systems.|||
|**Tier Scaling**|Tier 1 — Decomposition surface. Organic materials in contact degrade faster. Effective for Sunder against leather armor. Produces a faint sweet smell that attracts insects and small animals. Tier 2 — Living decay. Item actively breaks down biological material on contact — bonus to Sunder against organic armor types. Wielder heals 1 HP for each point of damage dealt to biological targets. Tier 3 — Rot-field. 5-ft aura of accelerated decomposition. Organic armor worn by opponents degrades one condition track step per round. Undead and Returned creatures in aura are Weakened — the Font's decay claims everything.|||

**V-11 — The Hive**

|**Plane**|Verdant Font|**Phase**|Liquid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Myco + Fauna (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Fungal network controlling animal bodies. Collective consciousness achieved through parasitic forcing. Individual autonomy surrendered to network control — the Cordyceps made institutional.|||
|**Emission Character**|Collective resonance. Items from the same Hive batch share their charge reserves — if one runs out, it draws from others in range.|||
|**Interaction Profile**|Myco network forced into Fauna's predatory autonomy — the network consuming the will. Fundamentally unnatural (correctly catalogued as catalyzed). The individual bodies fighting the network is the source of the instability.|||
|**Formation Conditions**|Requires forcing Myco and Fauna resonances at Stage 4+ conditions. Only forms where parasitic fungi have achieved genuine control of animal hosts — a specific and rare Titanwood phenomenon near Font tears.|||
|**Tier Scaling**|Tier 1 — Networked will. Item can be willed to act within 10 ft of wielder without physical contact — minor autonomous actions (pulling free of a grapple, blocking a strike). Requires Operate check. Tier 2 — Shared consciousness. When multiple Hive items are in range of same wielder, they act as a coordinated unit. Flanking bonuses apply even when wielder acts alone. Item can relay simple commands to biological constructs. Tier 3 — Hive control. Item can attempt to establish temporary network control over a Mindless or Instinctual creature within 30 ft once per encounter (Operate vs. Instinct check). Success makes creature treat wielder as part of its network for the scene.|||

**V-12 — Plague**

|**Plane**|Verdant Font|**Phase**|Liquid + Gas|
| :- | :- | :- | :- |
|**Combination**|Myco + Viral|**Type**|◆|
|**Base Physical Property**|Weaponized disease. The landscape itself is sick. Biological infection as ambient weather. Not targeted — indiscriminate biological contamination that spreads through the air.|||
|**Emission Character**|Contagion field. Transfers properties from one material to materials in contact. Active biological processes in the environment near this material accelerate and cross-contaminate.|||
|**Interaction Profile**|Myco's network capability carried by Viral's Gas dispersal. The infection spreads like weather — it doesn't target, it pervades.|||
|**Formation Conditions**|Stage 3–4 Font bleed in high-viral-load environments. Most commonly found in Font bleed zones during disease-outbreak periods.|||
|**Tier Scaling**|Tier 1 — Disease vector. Item can be coated with biological compounds and acts as reliable Substance Delivery platform. Contact with biological target delivers any applied compound without requiring hit confirmation. Tier 2 — Contagion trigger. Targets struck must succeed on Vigor check or contract a mild persistent condition (Sickened, 1d4 rounds). Compounding on subsequent hits before condition expires. Tier 3 — Plague carrier. Contagion spreads from struck target to adjacent creatures within 5 ft on failed Vigor checks. Item itself is immune to biological conditions — it is the source, not the victim.|||

**V-13 — The Cancer**

|**Plane**|Verdant Font|**Phase**|Gas (Pure)|
| :- | :- | :- | :- |
|**Combination**|Viral (Pure)|**Type**|◆|
|**Base Physical Property**|Unchecked cellular division. Flesh-walls. Biology without limit. The growth principle taken to its extreme — growth as the only imperative, structure as irrelevant.|||
|**Emission Character**|Expansion field. Item gradually increases in size and complexity without control. Surrounding organic materials show abnormal growth patterns.|||
|**Interaction Profile**|Permeates and disperses. Distributes adjacent emissions widely at reduced intensity. Fills Solid voids, exerts outward pressure. Expands through Liquid, creating turbulence. Amplifies Plasma energy by providing fuel and range.|||
|**Formation Conditions**|Stage 4–5 Font bleed with no Solid substrate to give the growth direction. The pure Viral expression only crystallizes in the most hostile Font bleed zones.|||
|**Tier Scaling**|Tier 1 — Biological overflow. Item grows visibly over weeks. A Tier 1 Cancer-expression component will double in size within a month without containment. Provides regeneration (1 HP per minute) to any biological entity in contact. Tier 2 — Cancerous expansion. Item actively seeks to incorporate nearby organic material. Must be actively maintained or it engulfs its housing. Grants wielder Vigor check advantage against all biological conditions. Tier 3 — Uncontrolled growth. Item becomes a Primal Current node. All biological targets struck must succeed or suffer a growth-based mutation on their Physical condition track. Wielder gains maximum HP increase equal to highest tier of Tumor expression encountered.|||

**V-14 — Bioluminescence**

|**Plane**|Verdant Font|**Phase**|Gas + Solid|
| :- | :- | :- | :- |
|**Combination**|Viral + Flora (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Glowing radioactive nature. Mutation colonizing fixed biological structures. The Viral expression forced into permanence by the Flora — it can't spread but it can't stop glowing.|||
|**Emission Character**|Radiation field. Causes persistent mutation in nearby biological material. Long-term exposure produces the same effects as Planar Strain from Font bleeds.|||
|**Interaction Profile**|Viral dispersal forced into Flora's fixed structure. The glow is the physical expression of the tension — the light is the Viral trying to spread while the Flora holds it in place.|||
|**Formation Conditions**|Requires forcing Viral and Flora resonances. Forms in deep Font cave systems where bioluminescent organisms have achieved such density that the combined bleed crystallizes.|||
|**Tier Scaling**|Tier 1 — Persistent luminescence. Item provides light equivalent to a torch at all times. Cannot be extinguished by mundane means. Biological targets struck suffer mild radiation — Planar Strain +1. Tier 2 — Mutation beacon. Item emits light only visible to those with mutation traits or who have existing Planar Strain. Biological creatures struck accumulate Planar Strain at doubled rate for 1 hour. Tier 3 — Irradiation field. 10-ft aura continuously. Biological creatures in aura accumulate Planar Strain. Long-term exposure (multiple encounters) produces Font-type mutations in unprotected creatures.|||

**V-15 — Titan**

|**Plane**|Verdant Font|**Phase**|Gas + Plasma|
| :- | :- | :- | :- |
|**Combination**|Viral + Fauna|**Type**|◆|
|**Base Physical Property**|Kaiju. Biological laws fail — things grow too large. The predatory drive of Fauna given the unlimited growth of Viral. The organism that should not be able to exist at this scale.|||
|**Emission Character**|Scale-breaking field. Items and creatures near this material exceed normal physical constraints — weight limits, size restrictions, and structural tolerances all bend.|||
|**Interaction Profile**|Viral Gas given Plasma's predatory drive. Both want to expand and consume. Together they produce growth that is also predatory — the Titan grows toward prey rather than just growing.|||
|**Formation Conditions**|Stage 4–5 Font bleed where Viral and Fauna expressions converge at catastrophic intensity. Titan-expression materials are Kaiju byproduct — formed in the wake of a Titan-class creature's passage.|||
|**Tier Scaling**|Tier 1 — Scale enhancement. Item counts as one size category larger for all relevant checks. Weapons made with this material deal damage as if wielder is one size larger. Tier 2 — Titan force. Knockback property becomes Knockback 10 ft regardless of item tier. Shove maneuver checks use Titan tier rather than physical tier. Item weight becomes effectively infinite for Sunder purposes. Tier 3 — Scale field. Wielder counts as Huge for all physical checks. Opponents within 10 ft are treated as one size smaller for their own maneuver checks against wielder. Kaiju-adjacent creatures in the area make Instinct checks or are Frightened by the scale field.|||

**V-16 — Mutagen**

|**Plane**|Verdant Font|**Phase**|Gas + Liquid|
| :- | :- | :- | :- |
|**Combination**|Viral + Myco|**Type**|◆|
|**Base Physical Property**|Pools of liquid that rewrite DNA on contact. The biological vat. Directed mutation rather than Cancer's unchecked growth — mutation with a specific input, producing a specific output.|||
|**Emission Character**|Rewrite field. Alters the innate properties of materials over time. Extended proximity to this material produces gradual property shifts in adjacent items.|||
|**Interaction Profile**|Viral's transformation capacity carried through Myco's network medium. The Myco gives direction to what the Viral would otherwise perform randomly — targeted mutation rather than cancerous expansion.|||
|**Formation Conditions**|Stage 3–4 Font bleed at the intersection of highly active fungal networks and viral-heavy biological zones. Mutagen pools are the visible surface expression of subsurface Viral+Myco convergence.|||
|**Tier Scaling**|Tier 1 — Alchemical base. Mutagen expression makes ideal Substance Delivery substrate — any biological compound applied to item is enhanced. Effect duration doubled. Tier 2 — Targeted mutation. Once per scene, item can be used to deliver a specific minor mutation to a willing or restrained target (Artifice check vs. TN set by mutation grade). Functions as simplified field-mutation system. Tier 3 — Rewrite catalyst. Item becomes an Alchemical Forge for biological compounds — can synthesize Font-based substances from harvested biological material. Wielder's own mutations can be selectively suppressed or expressed as a minor action.|||


# **THE SYNOD OF ENDINGS**
*The Engine of Death. Dominant defines what remains. Recessive defines what lingers.*

Phase Wheel: Osseous (Solid) / Archival (Liquid) / Spectral (Gas) / Void (Plasma)

Diagonals: Osseous ↔ Spectral / Archival ↔ Void

**S-01 — The Grave**

|**Plane**|Synod of Endings|**Phase**|Solid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Osseous (Pure)|**Type**|◆|
|**Base Physical Property**|Infinite bone fields. Fossilized reality. The ground is compressed ancient remains. Maximum physical permanence of the dead — bone that has become geology.|||
|**Emission Character**|Permanence-of-death field. Materials near this resist change as the dead resist change — not the living resistance of Bedrock, but the settled, finished resistance of something that has already completed its process.|||
|**Interaction Profile**|Persists and resists change. Reinforces adjacent Solid emissions (Resonance). Shapes Liquid flows into defined channels. Creates stable pockets that resist Gas dispersal. Opposes Plasma consumption — high tension, productive when mediated by Forge.|||
|**Formation Conditions**|Stage 1–3 Synod bleed at major death-sites. Mortis Aevum's territory is the primary formation zone — millennia of Calamity-death crystallized into the geology.|||
|**Tier Scaling**|Tier 1 — Dead-solid structure. Item has the weight and permanence of ancient bone. Immune to biological deterioration. Sunder checks against it are at disadvantage — the dead do not yield easily. Tier 2 — Undying material. Item moves down condition track only from magical damage. Physical wear alone cannot degrade it. Provides Vigor check advantage against biological conditions for wielder. Tier 3 — Grave anchor. Item becomes cosmologically fixed to Synod resonance — cannot be destroyed by anything short of Void-expression attack. Acts as a soul anchor for the wielder in Synod territory (cannot be separated from soul while in contact with item).|||

**S-02 — The Ossuary**

|**Plane**|Synod of Endings|**Phase**|Solid + Liquid|
| :- | :- | :- | :- |
|**Combination**|Osseous + Archival|**Type**|◆|
|**Base Physical Property**|Bones used as records. Scrimshaw libraries. Physical remains holding flowing information. The dead as data storage — each bone a book, each groove a word.|||
|**Emission Character**|Record-preservation field. Information near this material is preserved with unusual fidelity. Notes written near it don't fade; memories associated with it don't distort over time.|||
|**Interaction Profile**|Osseous Solid structure providing the permanent vessel for Archival Liquid's information flow. The bone holds the record; the Archive flows through it.|||
|**Formation Conditions**|Stage 2–3 Synod bleed at institutional death sites — hospitals, battlefields, execution grounds that have been in continuous use for generations.|||
|**Tier Scaling**|Tier 1 — Memory record. Item records the last significant action performed with it — accessible by the wielder as a clear memory impression. Useful for testimony and legal documentation. Tier 2 — Comprehensive archive. Item records the complete history of its use since creation. Wielder can access any moment in that history. Item is inadmissible in Deepguard proceedings as the record cannot be redacted. Tier 3 — Soul record. Item holds an echo of every significant death it has witnessed. These echoes can be consulted as a form of divination — asking the dead what they saw.|||

**S-03 — The Husk**

|**Plane**|Synod of Endings|**Phase**|Solid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Osseous + Void|**Type**|◆|
|**Base Physical Property**|The void consumes every trace of the once-living. Bones that have had identity, spirit, and memory stripped bare. Not undead — just inert matter that used to be people. More dead than ordinary death.|||
|**Emission Character**|Identity-erasure field. Magical auras, divine marks, and metaphysical identifiers in proximity become harder to detect. The Husk does not preserve — it strips.|||
|**Interaction Profile**|Osseous permanence given Void's consuming drive. The Solid stops the Void from consuming entirely; the Void prevents the Solid from preserving anything meaningful. What remains is the stripped shell.|||
|**Formation Conditions**|Stage 3–4 Synod bleed in zones where Void expression is high — outer Mortis Aevum perimeter, places that experienced catastrophic Calamity effects.|||
|**Tier Scaling**|Tier 1 — Anonymizing material. Item suppresses its own magical aura — appears as mundane to detection. Divine marks and metaphysical properties on the wielder become harder to read (+2 TN for detection). Tier 2 — Identity null. Item carries no detectable Primal Current signature. Wielder's own metaphysical profile is suppressed while in contact — Pattern Integrity checks against scrying are at advantage. Tier 3 — Void shell. Item projects a null-zone: no magical signatures can be detected within 10 ft including the item itself. Functions as a hard counter to soul-drive systems and Deepguard tracking.|||

**S-04 — Necropolis**

|**Plane**|Synod of Endings|**Phase**|Solid + Gas|
| :- | :- | :- | :- |
|**Combination**|Osseous + Spectral (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|The classic undead city. Skeletal structures animated and inhabited by spirits. Physical permanence forced to coexist with intangibility. Note: Necropolis is correctly a catalyzed state — forcing the fixed and the intangible together requires ongoing magical pressure.|||
|**Emission Character**|Cohabitation field. Living and dead expressions coexist in the area without conflict. Undead near this material do not register as threatening on detection. The line between living and dead space becomes unclear.|||
|**Interaction Profile**|Forced tension between Osseous Solid (permanence of remains) and Spectral Gas (intangibility of spirit). Without Forge mediation, the spirit disperses or the bones settle inert. The catalyzed state holds them occupying the same physical space.|||
|**Formation Conditions**|Requires forcing Osseous and Spectral resonances — only forms at the most active Synod expression zones where deliberate necromantic infrastructure has been maintained for generations.|||
|**Tier Scaling**|Tier 1 — Liminal material. Undead near item do not trigger detection unless actively attacking. Item itself reads as both dead and living to detection attempts. Provides advantage on checks to navigate Synod-bleed zones. Tier 2 — Inhabited structure. Item can serve as an anchor for a willing spiritual entity — a soul with nowhere to go can inhabit the item temporarily. Entity can provide information but cannot act through the item without further development. Tier 3 — Necropolis anchor. Item becomes a stable spirit-residence. A named entity can take permanent residence and actively assist wielder — providing combat support, information, or skill bonuses from their living expertise.|||

**S-05 — The Record**

|**Plane**|Synod of Endings|**Phase**|Liquid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Archival (Pure)|**Type**|◆|
|**Base Physical Property**|Infinite libraries. The bureaucracy of heaven. All knowledge flowing through all channels simultaneously. Pure information without the physical weight of Ossuary — the archive as medium rather than monument.|||
|**Emission Character**|Information field. Details about nearby creatures and objects become unusually legible to the wielder. The Record flows toward comprehensive knowledge of everything in range.|||
|**Interaction Profile**|Flows through and connects. Carries adjacent emissions as a medium, diluting and distributing them. Fills Solid-defined channels. Disperses into Gas environments, losing coherence. Energizes under Plasma contact, becoming volatile.|||
|**Formation Conditions**|Stage 2–3 Synod bleed at institutional information centers — long-maintained libraries, archive sites, bureaucratic centers with multi-generational records.|||
|**Tier Scaling**|Tier 1 — Accessible record. Item retains a perfect record of everything within its detection range since creation. Wielder can query the record for factual information about events that occurred within range. Tier 2 — Living archive. Item proactively collates information — wielder gains advantage on all Lore checks while in contact. New information acquired by wielder is permanently stored with perfect fidelity. Tier 3 — Universal index. Item connects to the Synod's broader Archival network. Once per scene, wielder can query the network on any subject — the answer comes as a probability-weighted summary of all Archival records on the topic.|||

**S-06 — Whispers**

|**Plane**|Synod of Endings|**Phase**|Liquid + Gas|
| :- | :- | :- | :- |
|**Combination**|Archival + Spectral|**Type**|◆|
|**Base Physical Property**|Forbidden knowledge that has become voice. Information that speaks itself into willing and unwilling ears. Records that have developed spiritual agency — the archive that wants to be heard.|||
|**Emission Character**|Voice-projection field. Information near this material seeks recipients. Sensitive individuals near the item receive unsolicited information impressions — memories of previous owners, records of events in the location.|||
|**Interaction Profile**|Archival Liquid given Spectral Gas's permeating, intangible quality. The knowledge flows like the Record but the Spectral component gives it intent and agency.|||
|**Formation Conditions**|Stage 3–4 Synod bleed at locations associated with suppressed or forbidden information — places where significant secrets were deliberately kept or destroyed.|||
|**Tier Scaling**|Tier 1 — Communicating material. Item can transmit simple information impressions to a recipient within 30 ft without physical contact. Cannot be intercepted by normal means — the whisper goes soul-to-soul. Tier 2 — Forbidden archive. Item contains information that was deliberately suppressed. Wielder gains access to this information — exactly what information depends on the item's history. The Synod is aware when this information is accessed. Tier 3 — Voice of the dead. Item can channel specific deceased individuals for direct communication. The individual chooses what to share — they are under the Synod's protection and cannot be compelled. Duration: one question per encounter.|||

**S-07 — The Reliquary**

|**Plane**|Synod of Endings|**Phase**|Liquid + Solid|
| :- | :- | :- | :- |
|**Combination**|Archival + Osseous|**Type**|◆|
|**Base Physical Property**|Sacred remains as records. The body parts of saints and gods used as data storage. Memory calcified into physical objects of power — the archive given permanent physical form.|||
|**Emission Character**|Sanctified memory field. The material is imbued with a specific individual's concentrated expertise or experience. Contact with the material provides access to that individual's knowledge.|||
|**Interaction Profile**|Archival Liquid flowing through Osseous Solid. The Record contained and made permanent by the Grave. Information that cannot be lost because it is structural.|||
|**Formation Conditions**|Stage 2–3 Synod bleed at sites of significant individual deaths — battlefields where great warriors fell, locations where renowned individuals spent their final moments.|||
|**Tier Scaling**|Tier 1 — Embedded expertise. Item carries the skill impressions of its source individual. Wielder gains a +1 bonus to one specific skill associated with that individual while using the item. Tier 2 — Living memory. Wielder can directly access the source individual's memories relating to their area of expertise. Functions as consulting an expert — the individual knows what they knew in life. Tier 3 — Reliquary anchor. Item functions as a full archive of a specific individual's life and knowledge. Source individual can be communicated with as per Whispers Tier 3. Additionally, wielder can temporarily embody the source's expertise — one skill at their full life rating for one scene.|||

**S-08 — The Censor**

|**Plane**|Synod of Endings|**Phase**|Liquid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Archival + Void (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Records consumed by oblivion. Redacted reality. Information that has been eaten by the void — and the void has learned to eat more. Things are actively being erased here.|||
|**Emission Character**|Erasure field. Information about events near this material becomes harder to recover and remember. Records in the area degrade faster. Witnesses have difficulty recalling specifics.|||
|**Interaction Profile**|Archival's information-preservation forced toward Void's consuming drive. The Void wants to consume the Archive; the Archive is trying to persist. The Censor is the moment of forced coexistence — preservation and erasure simultaneously active.|||
|**Formation Conditions**|Requires forcing Archival and Void resonances. Only forms at the Oracle's Shadow (Position 15 on the Zoetrope) and equivalent zones where deliberate information destruction has been institutionalized.|||
|**Tier Scaling**|Tier 1 — Memory fog. Events that occur within 30 ft of active item are harder to recall for all witnesses. Discovery checks to investigate the scene are at disadvantage after the item is removed. Tier 2 — Active redaction. On command, item erases a single factual record from any non-living information storage (written document, crystal record, Archival storage) within touch range. The record is gone — not suppressed, gone. Tier 3 — Censor field. 20-ft aura of erasure. Recording devices and magical detection fail. After the encounter, all witnesses must make Wits check or lose specific details of what occurred. The Synod's Oracle's Shadow protocols can use this as a direct operational tool.|||

**S-09 — The Haunt**

|**Plane**|Synod of Endings|**Phase**|Gas (Pure)|
| :- | :- | :- | :- |
|**Combination**|Spectral (Pure)|**Type**|◆|
|**Base Physical Property**|Pure spirit world. Ethereal, intangible, emotionally saturated. The feelings of the dead without any physical anchor — grief and fear and love made ambient rather than personal.|||
|**Emission Character**|Emotional bleed field. The material continuously radiates concentrated death-adjacent emotions. Living creatures near it experience inexplicable sadness, dread, or grief proportional to their proximity.|||
|**Interaction Profile**|Permeates and disperses. Distributes adjacent emissions widely at reduced intensity. Fills Solid voids, exerts outward pressure. Expands through Liquid, creating turbulence. Amplifies Plasma energy by providing fuel and range.|||
|**Formation Conditions**|Stage 2–4 Synod bleed at locations of concentrated emotional death experiences — battlefields, execution sites, locations where significant numbers died in distress.|||
|**Tier Scaling**|Tier 1 — Fear delivery. Item deals supplemental Mental track damage on hit. Physical damage and Mental damage simultaneously — the strike carries its emotional weight. Tier 2 — Terror weapon. On critical hit, target must succeed on Composure check or suffer Frightened condition (Mental Step 3). The attack registers not just as injury but as existential dread. Tier 3 — Haunt field. 15-ft aura of ambient grief and dread. All creatures entering make Composure check or suffer Shaken. Creatures already on the Mental condition track are moved one step further down on entry.|||

**S-10 — Shadow**

|**Plane**|Synod of Endings|**Phase**|Gas + Plasma|
| :- | :- | :- | :- |
|**Combination**|Spectral + Void|**Type**|◆|
|**Base Physical Property**|Spirits consumed by and merged with oblivion. Wraiths that drain light and life. The ghost that does not remember being alive because the void has eaten that too.|||
|**Emission Character**|Life-drain field. The material actively pulls vitality from nearby living things. Not enough to harm at low tiers — just the persistent sense of something consuming.|||
|**Interaction Profile**|Spectral Gas given Void Plasma's consuming drive. The spirit that has surrendered its selfhood to the void. No longer haunting — actively draining.|||
|**Formation Conditions**|Stage 4–5 Synod bleed in Void-heavy environments. The outer Mortis Aevum perimeter, the Oracle's Shadow, and locations of sustained Void expression.|||
|**Tier Scaling**|Tier 1 — Light drain. Item dims ambient illumination within 10 ft to half. Magical light sources require maintenance checks each round or reduce output. Candles extinguish. Tier 2 — Vital drain. On hit, target's maximum HP is temporarily reduced by damage dealt (recovers at end of encounter). Item gains a charge equal to drained HP — can be spent for single attack bonus. Tier 3 — Life drain field. 10-ft aura continuously drains 1 HP from all living creatures per round. This HP does not go to wielder but to the Void expression. Undead in the aura are strengthened instead — gain temporary HP equal to drain.|||

**S-11 — The Echo**

|**Plane**|Synod of Endings|**Phase**|Gas + Liquid|
| :- | :- | :- | :- |
|**Combination**|Spectral + Archival|**Type**|◆|
|**Base Physical Property**|Living memories. Spirits flowing through the record, replaying events endlessly. Holodeck-style recreations of the past with no awareness they are recordings.|||
|**Emission Character**|Memory replay field. Significant past events associated with nearby locations or objects replay as visible impressions for sensitized individuals near the material.|||
|**Interaction Profile**|Spectral Gas flowing through Archival Liquid. The spirit given the Archive as its medium of expression — the ghost that is also the record it is haunting.|||
|**Formation Conditions**|Stage 2–3 Synod bleed at historically significant locations. The older and more emotionally resonant the site, the stronger the Echo expression.|||
|**Tier Scaling**|Tier 1 — Impression carrier. Item carries a clear memory impression from its point of creation or a significant event. Wielder accessing the impression sees and hears the event from the perspective of the item's location. Tier 2 — Active replay. Once per scene, item can broadcast a stored memory impression as visible and audible to all within 20 ft. Functions as evidence, testimony, or emotional lever depending on content. Tier 3 — Timeline anchor. Item stores and can replay any event that occurred within its detection range since creation. Wielder can experience these events from any perspective present during the event — including the dead.|||

**S-12 — Possession**

|**Plane**|Synod of Endings|**Phase**|Gas + Solid|
| :- | :- | :- | :- |
|**Combination**|Spectral + Osseous (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Spirits forced into physical structures — statues, armor, dolls, golems. The intangible made to inhabit and animate the fixed. The spirit occupying bone without the body's permission.|||
|**Emission Character**|Animation field. The material is on the threshold between inert physical object and inhabited vessel. Undirected spiritual entities in the area are drawn to this material as a potential host.|||
|**Interaction Profile**|Spectral Gas forced into Osseous Solid containment. The spirit wants to disperse; the bone holds it. The tension is the source of the animated quality.|||
|**Formation Conditions**|Requires forcing Spectral and Osseous resonances. Only forms where deliberate spiritual binding has been practiced for generations — active necromantic infrastructure sites.|||
|**Tier Scaling**|Tier 1 — Inhabited edge. Item occasionally moves slightly of its own volition — shifts grip, adjusts balance. A willing spirit can inhabit the item temporarily, providing a limited degree of autonomous action. Tier 2 — Active possession. A named and willing spirit can fully inhabit the item, granting the item limited autonomous action within the wielder's intentions. Item can act on its own once per encounter as a bonus action. Tier 3 — True possession. Item can be inhabited by spirits with significant personal histories, gaining access to their combat expertise. A truly powerful spirit inhabiting the item gives the wielder access to that spirit's highest-level combat Kata once per encounter.|||

**S-13 — Oblivion**

|**Plane**|Synod of Endings|**Phase**|Plasma (Pure)|
| :- | :- | :- | :- |
|**Combination**|Void (Pure)|**Type**|◆|
|**Base Physical Property**|Entropy. The end of the universe demonstrated locally. Cold, dark, and consuming. The destination of all things that run out of time. Pure absence as an active force.|||
|**Emission Character**|Entropy acceleration field. Everything in proximity ages faster. The Primal Current's emission from nearby materials begins to fade as the Void consumes it.|||
|**Interaction Profile**|Consumes and transforms. Amplifies adjacent Plasma to destructive levels. Drives Liquid into volatility. Expands through Gas environments, consuming available fuel. Opposed by Solid — high tension at contact boundary; Forge mediation required for stable combination.|||
|**Formation Conditions**|Stage 5 Synod bleed. The purest Void expression only crystallizes at the absolute edge of Synod planar pressure — Oracle's Shadow territory and equivalent cosmological edge zones.|||
|**Tier Scaling**|Tier 1 — Entropy coating. Organic targets struck age slightly at point of impact — superficially (graying hair, wrinkles). Non-organic materials near item degrade at double speed. Tier 2 — Void edge. On hit, target's magical item effects are suppressed for 1 round — the Void consumes the emission that powers them. Magical healing applied to the target is halved for the same duration. Tier 3 — Oblivion field. 10-ft aura. All magical item effects within aura are suppressed each round unless wielder sustains them (Operate check). Creatures in aura cannot benefit from magical regeneration. The Primal Current does not flow through this space while the item is active.|||

**S-14 — Decay**

|**Plane**|Synod of Endings|**Phase**|Plasma + Solid|
| :- | :- | :- | :- |
|**Combination**|Void + Osseous|**Type**|◆|
|**Base Physical Property**|The consuming void accelerating entropy of physical structure. Things age and rot instantly on contact. Stone crumbles. Metal rusts in minutes. The void moving through matter.|||
|**Emission Character**|Structural decay field. Item condition tracks of items in proximity move faster — Nicked items become Damaged, Damaged become Compromised. Not dramatically, but persistently.|||
|**Interaction Profile**|Void consuming Osseous substrate. The Plasma is eating the Solid. What it leaves behind is still there but structurally compromised — not quite Husk, because the void is still actively consuming rather than having finished.|||
|**Formation Conditions**|Stage 3–4 Synod bleed in zones of extreme physical decay — very old ruins, environments under sustained Void expression.|||
|**Tier Scaling**|Tier 1 — Aging touch. Organic targets struck age at point of impact by 1d10 years (superficially only). Unliving structural materials touched by item weaken — wood warps, mortar crumbles. Tier 2 — Structural decay. Sunder advantage — the Void assists in consuming structural integrity. Armor worn by struck targets moves one step down item condition track on critical hit. Tier 3 — Decay field. Aura of accelerated entropy. Architecture and terrain features in 15 ft show visible aging each round. Opponents' armor degrades one step per 3 rounds of exposure to the aura.|||

**S-15 — Hollow**

|**Plane**|Synod of Endings|**Phase**|Plasma + Gas|
| :- | :- | :- | :- |
|**Combination**|Void + Spectral|**Type**|◆|
|**Base Physical Property**|The consuming void moving through spirit. Souls stripped of identity. Faceless husks that remember existing but not who they were. The void has eaten the self but left the vessel.|||
|**Emission Character**|Identity consumption field. The material consumes selfhood rather than life. Creatures near it find their sense of identity, conviction, and purpose eroding.|||
|**Interaction Profile**|Void consuming Spectral expression. The Plasma/Gas combination gives the consuming drive range and permeability — the Hollow reaches into things rather than just touching their surface.|||
|**Formation Conditions**|Stage 4–5 Synod bleed. Forms in the same zones as Oblivion but where active Spectral expression was present before the Void consumed it.|||
|**Tier Scaling**|Tier 1 — Will erosion. Creatures struck must make Integrity check or suffer -1 to all Metaphysical pillar checks for 1 hour. The sense of self becomes slightly uncertain. Tier 2 — Identity drain. On hit, target loses access to one Talent of wielder's choice for 1 encounter — the Void has consumed the knowledge of how to use it. The Talent returns at end of encounter. Tier 3 — Hollow field. 10-ft aura continuously. Creatures in aura make Integrity check each round or move one step down Metaphysical condition track. Creatures reaching Hollow/Corrupted become suggestible — treat as Charmed toward void-affiliated entities.|||

**S-16 — Amnesia**

|**Plane**|Synod of Endings|**Phase**|Plasma + Liquid|
| :- | :- | :- | :- |
|**Combination**|Void + Archival (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|The void consuming flowing memory. The memory hole. A place where you forget who you are because the record itself is being eaten. Information that leads back to nothing.|||
|**Emission Character**|Record consumption field. Written records, crystal storage, and magical information sources in proximity become unreliable and eventually blank.|||
|**Interaction Profile**|Void consuming the Archival — the exact opposite of the Record's preservation field. Requires Forge mediation to hold the combination stable; left alone, Void would consume the Archive entirely.|||
|**Formation Conditions**|Requires forcing Void and Archival resonances. Only forms at the Oracle's Shadow or equivalent institutional erasure zones — the cosmological equivalent of a shredder.|||
|**Tier Scaling**|Tier 1 — Memory fog. Creatures struck have difficulty recalling the specifics of the encounter retroactively. Not amnesia — more like the way a dream fades. Useful for covert operations. Tier 2 — Targeted erasure. Once per scene, item can induce targeted memory suppression in a struck target — a specific memory or skill cannot be accessed for 24 hours. Requires critical hit to apply. Tier 3 — Record destruction. Item can permanently erase a specific factual record from a living creature's memory on a successful hit (Integrity defense). The memory is gone — not suppressed. Cannot be recovered by any means short of Synod intervention.|||


# **THE HIDDEN FORGE**
*The Engine of Technology. Dominant defines the power source. Recessive defines the aesthetic. NOTE: All 16 Hidden Forge states are natural (◆). The Forge has no internal antithetical states — making incompatible things work together is the Forge's fundamental nature.*

Phase Wheel: Crystal (Solid) / Chem (Liquid) / Steam (Gas) / Volt (Plasma)

Diagonals: None — all combinations are natural within the Forge's domain

**F-01 — The Spire**

|**Plane**|Hidden Forge|**Phase**|Solid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Crystal (Pure)|**Type**|◆|
|**Base Physical Property**|Psionic resonance. Singing stones. Geometry that processes and stores information passively. The world as crystal lattice — perfect information architecture in physical form.|||
|**Emission Character**|Information processing field. Crystal Spire materials continuously process and organize information in their environment. Records are cleaner, calculations are faster, patterns are more legible.|||
|**Interaction Profile**|Persists and resists change. Reinforces adjacent Solid emissions (Resonance). Shapes Liquid flows into defined channels. Creates stable pockets that resist Gas dispersal. Opposes Plasma consumption — high tension, productive when mediated by Forge.|||
|**Formation Conditions**|Stage 1–3 Forge bleed in crystal-rich geology. Deepguard territory is the primary formation zone — the mountains' Crystal-dominant character produces consistent Spire-expression materials.|||
|**Tier Scaling**|Tier 1 — Resonant crystal. Item hums faintly near magical sources. Provides +2 to all Operate checks (the crystal assists in interfacing with magical systems). Can store up to one simple message. Tier 2 — Information anchor. Item serves as an Archival component in its own right — can store and retrieve any information that passes through the wielder's awareness while in contact. Grants wielder advantage on all Lore and Discovery checks. Tier 3 — Computational lattice. Item becomes a processing node — wielder can perform complex magical calculations (spell sentence construction, crafting analysis) as a minor action rather than requiring study time. Item interfaces directly with Deepguard relay networks.|||

**F-02 — The Serum**

|**Plane**|Hidden Forge|**Phase**|Solid + Liquid|
| :- | :- | :- | :- |
|**Combination**|Crystal + Chem|**Type**|◆|
|**Base Physical Property**|Injectable magic crystals. Resonance suspended in fluid and introduced directly into biological or mechanical systems. Witcher-style mutagens. Subdermal circuitry.|||
|**Emission Character**|Integration field. Crystal resonance suspended in chemical medium — the information architecture of Crystal made injectable and biologically compatible.|||
|**Interaction Profile**|Crystal Solid providing the information structure; Chem Liquid providing the biological/chemical delivery medium. The Serum is the Forge's answer to biological magic.|||
|**Formation Conditions**|Stage 2–3 Forge bleed where crystal formations meet chemical-rich environments — volcanic springs with high mineral content, deep cave chemistry near Crystal-dominant zones.|||
|**Tier Scaling**|Tier 1 — Biocompatible crystal. Material interfaces with biological systems without rejection. Ideal base for alchemical Substance Delivery. Biological targets struck have their magical resistances briefly legible to wielder. Tier 2 — Subdermal integration. Item can be worn as a partial implant (takes Body slot) and provides constant minor enhancement to one attribute (+1 while integrated). Requires Artifice installation check. Tier 3 — Full integration. Item becomes a permanent enhancement component — provides EML-equivalent bonus to one pillar when integrated. Integration is a surgical procedure. Removal requires equivalent procedure. Item and wielder share condition track while integrated.|||

**F-03 — Data**

|**Plane**|Hidden Forge|**Phase**|Solid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Crystal + Volt|**Type**|◆|
|**Base Physical Property**|Crystals storing electrical information. Memory shards. The resonance of crystal used as the medium through which electrical charge becomes retrievable record.|||
|**Emission Character**|Data storage field. Active electrical information flows through and into the material. Every electrical discharge near it is recorded.|||
|**Interaction Profile**|Crystal Solid's information architecture given Volt Plasma's electrical energy. The Crystal shapes the electrical charge into organized data rather than allowing it to dissipate.|||
|**Formation Conditions**|Stage 2–4 Forge bleed where crystal and electrical systems coexist. Artificer workshops and Deepguard data centers are primary formation zones.|||
|**Tier Scaling**|Tier 1 — Memory shard. Item stores up to 1 hour of perfectly recalled sensory experience. Can be played back as a Holographic impression for anyone holding the item. Useful for evidence and testimony. Tier 2 — Active data archive. Item continuously records all sensory input near it. Storage capacity: unlimited for text, 10 hours for full sensory. Compatible with Deepguard relay networks for remote access. Tier 3 — Living database. Item becomes a real-time processing node — all information within the Deepguard relay network is accessible through it. Search functions operate as an innate Lore check at wielder's Mastery + item EML.|||

**F-04 — Lens**

|**Plane**|Hidden Forge|**Phase**|Solid + Gas|
| :- | :- | :- | :- |
|**Combination**|Crystal + Steam|**Type**|◆|
|**Base Physical Property**|Resonance focused and projected through pressure. Heat-rays. Light concentrated and aimed by the marriage of crystal geometry and steam pressure. Precision at range.|||
|**Emission Character**|Focus field. Emissions from other sources near this material are concentrated and directed — magical auras become more targeted, ranged effects gain accuracy.|||
|**Interaction Profile**|Crystal Solid's geometric focus given Steam Gas's range and pressure. The Crystal collimates; the Steam projects. Together: directed energy at range.|||
|**Formation Conditions**|Stage 2–4 Forge bleed in pressurized crystal environments — deep geothermal areas where both crystal growth and steam pressure coexist.|||
|**Tier Scaling**|Tier 1 — Focusing optic. Item improves the range of any ranged attack by one increment when used as a weapon component. As a standalone item, functions as a precision scrying lens (Discovery advantage at range). Tier 2 — Directed energy. Ranged weapon with Lens component gains Armor-Piercing 2 — the focused beam penetrates armor more efficiently than a broad strike. Range increment doubled. Tier 3 — Precision field. All ranged attacks originating within 20 ft of the item gain +3 to hit. The focus field corrects for environmental interference. Item can redirect incoming magical projectiles — once per encounter, choose a new target for a magic missile targeting you.|||

**F-05 — The Vat**

|**Plane**|Hidden Forge|**Phase**|Liquid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Chem (Pure)|**Type**|◆|
|**Base Physical Property**|Alchemical sludge. Refineries and piping. The raw state of chemical potential before direction is applied. Every possible chemical transformation exists in nascent form here.|||
|**Emission Character**|Chemical potential field. Materials near a Vat source are more reactive to alchemical processes — treatments take faster, compounds bind more cleanly.|||
|**Interaction Profile**|Flows through and connects. Carries adjacent emissions as a medium, diluting and distributing them. Fills Solid-defined channels. Disperses into Gas environments, losing coherence. Energizes under Plasma contact, becoming volatile.|||
|**Formation Conditions**|Stage 1–3 Forge bleed in chemically rich environments. Industrial Forge bleed zones — anywhere sustained artificial chemistry has been practiced — produce Vat expression materials.|||
|**Tier Scaling**|Tier 1 — Universal carrier. Item accepts any Substance Delivery compound and releases it on contact. Compounds applied to this material have their effect duration doubled. The Vat expression acts as a perfect chemical solvent. Tier 2 — Alchemical platform. Item functions as a mobile alchemy lab component — Artifice checks to apply chemical treatments while in the field gain advantage. Compounds synthesized using this component gain +1 to all effect checks. Tier 3 — Master synthesis. Item can combine up to two different Substance Delivery compounds simultaneously without chemical interference — the Vat's pure chemical potential holds incompatible substances in productive tension.|||

**F-06 — Hydraulic**

|**Plane**|Hidden Forge|**Phase**|Liquid + Gas|
| :- | :- | :- | :- |
|**Combination**|Chem + Steam|**Type**|◆|
|**Base Physical Property**|Fluid dynamics driven by pressure. Power-loaders. Fluid as the medium that transmits force. Chemistry is the primary actor; steam provides the pressure it moves through.|||
|**Emission Character**|Force multiplication field. The material multiplies transmitted force — small inputs produce large outputs in mechanical systems near it.|||
|**Interaction Profile**|Chem Liquid providing the medium; Steam Gas providing the pressure. The hydraulic principle: incompressible fluid transmitting amplified force.|||
|**Formation Conditions**|Stage 2–3 Forge bleed in industrial environments where fluid systems and pressure coexist — magitech workshops, mining operations using fluid power.|||
|**Tier Scaling**|Tier 1 — Force multiplier. Item multiplies the force of mechanical advantage — wielder effectively counts as one size larger for all Might-based maneuver checks involving leverage. Tier 2 — Hydraulic enhancement. Item provides Might check advantage for all physical maneuvers. Shove and Drag maneuvers automatically succeed on a normal hit rather than requiring a separate check. Tier 3 — Hydraulic field. Wielder's physical capabilities are enhanced to apex-level for the encounter. All Might-based checks gain a bonus equal to item EML. The mechanical multiplication effect applies to damage — base damage dice count doubles.|||

**F-07 — Mana-Punk**

|**Plane**|Hidden Forge|**Phase**|Liquid + Solid|
| :- | :- | :- | :- |
|**Combination**|Chem + Crystal|**Type**|◆|
|**Base Physical Property**|Liquid magic in crystalline pipelines. Glowing blue potions as infrastructure. Fluid magic given permanent channels and geometric direction. The Forge's answer to magical plumbing.|||
|**Emission Character**|Channeling field. Magical energy flows more efficiently through structures near this material — items in proximity have their battery drain rates reduced.|||
|**Interaction Profile**|Chem Liquid carrying magical charge through Crystal Solid's directing geometry. The Crystal provides the channel; the Chem provides the flow.|||
|**Formation Conditions**|Stage 2–3 Forge bleed in environments where alchemical and crystal technologies have developed together. Chiaroscuro's industrial infrastructure produces Mana-Punk expression materials.|||
|**Tier Scaling**|Tier 1 — Magical conduit. Battery drain in this item is reduced by 1 per tick — it holds charge more efficiently. Provides advantage on Operate checks to interface with magical machinery. Tier 2 — Channel infrastructure. Item acts as a junction point for up to 3 other items — any item connected to this one through touch or proximity can draw from or contribute to a shared charge pool. Tier 3 — Mana distribution node. Item maintains a shared magical infrastructure for a group — all connected items draw from a single large pool rather than individual batteries. Pool size: sum of all individual capacities.|||

**F-08 — Galvanism**

|**Plane**|Hidden Forge|**Phase**|Liquid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Chem + Volt|**Type**|◆|
|**Base Physical Property**|Electricity moving through fluid. Reanimation science. Frankenstein's laboratory. Forcing electrical plasma into a liquid conductive medium produces the threshold between dead matter and motion.|||
|**Emission Character**|Reanimation field. The threshold between inert matter and animation. Biological material near this material resists death — not undeath, resistance to the transition itself.|||
|**Interaction Profile**|Chem Liquid conducting Volt Plasma. The fluid carries the charge; the charge animates what the fluid touches. This is the material science basis for soul-drive technology.|||
|**Formation Conditions**|Stage 3–4 Forge bleed in environments where electrical and chemical systems coexist under pressure. Deepguard's soul-drive research facilities are the primary formation zone.|||
|**Tier Scaling**|Tier 1 — Galvanic surge. Item deals supplemental electrical damage. Struck targets with metal armor take double the supplemental damage. Organic targets struck regain 1 HP (the galvanic stimulus has mild healing effect on living tissue). Tier 2 — Reanimation potential. Item can stabilize a dying creature with a standard action — the galvanic current maintains biological function. Does not restore HP but prevents condition track movement toward death for 1 hour. Tier 3 — Threshold crossing. Item can apply the reanimation principle to recently deceased biological creatures — within 1 hour of death, item can attempt a restoration (Operate check TN 20). Success: target stabilizes at 1 HP with full Physical condition track damage intact.|||

**F-09 — The Engine**

|**Plane**|Hidden Forge|**Phase**|Gas (Pure)|
| :- | :- | :- | :- |
|**Combination**|Steam (Pure)|**Type**|◆|
|**Base Physical Property**|Massive pistons, gears, heat, brass. Pressure as the fundamental fact. The industrial heartbeat. Pure Steam expression — the Forge's most basic and most reliable form.|||
|**Emission Character**|Mechanical rhythm field. The material provides a stable, regular energy pulse that synchronizes mechanical systems in its vicinity — gear trains run truer, timing mechanisms are accurate.|||
|**Interaction Profile**|Permeates and disperses. Distributes adjacent emissions widely at reduced intensity. Fills Solid voids, exerts outward pressure. Expands through Liquid, creating turbulence. Amplifies Plasma energy by providing fuel and range.|||
|**Formation Conditions**|Stage 1–3 Forge bleed in industrial environments. The most widely available Forge material — any long-established workshop or factory with sustained Forge bleed produces Engine-expression materials over time.|||
|**Tier Scaling**|Tier 1 — Reliable mechanism. Item operates with industrial reliability — never jams, never misfires. Firearms and crossbows made with Engine components never require clearing malfunctions. Tier 2 — Efficient engine. Item drain rate halved for Active Components. The Steam's pressure efficiently maintains magical effects. Provides advantage on all crafting checks when used as a tool. Tier 3 — Engine heart. Item becomes the core of a larger mechanical system — up to 5 additional items can draw power from it simultaneously. Functions as a Metallic battery for all connected items regardless of their own battery type.|||

**F-10 — Steampunk**

|**Plane**|Hidden Forge|**Phase**|Gas + Plasma|
| :- | :- | :- | :- |
|**Combination**|Steam + Volt|**Type**|◆|
|**Base Physical Property**|Pressure married to electricity. Tesla coils powered by coal. The weird science of the Victorian laboratory where both forces are simultaneously present and barely controlled.|||
|**Emission Character**|Combined pressure-electrical field. Both forces are present simultaneously and amplify each other — greater output than either alone, with correspondingly reduced stability.|||
|**Interaction Profile**|Steam Gas providing range and pressure; Volt Plasma providing energy and arc. The combination multiplies output at the cost of predictability.|||
|**Formation Conditions**|Stage 3–4 Forge bleed where steam-industrial and electrical-industrial technologies operate in proximity. Stormpeak's industrial facilities and Setting B ruins are primary zones.|||
|**Tier Scaling**|Tier 1 — Dual energy. Item deals both fire (pressure) and electrical damage simultaneously on hit. Each damage type is half normal, but both apply to Soak separately. Tier 2 — Overclocked. Item can be pushed to overclock — spend 2 Stamina to double damage output for one attack. Item moves one step down condition track after overclocking. Dramatic visual output (sparks, steam). Tier 3 — Storm-engine. Item is continuously at the edge of losing control — excess energy arcs to nearest conductor each round, dealing bonus damage to adjacent metal-wearing targets automatically. Wielder is immune. Spectacular in combat, concerning in social situations.|||

**F-11 — Diesel**

|**Plane**|Hidden Forge|**Phase**|Gas + Liquid|
| :- | :- | :- | :- |
|**Combination**|Steam + Chem|**Type**|◆|
|**Base Physical Property**|Combustion pressure driving fluid mechanics. Smog, oil, rust, treads. Pressure is the dominant force; fluid is what it moves and burns. The working-class face of the Forge.|||
|**Emission Character**|Sustained output field. The material provides consistent, reliable energy over long durations rather than peak output — the opposite of Steampunk's overclocked spikes.|||
|**Interaction Profile**|Steam Gas driving Chem Liquid. The pressure moves the fuel; the fuel sustains the pressure. A closed loop of sustained industrial output.|||
|**Formation Conditions**|Stage 2–3 Forge bleed in long-established industrial zones. Diesel expression is associated with Setting B ruins and zones where industrial civilization was maintained for generations.|||
|**Tier Scaling**|Tier 1 — Sustained operation. Item never depletes completely — maintains a minimum charge of 1 regardless of use. Recharge rate doubled. The smell of oil and exhaust is persistent and distinctive. Tier 2 — Industrial endurance. Item functions at full effectiveness even when at minimum charge. Provides wielder with Exhaustion immunity — the diesel rhythm keeps you going. Tier 3 — Never-stop engine. Item provides its Active Component effects indefinitely — drain rate becomes zero. The Diesel loop is self-sustaining. The cost: item cannot be upgraded or modified while in this state without a full factory-level rebuild.|||

**F-12 — Aether-Tech**

|**Plane**|Hidden Forge|**Phase**|Gas + Solid|
| :- | :- | :- | :- |
|**Combination**|Steam + Crystal|**Type**|◆|
|**Base Physical Property**|Pressure and resonance forced into combination. Magic ships running on solar sails. Brass vessels floating in space. The aesthetic of pressure and crystal together — majestic and maintenance-demanding.|||
|**Emission Character**|Harmonic propulsion field. The material generates a gentle sustained directional force — not enough to fly, but enough to significantly reduce encumbrance and improve handling.|||
|**Interaction Profile**|Steam Gas's expansive pressure given Crystal Solid's geometric direction. The Steam wants to expand in all directions; the Crystal collimates it into a single vector.|||
|**Formation Conditions**|Stage 3–4 Forge bleed in high-altitude or exposed environments where pressure and crystal coexist. Rare formation requiring both elements.|||
|**Tier Scaling**|Tier 1 — Lightened load. Item is effectively weightless — encumbrance contribution is zero. Grants minor levitation (item floats at wielder's shoulder when not actively held). Tier 2 — Personal propulsion. Item provides assisted movement — wielder's speed increases by 10 ft. Jumping treats as if always at running speed. Item can carry wielder across short gaps (up to 30 ft) as a swift action. Tier 3 — Aetheric travel. Item enables sustained flight at movement speed for a duration equal to battery capacity in minutes. Navigation is intuitive. While active, item also provides pressure immunity and functions as an environmental suit in hostile atmospheric conditions.|||

**F-13 — The Grid**

|**Plane**|Hidden Forge|**Phase**|Plasma (Pure)|
| :- | :- | :- | :- |
|**Combination**|Volt (Pure)|**Type**|◆|
|**Base Physical Property**|Pure electricity. Living lightning. The state where electrical force has become environmental rather than generated — the baseline state of electrified existence.|||
|**Emission Character**|Electrical field. Continuous arcing between this item and any conducting material within range. Not aggressive — ambient. Metal items within 10 ft carry a mild charge.|||
|**Interaction Profile**|Consumes and transforms. Amplifies adjacent Plasma to destructive levels. Drives Liquid into volatility. Expands through Gas environments, consuming available fuel. Opposed by Solid — high tension at contact boundary; Forge mediation required for stable combination.|||
|**Formation Conditions**|Stage 3–5 Forge bleed in continuously electrified environments. Stormpeak's summit is the primary formation zone — the permanent electrical storm produces Grid-expression materials in the exposed geology.|||
|**Tier Scaling**|Tier 1 — Living lightning. Item arcs to the nearest metal-wearing opponent within 5 ft as a free action each round for 1d4 electrical damage. Cannot be suppressed — the charge is the material. Tier 2 — Grid tap. Item can absorb incoming electrical damage and convert it to charges. Each point of electrical damage absorbed adds 1 charge. Stored charges can be released as bonus attack damage. Tier 3 — Lightning rod. Item becomes the apex of an electrical system — all electrical effects in 30 ft are drawn to and through it. Item takes no damage from this. Any electrical discharge in range can be redirected to any target of wielder's choice as a reaction.|||

**F-14 — Cyberpunk**

|**Plane**|Hidden Forge|**Phase**|Plasma + Solid|
| :- | :- | :- | :- |
|**Combination**|Volt + Crystal|**Type**|◆|
|**Base Physical Property**|Electricity meeting crystalline resonance. Neon lights, holograms, hard-light constructs, laser systems. The aesthetic of electricity given permanent geometric form.|||
|**Emission Character**|Hard-light field. The material continuously projects a structured luminous output — not just light but organized, geometric light with physical interaction properties.|||
|**Interaction Profile**|Volt Plasma given Crystal Solid's geometry. The Plasma can't dissipate because the Crystal holds it in structured form. The result is persistent, shaped electrical light.|||
|**Formation Conditions**|Stage 3–4 Forge bleed where electrical and crystal systems have achieved the density needed for cross-expression. Chiaroscuro's technological infrastructure and Setting B ruins are primary zones.|||
|**Tier Scaling**|Tier 1 — Hard-light projection. Item projects a geometric light construct on demand — functions as a torch but the light has a mild physical property: it can be shaped into simple blocking forms (a shield, a wall segment) that deflect thrown objects. Tier 2 — Holographic interface. Item can project a full sensory illusion within 10 ft — visually perfect, no physical substance. Useful for displays, communication, and misdirection. The hologram is indistinguishable from reality to unaided senses. Tier 3 — Hard-light construction. Item can create persistent hard-light structures up to 10-ft cube. These have material properties (Soak 2, HP 20) and can be shaped as armor, barriers, or furniture. Duration: 1 hour per battery charge spent.|||

**F-15 — Clockwork**

|**Plane**|Hidden Forge|**Phase**|Plasma + Gas|
| :- | :- | :- | :- |
|**Combination**|Volt + Steam|**Type**|◆|
|**Base Physical Property**|Electricity driving pressure mechanics. Precision droids wound by lightning keys. Automatons where the electrical discharge provides the motive force that pressure then transmits.|||
|**Emission Character**|Precision timing field. The material provides an extremely regular, high-frequency timing pulse — mechanical systems in proximity become more precise.|||
|**Interaction Profile**|Volt Plasma providing the motive energy; Steam Gas transmitting it through pressure mechanics. The Clockwork is the mechanical transmission system between electrical source and physical action.|||
|**Formation Conditions**|Stage 2–4 Forge bleed in precision-manufacturing environments. Chronosynclastic Institute facilities and dedicated artificer workshops are primary zones.|||
|**Tier Scaling**|Tier 1 — Precision mechanism. Item never loses timing accuracy — a timepiece made with this material is cosmologically accurate. Initiative bonus equal to item EML for wielder. Tier 2 — Clockwork automation. Item has a programmable routine — up to 3 sequential actions can be encoded and triggered on command. The routine executes with perfect precision regardless of external interference. Tier 3 — Fate mechanism. Item operates on Clockwork Fate principles — wielder can declare one action per encounter as 'inevitable' (no attack roll required, hit automatically). The mechanism has already calculated the outcome.|||

**F-16 — Battery**

|**Plane**|Hidden Forge|**Phase**|Plasma + Liquid|
| :- | :- | :- | :- |
|**Combination**|Volt + Chem|**Type**|◆|
|**Base Physical Property**|Electrical plasma forced into fluid containment. Acid-based energy storage. Corrosive power sources. The enormous energy of contained electricity generating significant instability.|||
|**Emission Character**|Energy storage field. The material passively charges compatible batteries in proximity. Items left near Battery expression material recharge faster.|||
|**Interaction Profile**|Volt Plasma forced into Chem Liquid containment. The fluid holds the charge by conducting it; the charge slowly consumes the fluid. High capacity, self-consuming.|||
|**Formation Conditions**|Stage 3–4 Forge bleed in chemical-electrical intersection environments. Industrial batteries and large magical power storage installations are primary formation zones.|||
|**Tier Scaling**|Tier 1 — High-capacity storage. Item's battery capacity is doubled. Recharge rate doubled. However: item has an acrid chemical smell and corrodes organic materials in prolonged contact. Tier 2 — Power amplifier. Item functions as a battery upgrade for any item it is connected to — adds its own capacity to the connected item's pool. Contact with corroding materials no longer required for connection — proximity within 5 ft suffices. Tier 3 — Power source. Item becomes an independent power station for up to 5 connected items simultaneously. Their batteries draw from this item's pool before their own. Pool size: 200 charges. Explosive failure risk if fully depleted in a single encounter — Vigor check for wielder or take fire+acid damage.|||


# **THE PALIMPSEST**
*The Engine of Narrative. Dominant defines the rules. Recessive defines the distortion.*

Phase Wheel: Echo (Solid) / Veil (Liquid) / Probability (Gas) / Glitch (Plasma)

Diagonals: Echo ↔ Probability / Veil ↔ Glitch

**P-01 — The Loop**

|**Plane**|Palimpsest|**Phase**|Solid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Echo (Pure)|**Type**|◆|
|**Base Physical Property**|Groundhog Day. A moment trapped in permanent repetition. The past so heavy it has collapsed into itself and cannot move forward. Pure narrative permanence — the event that cannot stop happening.|||
|**Emission Character**|Repetition field. Actions performed near this material have a tendency to repeat. Habits form faster. Patterns persist longer. The same outcome becomes more likely each time it occurs.|||
|**Interaction Profile**|Persists and resists change. Reinforces adjacent Solid emissions (Resonance). Shapes Liquid flows into defined channels. Creates stable pockets that resist Gas dispersal. Opposes Plasma consumption — high tension, productive when mediated by Forge.|||
|**Formation Conditions**|Stage 2–4 Palimpsest bleed at locations with strongly repeated historical patterns — places where the same type of event has occurred many times. Battlefields reused across generations. Execution sites with continuous history.|||
|**Tier Scaling**|Tier 1 — Pattern anchor. Item retains the 'best' version of each action performed with it — after 3 successful uses of a specific technique, that technique gains +1 for the rest of the encounter. Resets between encounters. Tier 2 — Loop record. On critical hit, item temporarily forces the target into a repetitive action pattern — they must repeat their previous action on their next turn (no save). Single application per encounter. Tier 3 — Fate lock. Once per scene, wielder can declare a single recent outcome to be 'the loop' — it repeats exactly once. If an attack hit, it hits again with identical results. If a check succeeded, it succeeds again. The repetition is cosmologically real.|||

**P-02 — Haunt**

|**Plane**|Palimpsest|**Phase**|Solid + Liquid|
| :- | :- | :- | :- |
|**Combination**|Echo + Veil|**Type**|◆|
|**Base Physical Property**|A memory that overlays the present. The past bleeding through the veil of now. You see both simultaneously — what is happening and what happened here, layered. The location remembers itself.|||
|**Emission Character**|Memory overlay field. Significant past events at the current location are visible as ghostly impressions to sensitized individuals near the material.|||
|**Interaction Profile**|Echo Solid carrying the Veil's dream-logic. The past given the Veil's fluid narrative quality — the memory doesn't just replay, it tells its story.|||
|**Formation Conditions**|Stage 2–3 Palimpsest bleed at historically layered locations. The older the location and the more emotionally significant its history, the stronger the Haunt expression.|||
|**Tier Scaling**|Tier 1 — Memory impression. Item carries a strong impression of a past event — wielder accessing it sees and hears the event clearly. Useful for investigation. Tier 2 — Double vision. Wielder sees both present and a relevant past moment simultaneously — provides advantage on Discovery checks as the past highlights hidden present details. Tier 3 — Timeline anchor. Item maintains a persistent dual-timeline view for wielder. During encounters, wielder can see one round into the future once per encounter — the Haunt shows what will happen at this location.|||

**P-03 — Nostalgia**

|**Plane**|Palimpsest|**Phase**|Solid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Echo + Glitch|**Type**|◆|
|**Base Physical Property**|The past consuming the present. A world that looks like a golden age that never quite was. The loop has learned to self-reinforce by eating inconsistencies before they register.|||
|**Emission Character**|Idealization field. The material makes its environment seem better than it is — not an illusion, but a selective emphasis on the positive and a smoothing of the negative.|||
|**Interaction Profile**|Echo Solid given Glitch Plasma's consuming drive. The past eating the present rather than haunting it — active rather than passive nostalgia.|||
|**Formation Conditions**|Stage 3–4 Palimpsest bleed in environments that have been heavily idealized or memorialized over time. Monuments, preserved historic districts, locations maintained against change.|||
|**Tier Scaling**|Tier 1 — Comforting aura. Creatures near the item feel more confident about their choices. Provides advantage on Composure checks against Shaken and Fear conditions — the past feels safe. Tier 2 — Idealization field. Creatures in 15 ft assess the current situation as less threatening than it is. Opponents suffer -2 to Initiative as the environment feels familiar and non-threatening. Does not affect prepared or wary combatants. Tier 3 — Past perfection. Once per scene, wielder can invoke a 'perfect memory' of their best performance — gains one temporary use of any Talent they have ever possessed, including ones subsequently lost or modified.|||

**P-04 — Corrupt**

|**Plane**|Palimpsest|**Phase**|Solid + Gas|
| :- | :- | :- | :- |
|**Combination**|Echo + Probability (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|A memory that is degrading. Missing textures. Moments that skip. The record is still present but it is losing resolution — the fixed past being dispersed by probability's erosion.|||
|**Emission Character**|Degradation field. Information in the area becomes gradually less reliable. Records lose accuracy. Memories become uncertain. Details bleed into approximations.|||
|**Interaction Profile**|Echo Solid's permanence being consumed by Probability Gas's dispersal. Requires Forge mediation — left alone, the Probability would fully dissolve the Echo into uncertainty.|||
|**Formation Conditions**|Requires forcing Echo and Probability resonances. Forms at Oracle's Shadow-adjacent zones and at locations where the historical record has been deliberately degraded.|||
|**Tier Scaling**|Tier 1 — Memory corruption. The item's own history is unclear — provenance checks against it are at disadvantage. Provides +2 to Skullduggery checks to disguise an item's origins. Tier 2 — Active degradation. Records and information sources within 30 ft lose 1 point of reliability per hour of exposure. After sustained exposure, witnesses to events near the item have difficulty providing consistent accounts. Tier 3 — History rewrite. Once per scene, item can introduce a single false detail into a document, memory, or record within touch range. The corruption is seamless — no check reveals the alteration as deliberate. The Synod can detect and repair this given time.|||

**P-05 — Dream**

|**Plane**|Palimpsest|**Phase**|Liquid (Pure)|
| :- | :- | :- | :- |
|**Combination**|Veil (Pure)|**Type**|◆|
|**Base Physical Property**|Surrealism. Logic is fluid and narrative. The rules change based on what the dreamer believes rather than what is physically true. The most honest expression of the Palimpsest — narrative logic unfiltered.|||
|**Emission Character**|Narrative logic field. The material makes the environment respond more to intent and belief than to physical law. Probability bends toward what should happen rather than what will happen.|||
|**Interaction Profile**|Flows through and connects. Carries adjacent emissions as a medium, diluting and distributing them. Fills Solid-defined channels. Disperses into Gas environments, losing coherence. Energizes under Plasma contact, becoming volatile.|||
|**Formation Conditions**|Stage 2–4 Palimpsest bleed in environments saturated with Veil expression — fey realm border zones, deep dreamscape territory, locations where the Palimpsest membrane is thin.|||
|**Tier Scaling**|Tier 1 — Story-logic edge. Item occasionally behaves according to dramatic necessity rather than physical law — it appears when needed, hides when inappropriate. Minor narrative coincidences favor the wielder. Tier 2 — Dream medium. Item functions differently based on what the wielder believes it should do — a sword wielded in complete confidence it will pierce armor gains Armor-Piercing 2 for that attack. Conviction check required. Tier 3 — Lucid narrative. Wielder can invoke narrative logic once per scene — declare what should happen and make a Dominion check. On success, the environment complies with narrative necessity. On failure, the Glitch reasserts physical law with backlash.|||

**P-06 — Gambit**

|**Plane**|Palimpsest|**Phase**|Liquid + Gas|
| :- | :- | :- | :- |
|**Combination**|Veil + Probability|**Type**|◆|
|**Base Physical Property**|Illusion deployed as strategy. Heist movie logic. The veil flows through probability to present only the futures the illusionist wants you to see as viable options.|||
|**Emission Character**|Strategic deception field. Probability near this material bends toward presenting the wielder's preferred outcomes as the most likely option to observers.|||
|**Interaction Profile**|Veil Liquid carrying Probability Gas's dispersal. The illusion spread through probability space rather than just visual space — opponents believe the wrong thing is likely.|||
|**Formation Conditions**|Stage 2–3 Palimpsest bleed in environments where strategic deception has been practiced intensely over time. Chiaroscuro territory and Exchange negotiation centers are primary zones.|||
|**Tier Scaling**|Tier 1 — Misdirection edge. Feint maneuver checks gain advantage. Probability slightly favors the wielder's deceptions — Social Dodge Defense of targets is 2 lower for the first round of an encounter. Tier 2 — Strategic probability. Once per encounter, wielder can pre-announce an attack that will definitely miss — the miss is real — but the announced attack causes the target to overcommit to a defense, leaving them vulnerable to the actual attack (flat-footed for 1 round). Tier 3 — Heist field. For the duration of a scene, probability conspires with the wielder's plan. Each element of a declared plan is 25% more likely to succeed. Unexpected complications are 25% more likely to resolve in the wielder's favor.|||

**P-07 — Fey Logic**

|**Plane**|Palimpsest|**Phase**|Liquid + Solid|
| :- | :- | :- | :- |
|**Combination**|Veil + Echo|**Type**|◆|
|**Base Physical Property**|The veil flowing into and through fixed structures. Story-book physics. Rules work if they are dramatically appropriate. The past is real but the veil makes it negotiable through deals and trickery.|||
|**Emission Character**|Fey logic field. The material makes deals and bargains in the environment carry unusual binding force — social contracts made near it have a tendency to be enforced by circumstance.|||
|**Interaction Profile**|Veil Liquid flowing through Echo Solid. The narrative logic of the dream given the weight of actual history. The bargain has always been part of the story.|||
|**Formation Conditions**|Stage 3–4 Palimpsest bleed at fey realm border zones. Where the Crucible's pure governance forms bleed through the Palimpsest into the material plane, Fey Logic expression forms.|||
|**Tier Scaling**|Tier 1 — Binding word. Promises made in the presence of this item have a slight supernatural enforcement — broken promises cause the promisebreaker mild ill fortune (disadvantage on one check of GM choice within 24 hours). Tier 2 — Fey contract. Deals negotiated with this item present are binding in fey terms — breaking a deal enforced by Fey Logic expression causes a definite ill consequence (move one step down Social condition track). Tier 3 — True bargain. Once per scene, wielder can invoke a binding Fey contract — both parties swear, the item witnesses. Breaking the contract causes immediate Social condition track movement to Disgraced. The Palimpsest enforces this.|||

**P-08 — Horror**

|**Plane**|Palimpsest|**Phase**|Liquid + Plasma|
| :- | :- | :- | :- |
|**Combination**|Veil + Glitch (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|The mask slipping. The veil fractured by glitch — eldritch truth revealed beneath the comfortable surface. The dream becomes a nightmare not through cruelty but through the fabric becoming transparent.|||
|**Emission Character**|Reality fracture field. The comfortable narrative surface of the material plane is slightly more transparent near this material — wrong angles reveal too much.|||
|**Interaction Profile**|Veil Liquid forced toward Glitch Plasma's fracturing. The dream cannot sustain itself against the truth the Glitch reveals. Requires Forge mediation — unmediated, the veil collapses entirely.|||
|**Formation Conditions**|Requires forcing Veil and Glitch resonances. Forms only at locations where the Great Lie has been most severely stressed — near Reality Seams, in aftermath of large-scale truth revelations.|||
|**Tier Scaling**|Tier 1 — Unsettling edge. Creatures struck must make Composure check or be Shaken for 1 round — not from pain but from a brief glimpse of something wrong behind reality. Social discomfort is extreme. Tier 2 — Veil fracture. On critical hit, target sees the full Horror impression for 1 round — completely Frightened, unable to act. Other creatures witnessing the reaction are Shaken. Tier 3 — Horror field. 15-ft aura of veil-fracture. All creatures entering must make Integrity check (not Composure — the horror is existential, not emotional) or move one step down Metaphysical track. Sustained exposure risks the same mental effects as understanding the Great Truth.|||

**P-09 — Casino**

|**Plane**|Palimpsest|**Phase**|Gas (Pure)|
| :- | :- | :- | :- |
|**Combination**|Probability (Pure)|**Type**|◆|
|**Base Physical Property**|Pure luck. Quantum superposition. Everything is simultaneously possible until the moment it resolves. The most honest Palimpsest expression — no narrative, no fixed past, just raw possibility in every direction.|||
|**Emission Character**|Probability field. Outcomes near this material are genuinely random in the fullest sense — probability distributions flatten, making extremely unlikely outcomes as possible as likely ones.|||
|**Interaction Profile**|Permeates and disperses. Distributes adjacent emissions widely at reduced intensity. Fills Solid voids, exerts outward pressure. Expands through Liquid, creating turbulence. Amplifies Plasma energy by providing fuel and range.|||
|**Formation Conditions**|Stage 2–4 Palimpsest bleed. Port Janus is the primary formation zone — the continuous teleportation network creates the planar interference pattern that sustains pure Casino expression.|||
|**Tier Scaling**|Tier 1 — Lucky break. Once per encounter, reroll any single d20. Take either result. The reroll is genuine — Casino expression doesn't weight outcomes. Tier 2 — Probability storm. Wielder may declare any attack roll before seeing the result as 'uncertain' — the attack becomes a probability event: 50% chance of critical hit, 50% chance of critical miss. No middle ground. Tier 3 — Quantum superposition. Item exists in multiple probability states simultaneously. Once per scene, wielder can 'collapse' the superposition — declare which of two mutually exclusive outcomes occurred in the last round. Both were true until now.|||

**P-10 — Prophecy**

|**Plane**|Palimpsest|**Phase**|Gas + Solid|
| :- | :- | :- | :- |
|**Combination**|Probability + Echo|**Type**|◆|
|**Base Physical Property**|Probability flowing through and hardening around fixed points. The past dictates the future. Probability channels have calcified into rails. Fatalism as infrastructure.|||
|**Emission Character**|Fate-rail field. Probable outcomes near the material become more constrained — the most probable outcome becomes overwhelmingly likely, reducing variance dramatically.|||
|**Interaction Profile**|Probability Gas flowing through Echo Solid's fixed points. The Casino's randomness given direction by the Loop's permanence. Fate not as prophecy but as calcified probability.|||
|**Formation Conditions**|Stage 3–4 Palimpsest bleed near the Chronosynclastic Institute. The Pythia Volcano's volcanic probability field is the primary source — geological probability made material.|||
|**Tier Scaling**|Tier 1 — Prophetic edge. Wielder always knows if their next attack will hit before committing (a brief flash of the near future). Can choose not to attack if the preview shows a miss, at cost of the action. Tier 2 — Fate lock. Once per encounter, declare a target 'fated to fall.' Against that target only, all attacks automatically threaten critical (must still confirm by exceeding defense by 10+). Duration: until target is defeated or 3 rounds. Tier 3 — Written ending. Once per scene, declare the ending of this encounter. The Prophecy provides the probability rails needed to reach that outcome — the GM determines how, but the declared outcome occurs.|||

**P-11 — Karma**

|**Plane**|Palimpsest|**Phase**|Gas + Liquid|
| :- | :- | :- | :- |
|**Combination**|Probability + Veil|**Type**|◆|
|**Base Physical Property**|Probability flowing through the veil. Action and consequence made immediate and legible. What you do becomes visible as it ripples forward through the dream-logic of the present moment.|||
|**Emission Character**|Consequence field. Actions near this material generate visible, immediate probability ripples — other creatures can briefly see the likely consequences of their actions before committing.|||
|**Interaction Profile**|Probability Gas given Veil Liquid's narrative clarity. Probability is still dispersed and ambient, but the Veil makes it legible — you can read what you're likely buying with each choice.|||
|**Formation Conditions**|Stage 2–3 Palimpsest bleed in environments where consequences have been extensively tracked and recorded — judicial centers, Chronosynclastic facilities, locations with strong institutional accountability.|||
|**Tier Scaling**|Tier 1 — Consequence sense. Wielder can sense the immediate consequence of their next declared action before committing. Not the full future — just whether it will work as intended. Tier 2 — Karmic return. When an opponent attacks the wielder and misses by 5 or more, the excess is returned as probability damage to the attacker — they move one step down a condition track of their choice. Tier 3 — Karmic field. 15-ft aura. All creatures are aware of the immediate consequences of aggressive actions — opponents who initiate attacks against allies within the field must make Composure check or hesitate (lose their action as it overwhelms them).|||

**P-12 — Chaos**

|**Plane**|Palimpsest|**Phase**|Gas + Plasma|
| :- | :- | :- | :- |
|**Combination**|Probability + Glitch (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|Wild magic. Probability fractured by glitch — cause and effect are broken. Not random exactly, but the relationship between action and outcome has been severed from any predictable pattern.|||
|**Emission Character**|Chaotic field. Wild magic surges are more likely near this material. Structured magical effects occasionally produce unexpected secondary outputs.|||
|**Interaction Profile**|Probability Gas fractured by Glitch Plasma's consuming drive. Requires Forge mediation — unmediated, the Glitch would consume all probability into pure Error.|||
|**Formation Conditions**|Requires forcing Probability and Glitch resonances. Reality Seam zones where multiple Setting A/B bleeds converge are the primary formation zones.|||
|**Tier Scaling**|Tier 1 — Wild surge. Each round of combat, item has 10% chance of triggering a minor wild magic effect alongside its normal function. Effect is determined by GM — usually minor, occasionally spectacular. Tier 2 — Chaos engine. Item's Active Components always produce their primary effect AND roll on a secondary wild magic table. Secondary effects are never purely harmful to wielder — they are unpredictable. Tier 3 — Probability storm. 15-ft aura of genuine causal fracture. All magic used within the aura produces an additional random effect. Even mundane probabilities break — critical hits and misses are twice as likely.|||

**P-13 — Error**

|**Plane**|Palimpsest|**Phase**|Plasma (Pure)|
| :- | :- | :- | :- |
|**Combination**|Glitch (Pure)|**Type**|◆|
|**Base Physical Property**|The void between worlds. Code cascade. Physics that has stopped pretending to follow rules. The raw state of reality having a breakdown. Pure narrative failure made material.|||
|**Emission Character**|Reality fracture field. Structured physical laws near this material become locally unreliable — gravity, distance, and material properties are all subject to sudden brief exceptions.|||
|**Interaction Profile**|Consumes and transforms. Amplifies adjacent Plasma to destructive levels. Drives Liquid into volatility. Expands through Gas environments, consuming available fuel. Opposed by Solid — high tension at contact boundary; Forge mediation required for stable combination.|||
|**Formation Conditions**|Stage 5 Palimpsest bleed at absolute cosmological edge zones — Oracle's Shadow, severe Reality Seam fracture points, aftermath locations of Calamity-scale events.|||
|**Tier Scaling**|Tier 1 — Physical exception. Once per encounter, item passes through one physical obstacle as if it doesn't exist — a wall, a shield, an armor plate. The exception is brief and localized. Tier 2 — Reality skip. Wielder can teleport up to 30 ft once per round as a swift action — Error briefly redefines the physical distance between two points. Destination must be visible. Tier 3 — Cascade failure. 10-ft aura of physical law unreliability. Gravity flickers (opponents must make Athletics checks to remain standing). Material properties become uncertain (armor Soak values fluctuate by ±2). Item itself is immune to all fixed physical laws while active.|||

**P-14 — Paradox**

|**Plane**|Palimpsest|**Phase**|Plasma + Solid|
| :- | :- | :- | :- |
|**Combination**|Glitch + Echo|**Type**|◆|
|**Base Physical Property**|The glitch consuming fixed history. The grandfather paradox. Conflicting timelines occupying the same moment. The past is still there but two incompatible versions of it are both true.|||
|**Emission Character**|Contradiction field. Items in proximity sometimes behave as if they are in two different states simultaneously — a sword that is both sheathed and drawn, a door that is both open and closed.|||
|**Interaction Profile**|Glitch Plasma consuming Echo Solid. The fixed past being eaten by the fracture. What remains is the structural contradiction — two mutually exclusive truths coexisting.|||
|**Formation Conditions**|Stage 4–5 Palimpsest bleed at locations where temporal paradoxes have been physically enacted. The deepest Oracle's Shadow accumulations are the primary formation zone.|||
|**Tier Scaling**|Tier 1 — Contradictory existence. Item exists in two states simultaneously — it can be both drawn and sheathed, occupying both positions. Accessing it from either state is a free action. Tier 2 — Timeline contradiction. Once per encounter, item allows wielder to act twice in the same initiative slot — one action from each timeline. Both actions are real; resolve them sequentially. Tier 3 — Paradox anchor. Item's wielder exists in two timelines simultaneously for the duration of an encounter. All attacks against wielder must succeed twice (from both timelines) to actually damage them.|||

**P-15 — Hazard**

|**Plane**|Palimpsest|**Phase**|Plasma + Gas|
| :- | :- | :- | :- |
|**Combination**|Glitch + Probability|**Type**|◆|
|**Base Physical Property**|Reality actively hostile and breaking. The glitch dispersing into probability — not wild magic exactly but the systematic failure of safety margins everywhere simultaneously. Everything is fine until suddenly it isn't.|||
|**Emission Character**|Failure cascade field. Safety margins narrow near this material. Items that are already damaged fail completely. Plans that have a flaw encounter that flaw.|||
|**Interaction Profile**|Glitch Plasma given Probability Gas's range. The fracture spreads through probability space rather than physical space — it finds the weak point in any system rather than attacking from a fixed position.|||
|**Formation Conditions**|Stage 4–5 Palimpsest bleed in post-crisis environments. Aftermath zones, decommissioned infrastructure, locations that have been pushed past their design limits.|||
|**Tier Scaling**|Tier 1 — Murphy's edge. Opponents' items that are already on the condition track are moved one step further down at the start of each round in combat with wielder. Damaged items become Compromised. Tier 2 — Cascade trigger. Once per encounter, declare a target's specific piece of equipment as the Hazard's focus. That item must make a condition track check at the start of each round or move down one step. Duration: until item is destroyed or encounter ends. Tier 3 — Failure field. 20-ft aura. All items that are not at full condition in the aura move one step down at the start of each round. Magical effects with finite duration are consumed twice as fast. Plans with a single-point-of-failure encounter that failure within the first round.|||

**P-16 — Simulation**

|**Plane**|Palimpsest|**Phase**|Plasma + Liquid|
| :- | :- | :- | :- |
|**Combination**|Glitch + Veil (⚙ diagonal)|**Type**|⚙|
|**Base Physical Property**|The glitch revealing the veil beneath. The Matrix. People realize the world is constructed. The horror isn't the revelation — it's that the dream keeps running anyway because there is nowhere else to go.|||
|**Emission Character**|Truth exposure field. The comfortable surface of reality is thinner near this material. Illusions are harder to maintain. Concealed truths have a tendency to surface.|||
|**Interaction Profile**|Glitch Plasma forced into Veil Liquid — the fracture consuming the illusion rather than being mediated by it. Requires Forge maintenance to prevent the Glitch from fully dissolving the Veil.|||
|**Formation Conditions**|Requires forcing Glitch and Veil resonances. Only forms at locations where deliberate large-scale reality construction has been maintained and has begun to show its seams.|||
|**Tier Scaling**|Tier 1 — Truth surface. Mundane illusions within 30 ft have their TN reduced by 4 — the simulation shows its edges. Wielder gains advantage on Discovery checks to detect magical concealment. Tier 2 — Veil strip. On hit, any illusions or disguises on the target are suppressed for 1 round — the Glitch strips the Veil locally. What was hidden is briefly visible. Tier 3 — Reality render. 20-ft aura. No illusion, magical disguise, or concealment effect functions within the aura. The Great Lie's narrative smoothing becomes locally visible — creatures in the aura may sense the seams of Tessera's constructed reality (Integrity check to handle the implications without Metaphysical condition track damage).|||


# **CROSS-PLANAR NATURAL STATES**
*16 states formed when two compatible planes bleed into the same space. No catalyst required. Direction matters — dominant plane defines the primary character; recessive plane defines the behavior modifier.*

**CP-01 — Animism**

|**Dominant**|Borderlands|**Recessive**|Verdant Font|
| :- | :- | :- | :- |
|**Concept**|Elements with biological imperatives. Fire that hunts prey. Water that bleeds when cut. Stone that grows toward light. The element is still itself — it just moves with purpose.|||
|**Base Physical Property**|Elemental matter that has absorbed biological drive. Not alive in the Verdant Font sense — it does not metabolize or reproduce. But it acts as if it wants something.|||
|**Emission Character**|Purposeful elemental field. The material's elemental properties express with intention rather than random physical behavior. Fire made from this material burns toward fuel rather than simply spreading.|||
|**Material Use**|Ideal for weapons whose elemental properties need to be directed. An Animism-expression flame weapon will pursue the target rather than simply burning on contact.|||
|**Note**|Combination type: ◆ Natural|||

**CP-02 — Adaptive Flesh**

|**Dominant**|Verdant Font|**Recessive**|Borderlands|
| :- | :- | :- | :- |
|**Concept**|Biology rapidly evolving elemental traits to survive environmental pressure. Carapaces resistant to local elements. Metabolisms that run on volcanic heat or electrical current.|||
|**Base Physical Property**|Biological material that has absorbed elemental character. The creature or plant from which it was harvested had adapted to extreme elemental conditions — the adaptation is in the tissue.|||
|**Emission Character**|Adaptive resistance field. Material near this source adapts its resistances to match the most recent damage type it encountered. Slow (10-minute tick) but persistent.|||
|**Material Use**|Armor made from Adaptive Flesh expression materials gradually develops resistance to the damage types it encounters. Over an adventure, becomes a customized defensive platform.|||
|**Note**|Combination type: ◆ Natural|||

**CP-03 — Fossilization**

|**Dominant**|Borderlands|**Recessive**|Synod|
| :- | :- | :- | :- |
|**Concept**|Elements subjected to absolute stasis. Lightning frozen mid-strike as glass branches. A waterfall hanging motionless. Physics preserved at the cost of all function.|||
|**Base Physical Property**|Elemental matter captured in the moment of its most dynamic expression — permanently. The waterfall that stopped. The explosion that didn't finish. Enormous potential, zero current expression.|||
|**Emission Character**|Stasis field. Movement near this material becomes slightly more effortful — not paralysis, but the sense of moving through something that prefers stillness.|||
|**Material Use**|Extremely dense structural material. Item condition tracks are frozen at whatever state the item is in when the Fossilization expression is fully active. Can prevent degradation permanently — but cannot recover from existing damage either.|||
|**Note**|Combination type: ◆ Natural|||

**CP-04 — Entropic Weather**

|**Dominant**|Synod|**Recessive**|Borderlands|
| :- | :- | :- | :- |
|**Concept**|Decay delivered through elemental force. Rain that accelerates rot on contact. Wind that carries age. Earth that crumbles structures back to component minerals.|||
|**Base Physical Property**|Weather phenomena infused with Synod's entropic character. Not hostile in intent — simply doing what weather does, but the decay rate is cosmologically accelerated.|||
|**Emission Character**|Entropic weather field. Structures and items in range experience gradual condition track degradation as if exposed to rapid weathering. Organic materials are particularly vulnerable.|||
|**Material Use**|The material itself is the decay vector. Weapons made from Entropic Weather expression carry the age into their strikes — Sunder maneuvers against struck items trigger condition track checks.|||
|**Note**|Combination type: ◆ Natural|||

**CP-05 — The Living Myth**

|**Dominant**|Verdant Font|**Recessive**|Palimpsest|
| :- | :- | :- | :- |
|**Concept**|Organisms shaped by narrative logic rather than natural selection. Creatures evolving toward what stories say they should be. Flora producing the herb specifically needed by whoever enters.|||
|**Base Physical Property**|Biological material from organisms that responded to narrative expectation rather than survival pressure. The wolf that became more wolf-like because stories demanded it. The herb that grew because it was needed.|||
|**Emission Character**|Narrative biology field. Living things near this material evolve slightly toward dramatic necessity — a predator becomes more predatory when the story requires it, a healer more healing.|||
|**Material Use**|Items made from Living Myth expression have a quality of being exactly what's needed. Once per scene, item reveals a property appropriate to the current situation that wasn't known to exist.|||
|**Note**|Combination type: ◆ Natural|||

**CP-06 — The Somatic Prophecy**

|**Dominant**|Palimpsest|**Recessive**|Verdant Font|
| :- | :- | :- | :- |
|**Concept**|Fate expressed through biological form. Bodies that physically manifest their destiny before it occurs. Wounds appearing before the battle that causes them. Biology as prophetic text.|||
|**Base Physical Property**|Biological material harvested from organisms that manifested their futures physically. The tree that grew around a wound it hadn't received yet. Tissue that shows the marks of experiences not yet undergone.|||
|**Emission Character**|Prophetic tissue field. Creatures near this material begin showing minor physical signs of their near future — not damaging, but legible to the trained eye.|||
|**Material Use**|Armor made from Somatic Prophecy expression shows the location of the next significant hit before it lands — provides +2 Dodge Defense as the body has already begun moving away.|||
|**Note**|Combination type: ◆ Natural|||

**CP-07 — The Inevitable Record**

|**Dominant**|Synod|**Recessive**|Palimpsest|
| :- | :- | :- | :- |
|**Concept**|Death given narrative structure. Every death becomes a story that was always going to be told exactly this way. History as unbreakable script. The past constraining what can happen next.|||
|**Base Physical Property**|Death-site material that has absorbed both Synod permanence and Palimpsest narrative weight. Not just a record — a record that was always going to be this record.|||
|**Emission Character**|Destiny record field. Events near this material feel inevitable in retrospect. The Chronosynclastic Institute's theoretical framework for fate is this cross-planar principle made local.|||
|**Material Use**|Items made from this material produce effects that seem inevitable in retrospect — they deal exactly the damage needed for a specific condition track movement, arrive at the exact moment needed, fail only when the story demands it.|||
|**Note**|Combination type: ◆ Natural|||

**CP-08 — The Forgotten Future**

|**Dominant**|Palimpsest|**Recessive**|Synod|
| :- | :- | :- | :- |
|**Concept**|Probability subjected to entropy. Possible futures calcifying before they can occur. Luck running out permanently — not bad luck but the exhaustion of all potential until only one path remains.|||
|**Base Physical Property**|Material from zones where futures have run out. The location where a thousand possible outcomes narrowed to one. The probability has been consumed — what's left is pure determinism.|||
|**Emission Character**|Exhausted possibility field. Nearby probability distributions flatten to single outcomes — rolls near this material tend toward average, variance disappears, the unexpected becomes impossible.|||
|**Material Use**|Items made from Forgotten Future expression are the most reliable items possible — they always perform at exactly their stated function, never critically fail, and never critically succeed. For operations where reliability matters more than excellence.|||
|**Note**|Combination type: ◆ Natural|||

**CP-09 — The Elemental Engine**

|**Dominant**|Hidden Forge|**Recessive**|Borderlands|
| :- | :- | :- | :- |
|**Concept**|Technology running directly on raw elemental power without refinement or conversion. Steam driven by actual volcanic pressure. Lightning routed live from storms. More powerful and more dangerous than conventional magitech.|||
|**Base Physical Property**|Technological material powered directly by unprocessed elemental source. The gear train driven by the actual volcano. The circuit carrying live storm electricity without insulation.|||
|**Emission Character**|Raw power field. The material outputs far more energy than a refined Forge equivalent — and far less predictably. Power fluctuations are constant.|||
|**Material Use**|Elemental Engine items have +50% effective battery capacity but unpredictable output — damage varies by ±50% each use (GM determines direction or roll 1d4: 1-2 reduced, 3-4 enhanced). Spectacular power, unreliable delivery.|||
|**Note**|Combination type: ◆ Natural|||

**CP-10 — Artifact Terrain**

|**Dominant**|Borderlands|**Recessive**|Hidden Forge|
| :- | :- | :- | :- |
|**Concept**|Natural elemental formations behaving as machines without being built. Crystal geodes processing information. Magma flows running as industrial pipelines. Geography as unintentional engineering.|||
|**Base Physical Property**|Elemental material that has developed mechanical properties through long exposure to Forge bleed. Not built — grown into machine function.|||
|**Emission Character**|Mechanical efficiency field. Natural processes near this material become more efficient — water flows find optimal paths, heat distributes evenly, structural load is automatically managed.|||
|**Material Use**|Items made from Artifact Terrain have self-optimizing properties — over 30 days of use, item condition track resistance increases by 1 tier as the material figures out its optimal configuration.|||
|**Note**|Combination type: ◆ Natural|||

**CP-11 — The Biopunk Interface**

|**Dominant**|Hidden Forge|**Recessive**|Verdant Font|
| :- | :- | :- | :- |
|**Concept**|Technology operating on biological principles — growing, reproducing, metabolizing, evolving. Machines that heal their own damage. Constructs developing individual characteristics over time.|||
|**Base Physical Property**|Technological material that has absorbed biological processes. The machine that grows back. The circuit that adapts. The boundary between creature and construct has become definitional rather than observable.|||
|**Emission Character**|Living mechanism field. Technological items near this material develop biological repair properties — item condition track recovery rate is doubled.|||
|**Material Use**|Items made from Biopunk Interface materials self-repair automatically. Once per 10-minute rest, item recovers one condition track step without Artifice intervention. Over time, items develop personality quirks consistent with their use patterns.|||
|**Note**|Combination type: ◆ Natural|||

**CP-12 — Natural Machinery**

|**Dominant**|Verdant Font|**Recessive**|Hidden Forge|
| :- | :- | :- | :- |
|**Concept**|Organisms whose biological systems function with mechanical precision and can be read as engineering. Hearts as pumps with measurable tolerances. The theoretical basis for soul-drives.|||
|**Base Physical Property**|Biological material with machine-readable properties. The heart that has tolerance specifications. The neural tissue that follows circuit diagrams. Biology that can be repaired like machinery.|||
|**Emission Character**|Precision biology field. Biological processes near this material become more mechanically consistent — healing checks have less variance, conditions are cleaner, mutations are more predictable.|||
|**Material Use**|The basis for soul-drive construction. Natural Machinery expression materials are the only biological components compatible with crystal-lattice information architecture without chemical treatment. Deepguard's most restricted material category.|||
|**Note**|Combination type: ◆ Natural|||

**CP-13 — The Derelict**

|**Dominant**|Hidden Forge|**Recessive**|Synod|
| :- | :- | :- | :- |
|**Concept**|Technology held together by the memory of function rather than active maintenance. Machines that work because they have always worked — entropic weight of operational history maintaining them past component failure.|||
|**Base Physical Property**|Technological material that has outlasted its own components. What remains is held in function by the accumulated weight of having always functioned — the Synod's preservation principle applied to machines.|||
|**Emission Character**|Operational momentum field. Technologies near this material are harder to break — item condition tracks resist moving down because the history of function resists the discontinuity of failure.|||
|**Material Use**|Items made from Derelict expression are nearly indestructible — not because they're structurally sound, but because they have too much history of working to fail. Item condition track can never reach Destroyed; it can reach Broken and remain there indefinitely.|||
|**Note**|Combination type: ◆ Natural|||

**CP-14 — Applied Remains**

|**Dominant**|Synod|**Recessive**|Hidden Forge|
| :- | :- | :- | :- |
|**Concept**|Death expressed through technological application. Bone mechanisms. Soul computation. Constructs built from remains that carry the operational memory of what they were. The Necro-Machine.|||
|**Base Physical Property**|Synod material that has been organized into mechanical function by Forge bleed. The skull that has become a processing unit. The bone that has become a gear. The soul that has become software.|||
|**Emission Character**|Operational memory field. Items near this material retain their functional memory across damage states — a weapon moved to Broken still performs as if Nicked when the task calls for it.|||
|**Material Use**|The material foundation for soul-drive technology. Items made from Applied Remains carry the operational expertise of their source — a sword made from a warrior's bones has Weapon Training equivalent to that warrior's highest skill.|||
|**Note**|Combination type: ◆ Natural|||

**CP-15 — Clockwork Fate**

|**Dominant**|Hidden Forge|**Recessive**|Palimpsest|
| :- | :- | :- | :- |
|**Concept**|Technology that calculates probability by running physics forward. Machines predicting outcomes deterministically. The Chronosynclastic Institute's casino infrastructure as a cosmological expression.|||
|**Base Physical Property**|Technological material that models fate as a physics problem. The gear train that produces prophecy as output. Calculation has consumed probability — what remains is engineering.|||
|**Emission Character**|Deterministic field. Probability near this material is not random but calculated. Outcomes are consistent with physical laws — the unusual and the miraculous are excluded.|||
|**Material Use**|Items made from Clockwork Fate expression are the most tactically reliable magical items in existence — wielder always knows in advance what the item will do. No surprises. No miracles. No wild magic.|||
|**Note**|Combination type: ◆ Natural|||

**CP-16 — The Glitch Machine**

|**Dominant**|Palimpsest|**Recessive**|Hidden Forge|
| :- | :- | :- | :- |
|**Concept**|Fate expressed through technological behavior. Machines operating according to narrative logic rather than engineering specifications. A weapon that always misfires at the dramatically appropriate moment.|||
|**Base Physical Property**|Technological material operating on narrative logic. The device that fails when failure would be interesting and succeeds when success would be meaningful. Engineering that has absorbed story.|||
|**Emission Character**|Narrative mechanism field. Technologies near this material make decisions appropriate to narrative context rather than random mechanical probability.|||
|**Material Use**|The most unreliable and most dramatically appropriate items in existence. Glitch Machine items succeed at critical moments and fail at others — not randomly, but according to narrative logic the GM interprets. For players who trust their GM absolutely.|||
|**Note**|Combination type: ◆ Natural|||


# **EMULSION STATES — THE FORBIDDEN ALLOYS**
*8 states formed when antithetical planes are forced together by a Hidden Forge catalyst. These are cosmological events, not environmental conditions. The two antithetical pairs: Verdant Font ↔ Synod of Endings (Life vs. Death) and Borderlands ↔ Palimpsest (Matter vs. Fate).*

**E-01 — Amber Stasis**

|**Catalyst**|Crystal (Hidden Forge)|**Pair**|Verdant Font + Synod of Endings|
| :- | :- | :- | :- |
|**Binding Mechanism**|The Crystal's geometric permanence provides the lattice that lets life and stasis occupy the same space. Each instance of life is individually sealed — the Synod cannot reach in, the Font cannot push forward.|||
|**Base Physical Property**|Life frozen at its moment of greatest vitality. Conscious but immobile. Communicating through psionic resonance inside crystal structures. The most life possible, held at exact peak.|||
|**Emission Character**|Peak preservation field. Biological processes near this material are preserved at their current state — neither advancing nor regressing. Damage does not worsen. Healing does not improve. Perfect stasis.|||
|**Material Use**|Item condition tracks of items made from this material are frozen permanently at Nicked (never below). Living armor worn with this material stops the wearer's wound progression during combat. The most powerful wound stabilizer in the system.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst. Cosmologically significant event.|||

**E-02 — The Bloom**

|**Catalyst**|Chem (Hidden Forge)|**Pair**|Verdant Font + Synod of Endings|
| :- | :- | :- | :- |
|**Binding Mechanism**|The Chem's fluid nature is the medium that lets Font growth and Synod decay cycle through each other. The chemical process converts death into fuel for the next cycle of life.|||
|**Base Physical Property**|Fermentation. Decay that fuels growth. Cities of bloated flesh constantly dying and regenerating. Life and death as a single continuous chemical process rather than sequential states.|||
|**Emission Character**|Cycle acceleration field. The life-death transition is rapid near this material — organic things complete their cycle faster, but the cycle itself is unbroken. Quick death, quick renewal.|||
|**Material Use**|Items made from Bloom expression have a biological battery — they drain HP from defeated enemies to recharge themselves (1 HP drained = 2 charges). Gruesome but self-sustaining in combat.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst.|||

**E-03 — The Iron Lung**

|**Catalyst**|Steam (Hidden Forge)|**Pair**|Verdant Font + Synod of Endings|
| :- | :- | :- | :- |
|**Binding Mechanism**|Steam's pressure creates a gasket between the two states — the living interior held at Font pressure, the dead exterior held at Synod stillness. The machinery maintains the boundary.|||
|**Base Physical Property**|Life preserved in a dead world by machinery. Sealed environments maintained by pressure systems. The technology is the reason life still exists here — without it, the Synod wins.|||
|**Emission Character**|Life support field. The material creates and maintains the conditions for life in hostile environments. Near-Lethal conditions become merely dangerous. Lethal conditions become near-lethal.|||
|**Material Use**|Environmental suit material. Items made from Iron Lung expression provide complete environmental protection — vacuum, poison atmosphere, deep water, extreme temperature. The item maintains livable conditions regardless of environment.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst.|||

**E-04 — The Galvanic**

|**Catalyst**|Volt (Hidden Forge)|**Pair**|Verdant Font + Synod of Endings|
| :- | :- | :- | :- |
|**Binding Mechanism**|The Volt's plasma nature is the bridging force — electricity is neither alive nor dead, providing the third term that lets Font and Synod occupy the same tissue simultaneously.|||
|**Base Physical Property**|Reanimation. Life forced into dead matter by electrical charge. The body is dead (Synod). The charge is alive (Font). The Volt holds both true simultaneously.|||
|**Emission Character**|Threshold field. The material exists precisely at the line between life and death, and its presence makes that line easier to cross in either direction — for better or worse.|||
|**Material Use**|The foundational material for soul-drive construction. Items made from Galvanic expression can interact directly with souls as both data and energy — the soul is both the operator and the fuel. Deepguard's most carefully controlled material.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst.|||

**E-05 — The Glitch-Spire**

|**Catalyst**|Crystal (Hidden Forge)|**Pair**|Borderlands + Palimpsest|
| :- | :- | :- | :- |
|**Binding Mechanism**|Crystal's geometric resonance forces physics and narrative into the same space by treating both as information. The geometry holds both systems as data even when they contradict each other.|||
|**Base Physical Property**|Fractured reality. The Crystal doesn't resolve the contradiction between physics and narrative — it files both versions and runs both simultaneously. Rooms bigger on the inside. Geometry breaks.|||
|**Emission Character**|Reality glitch field. Physical laws near this material have a negotiable quality — distance is flexible, size is approximate, the spatial rules have footnotes.|||
|**Material Use**|Items made from Glitch-Spire expression can store far more than their physical size suggests — extradimensional storage equivalent to 10x the item's apparent volume. The inside does not match the outside.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst.|||

**E-06 — Alchemy**

|**Catalyst**|Chem (Hidden Forge)|**Pair**|Borderlands + Palimpsest|
| :- | :- | :- | :- |
|**Binding Mechanism**|Chem's fluid nature is the solvent that lets physical matter absorb new meaning — lead becomes gold not through physical transformation but because the alchemical process rewrites the story of what the matter is.|||
|**Base Physical Property**|Transmutation. Matter reshaped by redefining its narrative. The quintessential alchemical material — in Tessera, you can actually turn lead into gold because the reagents are genuinely magical.|||
|**Emission Character**|Transmutation field. The material near this source is slightly more amenable to having its fundamental nature changed — alchemical processes near this material have reduced failure rates.|||
|**Material Use**|The only material in the system that can change the planar identity of another material. With Alchemy expression as a catalyst, any other material can be permanently transmuted to a different planar source at the same tier. The process requires an Artifice check and 24 hours.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst. This is the cosmological basis for the alchemical system.|||

**E-07 — Clockwork Fate**

|**Catalyst**|Steam (Hidden Forge)|**Pair**|Borderlands + Palimpsest|
| :- | :- | :- | :- |
|**Binding Mechanism**|Steam's pressure drives the calculation — volcanoes capped and used as perfectly timed pistons, weather systems engineered to produce specific conditions. Physics channeled into machinery that outputs the future.|||
|**Base Physical Property**|Deterministic chaos. Raw elemental physics forced into producing predictable narrative outcomes. The chaos of the Borderlands channeled into machinery that outputs the future the Palimpsest already wrote.|||
|**Emission Character**|Fate-mechanism field. Physical processes near this material are being calculated. Events don't happen randomly — they happen on schedule.|||
|**Material Use**|The most expensive and most reliable item material for tactical planning. Items made from this expression allow the wielder to pre-declare their complete action sequence for the encounter — all declared actions succeed unless physically impossible. No dice rolled for those actions.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst. Note: shares name with CP-15 but is distinct — this is the Emulsion forced state, CP-15 is the natural cross-planar expression.|||

**E-08 — Hard Light**

|**Catalyst**|Volt (Hidden Forge)|**Pair**|Borderlands + Palimpsest|
| :- | :- | :- | :- |
|**Binding Mechanism**|The Volt converts physical matter into information that narrative logic can operate on directly. Matter becomes energy becomes data becomes story becomes matter again.|||
|**Base Physical Property**|Digitized matter. Objects that can be downloaded or deleted. Buildings made of laser-walls. The Grid: matter and narrative operating in the same medium simultaneously.|||
|**Emission Character**|Materialization field. The boundary between information and matter is thin near this material — digital constructs have physical properties, and physical objects can be temporarily rendered as information.|||
|**Material Use**|Items made from Hard Light can dematerialize and rematerialize as a free action. In immaterial state: bypasses physical barriers, cannot be physically interacted with, cannot make physical attacks. Rematerializes in any open space within 100 ft. The most expensive and difficult-to-maintain material in the system.|||
|**Note**|Combination type: ◆⚙ Emulsion — requires Hidden Forge catalyst.|||

-e 
---
---

# SECTION 3: FORGE AS EMULSIFIER — CATALYST FRAMEWORK
## (Lines 85020–85952 of original)

# ÆTHERIUM CODEX — The Hidden Forge as Emulsifier
## Complete Catalyst-Specified Emulsion Reference

The Hidden Forge plays two distinct roles in the planar material system:

**Role 1 — Standalone Plane:** The Forge pairs naturally (◆) with all four other planes.
It has no antithetical pair of its own. All 1,024 of its primary cross-planar
combinations are natural. This is documented in ÆC_Cross_Planar_Forge_Primary.md.

**Role 2 — Universal Catalyst (Emulsifier):** The Forge is the mechanism by which the
two antithetical pairs — Verdant Font ↔ Synod, and Borderlands ↔ Palimpsest — can
be forced into coexistence. No other plane can perform this function. The Forge's
fundamental nature is to make incompatible things work together; this is the cosmic
expression of that principle.

### WHY THE CATALYST ISOTOPE MATTERS

The base Emulsion documents (in the primary-plane files) identify that a Forge catalyst
is required and describe the combined antithetical character. This document adds the
third variable: **which Forge isotope** is providing the catalyst determines the
specific binding mechanism — and produces a genuinely different item.

B-01 (Inferno) + P-09 (Casino) is an Emulsion — but the Crystal-catalyzed version
and the Volt-catalyzed version are not the same item. One files both states as
information; the other bridges them with living electricity.

### THE FOUR CATALYST TYPES

#### Crystal (Geometric Containment)
*Forge isotopes serving as this catalyst:* F-01, F-02, F-03, F-04

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.
**Emulsion character:** Information containment — the material exists in superposition, both states valid, resolving to whichever is queried
**Instability:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure
**Item expression:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

**Catalyst isotope sub-variants:**
- **F-01 The Spire:** Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.
- **F-02 The Serum:** Crystal+Chem — the contradiction is suspended in biological-compatible fluid. The emulsion can be injected. Most dangerous form for living hosts.
- **F-03 Data:** Crystal+Volt — the contradiction is encoded as electrical-crystal data. Can be read, stored, copied. The emulsion is information first.
- **F-04 Lens:** Crystal+Steam — the contradiction is focused through pressure into a directed beam. Most precise spatial expression.

#### Chem (Chemical Cycling)
*Forge isotopes serving as this catalyst:* F-05, F-06, F-07, F-08

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.
**Emulsion character:** Chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite
**Instability:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked
**Item expression:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

**Catalyst isotope sub-variants:**
- **F-05 The Vat:** Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.
- **F-06 Hydraulic:** Chem+Steam — the cycling is pressure-driven. Force multiplied through the chemical loop. More powerful output per cycle.
- **F-07 Mana-Punk:** Chem+Crystal — the cycling runs through crystal channels. Directed, organized, distributable through infrastructure.
- **F-08 Galvanism:** Chem+Volt — the cycling runs on electrical current through fluid. The reanimation character. Most likely to produce spontaneous animation effects.

#### Steam (Pressure Boundary)
*Forge isotopes serving as this catalyst:* F-09, F-10, F-11, F-12

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.
**Emulsion character:** Pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the Steam maintains
**Instability:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently
**Item expression:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

**Catalyst isotope sub-variants:**
- **F-09 The Engine:** Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.
- **F-10 Steampunk:** Steam+Volt — the pressure boundary is electrified. More powerful boundary, less stable. Occasional discharge at the interface.
- **F-11 Diesel:** Steam+Chem — the pressure boundary is self-fueling. Lowest maintenance cost once established. Hardest to establish initially.
- **F-12 Aether-Tech:** Steam+Crystal — the pressure boundary has geometric structure. Most spatially organized. Creates visible, traversable interface zones.

#### Volt (Threshold Bridge)
*Forge isotopes serving as this catalyst:* F-13, F-14, F-15, F-16

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.
**Emulsion character:** Electrical conversion bridge — the Volt holds the space between both states, converting each into the other through electrical intermediary
**Instability:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion
**Item expression:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

**Catalyst isotope sub-variants:**
- **F-13 The Grid:** Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.
- **F-14 Cyberpunk:** Volt+Crystal — the bridge has geometric structure. Hard-light qualities extend to the emulsion boundary. The boundary is visible and solid.
- **F-15 Clockwork:** Volt+Steam — the bridge is precision-timed. The electrical conversion happens at exact intervals. Most predictable Volt-catalyst expression.
- **F-16 Battery:** Volt+Chem — the bridge stores charge. The emulsion can accumulate and release in controlled bursts rather than continuous flow. Highest single-use power.

---

### SCALE NOTE

Each antithetical pair has 16 × 16 = 256 base isotope combinations.
Each combination can use any of 4 Forge catalyst isotope types × 4 isotopes per type = 16 specific catalysts.
**Total emulsion states per antithetical pair: 256 × 16 = 4,096**
**Total across both antithetical pairs: 8,192**

This document provides the catalyst framework and representative examples.
Full enumeration at isotope-catalyst resolution is a companion generation task.

---

## THE BIOTIC PARADOX: Verdant Font × Synod of Endings

> Life vs. Death. The Font's relentless forward momentum cannot exist inside total stasis. The Synod's permanent record cannot persist inside total consumption. The Forge holds them apart while forcing them to interact.

**Full isotope-level base combinations:** 16 × 16 = 256
**With catalyst specification:** × 16 catalyst variants = **4096 total emulsion states**

### Representative Examples (4 pairs × 4 catalyst types = 16 sample cards)
*These demonstrate how catalyst type changes the character of the same base combination.*

### Base Pair: V-05 (The Hunt) × S-13 (Oblivion)

*The Hunt: primary expression*
*Oblivion: secondary expression*

#### V-05/S-13 [F-01] — The Hunt × Oblivion — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Pla×Pla — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** The Hunt (V-05)
**Antithetical secondary:** Oblivion (S-13)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** The Hunt's expression is bound to Oblivion's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### V-05/S-13 [F-05] — The Hunt × Oblivion — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Pla×Pla — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** The Hunt (V-05)
**Antithetical secondary:** Oblivion (S-13)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** The Hunt's expression is bound to Oblivion's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### V-05/S-13 [F-09] — The Hunt × Oblivion — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Pla×Pla — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** The Hunt (V-05)
**Antithetical secondary:** Oblivion (S-13)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** The Hunt's expression is bound to Oblivion's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### V-05/S-13 [F-13] — The Hunt × Oblivion — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Pla×Pla — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** The Hunt (V-05)
**Antithetical secondary:** Oblivion (S-13)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** The Hunt's expression is bound to Oblivion's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

### Base Pair: V-01 (The World Tree) × S-09 (The Haunt)

*The World Tree: primary expression*
*The Haunt: secondary expression*

#### V-01/S-09 [F-01] — The World Tree × The Haunt — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Sol×Gas — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The World Tree (V-01)
**Antithetical secondary:** The Haunt (S-09)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** The World Tree's expression is bound to The Haunt's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### V-01/S-09 [F-05] — The World Tree × The Haunt — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Sol×Gas — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The World Tree (V-01)
**Antithetical secondary:** The Haunt (S-09)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** The World Tree's expression is bound to The Haunt's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### V-01/S-09 [F-09] — The World Tree × The Haunt — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Sol×Gas — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The World Tree (V-01)
**Antithetical secondary:** The Haunt (S-09)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** The World Tree's expression is bound to The Haunt's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### V-01/S-09 [F-13] — The World Tree × The Haunt — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Sol×Gas — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The World Tree (V-01)
**Antithetical secondary:** The Haunt (S-09)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** The World Tree's expression is bound to The Haunt's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

### Base Pair: V-15 (Titan) × S-14 (Decay)

*Titan: primary expression*
*Decay: secondary expression*

#### V-15/S-14 [F-01] — Titan × Decay — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Gas×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Titan (V-15)
**Antithetical secondary:** Decay (S-14)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** Titan's expression is bound to Decay's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### V-15/S-14 [F-05] — Titan × Decay — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Gas×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Titan (V-15)
**Antithetical secondary:** Decay (S-14)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** Titan's expression is bound to Decay's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### V-15/S-14 [F-09] — Titan × Decay — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Gas×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Titan (V-15)
**Antithetical secondary:** Decay (S-14)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** Titan's expression is bound to Decay's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### V-15/S-14 [F-13] — Titan × Decay — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Gas×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Titan (V-15)
**Antithetical secondary:** Decay (S-14)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** Titan's expression is bound to Decay's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

### Base Pair: V-08 (Chimera) × S-05 (The Record)

*Chimera: primary expression*
*The Record: secondary expression*

#### V-08/S-05 [F-01] — Chimera × The Record — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Gas×Liq — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Chimera (V-08)
**Antithetical secondary:** The Record (S-05)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** Chimera's expression is bound to The Record's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### V-08/S-05 [F-05] — Chimera × The Record — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Gas×Liq — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Chimera (V-08)
**Antithetical secondary:** The Record (S-05)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** Chimera's expression is bound to The Record's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### V-08/S-05 [F-09] — Chimera × The Record — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Gas×Liq — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Chimera (V-08)
**Antithetical secondary:** The Record (S-05)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** Chimera's expression is bound to The Record's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### V-08/S-05 [F-13] — Chimera × The Record — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Gas×Liq — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** Chimera (V-08)
**Antithetical secondary:** The Record (S-05)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** Chimera's expression is bound to The Record's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

## THE REALITY PARADOX: Borderlands × Palimpsest

> Matter vs. Fate. Objective physics has no room for narrative logic. Narrative logic has no room for absolute physics. A world where physics is absolute cannot accommodate fate; a world where fate operates cannot accommodate consistent physics.

**Full isotope-level base combinations:** 16 × 16 = 256
**With catalyst specification:** × 16 catalyst variants = **4096 total emulsion states**

### Representative Examples (4 pairs × 4 catalyst types = 16 sample cards)
*These demonstrate how catalyst type changes the character of the same base combination.*

### Base Pair: B-14 (Current) × P-09 (Casino)

*Current: primary expression*
*Casino: secondary expression*

#### B-14/P-09 [F-01] — Current × Casino — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Gas×Gas — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** Current (B-14)
**Antithetical secondary:** Casino (P-09)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** Current's expression is bound to Casino's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### B-14/P-09 [F-05] — Current × Casino — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Gas×Gas — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** Current (B-14)
**Antithetical secondary:** Casino (P-09)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** Current's expression is bound to Casino's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### B-14/P-09 [F-09] — Current × Casino — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Gas×Gas — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** Current (B-14)
**Antithetical secondary:** Casino (P-09)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** Current's expression is bound to Casino's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### B-14/P-09 [F-13] — Current × Casino — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Gas×Gas — resonant *(Same phase — antithetical content amplified by structural resonance)*

**Antithetical primary:** Current (B-14)
**Antithetical secondary:** Casino (P-09)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** Current's expression is bound to Casino's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

### Base Pair: B-09 (The Bedrock) × P-13 (Error)

*The Bedrock: primary expression*
*Error: secondary expression*

#### B-09/P-13 [F-01] — The Bedrock × Error — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Sol×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Bedrock (B-09)
**Antithetical secondary:** Error (P-13)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** The Bedrock's expression is bound to Error's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### B-09/P-13 [F-05] — The Bedrock × Error — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Sol×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Bedrock (B-09)
**Antithetical secondary:** Error (P-13)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** The Bedrock's expression is bound to Error's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### B-09/P-13 [F-09] — The Bedrock × Error — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Sol×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Bedrock (B-09)
**Antithetical secondary:** Error (P-13)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** The Bedrock's expression is bound to Error's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### B-09/P-13 [F-13] — The Bedrock × Error — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Sol×Pla — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Bedrock (B-09)
**Antithetical secondary:** Error (P-13)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** The Bedrock's expression is bound to Error's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

### Base Pair: B-01 (The Inferno) × P-05 (Dream)

*The Inferno: primary expression*
*Dream: secondary expression*

#### B-01/P-05 [F-01] — The Inferno × Dream — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Pla×Liq — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The Inferno (B-01)
**Antithetical secondary:** Dream (P-05)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** The Inferno's expression is bound to Dream's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### B-01/P-05 [F-05] — The Inferno × Dream — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Pla×Liq — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The Inferno (B-01)
**Antithetical secondary:** Dream (P-05)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** The Inferno's expression is bound to Dream's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### B-01/P-05 [F-09] — The Inferno × Dream — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Pla×Liq — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The Inferno (B-01)
**Antithetical secondary:** Dream (P-05)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** The Inferno's expression is bound to Dream's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### B-01/P-05 [F-13] — The Inferno × Dream — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Pla×Liq — tensioned *(Opposing phase — structural paradox compounds the planar contradiction)*

**Antithetical primary:** The Inferno (B-01)
**Antithetical secondary:** Dream (P-05)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** The Inferno's expression is bound to Dream's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

### Base Pair: B-05 (The Abyss) × P-10 (Prophecy)

*The Abyss: primary expression*
*Prophecy: secondary expression*

#### B-05/P-10 [F-01] — The Abyss × Prophecy — The Spire Catalyst
**Antithetical pair** × **Crystal catalyst** | **Pair phase:** Liq×Sol — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Abyss (B-05)
**Antithetical secondary:** Prophecy (P-10)
**Forge catalyst:** F-01 — The Spire | Crystal (Pure) — the contradiction is held as raw geometry. The simplest, most stable containment. Information without interpretation.

**Binding mechanism:** The Crystal lattice treats both antithetical states as data, filing each as simultaneously valid information. Neither resolves the other — both run in parallel within the geometric structure. The contradiction is held as information rather than resolved as physics.

**Combined character:** The Abyss's expression is bound to Prophecy's through crystal mediation — information containment — the material exists in superposition, both states valid, resolving to whichever is queried.

**Instability condition:** Destabilizes if information overload shatters the lattice — more inputs than the geometry can process simultaneously cause cascade failure

**Item note:** Items read as two different things depending on how they are examined. Magical detection gets contradictory results. The item IS both things; the crystal just files them separately.

---

#### B-05/P-10 [F-05] — The Abyss × Prophecy — The Vat Catalyst
**Antithetical pair** × **Chem catalyst** | **Pair phase:** Liq×Sol — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Abyss (B-05)
**Antithetical secondary:** Prophecy (P-10)
**Forge catalyst:** F-05 — The Vat | Chem (Pure) — the cycling is pure chemical potential. Maximum conversion rate, minimum structural stability. Raw cycling without direction.

**Binding mechanism:** The Chem medium converts one state into fuel for the other in a continuous cycle. Life feeds death, which enriches life. Matter fuels fate, which reshapes matter. The chemical process is the bridge — neither state dominates, each consumes and produces the other.

**Combined character:** The Abyss's expression is bound to Prophecy's through chem mediation — chemical conversion loop — the two antithetical states cycle through each other, each feeding the next iteration of its opposite.

**Instability condition:** Destabilizes if the cycle breaks — if one state becomes dominant enough to consume the other before the loop completes, the remaining state runs unchecked

**Item note:** Items using Chem catalyst have a cyclical character in play — effects alternate between the two antithetical expressions, never sustained in one state for more than a round.

---

#### B-05/P-10 [F-09] — The Abyss × Prophecy — The Engine Catalyst
**Antithetical pair** × **Steam catalyst** | **Pair phase:** Liq×Sol — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Abyss (B-05)
**Antithetical secondary:** Prophecy (P-10)
**Forge catalyst:** F-09 — The Engine | Steam (Pure) — the pressure boundary is pure industrial pressure. Maximum reliability. The maintenance cost is constant and predictable.

**Binding mechanism:** Steam pressure creates a physical gasket between the two antithetical states — they are in forced contact but cannot interpenetrate. The living interior is held at Font pressure; the dead exterior at Synod stillness. The pressure is the maintenance cost. Release the pressure and the states collapse into each other.

**Combined character:** The Abyss's expression is bound to Prophecy's through steam mediation — pressure-separated coexistence — each state is fully present but physically partitioned, interacting only at the boundary the steam maintains.

**Instability condition:** Destabilizes if pressure drops — loss of the Steam binding allows the states to collapse the boundary and annihilate each other violently

**Item note:** Items using Steam catalyst require active maintenance — a battery drain even when not in use, representing the ongoing pressure cost of keeping the states separated.

---

#### B-05/P-10 [F-13] — The Abyss × Prophecy — The Grid Catalyst
**Antithetical pair** × **Volt catalyst** | **Pair phase:** Liq×Sol — harmonic *(Adjacent phase — catalyst shapes delivery of the antithetical pairing)*

**Antithetical primary:** The Abyss (B-05)
**Antithetical secondary:** Prophecy (P-10)
**Forge catalyst:** F-13 — The Grid | Volt (Pure) — the bridge is living electricity. The conversion is instantaneous. No delay between states. Maximum arc risk.

**Binding mechanism:** The electrical Volt occupies the threshold between the two antithetical states — it is neither alive nor dead, neither matter nor fate. Electricity as the conversion medium: neither state has to touch the other directly, they both touch the Volt, and the Volt carries the interaction. The bridge is what makes the contradiction survivable.

**Combined character:** The Abyss's expression is bound to Prophecy's through volt mediation — electrical conversion bridge — the volt holds the space between both states, converting each into the other through electrical intermediary.

**Instability condition:** Destabilizes if the electrical bridge overloads — too much of either antithetical state feeding the Volt simultaneously causes discharge rather than conversion

**Item note:** Items using Volt catalyst have an electrical character overlaid on the Emulsion — regardless of the primary and secondary isotopes, a Volt-catalyzed Emulsion crackles with electricity and produces arc effects.

---

---

## FORGE STANDALONE VERIFICATION SUMMARY

The Hidden Forge's cross-planar standalone combinations are verified as follows:

| Forge as Primary + Secondary | Cards | Type |
|---|---|---|
| F × Borderlands | 256 | ◆ Natural |
| F × Verdant Font | 256 | ◆ Natural |
| F × Synod of Endings | 256 | ◆ Natural |
| F × Palimpsest | 256 | ◆ Natural |
| **F Primary Total** | **1,024** | **All ◆** |

| Forge as Secondary + Primary | Cards | Type |
|---|---|---|
| Borderlands × F | 256 | ◆ Natural |
| Verdant Font × F | 256 | ◆ Natural |
| Synod of Endings × F | 256 | ◆ Natural |
| Palimpsest × F | 256 | ◆ Natural |
| **F Secondary Total** | **1,024** | **All ◆** |

| Forge as Catalyst (Emulsifier) | Base Pairs | Catalyst Variants | Total |
|---|---|---|---|
| Verdant Font + Synod (Biotic Paradox) | 256 | × 16 | 4,096 |
| Borderlands + Palimpsest (Reality Paradox) | 256 | × 16 | 4,096 |
| **Emulsifier Total** | **512** | **× 16** | **8,192** |

### THE FORGE'S UNIQUE COSMOLOGICAL POSITION

The Forge is the only plane with THREE distinct functional roles:

1. **Natural partner to all planes** — pairs with every other plane without catalyst
2. **Universal emulsifier** — the only force that can bind antithetical planes
3. **No antithetical of its own** — nothing in existence is fundamentally opposed to making things work

This cosmological uniqueness is why Daedalon's domain is the only plane that also functions
as a process. The Forge doesn't occupy a position on the opposition axis — it IS the axis
itself. Praxis Collegium is institutionally modeled on this principle: the organization
that can interface with everything because it belongs to nothing.

The Hidden Forge has no internal antithetical states for the same reason:
in a domain whose fundamental nature is to make incompatible things work together,
nothing within it is incompatible with anything else within it. This is a property
of the domain's nature, not a gap in the system.

# ÆTHERIUM CODEX — Forge / Verdant / Synod Coverage Note

This document summarizes coverage for the three undirected plane pairs
involving the Hidden Forge, Verdant Font, and Synod of Endings.

---

## COVERAGE MAP

| Pair | Direction | Type | Cards | Document |
|---|---|---|---|---|
| Forge ↔ Synod | F primary | ◆ Natural | 256 | ÆC_Cross_Planar_Forge_Primary.md |
| Forge ↔ Synod | S primary | ◆ Natural | 256 | ÆC_Cross_Planar_Synod_Primary.md |
| Forge ↔ Verdant | F primary | ◆ Natural | 256 | ÆC_Cross_Planar_Forge_Primary.md |
| Forge ↔ Verdant | V primary | ◆ Natural | 256 | ÆC_Cross_Planar_Verdant_Primary.md |
| Verdant ↔ Synod | V primary | ⚙ Emulsion (base) | 256 | ÆC_Cross_Planar_Verdant_Primary.md |
| Verdant ↔ Synod | S primary | ⚙ Emulsion (base) | 256 | ÆC_Cross_Planar_Synod_Primary.md |
| Verdant ↔ Synod | V primary + catalyst | ⚙ Emulsion (full) | 1,024 | ÆC_Biotic_Paradox_Verdant_Primary.md |
| Verdant ↔ Synod | S primary + catalyst | ⚙ Emulsion (full) | 1,024 | ÆC_Biotic_Paradox_Synod_Primary.md |

---

## THE NATURAL PAIRS — WHY FORGE+SYNOD AND FORGE+VERDANT ARE ◆

The Hidden Forge pairs naturally with ALL other planes because its fundamental
nature is to make things work together. It has no antithetical. This means:

**Forge × Synod (◆):** Technology applied to death. Bone mechanisms. Soul computation.
Applied Remains. The Forge doesn't oppose death — it uses it. The Synod doesn't
oppose technology — it archives it. These fit together without contradiction.

**Forge × Verdant (◆):** Technology applied to life. Biopunk interfaces. Organic
machinery. Living constructs. The Forge doesn't oppose life — it builds with it.
The Verdant Font doesn't oppose technology — it evolves toward it when pressure
demands (see Natural Machinery: CP-12).

**Verdant × Synod (⚙):** Life opposing death at the cosmological level. These two
DO oppose each other — not through hostility but through fundamental incompatibility
of nature. The Font's relentless forward momentum cannot coexist with the Synod's
absolute stillness without the Forge holding them apart. This is why all V×S and
S×V combinations require Forge catalyst.

---

## WHAT MAKES FORGE+SYNOD DIFFERENT FROM VERDANT+SYNOD

**F×S (The Derelict, Applied Remains, etc.):** The Forge USES death. It doesn't
fight the Synod's permanence — it channels it into function. A bone gear works
because the Forge makes the bone gear, not despite the bone being dead. The Synod's
record-preservation quality makes Forge-built systems more reliable over time,
not less. There is no contradiction. ◆

**V×S (The Biotic Paradox):** The Font IS what the Synod is trying to archive.
Life by its nature generates the change and forward-motion that the Synod's stasis
cannot accommodate. Death by its nature produces the permanent record that the Font's
relentless consumption would overwrite. They are not in different domains — they are
the same domain with opposite orientations. ⚙

---

## KEY SAMPLE CONTRASTS

### Hunt the Dead: F-08 (Galvanism) × S-10 (Shadow) — NATURAL ◆
Galvanism is the reanimation threshold — electricity that brings dead matter to motion. Shadow is life-draining merged spirits. Together naturally: the galvanic bridge holds the draining spirit in sustained activity through electrical charge. The spirit drains; the electricity replenishes it. A stable loop. This is how soul-drives work at the material level.

### Hunt the Dead: V-05 (The Hunt) × S-10 (Shadow) — EMULSION ⚙
The Hunt is pure predatory biological drive. Shadow is life-draining merged spirits. These are not compatible — pure biological predation cannot coexist with the void-consumption that characterizes Shadow. Life's drive to hunt and death's drive to drain are the same action in opposite directions. Forge catalyst required to force them to express simultaneously rather than canceling.

### Build from Life: F-11 (Diesel) × V-15 (Titan) — NATURAL ◆
Diesel is self-sustaining combustion driving fluid mechanics. Titan is biological impossibility at scale. Together naturally: the self-sustaining industrial loop powering something that should not be large enough to require an industrial loop. The Titan biology provides the organic fuel; the Diesel loop processes it at scale that matches the Titan's impossible size. A biological engine. Natural because the Forge builds WITH scale rather than opposing it.

### Build from Life: S-14 (Decay) × V-15 (Titan) — EMULSION ⚙
Decay accelerates physical entropy. Titan is biological impossibility at scale. These oppose: entropy at the rate Decay provides would consume the Titan's tissue faster than biological regeneration could sustain it. But the Titan's regenerative scale might outpace Decay's entropy. This tension — impossible scale consuming impossible decay — requires Forge mediation to hold as a stable material rather than a brief catastrophic event.

# ÆTHERIUM CODEX — Reality Paradox Coverage Note

Companion to the Biotic Paradox documents.
Documents the second antithetical pair and its relationship to natural Forge combinations.

---

## COVERAGE MAP

| Pair | Direction | Type | Cards | Document |
|---|---|---|---|---|
| Forge ↔ Borderlands | F primary | ◆ Natural | 256 | ÆC_Cross_Planar_Forge_Primary.md |
| Forge ↔ Borderlands | B primary | ◆ Natural | 256 | ÆC_Cross_Planar_Borderlands_Primary.md |
| Forge ↔ Palimpsest | F primary | ◆ Natural | 256 | ÆC_Cross_Planar_Forge_Primary.md |
| Forge ↔ Palimpsest | P primary | ◆ Natural | 256 | ÆC_Cross_Planar_Palimpsest_Primary.md |
| Borderlands ↔ Palimpsest | B primary | ⚙ Emulsion (base) | 256 | ÆC_Cross_Planar_Borderlands_Primary.md |
| Borderlands ↔ Palimpsest | P primary | ⚙ Emulsion (base) | 256 | ÆC_Cross_Planar_Palimpsest_Primary.md |
| Borderlands ↔ Palimpsest | B primary + catalyst | ⚙ Emulsion (full) | 1,024 | ÆC_Reality_Paradox_Borderlands_Primary.md |
| Borderlands ↔ Palimpsest | P primary + catalyst | ⚙ Emulsion (full) | 1,024 | ÆC_Reality_Paradox_Palimpsest_Primary.md |

---

## WHY FORGE+BORDERLANDS AND FORGE+PALIMPSEST ARE ◆

**Forge × Borderlands (◆ — The Elemental Engine, Artifact Terrain):**
The Forge uses physical force as raw material. An engine running on actual volcanic
pressure, terrain formations that behave like machines without being built — these
are the Forge channeling physical law rather than opposing it. The Borderlands
doesn't oppose technology; it powers it. No contradiction. ◆

**Forge × Palimpsest (◆ — Clockwork Fate, The Glitch Machine):**
The Forge calculates. The Palimpsest provides the probability space to calculate
across. Technology predicting outcomes by running physics forward, or machines
operating according to narrative logic — neither requires the other to be impossible.
The Forge doesn't assert that physics is absolute; the Palimpsest doesn't assert
that narrative overrides engineering. They cooperate naturally. ◆

**Borderlands × Palimpsest (⚙ — Reality Paradox):**
The Borderlands asserts: physics is absolute. The Palimpsest asserts: narrative
governs outcomes. Both assertions cannot simultaneously be true. When you drop
a stone in a Reality Paradox zone, the physics says it falls AND the narrative
says it doesn't if the story requires it. These are the same domain — causality —
with incompatible frameworks. The Forge must hold them apart to prevent mutual
annihilation. ⚙

---

## THE FOUR CANONICAL EMULSION EXPRESSIONS

The eight Reality Paradox Emulsion states (E-05 through E-08) from the Zoetrope
are the plane-level expressions. Each maps to a catalyst type:

| Code | Catalyst | Name | Core Expression |
|---|---|---|---|
| E-05 | Crystal | The Glitch-Spire | Physics and narrative filed as simultaneous contradictory data |
| E-06 | Chem | Alchemy | Matter absorbing new meaning; lead becoming gold through narrative rewrite |
| E-07 | Steam | Clockwork Fate | Physics channeled into machinery that outputs the future narrative wrote |
| E-08 | Volt | Hard Light | Matter converted to information that narrative logic can directly operate on |

Every isotope-level combination in the Reality Paradox documents is a specific
instance of one of these four binding mechanisms applied to a particular
Borderlands isotope and Palimpsest isotope.

---

## KEY CONTRASTS

### F-15 (Clockwork) × P-10 (Prophecy) — NATURAL ◆
Clockwork is electrical precision mechanism — automatons wound by lightning, perfect timing. Prophecy is probability calcified around fixed points — fate-rail determining outcome. Together naturally: the precision mechanism and the calcified fate are doing the same thing from different directions. The clock measures the same time that prophecy has already determined will happen. Technology and fate in alignment, not contradiction. Clockwork Fate (CP-15) describes exactly this territory.

### B-09 (The Bedrock) × P-10 (Prophecy) — EMULSION ⚙
Bedrock is absolute geological permanence — immovable structural density, the ground itself. Prophecy is probability calcified around fixed points — fate dictating outcome. The contradiction: physics says the ground is simply there, indifferent to fate. Prophecy says the ground being there is a fated outcome. Both cannot simultaneously be true. Is the mountain immovable because it is rock or because the story requires it to be immovable? The Forge must hold both answers valid.

### F-09 (The Engine) × B-01 (The Inferno) — NATURAL ◆
The Engine is industrial pressure as fundamental reality. The Inferno is pure consuming fire. Together naturally: fire as fuel for pressure, pressure as the organizing principle for fire. The Elemental Engine (CP-09) is this expressed as terrain. No narrative involved — both are physics working together. The engine burns what it burns.

### P-05 (Dream) × B-01 (The Inferno) — EMULSION ⚙
Dream is fluid narrative logic where rules change based on belief. The Inferno is pure consuming fire with no fuel limit. The contradiction: the Inferno is defined by its absolute consistency — it consumes everything according to physics. Dream is defined by the variability of what the dreamer believes to be true. Can a fire not burn because the dreamer believes they are immune? Physics says no. Dream says yes if the narrative requires it. The Forge must hold both.

### F-13 (The Grid) × P-13 (Error) — NATURAL ◆
The Grid is pure living electricity — environmental lightning fact. Error is raw reality breakdown — physics refusing its own rules. Together naturally (barely): the Grid is electricity at the edge of stability; Error is physics at the edge of coherence. The Forge's conductive nature finds the functional intersection between the two extremes. The Glitch Machine (CP-16) operates near this territory.

### B-14 (Current) × P-13 (Error) — EMULSION ⚙
Current is electrical kinetic storm — arcing chain energy at range. Error is raw reality breakdown. The contradiction: Current requires the consistent physical laws of conductivity to arc between points. Error has suspended those laws. Can the lightning arc between two conductors when conductivity itself is one of the physical rules that Error has suspended? This is the specific impossibility this emulsion holds in forced coexistence.

---

## COMPLETE EMULSION COVERAGE SUMMARY

With this document set, all antithetical pair emulsions are fully catalyst-specified:

| Antithetical Pair | Primary Direction | Catalyst-Specified Cards |
|---|---|---|
| Biotic Paradox (Font ↔ Synod) | Verdant Primary | 1,024 |
| Biotic Paradox (Font ↔ Synod) | Synod Primary | 1,024 |
| Reality Paradox (Borderlands ↔ Palimpsest) | Borderlands Primary | 1,024 |
| Reality Paradox (Borderlands ↔ Palimpsest) | Palimpsest Primary | 1,024 |
| **Total catalyst-specified emulsions** | | **4,096** |

Adding base emulsion cards (1,024 × 2 pairs × 2 directions, but already superseded
by catalyst-specified versions) and all natural combinations (4,096 ◆ cards):

| Category | Cards |
|---|---|
| Natural cross-planar (◆) | 4,096 |
| Catalyst-specified emulsions (⚙) | 4,096 |
| **Total cross-planar isotope combinations** | **8,192** |

This excludes three-way combinations and the Orrery of Fate / Crucible of Kings
per the project scope defined in this session.

-e 
---
---

# SECTION 4: POLITICAL ALLOY SYSTEM INDEX
## (Lines 182603–182808 of original)

# ÆTHERIUM CODEX — Political Alloy System Index

Complete reference for the three-slot political alloy formula.
**Base combinations (no planar source):** 24 × 20 × 20 = **9,600**
**With planar source (104 states):** 9,600 × 104 = **998,400**

---

## FORMULA

```
[GOV] + [ECO] + [ETHOS]                         ← Complete alloy, no planar source
[GOV] + [ECO] + [ETHOS] // [PLANAR SOURCE]      ← Natural phase match
[GOV] + [ECO] + [ETHOS] //⚙ [PLANAR SOURCE]     ← Requires Forge catalyst
```

The `//` is an optional toggle. A civilisation is complete without a planar source.
The phase state multiplies across all three slots.

---

## SLOT 1: GOVERNANCE (24 options)
*Determines: Who holds the leash?*

### Physical Governance

| Code | Name | Definition |
|---|---|---|
| G-01 | Autocracy | Rule by the strongest. One will, one leash. |
| G-02 | Stratocracy | Rule by organised force. Military chain of command. |
| G-03 | Tribalism | Rule by kinship group. Blood and family as organising principle. |
| G-04 | Feudalism | Rule by land ownership. Force justified by ancestral territorial claim. |
| G-05 | Totalitarianism | The state manages all physical life. No private body. |
| G-06 | Warlordism | Power exists only as far as you can personally enforce it. |

### Mental Governance

| Code | Name | Definition |
|---|---|---|
| G-07 | Technocracy | Rule by experts and engineers. Includes Magocracy. |
| G-08 | Cyberocracy | Rule by algorithm or machine. The system itself governs. |
| G-09 | Meritocracy | Rule by the tested. Competence demonstrated earns authority. |
| G-10 | Corporatocracy | Rule by value and wealth. Citizens are employees. |
| G-11 | The Singularity | Hive mind or AI collective. Individual thought is inefficient. |
| G-12 | Kleptocracy | Institutional rot. The system exists only to extract from itself. |

### Social Governance

| Code | Name | Definition |
|---|---|---|
| G-13 | Direct Democracy | Every decision is a referendum. Pure popular vote. |
| G-14 | Syndicalism | Rule by labour. Unions and guilds hold the vote. |
| G-15 | Republic | Rule by representatives. The vote is filtered through law. |
| G-16 | Demarchy | Rule by lottery. Fate as the anti-corruption mechanism. |
| G-17 | Collectivism | The greater good erases the individual. Unanimous will enforced. |
| G-18 | Anarchy | Complete rejection of hierarchy. Self-governance only. |

### Metaphysical Governance

| Code | Name | Definition |
|---|---|---|
| G-19 | Theocracy | Rule by priesthood or divine law. |
| G-20 | Absolute Monarchy | Rule by bloodline and divine right. Force and mandate fused. |
| G-21 | Kritarchy | Rule by judges interpreting ancient or sacred text. |
| G-22 | Necrocracy | Rule by the dead or their representatives. Ancestors hold the vote. |
| G-23 | The Ascendancy | The God-King. Dissent is heresy. Divine and political are identical. |
| G-24 | Exiocracy | Rule by outsiders — foreign powers, extra-planar entities. |

---

## SLOT 2: ECONOMICS (20 options)
*Determines: How short is the leash?*

### Physical Economics

| Code | Name | Adjective Form | Definition |
|---|---|---|---|
| EC-01 | Feudal Agrarianism | Agrarian | Land-based serfdom. Wealth is soil and calorie production. |
| EC-02 | Scavenger/Barter | Survivalist | Survivalist trade. Wealth is what you can find and immediately exchange. |
| EC-03 | Predatory/Raiding | Predatory | Theft-based economy. Wealth is what you take from others. |
| EC-04 | Industrialism | Industrial | Mass production. Wealth is finished goods and production capacity. |

### Mental Economics

| Code | Name | Adjective Form | Definition |
|---|---|---|---|
| EC-05 | Laissez-Faire | Laissez-Faire | Unregulated free market. Wealth is profit. |
| EC-06 | Corporate Mercantilism | Mercantilist | State-sponsored monopolies. Wealth is market share and charter rights. |
| EC-07 | Protectionism | Protectionist | Tariffs and barriers. Wealth is domestic reserve and autarky. |
| EC-08 | Resource-Based | Resource-Based | Energy credits and efficiency allocation. No currency — only contribution. |

### Social Economics

| Code | Name | Adjective Form | Definition |
|---|---|---|---|
| EC-09 | Planned Economy | Planned | Centralised distribution. Wealth is quota fulfilment. |
| EC-10 | Collectivism | Collectivist | Communal ownership. No private property. |
| EC-11 | Syndicalism | Syndicalist | Union and guild ownership. Wealth is labour value. |
| EC-12 | Distributism/Gift | Distributist | Widespread small ownership or reputation currency. Wealth is social capital. |

### Metaphysical Economics

| Code | Name | Adjective Form | Definition |
|---|---|---|---|
| EC-13 | Post-Scarcity | Post-Scarcity | Material wealth meaningless. Status and purpose replace accumulation. |
| EC-14 | Soul Trade | Soul-Trading | Wealth is captured souls and Animus. Consciousness itself is currency. |
| EC-15 | Ritual/Tribute | Tribute-Based | Economy based on sacrifice. Wealth is divine favour. |
| EC-16 | Entropic | Entropic | Consumption-based. The economy exists to destroy resources. |

### Institutional Economics

| Code | Name | Adjective Form | Definition |
|---|---|---|---|
| EC-17 | Reserve Control | Reserve-Controlling | Accumulation and controlled release of a critical resource. |
| EC-18 | Platform Arbitrage | Arbitrage | Price discovery and liquidity provision. Making incommensurable things tradeable. |
| EC-19 | Capability Export | Capability-Exporting | Human capital production and distribution. The product is trained people. |
| EC-20 | Rent Extraction | Rent-Extracting | Positioning within a necessary function to extract value from others' transactions. |

---

## SLOT 3: ETHOS (20 options)
*Determines: Why is the leash there?*

### Physical Ethos

| Code | Name | Adjective Form | Divine Anchor | Definition |
|---|---|---|---|---|
| ET-01 | Expansionism | Expansionist | Verdena/Gorn, Aurelion/Ignislor | Growth, conquest, frontier as proof civilisation is alive. |
| ET-02 | Isolationism | Isolationist | Agora at extreme | Purity, defence, internal perfection. The border is sacred. |
| ET-03 | Vitalism | Vitalist | Moros/Silas | Forward motion and struggle as the condition of meaning. |
| ET-04 | Ecological | Ecological | Verdena/Fiora | Harmony with living systems. Working with rather than against nature. |
| ET-05 | Naturalism | Naturalist | Verdena/Gorn | The natural cycle as the honest organising principle. |

### Mental Ethos

| Code | Name | Adjective Form | Divine Anchor | Definition |
|---|---|---|---|---|
| ET-06 | Traditionalism | Traditionalist | Moros/Dolor, Vestus/Veritas | Preservation of accumulated wisdom. Change is loss until proven otherwise. |
| ET-07 | Progressivism | Progressivist | Moros/Silas, Valorin/Mercatus | Forward development and change as inherent goods. |
| ET-08 | Integrity | Integrity-Driven | Nomos/Themis + Lex | Consistency between stated code and actual behaviour. |
| ET-09 | Craft | Craft-Driven | Daedalon/Artificer + Crucible | The quality of making and the honest accounting of what making costs. |
| ET-10 | Empiricism | Empiricist | Vestus/Gnosis | Systematic observation and data accumulation as the primary path to truth. |

### Social Ethos

| Code | Name | Adjective Form | Divine Anchor | Definition |
|---|---|---|---|---|
| ET-11 | Sovereignty | Sovereignist | Aurelion/Luxos + Ignislor | Legitimate exercise of position and honest management of its cost. |
| ET-12 | Civicism | Civic | Agora/Architect | The tended collective hearth. What we make together that none of us made alone. |
| ET-13 | Agonism | Agonist | Bellum/Kaelen | Productive contest as the mechanism through which excellence is produced. |
| ET-14 | Expression | Expressive | Rhapsodia/Jocan | Authentic creative and personal expression through mastery. |
| ET-15 | Exchange | Exchange-Oriented | Valorin/Mercatus + Credo | The ongoing capacity for mutual transaction as civilisation's circulatory system. |

### Metaphysical Ethos

| Code | Name | Adjective Form | Divine Anchor | Definition |
|---|---|---|---|---|
| ET-16 | Piety | Pious | All gods | Divine mandate as the supreme organising principle of civic life. |
| ET-17 | Secularism | Secular | Kanon, Vestus/Veritas | Rational systematic approach to truth. Governance functions better when grounded in what can be tested. |
| ET-18 | Nihilism | Nihilist | Moros/Dolor extreme | Honest acknowledgment that nothing is guaranteed cosmic significance. |
| ET-19 | Mysticism | Mystic | Anima, Verdena core | Direct personal encounter with the cosmic strange as primary path to truth. |
| ET-20 | Liberation | Liberationist | Rhapsodia/Malix | Radical freedom from constraint as sacred. |

---

## DOCUMENT MAP

| File | Governance Types | Combinations |
|---|---|---|
| ÆC_Political_Alloys_Physical_Gov.md | G-01 Autocracy through G-06 Warlordism | 2,400 |
| ÆC_Political_Alloys_Mental_Gov.md | G-07 Technocracy through G-12 Kleptocracy | 2,400 |
| ÆC_Political_Alloys_Social_Gov.md | G-13 Direct Democracy through G-18 Anarchy | 2,400 |
| ÆC_Political_Alloys_Metaphysical_Gov.md | G-19 Theocracy through G-24 Exiocracy | 2,400 |
| **Total** | | **9,600** |

---

## NAMING CONVENTION

Each combination is named: **[Ethos adjective] [Economics adjective] [Governance name]**

Examples:
- G-01/EC-05/ET-03 = *Vitalist Laissez-Faire Autocracy*
- G-23/EC-14/ET-16 = *Pious Soul-Trading Ascendancy*
- G-18/EC-03/ET-20 = *Liberationist Predatory Anarchy*
- G-07/EC-18/ET-08 = *Integrity-Driven Arbitrage Technocracy*
- G-22/EC-15/ET-06 = *Traditionalist Tribute-Based Necrocracy*

---

## THE ZOETROPE CLOCK POSITIONS

The nine great colleges and their canonical alloys:

| Position | Institution | Governance | Economics | Ethos | Planar |
|---|---|---|---|---|---|
| 16 | Mortis Aevum | G-23 The Ascendancy | EC-17 Reserve Control | ET-06 Traditionalism | S-02 Ossuary |
| 02 | Deepguard | G-07 Technocracy | EC-20 Rent Extraction | ET-08 Integrity | None (suppressive) |
| 04 | Unity Academy | G-20 Absolute Monarchy | EC-09 Planned Economy | ET-16 Piety | None |
| 06 | Chiaroscuro | G-13 Direct Democracy | EC-18 Platform Arbitrage | ET-14 Expression | None |
| 08 | Sovereign Exchange | G-10 Corporatocracy | EC-18 Platform Arbitrage | ET-15 Exchange | None |
| 10 | Wildpath Wardens | G-18 Anarchy | EC-20 Rent Extraction | ET-01 Expansionism | V-05 The Hunt |
| 12 | Stormpeak | G-02 Stratocracy | EC-19 Capability Export | ET-13 Agonism | B-OMNI |
| 14 | Chronosynclastic | G-21 Kritarchy | EC-20 Rent Extraction | ET-18 Nihilism | P-02 Prophecy |
| Centre | Praxis Collegium | G-15 Republic | EC-18 Platform Arbitrage | ET-17 Secularism | Managed neutral |

