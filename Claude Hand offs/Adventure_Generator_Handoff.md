# ÆTHERIUM CODEX — Adventure Generator Development Handoff

## Purpose of This Document

This is a handoff brief for developing the ÆC Adventure Generator and Society Generator systems in a new chat session. It captures architectural decisions, established systems, identified gaps, and the specific role the generator plays in the broader production ecosystem. Read this before beginning work.

---

## What the Adventure Generator IS

The Adventure Generator operates at **S5–S6 scope** — the city/territory layer where local governments operate, guild halls exist, and players have a base of operations. It is the scope step between guilds (S4) and colleges (S7). It produces adventure hooks and mission frameworks that:

- Emerge procedurally from established setting systems (isotopes, political alloys, institutional fronts)
- Function as mini-arcs that build into campaign arcs
- Serve as player backstory elements that cook over a campaign
- Represent local governments asking for help or running operations
- Generate the content the protagonist walks through in the novel/audiobook pipeline
- Feed the production model (each generated hook produces harvestable products across the scope stack)

The generator does NOT invent content from nothing. It reveals what a territory's configuration *necessarily produces* given its inputs.

---

## The Three Inputs That Drive Generation

### Input 1: Political Alloy (Zoetrope Position)

Every territory sits at a position on the 16-position Political Zoetrope. Each position is defined by a three-axis alloy:

- **Governance** (24 types: e.g., Technocracy, Republic, Kritarchy, Theocracy, Stratocracy)
- **Economic Model** (20 types: e.g., Platform Arbitrage, Rent Extraction, Soul Trade, Capability Export)
- **Ethos** (20 types: e.g., Integrity, Agonism, Secularism, Traditionalism, Piety)

The alloy determines what the local government's priorities are, how it operates, and what it values. This directly determines what kinds of contracts appear on the guild hall board.

Reference document: **Political Zoetrope system v2.docx** — contains all 16 positions with full alloy specifications, gradient zones between positions, and lifecycle role descriptions.

### Input 2: Isotope Profile

Every territory has a dominant and secondary planar layer from the five planes, a Formation Stage band (1–10), and resource distribution asymmetries.

- **Five Planes:** Borderlands (physical), Verdant Font (biological), Synod of Endings (entropic), Palimpsest (informational/dimensional), Hidden Forge (directed/catalytic)
- **104 isotopes** across five planes, each with defined natural effects, hard exclusions, and Formation Stage shift behaviors
- **Geology-bleed resonance model:** matching geology + bleed = laminar high-intensity; mismatched = turbulent reduced-intensity

The isotope profile determines what environmental conditions exist, what resources are available, what creatures emerge, and what kinds of hazards the territory produces.

Reference documents: **ÆC Isotopes Combined.md**, **AC Unified Architecture.md** (Part I: The Dissolved Solution, Isotope Expression Guide section)

### Input 3: Institutional Landscape

Which colleges, guilds, noble houses, corporations, Fey courts, unaffiliated populations, and criminal economies operate in the territory. Each institutional presence generates fronts. Each overlap or gap between institutions generates pressure points.

Reference documents: **Merged Colleges v1.md**, **Aetheric pet system unified (1).md** (guild structure section), **0_ÆC Operating Philosophy Final 1.docx** (Front Architecture, Faction Turn Procedures)

### Derived: Territorial FP

Count the pressure points: Zoetrope transition pressures, isotope asymmetries, institutional conflicts, population tensions. More pressure points = more active territory = more simultaneous hooks = larger GM narrative energy budget.

Reference document: **0_ÆC Operating Philosophy Final 1.docx** (Profiling Territories section in Document 1B)

---

## Existing Component Systems (Already Built)

These systems exist and are documented. The Adventure Generator assembles them into a unified procedure.

### Document 5A — Seed Management
Seven-step prep workflow using five tools: Three Clue Rule, Schrödinger's Gun, Chekhov's Gun, Lazy DM Prep, Node-Based Design. Seeds are potential events that become actual when players engage.

### Document 5B — Oracle Tables
Three-axis random generation: d10 (Axis 1: planar source) × d20 (Axis 2: effect type) × d6 (Axis 3: contextual modifier) = 1,200 combinations. Includes interpretation procedure and worked examples.

### Document 5C — Isotope Expression Guide
Five alchemy layer profiles with cross-layer symptoms and a five-step translation procedure:
1. Identify the effect (from clock symptoms or oracle Axis 2)
2. Identify the plane (from driving college alignment or oracle Axis 1)
3. Check the territory's local isotope distribution
4. Select the expression (effect + layer = visual vocabulary)
5. Add human-scale detail ("Not 'vegetation surge in sector 7.' Instead: 'The baker's garden has grown through his kitchen wall overnight.'")

### Document 4C — Pacing and Beat Analysis
Beat vocabulary, Scene/Sequel structure, session generator integration, six session patterns, session boundaries.

### Document 1B — Profiling Companions
How to apply the Psyche Schema to territories: Zoetrope position as Core Philosophy equivalent, isotope profile as Resource Landscape, institutional landscape as Operational Context. Territorial FP generation from these inputs.

### Document 3A — Front Architecture
Four front types (Institutional, Individual, Environmental, Reactive), eight-field template (Identity, Motivation, Methodology, Assets, Representation Chain, Clocks, Relationships, Failure Trajectory).

### Document 3C — Faction Turn Procedures
Four action types (Expand, Defend, Attack, Influence), nine-college methodology matrix showing how each college expresses each action type, ten-step between-session procedure.

---

## What Needs Building

### The Adventure Generator Coupling Document
Referenced in the Operating Philosophy as a "future build" dependency. It needs to formalize how Schema pressure points tag to adventure situations for mid-session FP recovery. The pressure points are pre-identified (Document 2A). The situations need pre-tagging. The intersection is a lookup operation.

### The Society Generator (Pages 3–9 Unextracted)
Source material exists from prior Gemini sessions but has not been extracted or uploaded. If the original source documents can be located, extract before rebuilding from scratch.

### The Adventure Generator (Pages 4–9 Unextracted)
Same status. Source material likely exists in prior Gemini conversation exports or original design documents.

### The Hookgen Procedure (New)
Formalized procedure combining all three inputs into adventure hook output. Proposed seven-step process (from this conversation):

1. **Set the alloy.** Pick or roll governance + economic model + ethos. This tells you what the local government posts to the guild hall.
2. **Set the isotope profile.** Pick or roll dominant/secondary planar layers, Formation Stage band, asymmetries. Cross-reference with Isotope Expression Guide for environmental conditions. Each condition is a potential hook.
3. **Set institutional presence.** Determine which colleges, guilds, noble houses, corporations, Fey, and unaffiliated populations operate. Each overlap or gap is a potential hook.
4. **Derive territorial FP.** Count pressure points. This determines how many hooks are active simultaneously.
5. **Apply Isotope Expression Guide translation.** For each active environmental condition, translate through the five-step procedure to produce human-scale adventure seeds.
6. **Apply institutional intersection.** For each pair of competing interests, identify what each side wants and where methods collide. Each collision is a contract opportunity arriving at the guild hall as competing job postings.
7. **Apply social deviance overlay.** For each institutional presence, generate its shadow: anti-collegiate community, wildcat practitioners, criminal economy, religious heterodoxy.

### Hook-to-Product Pipeline Mapping
Each generated hook should automatically map to a product pipeline slot:
- Which scope level does this hook operate at?
- Which content type does it produce? (adventure module, creature reveal, NPC dossier, etc.)
- Which delivery channel carries it? (Patreon, audiobook, weekly drop, etc.)

---

## The Default Timeline Context

The adventure generator operates within a world that has specific ongoing conditions. These are NOT adventure hooks themselves — they are the background state that the generator operates within. Hooks emerge from the intersection of these conditions with specific territorial configurations.

### Ongoing Operational Theaters
- **The Titanwood** — permanent hazardous zone, convoys, creature encounters, Fey diplomacy, biological harvesting
- **The Desert Ruins** — Palimpsest folds near Calamity ground zero, spelunking, artifact recovery
- **Maritime Operations** — merged ocean jurisdictions, piracy, sea creatures, coast guard
- **Air Operations** — WW2-Vietnam era aircraft + flying creatures, contested air superiority
- **Convoy Duty** — routine trade route security through unmapped wilderness
- **Harvesting** — isotope materials, creature components, Palimpsest artifacts

### Ongoing Institutional Intersections
- **Position 13 — The Games** — formalized combat as entertainment/political proxy
- **Lyra vs. The Maestro** — grand strategic chess match across the clock
- **Noble/Corporate Cold War** — magi-feudal proxy conflicts
- **Soul Queue Politics** — jurisdictional disputes, soul stone black market

### Ongoing Environmental Phenomena
- **Three generations of Fey** — Elder, Lost, Newborn (narrative immune response)
- **Lacunae** — gaps where the Smoothing Effect didn't take
- **Mutation Pressure Zones** — high Formation Stage slow accumulation
- **Reality Seam Activity** — Dormant through Catastrophic
- **Ætherforged** — war golems with experiential continuity
- **Cephalarchs** — void-touched intelligences breaking probability models
- **Strange Signals** — Kan-tech broadcasts from unmapped locations
- **Anomalous Biological Phenomena** — unclassified encounters

### Ongoing Social Deviance
- **Smoothing Effect Deniers** — perceptible at Master+ mastery level
- **Anti-Collegiate Movements** — frontier communities refusing institutional jurisdiction
- **Wildcat Magic Users** — folk traditions predating the colleges
- **The Unaffiliated Ecosystem** — freelancers, deserters, criminals (needs own system track)
- **Criminal Economies** — shadow versions of every college's commercial services
- **Alchemists / Mutation Chasers** — legitimate researchers vs. uncontrolled self-experimenters
- **Religious Heterodoxy** — local deities, positional divinity, potential Lacuna entities
- **Information Anarchists** — stealing and freely distributing curated intelligence

---

## Nine College Commercial Services (for guild hall context)

Each college provides a purchasable service to ordinary people. These determine what kinds of institutional contracts appear at guild halls.

| College | Service | Commercial Expression |
|---|---|---|
| Mortis Ævum | Closure | Funeral services, resurrection processing, ancestral records, grief counseling |
| Deepguard | Security | Wards, self-executing contracts, vault storage, licensing |
| Stormpeak | Protection | Contingency charms, infrastructure, trauma medicine, military escort |
| Unity | Wellness | Sim stims, Mycora bonding, social integration, psychological assessment |
| Chiaroscuro | Entertainment | Media, performances, broadcasts, news |
| Chronosynclastic | Probability | Insurance, risk assessment, forecasting, casino |
| Sovereign Exchange | Access | Trade brokerage, enchanted goods, currency exchange |
| Wildpath | Biological Expertise | Creature management, pest control, environmental assessment, guide services |
| Praxis | Education | Basic magical literacy, cross-disciplinary training |

---

## Guild Structure (the S4 layer the generator feeds into)

### Three Tiers
- **Tier 1 — Corporate Body:** Major cities, regional capitals. Funding, logistics, legal authority, licensing.
- **Tier 2 — Way Stations:** Local hubs across all inhabited lands. Tavern/Inn, Guild Hall (job boards, mission payouts), Apothecary, Lab/Forge, Garden.
- **Tier 3 — Shell Game:** Political maneuvering. Rival guilds, government factions, college schools, noble houses competing for exclusive rights, contracts, sponsorship, territory.

### Multi-Financing
A single guild can be simultaneously funded by a college (research mandate), local government (public safety), noble house (private interests), and private investors (profit). Competing loyalties create philosophical tensions that ARE adventure hooks.

### Guild Contract Types (from Aetheric Pet System)
1. Creature Capture Contracts (2–10 days)
2. Planar Breach Response (1–4 days, high danger)
3. Territory Clearance (3–10 days)
4. Breeding Program Support (ongoing)
5. Research Expeditions (1–4 weeks)
6. Diplomatic Mission (variable)
7. Creature Rescue (2–7 days, combat-heavy)

These are creature-focused. The adventure generator should produce equivalent contract type lists for ALL guild functions, not just creature handling.

---

## The Production Pipeline Connection

Every adventure hook generated should be traceable to a production pipeline slot. The production model established in this conversation:

**The narrative dictates the yield, not a production quota.** Nothing exists as a standalone product that doesn't first exist in the narrative. If a rote card shows up in a weekly drop, somewhere in the manuscript a character cast it. The traceability IS the coherence the system rewards.

**Core Production Assets (master sources everything is cut from):**
1. **The Script** — one continuous narrative scene producing audiobook, audio walkthrough, radio drama, journal fragments, TikToks, podcast episodes, and all text derivatives
2. **Creature Design Package** — one creature producing 10+ deliverables from silhouette tease through compendium
3. **Zone Dossier** — one territory producing territory supplement, map, adventure setting, NPCs, creatures, items, music, art, advertisements
4. **Spell/Rote, Item, NPC Designs** — each branches into cards, curriculum entries, audio segments, encounter elements
5. **Art and Music** — each piece feeds 9+ product channels

**The adventure generator's output should tag which production assets each hook requires.** A hook involving a new creature triggers a Creature Design Package obligation. A hook set in an undefined territory triggers a Zone Dossier obligation. A hook involving a specific rote triggers a Spell Design obligation. This connects the generator directly to the production schedule.

---

## Canonical Terminology (must use exactly)

Soak (not DR), TN (not DC), Kan-tech (not magi-tech), Composite Defense (not AC), Poise (social HP pool), Clout (not Influence for the background), Achieved ESL, Pivot Pool, Construction Pool, Equivalent Exchange, Psyche Schema, Spell Sentence, Formation Stage, Fulcrum Points, Planar Strain, Aetheric Corruption, Smoothing Effect, Lacunae, Primal/Structured Current, Torrent flow state.

The Synod of Endings is not "the plane of death." The Verdant Font is not "the plane of life." The Palimpsest is not a featureless void.

---

## Key Design Principles

- The same unified grammar operates at every scale with no special cases
- Condition Tracks ARE clocks (identity statement, not analogy)
- The Spell Sentence IS the symptom vocabulary at every scale
- Narrative-first, not player-forward
- Raise the floor so all options achieve comparable depth — never reduce power to achieve balance
- Every subsystem must derive from the setting's own cosmology
- The struggle is the golden age; every Zoetrope position functions simultaneously
- Do not import external framework affect (Spenglerian decline, "dark fantasy") onto an ongoing setting
- Do not flatten cognitive complexity in the name of accessibility — this breaks the teaching function
- Read source files before asserting anything about setting content
- Catalogue all source concepts before making consolidation decisions — full survey precedes implementation

---

## Priority Actions for the New Chat

1. **Locate and extract** the Adventure Generator (pages 4–9) and Society Generator (pages 3–9) source documents if they exist in uploaded files or can be provided
2. **Survey** existing component systems (5A, 5B, 5C, 4C, 1B, 3A, 3C) to identify what's already formalized
3. **Build the hookgen procedure** as a formalized seven-step process connecting the three inputs to adventure hook output
4. **Define adventure hook categories** beyond creature-handling: institutional, environmental, social deviance, criminal, theological, ecological, personal (NPC Schema-driven)
5. **Create the FP × situation coupling table** — how Schema pressure points tag to adventure situations for mid-session recovery
6. **Map hook output to production pipeline slots** — each hook automatically identifies which production assets it requires and which scope/channel it feeds

---

*End of handoff. This document should be provided as context at the start of the new chat along with the project knowledge files.*
