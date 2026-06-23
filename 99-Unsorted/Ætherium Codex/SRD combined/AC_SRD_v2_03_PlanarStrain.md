# THE ÆTHERIUM CODEX — System Reference Document
## Section: Planar Strain & The Mutation Economy

*Alpha SRD — Second Draft*

---

### PREAMBLE

Aíon did not want portals blinking open and closed. A portal is a rupture — raw planar energy flooding into an unprepared environment, destroying everything it contacts. Instead, Aíon caused planar boundaries to bleed. The bleed is gradual, sustained, and most importantly — it gives the affected area time to adapt. Trees near a Borderlands fire bleed develop fire-resistant bark over generations. Animals in a Verdant Font bleed zone develop accelerated healing. Soil in a Synod bleed zone mineralizes and fossilizes.

Mutations are not damage. They are adaptation. The Planar Strain system tracks the pressure that drives that adaptation, and the Mutation Economy tracks the cost of carrying the resulting power.

These are two connected but distinct systems:

**Planar Strain** governs WHEN a mutation expresses and WHAT it is. It operates before the mutation manifests.

**The Mutation Economy** governs the XP cost of having the mutation and the consequences of carrying more adaptation than your development can support. It operates after the mutation manifests.

The handoff point is the moment of expression — Strain builds until adaptation triggers, at which point a Nascent mutation manifests and its cost enters the debt ledger.

---

## PART I: PLANAR STRAIN — THE ADAPTATION PRESSURE SYSTEM

### What Strain Tracks

Strain measures how much adaptation pressure a specific planar expression is applying to a subject. Every planar exposure — ambient bleed zones, alchemical compounds, direct contact with expressed materials, magical effects — applies pressure that the subject's biology or material structure must negotiate.

Strain is tracked **per isotope.** A character exposed to B-01 Inferno and V-13 Cancer simultaneously carries two separate Strain counters because those are two different adaptations trending toward two different mutations. This is consistent with how real hazard exposure is tracked separately per substance.

### How Strain Accumulates

Each exposure event generates **Adaptation Pressure** — a value representing how intensely the incoming planar expression is pushing the subject toward a new state.

**Adaptation Pressure = Source Formation Stage × 2**

This value is then modified by the **interaction type** between the incoming expression and the subject's current state:

| Interaction Type | Pressure Modifier | Description |
|---|---|---|
| **Cooperative** | ×0.25 | The expression aligns with the subject's existing state. The body accepts it. Minimal adaptation needed. Healing potions, compatible enhancement, expression reinforcing what's already there. |
| **Competing** | ×1.0 | The expression conflicts with the subject's current state. The body must negotiate. Standard adaptation pressure. Incompatible expressions, forced exposure, occupational chemical contact. |
| **Cancellation** | ×1.5 | The expressions fight. The subject is caught between. Higher stress, higher adaptation demand. Antithetical exposure without Forge mediation. |
| **Emergent** | ×2.0 | Something new is being created. The subject has no template for this. Maximum adaptation demand. Emulsion exposure, unprecedented combinations. |

### Defense Against Strain

The subject defends using the **Metaphysical pillar.** Planar adaptation is a Metaphysical phenomenon — it changes what the subject IS at the planar level. The Metaphysical defense stats (Pattern, Dodge, Deflect, Soak, Threshold) apply.

The modified Adaptation Pressure acts as an "attack" against the Metaphysical defense. If the pressure penetrates the defense, the penetrating amount is added to the Strain counter for that specific isotope.

If the defense fully absorbs the pressure, no Strain accumulates from that exposure event. The subject's current planar identity successfully resisted the incoming influence.

### The Adaptation Threshold

When accumulated Strain on a specific isotope exceeds **(Integrity × 5)**, a Nascent Mutation manifests.

- High Integrity characters resist longer. More pressure must accumulate before expression triggers. But when it does, the higher accumulated Strain produces a more powerful mutation — they adapted slowly but thoroughly.
- Low Integrity characters mutate faster from less exposure. The mutations are proportionally weaker because less Strain had accumulated at the point of expression. They adapted quickly but shallowly.

At the moment of expression:
1. The Strain counter converts to a Nascent Mutation
2. The mutation's nature is determined by the source isotope's profile
3. The mutation's power level is built through the spell sentence system — higher accumulated Strain at expression produces higher ESL
4. The mutation's ESL determines its XP cost, which enters the Mutation Debt ledger
5. The Strain counter for that isotope resets to zero

### Exposure Types

**Acute Exposure (single event):**
One contact, one check. Direct touch of a mutated material, being hit by a planar expression in combat, drinking an alchemical compound. The full Adaptation Pressure is applied once.

**Chronic Exposure (sustained contact):**
Repeated or continuous exposure over time. Living in a bleed zone, working daily with hazardous materials, ongoing proximity to a strong planar source. Each exposure interval (per day for occupational, per week for environmental) applies Adaptation Pressure separately. Strain accumulates across intervals until the threshold is crossed.

**Deliberate Exposure (intentional mutation):**
The subject (or their alchemist) is deliberately seeking mutation. The Witcher potion, the Wildpath Warden's bio-management discipline. The exposure intensity and isotope are chosen by the practitioner. A Forge Calibrated component (F-16 Forge Mutagen) determines which specific mutation pathway expresses from the source isotope's profile, turning random adaptation into directed evolution.

### Interaction Type Determination

How to determine which interaction type applies:

**Cooperative:** The incoming expression reinforces or aligns with the subject's existing biology or planar profile. Healing a biological creature with V-01 World Tree is cooperative — the expression does what healthy biology already does. Enhancing a fire-adapted creature with B-01 Inferno is cooperative — more of what it already is.

**Competing:** The incoming expression conflicts with the subject's current state but isn't antithetical. Mercury exposure to a healthy human is competing — mercury's Borderlands mineral expression pushes toward mineralization, which conflicts with biological function but isn't cosmologically opposed to it. Most occupational and environmental exposures are competing.

**Cancellation:** The incoming expression is antithetical to an existing expression the subject carries. A Synod expression contacting a Font-mutated creature. A Borderlands expression contacting a Palimpsest-mutated material. The two expressions fight rather than negotiating. Without Forge mediation, one may destroy the other.

**Emergent:** The combination of incoming and existing expressions produces something neither would produce alone. This typically occurs with emulsion-bearing compounds or when multiple strong planar expressions interact within the same subject simultaneously. The result is unpredictable — the subject has no template for what they're becoming.

---

## PART II: PRACTICAL STRAIN SCENARIOS

### Standard Adventuring Potions (Safe)

A healing potion (V-01, FS 3, cooperative with healthy biology):
- Adaptation Pressure: 3 × 2 = 6
- Cooperative modifier: 6 × 0.25 = 1.5, round to 2
- Against standard Metaphysical defenses, this doesn't penetrate
- Result: the potion heals and passes through. No Strain. Safe for routine use.

### Professional Enhancement Compounds (Monitor)

A Hunt enhancement elixir (V-05, FS 5, cooperative with predatory biology):
- Adaptation Pressure: 5 × 2 = 10
- Cooperative modifier: 10 × 0.25 = 2.5, round to 3
- Single use: probably doesn't penetrate. Safe periodically.
- Daily use for months: 3 Strain per day accumulating. A scout relying on these daily eventually develops predatory biological traits. They adapted to their own medicine.

### Occupational Chemical Exposure (Manage)

An alchemist working unprotected with mercury (Borderlands mineral, FS 4, competing with biology):
- Adaptation Pressure: 4 × 2 = 8
- Competing modifier: 8 × 1.0 = 8
- Per day of unprotected exposure, 8 pressure against Metaphysical defense
- WITH proper protection (reducing effective FS reaching the body): lower daily pressure
- WITHOUT protection: Strain accumulates steadily. Borderlands mineral mutations develop — nervous system mineralization. This IS mercury poisoning.

### Deliberate Mutation Compound (Intentional)

A Witcher mutation potion (V-16 + F-16 Forge Mutagen, FS 7, competing with current template):
- Adaptation Pressure: 7 × 2 = 14
- Competing modifier: 14 × 1.0 = 14
- Penetrates most defenses significantly. Large single-dose Strain accumulation.
- Probably exceeds the Integrity × 5 threshold immediately, triggering Nascent expression.
- The F-16 Forge Calibrated component selects WHICH mutation pathway expresses — directed evolution rather than random adaptation.

### Emulsion Artifact Exposure (Extreme)

Contact with a Biotic Paradox emulsion artifact (Font + Synod, FS 6, emergent):
- Adaptation Pressure: 6 × 2 = 12
- Emergent modifier: 12 × 2.0 = 24
- Blows through almost any Metaphysical defense
- Massive immediate Strain. Likely triggers Nascent expression of something unprecedented.
- This is why emulsion artifacts are the most regulated items in the setting.

---

## PART III: THE MUTATION ECONOMY — THE XP DEBT SYSTEM

### Front-Loaded Power

Mutations give you power NOW. The ability is immediately available from the moment of Nascent expression. But the power has a cost, and the cost must be paid over time through XP investment.

### Mutation Cost

A mutation's XP cost is determined by building it through the spell sentence system. The mutation IS a complete spell sentence in a specific fixed configuration (a rote) — with an Effect, an Isotope, target geometry, range, duration, and any additives. The ESL of this rote determines the base XP cost.

The mutation also carries detriments if the character is in the Stressed zone. Each detriment costs the same XP as the positive side of the mutation.

### The Debt Ledger

When a Nascent mutation manifests, its total XP cost enters the character's **mutation debt ledger.** The power is immediately available. The debt remains until paid.

### The Two Thresholds

The thresholds are calculated from the character's **total lifetime XP** — including the equivalent XP value of creation choices (starting dots, backgrounds, etc.).

| Zone | Debt Range | Status | Consequences |
|---|---|---|---|
| **Safe** | Debt ≤ Lifetime XP × 2 | Clean adaptation | No detriments. The character's growth can absorb this level of change. The mutation expresses its benefits only. |
| **Stressed** | Lifetime XP × 2 < Debt ≤ Lifetime XP × 8 | Strained adaptation | Detriments manifest alongside benefits. The character is carrying more adaptation than their development cleanly supports. Each mutation in this zone expresses both positive effects AND negative side effects. |
| **Overwhelmed** | Debt > Lifetime XP × 8 | Catastrophic adaptation | The character's identity is losing coherence. Mutations are expressing uncontrollably. This is the crisis state that produces monstrous transformation. |

### Automatic Repayment

When mutation debt exceeds the ×2 Safe threshold:

**25% of all XP gained is automatically deducted and applied to mutation debt.** The character's growth is being consumed by adaptation pressure. This isn't optional — the body is directing resources toward integrating the change.

**Minimum floor:** There is a guaranteed minimum XP the player receives per session regardless of mutation debt. The player always has some agency over their character's development. The adaptation tax cannot consume everything.

### Natural Threshold Growth

Because the thresholds are based on **current lifetime XP**, simply gaining XP over time moves the ×2 and ×8 lines upward. A mutation that pushed you into the Stressed zone at Mastery 3 might fall into the Safe zone by Mastery 5 — not because you paid anything toward it, but because your total development grew enough that the mutation is proportionally smaller relative to who you are now.

You grew around it. The fire adaptation that was destabilizing at level 3 is just part of you at level 6.

### Paying Down Debt

A character can voluntarily invest XP into mutation debt at any time. This accelerates the payoff process beyond the 25% automatic deduction.

**Paying off the positive side (full debt clearance) = Calcification.** The mutation becomes permanent baseline. It costs nothing ongoing. It's just what you are. The Synod has Settled it. The Heritage State shifts from Active to Settled.

**Paying off the positive side does NOT remove the mutation.** The power stays. The obligation goes.

### Detriments

Each detriment that manifests in the Stressed zone has its own XP cost equal to the positive side of the mutation. Detriments are tracked separately in the debt ledger.

**Paying off a detriment ELIMINATES it.** Unlike the positive side (which stays when paid), the negative side disappears when its debt is cleared. You outgrew the problem. The fire adaptation no longer burns you from the inside because your biology learned to handle it.

Detriments can be bought down independently from the positive side's debt. A character might choose to pay off their detriment first (eliminating the downside) while still carrying debt on the positive side (the power remains, the obligation remains, but it no longer hurts).

### What Detriments Look Like

Detriments are the negative expressions of the same isotope that produced the positive mutation. They are mechanically built through the same spell sentence system as the positive side, using effects from the isotope's natural profile that work against the character.

A B-01 Inferno mutation in the Stressed zone might produce:
- **Positive:** Fire damage on contact, heat immunity, light production
- **Detriment:** Vulnerability to cold (the fire adaptation made the character cold-sensitive), uncontrolled combustion under stress (the fire expresses when the character doesn't want it to), or chronic tissue dehydration (the internal heat damages their own biology)

The detriment's nature is determined by the isotope profile and the character's specific situation. The storyteller selects detriments that are narratively meaningful — consequences that create story, not just penalties that punish.

---

## PART IV: THE FULL LIFECYCLE

### Stage 1: Exposure

The character encounters a planar expression — ambient bleed zone, alchemical compound, magical effect, direct material contact. Adaptation Pressure is calculated from the source's Formation Stage and the interaction type.

### Stage 2: Defense

The Adaptation Pressure "attacks" the character's Metaphysical defense. If it penetrates, the penetrating amount is added to the Strain counter for that specific isotope.

### Stage 3: Accumulation

Strain accumulates across exposure events. A single intense exposure might cross the threshold immediately. Chronic low-level exposure builds over weeks or months. The Alchemist path's chronic exposure management talent monitors these counters.

### Stage 4: Expression (Nascent)

When Strain exceeds (Integrity × 5), a Nascent Mutation manifests. The mutation's nature comes from the source isotope profile. Its power level is determined by the accumulated Strain, built through the spell sentence system. Its XP cost enters the debt ledger.

The character has the power immediately. The debt clock starts.

### Stage 5: Integration or Struggle

If total mutation debt is in the Safe zone (≤ Lifetime XP × 2): clean integration. Benefits only. The character adapts smoothly.

If total mutation debt is in the Stressed zone (> ×2, ≤ ×8): detriments manifest. The character has the power but it's causing problems. The 25% auto-repayment begins. The character is actively struggling with the adaptation.

### Stage 6: Growth

Over time, through automatic repayment, voluntary investment, and natural threshold growth from gaining XP, the debt shrinks relative to the character's total development.

Detriments can be bought off individually — each one eliminated is a problem solved.

### Stage 7: Calcification (Settled)

When all debt on a specific mutation is cleared — both positive and negative sides — the mutation Calcifies. Heritage State shifts to Settled. The mutation is permanent baseline. It costs nothing. It's who you are.

The Synod has claimed it. The adaptation is complete. The record is Settled.

---

## PART V: INHIBITORY TREATMENT

Synod Inhibitory expression (the anti-proliferative compounds from the Synod's functional repertoire) can arrest the adaptation process at any stage.

### Arresting Strain Accumulation

Inhibitory treatment applied during the accumulation phase reduces the rate of Strain buildup. The Inhibitory compound's Formation Stage reduces the effective Adaptation Pressure per exposure event. A FS 4 Inhibitory treatment reduces incoming pressure by 8 (FS 4 × 2), potentially preventing any Strain accumulation from low-intensity sources.

This is the alchemist's protective equipment expressed through the Synod — PPE as anti-adaptation chemistry.

### Arresting Nascent Mutation

Inhibitory treatment applied to a Nascent mutation shifts its Heritage State from Active to Arrested. The mutation persists at whatever level it reached but stops developing. Detriments that have manifested persist but don't worsen. The adaptation is frozen mid-process, carrying tension.

The mutation debt remains in the ledger. The 25% auto-repayment continues. The character still needs to pay off the obligation — but the mutation isn't getting worse.

Removing the Inhibitory treatment lets the process resume from where it was arrested. If the character is still exposed to the source isotope, Strain begins accumulating again from the current level.

### Inhibitory Treatment Cannot Reverse Calcification

Once a mutation has Calcified (Settled Heritage State, debt fully cleared), Inhibitory treatment has no effect. The adaptation is complete. The Synod has Settled it. Reversal would require Decomposition (alchemical operation to strip the expression) or Displacement (alchemical operation to replace it with a different expression), both of which are separate, significant procedures.

---

## PART VI: ITEMS AND STRAIN

Items experience planar adaptation through the same system but with different parameters.

Items do not have XP. They do not have a debt ledger. Their adaptation is tracked through Formation Stage progression and the condition track system.

When an item accumulates Strain beyond its material's current capacity (determined by base material Tier rather than Integrity), it manifests a mutation. The mutation's nature comes from the source isotope. Its power level is constrained by the material's Formation Stage (the bottlenecking principle). The mutation becomes part of the item's combined state.

Item mutations don't have "detriments" in the XP sense — they have the crafting mutation system (benefits and flaws from the Item Creation section). A mutation that manifests in an item through environmental exposure rather than deliberate crafting follows the same benefit/flaw logic but without the crafter's ability to manage the outcome.

This is why naturally mutated materials are valued — the mutation occurred through genuine adaptation, producing expressions that are organically integrated with the material's nature. And why they're unpredictable — nobody controlled the conditions under which the adaptation occurred.

---

*End of Planar Strain & Mutation Economy. Next section: Item Creation — The Crafting System.*
