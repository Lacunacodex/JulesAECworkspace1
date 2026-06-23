# ÆTHERIUM CODEX — The Economic Value System
## Intrinsic Value & The Twenty Economic Filters

*Working Document — Alpha Development*

---

## PART I: INTRINSIC VALUE (PHYSICAL — What Something Is Actually Worth)

### The Baseline

A common worked item — EML 1, FS 2-3, no significant hazard, basic workshop conditions — is the baseline. Its value ratio = **1.0**. Everything else is expressed as a multiple of this baseline.

### The Variables

All variables are physical/chemical measurements already tracked in the system:

| Variable | Source | What It Measures |
|---|---|---|
| **Labor** | PV | Total skilled work required |
| **Scarcity** | Formation Stage + geological/chemical rarity | How difficult the material is to find in nature |
| **Utility** | Compatibility breadth (cooperative interaction count) | How many processes and applications the material participates in |
| **Risk** | NFPA hazard ratings | How dangerous the material is to work with |
| **Infrastructure** | Crafting TN conditions count | What facilities are needed |
| **Time** | Weeks to completion | Calendar time invested |

### The Ratio Formula

**Value Ratio = Labor Factor × Scarcity Factor × Utility Factor**

Risk and Infrastructure modify the Labor Factor (they increase production cost). Time is embedded in Labor through PV.

**Labor Factor** = (PV + Risk Premium + Infrastructure Premium) ÷ Baseline PV

| Component | Calculation |
|---|---|
| Baseline PV | 100 (simple weapon, standard quality) |
| Risk Premium | Highest hazard 0-2: +0, 3-4: +50, 5-6: +100, 7-8: +200, 9-10: +400 |
| Infrastructure Premium | 1-2 conditions: +0, 3-4: +50, 5-6: +100, 7+: +200 |

**Scarcity Factor** (U-curve — both extremes rarer than middle)

| Formation Stage | Factor | Availability |
|---|---|---|
| 0 | 1.5 | Uncommon — requires absence of planar exposure |
| 1 | 1.2 | Slightly uncommon — minimal exposure |
| 2-3 | 1.0 | Very common — ambient accumulation (BASELINE) |
| 4 | 1.3 | Common but curated — moderate bleed zones |
| 5 | 2.0 | Uncommon — sustained bleed or processing |
| 6 | 3.0 | Uncommon-rare — significant bleed or intensive processing |
| 7 | 5.0 | Rare — deep bleed zones or master processing |
| 8 | 8.0 | Very rare — extreme planar proximity |
| 9 | 12.0 | Extremely rare — legendary sources |
| 10 | 20.0 | Near-unique — peak planar concentration |

**Utility Factor** (compatibility breadth — how many processes the material participates in)

| Utility Rating | Factor | Character |
|---|---|---|
| 10 (universal) | 3.0 | Water-equivalent. Participates in nearly everything. |
| 7-9 (broad) | 2.0-2.5 | Common metals, biological tissue. Many applications. |
| 4-6 (moderate) | 1.0-1.5 | Specialized materials. Significant but limited application. |
| 2-3 (narrow) | 0.5-0.8 | Exotic materials. Few applications but potent in those. |
| 1 (inert) | 0.3 | Noble gas equivalent. Almost nothing uses it. |

### Test Items — Raw Value Ratios

| Item | PV | Risk | Infra | Labor Factor | Scarcity | Utility | Raw Ratio |
|---|---|---|---|---|---|---|---|
| **A: Iron knife** | 100 | +0 | +0 | 1.0 | 1.0 (FS 2) | 2.0 (broad — iron is useful) | **2.0** |
| **B: Steel longsword** | 200 | +0 | +50 | 2.5 | 1.0 (FS 3) | 2.0 (broad — steel is versatile) | **5.0** |
| **C: Expressed blade** | 400 | +50 | +100 | 5.5 | 2.0 (FS 5) | 1.5 (moderate — specific expression) | **16.5** |
| **D: Master weapon** | 800 | +200 | +200 | 12.0 | 5.0 (FS 7) | 1.5 (moderate) | **90.0** |
| **E: Legendary emulsion** | 2000 | +400 | +200 | 26.0 | 12.0 (FS 9) | 0.8 (narrow — emulsion is specialized) | **249.6** |

*Note: Item E has LOWER utility factor than Item D despite higher EML because emulsion materials are narrowly compatible — they do one thing extremely well but can't participate in most standard processes. Scarcity does the heavy lifting on its value.*

### The Value Curve

| Tier | Raw Ratio | Context |
|---|---|---|
| Common worked item | 1.0-3.0 | A day laborer's wages buy these |
| Quality martial equipment | 3.0-8.0 | A professional's monthly income |
| Expressed equipment | 10.0-30.0 | A professional's seasonal income |
| Master-grade expressed | 50.0-150.0 | Institutional purchase level |
| Legendary/Emulsion | 200.0-500.0 | Kingdom-level asset |
| Theoretical maximum | ~1,000+ | Civilization-defining artifact |

---

## PART II: THE TWENTY ECONOMIC FILTERS (SOCIAL — What Someone Actually Pays)

Each economy reweights the physical variables based on what that society VALUES. The raw ratio enters the filter. A modified price ratio exits. The same item has different prices in different economies because different societies care about different things.

### How to Read Each Filter

**Dominant Variable:** Which physical variable this economy cares about most — it amplifies this.
**Suppressed Variable:** Which physical variable this economy ignores or devalues — it diminishes this.
**Social Modifier:** What non-physical factor this economy adds to the price.
**Price Formula:** How to convert raw ratio to local price ratio.
**Effect on Test Items:** How items A through E price differently here versus raw.

---

### PHYSICAL ECONOMIES (EC-01 through EC-04)

#### EC-01: Feudal Agrarianism
*"Value is soil and calorie production."*

**Dominant:** Labor (measured in equivalent agricultural work-seasons)
**Suppressed:** Utility above local understanding — if nobody locally knows what an emulsion does, its utility factor drops to 1.0
**Social Modifier:** Land-equivalence. All prices expressed in "how many acres would this buy?"
**Price Formula:** Raw ratio × 1.0, but Utility Factor capped at 2.0 for items above EML 3 (local understanding ceiling). Items above EML 5 enter barter-only territory — no standard price exists.

| Item | Raw | EC-01 Price | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | 2.0 | Understood, valued, priced normally |
| B: Steel longsword | 5.0 | 5.0 | Understood, valued, priced normally |
| C: Expressed blade | 16.5 | 11.0 | Utility capped — locals don't fully grasp what it does |
| D: Master weapon | 90.0 | BARTER | Above local understanding ceiling |
| E: Legendary emulsion | 249.6 | BARTER | Incomprehensible to local economy |

#### EC-02: Scavenger/Barter
*"Value is what you can find, carry, and immediately exchange."*

**Dominant:** Utility (what can it do for me RIGHT NOW?)
**Suppressed:** Labor and Infrastructure (the scavenger didn't make it — they found it)
**Social Modifier:** Portability — heavy items worth less because they're harder to carry and trade
**Price Formula:** Labor Factor halved. Utility Factor doubled. Scarcity Factor halved (if you found it, you didn't pay for rarity). Density penalty: items with Density 7+ get ×0.75.

| Item | Raw | EC-02 Price | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | 2.0 | Useful, portable, good trade |
| B: Steel longsword | 5.0 | 3.8 | Useful but heavy — slight density penalty |
| C: Expressed blade | 16.5 | 16.5 | Useful AND expressed — utility doubling offsets labor halving |
| D: Master weapon | 90.0 | 67.5 | Scarcity matters less to someone who found it in a ruin |
| E: Legendary emulsion | 249.6 | 124.8 | Found is found — but the utility is narrow so doubling utility doesn't help much |

#### EC-03: Predatory/Raiding
*"Value is what you take from others."*

**Dominant:** None of the production variables — the raider didn't make anything
**Suppressed:** ALL production variables. The cost is military, not economic.
**Social Modifier:** Acquisition risk — what it cost to take. Expressed as casualties and resources expended.
**Price Formula:** Raw ratio replaced by (Combat Power of Defender × Casualty Risk). For SELLING stolen goods: raw ratio × 0.5 (fence discount — stolen goods sell below value).

| Item | Raw | EC-03 Price (to acquire) | EC-03 Price (to sell) | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | ~0.5 (undefended) | 1.0 | Easy to take, sells at half |
| B: Steel longsword | 5.0 | ~3.0 (armed target) | 2.5 | Must defeat the wielder |
| C: Expressed blade | 16.5 | ~10.0 (capable wielder) | 8.3 | Harder to take from someone who can use it |
| D: Master weapon | 90.0 | ~60.0 (elite guard) | 45.0 | Institutional protection |
| E: Legendary emulsion | 249.6 | ~200.0+ (army required) | 124.8 | Kingdom-level heist |

#### EC-04: Industrialism
*"Value is finished goods and production capacity at scale."*

**Dominant:** Labor efficiency — mass production reduces per-unit cost
**Suppressed:** Scarcity for reproducible items (the factory produces supply). Utility premium for common items (competition drives margins down).
**Social Modifier:** Schematic access — mass production requires Guild+ schematics
**Price Formula:** With schematic: Labor Factor × 0.6 (mass production efficiency). Without schematic: raw ratio × 1.2 (artisan premium for handmade in an industrial economy). Scarcity only applies to materials that can't be industrially sourced.

| Item | Raw | EC-04 Price (mass) | EC-04 Price (artisan) | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 1.2 | 2.4 | Mass-produced knives are cheap |
| B: Steel longsword | 5.0 | 3.0 | 6.0 | Factory swords vs handmade |
| C: Expressed blade | 16.5 | N/A (can't mass produce) | 19.8 | Artisan premium in industrial economy |
| D: Master weapon | 90.0 | N/A | 108.0 | Artisan premium — these can't be factored |
| E: Legendary emulsion | 249.6 | N/A | 299.5 | Handmade commands premium when everything else is mass-produced |

---

### MENTAL ECONOMIES (EC-05 through EC-08)

#### EC-05: Laissez-Faire
*"Value is profit. Competition determines everything."*

**Dominant:** Whatever the market says today — high variance
**Suppressed:** Nothing permanently — the market fluctuates
**Social Modifier:** Competition. Multiple sellers drive prices down. Monopoly drives prices up.
**Price Formula:** Raw ratio × (0.7 to 1.5) depending on local supply/demand. Roll d6 for market conditions: 1-2 = buyer's market (×0.7-0.8), 3-4 = balanced (×0.9-1.1), 5-6 = seller's market (×1.2-1.5). Most volatile economy.

| Item | Raw | EC-05 Range | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | 1.4-3.0 | Commodity — market swings affect even basics |
| B: Steel longsword | 5.0 | 3.5-7.5 | Standard martial — moderate variance |
| C: Expressed blade | 16.5 | 11.6-24.8 | Specialist market — higher variance |
| D: Master weapon | 90.0 | 63.0-135.0 | Auction territory — buyer competition |
| E: Legendary emulsion | 249.6 | 174.7-374.4 | Maximum variance — unique items have no stable price |

#### EC-06: Corporate Mercantilism
*"Value is market share and charter rights."*

**Dominant:** Institutional control — whoever holds the charter sets the price
**Suppressed:** Competition (monopoly eliminates alternatives)
**Social Modifier:** Charter markup — the chartered producer adds 50-100% margin because no competition exists
**Price Formula:** Raw ratio × 1.5 for chartered goods (the institution adds margin). Raw ratio × 0.8 for non-chartered goods (suppressed to protect the charter). Black market chartered goods: raw ratio × 1.0 (dodging the markup but accepting political risk).

| Item | Raw | EC-06 Price (chartered) | EC-06 Price (non-chartered) | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 3.0 | 1.6 | Ironworker guild controls pricing |
| B: Steel longsword | 5.0 | 7.5 | 4.0 | Weaponsmith charter |
| C: Expressed blade | 16.5 | 24.8 | 13.2 | Expressed items require institutional charter |
| D: Master weapon | 90.0 | 135.0 | ILLEGAL | Only chartered masters may produce |
| E: Legendary emulsion | 249.6 | 374.4 | ILLEGAL | Institutional monopoly absolute |

#### EC-07: Protectionism
*"Value is domestic reserve and autarky."*

**Dominant:** Scarcity of imported materials (tariffs inflate foreign-sourced scarcity)
**Suppressed:** Utility of foreign goods (domestic alternatives promoted even if inferior)
**Social Modifier:** Import tariff. Foreign-sourced materials: Scarcity Factor × 2.0. Domestic materials: Scarcity Factor × 0.8 (subsidized).
**Price Formula:** Domestic items: raw ratio × 0.9. Imported items: raw ratio × 1.5-2.0. Items requiring imported components: blended rate.

| Item | Raw | EC-07 Domestic | EC-07 Imported | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 1.8 | 3.0 | Local iron subsidized, foreign taxed |
| B: Steel longsword | 5.0 | 4.5 | 7.5 | Same pattern |
| C: Expressed blade | 16.5 | 14.9 | 33.0 | Expressed materials often require import — heavy tariff |
| D: Master weapon | 90.0 | 81.0 | 180.0 | Rare materials almost always imported |
| E: Legendary emulsion | 249.6 | N/A (can't source domestically) | 499.2 | Full import tariff — doubled |

#### EC-08: Resource-Based
*"No currency — only measured contribution."*

**Dominant:** Labor (measured in energy-equivalent work units)
**Suppressed:** Scarcity (the system allocates resources by need, not market). Utility premium eliminated (a sword and a plowshare cost the same work).
**Social Modifier:** Need assessment — items are allocated by committee determination of social need
**Price Formula:** Labor Factor only. All other multipliers = 1.0. Price = pure production cost in energy credits. No profit, no scarcity premium, no utility premium.

| Item | Raw | EC-08 Price | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | 1.0 | Pure labor cost — iron knife = 100 PV of work |
| B: Steel longsword | 5.0 | 2.5 | More work = more energy credits |
| C: Expressed blade | 16.5 | 5.5 | Only labor + risk + infrastructure count |
| D: Master weapon | 90.0 | 12.0 | Dramatically cheaper — scarcity and utility stripped |
| E: Legendary emulsion | 249.6 | 26.0 | Same — only production cost matters |

*Note: EC-08 makes powerful items MUCH more accessible but requires committee approval for allocation. The price is low but the access is controlled by need assessment rather than wealth.*

---

### SOCIAL ECONOMIES (EC-09 through EC-12)

#### EC-09: Planned Economy
*"Value is quota fulfillment."*

**Dominant:** Central authority pricing — the state decides
**Suppressed:** Market signals (no supply/demand adjustment)
**Social Modifier:** Policy weighting. Essential items (healing potions, basic weapons) priced below raw ratio (subsidized). Luxury items priced above (taxed). The authority absorbs the difference.
**Price Formula:** Essential items: raw ratio × 0.6. Standard items: raw ratio × 1.0. Luxury items: raw ratio × 1.5. Classification is political — what counts as "essential" is a policy decision.

| Item | Raw | EC-09 Price | Classification | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 1.2 | Essential tool | Subsidized — everyone needs basic tools |
| B: Steel longsword | 5.0 | 5.0 | Standard | Military equipment — no adjustment |
| C: Expressed blade | 16.5 | 24.8 | Luxury | Taxed — expressed items are luxury goods |
| D: Master weapon | 90.0 | 135.0 | Luxury | Heavy luxury tax |
| E: Legendary emulsion | 249.6 | STATE ASSET | Controlled | Not available for individual purchase |

#### EC-10: Collectivism
*"No private property. Everything managed by collective will."*

**Dominant:** Social consensus on need
**Suppressed:** Individual ownership — you don't buy things, they're assigned
**Social Modifier:** Communal allocation. Items belong to the community, not individuals. "Price" is reputation cost — what the community thinks of you requesting this item.
**Price Formula:** No monetary price. Allocation based on demonstrated need + community standing. Raw ratio determines allocation priority — higher ratio items require more community justification.

| Item | Raw | EC-10 "Price" | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | Automatic allocation | Basic need, no justification required |
| B: Steel longsword | 5.0 | Role-based allocation | Assigned to community defenders |
| C: Expressed blade | 16.5 | Community vote | Must justify why YOU specifically need this |
| D: Master weapon | 90.0 | Council approval | Significant community asset — requires formal justification |
| E: Legendary emulsion | 249.6 | Community treasure | Belongs to everyone — assigned to whoever the community chooses |

#### EC-11: Syndicalism
*"Value is labor value measured in hours and skills."*

**Dominant:** Labor — but specifically SKILLED labor. Higher-skill work is worth more per hour.
**Suppressed:** Scarcity premium (the union controls supply to stabilize prices). Utility premium moderated (the guild sets fair prices, not the market).
**Social Modifier:** Skill tier multiplier. Novice labor: ×1.0. Journeyman: ×2.0. Master: ×3.0. The crafter's rank directly multiplies the labor component.
**Price Formula:** Labor Factor × Skill Multiplier × Scarcity Factor (moderated to ×0.7 of raw). Utility Factor capped at 1.5.

| Item | Raw | EC-11 Price | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | 2.0 | Novice work, standard material |
| B: Steel longsword | 5.0 | 7.0 | Journeyman work — skill multiplier kicks in |
| C: Expressed blade | 16.5 | 16.5 | Journeyman+ work, utility cap moderates |
| D: Master weapon | 90.0 | 126.0 | Master skill multiplier ×3 on labor |
| E: Legendary emulsion | 249.6 | 280.0 | Master work but utility cap and scarcity moderation contain the price |

#### EC-12: Distributism / Gift Economy
*"Value is social capital."*

**Dominant:** Reputation and relationship — you don't buy, you exchange favors
**Suppressed:** Monetary value entirely. Scarcity matters (rare gifts are more impressive) but labor doesn't (the effort is invisible — the gift just appears).
**Social Modifier:** Social debt. Receiving a gift creates obligation. The "price" is the reciprocal obligation incurred.
**Price Formula:** No monetary price. Value ratio determines the magnitude of social debt incurred. Item A creates minor obligation. Item E creates life-debt.

| Item | Raw | EC-12 "Price" | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | Minor favor owed | Small gift, small obligation |
| B: Steel longsword | 5.0 | Significant favor | Meaningful gift to a warrior |
| C: Expressed blade | 16.5 | Major obligation | Serious gift requiring serious reciprocation |
| D: Master weapon | 90.0 | Life-service | This gift binds you to the giver |
| E: Legendary emulsion | 249.6 | Generational debt | Your family owes their family |

---

### METAPHYSICAL ECONOMIES (EC-13 through EC-16)

#### EC-13: Post-Scarcity
*"Material wealth meaningless. Status and purpose replace accumulation."*

**Dominant:** Meaning — what does the item represent?
**Suppressed:** ALL physical variables. Materials are abundant. Labor is automated or trivial. Scarcity is engineered not natural.
**Social Modifier:** Purpose premium. Items with Legacy (Social condition track above Broken) are the ONLY items worth anything. Raw materials and standard equipment have no value because anyone can get them.
**Price Formula:** Items without Legacy: effectively free. Items with Legacy history: raw ratio × Social Condition multiplier (Broken ×0, Damaged ×1, Worn ×5, Pristine ×20).

| Item | Raw | EC-13 Price | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | FREE | Anyone can fabricate this |
| B: Steel longsword | 5.0 | FREE | Standard equipment — no scarcity |
| C: Expressed blade | 16.5 | FREE (unless Legacy) | The expression alone isn't rare here |
| D: Master weapon (with history) | 90.0 | 450.0 (if Social Worn) | The STORY is what matters |
| E: Legendary emulsion (Pinnacle item) | 249.6 | 4,992.0 (if Social Pristine) | A famous artifact in a post-scarcity world is priceless |

#### EC-14: Soul Trade
*"Consciousness is currency."*

**Dominant:** Metaphysical properties — EML, FS, isotope identity
**Suppressed:** Physical labor (bodies are cheap). Infrastructure (souls build facilities).
**Social Modifier:** Soul-equivalent pricing. Value measured in fractions of a soul's worth. The metaphysical variables are weighted at ×2, physical variables at ×0.5.
**Price Formula:** (Labor Factor × 0.5) × (Scarcity Factor × 2.0) × (Utility Factor × 2.0). Powerful magical items cost MUCH more. Mundane items cost much less.

| Item | Raw | EC-14 Price | Why |
|---|---|---|---|
| A: Iron knife | 2.0 | 1.0 | Physical labor devalued |
| B: Steel longsword | 5.0 | 2.5 | Physical goods are cheap when souls are currency |
| C: Expressed blade | 16.5 | 33.0 | Metaphysical properties doubled |
| D: Master weapon | 90.0 | 360.0 | High FS + high EML = extremely expensive |
| E: Legendary emulsion | 249.6 | 998.4 | The most expensive economy for powerful magical items |

#### EC-15: Ritual/Tribute
*"Economy based on sacrifice. Value is divine favor."*

**Dominant:** Sacred significance — items connected to divine values cost divine favor
**Suppressed:** Secular utility. A plow and a sword cost the same tribute if the god values both equally.
**Social Modifier:** Divine alignment. Items whose isotope aligns with the local deity: price reduced (the god provides). Items antithetical to local deity: price increased (offering to an opposing force).
**Price Formula:** Aligned items: raw ratio × 0.5 (divine subsidy). Neutral items: raw ratio × 1.0. Antithetical items: raw ratio × 2.0 (sacrilegious surcharge).

| Item | Raw | EC-15 (aligned) | EC-15 (antithetical) | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 1.0 | 4.0 | Depends on local deity's relationship to Bedrock |
| B: Steel longsword | 5.0 | 2.5 | 10.0 | Same — divine alignment matters |
| C: Expressed blade | 16.5 | 8.3 | 33.0 | Expressed items are more sensitive to alignment |
| D: Master weapon | 90.0 | 45.0 | 180.0 | Major alignment discount or surcharge |
| E: Legendary emulsion | 249.6 | 124.8 | 499.2 | Antithetical emulsion in a temple economy is ruinously expensive |

#### EC-16: Entropic
*"The economy exists to destroy resources. Production feeds destruction."*

**Dominant:** Consumability — items that get used up are valued. Items that persist are waste.
**Suppressed:** Durability and permanence. A lasting sword is LESS valuable than a consumable one because the economy values throughput, not accumulation.
**Social Modifier:** Consumption premium. Consumables (potions, scrolls, ammunition): raw ratio × 1.5. Permanent items: raw ratio × 0.5. The economy penalizes hoarding.
**Price Formula:** Consumable items: raw ratio × 1.5. Permanent items: raw ratio × 0.5.

| Item | Raw | EC-16 Price | Why |
|---|---|---|---|
| A: Iron knife (permanent) | 2.0 | 1.0 | Permanent — devalued |
| B: Steel longsword (permanent) | 5.0 | 2.5 | Permanent — devalued |
| C: Expressed blade (permanent) | 16.5 | 8.3 | Permanent — devalued |
| D: Master weapon (permanent) | 90.0 | 45.0 | Permanent — heavily devalued |
| E: Healing potion (consumable) | 5.0 | 7.5 | Consumable — premium |
| E: Alchemist's fire (consumable) | 8.0 | 12.0 | Consumable — premium |

---

### INSTITUTIONAL ECONOMIES (EC-17 through EC-20)

#### EC-17: Reserve Control
*"Accumulation and controlled release of critical resource."*

**Dominant:** Access control — the institution holds the supply and meters release
**Suppressed:** Market price discovery (no competition — one source)
**Social Modifier:** Queue position fee + release fee. The institution charges for the right to access, then charges again for the actual item.
**Price Formula:** Raw ratio + Access Fee (flat, based on institutional tier: local ×0.5 raw, regional ×1.0 raw, national ×2.0 raw) + Release Fee (10-30% of raw ratio).

**Setting Expression:** Mortis Aevum's soul queue. The "price" of resurrection includes queue position fee + processing fee + the soul's actual metaphysical value.

| Item | Raw | EC-17 Price (local) | EC-17 Price (national) | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 3.5 | 6.0 | Access fee exceeds item value at national level |
| B: Steel longsword | 5.0 | 8.3 | 12.5 | Access fee is significant portion |
| C: Expressed blade | 16.5 | 25.6 | 38.1 | Access fee proportionally smaller |
| D: Master weapon | 90.0 | 130.5 | 184.0 | Institution controls all rare materials |
| E: Legendary emulsion | 249.6 | 362.0 | 511.6 | Maximum institutional control |

#### EC-18: Platform Arbitrage
*"Price discovery and liquidity provision."*

**Dominant:** Market efficiency — the platform finds the true price through competitive bidding
**Suppressed:** Nothing permanently — the platform is neutral
**Social Modifier:** Transaction fee (5-15% of final price to the platform operator). Information advantage — traders with Appraiser skills get better prices.
**Price Formula:** Raw ratio is the opening bid. Final price determined by auction mechanics. Platform fee deducted. Typical range: raw ratio × 0.9-1.3 depending on competition.

**Setting Expression:** The Sovereign Exchange. Price discovery through competitive bidding. The Exchange takes its cut.

| Item | Raw | EC-18 Range | Platform Fee | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 1.8-2.6 | 0.1-0.3 | Commodity — efficient pricing |
| B: Steel longsword | 5.0 | 4.5-6.5 | 0.3-0.7 | Standard goods — moderate variance |
| C: Expressed blade | 16.5 | 14.9-21.5 | 0.8-2.2 | Specialist market — more variance |
| D: Master weapon | 90.0 | 81.0-117.0 | 4.5-11.7 | Auction territory — significant fees |
| E: Legendary emulsion | 249.6 | 224.6-324.5 | 12.5-32.5 | The Exchange's biggest transactions |

#### EC-19: Capability Export
*"The product is trained people."*

**Dominant:** Knowledge embodied in the item — schematic value, technique represented
**Suppressed:** Raw material value (the institution produces capability, not goods)
**Social Modifier:** Training premium. Items that TEACH (schematics, training manuals, apprentice tools) are valued above raw ratio. Items that only PERFORM (finished goods with no educational component) are valued at or below raw.
**Price Formula:** Items with schematic/educational value: raw ratio × 1.5-2.0. Standard items: raw ratio × 0.8.

**Setting Expression:** Stormpeak and Praxis. They export trained graduates, not finished products. A Stormpeak-certified schematic is worth more than the items it produces.

| Item | Raw | EC-19 (standard item) | EC-19 (with schematic) | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 1.6 | 3.0 (schematic for the knife) | The recipe is worth more than the product |
| B: Steel longsword | 5.0 | 4.0 | 7.5 | Training value exceeds item value |
| C: Expressed blade | 16.5 | 13.2 | 33.0 | Expressed item schematic is extremely valuable |
| D: Master weapon | 90.0 | 72.0 | 180.0 | Master schematic is the real product |
| E: Legendary emulsion | 249.6 | 199.7 | 499.2 | The knowledge of how to make this IS the treasure |

#### EC-20: Rent Extraction
*"Positioning within a necessary function."*

**Dominant:** Positional control — you MUST pass through this chokepoint
**Suppressed:** Intrinsic value is irrelevant — the rent is based on the cost of NOT using the chokepoint
**Social Modifier:** Positional rent. The markup is based on what the alternative costs (going around, making your own, doing without), not on the item's actual value.
**Price Formula:** Raw ratio + Positional Rent. Rent = (Cost of Alternative − Raw Ratio) × Capture Rate (30-70%). If no alternative exists: rent = raw ratio × 0.5-1.0 (pure monopoly markup).

**Setting Expression:** Deepguard, Wildpath, Chronosynclastic. Each controls a chokepoint — security, wilderness access, temporal knowledge.

| Item | Raw | EC-20 (alternative exists) | EC-20 (no alternative) | Why |
|---|---|---|---|---|
| A: Iron knife | 2.0 | 2.5 (alternatives are easy) | 3.0 | Low rent — alternatives abundant |
| B: Steel longsword | 5.0 | 6.5 | 7.5 | Moderate rent — some alternatives |
| C: Expressed blade | 16.5 | 23.1 (alternative is expensive) | 24.8 | Higher rent — fewer alternatives |
| D: Master weapon | 90.0 | 135.0 | 180.0 | High rent — almost no alternatives |
| E: Legendary emulsion | 249.6 | 374.4 | 499.2 | Maximum rent — literally no alternative source |

---

## PART III: CROSS-ECONOMY COMPARISON

*How the same Item C (Expressed Blade, raw ratio 16.5) prices across all 20 economies:*

| EC | Type | Price | Relative to Raw |
|---|---|---|---|
| EC-01 | Feudal Agrarianism | 11.0 | 0.67× (utility capped) |
| EC-02 | Scavenger/Barter | 16.5 | 1.0× (utility/labor wash) |
| EC-03 | Predatory/Raiding | 8.3 (fence) | 0.5× (stolen goods discount) |
| EC-04 | Industrialism | 19.8 | 1.2× (artisan premium) |
| EC-05 | Laissez-Faire | 11.6-24.8 | 0.7-1.5× (volatile) |
| EC-06 | Corp. Mercantilism | 24.8 (chartered) | 1.5× (monopoly markup) |
| EC-07 | Protectionism | 14.9-33.0 | 0.9-2.0× (domestic vs import) |
| EC-08 | Resource-Based | 5.5 | 0.33× (only labor counts) |
| EC-09 | Planned Economy | 24.8 | 1.5× (luxury tax) |
| EC-10 | Collectivism | Community vote | N/A (no monetary price) |
| EC-11 | Syndicalism | 16.5 | 1.0× (skill-weighted) |
| EC-12 | Distributism/Gift | Major obligation | N/A (social debt) |
| EC-13 | Post-Scarcity | FREE (or 82.5 with Legacy) | 0-5.0× (story value only) |
| EC-14 | Soul Trade | 33.0 | 2.0× (metaphysical doubled) |
| EC-15 | Ritual/Tribute | 8.3-33.0 | 0.5-2.0× (divine alignment) |
| EC-16 | Entropic | 8.3 | 0.5× (permanent = devalued) |
| EC-17 | Reserve Control | 25.6-38.1 | 1.5-2.3× (access fees) |
| EC-18 | Platform Arbitrage | 14.9-21.5 | 0.9-1.3× (market-discovered) |
| EC-19 | Capability Export | 13.2 (item) / 33.0 (schematic) | 0.8-2.0× (knowledge premium) |
| EC-20 | Rent Extraction | 23.1-24.8 | 1.4-1.5× (positional rent) |

**Lowest price:** EC-08 Resource-Based (5.5 — only labor counts)
**Highest monetary price:** EC-14 Soul Trade (33.0 — metaphysical properties doubled)
**Most volatile:** EC-05 Laissez-Faire (11.6-24.8 range)
**Most stable:** EC-09 Planned Economy (24.8 — fixed by authority)
**Non-monetary:** EC-10 and EC-12 (social debt replaces currency)

---

*End of Economic Value System working document.*
*Note: All multiplier values are playtest targets. The structure — physical variables producing intrinsic value, social filters converting to local price — is the design. The specific numbers will require calibration through actual play.*
