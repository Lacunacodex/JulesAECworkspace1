# ----------------------------------------------------------------------------

# RULE: rename / merge operations target `id`, NEVER the bare `label`.

#       `locked: true` terms reject any label-level find-replace.

#

# Two hazard classes:

#   homonym -> different things that share a word  (fix = unique id per domain)

#   alias   -> one thing mid-rename                (old name is a stale pointer)

# ----------------------------------------------------------------------------

  

terms:

  

  # --- HOMONYMS — collision made structurally impossible by id ---------------

  - id: god.anima              # the GOD on the Kanon/Anima axis

    label: Anima

    domain: psyche_schema

    locked: true

    hazard: homonym

    note: "NOT the attribute. Never rename. Never global-replace the word 'Anima'."

  

  - id: attr.essence           # the attribute (THIS is what the rename targets)

    label: Essence

    domain: character_sheet

    was: Anima                 # legacy label -> retire via id, not via text search

    hazard: homonym

  

  - id: dimension.silas        # live Heart's Compass / Philia dimension

    label: Silas

    domain: hearts_compass

    locked: true

    hazard: homonym

    note: "Collides with the RETIRED Moros aspect 'Silas'. Never blind-replace."

  

  # --- ALIASES — old name is a stale pointer; risk is half-finished migration -

  - id: attr.moiety

    label: Moiety

    was: Integrity             # retire 'Integrity' everywhere, deliberately

    hazard: alias

  

  - id: attr.elusivity

    label: Elusivity

    was: Acuity                # CONFIRM: is "Acuity (defense)" a separate keep?

    hazard: alias

  

  - id: skill.instinct

    label: Instinct

    was: Insight

    hazard: alias

  

policy:

  rename_by: id_only

  on_locked_label_replace: reject

  migration_done_when: "no `was:` label remains anywhere in the corpus"