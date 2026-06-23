**ÆTHERIUM CODEX**

**Item Creation System**

**Complete Rewrite --- Five Ways Integrated Edition**

*Alpha Draft --- Supersedes all prior Item Creation documents*

**PREAMBLE --- THE INSEPARABILITY PRINCIPLE**

Alchemy is not an overlay on item creation. It is item creation\'s
foundation. The inseparability principle: just as a real element\'s
chemical reactions are not properties added to it but are the same thing
as the element expressed from a different angle, an item\'s alchemical
specification IS its mechanical specification. The Dual Periodic Table
entry for a material IS its stat block. The Five Ways specification IS
its component register.

This means every number in item creation is derivable from first
principles. A GM does not decide that a steel longsword deals 1d8
damage. The Dual Periodic Table specifies that CP-10 steel (B-09/F-09)
has a tensile strength placing it in the 1d8 damage tier. A designer
does not decide that a healing potion has CML 3. The planar tier of the
Generative Font compound combined with the Spell Sentence modifier
produces CML 3. The design space is discovered, not invented.

  -----------------------------------------------------------------------
  *SYSTEM ARCHITECTURE: Item creation has four steps and three mechanical
  layers. The four steps (Material Identification, Processing, Slot
  Architecture, Legacy) describe WHAT the crafter does. The three layers
  (Core Process, Artifice Engine, Ascension) describe HOW the system
  handles each step mechanically. The Five Ways documents specify the
  alchemical content that flows through all four steps and all three
  layers.*

  -----------------------------------------------------------------------

**OVERVIEW --- THE FOUR STEPS**

  ----------------------------------------------------------------------------
  **Step**           **What It Is**        **Way             **Output**
                                           Participation**   
  ------------------ --------------------- ----------------- -----------------
  **Step 1 ---       Reading the           All five Ways     Complete material
  Material           material\'s complete  potentially       specification:
  Identification**   alchemical passport.  present as        base stats (Soak,
                     Which Ways does this  read-only data.   damage tier,
                     material participate  No active Way     weight), Way
                     in? What are its      operation ---     participation
                     Chemical Lane,        this step is      flags, Natural
                     Aetheric Profile,     observation only. and Forbidden
                     Formation Stage, and                    combinations,
                     planar tier? What                       affinity
                     combinations does it                    alignment for
                     enter naturally and                     Innate/Powered
                     which require Forge                     determination.
                     catalyst?                               

  **Step 2 ---       Transforming raw      Way 4 (Hidden     Workable material
  Processing**       material into         Forge) primary.   at the required
                     workable form. Every  Way 1             processing grade.
                     processing step       (Borderlands)     Crafting TN set
                     (roasting, smelting,  secondary. Way 3  by difficulty of
                     refining, tempering,  (Synod) as the    Forge mediation.
                     quenching) is a Way 4 endpoint being    PV consumed.
                     Forge operation       targeted.         Artifice Events
                     applied to the                          occur here.
                     material\'s Way 1                       
                     Borderlands                             
                     expression, driving                     
                     it toward a Way 3                       
                     Synod stable                            
                     endpoint.                               

  **Step 3 --- Slot  Installing alchemical Way 4 (Forge) for Functional item
  Architecture**     expressions as Active the installation  with specified
                     and Enabling          process. The      effects. CML and
                     Components. A         installed         EML calculated.
                     component is not a    component\'s      Battery type and
                     spell applied to an   native Way(s) for capacity
                     item --- it is a      the expression    determined.
                     specific planar       itself. Way 5     Innate or Powered
                     expression drawn to   (Palimpsest) for  alignment
                     the surface and fixed affinity          confirmed.
                     by Forge mediation.   alignment and CML 
                                           selection.        

  **Step 4 ---       The item\'s           Way 5             Ascension Traits
  Legacy**           alchemical expression (Palimpsest)      at AP thresholds.
                     deepening through     primary ---       Emulsion slot
                     use. AP accumulation  probability       available at
                     is the item\'s Way 5  crystallizing     Mastery tier.
                     probability space     into fixed        Aberration
                     narrowing --- the     identity. Way 3   specified for
                     Palimpsest            (Synod            incompatible
                     progressively         Sepulchral) ---   trait attempts.
                     Resolves toward       the record of use 
                     specific Ascension    becoming          
                     Traits based on the   permanent. Way 4  
                     AP pattern.           (Forge            
                                           Calibrated) ---   
                                           precision         
                                           deepening.        
  ----------------------------------------------------------------------------

  -----------------------------------------------------------------------
  **STEP 1: MATERIAL IDENTIFICATION**

  -----------------------------------------------------------------------

Material Identification is the Two-Table Check: read the real Periodic
Table for physical properties, then read the Alchemical Periodic Table
for planar identity. Both readings are required for a complete material
specification.

  -----------------------------------------------------------------------
  **STEP 1 OUTPUTS: 1. Base Stats: Soak from Hardness Score, Damage Tier
  from tensile strength (MPa), Weight Class from density (g/cm³) 2.
  Chemical Lane: Corrosive/Caustic/Volatile/Inert (sub-type) from pH and
  reactivity 3. Aetheric Profile: Projecting/Absorbing/Static/Cycling
  from planar primary expression 4. Way Participation: which of the Five
  Ways the material natively expresses 5. Formation Stage: 1-5 (sets
  crafting TN floor, determines rate in reactions) 6. Planar Tier: 1-10
  (determines CML floor for components from this material) 7. Affinity
  Alignment: which component effects the material is Innate for**

  -----------------------------------------------------------------------

**The Affinity Alignment Rule (Innate vs. Powered)**

The old affinity lookup table (checking material archetype against spell
effect category) is replaced by a single derivable rule based on Way
participation.

  -----------------------------------------------------------------------
  *THE RULE: If the item\'s base material shares a primary or secondary
  Way with the Active Component being installed, the item is INNATE for
  that component --- no battery required for passive/continuous effects,
  +1 Efficiency Step for active effects. If the Ways do not match, the
  item is POWERED and requires an Enabling Component battery. Read both
  Way participation flags from the Dual Periodic Table entries.*

  -----------------------------------------------------------------------

  ------------------------------------------------------------------------
  **Material Way**   **Component Way**  **Affinity**   **Result**
  ------------------ ------------------ -------------- -------------------
  Way 2 (Verdant     Way 2 Generative   INNATE ---     No battery for
  Font)              (healing)          same Way       passive healing.
                                                       Healing potion in
                                                       wooden vessel:
                                                       Innate.

  Way 1              Way 2 (Verdant     POWERED ---    Battery required.
  (Borderlands)      Font --- healing)  different Ways Iron flask holding
                                                       healing compound:
                                                       the Forge must
                                                       bridge Way 1 and
                                                       Way 2.

  Way 4 (Forge) ---  Way 1 (Borderlands INNATE         +1 Efficiency Step.
  steel              --- fire damage)   secondary ---  No battery for fire
                                        Borderlands is damage in steel
                                        steel\'s       weapon.
                                        secondary Way  

  Way 3 (Synod) ---  Way 3 Sepulchral   INNATE ---     Soul stone prepared
  bone               (archival)         same Way       in bone housing:
                                                       Innate.

  Way 1              Way 5 (Palimpsest  POWERED ---    Forge Catalyst
  (Borderlands) ---  --- probability    different      required in
  glass              field)             Ways, and      addition to
                                        antithetical   battery. Glass
                                        (Reality       containing
                                        Paradox)       Palimpsest
                                                       compound: Way 4
                                                       mediation
                                                       mandatory.
  ------------------------------------------------------------------------

  -----------------------------------------------------------------------
  **STEP 2: PROCESSING**

  -----------------------------------------------------------------------

Processing is the Way 4 Forge operation applied to the material. The
practitioner\'s skill is Forge expression; the material\'s chemistry is
Borderlands expression. The Forge drives the material toward a Synod
stable endpoint that the practitioner specifies.

**Processing Operations --- Forge Lane Mapping**

  ---------------------------------------------------------------------------------------------
  **Processing          **Forge Lane**       **Borderlands Lane   **Synod        **Crafting TN
  Operation**                                Active**             Endpoint**     Modifier**
  --------------------- -------------------- -------------------- -------------- --------------
  Smelting (ore →       Channeled (furnace   Volatile             Mineral        Base TN.
  metal)                infrastructure       (combustion) +       (molten metal  Standard for
                        directs heat)        Inert-β (ore         cools to pure  common metals.
                                             dissolves as stable  stable form)   
                                             metal)                              

  Refining (impurity    Interfacial          Corrosive (flux) +   Mineral (purer TN +2.
  removal)              (slag-metal boundary Inert-β (metal)      stable form)   Interfacial
                        does the work)                                           work requires
                                                                                 precision.

  Alloying (combining   Interfacial          Inert-β × Inert-β    Mineral (alloy TN +3.
  metals)               (metal-metal         (two metals          stable         Two-lane Forge
                        boundary             combining at         endpoint) ---  work. Produces
                        interdiffusion) +    boundary)            specific       specific alloy
                        Calibrated                                polymorph      properties.
                        (selecting specific                       selected by    
                        alloy composition)                        Calibrated     

  Tempering/Quenching   Channeled            Inert-β with Synod   Preservative   TN +2.
  (hardness adjustment) (temperature         Mineral endpoint     (the specific  Preservative
                        control) +           interrupted at       phase state    endpoint is
                        Calibrated           specific point       locked before  what makes
                        (selecting hardness                       reaching       tempering work
                        level)                                    maximum        --- you stop
                                                                  stability)     the Synod
                                                                                 before it
                                                                                 reaches the
                                                                                 fully stable
                                                                                 (brittle)
                                                                                 state.

  Distillation          Channeled            Volatile/Corrosive   Preservative   TN +1 per
  (compound separation) (infrastructure) +   (more volatile       (each fraction additional
                        Interfacial          component)           preserved in   fraction.
                        (vapor/liquid        separating from      its separated  Standard
                        boundary)            Inert/Caustic (less  state)         alchemical
                                             volatile)                           operation.

  Biological            Channeled (growth    Way 2 Generative or  Way 2 Synod    TN +4. Way 2
  cultivation (Way 2    infrastructure) +    Propagative (the     endpoint       processing
  material)             Propagated           organism\'s biology) (Biotic ---    requires
                        (biological chain                         requires Forge sustained
                        once initiated)                           at all stages) biological
                                                                                 mediation.
  ---------------------------------------------------------------------------------------------

**PV, Crafting TN, and Artifice Events**

  -----------------------------------------------------------------------
  **CRAFTING TN = 10 + (Processing Operation base TN mod) + (Formation
  Stage of material) − (Forge Calibrated Schematic authority level bonus)
  PV per week = (Artifice Rank × 10) + (Relevant Attribute Bonus × 5)
  Weeks to completion = Item Total PV ÷ PV per week**

  -----------------------------------------------------------------------

  ------------------------------------------------------------------------------
  **Artifice Event** **Trigger**        **Mechanical Effect**
  ------------------ ------------------ ----------------------------------------
  **BREAKTHROUGH**   Critical success   Choose: extra output (secondary
                     on Artifice check  precipitate at no additional cost),
                     (natural 20 or TN  hidden property revealed, or PV progress
                     beaten by 10+)     doubled this week. The material\'s
                                        natural Way expression cooperated with
                                        the Forge direction.

  **FORK IN THE      Success but within Choose between: slower and safe (half PV
  ROAD**             2 of TN, or GM     this week, no risk) or pushed and risky
                     choice at a        (full PV, but +1 Complication range next
                     decision point     week). The material is resisting Forge
                                        mediation.

  **COMPLICATION**   Failed Artifice    Choose: accept the complication (item
                     check              has a quirk, reduced stat, or limited
                                        condition) or lose the week\'s PV and
                                        restart that processing stage. The
                                        material\'s natural Way expression
                                        asserted against the Forge direction.

  **CRITICAL         Failed Artifice    Materials lost. Must restart. If working
  FAILURE**          check by 5+        with antithetical emulsion: Toxicity
                                        Type applies. The Forge mediation
                                        collapsed entirely.
  ------------------------------------------------------------------------------

  -----------------------------------------------------------------------
  **STEP 3: SLOT ARCHITECTURE**

  -----------------------------------------------------------------------

**CML Formula --- Revised**

The Spell Sentence cost remains the primary CML driver. The planar tier
of the dominant material sets a minimum floor. The higher value applies.

  -----------------------------------------------------------------------
  **COMPONENT MASTERY LEVEL (CML): Spell Sentence Driver: Base Effect
  Cost + Usage Modifier + Limitation Discounts (see table below) Material
  Floor: Formation Stage of dominant reagent (Stage 1=CML 1, Stage 2=CML
  2-3, Stage 3=CML 4-5, Stage 4=CML 6-7, Stage 5=CML 8+) Final CML =
  max(Spell Sentence result, Material Floor) EFFECTIVE MASTERY LEVEL
  (EML): EML = Highest Active Component CML + floor((Active Components
  − 1) ÷ 4)**

  -----------------------------------------------------------------------

  --------------------------------------------------------------------------
  **Modifier**    **Value**                        **Notes**
  --------------- -------------------------------- -------------------------
  **BASE EFFECT   Damage/Features/Speed: 1 \|      Read from Spell Sentence
  COST**          Protection/Healing/Illusion: 2   list. This is the floor
                  \|                               CML before any modifiers.
                  Teleport/Nullify/Resurrection: 3 
                  \| Immunity/Time/Dimensional: 4  

  **USAGE         Continuous/Passive: +2 \|        How the item expresses
  MODIFIERS**     Reactive/Triggered: +1 \|        the effect.
                  Command (Standard Action): +0 \| 
                  Spell Trigger (requires skill):  
                  −1                               

  **LIMITATION    Severe Restriction (range/target Each applicable
  DISCOUNTS**     limited): −1 \| Slot Dependency  limitation applies once.
                  (must be worn in specific slot): 
                  −1 \| Battery Reliance (inert    
                  without battery): −1 \|          
                  Alignment Lock (specific Way     
                  only): −1                        

  **WAY           Adaptive lane (Way 2): +1 \|     Derived from the Five
  MODIFIERS**     Sepulchral lane (Way 3): +1 \|   Ways documents.
                  Way 5 Suspended: +1 \| Way 5     
                  Reality Paradox: +2 \| Forge     
                  Calibrated mediation applied: −1 
  --------------------------------------------------------------------------

**The Battery System --- Revised**

Battery type is now determined by the Way and Lane of the Enabling
Component, not by a material category lookup. Every battery is a
specific alchemical compound that recharges according to its planar
expression.

  -------------------------------------------------------------------------------------------------------------------
  **Battery Type** **Way + Lane** **Recharge**      **Capacity**      **Drip Rate**              **Typical Material**
  ---------------- -------------- ----------------- ----------------- -------------------------- --------------------
  **Generative     Way 2          Short Rest        Medium            Consistent                 World Tree
  Font**           Generative     (biological                                                    heartwood, troll
                                  healing cycle)                                                 gland, regenerating
                                                                                                 tissue

  **Propagative    Way 2          Very fast ---     Low               Spikes on use              Mycelium network
  Net**            Propagative    draws from                                                     fragment, hive
                                  environment                                                    organ, fungal
                                  continuously                                                   network crystal

  **Consumptive    Way 2          Long Rest         Medium-High       Accelerates under stress   Predator heart, apex
  Burn**           Consumptive    (metabolic cycle)                                              gland,
                                                                                                 combustion-biology
                                                                                                 organ

  **Mineral        Way 3 Mineral  Extremely slow    Very High         Ultra-stable, never spikes Fossil bone, ancient
  Permanence**                    --- geological                                                 crystal, geological
                                  pace (weeks)                                                   mineral deposit

  **Preservative   Way 3          Slow --- identity High              Perfectly stable           Amber fragment,
  Hold**           Preservative   stasis (Long                                                   preserved spirit
                                  Rest, some                                                     vessel, stasis
                                  require Synod                                                  compound carrier
                                  bleed zone)                                                    

  **Channeled      Way 4          Depends on fuel   Fuel-limited      Infrastructure-dependent   Boiler crystal,
  Industrial**     Channeled      source (replenish                                              pressure vessel,
                                  fuel to recharge)                                              steam accumulator

  **Calibrated     Way 4          Slow ---          High              Precise --- never          Singing stone, Data
  Geometric**      Calibrated     geometric charge                    over-drains                crystal (F-15),
                                  accumulation                                                   Spire fragment
                                  (Long Rest)                                                    (F-13)

  **Propagated     Way 4          Self-sustaining   Self-sustaining   Chain-dependent --- stable Grid crystal (F-05),
  Chain**          Propagated     once initiated OR or one-use        until chain breaks         Clockwork mechanism
                                  none (fully                                                    (F-06)
                                  discharges)                                                    

  **Resolved       Way 5 Resolved Does not recharge Fixed (set at     Stable until depleted      Echo crystal (P-01),
  Echo**                          --- fixed charge  creation)                                    Prophecy stone
                                  depletes to zero                                               (P-02)

  **Contested      Way 5          Probabilistic --- Random variance   Unpredictable              Casino dust (P-05),
  Field**          Contested      each rest: roll                                                Karma crystal (P-06)
                                  1d6, recharge on                                               
                                  4+ (Standard), 3+                                              
                                  (Awakened)                                                     
  -------------------------------------------------------------------------------------------------------------------

**Slots, Tiers, and Wand Architecture**

  ----------------------------------------------------------------------------------
  **Item Tier**    **Slots**   **EML       **Default         **Notes**
                               Ceiling**   Isolation**       
  ---------------- ----------- ----------- ----------------- -----------------------
  Tier 1 (Simple)  2--3        EML 2       Each slot fully   Charms, simple focii,
                                           isolated          minor tools

  Tier 2           4           EML 4       Isolated by       Longsword, wand,
  (Standard)                               default           helmet, standard
                                                             equipment

  Tier 3           6           EML 6       Isolated by       Full plate, composite
  (Professional)                           default           bow, complex devices

  Tier 4 (Master)  8           EML 8       May be linked     Staves, high-quality
                                           with Forge        armor, masterwork items
                                           Calibrated        
                                           component         

  Tier 5           10          EML 10+     Linked            Legendary items,
  (Pinnacle)                               architecture      artifacts, Ascended
                                           possible          relics
  ----------------------------------------------------------------------------------

  -----------------------------------------------------------------------
  *WAND ISOLATION: Wands installed in a staff are isolated by default ---
  Wand A does not interact with Wand B unless a Forge Catalyst component
  is installed to bridge them. This allows a staff to function as a
  library of distinct effects (3.5-style spell stave). Bridge
  installation requires a Forge Calibrated+Interfacial component in an
  Enabling Component slot. The bridge determines which two wands interact
  and how.*

  -----------------------------------------------------------------------

**Way 3 Compound Classes --- Stabilization Items**

Synod-primary compounds produce item effects through stabilization,
preservation, arrest, and information permanence rather than damage or
condition delivery. All Way 3 compounds are Enabling or Active
Components in item slots.

  ------------------------------------------------------------------------------------------------
  **Compound       **Lane Combination**        **Slot Type**    **Mechanical         **CML Floor**
  Class**                                                       Effect**             
  ---------------- --------------------------- ---------------- -------------------- -------------
  **Preservative   Synod                       Active           Target biological:   Formation
  Compound**       Preservative×Preservative   (Preservation)   all biological       Stage of
                   or Preservative×Mineral                      processes arrested   dominant
                                                                (including aging,    S-isotope
                                                                wound progression,   
                                                                disease) for CML × 2 
                                                                hours. Condition     
                                                                track frozen. Target 
                                                                material: condition  
                                                                track cannot move    
                                                                downward while       
                                                                active.              

  **Inhibitory     Synod Inhibitory×Inhibitory Active           Suppresses all Way 2 Stage + 1
  Compound**       (at low Stage) or           (Counter-Font)   Propagative and      (Inhibitory
                   Inhibitory×Mineral                           Generative           is complex)
                                                                expressions within   
                                                                (Formation Stage × 5 
                                                                ft) radius.          
                                                                Advantage on saves   
                                                                against biological   
                                                                conditions. Counters 
                                                                mutation and disease 
                                                                spread.              

  **Archival       Synod                       Enabling         Seals any            Stage + 1
  Seal**           Sepulchral×Preservative     (Information     information encoded  (Sepulchral
                                               Lock)            in the item against  modifier)
                                                                modification,        
                                                                forgery, or magical  
                                                                alteration. TN to    
                                                                access scales with   
                                                                Formation Stage.     
                                                                Cannot be altered    
                                                                short of physical    
                                                                destruction.         

  **Decay          Synod Inhibitory×Mineral    Active (Targeted Targeted biological  Stage × 2
  Accelerant**                                 Decay)           tissue degradation   (extreme
                                                                at Formation Stage   effect)
                                                                rate. Stage 1: years 
                                                                per round (surgical  
                                                                precision). Stage 3: 
                                                                hours per round.     
                                                                Stage 5: seconds per 
                                                                round. Non-selective 
                                                                at Stage 4+.         

  **Soul Stone**   Four-Way (S primary, V      Enabling (Soul   Complete soul        Stage 4
                   secondary, F catalyst, P    Archive)         storage vessel. Way  minimum
                   tertiary)                                    2 retrieval access   (four-Way
                                                                to soul content.     compound)
                                                                Archival Seal        
                                                                prevents             
                                                                modification. Full   
                                                                production process   
                                                                in                   
                                                                ÆC_Way3_Synod.docx   
                                                                Section V.           
  ------------------------------------------------------------------------------------------------

**Way 5 Compound Classes --- Probability Items**

Palimpsest-primary compounds produce item effects through outcome
determination, equilibrium manipulation, and chirality selection. They
do not produce effects --- they determine whether and which effects
occur.

  ------------------------------------------------------------------------------------
  **Compound      **Lane Combination**  **Slot Type**  **Mechanical        **CML
  Class**                                              Effect**            Floor**
  --------------- --------------------- -------------- ------------------- -----------
  **Fixed Outcome Palimpsest            Active (Fate   One specified       Stage + 1
  (Fate Lock)**   Resolved×Resolved     Lock)          outcome is          (Resolved
                                                       guaranteed for the  is complex)
                                                       next triggering     
                                                       event. No variance  
                                                       roll. TN =          
                                                       Formation Stage × 5 
                                                       to override with    
                                                       Way 3+5             
                                                       counter-compound.   

  **Probability   Palimpsest            Active         Random outcome on   Stage
  Field**         Contested×Contested   (Randomizer)   each use. Roll on   
                                                       the item\'s         
                                                       Probability Table   
                                                       (GM generates at    
                                                       creation based on   
                                                       source isotopes).   
                                                       Higher Stage =      
                                                       wider variance.     

  **Chirality     Palimpsest            Enabling       The item exists as  Stage + 1
  Lock**          Handed×Handed         (Version Lock) one of two possible (Handed
                                                       configurations. Its modifier)
                                                       properties are      
                                                       those of the        
                                                       selected            
                                                       configuration only. 
                                                       Requires complete   
                                                       reconstruction to   
                                                       switch              
                                                       configurations.     

  **Palimpsest    Palimpsest            Active         All divination and  Stage
  Dust Screen**   Resolved+Suspended    (Divination    fate-reading        
                  (natural precipitate) Block)         targeting covered   
                                                       subject: TN +       
                                                       Formation Stage ×   
                                                       4. Area version:    
                                                       (Formation Stage ×  
                                                       10 ft) radius.      
                                                       Lasts until         
                                                       physically removed  
                                                       or dissolved.       

  **Fate Window** Palimpsest            Active         Creates a period of Stage
                  Resolved×Contested    (Temporal      genuine probability 
                                        Window)        openness in a       
                                                       determined          
                                                       situation.          
                                                       Duration: Formation 
                                                       Stage rounds.       
                                                       During window,      
                                                       Resolved outcomes   
                                                       can be redirected.  
                                                       After window:       
                                                       outcome Resolves    
                                                       permanently.        
  ------------------------------------------------------------------------------------

**Mutation Compounds --- Way 2 Adaptive Class**

Mutation compounds trigger the Mutation System. They are Active
Components that initiate the Strain→Nascent→Calcification cycle rather
than delivering a direct mechanical effect.

  ----------------------------------------------------------------------------------------------------
  **Compound Class**       **Lane Combination**  **Slot Type**   **Mechanical Trigger** **CML**
  ------------------------ --------------------- --------------- ---------------------- --------------
  **Directed Mutation**    Way 2                 Active          On contact or hit:     Stage + 1
                           Adaptive×Generative   (Mutation       Integrity save TN 10 + (Adaptive
                           with Forge Calibrated Trigger ---     CML. Failure: Nascent  modifier) − 1
                                                 directed)       Mutation from specific (Forge
                                                                 source V-isotope       Calibrated
                                                                 expression. Forge      precision) =
                                                                 Calibrated means the   Stage
                                                                 mutation is directed   
                                                                 toward a specific      
                                                                 template.              

  **Mutagenic Saturation** Way 2                 Active          On contact: Integrity  Stage + 1
                           Adaptive×Adaptive     (Mutation       save TN 15 + CML.      (Adaptive) + 1
                           (unmediated)          Trigger ---     Failure: Nascent       (Runaway) =
                                                 uncontrolled)   Mutation from Runaway  Stage + 2
                                                                 Transmutation table    
                                                                 (random V-isotope      
                                                                 expression). Without   
                                                                 Forge Calibrated:      
                                                                 multiple saves per     
                                                                 extended exposure.     

  **Anti-Proliferative**   Way 3 Inhibitory      Active          Suppresses all         Stage
                           applied to Way 2      (Mutation       Propagative Font       
                           Propagative           Counter)        expressions. Arrests   
                                                                 ongoing mutation       
                                                                 cascade in Nascent     
                                                                 state (Purge           
                                                                 function). Does not    
                                                                 remove Calcified       
                                                                 mutations. TN =        
                                                                 Formation Stage × 3    
                                                                 vs. ongoing            
                                                                 mutation\'s CML.       
  ----------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------
  **STEP 4: LEGACY**

  -----------------------------------------------------------------------

The Legacy system is the item\'s alchemical expression deepening through
use. Every AP accumulated is the item\'s Way 5 Palimpsest probability
space narrowing --- the Contested space of possible Ascension Traits
becomes progressively more Resolved toward specific outcomes based on
the AP pattern established by the item\'s use history.

**Ascension Tiers --- Palimpsest Expression**

  --------------------------------------------------------------------------------
  **AP       **Tier Name**   **Palimpsest      **Emulsion   **What Changes**
  Range**                    State**           Slot**       
  ---------- --------------- ----------------- ------------ ----------------------
  0--49 AP   **UNATTUNED**   Contested --- all None         Item functions at base
                             Ascension                      specification. No
                             outcomes equally               Ascension Traits. Any
                             probable                       supported trait could
                                                            theoretically develop.

  50--99 AP  **AWAKENED**    Contested         None         Item can hold one
                             narrowing toward               Ascension Trait. The
                             Resolved ---                   AP pattern has
                             specific traits                constrained the
                             becoming more                  probability space.
                             probable                       Certain trait
                                                            categories are now
                                                            more probable based on
                                                            use history.

  100--199   **MASTERY**     Resolved ---      One Emulsion Item can hold two
  AP                         probability has   Slot         Ascension Traits.
                             crystallized      available    Emulsion Slot allows
                                                            one antithetical
                                                            emulsion. Item\'s
                                                            identity is Resolved
                                                            --- the Palimpsest has
                                                            made its selection.

  200+ AP    **PINNACLE**    Resolved          Two Emulsion Item can hold three
                             (permanent, Synod Slots        Ascension Traits and
                             Sepulchral seal   available    two Emulsions. The
                             applied)                       item\'s identity has
                                                            been claimed by the
                                                            Synod Sepulchral lane
                                                            as a permanent record.
                                                            It has a soul.
  --------------------------------------------------------------------------------

**Aberration --- The Suspended Failed Ascension**

An Aberration occurs when a proposed Ascension Trait conflicts with the
item\'s Resolved probability state. The Palimpsest rejects the
installation because the item\'s AP history does not support that trait.

  -------------------------------------------------------------------------
  **Condition**      **Way 5 State**    **Mechanical       **Recovery**
                                        Result**           
  ------------------ ------------------ ------------------ ----------------
  Proposed trait     Suspended --- the  The AP spent on    Attempt the
  contradicts        attempt is real    the Ascension      compatible trait
  item\'s primary    but cannot sustain attempt is         instead. Or
  Way expression     itself             refunded. The item invest in an
  (e.g., Verdant                        rejects the trait. Emulsion slot to
  Font Font-item                        A Suspended echo   hold the
  receiving a Synod                     of the trait       contradiction.
  Sepulchral trait                      remains ---        
  without Emulsion                      visible to Way 5   
  slot)                                 or Way 3 Analyzer  
                                        checks as a ghost  
                                        expression.        

  Proposed trait     Suspended --- the  The AP spent is    Only Way 5
  contradicts an     new trait          not refunded ---   Probability
  already-Resolved   conflicts with the it represents the  Field compound
  Ascension Trait    Resolved           failed attempt and or Reality
  (two traits that   probability state  the Palimpsest     Paradox emulsion
  cannot coexist)    established by the recording the      can reopen the
                     existing trait     conflict. A Minor  Palimpsest\'s
                                        Quirk is added to  Resolved state.
                                        the item as the    Extremely
                                        unresolved tension difficult.
                                        manifests.         

  Proposed trait     Contested --- the  The AP spent is    Change use
  contradicts the    probability was    refunded. No       pattern. Engage
  item\'s legacy use never narrowed     damage. The AP     the AP trigger
  pattern (e.g., a   toward this trait  pattern simply has conditions for
  blade that has                        not established    the desired
  only ever been                        the probability    trait category,
  used defensively                      for this trait.    accumulate AP in
  receiving an                                             that direction,
  aggressive combat                                        reattempt.
  trait)                                                   
  -------------------------------------------------------------------------

**The Emulsion Slot --- Four Catalyst Types**

The Emulsion Slot available at Mastery tier allows one antithetical
emulsion compound to be installed. The Biotic Paradox (Way 2 + Way 3)
and Reality Paradox (Way 1 + Way 5) require a Forge
Calibrated+Interfacial catalyst. The catalyst type determines the
emulsion\'s character.

  ---------------------------------------------------------------------------------------
  **Catalyst   **Forge       **Emulsion Character**      **Instability     **Formation
  Sub-type**   Lane**                                    Mode**            Stage
                                                                           Required**
  ------------ ------------- --------------------------- ----------------- --------------
  **Crystal    Forge         Geometric lattice           Shatters if       Stage 3
  Catalyst**   Calibrated    containment. Both           information load  minimum
               (F-13 through antithetical expressions    exceeds geometric (F-13/F-14).
               F-16)         held as simultaneous        capacity (too     Stage 4 for
                             information. High fidelity, many simultaneous F-15/F-16.
                             potentially brittle under   queries).         
                             query load. The Amber Lock.                   

  **Chemical   Forge         Chemical cycling medium     Bridge overload   Stage 3
  Catalyst**   Interfacial   continuously converts       when one          minimum.
               (F-09 through between antithetical        expression floods 
               F-12)         states. Experiential,       the cycling       
                             immersive character.        medium faster     
                             Subject to chemical         than the other    
                             degradation over time.      can absorb.       

  **Steam      Forge         Pressure boundary           Pressure loss --- Stage 2
  Catalyst**   Channeled     containment. Physically     if infrastructure minimum (most
               (F-01 through robust, mechanically        fails,            accessible).
               F-04)         consistent, requires active antithetical      
                             pressure maintenance. The   expressions come  
                             Iron Lung.                  into direct       
                                                         contact and       
                                                         annihilate.       

  **Volt       Forge         Electrical threshold        Bridge overload   Stage 3
  Catalyst**   Propagated    bridge. Neither             --- both states   minimum. Most
               (F-05 through antithetical state touches  push maximum      powerful and
               F-08)         the other --- both touch    simultaneously,   most
                             the Volt. Most              discharging       dangerous.
                             emotionally/energetically   rather than       
                             intense. The Galvanic.      converting.       
  ---------------------------------------------------------------------------------------

**THE SCHEMATIC SYSTEM --- CALIBRATED+CALIBRATED**

A Schematic is a Way 4 Calibrated+Calibrated expression --- the only
Forge combination that operates without physical substrate. It is the
documented procedure that makes a process reproducible by anyone trained
to the standard. The Ætheric Scrivener path produces Schematics. Every
other Artifice Path uses them.

  ----------------------------------------------------------------------------------------------------
  **Authority Level** **Who Can Use**  **TN          **Variance    **Yield**         **Institutional
                                       Reduction**   Reduction**                     Recognition**
  ------------------- ---------------- ------------- ------------- ----------------- -----------------
  **PRACTITIONER**    The practitioner −1            −1            Consistent within None --- personal
                      who wrote it +                               one               knowledge only
                      personally                                   practitioner\'s   
                      trained                                      work              
                      apprentices                                                    

  **GUILD STANDARD**  Any practitioner −2            −2            Consistent yield  Guild
                      trained to the                               ±10% of           recognition.
                      Guild standard                               specification     Legally binding
                      and certified                                                  for product
                      for this process                                               certification.

  **INSTITUTIONAL**   Any practitioner −3            −3            Consistent yield  Institutional
                      holding                                      ±5% of            recognition.
                      institutional                                specification     Quality guarantee
                      certification                                                  carries legal
                      (Deepguard,                                                    weight in courts.
                      Praxis,                                                        
                      Sovereign                                                      
                      Exchange)                                                      

  **ARCHIVAL RECORD** Any practitioner −4            −4            Consistent yield  Mortis Aevum
                      with archive                                 ±2% of            Sepulchral seal.
                      access and                                   specification.    Cannot be
                      appropriate                                  Best achievable.  altered. Treated
                      clearance                                                      as historical
                                                                                     fact in legal
                                                                                     proceedings.
  ----------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------
  **SCHEMATIC CREATION: PV Cost = 500 + (100 × Item PV ÷ 1,000) --- round
  up Creation Time = 1 week per 1,000 PV of documented item Prerequisite
  = Ætheric Scrivener path, Journeyman minimum for Guild Standard; Master
  for Institutional Materials = vellum/metal plate (Setting A), printed
  specification sheet (Setting B), dual-register document (Setting C)**

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  *THE LIVING SCHEMATIC: At Master Scrivener Rank 10+, a Schematic can be
  enchanted with Way 5 Contested+Generative expression --- the
  document\'s probability space remains live to new technique
  discoveries. Each successful use of the Schematic that produces a
  Breakthrough event can update the document. The Schematic learns from
  its own application. This is the Forge+Palimpsest combination in
  document form.*

  -----------------------------------------------------------------------

**THE CORRUPTION TRACK --- WAY 3 AS DEFAULT PRESSURE**

Every item in existence is subject to the Synod\'s stabilization claim.
The Synod patiently asserts that everything will eventually reach its
most stable state. For items, this manifests as the condition track. The
Forge mediation of the crafting process is what keeps the item from
immediately settling --- but that mediation requires maintenance to
sustain.

  --------------------------------------------------------------------------------
  **Condition     **Synod Expression**  **Recovery Method**      **Way
  Track**                                                        Participation**
  --------------- --------------------- ------------------------ -----------------
  **PRISTINE**    Forge mediation fully No recovery needed.      Way 4 Forge
                  overcoming Synod      Normal operation.        active, Way 3
                  Inhibitory pressure.                           Synod passive.
                  Item operates as                               
                  designed.                                      

  **WORN**        Synod Mineral and     Standard maintenance.    Way 3 Synod
                  Inhibitory beginning  Way 4 Forge Channeled    Mineral beginning
                  to assert. Minor      repair process. Cost:    to win ground.
                  structural settling.  10% of original PV.      

  **DAMAGED**     Synod Mineral         Artifice repair.         Way 3 Synod
                  claiming structural   Requires Synod           winning. Way 4
                  elements. Active      Inhibitory               Forge retreating.
                  Inhibitory pressure   counter-treatment        
                  on functional         (anti-corrosion) + Forge 
                  components.           Calibrated restoration.  
                                        Cost: 25% of original    
                                        PV.                      

  **BROKEN**      Synod has             Major Artifice work.     Way 3 Synod
                  significantly claimed Borderlands physical     dominant.
                  the item toward its   repair + Synod           Structural Way 4
                  stable inorganic      Inhibitory arrest +      Forge expression
                  state. Functional     Forge Channeled          largely lost.
                  components            reconstruction. Cost:    
                  compromised.          50% of original PV.      

  **DESTROYED**   Synod has completed   Cannot be repaired to    Way 3 Synod
                  its claim. Item has   original form. Only Way  Mineral endpoint
                  reached its stable    3 Synod Sepulchral can   reached. The
                  final state.          recover the item\'s      item\'s history
                                        record. Physical         is now a
                                        reconstruction requires  Sepulchral
                                        entirely new materials   record.
                                        at full PV.              
  --------------------------------------------------------------------------------

**THE SIX ARTIFICE PATHS**

Each Artifice Path is grounded in a primary Way expression. The Path
determines which aspects of item creation the practitioner specializes
in and how they interact with the Five Ways system.

  -------------------------------------------------------------------------------------
  **Path**        **Primary Way**          **Focus**             **Key Tier
                                                                 Capability**
  --------------- ------------------------ --------------------- ----------------------
  **Mundane       Way 1 (Borderlands) +    Non-magical items of  Master: produce items
  Artisan**       Way 4 (Forge Channeled)  exceptional physical  at the maximum
                                           quality. Masterwork   physical tier
                                           expression at Way 1.  derivable from the
                                                                 material. No magical
                                                                 components, but the
                                                                 physical precision is
                                                                 unsurpassed.

  **Appraiser**   Way 5 (Palimpsest) + Way Economic and social   Master: Legendary
                  3 (Synod Sepulchral)     valuation,            Provenance ---
                                           provenance, market    psychometry via Way 3
                                           analysis.             Sepulchral read of
                                                                 item history. Can
                                                                 determine Chirality
                                                                 Lock orientation of
                                                                 Palimpsest compounds.

  **Analyzer**    Way 5 (Palimpsest) + Way Identification and    Master: reads the full
                  4 (Forge Calibrated)     deconstruction of     Five Ways
                                           magical properties.   specification of any
                                           Reading the item\'s   item including
                                           Way participation.    Emulsion catalyst
                                                                 sub-type, Aberration
                                                                 ghosts, and AP
                                                                 pattern.

  **Ætheric       Way 4                    Creation of           Master: Archival
  Scrivener**     (Calibrated+Calibrated = Schematics, scrolls,  Record authority
                  Schematic) + Way 3       runic wards, and      Schematics. Living
                  (Synod Sepulchral)       enchanted documents.  Schematics (Way 5
                                                                 Contested expression
                                                                 allows update).
                                                                 Institutional
                                                                 certification
                                                                 capacity.

  **Alchemist**   Way 1 (Borderlands) +    Consumable compounds, Master: Soul stone
                  Way 2 (Verdant Font) +   potions, elixirs,     production (four-Way
                  Way 3 (Synod)            salves. All five Ways compound). Biotic
                                           as working material.  Paradox consumables.
                                                                 Full mutation compound
                                                                 class. Way 5
                                                                 chirality-controlled
                                                                 pharmaceutical
                                                                 synthesis.

  **Enchanter**   Way 4 (Forge) + all      Permanent enchanted   Master: Emulsion
                  other Ways as Active     items. Slot           installation at
                  Component sources        installation, EML     Mastery tier. Reality
                                           management, Emulsion  Paradox item
                                           installation.         construction. Pinnacle
                                                                 tier item
                                                                 architecture.
  -------------------------------------------------------------------------------------

**SETTING C LANGUAGE --- ITEMS**

Item descriptions in Tessera use the three-register language system
established in the Five Ways Framework. A complete item spec in Setting
C uses spiritual/common names for the nouns and formal codes as
precision qualifiers.

+-----------------------------------------------------------------------+
| **EXAMPLE ITEM SPECIFICATION --- Setting C Synthesis:**               |
|                                                                       |
| **Steel Hunting Blade (Journeyman Grade)**                            |
|                                                                       |
| Core: CP-10 steel --- strong Bedrock character organized by the       |
| Engine\'s nature. Stage 2 formation, clean sample. Damage: 1d8        |
| (tensile tier). Soak contribution: 2. Weight: Standard.               |
|                                                                       |
| Active Component (Slot 1): Cordyceps Tincture --- V-07 expression,    |
| Stage 2 formation. Consumptive+Propagative character. On a telling    |
| hit, the target gains 1 Strain (Verdant Font, Fauna/Myco source). TN  |
| 12 Integrity save or begin accumulating toward Nascent Mutation if    |
| Strain track hits threshold.                                          |
|                                                                       |
| Enabling Component (Battery): Hunt\'s Heart --- V-05 Fauna primary,   |
| Long Rest recharge. Consumptive battery. Powers the Cordyceps Active  |
| Component. Innate alignment: the steel\'s Borderlands secondary and   |
| the Hunt\'s Way 2 Consumptive are compatible.                         |
|                                                                       |
| EML: highest CML (CML 2, Cordyceps Tincture at Stage 2) + floor((1    |
| active − 1) ÷ 4) = EML 2.                                             |
|                                                                       |
| Legacy Triggers: \[AWAKENED\] Strike an apex predator with a killing  |
| blow (Consumptive, The Hunt). \[MASTERY\] Pursue and bring down prey  |
| that has fled a full encounter (Propagative persistence).             |
+-----------------------------------------------------------------------+
