# Life 101 v2 — Import Guide

A complete, audited rebuild of the **Answering Questions + Life 101** RemNote base. Same intent, same voice, same knowledge — with every known error fixed, every mandated gap filled, and every card checked to import cleanly. **2,186 cards across 11 files.**

Built and verified August 2026. The original export remains untouched at `life-101/source/`.

---

## How to import into RemNote

1. In RemNote: **Import → Markdown**, one file at a time. Each file becomes one document; `::` lines become cards; `{{…}}` become clozes.
2. Import into a **fresh folder named "Life 101 v2"** so nothing collides with your existing rems.
3. **Archive, don't delete, the originals** until you've reviewed the new set for a few weeks.
4. **Do not import the old `Answers for My Kids RemNote Flashcards`** (v1). It is fully superseded by Kids Questions v4 Part A, and it carries the wrong lunar period — importing it would reintroduce a contradiction.

Every file has been verified free of: banned export delimiters (`↔ → ← ;; >>>`), unbalanced `{{ }}` braces, duplicate prompts (within *and* across files), and clozes whose answers leak into their own prompt.

---

## File inventory

| File | Cards | Covers |
|---|---:|---|
| The Foundational 200 v2 — Part A (Cosmos, Earth, Body) | 112 | Physics and cosmology rebuilt to full strength, Earth and biology, human physiology |
| The Foundational 200 v2 — Part B (Mind, Biases, Math, Tools) | 140 | Psychology, the 15-bias vocabulary, probability incl. Bayesian updating, thinking tools with patch-pairs |
| The Foundational 200 v2 — Part C (History, Civics, Economics, Tech, Ethics, Practice) | 172 | History as information-storage upgrades, expanded civics, economics, technology, ethics, practical competence |
| Kids Questions v4 — Part A (The Physical World) | 221 | Cosmos, matter and forces, weather and optics, the body, animals — all broken cards repaired |
| Kids Questions v4 — Part B (Technology, Math, Mysteries, Society, Philosophy) | 202 | Converted from prose: how things work, math, everyday mysteries, society, the big questions |
| Kids Questions v4 — Part C (Growing Up, Genetics, Justice, Money, Thinking) | 126 | Converted from prose: puberty and feelings, genetics, justice and ethics, money, media literacy |
| Life Skills v2 — Personal Finance | 294 | Credit, banking, debt, emergency fund, taxes, estate, and a completed retirement module |
| Life Skills v2 — Housing & Vehicles | 252 | Buying, renting, home systems and maintenance, car buying, maintenance, insurance |
| Life Skills v2 — Emergency Preparedness & First Aid | 224 | LA evacuation plan, wildfire and smoke, earthquake, fire, first aid, home and digital security |
| Life Skills v2 — Food & Health | 223 | Food safety, cooking technique, nutrition, groceries, insurance, care navigation, mental health |
| Life Skills v2 — Relationships & Productivity | 220 | Communication, boundaries, friendship, romance, repair, endings, habits, focus, procrastination |

---

## Tag legend

- **`#volatile`** — a number that expires. Verified current as of 2026; re-check yearly.
- **`#us`** — United States–specific law, tax, or institution. Not portable to other countries.
- **`#safety`** — verified against authoritative guidance (USDA, American Heart Association, Red Cross, FEMA, EPA/AirNow, 988) in August 2026.
- **`#theory`**, or an answer opening with `Theory:` / `Contested:` — the claim is a hypothesis or is actively disputed. The hedge is part of the card.
- **`#high-frequency`** — your own tag, preserved: the cards you expect to actually need.
- **`#verify-personally`** — depends on *your* home, vehicle, or family. Confirm against reality before trusting it.

---

## Maintenance schedule

- **Every January:** review all `#volatile` cards. Contribution limits, tax brackets, and thresholds change annually.
- **Every year:** actually drive one of the evacuation routes. A route that exists only on a card has never been tested.
- **Every two years:** re-check `#safety` cards against current guidance. First-aid protocols and AQI recommendations do get revised.
- **Whenever you move, change vehicles, or your household changes:** revisit every `#verify-personally` card.

---

## What changed from v1

**Safety fixes**
- Ground poultry now correctly taught at 165°F — the old card taught 160°F for all ground meat, which undercooks chicken and turkey.
- The self-contradicting 2-2-2 rule is retired and replaced by one reconciled canon (2-hour room-temp limit, two-stage cooling, 3–4 day storage, 165°F reheat), with a card explaining the retirement.
- Added the entire missing response half: hands-only CPR, choking, severe bleeding, stroke (FAST and BE-FAST), earthquake's first sixty seconds, home fire and PASS, shelter-in-place.
- Added wildfire and smoke — the largest gap in an LA-focused plan: red-flag warnings, order-vs-warning terminology, go-time triggers, N95/P100, AQI action thresholds, defensible space.
- Added the mental-health crisis protocol: 988, warning signs, and how to support someone.

**Corrections**
- The I-105 rationale no longer claims post-Northridge construction (the freeway opened three months *before* Northridge); the honest rationale — newest freeway, most modern standards — replaces it, and the false 405/10 interchange collapse claim is gone.
- Added the compound earthquake-plus-tsunami scenario the plan never handled.
- The vacated $43,888 exempt-salary threshold is removed; all tax figures re-verified for 2026.
- The reversed Roth phase-out card, the `{{$}}` orphan clozes, the mangled oil-check card, the FAST/PASS/Eisenhower cards destroyed in export, and the Deontology card's pasted AI scaffolding are all repaired or rewritten.
- Second Law now says entropy *never decreases*; the "General Relativity" card that actually defined gravity is renamed and a real GR card added.

**Completions**
- All 109 kids' questions that were never converted from prose are now cards — technology, math, everyday mysteries, society, philosophy, growing up, justice, money, and media literacy.
- The retirement module the author flagged "(needs work?)" is finished: 401(k), Social Security, RMDs, asset allocation, index funds and expense ratios, safe withdrawal rates.
- Compounding is now taught positively (Rule of 72, growth over decades), not only as a debt trap.
- Bayesian updating added — the formal engine the whole epistemology implied but never contained.
- Cooking technique, procrastination, the apology-when-you-were-wrong script, relationship endings, and workplace basics all added.

**Structural**
- One canonical money priority order replaces the two that contradicted each other, with a card explaining how the emergency-fund phases and contribution order interlock.
- Auto insurance moved out of Tax Planning; health insurance's two competing treatments merged into one.
- Contested claims labeled throughout: the marshmallow test, Love Languages, love's 6–24 month chemistry window, bear torpor, yawning's brain-cooling hypothesis, the obstetric dilemma.
- Every generic prompt stem ("Why it matters", "How it works") is now topic-scoped, so no card is ambiguous when it surfaces alone in review.
