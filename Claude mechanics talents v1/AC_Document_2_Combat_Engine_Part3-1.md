# THE ÆTHERIUM CODEX — THE COMBAT ENGINE
## Document 2, Part III: Resolution at the Dice Level
### Canonical Draft — April 15, 2026

---

## PREAMBLE

Part I established the architectural foundations. Part II covered engagement states, the reaction economy, multi-pillar combat, multi-Scope play, and representative S0-S2 action atoms. Part III specifies dice-level resolution: initiative, defense checks, the critical system, damage aggregation, condition track movement, weapon mechanics in combat, advanced reaction chains, worked multi-Scope scenarios testing the 1-tempo transition cost, Systemic Catalyst applications drawn from real historical events, pressure point engagement during active combat, and the Smoothing Effect as structural rather than mechanical limit.

---

# PART I: INITIATIVE AND PHRASE ORDER

## Tempo-Weighted Initiative

When a phrase begins, actors are ordered by tempo capacity.

**Initiative Value = Wits + Mastery**

This is the same formula that generates the tempo pool. The same attributes that let you process more OODA cycles per phrase also let you begin processing first. Initiative is not a separate stat.

## Tie Breaking

When multiple actors have identical Initiative Values:

1. Higher Wits acts first (processing speed)
2. Higher Mastery if Wits ties (trained efficiency)
3. Player choice if both tie

Most ties will resolve at step 1. Step 3 almost never comes up in play.

## The Phrase Structure

A phrase unfolds in rounds. Each round, actors take turns in initiative order. Each turn is one combat action consuming 1-3 tempo (Light/Standard/Heavy). The phrase continues until resolution conditions are met.

### Within a Round

1. Actor on highest initiative takes their turn
2. They declare one action (Light/Standard/Heavy)
3. They spend appropriate tempo from their pool and FP from the relevant pillar
4. Resolution (attack check, defense check, damage/effect, reactions)
5. Consequences applied
6. Next actor in initiative order takes their turn
7. Continue until all actors have had one turn

### Between Rounds

If any actor is still Engaged and has tempo remaining, a new round begins. Same initiative order. Each actor takes another turn.

### Phrase End

The phrase ends when:
- All actors have disengaged
- One side is eliminated or incapacitated
- An actor with no remaining tempo cannot continue (involuntary disengagement)
- Situation resolves (third party intervention, objective achieved)

At phrase end, aggregated damage totals trigger condition track checks, final consequences apply, and the encounter state updates.

## Tempo Across Rounds

A character's total tempo pool is Wits + Mastery. This budget is spent ACROSS THE PHRASE, not per round. A character with 9 tempo might spend 3 tempo in round 1 (one Heavy action), 2 tempo in round 2 (one Standard action), 3 tempo in round 3 (another Heavy action), with 1 tempo remaining for potential reactions' trigger responses.

Characters who burn their entire tempo pool in the first round are DONE for the phrase. They remain in the engagement but cannot act. This is not "stuck on defense" — it's operational exhaustion. They may still react if FP is available, but their OWN phrase is complete.

This creates a real tactical decision: commit your bandwidth early for burst output, or pace it across the phrase for sustained presence.

## Mid-Phrase Initiative Changes

Initiative order is fixed at phrase start. Events that would change initiative (Chronos effects, critical hits altering tempo pools) don't reshuffle the order — they modify how many actions each actor can take within their slot in the existing order.

**Exception:** A character who gains bonus tempo from another actor's critical failure uses it immediately on their next turn in the existing order. They don't jump in line.

---

# PART II: STATIC DEFENSE MECHANICS

## The Defense Formula

Defense is static. The attacker rolls; the target's defense provides a Target Number (TN).

**Attack Check = d20 + Attack Modifier + Mastery + Situational Modifiers**

**Defense TN = 10 + Pillar Defense Modifier + Mastery + Talent Bonuses + Protection Effects**

The attacker succeeds if their roll equals or exceeds the Defense TN.

## The 4×4 Defense Matrix

Each pillar has four defense axes. The attacker (or their effect) targets one specific axis. Different attack types naturally target different axes:

| Pillar | Evasion | Guard | Toughness | Vigor |
|---|---|---|---|---|
| Physical | Ranged attacks, AoE | Melee attacks, maneuvers | Blunt force, impact | Sustained stress, poison |
| Mental | Surprise mental attacks | Focused mental combat | Sustained mental pressure | Prolonged stress |
| Social | Public exposure, shock | Direct social challenge | Sustained social pressure | Long campaigns |
| Metaphysical | Sudden planar events | Direct metaphysical combat | Sustained planar stress | Prolonged exposure |

The effect determines which axis applies. Damage effects typically target the pillar's "hit" axis (Guard for melee, Evasion for ranged). Affliction effects target the axis matching their imposition method. Protection effects increase the appropriate axis based on the isotope and expression.

## Defense Currencies

When Protection effects apply to a target, they increase one or more of these five defense currencies (SRD v3):

- **Defense Bonus** — added to the target's defense TN
- **Soak** — flat damage reduction per hit
- **Energy Resistance** — specific resistance by isotope type
- **Threshold Bonus** — how much damage before track movement triggers
- **Barrier HP** — separate HP pool that absorbs damage before reaching the target

The attacker rolls vs. the Defense TN (which includes the Defense Bonus if any Protection is active). If the attack hits, damage is reduced by Soak and Energy Resistance before applying to HP. Threshold Bonus and Barrier HP affect aggregation and track movement.

## Reading the Roll

The attacker's check produces one of four outcomes based on the margin:

| Margin | Result |
|---|---|
| TN +10 or higher, OR natural 20 | Critical Success |
| TN to TN +9 | Hit |
| TN −1 to TN −9 | Miss |
| TN −10 or lower, OR natural 1 | Critical Failure |

See Part IV for critical mechanics.

## Persistent Additive

Attacks carrying the Persistent additive (+3 CP) force the target to defend twice, taking the worse result. This effectively lowers the Defense TN by approximately 3-4 in expected value. Persistent effects feel "sticky" because they give the attack two chances to find purchase.

## Alternate Resistance Additive

Attacks carrying the Alternate Resistance additive (+2 CP) target a different pillar's defense than the effect would normally engage. A Damage effect with Alternate Resistance might target Social pillar defense instead of Physical — a "devastating public accusation" that deals Physical damage through humiliation rather than direct force.

---

# PART III: THE CRITICAL SYSTEM

## The Five Outcome States (Adapted)

Combat attack resolution uses four outcome states adapted from the crafting system's Five Outcome States:

| Attack Result | Outcome |
|---|---|
| Attack vs Defense **+10 or higher, OR natural 20** | **Critical Success** |
| Attack vs Defense **+0 to +9** | **Hit** |
| Attack vs Defense **−1 to −9** | **Miss** |
| Attack vs Defense **−10 or lower, OR natural 1** | **Critical Failure** |

The "Success with Flaw" middle state from crafting does not translate to combat — binary hit/miss keeps combat fast.

## Critical Success

**Effects:**
- Normal damage applies (not doubled)
- The attacker's weapon/spell/effect applies its predetermined critical expression
- The attacker receives 1 FP refund into the active pool (the pillar they drew from for this action)

**The Critical Expression:**

Every weapon, spell, or effect has a predetermined critical expression defined at creation or composition. Examples from the SRD v3:

- **B-11 Acid** — bypasses Soak on critical hit
- **B-14 Current** — chains to the nearest conductor within range on critical hit
- **Keen property** (Ascension trait) — extends critical threat range by 2 (the TN margin for critical success becomes TN +8)

For weapons or spells without a documented critical expression, the GM assigns one on the spot using the isotope's Natural Effects list as a menu. This becomes canon for that item/expression going forward. The system fills its own gaps through play.

**Design guidance for critical expressions:**

Critical expressions should be flavor-forward and moderate in mechanical weight. They are a touchpoint that makes each weapon and spell feel distinct, not a damage multiplier. Good examples:

- **Bedrock hammer:** impact point becomes difficult terrain for 1 round
- **Still Verse blade:** target's next tempo action takes a penalty
- **Inferno-channeled firearm:** target takes ongoing minor fire damage
- **Mind Link attack (critical):** attacker briefly glimpses a memory of the target
- **Senses (critical scan):** reveals one piece of hidden information about the target beyond what was sought

## Critical Success — The Palimpsest Framing

Critical successes are moments of probability collapse. The Palimpsest's fabric briefly aligns with the attacker's intent. This is why the FP refund exists — the Palimpsest rewards the active channel. It's also why the critical expression emerges naturally from the isotope in play — the collapse makes the isotope's character MORE expressed, not less.

This is mechanically and thematically distinct from the Smoothing Effect. The Smoothing Effect dampens reality's tendency toward dramatic change. Critical successes are probability collapse IN FAVOR OF expression. They are not exceptions to Smoothing — they are moments when Smoothing is not operating (personal-scale actions don't trigger Smoothing).

## Hit (Normal)

Full normal damage/effect applies. No additional consequences beyond what the base action specifies.

## Miss

No damage or effect. The attacker's FP and tempo are spent. This is the default failure state — the attack didn't land.

## Critical Failure

**Effects:**
- No damage or effect
- The attacker's FP and tempo are spent
- Every actor currently "already engaged" with the critically failing attacker gains 1 bonus tempo this phrase

**Definition of "Already Engaged":**

An actor is "already engaged" with the critically failing attacker if ALL three conditions are met:

1. **Active targeting window:** The actor attacked or intentionally targeted the critically failing attacker at any point since the end of the failing attacker's previous phrase.

2. **No disengagement:** The actor has not disengaged from the failing attacker (paid the 2-tempo disengagement cost) between that targeting action and the current critical failure.

3. **No redirection:** The actor has not redirected their target to a different opponent since their last action against the failing attacker.

**Included:**
- Actors who attacked the failing attacker this phrase or in response to their previous phrase's actions
- Actors who parried, dodged, counter-spelled, or otherwise reactively engaged with the failing attacker (reactive engagement IS engagement)
- Actors who failed attacks against the failing attacker (attempted engagement still counts)

**Excluded:**
- Actors engaged with DIFFERENT opponents, even if positioned nearby
- Actors who broke contact or disengaged
- Actors who redirected to a new target after engaging
- Third parties observing but not participating
- Actors who haven't yet acted this phrase (they may act later, but aren't engaged until they commit)

**The bonus tempo:**

The bonus tempo is added to the engaged actor's pool for this phrase only. It does not carry over. It must be spent on their next turn in initiative order — they don't jump in line, but their next action has a "free ride" on this extra tempo.

This can be used to:
- Take a Light action as a free addition to their planned turn
- Reduce a Standard action's cost to 1 tempo
- Reduce a Heavy action's cost to 2 tempo
- Bank the bonus against a reaction trigger later in the phrase

## Critical Failure — The Palimpsest Framing

Where critical successes are probability collapsing IN FAVOR of expression, critical failures are probability collapsing AGAINST the actor. The disturbance ripples through the local probability space — which IS the space of actors already committed to the exchange. Everyone present to see and exploit the opening gets a moment of clarity.

This matches real tactical history. When a combatant overextends or exposes themselves in a multi-actor engagement, everyone committed to the exchange capitalizes — not just one person. The pike block that runs down an overextended opponent, the trench-raid ambushers whose combined fire punishes a single exposed raider, the dogfight pack that all turns on the pilot who breaks formation. The engagement itself IS the probability space where the failure expresses.

---

# PART IV: DAMAGE APPLICATION AND CONDITION TRACKS

## Aggregated Damage

Damage within a phrase aggregates per target. All damage from all sources hitting the same target during the phrase accumulates into one total. At phrase end, this aggregate is processed against thresholds.

**During the phrase:**
- Damage applies to HP immediately (the target's HP pool for the pillar damaged drops)
- Damage is tracked per pillar (Physical damage to Vitality, Mental to Resolve, Social to Poise, Metaphysical to Pattern)
- Protection effects reduce individual hits at the moment of impact (Soak, Energy Resistance)

**At phrase end:**
- Total aggregated damage per pillar is compared to the target's threshold
- Condition track movement is calculated based on threshold crossings
- Discrete conditions from Afflictions apply separately

## The Three-Layer Damage System (SRD v3)

**Layer 1: HP Pools (Four Pillars).** Damage reduces. Healing restores. The baseline buffer.

**Layer 2: Condition Tracks (Four Pillars, 5 Steps Each).** Threshold-exceeding damage or Affliction effects move tracks downward. Tracks represent accumulated stress states, not discrete injuries.

**Layer 3: Discrete Conditions.** Binary on/off states imposed by Affliction effects or specific situations. Independent of tracks.

## Threshold Mechanics

The damage threshold for track movement is a derived statistic. A character's threshold for each pillar is:

**Threshold = (Primary Attribute for that Pillar × 2) + Mastery + Threshold Bonus (from Protection effects)**

If aggregated damage in a phrase exceeds the target's threshold, the condition track moves one step downward. If aggregated damage exceeds 2× threshold, it moves two steps. 3× threshold = three steps. And so on.

**Example:** A character with Vigor 4 and Mastery 5 has a Physical threshold of (4 × 2) + 5 = 13. If they take 20 aggregated Physical damage in a phrase, their Physical condition track moves 1 step (20 exceeds 13 but not 26). If they take 30 damage, it moves 2 steps (30 exceeds 26).

## Condition Track States

Each pillar's condition track has 5 steps:

| Step | State | Mechanical Effect |
|---|---|---|
| 0 | Normal | No penalty |
| -1 | Shaken | Minor penalty to actions in the affected pillar |
| -2 | Impaired | Moderate penalty, reduced capability |
| -3 | Crippled | Major penalty, severely limited capability |
| -4 | Incapacitated | Cannot act in the affected pillar |
| -5 | Terminal | Pillar-specific catastrophic state |

The terminal state is pillar-specific:
- **Physical Terminal:** Dying (soul cycle engages)
- **Mental Terminal:** Broken (persistent mental break, requires specialized treatment)
- **Social Terminal:** Disgraced (reputation fully collapsed, institutional ejection)
- **Metaphysical Terminal:** Unmade (soul pattern dissolving, Synod intervention required)

## Aggregation Examples

**Example 1 — Single combatant scenario:**

Bob attacks Alice three times in a phrase. Alice has Physical threshold 15.
- Hit 1: 6 damage
- Hit 2: 4 damage
- Hit 3: 8 damage
- Total: 18 damage

At phrase end, Alice's 18 damage exceeds her 15 threshold by 3. Condition track moves 1 step (18 > 15 but not 30). If the hits were spread across two phrases, each individual hit would need to exceed threshold alone. Aggregation matters because it lets lots of small hits add up to track damage.

**Example 2 — Multiple attackers scenario:**

Three attackers each hit Alice twice during the phrase for 4 damage each (6 total hits, 24 damage aggregated). Alice's threshold is 15. Aggregate damage is 24, exceeding threshold by 9. Track moves 1 step (24 > 15 but not 30).

Against six attackers each doing the same (12 hits, 48 damage), Alice's track moves 2 steps (48 > 30 but not 45).

## Affliction and Track Movement

Affliction effects can directly impose track movement (SRD v3 Amendment 7F):

| Track Steps Imposed | Affliction BER |
|---|---|
| 1 step | 2 |
| 2 steps | 3 |
| 3 steps | 4 |
| 4 steps | 5 |

Affliction track movement applies immediately on successful imposition, not at phrase end. It stacks with aggregated damage threshold movement — if Alice fails a save against a BER 3 Affliction moving her track 2 steps, then takes 20 damage during the phrase (1 more step from threshold), her total track movement is 3 steps.

## Recovery

Condition tracks recover during downtime. The recovery rate depends on the track state:

- **Shaken (-1):** Recovers at S2 rate (×1 drip, 10 minutes of rest)
- **Impaired (-2):** Recovers at S3 rate (tens of minutes to hours of rest)
- **Crippled (-3):** Recovers at S4-S5 rate (hours to days), often requires specific treatment
- **Incapacitated (-4):** Recovers at S5 rate (days), typically requires medical or magical intervention
- **Terminal (-5):** Requires exceptional circumstances — specific narrative resolution, Panacea effect at high ESL, institutional/divine intervention

The recovery rate is the pillar's natural resilience. Calm environments double the rate. Active treatment (Healing effects, medical care, specific recovery techniques) accelerates it further.

Lasting damage persists even after full HP restoration — healing restores the pool, but tracks recover on their own timeline. A character with full HP and a -2 Impaired Physical track is functional but carrying residual damage.

---

# PART V: WEAPON AND ITEM MECHANICS IN COMBAT

## The Four-Layer Item Model in Action (SRD v3)

Every item in combat has up to four active layers contributing to its output:

**Layer 1: Base Material.** Physical properties (Hardness, Tensile Strength, Density, Conductivity, Elasticity) feed spell sentence parameters. The material's isotope identity determines Feature effects and natural riders.

**Layer 2: Expressions (Mutations/Enchantments).** Internal rotes the item carries. Activate through drip recharge. Count toward EML.

**Layer 3: Attachments.** Sub-items with their own rotes, installed in slots. Portable. Contribute their material properties to routed spells.

**Layer 4: Insets.** Spell sentence modifiers in slots. Don't carry their own rotes. Modify anything routed through them.

## Damage Die Size from Material

The weapon's damage die size is determined by its material's Tensile Strength on the 1-10 scale:

| Tensile Strength | Damage Die |
|---|---|
| 1-2 | d4 (floor — cloth, soft wood) |
| 3-4 | d6 (standard — hardwood, low-grade metal) |
| 5-6 | d8 (ceiling — quality steel, bronze) |
| 7-8 | d10 (specialized — master steel, advanced alloys) |
| 9-10 | d12 (legendary — mythic materials, isotope-infused metals) |

This is the die the attacker rolls on a hit. ESL determines how many dice (from the SRD v3 Damage scaling table: 1d6 at ESL 1, 18d6 at ESL 10 for a d6-band weapon).

## Attack Bonus from Item

The weapon or implement provides an attack bonus based on its quality and the wielder's mastery. Standard mundane weapons: +0 base. Masterwork: +1. Each Formation Stage band in the item's material adds further bonuses.

Weapons that are Expressed (have internal rotes or enchantments) contribute their EML to attack bonus when channeling through them. A Tier 6 staff with EML 5 contributes +5 to channeled spell attack rolls.

## Wielding Styles and Combat Petal Talents

The 18 Ætherforged Precepts (Part I of this document) organize combat style talents into coherent philosophies. Each Precept's associated Crux talents and supporting talent trees determine what actions a character has access to and at what tempo cost.

A character with Finesse Style trained to Master level executes Parry-Riposte as a Light action (1 tempo, 1 FP) because their training compressed what would otherwise be two separate actions into one. An untrained character parrying and riposting pays the full 2 tempo / 3 FP for each action separately.

Training reduces tempo costs. Isotope channeling adds effect riders. Spell Sentence construction adds full effects. The three tiers of expression (Trained → Directed → Full) stack when used together.

## Item Drip Recharge in Combat

Items generate their own charges through drip recharge (SRD v3 Part XIV). A weapon with a 1-charge-per-interval rate can use its expression once every 10 minutes of play. During active combat (stressful conditions, ×1 rate), this means about once per encounter.

Items with multiple charges banked can expend them rapidly, then recharge during downtime. The charge pool is the item's "fuel" analog to the character's FP pool.

## Critical Expressions by Item

Each Expressed item has a predetermined critical expression. For mundane weapons, the critical expression is determined by the material's dominant isotope — a steel sword without explicit enchantment still uses its Hidden Forge material character on critical. For Expressed weapons, the critical expression can be specified at creation.

Masterwork items frequently include signature properties like Keen (extends critical threat range by 2). An item with Keen critically hits on attack vs Defense +8 or higher instead of +10, dramatically increasing the frequency of critical expressions.

---

# PART VI: ADVANCED REACTION CHAINS

## Reactions as Triggers

Part II established that reactions are FP-fueled responses to specific triggers. A reaction IS a combat action — which means it can itself trigger further reactions.

**The chain principle:** Every combat action is a potential trigger. Reactions are combat actions. Reactions to reactions are possible.

## A Simple Chain

**Setup:** Alice attacks Bob with a Damage effect.

1. **Alice's attack** (the initial trigger)
2. **Bob reacts** with a Parry (Protection effect, reactive — paying Physical FP)
3. **The Parry succeeds** — Alice's attack is redirected
4. **Alice may now react** to the redirection (if she has FP available) — she might spend Physical FP on a Movement action to reposition, avoiding the redirect's consequences

Three actions from one initiating trigger. Each uses FP. None uses tempo (all are reactive). The chain ends when no further triggers are generated or actors decline to react.

## Nullify Chains — The Exothermic Cascade

Nullify at ESL 5+ produces collateral burst damage (SRD v3 Amendment 8F). This collateral is itself a trigger.

**Scenario:** Alice casts a Fireball (Damage ESL 5) at Bob. Charlie (Bob's ally, adjacent) attempts to Nullify.

1. **Alice's Fireball** — ESL 5 Damage, 15-foot radius
2. **Charlie reacts with Nullify ESL 5** — targeting Alice's Fireball
3. **Nullify succeeds** — the Fireball is neutralized
4. **Exothermic burst** — Nullify ESL 5 produces 2d6 collateral damage in a 15-foot radius
5. **The burst hits Alice, Bob, Charlie, and anyone else in the zone**
6. **Each target of the burst may react** — Alice might use Protection, Bob and Charlie might attempt their own defensive reactions

Every actor in the burst zone is a potential chain continuer. If any of them use a reaction that itself produces a trigger, the chain extends further.

## Chain Termination Conditions

Chains end when:
- No new triggers are generated (all reactions resolve cleanly)
- Actors decline to react (by choice or FP exhaustion)
- The reactions themselves are low enough ESL to produce no cascading triggers
- FP pools across all participants are depleted below viable reaction cost

## Chain Tempo Accounting

Reactions don't consume tempo from anyone's phrase budget. A single attack producing a five-reaction chain still only consumes the attacker's original tempo (the Heavy action that started it).

**Exception:** If a reaction's target "redirects" the consequences (such as a Deflect additive rerouting damage to a different target), the redirect uses the reactor's FP but does not create a new tempo event — it's still inside the reaction framework.

## Managing Chains at the Table

For table-level pragmatism: chains rarely exceed 3-4 links in practice because FP pools and reasonable judgment stop them. The GM should call the chain's end when it stops producing meaningful new consequences. Complex chains involving 5+ links should be narrated through rather than mechanically resolved step-by-step — the GM describes the overall cascade and applies aggregated consequences.

This matches how real combat cascades work. A firefight has complex interlocking reactions, but participants don't resolve each nanosecond of decision. The exchange produces an overall outcome.

---

# PART VII: COMPLEX MULTI-SCOPE SCENARIOS

## The 1-Tempo Transition Cost in Practice

Part II established that splitting attention across Scopes costs 1 tempo per Scope transition within a phrase. Part III tests this through worked scenarios. Whether this cost feels right becomes clear when we see it applied.

## Scenario 1: The Field Officer Under Attack

**Setup:** Captain Vesren is commanding a squad (S1 operations, ongoing) when his command post is directly attacked (S0 combat beginning). He is Engaged at both Scopes simultaneously.

**Stats:** Vesren has Wits 4 + Mastery 6 = 10 tempo at every Scope.

**Phrase 1 — Attack begins:**

- **S0 activation:** Vesren pays 1 tempo to activate S0 combat (entering Engaged state at S0 from Threatened)
- **S0 action:** Vesren draws his sidearm and fires at the attacker (Standard action, 2 tempo, 3 Physical FP)
- **Transition cost:** Vesren shifts attention to S1 command (1 tempo)
- **S1 action:** Vesren shouts an order to his squad to reposition (Light action, 1 tempo, 1 Social FP)
- **Transition cost:** Vesren shifts attention back to S0 (1 tempo)
- **S0 reaction trigger:** Vesren may react to the attacker's next strike

**Tempo accounting for phrase:** 1 (S0 activation) + 2 (fire) + 1 (transition) + 1 (command) + 1 (transition) = 6 tempo spent on 2 combat actions + 1 command action. Vesren has 4 tempo remaining.

**Analysis:** The transition cost is real and meaningful. Vesren spent 2 tempos on transitions alone — the equivalent of a Standard action's worth of bandwidth. If the transition cost were free, he could have spent that bandwidth on more actions. The mechanic creates pressure to commit fully at one Scope when possible.

**Playability test:** Is 2 tempo on transitions a reasonable price for splitting attention across Scopes in a high-stakes moment? The officer pays a 20% bandwidth tax on their 10-tempo pool. This feels right for the narrative weight — a field officer under direct attack CAN continue commanding, but their command effectiveness degrades.

## Scenario 2: The Stormpeak Phalanx in Action

**Setup:** Legionary Kalin is part of a shield wall (Way of the Phalanx, Overt) during a battlefield engagement. She's Engaged at S0 (personal combat with the enemy in front of her), Engaged at S1 (her fireteam's cohesion), and Engaged at S2 (the broader shield wall's formation).

**Stats:** Kalin has Wits 3 + Mastery 5 = 8 tempo.

**The Way of the Phalanx mechanically:**

Phalanx training reduces S0 tempo expenditure. Shield wall defensive posture is a 0-tempo reactive stance once established. Kalin's defensive reactions cost only FP, not tempo. Her S0 tempo is freed for offensive actions only — making her look "inactive" but actually deeply engaged.

**Phrase 1:**

- **S0 action:** Kalin thrusts her spear at the enemy opposite her (Standard action, 2 tempo, 3 Physical FP)
- **Transition cost:** Kalin shifts to S1 (1 tempo)
- **S1 action:** Kalin maintains the shield link with her fireteammates (passive, 0 tempo — trained reflex)
- **Transition cost:** Kalin shifts to S2 (1 tempo)
- **S2 awareness check:** Kalin reads the overall shield wall's state (passive, 0 tempo — Phalanx training)
- **Transition cost:** Kalin shifts back to S0 (1 tempo)
- **S0 reaction:** Enemy attacks — Kalin's Phalanx reactive defense triggers (0 tempo, 3 Physical FP)

**Tempo accounting for phrase:** 2 (thrust) + 1 (S0→S1) + 0 (team link) + 1 (S1→S2) + 0 (wall read) + 1 (S2→S0) + 0 (defense) = 5 tempo spent on one offensive action while monitoring three Scopes and maintaining defensive posture.

**Analysis:** Phalanx training front-loads its investment — Kalin spent talent investment on making S0 defense and S1-S2 passive monitoring 0-tempo. Her transitions still cost tempo, but her individual actions at each Scope are cheaper. Net effect: she maintains broad awareness at modest bandwidth cost.

**Playability test:** The Phalanx design philosophy from Part I (minimize S0 tempo expenditure to preserve bandwidth for higher Scopes) is mechanically expressed through talent investments that zero-out specific tempo costs. This matches the thematic intent.

## Scenario 3: The Chronos-Enhanced Duelist

**Setup:** Mistress Akare of the Chronosynclastic Institute is in a duel. She has ESL 5 Chronos active on herself (extra standard action per round — SRD v3 scaling table). She's Engaged at S0.

**Stats:** Akare has Wits 5 + Mastery 8 = 13 tempo at S0.

**Chronos modification:** ESL 5 Chronos grants an extra standard action per round. Mechanically, this is 2 additional tempo per round for Standard actions specifically (not applicable to Heavy actions that consume the standard action slot).

**Phrase 1:**

- **Round 1:**
  - Akare's turn: Standard attack (2 tempo, 3 Physical FP) + Chronos-granted extra Standard action (2 tempo from Chronos pool, 3 Physical FP)
  - Total for round: 4 tempo (2 own + 2 Chronos), 6 Physical FP, 2 actions

- **Round 2:**
  - Akare's turn: Heavy action (3 tempo, 5 Physical FP) — no Chronos benefit on Heavy actions
  - Total for round: 3 tempo, 5 Physical FP, 1 action

- **Round 3:**
  - Akare's turn: Two Light actions (2 tempo, 2 Physical FP) + Chronos Standard (2 tempo from Chronos, 3 Physical FP)
  - Total for round: 2 tempo + 2 Chronos, 5 Physical FP, 3 actions

**Tempo accounting across phrase:** Own tempo spent: 4+3+2 = 9 of 13. Chronos-granted tempo used: 2+0+2 = 4. Total actions: 2+1+3 = 6. A non-Chronos duelist with the same 13 tempo might have executed 4 actions. Akare's Chronos buys 50% more actions per phrase.

**Analysis:** Chronos at ESL 5 is genuinely game-changing. The extra-action-per-round mechanic effectively gives Akare a parallel tempo budget specifically for Standard actions. She can maintain aggressive offense while non-Chronos opponents rotate through their full budgets more carefully.

**Playability test:** Is this too powerful? Consider: Akare is spending ÆP to maintain Chronos on herself (ESL 5 Chronos costs 9 ÆP per casting, likely Hours duration at CP investment). She's dedicated significant FP budget to BEING enhanced, which means less FP for her actual offensive spellcasting. The power curve balances through resource commitment.

## The 1-Tempo Transition Verdict

Based on these worked scenarios, the 1-tempo transition cost produces the intended effect:

- Characters CAN operate at multiple Scopes simultaneously
- The cost is noticeable (10-30% bandwidth tax depending on how many transitions)
- Training (Phalanx-style talents) can reduce individual-Scope action costs but NOT transition costs
- Heavy transition expenditure becomes a real decision point

**Recommendation:** Keep the 1-tempo transition cost as specified. It produces meaningful tactical decisions without being oppressive.

---

# PART VIII: SYSTEMIC CATALYST WORKED EXAMPLES

## Method

Each example uses a real historical incident stripped of names, specific factions, and date-identifiers. The historical event provides the mechanical shape — who targeted what, what the cascade looked like, what the consequences were. The narrative details are replaced with Tessera setting elements so the pattern remains playable without being a reconstruction of the actual event.

## Local Scale (×2) — The Enclosed Hazard

**Historical source:** A type of engagement common in confined-space combat throughout modern warfare. Gas and chemical incidents in closed rooms, storage facilities, mineshafts.

**Scenario:** The party has cornered three enemies in a small stone chamber with a central brazier. One party member has Knowledge of Borderlands Fire isotopes and identifies the brazier as a Local-scale leverage point (the heating element in a closed room).

**Action:** A party member applies a Damage effect (Isotope: B-01 Inferno, ESL 2) targeting the brazier with Systemic Catalyst invoked.

**Mechanical resolution:**
- Base Damage ESL 2 at Individual target
- Systemic Catalyst ×2 multiplier (Local scale)
- Effective reach: 2× normal area, covering the entire chamber rather than a single target
- Precision lost proportionally: cannot exclude allies from the effect

**Outcome:** The brazier erupts. All three enemies take the Damage effect at ESL 2 (Competing interaction for two of them, Cancellation ×1.5 for the one with partial Fire resistance). One party member adjacent to the brazier also takes damage — the imprecision of the Catalyst caught them.

**Why this works mechanically:** A single ESL 2 action (3 Metaphysical FP) produced an area effect that would normally require ESL 4 geometry (Burst Small) with Dialect-tier access. The party punched above their weight class by identifying the correct leverage point, but paid the cost in imprecision.

## Site Scale (×5) — The Structural Key

**Historical source:** Urban warfare demolitions throughout the 20th century. Building collapse through targeted structural failure at load-bearing points.

**Scenario:** An enemy stronghold is built into a cliff, with a carved supporting pillar at its center. The party's Knowledge-petal specialist identifies the pillar as a Site-scale leverage point (structural keystone).

**Action:** A party member applies a Damage effect (Isotope: B-11 Acid, ESL 3) targeting the supporting pillar with Systemic Catalyst.

**Mechanical resolution:**
- Base Damage ESL 3 at Individual target (the pillar)
- Systemic Catalyst ×5 multiplier (Site scale — building keystone)
- Effective reach: structural failure propagates through the entire building
- Precision lost: ×5 means "mostly uncontrollable" — the collapse direction cannot be precisely aimed

**Outcome:** The pillar dissolves under acid damage. The building collapses along natural structural lines. Everyone inside (enemies and any captives) must make Physical Evasion checks to escape the rubble. Party members outside the building are safe; party members inside are caught in the cascade.

**Why this works mechanically:** A personal-scale attack produced a Site-scale consequence. The mechanical cost was 5 Metaphysical FP (ESL 3) plus the talent investment in Systemic Catalyst. The narrative cost was loss of precision — the party destroyed the stronghold but also anything valuable inside it.

## Block Scale (×10) — The Utility Node

**Historical source:** The Boston Molasses Flood of 1919. A single containment tank ruptured, flooding 15 blocks of the North End with molasses. 21 dead, 150 injured, buildings crushed. The failure of a single infrastructure node cascaded to district-level consequence.

**Scenario:** A Forge-manufactured water main runs under the enemy faction's fortified neighborhood. The party identifies the main's pressure regulator as a Block-scale leverage point (utility node affecting street-level consequence).

**Action:** A party member applies a Nullify effect (targeting the regulator's pressure-containment enchantment, ESL 4) with Systemic Catalyst.

**Mechanical resolution:**
- Base Nullify ESL 4 at Individual target
- Systemic Catalyst ×10 multiplier (Block scale — utility node)
- Effective reach: the street-level water main fails across 10 city blocks
- Exothermic burst from Nullify ESL 4 triggers additionally: significant area energy release as the containment fails
- Precision lost: cannot control which blocks flood first or which structures are most affected

**Outcome:** The regulator's pressure containment fails. Water pressure cascades through the main, rupturing at weak points across ten blocks. The enemy faction's fortified neighborhood floods. Streets are impassable. Basements fill. The faction's operations are paralyzed — not by direct damage, but by infrastructure collapse. Civilian collateral is extensive.

**Why this works mechanically:** A single ESL 4 action neutralized a piece of enchanted infrastructure, producing Block-scale consequence through engineering failure cascade. The party achieved strategic disruption without direct military engagement. The ethical weight of civilian collateral is real and should be part of the consequences.

## District Scale (×25) — The Communication Hub

**Historical source:** The Northeast Blackout of November 9, 1965. A single relay at the Adam Beck Station (Ontario) failed, cascading through the interconnected grid and blacking out 80,000 square miles and 30 million people across 8 states and 2 provinces. One faulty relay. One switch.

**Scenario:** The dominant faction's information network runs through a Forge-constructed relay station at a tributary junction. The party identifies the relay as a District-scale leverage point (tributary junction for power/information grid).

**Action:** A party member applies a Damage effect (Isotope: B-14 Current, ESL 4) targeting the relay's resonance core with Systemic Catalyst.

**Mechanical resolution:**
- Base Damage ESL 4 at Individual target
- Systemic Catalyst ×25 multiplier (District scale — grid node)
- Effective reach: cascading failure propagates through the interconnected infrastructure
- Precision lost: the cascade affects everything connected to the grid, not just the target faction

**Outcome:** The relay core overloads. Current propagates through the interconnected infrastructure faster than the network's safety systems can contain. Forge-powered devices across the district fail. Communication networks collapse. Transportation nodes lose power. Markets close. The faction's information advantage is neutralized — but so is everyone else's. The district falls into operational darkness for days or weeks until the grid can be repaired.

**Why this works mechanically:** A single ESL 4 action produced district-wide consequence. The party achieved what would normally require institutional-scale operations. The cost: massive civilian impact, loss of general-purpose infrastructure, and political consequences from the cascade reaching non-target parties. Getting away with this requires either anonymity or institutional backing.

## Regional Scale (×100) — The Pressure Gradient

**Historical source:** The Huayuankou Dike Breach of June 1938. Chinese nationalist forces deliberately breached the Yellow River dike to slow Japanese military advance. The flood killed hundreds of thousands of civilians, displaced millions, and altered the river's course. The military delay was measured in weeks; the regional consequence persisted for a decade.

**Scenario:** The enemy's supply route runs along a river valley downstream of a Forge-constructed dam holding a reservoir. The party identifies the dam as a Regional-scale leverage point (pressure gradient, aquifer source).

**Action:** A party member applies a Damage effect (Isotope: B-05 The Abyss, ESL 5) targeting a critical stress point in the dam with Systemic Catalyst.

**Mechanical resolution:**
- Base Damage ESL 5 at Individual target
- Systemic Catalyst ×100 multiplier (Regional scale — pressure gradient)
- Effective reach: catastrophic water release floods the entire valley downstream
- Precision lost: "act of god pointed in a direction" — the flood's path cannot be controlled once initiated
- Exothermic burst from damage to an Expressed structure

**Outcome:** The dam fails. The reservoir empties in hours, producing a flood wave that travels the length of the valley. The enemy's supply route is destroyed. The enemy's forces in the valley are killed or scattered. And every civilian settlement in the valley is destroyed. Thousands to tens of thousands of non-combatants dead. The geography of the region permanently altered.

**The party has won the military objective and committed a war crime in the same action.**

**Why this works mechanically:** A single ESL 5 action produced regional-scale consequence. The mechanical power is appropriate. The ethical weight is appropriate. This is exactly what Systemic Catalyst at Regional scale should feel like — strategic victory at unconscionable cost, or desperate last resort by a faction that has no better options.

## Territorial Scale (×500) — The Ecosystem Breach

**Historical source:** Operation Popeye (1967-1972). The US military used cloud-seeding to extend the monsoon season over the Ho Chi Minh Trail, attempting to degrade enemy supply lines. The operation ran for five years before being exposed. It produced measurable weather modification at regional-to-territorial scale. The political consequences contributed to the 1976 Environmental Modification Convention banning weather warfare.

**Scenario:** The enemy's entire civilization depends on a specific weather pattern — a jet stream that brings monsoon rains to their agricultural regions. A party member with extraordinary Palimpsest isotope knowledge and Systemic Catalyst at maximum scale identifies the jet stream boundary as a Territorial-scale leverage point.

**Action:** The party member applies a sustained Transform effect (Isotope: B-13 The Void Sky, ESL 7) to the jet stream's boundary condition with Systemic Catalyst over a campaign-length operation.

**Mechanical resolution:**
- Base Transform ESL 7 at Individual target
- Systemic Catalyst ×500 multiplier (Territorial scale — jet stream boundary)
- Effective reach: continent-scale weather modification
- Precision lost: ×500 is "act of god pointed in a direction" — consequences are unpredictable in detail even if predictable in general shape
- Sustained operation: not a single action but a campaign of repeated Systemic Catalyst applications over seasons or years

**Outcome:** The jet stream's path shifts. The enemy's monsoon fails. Their agriculture collapses. Their civilization enters famine. Refugees flood across territorial borders. The diplomatic backlash implicates every institution suspected of capability. The ecological consequences include species displacement and soil destabilization that persists for generations.

**The party has unmade a civilization through weather warfare. The party is now among the most wanted entities in the setting.**

**Why this works mechanically:** Territorial-scale Systemic Catalyst is the most extreme power individual characters can access. The mechanical path is real but narrow — it requires sustained investment, exceptional knowledge, and access to specific leverage points that institutions jealously guard. The consequences are civilizational and irreversible on mortal timescales.

**Campaign implication:** When a party considers Territorial-scale Systemic Catalyst, the GM should treat this as the kind of act that ends campaigns. Not because it's forbidden, but because the aftermath BECOMES the campaign. Any party willing to reach this scale should understand they are becoming the threat that other parties will be sent to stop.

## Systemic Catalyst Design Principle

The escalation through scales produces a clear design principle: **mechanical power at Systemic Catalyst scale comes with proportionally increasing narrative consequence.** Local scale is a tactical option. Territorial scale is a civilizational event. The system doesn't prevent players from escalating — it ensures they understand what they're doing when they do.

This matches historical reality. Powerful people have committed atrocities by identifying and acting against leverage points throughout history. The mechanical framework doesn't enable players to do what was historically impossible. It enables players to engage with what has always been possible and make the choice knowing the cost.

---

# PART IX: PRESSURE POINT ENGAGEMENT MID-COMBAT

## The Free Action Rule

Engaging with a Schema pressure point during active combat is a free action — it costs neither tempo nor FP directly. However, engagement can only happen ONCE per trigger event.

**The trigger event** is a narrative moment that invokes the character's pressure point. Examples:

- A Conviction-axis character faces a situation that tests their core belief
- A Courage-axis character encounters their specific fear
- A Physical-heritage character experiences a crisis that activates their adaptation
- A Social-heritage character encounters exposure (Goffman Gap revealed)

When the GM signals that a trigger has occurred (narration, direct description, situational pressure), the character may choose to engage. If they engage, they recover FP into the pillar most aligned with the engagement. The exact amount is determined by Schema pressure point severity (outlier/split/break) — typically 2-5 FP.

## Deliberate Targeting of Pressure Points

Opponents can deliberately target a character's pressure points as a form of Mental pillar attack. This is the mechanical basis for the Intimidation Style, demoralization tactics, and psychological warfare in general.

**The pressure point attack:**

- Attacker spends Mental FP to attempt a pressure point attack (ESL 2-5 typically)
- Attacker must have knowledge of the target's pressure point (requires Senses effect at ESL 3+ or narrative reveal)
- Attack vs target's Mental pillar defense (Willpower for Intrusion attacks, Control for Overwhelm, Conviction for Erosion, Courage for Dread)
- On hit: target takes Mental damage AND must choose whether to engage their pressure point
- On engagement: target recovers FP as normal (Mental attack actually refilled them in part)
- On refusal to engage: target takes additional Mental track movement from the unreleased pressure

**This creates the meaningful Intimidation dynamic:** the attacker is trying to force the target into a trauma response. Engagement releases the pressure (the target recovers FP but also acknowledges the wound). Refusal prevents the release but compounds the damage.

The Adamant Heart Way (Unity Academy, Overt) specifically trains practitioners in this tactic. Identifying and attacking pressure points produces reliable Mental damage while testing the target's fundamental identity stability.

## GM Signaling

For the system to work at the table, the GM must signal when a trigger has occurred. This can be:

- **Explicit:** "This situation tests your Conviction pressure point — do you engage?"
- **Narrative:** Describing the scene in a way that invokes the trigger, trusting the player to recognize and choose
- **Prompted:** After an ambiguous moment, the GM asks "Does this connect to your character's pressure point?"

Players should be encouraged to engage pressure points actively. The mechanical reward (FP recovery) is the incentive. The narrative reward (the character is the kind of person who grows through their tensions) is the payoff.

## Pressure Point Attacks in the Critical System

If a pressure point attack rolls a critical success, the target's pressure point is not just targeted — it's EXPOSED. Other observers in the scene now know the target's weakness. This creates long-term consequences beyond the immediate Mental damage: the target is now vulnerable to follow-up attacks from anyone who witnessed the exposure.

If a pressure point attack rolls a critical failure, the attacker's own pressure points may come into play. The failed attack backfires — the attacker's projection reveals as much as the attempted attack would have. The GM may invoke the attacker's pressure point in response.

---

# PART X: THE SMOOTHING EFFECT AS STRUCTURAL LIMIT

## Not a Dice Modifier

The Smoothing Effect (from the Operating Philosophy and referenced throughout the SRD v3) does NOT manifest as a dice penalty, TN increase, or damage reduction. It is not mechanical at the roll level.

The Smoothing Effect is STRUCTURAL. It manifests as:

1. **CP access tier enforcement** (SRD v3 Amendment 6): Encounter-scale geometry (CP 0-3) is Common. Battlefield-scale (CP 4-6) is Dialect — must be learned through play. Geographic-scale (CP 7-10) is Treasure — must be acquired through exceptional circumstances.

2. **Institutional pooling requirements** for high-Scope operations: Individual characters cannot reach Scope 5+ through personal ESL alone. They need either institutional FP pooling or Systemic Catalyst with exceptional leverage.

3. **Nested clock architecture**: Higher-Scope clocks must be filled through accumulated lower-Scope ticks. Characters cannot skip Scope levels — the Smoothing Effect requires each clock be filled in sequence.

4. **The 10-tempo pool ceiling at starting play**: The initial Wits + Mastery total is naturally bounded. Mastery growth is gated through training milestones. The Smoothing Effect ensures that reaching peak capability requires sustained investment.

## What Smoothing Does NOT Prevent

Smoothing is not a prohibition. Characters can and do exceed normal operational parameters through specific mechanical paths:

- **Systemic Catalyst:** allows individuals to produce Geographic-scale consequences by leveraging natural systems (Part VIII of this document)
- **Institutional Pooling:** allows coordinated groups to execute high-Scope actions through FP aggregation (Part I of this document)
- **Chronos effects:** allow temporal manipulation that breaks normal tempo constraints (Part I of this document)
- **Treasure-tier geometry:** allows specific actions at Geographic scale through acquired capability
- **Penetrating Additive (+2/+4/+6):** breaks Immunity specifically. Does NOT break Smoothing.

## Aíon's Continuous Maintenance

The Operating Philosophy establishes that Aíon continuously expends infinite FP at Scope ∞ to maintain the Smoothing Effect. This is setting cosmology, not a mechanical variable in play — players cannot "target Aíon" or reduce Smoothing resistance directly.

What players CAN do is perform actions that stress the Smoothing Effect in their region. Enough stress accumulated over time can produce Reality Seam events (location-specific breakdowns where multiple planar expressions overlap without Aíon's full moderation). These are narrative events, not mechanical outputs — the GM introduces them when the accumulated stress warrants.

## The Smoothing Effect at High Scopes

At Scope 7-8 and above, the Smoothing Effect's resistance becomes narratively visible. Institutions attempting civilizational-scale changes encounter:

- Political opposition
- Economic resistance
- Logistical complications
- Unforeseen consequences
- Third-party intervention

These are not separate mechanical systems. They are the Smoothing Effect expressing through the fronts/clocks/adventures architecture from the Operating Philosophy. The institution with an ambitious S7 goal must fill many S0-S6 clocks through accumulated pressure to achieve their objective. The Smoothing Effect ensures that this takes real time and produces real friction.

Combat engine implication: when player characters engage with high-Scope institutions or attempt high-Scope operations, the mechanical resolution still happens at S0-S2 combat level. The Smoothing Effect means that their individual actions are one tick in a much larger clock. They cannot win a war in a single battle because the war's clock has many segments that must be filled.

This is why campaigns produce sustained narrative arcs rather than single decisive encounters. The mechanical system enforces the narrative structure.

---

*End of Document 2, Part III. This completes the core combat engine specification. Future documents will address: specific talent tree mechanics, the companion/summon system integration, advanced magical expressions, and cross-document integration with the mutation economy, crafting system, and legacy/ascension systems.*
