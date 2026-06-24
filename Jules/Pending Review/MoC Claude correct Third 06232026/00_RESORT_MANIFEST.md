# AEC Glossary Re-Sort — Manifest & Handoff
> 2026-06-23 · Re-classification of the v3 Jules digest set

## What this is
The six `AEC_Jules_*_v3` files were Jules's glossary-classification pass — one
`**Term**: gloss [Source: file]` per line, binned by category. The bins were wrong
in three compounding ways. This pass corrects placement, deduplicates, and re-cuts
into **seven** files (the original six minus Unsorted, plus Isotopes and Rejects).

## Corrected hierarchy (the rule Jules should sort by)
- **Engine layer** — the generative grammar everything references:
  - `SRD` — Spell Sentence + effects list, conditions, pools/attributes/defenses,
    resolution, action-economy tags, delivery components, mutation/heritage system,
    item-creation *rules*.
  - `Isotopes` — **separated** but engine-layer. Identities, the combination
    interfaces (political-alloy positions where isotopes are an *option* on
    GOV×ECO×ETHOS, spell-sentence, item-creation), and forthcoming compounds.
- **Subsystem layer** (downstream of the engine, not peers that absorb it):
  - `Bestiary` — creature subsystem: type taxonomy, planar subtypes, companion/bond
    rules, containment/care, harvesting, mutation-as-applied-to-creatures, plus named
    creature instances.
  - `Item Compendium` — item subsystem: condition tracks + item instances.
- **Consumer layer**:
  - `Setting Bible` — world, cosmology, divinity, institutions, geography, narrative
    framing.
  - `Adventure Generator` — hooks, sites, generator machinery.
- `Rejects` — parse artifacts, removed from circulation.

## The three failures corrected
1. **~5× duplication (mechanical).** Bestiary was 801 entries / 86 unique (89% dupes);
   SRD 629/110; Item 206/36. Root cause is upstream: the source corpus contains TWIN
   files and Jules emitted one entry per source occurrence —
   `1. SRD v3 Combined (2).md` + `(cutting copy).md` (both 708);
   `ÆC Isotopes Combined.md` + `Combined v2.md` (both 527); and every isotope file
   existing twice (`AC_SRD_Isotopes_X` *and* `ÆC_Complete_Isotope_Reference_X`).
   → **ACTION FOR JULES: dedupe the source corpus before the next compile.**
2. **Spell-Sentence grammar shredded across 3 buckets.** Damage, Healing, Create,
   Flight, Enhanced Trait, Affliction, etc. lived simultaneously in SRD + Bestiary +
   Item. They are the shared vocabulary; the glossary definition is SRD; a creature
   that flies or an item that heals is an *application*, not a separate term.
   All collapsed to SRD.
3. **Setting Bible starvation.** It held 18 narrative-theory terms; the actual world
   (planes, economy, institutions, the operational Fronts) was stranded in Unsorted.
   Repopulated.

## Flagged judgment calls (review these)
- **⚙ EMULSION** routed to `Isotopes` as a material-formation type, but its gloss
  ("antithetical planes forced together by Hidden Forge catalyst; cosmological event")
  also names the core Tessera merger. → It likely also needs a `Setting` entry as the
  founding cosmological premise. Not duplicated automatically.
- **Planes are double-keyed.** Register entries `Borderlands (W1)`, `Verdant Font (W2)`,
  `Synod of Endings (W3)`, `Palimpsest (W5)` → `Isotopes` (they define isotope families
  + phase wheels). The places `The Borderlands`, `Verdant Font`, `Synod of Endings`,
  `Palimpsest` → `Setting`. Note: **W4 is not a gap** — it is the Hidden Forge (the F-##
  isotope family); it simply isn't tagged "(W4)" in the digests.
- **Fey** routed to `Bestiary` as creature instances, but the Elder/Lost/Newborn
  story-ghost split is load-bearing Setting-A / Setting-B cosmology and should also be
  reflected in `Setting`.
- **`All 64 political alloy music cores`** routed to `Setting` (Zoetrope / Musical
  Alloy), but the alloy *mechanic* is engine-layer — cross-reference, don't move.

## Source-extraction debt this surfaced (NOT a sorting problem)
- **Bestiary and Item are nearly empty of instances.** After grammar→SRD and material→
  Isotopes, Bestiary holds creature *rules* + a handful of archetypes; Item holds only
  the four condition tracks. The real instances are not in these digests — they live in
  `Cephalarch_Notes`, `Vespidans_Notes`, `Eidolon_Notes`, `ÆC_Novice_Magic_Items`,
  `ÆC_Iconic_Spells`. These need proper extraction.
- **Trapped content (55 Rejects).** Faction/organization templates, the Sun God-King
  deity entry (Luxos / Ignislor — Sun/Fire/Leadership), and the companion-bond table
  were scraped as stat-block COLUMN HEADERS (`Crops`, `Uniforms`, `Portfolio`,
  `Aspects`, `What`, `Role`…). Reject the labels; re-extract the templates as structured
  records from `Merged Colleges & Divinity` and `Aetheric pet system unified`.
- **Vespidans** appear only as the fragment "Far East snake-like people" (+ a eusocial-
  colony gloss). Re-extract as a proper creature entry.

## Files
| File | Unique terms |
|---|---|
| AEC_SRD_v3_resorted.md | 121 |
| AEC_Isotopes_v3_resorted.md | 23 |
| AEC_Bestiary_v3_resorted.md | 55 |
| AEC_Setting_Bible_v3_resorted.md | 28 |
| AEC_Adventure_Generator_v3_resorted.md | 24 |
| AEC_Item_Compendium_v3_resorted.md | 5 |
| AEC_Rejects_v3_resorted.md | 55 |
