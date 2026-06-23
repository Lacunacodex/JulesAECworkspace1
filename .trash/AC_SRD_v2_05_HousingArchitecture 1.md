# THE ÆTHERIUM CODEX — System Reference Document
## The Housing Architecture — Staves, Attachments & Insets

*Alpha SRD — Second Draft*

---

## PREAMBLE

A staff is not a weapon that casts spells. It is a platform — an architectural housing built from a material whose quality determines how many systems it can support, how powerful those systems can be, and how they route to produce their effects. A wand is the same architecture at smaller scale with a lower ceiling. The distinction is material quality, not purpose. Everything described here applies to any item with slots — swords, armor, rings, staves, wands. The architecture is universal.

---

## PART I: MATERIAL GRADE AND CAPACITY

Material Tier — derived from physical properties as modified by mutations — determines architectural capacity. Tier equals slots. Tier caps maximum EML.

**Wand-Grade (Tier 1-4):** Limited slots, low EML ceiling. Single-purpose tools, consumer-grade equipment, focused devices. The material cannot support complex architecture regardless of effort.

**Staff-Grade (Tier 5-10):** Sufficient capacity for complex multi-system architectures. The platform grows with the wielder as slots are filled over a career.

| Tier | Grade | Slots | EML Ceiling |
|---|---|---|---|
| 1 | Wand | 1 | 1 |
| 2 | Wand | 2 | 2 |
| 3 | Wand | 3 | 3 |
| 4 | Wand | 4 | 4 |
| 5 | Staff | 5 | 5 |
| 6 | Staff | 6 | 6 |
| 7 | Staff | 7 | 7 |
| 8 | Staff | 8 | 8 |
| 9 | Staff | 9 | 9 |
| 10 | Staff | 10 | 10 |

**Ceiling Versus Current Expression:** A Tier 8 staff with one EML 2 rote is currently EML 2 sitting in a Tier 8 housing with seven empty slots. Material quality is an investment in future potential.

---

## PART II: INTERNAL EXPRESSIONS

A housing's base material — through its mutations and enchantments — can possess its own internal rotes. These belong to the material itself.

Internal rotes:
- Originate from base material mutations/enchantments
- Use the item's own EML when activated
- Generate charges through the drip recharge system
- Are permanent features — removal requires alchemical decomposition
- Count as Active Expressions toward EML
- Route through internal architecture and can be modified by insets they pass through

All housings are inherently hybrid — every item with a material Tier can carry internal rotes AND accept attachments AND channel spells through it. These are not separate configurations but simultaneous capabilities of the same architecture.

---

## PART III: SLOT COMPONENTS

Every slot on a housing can hold one of four component types:

### Attachments

A sub-item carrying one rote, installed in a slot. Each attachment is a complete item with its own full material reading:
- Base material with physical properties (Hardness, Tensile, Density, Conductivity, Elasticity on 1-10 scales)
- Heritage State, Formation Stage, isotope identity
- Own four-pillar condition track (Physical/Mental/Social/Metaphysical)
- Own charge pool generated from own material through the drip system

**Portability:** Attachments can be removed from one housing and installed in another, provided the destination has an empty slot and the attachment is compatible. Removal and installation are separate Artifice checks performed by an Enchanter.

**Material Contribution:** When a spell routes through an attachment, the attachment's material properties modify the spell alongside the parent housing's properties. A copper attachment in a heartwood staff contributes copper's conductivity to spells routed through it.

**Rote:** Each attachment carries one rote — a complete spell sentence in fixed configuration. Changing the rote requires decomposition and recomposition. When activated, uses item EML.

### Insets

A spell sentence modifier installed in a slot. Does not carry its own rote. Each inset corresponds to one or more Additives or Subtractives from the spell sentence system, made into a physical component.

**What Insets Modify:** Any rote or channeled spell that passes through the inset's position in the routing architecture. A Chain inset adds Chain targeting. A Range inset extends reach. The modification applies automatically to everything routed through that position.

**Charge Generation:** Insets generate charges as a secondary function of their material. These can be linked to other components via Forge Links to supplement charge-hungry rotes elsewhere.

**Material Properties:** The inset's material shapes HOW the modification expresses. A Chain inset in copper performs differently from a Chain inset in ceramic.

**Stacking:** Same-type insets in the same routing path do not stack (take highest). Different-type insets in the same path do stack. Insets in different routing paths only affect expressions passing through their specific path.

### Batteries

A dedicated power storage component occupying a regular slot. The base material generates its own charges naturally, so a battery is a trade-off — more power budget at the cost of one fewer capability slot. The battery's material determines its recharge rate through the drip system.

### Forge Links

A Forge Interfacial component connecting two or more slots to share charge pools. The shared pool is capped by the lower expression of the linked components. Linking doesn't enhance — it shares. Useful when one component generates surplus charges and another runs a deficit.

---

## PART IV: THE EML CALCULATION

**EML = Highest Active Expression + floor((Total Active Expressions − 1) ÷ 4)**

**Active Expressions include:**
- The housing's own internal rotes (from mutations/enchantments)
- Each attachment's rote

**Active Expressions do NOT include:**
- Insets (modify, don't produce independent effects)
- Batteries (store, don't produce effects)
- Forge Links (connect, don't produce effects)

**Example:** A Tier 8 staff with 2 internal rotes (CML 4, CML 3), 3 attachments (CML 4, CML 3, CML 2), 2 insets, 1 Forge Link:
- Active Expressions: 5 (2 internal + 3 attachments)
- Highest CML: 4
- EML = 4 + floor((5−1) ÷ 4) = 4 + 1 = **EML 5**

Fits within Tier 8 ceiling. Three more slots available. Room to grow.

---

## PART V: THE ROUTING ARCHITECTURE

When a spell is activated or channeled through a housing, it follows a physical path. The spell is modified ONLY by what it passes through — base material, attachments in the path, insets in the path. Components outside the routing path have no effect.

The Forge Channeled lane builds the channels. The Forge Interfacial lane builds the junctions and gates. Routing is a deliberate, permanent crafting decision.

### Linear Routing

Everything in sequence. Spell enters at one end, passes through all components, exits. All modifiers stack. Maximum modification, zero selectivity. Simplest architecture — novice crafters default to it.

### Parallel Routing

Independent channels. Spell enters base material, wielder directs to one channel. Only that channel's modifiers apply. Maximum selectivity, each path less modified. Architecture for multi-purpose items.

### Selective Routing

Junction points with Forge Interfacial switches. Wielder directs flow between paths, combines paths, or bypasses components. Tactical options — fire channel alone, ice channel alone, or both through a shared modifier. Most complex architecture, requires Journeyman+ Forge work.

### Routing and Internal Rotes

When the housing activates its own internal rote, the expression originates in the base material and follows the architecture. If the channel passes through an inset, the inset modifies the internal rote. Strategic inset placement enhances innate abilities.

### Routing and Channeled Spells

When a caster channels their own spell, the spell enters the base material and follows the designated path. The base material's physical properties modify spell parameters through the property-to-spell-sentence mapping. Insets and attachments in the path further modify. The caster uses their own stats (Mastery, Effect Tier, Isotope Tier). The housing adds its material contributions on top.

---

## PART VI: CHARGE POOLS AND POWER

### Self-Generation

Every rote-bearing component generates its own charges through the drip system. The housing's base material powers its internal rotes. Each attachment powers its own rote from its own material. Generation rate determined by Formation Stage and interaction profile. Pools are isolated by default.

### Forge Links

Bridge two or more pools. Shared pool capped by lower expression. Surplus feeds deficit through the link.

### Channeled Spell Costs

Channeling through the housing uses the caster's own ÆP. The housing's charges are not consumed — the caster provides energy, the housing provides modification. Housing charges are only consumed when internal rotes or attachment rotes are triggered.

---

## PART VII: ACTIVATION AND ACTION ECONOMY

**Triggering an item rote:** Standard action. Uses item EML. Wielder does not need to be a practitioner — the item does all the work.

**Channeling through the item:** Whatever action the spell normally requires. Material modifications apply automatically as part of casting. No additional action cost.

**Multiple activations:** Each rote is independent. Activating one doesn't prevent activating another next round. The action economy limits throughput — one standard action per round, multiple tactical options available.

---

## PART VIII: INSTALLATION AND REMOVAL

### Installation

Requires empty slot, component to install, appropriate tools, Enchanter-path Artifice skill. Artifice check vs TN (10 + component CML + item's current Instability rating). Time: 1 day per CML minimum.

**Success:** Component seated and integrated. EML recalculated if Active Expression added.
**Failure:** Component damaged. Failure by 5+: slot itself damaged, requires repair before accepting new component.

### Removal

Same practitioner skill and TN. 

**Success:** Component extracted intact. Slot cleared.
**Failure:** Component damaged or destroyed. Failure by 5+: slot damaged.

### Compatibility

An Analyzer/Appraiser can assess compatibility before installation — identifying competing combinations, antithetical conflicts, and Metaphysical condition track risks before the attempt.

### Nested Architecture Limits

Two levels only — housing and components. Attachments cannot hold further nested components. Prevents infinite complexity.

### Condition Track Independence

Each component maintains its own condition track independently. The housing can be Pristine while an attachment is Worn. Damage to one doesn't automatically damage others (unless specifically targeted or distributed proportionally). A component at Broken or Destroyed ceases functioning — its rote, modifications, and charge generation stop until repaired or replaced.

---

## PART IX: ITEMS AS CAREER PLATFORMS

The housing architecture is designed for long-term growth.

**Early Career:** Staff-grade material acquired. One or two rotes installed. Most slots empty. EML low. The material represents potential far exceeding current expression.

**Mid Career:** Attachments added as capabilities develop. Insets installed. Routing becomes more complex. EML climbs. The item reflects the wielder's growing expertise.

**Mastery:** Most slots occupied. Sophisticated selective routing. Forge Links managing charge distribution. Internal rotes deepened through Legacy. EML approaching Tier ceiling. The item has a reputation, a history, a legend — its Social condition track reflects decades of significant use.

---

*End of Housing Architecture. Next section: Legacy & Ascension.*
