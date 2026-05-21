# Wolves of Wand Street — Design Document Q&A

> This document captures all questions and answers needed to complete the Design Document.
> Organized by Design Doc section. All information is extracted from existing game materials.
> **Goal:** Maximize assessment score by addressing every criterion thoroughly.

---

## §1 · Target Experience

### Q1.1: What is the High Concept (Elevator Pitch)?

**A:** Wolves of Wand Street is a card-driven area-control game for 3–4 players set in a fantasy-tinged financial district where wizard-investors wage economic warfare over territories. Each round (~15 min total), players draw cards, accumulate Gold, deploy Investors, and clash for control of 13 territories — blending resource management, tactical combat, and hand management into a tight competitive experience. The game distills the fantasy of ruthless corporate raiders wielding both coin and arcane power to dominate a market-like map.

---

### Q1.2: What is the Fellowship (Social Dynamic)?

**A:** The game is a **3–4 player competitive** free-for-all with no teams or hidden traitors. Interaction is driven by **territorial adjacency** — you must expand into spaces your opponents control or covet. There is no passive play: every territory gained is taken from (or defended against) another player. The social dynamic encourages **temporary alliances of convenience** (e.g., two players cooperating to weaken a leader) while maintaining the understanding that all alliances are ultimately self-serving. The turn-order shuffle each round prevents permanent king-making dynamics.

---

### Q1.3: What is the Challenge?

**A:** The game presents two layers of challenge:

**Intellectual Challenge:**
- **Hand Management:** With a hand limit of 6 and 3 card types (Economy, Claim, Combat), players must decide which cards to play now, which to hold, and which to exchange during the Exchange Phase.
- **Resource Conversion:** Gold is a renewable but limited resource. Players must evaluate when to convert Gold into Investors (military presence) versus when to bank it for endgame tiebreakers.
- **Spatial Strategy:** The adjacency rule for attacks means territorial positioning matters. Players must plan multi-turn expansion paths while defending vulnerable borders.
- **Information Assessment:** With only 3 card categories and limited combat card templates, players can reasonably deduce opponents' capabilities and plan accordingly.

**Social Challenge:**
- **Timing Aggression:** Attacking too early makes you a target; waiting too long lets opponents entrench. Reading the table is essential.
- **Threat Assessment:** Identifying the current leader and deciding when to cooperate versus when to press your own advantage.
- **Bluffing:** Holding Combat Cards creates uncertainty — opponents don't know if you're prepared for defense or saving cards for an attack.

---

### Q1.4: What is the Drama?

**A:** The dramatic arc follows a classic escalation pattern:

- **Early Game (Rounds 1–2):** Exploration and positioning. Players establish starting territories, accumulate Gold, and begin claiming adjacent empty territories. Tension is low but stakes are being set.
- **Mid Game (Rounds 3–4):** First conflicts erupt. Borders meet, Combat Cards are played, and the power balance shifts. This is where the game is most dynamic — alliances form and break, and leaders emerge.
- **Late Game (Round 5):** Desperation. The draw pile is running low, forcing players into aggressive plays. The hand limit prevents hoarding, and every action counts. The final round creates a "last chance" urgency where a single well-timed Combat Card or Hostile Takeover can swing the game.

The **draw-pile-as-timer** mechanic is the primary dramatic engine: players can see the deck thinning, creating mounting tension about whether to act now or wait for a better hand.

---

### Q1.5: What is the Fantasy?

**A:** The game's form supports its fiction in several ways:

- **"Wolves of Wand Street"** evokes the predatory energy of Wall Street traders — the "wolves" are investor-wizards competing for market dominance.
- **Gold as currency** maps directly to the financial fantasy — territories produce Gold like revenue streams, and Investors are deployed like corporate assets.
- **Combat Cards** with names like "Hostile Takeover," "Strike Action," "Corporate Espionage," and "Market Crash" reinforce the economic warfare theme while providing magical flavor.
- **Territory names** (Inner/Outer territories, Hub) suggest a corporate district with valuable core offices and satellite branches.
- **The adjacency rule** mirrors real-world market expansion — you can only grow into adjacent markets, not teleport to distant ones.

---

## §2 · Core Gameplay

### Q2.1: What are the Core Systems?

**A:** The game has three interlocking core systems:

1. **The Economy System** (Gold generation and spending)
2. **The Card System** (Hand management, draw, exchange, and card effects)
3. **The Territory/Combat System** (Area control, deployment, and battle resolution)

Each system exists to create a specific type of decision tension, and they interact to ensure no single strategy dominates.

---

### Q2.2: How Does the Economy System Work?

**A:**

**Mechanics:**
- Players draw 4 cards at the start of each turn.
- Playing an **Economy Card** (as 1 major action) generates Gold tokens: Small Profit (2 Gold), Market Gain (3 Gold), or Risky Deal (4 Gold + discard 1).
- Gold is spent on **purchasing Investors** (1 Gold = 1 Investor token, default).
- Purchased Investors enter the player's **reserve** and must be deployed as a separate action.
- Gold also serves as a **secondary tiebreaker** at game end.

**Design Intent:**
- Gold creates a **conversion decision**: every Gold spent on Investors is Gold that won't help in a tiebreaker, and every Economy Card played is a card that could have been a Claim or Combat Card.
- The Economy Card templates are intentionally simple (gain 2/3/4 Gold) to reduce cognitive load — their role is to convert hand cards into purchasing power.
- The 1:1 Gold-to-Investor exchange rate was chosen for simplicity; playtesting may reveal this needs adjustment (see §23 of v0.2 rules).

**Interaction with Other Systems:**
- Economy feeds into Territory/Combat by enabling Investor purchases.
- Card System limits Economy by requiring you to draw Economy Cards and spend actions playing them.

---

### Q2.3: How Does the Card System Work?

**A:**

**Mechanics:**
- **Draw Phase:** Draw 4 cards from the face-down draw pile.
- **Exchange Phase:** Optionally discard up to 3 cards, drawing 1 replacement per discard (max 3 redraws).
- **Action Phase:** Up to 2 major actions per turn. Playing a card (Economy, Claim, or non-combat Combat Card) costs 1 action.
- **Discard Phase:** Hand limit of 6; discard excess.
- **Card Types:**
  - **Economy Cards (18):** Generate Gold.
  - **Claim Cards (18):** Required to occupy empty territories or attack enemy territories.
  - **Combat Cards (12):** Used during battle to modify outcomes.

**Design Intent:**
- The **Exchange Phase** gives players agency over their hand without guaranteeing what they need — you can cycle up to 3 cards but might draw worse ones.
- The **2-action limit** forces prioritization: Do you play 2 Economy Cards for Gold? Play 1 Economy + 1 Claim? Save actions for later?
- The **3-category system** (reduced from 52 unique cards in the original design) was a deliberate response to playtesting feedback that players couldn't remember or predict card effects.
- **No free actions** in v0.2 — every meaningful operation costs an action, card, Gold, or Investor. This was a direct fix from playtesting.

**Interaction with Other Systems:**
- Cards are the **gatekeeper** for all other systems — you need the right card type to take the corresponding action.
- Hand management creates tension between short-term plays and holding valuable cards.

---

### Q2.4: How Does the Territory/Combat System Work?

**A:**

**Territory Mechanics:**
- 13 territories: 4 clusters of 3 (1 Inner + 2 Outer each) + 1 central Hub.
- Each player starts with their Inner territory + 1 chosen Outer territory, each with 2 Investors.
- **Control:** A territory is controlled by the player with the most Investors on it (minimum 1, no opponents present).
- **Adjacency Rule:** Players can only attack/occupy territories adjacent to ones they control. Exception: a player with no territories may occupy any empty territory.

**Combat Mechanics:**
1. Attacker plays 1 **Claim Card** (costs 1 action).
2. Attacker commits Investors from adjacent territories or reserve.
3. Defender may reinforce from reserve.
4. **Combat Card Phase:** Attacker plays up to 1 Attack Card, Defender plays up to 1 Defence Card.
5. **Resolution:** Higher Battle Strength wins (1 Investor = 1 Strength + Combat Card modifiers). **Ties go to the defender.**
6. **Attacker wins:** Defender loses all committed Investors. Attacker must place ≥1 Investor on captured territory, loses 1 additional Investor.
7. **Defender wins:** Attacker loses all committed Investors. Defender loses 1 Investor (minimum 1 survives).
8. Removed Investors go to **general supply** (not reserve) — they must be repurchased with Gold.

**Design Intent:**
- The **adjacency rule** creates natural frontlines and prevents sudden backdoor attacks, making territorial positioning meaningful.
- **Ties favor the defender** to make aggression costly — attackers must commit more than the defender to succeed, creating a natural defensive advantage that encourages building up before attacking.
- **Casualties on both sides** prevent infinite snowballing — even a successful attack costs resources.
- The **Claim Card requirement** for attacks means combat competes with occupation for card resources.

---

### Q2.5: What Additional Mechanics Support the Core Systems?

**A:**

1. **Turn Order Shuffle:** Turn order is reshuffled every round, preventing permanent positional advantages and creating fresh dynamics each round.

2. **Hub Territory:** The central Hub produces more resources (4 Gold + 1 Influence in the original version) and is adjacent to all four player areas, making it a natural focal point for conflict.

3. **Draw Pile as Timer:** The game ends when the draw pile is exhausted (after completing the current round + 1 final round). This creates urgency without a fixed round counter — players can see the deck thinning.

4. **Card Exchange Mechanism:** The Exchange Phase (discard up to 3, redraw) reduces the impact of bad draws while maintaining uncertainty.

5. **Scaling by Player Count:** Works for 3–4 players. With 3 players, the 4th starting area becomes contested territory; with 4 players, all areas are claimed from the start.

---

## §3 · Interesting Decisions

### Q3.1: What is Decision 1 — Resource Conversion (Economy Cards vs. Other Cards)?

**A:**

Each turn, players draw 4 cards from a mixed deck. They must decide how to use Economy Cards versus Claim and Combat Cards.

1. **Balanced:** Economy Cards generate Gold (needed for Investors), Claim Cards enable expansion, and Combat Cards provide battle advantage. All three are valuable, and their relative worth shifts with game state.
2. **Informed:** Players can see the Market (5 face-up cards), know their own hand, and can observe opponents' territories and visible Investor counts. However, opponents' hands are hidden — you don't know if they're holding Combat Cards.
3. **Consequential:** Playing an Economy Card now means not having that card for a future turn. Spending an action on Gold generation means not attacking this turn. Missing an expansion window can cost territories permanently.
4. **Situational:** Early game favors Economy (build Gold reserves); mid-game favors Claim Cards (expand territory); late game favors Combat Cards (decisive battles). The Exchange Phase lets players cycle toward what they need, but with only 3 redraws.

---

### Q3.2: What is Decision 2 — Territory Expansion vs. Consolidation?

**A:**

Players must decide whether to spread Investors across many territories or concentrate them on key positions.

1. **Balanced:** Expanding grants more territory income but creates thin defenses. Consolidating makes territories nearly impregnable but limits income growth. Neither extreme is optimal.
2. **Informed:** Players can see all territories and Investor counts on the board. The map layout shows which territories are adjacent to opponents, informing threat assessment.
3. **Consequential:** Over-expansion leaves territories vulnerable to a single Claim Card attack. Over-consolidation means falling behind in territory income, which compounds over rounds.
4. **Situational:** When leading, consolidation protects your advantage. When behind, expansion is necessary to catch up. The Hub's adjacency to all areas makes it a strategic pivot point.

---

### Q3.3: What is Decision 3 — Combat Card Timing (Play vs. Hold)?

**A:**

In each battle, each side may play up to 1 Combat Card. Players must decide when to use their limited Combat Cards.

1. **Balanced:** Playing a Combat Card can swing a battle, but holding it creates uncertainty for opponents in future battles. The 6 Combat Card templates (Attack +2, Breakthrough, Safe Retreat, Defence +2, Fortify, Counter) offer different value depending on context.
2. **Informed:** Players know what Combat Cards exist (limited templates) but not which ones opponents hold. They can observe past battles to infer what cards have been used.
3. **Consequential:** A well-timed Defence +2 can save a critical territory. A Counter can negate an opponent's advantage. But wasting a Combat Card on a losing battle is a costly mistake.
4. **Situational:** Against a strong attacker, Defence cards are critical. When attacking a key territory, Attack cards and Breakthrough are more valuable. The Counter card's value depends entirely on what the opponent plays.

---

### Q3.4: What is Decision 4 — Investor Deployment (Reserve vs. Board)?

**A:**

Purchased Investors enter the reserve. Players must decide when to deploy them onto territories versus keeping them in reserve.

1. **Balanced:** Deployed Investors provide territorial control and combat strength but are committed and visible. Reserve Investors are flexible — they can reinforce any adjacent territory during combat — but don't contribute to territory control.
2. **Informed:** Players can see all deployed Investors. Reserve counts are hidden, creating information asymmetry about defensive capabilities.
3. **Consequential:** Deploying too many Investors signals strength but commits resources. Keeping Investors in reserve maintains flexibility but leaves territories potentially undefended.
4. **Situational:** Before an expected attack, deploying Investors to a threatened territory is wise. Before attacking, keeping Investors in reserve allows surprise reinforcement. The 10-Investor limit per player forces careful allocation.

---

### Q3.5: What is Decision 5 — When to Attack the Leader?

**A:**

In a multiplayer free-for-all, players must decide when and whom to attack.

1. **Balanced:** Attacking the leader helps catch up but weakens you against other opponents. Attacking a weaker player is easier but lets the leader pull further ahead. Ignoring conflict lets others set the terms.
2. **Informed:** Territory counts and Investor deployments are public. Gold and hand cards are private. Players can assess relative strength from visible information.
3. **Consequential:** A successful attack on the leader can redistribute 2–3 territories' worth of income. But a failed attack wastes Claim Cards, Combat Cards, and Investors while other opponents grow.
4. **Situational:** In the final round, attacking the leader becomes paramount. In early rounds, building your own engine is often better. The turn-order shuffle means you can't predict who goes first each round, affecting attack timing.

---

## §4 · Adding Variety

### Q4.1: What Ensures Each Playthrough Feels Different?

**A:**

1. **Card Draw Randomness:** The 48-card deck is shuffled each game. The order of Economy, Claim, and Combat Cards drawn varies, creating different resource and action availability each game.

2. **Turn Order Shuffle:** Reshuffled every round, preventing fixed positional advantages and creating different initiative dynamics.

3. **Starting Territory Choice:** Each player picks 1 of 2 Outer territories to start with, creating 2^4 = 16 possible starting configurations for 4 players.

4. **Player-Driven Variability:** The free-for-all nature means player interactions change every game — temporary alliances, target selection, and aggression timing are all emergent.

5. **Combat Card Uncertainty:** The limited set of Combat Card templates means players must read opponents' tendencies. Some players bluff by holding cards; others use them aggressively. This meta-game evolves across plays.

6. **Draw Pile as Variable Timer:** The game length varies based on Exchange Phase usage — more cycling means faster deck depletion, creating variable game lengths.

---

## §5 · Meeting the Design Brief

### Q5.1: How Does the Game Meet Each COMP2150 Requirement?

**A:**

| Requirement | How It's Met |
|-------------|-------------|
| **Custom deck of cards** | 48-card custom deck with 3 categories: 18 Economy, 18 Claim, 12 Combat. Each card has custom names, effects, and artwork (see Appendix A). |
| **3–4 players** | Designed for 3–4 players. 4-player uses all 4 starting areas; 3-player leaves one area as contested neutral territory. |
| **At least 2 distinct resources** | **Gold** (economic — generates Investors, secondary tiebreaker) and **Investors** (military — controls territories, primary combat unit). Each has distinct earning, spending, and strategic roles. |
| **Meaningful round in ≤15 min** | Each turn ~45 seconds (draw 4, optional exchange, 2 actions, discard). With 4 players × 5 rounds = 20 turns per player, total ~15 minutes. |
| **playingcards.io compatible** | Game implemented on playingcards.io with custom card images, token zones, and map layout (wolves_of_wand_street.pcio). |

### Q5.2: How Does the Game Achieve the Experience Goals?

**A:**

| Experience Goal | How It's Achieved |
|----------------|-------------------|
| **Fellowship** | Competitive free-for-all with temporary alliances. Adjacency rules force interaction. No player can win in isolation. |
| **Challenge** | Multi-layered decisions: hand management + resource conversion + spatial strategy + combat timing. The 2-action limit forces prioritization. |
| **Drama** | Draw-pile-as-timer creates escalating tension. Casualty rules ensure battles are costly. The final round creates desperate last-stand moments. |

---

## §6 · Production Process

### Q6.1: What Tools Were Used?

**A:**
- **playingcards.io:** Digital implementation and online playtesting platform. The `.pcio` file contains the complete game with custom card zones, map layout, and token management.
- **LaTeX + Python scripts:** Card asset generation. The `cards_png_assets.tex` and `Assets/Scripts/` directory contain automated card rendering pipelines producing PNG card images.
- **Paper prototyping:** Initial playtesting with hand-drawn territories and standard playing cards mapped to game cards (see §20 of v0.2 rules for the mapping).
- **Git/GitHub:** Version control and collaboration. Design documents, rules, and assets are all tracked in the repository.
- **Google Docs:** Shared design document for collaborative editing (linked in README).

### Q6.2: What Was the Team Workflow?

**A:**
*(Note: Please update this section with specific team member names and roles if applicable.)*

- **Design & Rules:** Iterative design with multiple rule versions (original v1 → simplified v0.2) driven by playtesting feedback.
- **Asset Production:** Automated pipeline from LaTeX/card definitions → PNG images → playingcards.io import.
- **Playtesting:** At least 3 documented playtests with structured feedback collection (see `note_for_playtest_new-rule.md`).

### Q6.3: What Was the Timeline?

**A:**

| Phase | Description |
|-------|-------------|
| **Concept** | Initial design with 52-card deck, Influence scoring, Free Actions, and complex card effects (v1 rules). |
| **Paper Prototype** | Physical playtesting with standard playing cards mapped to game cards. 3+ playtests documented. |
| **Playtest Feedback** | Identified 3 critical problems: Free Actions undermine action economy, Influence hoarding, excessive cognitive load from 52 unique cards. |
| **Redesign (v0.2)** | Simplified to 48 cards (3 categories), removed Influence scoring, eliminated Free Actions, standardized Combat Card templates. |
| **Digital Implementation** | Built playingcards.io version with custom card artwork, automated card generation pipeline. |
| **Final Playtesting** | Ongoing balance testing with v0.2 rules. |

---

## §7 · Reflection

### Q7.1: What Works Well?

**A:**

1. **Three-Category Card System:** Reducing from 52 unique cards to 3 categories (Economy/Claim/Combat) dramatically lowered the learning curve while maintaining strategic depth. Players can now reasonably predict opponents' capabilities, enabling meaningful bluffing and counterplay.

2. **Elimination of Free Actions:** The v0.2 change to require actions/cards/Gold for every meaningful operation restored decision tension. The 2-action limit now genuinely constrains players.

3. **Territory Income Scaling:** The tiered income system (more territories = more Gold/Influence) creates natural catch-up mechanics — expanding is rewarding but risky.

4. **Adjacency-Based Combat:** This prevents unrealistic "teleportation" attacks and creates natural frontlines, making territorial positioning meaningful.

5. **Draw Pile as Timer:** Using deck depletion as the game-end trigger is elegant — it's visible, creates urgency, and varies game length based on player behavior (more Exchange cycling = shorter games).

### Q7.2: What Needs Improvement?

**A:**

1. **Balancing Investor Pricing:** The default 1 Gold = 1 Investor may be too generous. Playtesting showed rapid territory occupation. Consider 2 Gold = 1 Investor to slow expansion.

2. **Defender Advantage Balance:** Ties favoring the defender + defender reinforcement from reserve may make defense too strong, leading to stalemates. May need to restrict reserve reinforcement or adjust tie-breaking.

3. **Late-Game Card Exhaustion:** When the draw pile empties, players with fewer cards have a significant disadvantage. The current "skip draws" rule may need adjustment.

4. **Hub Dominance:** The central Hub's adjacency to all areas and higher income makes it extremely valuable. First-mover advantage in securing the Hub may be too strong.

5. **Playtest Score Imbalance:** All 3 documented playtests were won by Player 4 (scores: 9, 8, —), suggesting a positional or turn-order advantage that needs investigation.

### Q7.3: What Were the Lessons Learned?

**A:**

1. **Simplicity Wins:** The biggest improvements came from removing complexity (Free Actions, 52 unique cards, Influence scoring) rather than adding features. Less is more.

2. **Playtest Early, Playtest Often:** The gap between design intent and player experience was only visible through playtesting. The 3 identified problems (Free Actions, hoarding, cognitive load) were not apparent during design.

3. **Every System Must Create Tension:** The original Influence scoring system created perverse incentives (hoarding > spending). Removing it and making Gold a secondary tiebreaker instead created better strategic tension.

4. **Information Design Matters:** The 3-category card system works because players can hold the entire card taxonomy in their head, enabling strategic planning and opponent reading.

5. **Iterative Design is Essential:** The evolution from v1 (complex) to v0.2 (streamlined) demonstrates the value of willingness to cut features that don't serve the core experience.

---

## §8 · Open Design Questions (Pending Playtest Confirmation)

### Q8.1: Should Investor Pricing Change?

**Current:** 1 Gold = 1 Investor.
**Alternative:** 2 Gold = 1 Investor (slower expansion, more strategic Gold use).
**Testing:** If playtests show too-rapid territory occupation, increase price.

### Q8.2: What Is the Optimal Investor Limit?

**Current:** 10 per player.
**Alternatives:** 8 (tighter, more combat) or 12 (more room for buildup).
**Testing:** If map feels overcrowded, reduce. If combat is too rare, increase.

### Q8.3: Should Remote Occupation Be Allowed?

**Current:** Must be adjacent.
**Alternative:** Pay 2 Gold to occupy a non-adjacent empty territory.
**Testing:** If players get stuck behind enemy lines, enable remote occupation.

### Q8.4: Can Defenders Reinforce from Reserve?

**Current:** Yes.
**Alternative:** Only Investors already on the territory can defend.
**Testing:** If defense is too strong (stalemates), restrict reinforcement.

### Q8.5: What Is the Optimal Deck Size?

**Current:** 48 cards.
**Alternatives:** 52 (add 4 wild/advanced cards) or smaller for shorter games.
**Testing:** If games run too long, reduce deck or increase draw amount.

---

## Appendix Checklist

| Appendix | Content | Source |
|----------|---------|--------|
| **A: Card Reference** | Full card list with effects, costs, and images | `README.md` card images + `Wolves_of_WandStreet.md` §6 |
| **B: Map/Board Reference** | Territory layout, adjacency diagram, income values | `rules_v0_2.md` §4.1 + `Wolves_of_WandStreet.md` §1.1 |
| **C: Quick Reference Card** | Condensed turn summary, action list, combat resolution | `rules_v0_2.md` §24 |

---

## Word Count Targets

| Section | Target | Notes |
|---------|--------|-------|
| §1 Target Experience | ~800 words | 5 sub-sections (High Concept, Fellowship, Challenge, Drama, Fantasy) |
| §2 Core Gameplay | ~1200 words | 3 core systems + additional mechanics |
| §3 Interesting Decisions | ~1500 words | 5 decisions × 4 criteria each |
| §4 Adding Variety | ~300 words | 6 sources of variability |
| §5 Meeting the Brief | ~300 words | Requirements table + experience goals |
| §6 Production Process | ~400 words | Tools, workflow, timeline |
| §7 Reflection | ~400 words | Strengths, improvements, lessons |
| **Total** | **~4900 words** | Plus appendices (no word count) |

---

## Assessment Criteria Alignment

| Criterion | Where Addressed | Key Evidence |
|-----------|----------------|--------------|
| **Target Experience** | §1 | Clear high concept, social dynamics, challenge analysis, dramatic arc, thematic coherence |
| **Core Systems** | §2 | 3 interlocking systems with mechanics + design intent + interaction analysis |
| **Interesting Choices** | §3 | 5 decisions with Balanced/Informed/Consequential/Situational analysis (Hualalai benchmark) |
| **Variety/Replayability** | §4 | Card randomness, turn order, player-driven variability |
| **Design Brief Compliance** | §5 | Explicit checklist of all 5 requirements |
| **Production Process** | §6 | Tools, workflow, iterative timeline |
| **Critical Reflection** | §7 | Honest assessment of strengths/weaknesses, lessons from playtesting |
| **Professional Presentation** | Throughout | Structured format, clear language, appendices for reference material |

---

## §9 · COMP2150 Rubric Deep-Dive (How to Score Outstanding/HD)

### Q9.1: What Are the 4 Assessment Components?

**A:** The rubric has **4 equally weighted components**:

| Component | Weight | What It Evaluates |
|-----------|--------|-------------------|
| **Game Design** | 25% | Mechanics, dynamics, interesting choices, player experience goals, form & fiction |
| **Game Communication** | 25% | Design documentation quality, theory use, production process, reflection |
| **Playtesting Design** | 25% | Playtest methodology, design questions, sample selection, mixed-methods |
| **Playtesting Execution** | 25% | Evidence of playtesting program, data collection, iteration from results |

### Q9.2: What Does "Outstanding" (85-100%) Look Like for Game Design?

**A:**
- Game design **capitalises on constraints** with finely-tuned mechanics
- Produces **engaging dynamics** and **expertly balanced interesting choices**
- Player experience goals are **frequently and meaningfully satisfied**
- Game's form and fiction has **excellent readability and usability**
- Frequently approaches a **professional level** of clarity and creativity

**Action Items:**
- [ ] Ensure every constraint is explicitly turned into a design advantage (e.g., 15-min time limit → draw-pile-as-timer)
- [ ] Verify all 3 experience goals (Fellowship, Challenge, Drama) are meaningfully addressed
- [ ] Card artwork and naming must be polished and professional

### Q9.3: What Does "Outstanding" (85-100%) Look Like for Game Communication?

**A:**
- Documentation **expertly encapsulates** the group's game design
- **Mobilises relevant theory** to justify design decisions
- Shows **significant depth of insight** through detailed understanding of mechanics, decisions, dynamics, and player experience
- Production processes **concretely outlined** with **convincing evidence of forward planning**
- Reflections are **insightful, relevant and actionable** for future projects

**Action Items:**
- [ ] Reference game design theory explicitly (e.g., "interesting choices" framework from Hunicke/LeBlanc, MDA framework)
- [ ] Each design decision should have a clear WHY (design intent) not just WHAT (mechanics)
- [ ] §6 Production Process must show forward planning, not just chronology
- [ ] §7 Reflection must be actionable — "If we did this again, we would..."

### Q9.4: What Does "Outstanding" (85-100%) Look Like for Playtesting Design?

**A:**
- Playtest design follows **best practice** and is **highly ambitious**
- **Expertly aligned** with game design considerations
- **Considered mixed-methods testing** of both analog and digital versions
- Includes: design questions, prototype, selected sample, chosen methods, procedure, instruments

**Action Items:**
- [ ] Each playtest must have a **clear design question** (e.g., "Does the 2-action limit create meaningful tension?")
- [ ] Each playtest must have **defined methodology** (observation, survey, structured interview)
- [ ] Must test **both** physical prototype AND playingcards.io version
- [ ] Need **at least 3 distinct playtests** with different design questions

### Q9.5: What Does "Outstanding" (85-100%) Look Like for Playtesting Execution?

**A:**
- **Clear and convincing evidence** of an extensive program of playtesting
- At least **3 unique playtest designs** executed externally
- **4 or more sessions per playtest** (recommended for HD+)
- All required sections/elements clear and complete
- **Copies of raw results and instrument templates** in appendices
- **Clear evidence of thoughtful application** of playtesting results across iterations

**Action Items:**
- [ ] Need **minimum 3 × 2 sessions** for pass, **3 × 4 sessions** for HD+
- [ ] Each playtest session needs: date, participants, data collected, results
- [ ] Raw data (surveys, observation notes) must be in appendices
- [ ] Must show **iteration**: "After Playtest 1 showed X, we changed Y, then Playtest 2 confirmed Z"

---

## §10 · Playtesting Report Q&A (SEPARATE from Design Doc)

### Q10.1: What Playtests Do We Have?

**A:** Based on `note_for_playtest_new-rule.md`, we have documented playtests:

| Playtest | Winner | Score | Key Findings |
|----------|--------|-------|--------------|
| Playtest 1 | Player 4 | 9 pts | Territory occupied too quickly; 1 investor can take down half of opponent's; Hostile Takeover too strong |
| Playtest 2 | Player 4 | 8 pts | Added contest limit to 1; changed Small Trade to Aggressive Expansion; added rules on cards; Hostile Takeover needs ≥1 investor |
| Playtest 3 | (incomplete) | — | Not documented |

**PROBLEM:** We only have **2 completed playtests** and **1 incomplete**. The rubric requires **minimum 3 playtests** with **minimum 2 sessions each** (for pass) or **4 sessions each** (for HD+).

### Q10.2: What Playtests Are Missing?

**A:**

| Playtest | Design Question | Status | What's Needed |
|----------|----------------|--------|---------------|
| **Playtest 1** (Action Economy) | "Does the v0.2 action system create meaningful decision tension?" | ⚠️ Partial | Need 2-3 more sessions with different groups, structured data collection |
| **Playtest 2** (Combat Balance) | "Is the combat system balanced between attack and defense?" | ⚠️ Partial | Need 2-3 more sessions, formal survey/observation data |
| **Playtest 3** (Overall Balance) | "Does the game produce close/competitive outcomes?" | ❌ Missing | Need full playtest with 2-4 sessions |

### Q10.3: What Data Collection Instruments Do We Need?

**A:**

For **each playtest**, the rubric expects:
1. **Design Question** — What specific question this playtest answers
2. **Methodology** — How data is collected (observation, survey, interview, scoring)
3. **Participants** — Who played (number, experience level, session date)
4. **Raw Data** — Actual scores, survey responses, observation notes
5. **Analysis** — What the data tells us
6. **Iteration** — What we changed based on the results

**Templates needed:**
- [ ] Post-game survey (Likert scale + open questions)
- [ ] Observer checklist (tracking specific behaviors)
- [ ] Score tracking sheet
- [ ] Player feedback form

### Q10.4: How Should We Structure the Playtesting Report?

**A:**

The report should include for EACH of the 3 playtests:
1. **Design Question** — What are we testing?
2. **Hypothesis** — What do we expect to find?
3. **Method** — How are we testing it?
4. **Participants** — Who played and when?
5. **Results** — What happened? (data, scores, observations)
6. **Analysis** — What does this mean?
7. **Iteration** — What did we change? How did it affect the next playtest?

---

## §11 · Document Structure Checklist

The final PDF submission (~5000 words) should contain:

| Section | Word Count | Status | Notes |
|---------|-----------|--------|-------|
| **Instructions for Play** | NOT counted | ❌ Missing | Rules, setup, card reference — can use existing rules docs |
| **§1 Target Experience** | ~800 | ❌ Not written | High Concept, Fellowship, Challenge, Drama, Fantasy |
| **§2 Core Gameplay** | ~1200 | ❌ Not written | 3 core systems + design intent |
| **§3 Interesting Decisions** | ~1500 | ❌ Not written | 5 decisions × 4 criteria |
| **§4 Adding Variety** | ~300 | ❌ Not written | Replayability sources |
| **§5 Meeting the Brief** | ~300 | ❌ Not written | COMP2150 requirements checklist |
| **§6 Production Process** | ~400 | ❌ Not written | Tools, workflow, timeline |
| **§7 Reflection** | ~400 | ❌ Not written | Strengths, improvements, lessons |
| **Playtesting Report** | ~500-1000 | ⚠️ Partial | Need structured report for 3 playtests |
| **Appendix A: Cards** | NOT counted | ✅ Have assets | Card images exist in Assets/Cards-png/ |
| **Appendix B: Map** | NOT counted | ⚠️ Need diagram | Have text description, need visual |
| **Appendix C: Quick Ref** | NOT counted | ❌ Missing | Need condensed rules summary |
| **Appendix D: Playtest Data** | NOT counted | ⚠️ Partial | Need raw data, surveys, instruments |

---

## §12 · Critical Action Items (Priority Order)

### 🔴 MUST DO (Before 24/05/2026 Deadline)

| # | Task | Priority | Est. Time |
|---|------|----------|-----------|
| 1 | Write §1-§7 of Design Doc | 🔴 Critical | 3-4 hours |
| 2 | Structure Playtesting Report (3 playtests) | 🔴 Critical | 2-3 hours |
| 3 | Create playtest data collection instruments | 🔴 Critical | 1 hour |
| 4 | Conduct Playtest 3 (minimum) | 🔴 Critical | 1-2 hours |
| 5 | Compile final PDF | 🔴 Critical | 1 hour |
| 6 | Update .pcio file if needed | 🟡 High | 30 min |
| 7 | Git commit & push | 🟢 Low | 5 min |

### 🟡 SHOULD DO (For Higher Marks)

| # | Task | Priority | Impact |
|---|------|----------|--------|
| 8 | Additional playtest sessions (4 per playtest for HD+) | 🟡 | Playtesting Execution rubric |
| 9 | Reference game design theory in §1-§3 | 🟡 | Game Communication rubric |
| 10 | Create Appendix B map diagram | 🟡 | Professionalism |
| 11 | Create Appendix C Quick Reference Card | 🟡 | Game Design rubric (usability) |

---

## §13 · Key Theory to Reference (For HD+ Communication Score)

### Q13.1: What Game Design Theory Should We Reference?

**A:**

| Theory | Where to Apply | Reference |
|--------|---------------|-----------|
| **MDA Framework** (Mechanics, Dynamics, Aesthetics) | §2 Core Gameplay | Hunicke, LeBlanc & Zubek (2004) |
| **Interesting Choices** | §3 Interesting Decisions | Sid Meier's "A game is a series of interesting choices" |
| **Bartle's Player Types** | §1 Fellowship | Explain how the game appeals to Achievers (territory control) and Killers (combat) |
| **Emergence vs. Progression** | §4 Adding Variety | The game's variety comes from emergence (player interaction), not scripted progression |
| **Salen & Zimmerman - Rules of Play** | §2 Core Gameplay | Game as system of rules creating meaningful play |
| **Cost of Attack / Defensive Advantage** | §3 Decisions | The tie-goes-to-defender rule as intentional design for strategic depth |
| **Resource Scarcity** | §2 Economy System | Gold and Investor limits create tension (not too scarce = no decisions, not too abundant = no tension) |
| **Information Asymmetry** | §3 Decisions | Hidden hand vs. public board state creates strategic depth |

---

## §14 · Existing Materials Inventory

| Material | Location | Quality | Usable? |
|----------|----------|---------|---------|
| Original rules (v1) | `Doc/Wolves_of_WandStreet.md` | Detailed, 234 lines | Yes — for §7 Reflection |
| Simplified rules (v0.2) | `wolves_of_wand_street_rules_v0_2.md` | Complete, 748 lines | Yes — for Instructions for Play |
| Playtest notes | `note_for_playtest_new-rule.md` | Brief, 46 lines | Partial — needs structuring |
| Playtest reflections | `Design_Doc.md` | 15 lines | Yes — for §7 Reflection |
| Card images (26 cards) | `Assets/Cards-png/` | PNG files | Yes — for Appendix A |
| .pcio game file | `wolves_of_wand_street.pcio` | Complete | Yes — submission ready |
| Card generation pipeline | `Assets/Scripts/` + `cards_png_assets.tex` | LaTeX + Python | Yes — for §6 Production |
| Hualalai example | `Doc/Hualalai_-_Design_Doc_Example.pdf` | 6 pages | Yes — benchmark for quality |
| COMP2150 brief | `Doc/COMP2150_Tabletop_Game_Description.pdf` | Full rubric | Yes — for §5 and rubric alignment |
