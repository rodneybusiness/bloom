# Life 101 v2 — Import Guide

A complete, audited rebuild of the **Answering Questions + Life 101** RemNote base, plus the connective **spine** deck that the original never had. Same intent, same voice, every known error fixed, every card checked to import cleanly. **2,528 cards across 14 files.**

Built and verified August 2026. The original export remains untouched at `life-101/source/`.

---

## How to import into RemNote

These files are in **native RemNote format** — indentation-based hierarchy, no markdown bullets, and RemNote's six card delimiters. Import by **copy-paste**: open a file, select all, paste into an empty RemNote document. Hierarchy and card types are preserved automatically.

The six card types in use:

| Symbol | Type | Direction | Used for |
|---|---|---|---|
| `::` | Concept | bidirectional | core definitions |
| `;;` | Descriptor | forward only | properties of a parent concept |
| `>>` | Basic | forward only | why / how / application |
| `{{ }}` | Cloze | — | formulas and verbatim only |
| `>>>` | Set | — | unordered lists |
| `1. >>>` | Sequence | — | ordered steps |

1. Paste one file at a time into its own document.
2. Import into a **fresh folder named "Life 101 v2"** so nothing collides with your existing rems.
3. **Import the two spine files first** — see "What the spine deck is for" below. They are the smallest files and carry the most transferable value.
4. **Archive, don't delete, the originals** until you've reviewed the new set for a few weeks.
5. **Do not import the old `Answers for My Kids RemNote Flashcards`** (v1). It is fully superseded by Kids Questions v4 Part A, and it carries the wrong lunar period — importing it would reintroduce a contradiction.

Every file is validated by `validate_cards.py` in this folder, which checks card-type distribution against the design targets and flags markdown bullets, legacy arrow delimiters, unbalanced braces, orphaned descriptors, duplicate prompts, answer-in-prompt leaks, yes/no recognition cards, and over-length answers. The set currently passes with zero critical issues.

---

## What the spine deck is for

An audit of the domain decks found something worth naming: they held roughly 2,200 individually excellent cards and almost no structure. Only 12% of cards carried a *why*. Only **2 cards out of 986 Life Skills cards referenced a Foundational 200 concept** — the thinking-tools half and the practical half were hermetically sealed from each other. And there were zero application-level cards: everything fired at review time, nothing at decision time.

Reviewed alone, that set installs a warehouse of facts and no way to navigate it.

The two spine files answer that. **The Spine** carries the seven cross-cutting patterns that hold the whole base together, each with the mechanism that makes it true and three instances that index real cards elsewhere in the set — plus the five identities that weld two domains into one mechanism. **Transfer and Triggers** carries each thinking tool into the concrete situations where it bites, then runs the other direction with situation-first cards ("you are in the dealership finance office and they've started talking in monthly payments — what applies?") that name the specific frameworks to reach for.

They are about 6% of the cards and carry most of the transferable value. **Review the spine daily, even when the domain decks are on a slower schedule.** The domain facts are lookupable; the structure is not.

---

## File inventory

| File | Cards | Covers |
|---|---:|---|
| **Life 101 v2 — The Spine (Patterns and Identities)** | 93 | The unifying thesis, the seven patterns, the meta-pattern, the five identities |
| **Life 101 v2 — Transfer and Triggers** | 79 | Thinking tools carried into practice; situation-first retrieval cards |
| Life 101 v2 — AI and Digital Literacy | 45 | What an LLM is, hallucination, verification, deepfakes and voice cloning, scams, kids and AI |
| The Foundational 200 v2 — Part A (Cosmos, Earth, Body) | 112 | Physics and cosmology, Earth and biology, human physiology |
| The Foundational 200 v2 — Part B (Mind, Biases, Math, Tools) | 140 | Psychology, the bias vocabulary, probability incl. Bayesian updating, thinking tools |
| The Foundational 200 v2 — Part C (History, Civics, Economics, Tech, Ethics, Practice) | 172 | History as information upgrades, civics, economics, technology, ethics, competence |
| Kids Questions v4 — Part A (The Physical World) | 221 | Cosmos, matter and forces, weather and optics, the body, animals |
| Kids Questions v4 — Part B (Technology, Math, Mysteries, Society, Philosophy) | 202 | How things work, math, everyday mysteries, society, the big questions |
| Kids Questions v4 — Part C (Growing Up, Genetics, Justice, Money, Thinking) | 162 | Puberty, consent and body autonomy, bullying, substances, grief, genetics, justice, money, media literacy |
| Life Skills v2 — Personal Finance | 335 | Credit, banking, debt, emergency fund, retirement, taxes, estate, disability insurance, death administration, identity theft, salary negotiation |
| Life Skills v2 — Housing & Vehicles | 266 | Buying, renting, home systems, car buying and maintenance, insurance |
| Life Skills v2 — Emergency Preparedness & First Aid | 224 | Evacuation, wildfire and smoke, earthquake, fire, first aid, home and digital security |
| Life Skills v2 — Food & Health | 245 | Food safety, cooking technique, nutrition, insurance, care navigation, mental health, aging parents and caregiving |
| Life Skills v2 — Relationships & Productivity | 232 | Communication, boundaries, friendship, romance, repair, endings, habits, focus, procrastination |

---

## Tag legend

Tags use RemNote's double-hash form (`##tag`), which creates real tag properties rather than plain text. Priority tags from the card-design system — `##core-concept`, `##big-picture`, `##connection`, `##confusing`, `##prerequisite`, `##practical`, `##high-frequency` — mark the cards worth extra review attention.

- **`##spine`** — the connective deck. Marks a card whose job is to hold other cards together rather than to teach a fact. Review these daily even when the domain decks are on a slower schedule.
- **`##volatile`** — a number that expires. Verified current as of 2026; re-check yearly.
- **`##us`** — United States–specific law, tax, or institution. Not portable to other countries.
- **`##safety`** — verified against authoritative guidance (USDA, AHA/Red Cross, FEMA, EPA/AirNow, FTC, 988) in August 2026.
- **`##theory`**, or an answer opening with `Theory:` / `Contested:` — the claim is a hypothesis or is actively disputed. The hedge is part of the card.
- **`##high-frequency`** — your own tag, preserved: the cards you expect to actually need.
- **`##verify-personally`** — depends on *your* home, vehicle, or family. Confirm against reality before trusting it.

---

## Maintenance schedule

- **Every January:** review all `##volatile` cards. Contribution limits, tax brackets, care costs, and thresholds change annually.
- **Every year:** actually drive one of the evacuation routes. A route that exists only on a card has never been tested.
- **Every two years:** re-check `##safety` cards against current guidance. First-aid protocols and AQI recommendations do get revised.
- **Whenever you move, change vehicles, or your household changes:** revisit every `##verify-personally` card.
- **After any marriage, divorce, birth, or death:** review every beneficiary designation. They override the will.

---

## What changed from v1

**Safety fixes**
- Ground poultry now correctly at 165°F — the old card taught 160°F for all ground meat, which undercooks chicken and turkey.
- The self-contradicting 2-2-2 rule retired, replaced by one reconciled canon, with a card explaining the retirement.
- The entire missing response half added: hands-only CPR, choking, severe bleeding, stroke (FAST and BE-FAST), earthquake's first sixty seconds, home fire and PASS, shelter-in-place.
- Wildfire and smoke added — the largest gap in an LA-focused plan.
- Mental-health crisis protocol added: 988, warning signs, how to support someone.

**Corrections**
- The I-105 rationale no longer claims post-Northridge construction; the false 405/10 interchange collapse claim is gone; the compound earthquake-plus-tsunami case is handled.
- The vacated $43,888 exempt-salary threshold removed; all tax figures re-verified for 2026.
- Reversed, mangled, and AI-scaffolded cards repaired throughout.
- Second Law now states entropy *never decreases*; the "General Relativity" card that defined gravity renamed with a real GR card added.

**Completions**
- All 109 kids' questions that were never converted are now cards.
- Retirement completed: 401(k), Social Security, RMDs, asset allocation, index funds, safe withdrawal rates.
- Bayesian updating added; compounding now taught positively as well as negatively.
- New modules: cooking technique, procrastination, apology and repair, relationship endings, workplace basics.

**This pass — structure and remaining gaps**
- **The spine deck** (149 cards): seven patterns, five identities, transfer cards, and trigger cards. Cross-domain references went from 2 to roughly 70.
- **Why-siblings** added to the load-bearing thresholds, so numbers can be re-derived rather than merely recalled — and where a number's provenance is actually folkloric (hydration formulas, the 8-week habit mark, the 90-minute focus block), the card says so instead of inventing a mechanism.
- **Disability insurance** — was zero cards, and the largest hole in the practical half.
- **Death administration** — the executor's actual job, including that beneficiary designations override the will.
- **Identity theft response**, **salary negotiation**, **aging parents and caregiving** — each previously absent.
- **Consent and body autonomy, bullying, substances, grief** added to the kids' deck.
- **AI and digital literacy** as a new file, including the family verification password against voice-clone scams.
