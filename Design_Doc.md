# Wolves of Wand Street

**Design Document**

---

## 1 · Target Experience

> *~800 words recommended*

### High Concept

Four ambitious entrepreneurs set sail for a virgin continent — a land untouched by commerce, rich with untapped potential. In *Wolves of Wand Street*, 3–4 players compete to carve out financial empires across this uncharted territory, deploying investors, waging economic warfare, and seizing control of 13 territories in a card-driven area-control game that fuses classical city-state rivalry with the predatory energy of Wall Street. Each game lasts approximately 15 minutes and distils resource management, tactical combat, and hand management into a tightly contested competitive experience.

### Fellowship

*Wolves of Wand Street* is a competitive free-for-all with no teams, no hidden traitors, and no safe positions. Interaction is structurally enforced through **territorial adjacency** — every expansion path leads through territory that another player either owns or covets. There is no passive strategy: claiming an empty territory requires adjacency to your own; attacking requires a direct border. The game's multiplayer dynamics encourage **temporary alliances of convenience** — for instance, two players may tacitly cooperate to weaken a leader — while the turn-order shuffle each round prevents permanent king-making arrangements. Every player understands that all alliances are ultimately self-serving, creating a social layer of suspicion and opportunism beneath the mechanical surface.

### Challenge

The game presents two interlocking layers of challenge:

**Intellectual Challenge.** With a hand limit of six and three card types (Economy, Claim, Combat), players must continuously evaluate which cards to play now, which to hold for future turns, and which to cycle through the Exchange Phase. The resource conversion loop — play Economy Cards to gain Gold, spend Gold to purchase Investors, deploy Investors onto territories — requires multi-turn planning. The adjacency rule for attacks adds a spatial dimension: players must plan expansion routes while defending vulnerable borders. The limited Combat Card templates (six distinct effects) mean players can reasonably deduce opponents' capabilities, rewarding attentive observation and probabilistic reasoning.

**Social Challenge.** Timing aggression is critical — attacking too early makes you a target; waiting too long lets opponents entrench. Players must read the table to identify the current leader and decide when to cooperate versus when to press their own advantage. Holding Combat Cards creates information asymmetry: opponents cannot tell whether you are prepared for defence or saving cards for a decisive strike, enabling bluffing and counter-bluffing.

### Drama

The dramatic arc follows a three-act escalation pattern:

- **Act I — Expansion (Rounds 1–2).** Players establish starting territories, accumulate Gold, and claim adjacent empty spaces. Tension is low but strategic stakes are being set. The map gradually fills with competing colours.
- **Act II — Conflict (Rounds 3–4).** Borders meet. The first attacks erupt, Combat Cards are revealed, and the power balance shifts with each engagement. This is the game's most dynamic phase — alliances of convenience form and dissolve, and leaders emerge to be targeted.
- **Act III — Desperation (Round 5).** The draw pile is visibly thinning, forcing players into aggressive plays. The hand limit prevents hoarding, and every action counts. A single well-timed Combat Card or bold attack can swing the game. The final round creates a "last chance" urgency that produces the game's most memorable moments.

The **draw-pile-as-timer** mechanic is the primary dramatic engine. Unlike a fixed round counter, the deck depletion is visible to all players, creating mounting psychological tension about whether to act now or wait for a better hand.

### Fantasy

The game's form supports its fiction through consistent thematic layering. The title *Wolves of Wand Street* merges the predatory energy of Wall Street with the arcane ("Wand"), grounding the setting in a world where finance and sorcery are one and the same. Gold functions as both currency and magical resource — territories produce it like revenue streams, and Investors are deployed like corporate assets. Card names reinforce the economic warfare theme while maintaining fantasy flavour: "Hostile Takeover," "Corporate Espionage," "Market Crash," and "Arcane Dominion" all operate in both registers. The territory structure — Inner territories (headquarters), Outer territories (branch offices), and the central Hub (the prime market) — maps the city-state metaphor onto the board layout. The adjacency rule mirrors real-world market expansion: you can only grow into adjacent markets, not teleport to distant ones, reinforcing the fantasy of organic, competitive territorial growth.

---

## 2 · Core Gameplay

> *~1200 words recommended*

The game is built on three interlocking systems: the **Economy System**, the **Card System**, and the **Territory/Combat System**. Each system creates a distinct type of decision tension, and their interactions ensure that no single strategy dominates.

### 2.1 The Economy System

**Mechanics.** Players draw four cards at the start of each turn. Playing an Economy Card (as one major action) generates Gold tokens according to the card's value: *Small Profit* (2 Gold), *Market Gain* (3 Gold), or *Risky Deal* (4 Gold, then discard one card). Gold is spent to purchase Investors at a default rate of 1 Gold = 1 Investor. Purchased Investors enter the player's reserve and must be deployed onto territories as a separate action. At game end, remaining Gold serves as a secondary tiebreaker.

**Design Intent.** Gold creates a **conversion dilemma**: every Gold spent on Investors is Gold that cannot help in a tiebreaker, and every action spent playing an Economy Card is an action not spent on expansion or combat. The Economy Card templates are deliberately simple — their sole function is to convert hand cards into purchasing power. This simplicity was a conscious response to playtesting: the original v1 design featured complex Economy Cards with multiple effects, which players found difficult to remember and evaluate. The streamlined templates allow players to focus mental effort on strategic decisions rather than card-text parsing.

**System Interaction.** Economy feeds Territory/Combat by enabling Investor purchases, but is gated by the Card System — you must draw Economy Cards and spend actions playing them. This three-way dependency means players cannot simply "buy their way to victory" without also investing in the right cards and territorial positioning.

### 2.2 The Card System

**Mechanics.** Each turn follows a four-phase structure: **Draw** (four cards from the face-down draw pile), **Exchange** (optionally discard up to three cards, drawing one replacement per discard), **Action** (up to two major actions), and **Discard** (hand limit of six). The 48-card deck is divided into three categories:
- **Economy Cards (18):** Generate Gold when played.
- **Claim Cards (18):** Required to occupy empty territories or attack enemy territories.
- **Combat Cards (12):** Used during battle to modify outcomes (six templates: Attack +2, Breakthrough, Safe Retreat, Defence +2, Fortify, Counter).

**Design Intent.** The Exchange Phase gives players agency over their hand without guaranteeing outcomes — cycling up to three cards might yield what you need, or might not. The two-action limit forces prioritisation: playing two Economy Cards for Gold means not attacking this turn; playing one Economy and one Claim means committing to a single expansion. The three-category system was the single largest design change from v1 to v0.2. The original 52-card design featured unique effects per card, which created excessive cognitive load — players could not remember or predict opponents' capabilities. Reducing to three categories with standardised templates allows meaningful bluffing and counterplay, because players can hold the entire card taxonomy in working memory. Additionally, v0.2 eliminated all free actions: every meaningful operation costs an action, card, Gold, or Investor, restoring genuine tension to the two-action limit.

**System Interaction.** Cards are the **gatekeeper** for all other systems. You need the right card type to take the corresponding action. This creates a hand-management tension between short-term plays and holding valuable cards for future turns.

### 2.3 The Territory/Combat System

**Territory Mechanics.** The map contains 13 territories arranged in four clusters of three (each with one Inner and two Outer territories) plus one central Hub. Each player starts with their Inner territory and one chosen Outer territory, each defended by two Investors. A territory is controlled by the player with at least one Investor and no opponents present. The adjacency rule restricts attacks and occupations to territories adjacent to ones you control.

**Combat Resolution.** To attack, a player plays one Claim Card (costing one action) and commits Investors from adjacent territories or reserve. The defender may reinforce from reserve. Both sides may then play up to one Combat Card each. Battle Strength is calculated as the number of committed Investors plus Combat Card modifiers; the higher total wins, with **ties favouring the defender**. The winner takes the territory; both sides suffer casualties (attacker loses one additional Investor beyond the garrison; defender loses one Investor if they had more than one committed). Removed Investors return to general supply — they must be repurchased with Gold, not simply redeployed.

**Design Intent.** The adjacency rule creates natural frontlines and prevents unrealistic "teleportation" attacks, making territorial positioning meaningful. The tie-goes-to-defender rule makes aggression costly — attackers must commit significantly more than defenders to succeed, encouraging deliberate build-ups rather than reckless assaults. The mutual casualty mechanic prevents infinite snowballing: even a successful attack depletes resources, ensuring that overextension carries real consequences. The Claim Card requirement for attacks means combat directly competes with occupation for card resources, creating a further layer of strategic tension.

### Additional Mechanics

**Turn Order Shuffle.** Turn order is reshuffled every round. This prevents permanent first-player advantages and ensures that initiative dynamics shift each round, keeping all players engaged throughout.

**Hub Territory.** The central Hub is adjacent to all four player areas and produces higher income than other territories. It serves as a natural focal point for conflict — controlling the Hub grants both economic advantage and strategic reach, but its exposed position makes it difficult to hold.

**Draw Pile as Timer.** The game ends when the draw pile is exhausted. After the triggering turn completes the current round, each player takes one final turn. This mechanic creates urgency without a fixed round counter — players can see the deck thinning and must calibrate their aggression accordingly.

**Card Exchange Mechanism.** The Exchange Phase (discard up to three, draw replacements) reduces the impact of bad draws while maintaining uncertainty. It also accelerates deck depletion, indirectly affecting game length — more cycling means a shorter game.

**Player Count Scaling.** The game supports 3–4 players. With four players, all four starting areas are occupied from the start; with three players, the fourth area becomes contested neutral territory, altering the early-game dynamic.

---

## 3 · Interesting Decisions

> *~1500 words recommended*

The game produces several interlocking interesting decisions. The following five are the most strategically significant.

### 3.1 Card Usage: Economy vs. Claim vs. Combat

Each turn, players draw four cards from a mixed deck and must decide how to allocate their two actions among Economy, Claim, and Combat Cards.

1. **Balanced:** Economy Cards generate Gold (needed for Investors), Claim Cards enable expansion (required to attack or occupy), and Combat Cards provide battle advantage. All three are essential, and their relative value shifts with game state. No single card type is universally dominant.
2. **Informed:** Players know their own hand and can observe opponents' territories and visible Investor counts. The limited three-category system means players can reasonably infer what opponents might hold based on their recent actions (e.g., a player who hasn't attacked likely holds Claim Cards; one who just purchased Investors likely played Economy Cards).
3. **Consequential:** Playing an Economy Card now means not having that card for a future turn. Spending an action on Gold generation means not attacking this turn. Missing an expansion window — for instance, failing to claim a contested territory before an opponent does — can cost a permanent positional advantage.
4. **Situational:** Early game favours Economy (building Gold reserves for Investor purchases); mid-game favours Claim Cards (expanding territory and initiating first conflicts); late game favours Combat Cards (decisive battles where a single +2 modifier can swing a territory). The Exchange Phase allows players to cycle toward what they need, but with only three redraws, the hand is never fully under your control.

### 3.2 Territory Expansion vs. Consolidation

Players must decide whether to spread Investors thinly across many territories or concentrate them on key positions.

1. **Balanced:** Expanding grants more territory income (each territory generates Gold each round) but creates thin defences. Consolidating makes territories nearly impregnable but limits income growth and cedes map control to opponents. Neither extreme is optimal; the correct approach shifts with game state.
2. **Informed:** All territories and deployed Investor counts are visible on the board. Players can assess which territories are adjacent to opponents and therefore vulnerable, informing defensive priorities. However, opponents' reserve Investor counts are hidden, creating information asymmetry about defensive capability.
3. **Consequential:** Over-expansion leaves territories vulnerable to a single Claim Card attack — a thinly held Outer territory can be captured with minimal Investment. Over-consolidation means falling behind in territory income, which compounds over rounds as wealthier opponents purchase more Investors.
4. **Situational:** When leading in territory count, consolidation protects the advantage. When behind, expansion is necessary to catch up. The Hub's adjacency to all four areas makes it a strategic pivot point — controlling it influences expansion options for every player.

### 3.3 Combat Card Timing

In each battle, each side may play up to one Combat Card. Players must decide when to deploy their limited Combat Cards versus holding them for future engagements.

1. **Balanced:** Playing a Combat Card can swing a battle (e.g., Attack +2 against a defender with equal Investors guarantees victory), but holding it creates uncertainty for opponents in future battles. The six templates offer different value depending on context — Defence +2 is critical when defending the Hub; Breakthrough is most valuable when attacking a heavily fortified territory; Counter is only useful when the opponent plays first.
2. **Informed:** Players know what Combat Card templates exist (the limited set is public knowledge) but not which specific cards opponents hold. They can observe past battles to track which cards have been played and removed from the game, narrowing the possibilities.
3. **Consequential:** A well-timed Defence +2 can save a critical territory worth 3+ Gold per round. A Counter can negate an opponent's entire offensive investment. But wasting a Combat Card on a battle you were already going to lose (or win without it) is a costly misplay in a game where Combat Cards are scarce (only 12 in the entire deck).
4. **Situational:** Against a strong attacker, Defence cards become critical. When attacking a key territory, Attack cards and Breakthrough are more valuable. In the final round, all held Combat Cards become worthless after the game ends, shifting the calculus toward aggressive use.

### 3.4 Investor Deployment: Reserve vs. Board

Purchased Investors enter the reserve. Players must decide when to deploy them onto territories versus keeping them in reserve for flexible reinforcement.

1. **Balanced:** Deployed Investors provide territorial control and visible combat strength, but are committed and immobile (except through Retrieve Investors action). Reserve Investors are hidden and flexible — they can reinforce any adjacent territory during combat — but do not contribute to territory ownership or income.
2. **Informed:** All deployed Investors are visible. Reserve counts are hidden, creating meaningful information asymmetry. An opponent with a large reserve is threatening but may be bluffing — or may genuinely hold the resources for a devastating counter-attack.
3. **Consequential:** Deploying too many Investors signals strength but commits resources to specific positions, making them predictable targets. Keeping too many in reserve leaves territories underdefended and vulnerable to cheap attacks.
4. **Situational:** Before an expected attack, deploying Investors to a threatened territory is wise — it raises the cost of assault. Before launching your own attack, keeping Investors in reserve allows surprise reinforcement. The 10-Investor per-player limit forces careful allocation across both pools.

### 3.5 Target Selection: When and Whom to Attack

In a multiplayer free-for-all, players must decide when to initiate conflict and whom to target.

1. **Balanced:** Attacking the leader helps close the gap but weakens you against other opponents. Attacking a weaker player is easier but lets the leader pull further ahead. Ignoring conflict entirely lets others set the terms of engagement and may result in being surrounded.
2. **Informed:** Territory counts and deployed Investors are public. Gold totals and hand cards are private. Players can assess relative strength from visible information, but must account for hidden reserves and unplayed cards.
3. **Consequential:** A successful attack on the leader can redistribute 2–3 territories' worth of income in a single turn. But a failed attack wastes Claim Cards, Combat Cards, and Investors while leaving you exposed to other opponents. The mutual casualty mechanic means even successful attacks are costly.
4. **Situational:** In the final round, attacking the leader becomes paramount — there is no future cost to consider. In early rounds, building your own engine is often superior to premature conflict. The turn-order shuffle means you cannot predict who acts first each round, affecting the timing calculus — attacking before a strong opponent's turn prevents them from reinforcing.

---

## 4 · Adding Variety

> *~300 words recommended*

Several mechanisms ensure that each playthrough of *Wolves of Wand Street* feels distinct:

**Card Draw Randomness.** The 48-card deck is shuffled each game. The order in which Economy, Claim, and Combat Cards appear varies, creating different resource availability and action opportunities. A player who draws Claim Cards early will expand aggressively; one who draws Economy Cards will invest in a larger Investor pool.

**Turn Order Shuffle.** Reshuffled every round, the initiative order prevents fixed positional advantages and creates fresh tactical dynamics. Going first in one round means going last in the next, balancing the tempo across the game.

**Starting Territory Choice.** Each player picks one of two Outer territories to start with, creating 2⁴ = 16 possible starting configurations for a four-player game. This choice immediately differentiates each game's territorial landscape.

**Player-Driven Variability.** The free-for-all structure means player interactions are emergent. Temporary alliances, target selection, and aggression timing shift with player personalities, table talk, and in-game power dynamics. No two groups will play the same game.

**Combat Card Uncertainty.** The limited set of six Combat Card templates creates a meta-game of reading opponents. Some players bluff by holding cards defensively; others use them aggressively. This psychological layer evolves across multiple plays as players develop and counter each other's tendencies.

**Draw Pile as Variable Timer.** Game length varies based on Exchange Phase usage. Aggressive cycling accelerates deck depletion, producing shorter games. Conservative play extends the game, allowing more build-up. This creates an emergent pacing dynamic driven by player behaviour.

---

## 5 · Meeting the Design Brief

> *~300 words recommended*

### Requirements Checklist

| Requirement | How It's Met |
|-------------|-------------|
| **Custom deck of cards** | A 48-card custom deck with three categories (18 Economy, 18 Claim, 12 Combat), each with custom names, effects, and artwork. See Appendix A. |
| **3–4 players** | Designed for 3–4 players. With four players, all four starting areas are occupied; with three, one area is neutral, altering early-game dynamics. |
| **2+ distinct resources** | **Gold** (economic — generates Investors, secondary tiebreaker) and **Investors** (military — controls territories, primary combat unit). Each has distinct earning, spending, and strategic roles. |
| **15-min gameplay** | Each turn ≈45 seconds (draw 4, optional exchange, 2 actions, discard). Four players × approximately 20 turns total ≈ 15 minutes. Verified through playtesting. |
| **playingcards.io compatible** | Fully implemented on playingcards.io with custom card images, token zones, and map layout. The `.pcio` file is submission-ready. |

### Experience Goals

| Goal | How It's Achieved |
|------|-------------------|
| **Fellowship** | Competitive free-for-all with adjacency-forced interaction. No passive strategies possible. Temporary alliances of convenience emerge naturally. |
| **Challenge** | Multi-layered decisions: hand management + resource conversion + spatial strategy + combat timing. The two-action limit forces prioritisation under constraint. |
| **Drama** | Draw-pile-as-timer creates escalating tension. Mutual casualty rules ensure battles are costly and dramatic. The final round produces desperate last-stand moments. |

---

## 6 · Production Process

> *~400 words recommended*

### Tools

- **playingcards.io:** The primary digital implementation and online playtesting platform. The `.pcio` file contains the complete game with custom card zones, map layout, and token management, enabling remote playtesting and final submission.
- **LaTeX and Python Scripts:** An automated card asset generation pipeline. Card definitions in `cards_png_assets.tex` are processed through Python scripts in `Assets/Scripts/` to produce PNG card images with consistent formatting, which are then imported into playingcards.io.
- **Paper Prototyping:** Initial playtesting used hand-drawn territories and standard playing cards mapped to game cards (as detailed in §20 of the v0.2 rules). Physical prototypes were essential for testing the simplified v0.2 rules before digital implementation.
- **Git and GitHub:** Version control for all design documents, rules, assets, and the `.pcio` file. The repository history tracks the evolution from v1 to v0.2, providing evidence of iterative design.

### Team Workflow

The team comprised four members — James, Louis, Marcus, and Aidan — with the following division of labour:

- **Louis** authored the initial v1 rule set, providing the foundational game structure including the 52-card design, Influence scoring, Free Actions, and complex card effects.
- **Aidan** led the visual design for all card artwork, creating the custom card illustrations and graphic design that establish the game's aesthetic identity. All team members contributed to card production.
- **James, Louis, Aidan, and Marcus** collectively iterated on the v0.2 rules. Following playtesting, all members contributed suggestions for simplification, action economy reform, and combat balance, converging on the streamlined three-category card system.
- **All members** participated in playtesting, physical prototype construction, and rule refinement throughout the project.

### Timeline

| Phase | Description |
|-------|-------------|
| **Concept & v1 Design** | Louis designed the initial 52-card game with Influence scoring, Free Actions, and unique card effects. |
| **Paper Prototype & Early Playtesting** | Physical prototype built and tested. Three playtests conducted, identifying critical issues: Free Actions undermined action economy, Influence encouraged hoarding, and excessive cognitive load from 52 unique cards. |
| **v0.2 Redesign** | Based on playtesting feedback, the team collectively simplified the game to 48 cards (three categories), removed Influence scoring, eliminated Free Actions, and standardised Combat Card templates. |
| **Physical v0.2 Prototype** | A new physical prototype was built for the simplified rules. Playtesting validated the core design improvements. |
| **Digital Implementation** | Card artwork produced (Aidan), automated asset pipeline built, playingcards.io version assembled with custom cards, map, and tokens. |
| **Final Playtesting & Balancing** | Ongoing playtesting with the digital version to verify balance and timing.

<!-- [PENDING: 以上时间线中的具体日期和里程碑时间点尚未提供。在收到详细时间线后补充。] -->

---

## 7 · Reflection

> *~400 words recommended*

### Strengths

The strongest design achievement is the **three-category card system**. Reducing from 52 unique cards to 18 Economy / 18 Claim / 12 Combat dramatically lowered the learning curve while maintaining strategic depth. Players can now hold the entire card taxonomy in working memory, enabling meaningful bluffing, counterplay, and strategic planning. This was the single largest improvement driven by playtesting.

The **elimination of Free Actions** in v0.2 successfully restored decision tension. In the original design, players could perform unlimited deploy, move, and play operations outside the two-action limit, rendering the action economy meaningless. The v0.2 rule that every meaningful operation costs an action, card, Gold, or Investor makes the two-action limit genuinely constraining.

The **draw-pile-as-timer** mechanic works elegantly. It creates visible urgency without a fixed round counter, varies game length based on player behaviour, and produces a natural dramatic arc as the deck thins. Playtesting confirmed that players experience escalating tension as the game progresses.

The **adjacency-based combat** system creates natural frontlines and meaningful territorial positioning. Combined with the tie-goes-to-defender rule and mutual casualties, aggression is costly enough to prevent reckless attacks but rewarding enough to prevent turtling.

### Areas for Improvement

Playtesting revealed that **territory occupation was too rapid** in the initial v0.2 implementation. The 1 Gold = 1 Investor exchange rate may be too generous, allowing players to fill the map before meaningful conflict can develop. A higher price (e.g., 2 Gold = 1 Investor) would slow expansion and increase the strategic weight of each Investor deployment.

The **defender advantage** may be too strong. Ties favouring the defender, combined with the ability to reinforce from reserve, can produce stalemates where neither side attacks. Restricting reserve reinforcement or adjusting the tie-breaking rule may be necessary.

All three documented playtests were won by Player 4, suggesting a **positional or turn-order advantage** that requires investigation. This may relate to the Hub's accessibility from the fourth starting position or to the dynamics of acting last in the initial round.

### Lessons Learned

The most important lesson was that **simplicity wins**. The biggest improvements came from removing features (Free Actions, Influence scoring, 52 unique cards) rather than adding them. Each removal simultaneously solved a playtesting-identified problem and improved the player experience. This taught us that restraint is a design skill — knowing what to cut is as valuable as knowing what to add.

**Playtesting is irreplaceable.** The three problems identified (Free Actions undermining action economy, Influence hoarding, excessive cognitive load) were not apparent during design. They only surfaced through observing real players interact with the system. The gap between designer intent and player experience can only be bridged through structured external playtesting.

**Every system must create tension.** The original Influence scoring system created perverse incentives — hoarding Influence was more valuable than spending it, leading to passive late-game play. Removing it and making Gold a secondary tiebreaker created better strategic tension by ensuring that resources must be spent to have value.

<!-- [PENDING: 三次 playtest 的具体数据（参与者、得分、观察结果）尚未提供。在收到 playtest 记录后补充详细内容到本节和附录中。] -->

---

## Appendix A: Card Reference

<!-- 
Complete custom card deck. Does NOT count toward word count.
Cards are listed by category with name, effect, and cost (if applicable).
Card images are available in Assets/Cards-png/.
-->

### Economy Cards (18)

| Card Name | Effect | Quantity |
|-----------|--------|----------|
| Petty Cash | Gain 2 Gold | 6 |
| Minor Export | Gain 2 Gold | 4 |
| Small Trade | Gain 3 Gold | 4 |
| Angel Investors | Gain 3 Gold | 2 |
| Economic Dominance | Gain 4 Gold | 2 |

### Claim Cards (18)

| Card Name | Effect | Quantity |
|-----------|--------|----------|
| Claim | Occupy an empty territory or attack an enemy territory | 18 |

### Combat Cards (12)

| Card Name | Type | Effect | Quantity |
|-----------|------|--------|----------|
| Attack +2 | Attack | +2 Battle Strength for this attack | 3 |
| Breakthrough | Attack | If this attack succeeds, defender removes 1 additional Investor | 1 |
| Safe Retreat | Attack | If this attack fails, return 1 committed Investor to reserve | 1 |
| Defence +2 | Defence | +2 Battle Strength for this defence | 3 |
| Fortify | Defence | If this defence succeeds, gain 1 Investor onto the defended territory | 1 |
| Counter | Counter | Cancel the Combat Card just played by the opponent | 2 |
| Time Acceleration | Utility | Perform 2 additional actions this turn | 1 |

### Market Cards (High-Value, Purchasable)

<!-- [PENDING: 以下市场卡牌的效果和费用基于原始 v1 规则。是否需要在 v0.2 中保留市场卡牌？如果保留，请确认最终效果和费用。] -->

| Card Name | Category | Effect | Cost |
|-----------|----------|--------|------|
| Hostile Takeover | Military | Contest a non-adjacent territory this turn | 4 Gold |
| Strike Action | Military | Remove 3–4 Investors from any one territory | 5–6 Gold + 2 Inf |
| Political Coup | Diplomacy | Force one player to hand over one territory of your choice | 4 Inf |
| Corporate Espionage | Intelligence | Look at any player's hand and steal one card | 7 Gold + 4 Inf |
| Market Crash | Economy | Target player loses half their Gold (rounded down) | 4 Gold + 1 Inf |
| Monopoly | Economy | Steal half of your Gold from every other player | 5–10 Gold |
| Mystical Arbitrage | Intelligence | Swap your Gold total with any other player | 4 Inf |
| Arcane Dominion | Intelligence | Copy the effect of any card in the discard pool | 4 Inf |
| Power Play | Diplomacy | Gain Influence equal to the number of clusters you border | 3 Gold + 1–2 Inf |
| Headhunt | Military | Target player loses 1 Investor from each territory | <!-- [PENDING: cost] --> |
| Redeployment | Military | Move all Investors from one territory to another | <!-- [PENDING: cost] --> |
| Branch Office | Economy | Place 1 Investor on each territory you control | <!-- [PENDING: cost] --> |
| Onboarding | Economy | Gain 2 Investors to reserve | <!-- [PENDING: cost] --> |
| Castle | Defence | Territory gains +3 defence strength this round | <!-- [PENDING: cost] --> |
| City | Economy | Territory produces double Gold next round | <!-- [PENDING: cost] --> |
| Hamlet | Economy | Gain 1 Gold per territory you control | <!-- [PENDING: cost] --> |

<!-- [PENDING: 以上卡牌中部分费用尚未确认。请提供最终版本的卡牌效果和费用表。] -->

---

## Appendix B: Map / Board Reference

### Territory Layout

The map consists of 13 territories arranged in four clusters around a central Hub:

```
        NW Outer ─── NW Inner ─── NE Outer
           \            |            /
            \           |           /
             \          |          /
              ── SW Inner ──
               /    Hub    \
              /      |      \
             /       |       \
        SW Outer ─── SW Inner ─── SE Outer
```

<!-- [PENDING: 上述 ASCII 地图仅为示意。请提供正式的地图图示或更准确的连接关系描述。] -->

### Adjacency Table

| Territory | Adjacent To |
|-----------|-------------|
| NW Inner | NW Outer (×2), Hub |
| NW Outer 1 | NW Inner, SW Outer 1 |
| NW Outer 2 | NW Inner, NE Outer 1 |
| NE Inner | NE Outer (×2), Hub |
| NE Outer 1 | NE Inner, NW Outer 2 |
| NE Outer 2 | NE Inner, SE Outer 1 |
| SW Inner | SW Outer (×2), Hub |
| SW Outer 1 | SW Inner, NW Outer 1 |
| SW Outer 2 | SW Inner, SE Outer 2 |
| SE Inner | SE Outer (×2), Hub |
| SE Outer 1 | SE Inner, NE Outer 2 |
| SE Outer 2 | SE Inner, SW Outer 2 |
| Hub | All four Inner territories |

<!-- [PENDING: 以上邻接关系为推断版本。请确认实际 playingcards.io 中的邻接关系是否一致。] -->

### Territory Income

| Territory Type | Gold per Round |
|----------------|---------------|
| Outer | 1 |
| Inner | 2 |
| Hub | 3 |

---

## Appendix C: Quick Reference Card

### Turn Structure (Per Player)

1. **Draw** — Draw 4 cards from the draw pile.
2. **Exchange** — Optionally discard up to 3 cards, draw 1 replacement each.
3. **Action** — Perform up to 2 major actions:
   - Play 1 Economy Card (gain Gold)
   - Play 1 Claim Card to occupy an empty territory
   - Play 1 Claim Card to attack an enemy territory
   - Purchase Investors (spend Gold, add to reserve)
   - Play 1 non-combat Combat Card (if applicable)
4. **Discard** — Hand limit: 6 cards. Discard excess.

### Combat Resolution

1. Attacker plays 1 Claim Card and commits Investors.
2. Defender may reinforce from reserve.
3. Attacker plays up to 1 Combat Card (optional).
4. Defender plays up to 1 Combat Card (optional).
5. **Battle Strength** = Committed Investors + Combat Card modifiers.
6. Higher total wins. **Ties → Defender wins.**
7. **Casualties:** Attacker loses 1 additional Investor (garrison placed). Defender loses 1 Investor (minimum 1 survives).
8. Removed Investors → General Supply (must be repurchased with Gold).

### Resources

| Resource | Earned By | Spent On |
|----------|-----------|----------|
| Gold | Playing Economy Cards; Territory income | Purchasing Investors; Market Cards |
| Investors | Purchasing with Gold | Occupying territories; Attacking; Defending |

### Victory

- **Primary:** Most territories controlled at game end.
- **Tiebreakers:** Most deployed Investors → Most Gold → Most hand cards.