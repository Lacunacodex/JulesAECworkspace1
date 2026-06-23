# THE ÆTHERIUM CODEX — System Reference Document
## Section: Attachments & Insets — Components in the Architecture

*Alpha SRD Draft — Working Document*

---

### PREAMBLE

The Staves section established the housing architecture — material grade, slots, routing, charge pools, and activation. This section addresses the two primary component types that occupy those slots: attachments (rote holders) and insets (spell sentence modifiers). Both are modular. Both are portable. Both are crafted items in their own right with their own material readings.

---

## PART I: ATTACHMENTS

An attachment is a sub-item installed in a slot on a parent housing. It carries one rote, has its own base material with its own physical properties, generates its own charges through the drip recharge system, and contributes its material properties to any spell that routes through it.

### Attachments as Independent Items

Every attachment has its own full material reading:
- Base material with physical properties (hardness, tensile strength, density, conductivity, elasticity)
- Heritage state (Active, Arrested, or Settled)
- Formation Stage (determining quality and charge generation rate)
- Any mutations expressing in its own material
- Its own four-pillar condition track (Physical, Mental, Social, Metaphysical)

An attachment is a complete item that happens to be designed for installation in a larger housing. A wand removed from a staff is still a functional wand. It retains its rote, its charge pool, its material properties, and its condition tracks. It simply loses the routing context of the parent housing.

### Portability

Attachments can be removed from one housing and installed in another, provided:
- The destination housing has an empty slot
- The attachment is physically compatible with the housing's architecture (an Enchanter or qualified Artisan can assess compatibility)
- The installation procedure is performed by a practitioner with appropriate Artifice skill

Removal and installation follow the Enchanter path's procedures. Successful removal preserves the attachment intact. Failed removal risks damage to the attachment, the slot, or both.

### Attachment Material Contribution

When a spell routes through an attachment, the attachment's material properties modify the spell alongside the parent housing's material properties. A copper wand-attachment installed in a heartwood staff contributes copper's conductivity to spells routed through it, even though the staff itself is wood.

This means attachment material selection is a deliberate tactical decision. The crafter choosing what material to build the attachment from is choosing what modifications that attachment will impose on everything passing through it — in addition to whatever rote it carries.

### Attachment Rotes

Each attachment carries one rote — a complete spell sentence in fixed configuration. The rote is composed during creation using the spell sentence grammar and is permanent once installed in the attachment. Changing the rote requires alchemical decomposition of the existing rote and composition of a new one — effectively rebuilding the attachment's magical core.

The rote's parameters (Effect, Isotope, Target/Range/Duration, Additives) are determined at composition. When activated, the rote uses the item's EML for power scaling. The attachment's own material properties influence the rote's expression through the property-to-spell-sentence mapping.

### Attachment Charges

Each attachment generates its own charges from its own material through the drip recharge system. The generation rate is determined by the attachment's Formation Stage and its interaction profile (Static, Cycling, Projecting, or Absorbing). This pool is isolated by default — it powers only this attachment's rote unless a Forge Link connects it to another component's pool.

---

## PART II: INSETS

An inset is a spell sentence modifier installed in a slot on a parent housing. It does not carry its own rote. Its function is to alter specific parameters of rotes or channeled spells that pass through its position in the routing architecture.

### What an Inset Modifies

Each inset corresponds to one or more entries from the spell sentence system's Additives or Subtractives. The inset IS the Additive or Subtractive made into a physical component and installed in the item's architecture.

**Additive Insets** — enhance expressions passing through them:

| Inset Type | Spell Sentence Equivalent | What It Does |
|---|---|---|
| Chain Inset | Chain (+3) | Expressions arc to secondary targets |
| Range Inset | Enlarge equivalent | Expressions reach further |
| Area Inset | Widen equivalent | Expressions cover more space |
| Duration Inset | Extend equivalent | Expressions persist longer |
| Penetrating Inset | Penetrating (+2/+4/+6) | Expressions bypass defenses |
| Selective Inset | Selective (+1) | Wielder can exclude targets from area effects |
| Split Inset | Split (+1) | Single-target expression divides between multiple targets |
| Persistent Inset | Persistent (+3) | Target must make two defense checks, take worse result |
| Homing Inset | Homing (+2) | Missed projectiles get additional chances |
| Subtle Inset | Subtle (+1/+2) | Expression is difficult or impossible to perceive |

**Subtractive Insets** — impose limitations in exchange for reduced costs:

| Inset Type | Spell Sentence Equivalent | What It Does |
|---|---|---|
| Focus Inset | Limited (-1 to -4) | Expression restricted to specific target types — but more potent against them |
| Concentration Inset | Concentration (-2) | Expression requires active focus to maintain |
| Delayed Inset | Delayed Activation (-1) | Expression activates on a trigger condition rather than immediately |

This list is not exhaustive. Any Additive or Subtractive from the spell sentence system can theoretically be built into an inset. The crafting difficulty and Formation Stage requirements scale with the Additive's complexity cost.

### Inset Charge Generation

Insets do generate charges through the drip recharge system based on their own material's Formation Stage and interaction profile. This is not their primary function — their primary function is modification — but the charge generation exists as a property of the material. These charges can be linked to other components through Forge Links, potentially supplementing a charge-hungry rote elsewhere in the architecture.

### Inset Material Properties

Like attachments, insets have their own material reading. The inset's material properties contribute to the modification it provides. A Chain inset made from high-conductivity copper performs differently than a Chain inset made from insulative ceramic — the copper's conductivity enhances the arcing behavior, while the ceramic might produce a more controlled, directed chain.

This means inset material selection matters beyond just meeting Formation Stage requirements. The material shapes HOW the modification expresses, not just WHETHER it applies.

### Stacking and Interaction

Multiple insets of the same type in the same routing path do not stack by default — you take the highest. This follows the modifier type system: insets providing the same modification are the same modifier type and the best one applies.

Multiple insets of DIFFERENT types in the same path do stack — each modifies a different parameter and all apply. A Chain inset and a Range inset in the same routing path produce an expression that both arcs to secondary targets and reaches further. These are different modifications that combine.

Insets in DIFFERENT routing paths only affect expressions that pass through their specific path. An inset in Channel A has no effect on expressions routed through Channel B.

---

## PART III: INSTALLATION AND REMOVAL

### Installation

Installing an attachment or inset into a housing requires:
- An empty slot on the housing
- The component to be installed
- Appropriate tools
- A practitioner with sufficient Artifice skill (Enchanter path)

The installation is an Artifice check against a TN determined by the component's complexity and the housing's current architecture. Successful installation seats the component in the slot and integrates it into the routing architecture. The item's EML is recalculated if the new component is an Active Expression (attachment with rote).

### Removal

Removing an attachment or inset requires the same practitioner skill and tools. Removal is an Artifice check against the same TN as installation.

- **Successful removal:** The component is extracted intact. The slot is now empty and available. The component can be stored, traded, or installed in a different housing.
- **Failed removal:** The component is damaged during extraction. Depending on severity, it may be degraded (condition track damage) or destroyed. If the failure is severe (by 5 or more), the slot itself may be damaged and require repair before accepting a new component.

### Swapping

Replacing one component with another requires removal of the existing component followed by installation of the new one. These are two separate Artifice checks — one for removal, one for installation. A failed removal doesn't prevent attempting installation of the new component (the slot is cleared regardless, the question is whether the old component survives), but a damaged slot from a severely failed removal must be repaired first.

---

## PART IV: COMPATIBILITY AND EDGE CASES

### Material Compatibility

Not every attachment is compatible with every housing. An attachment whose material properties produce interactions that conflict with the housing's material may cause:
- Competing combinations at the contact boundary (the attachment's planar expression fights the housing's)
- Degradation of one or both materials over time (the Synod's claim accelerates when antithetical expressions are forced into proximity)
- Reduced effectiveness of rotes routed through the conflict zone

An Analyzer can assess compatibility before installation. An Enchanter with Forge Interfacial skill can install boundary management components to mitigate incompatibility — but this consumes additional slots.

### Orphaned Attachments

An attachment removed from a housing and not installed elsewhere continues to function as a standalone wand. It retains all properties. However, without the parent housing's routing architecture, it loses access to any inset modifications and any Forge Link charge sharing it previously benefited from.

### Nested Architecture Limits

A staff can hold wand-attachments. Those wand-attachments cannot themselves hold further nested components. The architecture permits two levels — housing and components — but not recursive nesting. This prevents infinite complexity and keeps the system tractable at the table.

### Condition Track Independence

Each component maintains its own condition track independently of the parent housing. The staff can be Physically Pristine while one of its wand-attachments is Physically Worn from heavy use. Damage to the staff doesn't automatically damage the attachments (unless specifically targeted or distributed under the proportional distribution rule). Damage to an attachment doesn't damage the staff.

However, a component whose Physical condition reaches Broken or Destroyed ceases to function in the architecture. Its rote cannot be activated, its inset modifications don't apply, its charge generation stops. The slot is effectively dead until the component is repaired or replaced.

---

*End of Attachments & Insets section. Next section: Legacy & Ascension — The Palimpsest History.*
