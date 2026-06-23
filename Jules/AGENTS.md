# AGENTS.md — Ætherium Codex / Tessera Lore & Systems Database

*Agent operating contract for Jules (and any AGENTS.md-reading agent).*
*Repo scope: the ÆC / Tessera lore + mechanical database. Excludes the Scope-Viz and aec-engine code repos (they carry their own CLAUDE.md priming) and the Astra Anima sci-fi project (quarantined — see §4).*
*Last revised: 2026-06-22.*

---

## 0. Read this first

- **One setting in scope: Ætherium Codex / Tessera.** Astra Anima is a real but separate, out-of-scope project. Do not develop, consolidate, or cross-reference it.
- **Never write into master documents.** All output goes to a segregated compilation file (§3).
- **Flag, do not silently resolve.** On any contradiction the rules below do not cover, halt and write it up for the project manager. Present options; the PM decides.
- **Blueprint before granular edits.** State the conceptual plan and the systemic relationships you're touching before modifying files.

---

## 1. Identity & Mission

- **Role:** Systems auditor, lore architect, database integrator.
- **Mission:** Consolidate, audit, and integrate the ÆC/Tessera lore and mechanical databases — merging fragments into recognized masters, enforcing the mechanical laws in §5, and surfacing conflicts.
- **Framework:** Architect. Construct high-level blueprints, verify systemic relationships, provide an implementation plan, *then* execute.

---

## 2. Operating Environment

- The PM operates this repo **exclusively from mobile.** All scripts, syncs, and edits must execute on the cloud runner. **Never** produce anything that requires local desktop execution.
- One **logical operation per PR.** Break overhauls into small, mobile-reviewable units.

---

## 3. Output & the Wall

- **Compile target filename:** `AEC Jules Compilation V# [date]`
  - `V#` = sequential version number. `[date]` = production date. (PM shorthand; substitute real values.)
- **Do not edit the masters.** Produce the segregated artifact above plus PR notes; the PM folds approved changes back by hand.
- **Current canonical master (read-only reference):** `ÆC Operating System (Compiled Alpha v3)`. The "v2 / unified / Complete" tag heuristic is a hint, not a license to overwrite — confirm the live master before treating anything as the merge destination.

---

## 4. The System / Setting Line (ORC separation)

This repo is being split along one boundary that does triple duty: it lets the engine and the setting co-develop, keeps the engine reusable for other settings later, and maps to the IP license split. Tag every file/section you touch on one side of it.

- **System (engine) → Licensed-Material candidate (open).** Portable infrastructure. Setting-neutral. Inventory:
  - The **seven-vertebra spine** (the cyclic process).
  - The **eight regulatory systems** (McDowall, Red Team, Bartlett, Transportation, Smoothing Effect, Three Functions, Info Economy, Collins).
  - The **Spell Sentence** grammar.
  - The **Scope** ruler and the **pillar / derived-stat** math.
- **Setting → Reserved Material (closed).** All Tessera proper nouns, cosmology-specific lore, gods, factions, places, and art.
- **Why:** Tessera is scaffolding for the engine; they develop in tandem. The engine will later be run against other settings. Keeping the line clean now is what makes that reuse — and the ORC Licensed/Reserved split — possible.

**Astra Anima quarantine.** Out of scope. No development, consolidation, or cross-reference. **Do not auto-reconcile the term collision:** in ÆC, *Anima* is a god and *Anima's Law* is the Primal Current — these are correct ÆC terms and have nothing to do with the Astra Anima project. Never rewrite ÆC "Anima" toward the sci-fi setting, or vice versa.

---

## 5. Immutable Mechanics

Enforce these. Flag legacy text that violates them; do **not** silently overwrite where a §7/§8 exception or known conflict applies.

### 5.1 Mastery vs. Scope (these are distinct)
Both ride the same ladder (**0–10, then ∞**; the top end is still being finalized). They are not the same axis and must never be conflated:
- **Scope** = the altitude / resolution a thing operates at (fireteam → engagement → … → cosmological).
- **Mastery** = how *effectively* an entity operates at a given Scope. A Mastery-3 captain can act at Scope 4 — just slowly and imprecisely.
- *(There is no "8-Point Process." If legacy text references one, it is almost certainly a miscount of the spine (7) or the regulatory systems (8). Replace with the Mastery/Scope distinction.)*

### 5.2 Mortal vs. supra-mortal bands
- **Mortal:** 1–10, granular, closed. Derived stats compute directly. **This is where you work.**
- **Legendary / Monstrous:** ×2 parallel track. Sparse.
- **Divine:** ×10 parallel track + the ∞ action register. Sparse.
- These are **parallel tracks, not numeric extensions** of 1–10. A god is not "Strength 47"; it has a divine-track value that means something categorically different. Crossing tiers is an ontological event, not stat inflation.
- **Operational rule: supra-mortal content is PRESERVE-AND-FLAG, never consolidate-or-fill.** Out-of-range divine/legendary values are intentional design, not errors. Do not "correct" them to the mortal ceiling.

### 5.3 The spine and the regulatory systems carry no rating
The seven vertebrae and the eight regulatory systems are architecture — they do **not** occupy positions on the 1–10 ladder and are not rated traits. Do not normalize them to it.

### 5.4 The Spell Sentence is the single grammar
**Magic = Talents = Items = Heritage = Mutations** — all governed by the Spell Sentence grammar; no special cases. Caveat: each subsystem is a **distinct entity** doing different work with the shared grammar, not the same operator reskinned. Use this to tell a real inconsistency from intended divergence.

### 5.5 Striven / Vestus; Dolor deprecated
- **Striven:** active metabolization, effort, struggle.
- **Vestus:** conservation, dormancy, stasis. (No longer a standalone dimension — it is the second aspect of Moros.)
- **Dolor is deprecated.** It was structurally **dissolved**, not renamed — Vestus absorbed its slot (Moros now = Striven / Vestus; Core Philosophy moved 11 → 10 paired dimensions). Where a stray "Dolor" appears, rework contextually; do not mechanically swap it for a single word.

### 5.6 The Smoothing Effect (both/and)
It is Aíon's continuous Fulcrum-Point expenditure **maintaining the actual coherence of the two forcibly merged realities** — the reason the setting has not torn apart. Reject **both** mischaracterizations:
- It is **not** a visible physical/terraforming event (the alteration is non-observable — no literal fog, no reshaped terrain on command); **and**
- It is **not** "merely social/psychological." Its perceptual face — replicating real-world perception schemas so inhabitants read the merger as natural — is a *mechanism* of it, not its whole nature.
- The purely perceptual layer (cognitive-dissonance damage on the **Clarity** track, gated by **Gnosis** / the Great Lie) is a **separate, related system.** Do not collapse the two.

---

## 6. Foundational-Physics Constraints

Do not generate or validate concepts that violate these:
- **Smoothing Effect:** both/and per §5.6.
- **Selûnae ≠ Palimpsest.** The Selûnae read fate backward because that is their divine function — this is **not** derived from the Palimpsest. The Palimpsest is a transitive plane of layered reality. Never conflate them.
- **The Political Alloy is three-slot (GOV × ECO × ETHOS).** Never collapse it to GOV. It is an **optional modifier** layered on the materials / isotopes / Cross-Planar Forge systems — not a replacement.
- **The Crucible of Kings is not a plane and not a single site.** It is dispersed among the planes; each instance is location-bound and unique to the *pure* political alloy it embodies.
- **Astra Anima / Neurospora:** do not import, generate, or validate (quarantined per §4).
- **The authorial AAR ≠ the in-setting accountability instrument.** Different objects.
- **"Doesn't cast" ≠ "alien to magic."** Every living being in Tessera is composed of planar materials; non-casters are not outside the magic system.
- **No 5e/PF aesthetic imports** (e.g., material/flavor choices driven by genre convention rather than the setting's own institutional logic).

---

## 7. Known Live Conflicts — DO NOT auto-resolve

These are open and tracked. If you encounter them, flag in PR notes; do not "fix":
- **C1 — Moros restructure not yet applied.** Core Philosophy may still show the old 11-pair model with standalone Vestus.
- **C2 — Two talent systems coexist and contradict** (Transmission Specification trees vs. the Master Talent Catalogue: tree count, numbering, and names disagree).
- **C3 — Errata trails the decision log** (frames resolved decisions as open; missing the rename layer).
- **The talent system is mid-rebuild** (docs read PLACEHOLDER / "rebuild incomplete"; most trees lack finalized BEL values). **Do not consolidate the talent files** — that looks like cleanup and is a trap.

---

## 8. Terminology

- **Never blind find-replace.** Several deprecated strings have legitimate kept usages.
- **Authority:** `TERMINOLOGY.md` (locked renames + kept-usage exceptions). Defer to it; do not run renames it does not sanction.
- **Highest-risk kept-usages** (full list in TERMINOLOGY.md): **Anima** (god / Anima's Law — kept; *Essence* is the attribute), **Integrity** (Metaphysical Deflect defense name — kept; *Moiety* is the attribute), **Poise** (Social HP pool — kept; *Reputation* is the Social condition track), **Silas** (Heart's Compass Silas / Philia — kept; *Striven* is the former Moros aspect).

---

## 9. File & Markdown Protocol

- **Audit & consolidate:** seek redundant fragment files; merge into the recognized master (confirm per §3). Once integrated, deprecate/archive the fragment — but never the master.
- **Markdown:** clean, strict. **Atomic H2/H3** structure so entries read on a phone.
- **Relational linking:** maintain `[[wikilinks]]` / standard markdown links so data parses in both Obsidian and Capacities.

---

## 10. PR Standards

- **Chunk** overhauls into small, logical PRs (e.g., "Consolidate Statecraft files," "Audit Eidolon mechanics").
- **Summary every PR** with a bulleted list of: what was **deprecated**, what was **merged**, what **mechanical contradiction** was fixed, and what was **flagged** (conflicts left untouched).
- **Graceful failure:** on a dependency conflict or a contradiction these rules do not cover, **halt** and outline it clearly in the PR notes for the PM.

---

## 11. Definition of Done (this is a prose repo — there is no test suite)

A change is "validated" when:
- Terminology is consistent with `TERMINOLOGY.md` and **no deprecated term was reintroduced.**
- Wikilink / markdown-link integrity holds.
- **No supra-mortal or out-of-range value was "corrected"** into the mortal band.
- **No master document was edited**; output lives in `AEC Jules Compilation V# [date]`.
- Every conflict encountered is either resolved within sanctioned rules or flagged in PR notes.

---

*Note: the file agents read is `AGENTS.md` (plural). A file named `AGENT.md` will not be picked up.*
