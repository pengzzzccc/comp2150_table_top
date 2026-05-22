# Design Document Review Rubric

> **Purpose:** Team members read the Design Doc (`Design_Doc.md`), use this rubric to identify issues, then generate an AI prompt to fix them.
>
> **How to use:**
> 1. Read through `Design_Doc.md` carefully.
> 2. For each checklist item below, mark ✅ (good), ⚠️ (needs improvement), or ❌ (missing/incorrect).
> 3. In the **"Issues Found"** column, briefly describe what's wrong.
> 4. After completing all checks, fill in the **AI Prompt Template** at the bottom with your findings.
> 5. Send the filled prompt to an AI assistant to get targeted revisions.

---

## Part A: COMP2150 Rubric Alignment Check

> *Reference: `Doc/COMP2150_Tabletop_Game_Description.pdf`*

### A1. Game Design (25%)

| # | Criterion | Check | Status | Issues Found |
|---|-----------|-------|--------|-------------|
| 1 | Game design capitalises on constraints | Does the doc explain how constraints (15-min limit, 3-4 players, custom deck) became design advantages? | | |
| 2 | Finely-tuned mechanics | Are mechanics described with enough detail that a reader could implement them? | | |
| 3 | Engaging dynamics | Does the doc explain what dynamics emerge from the mechanics (not just what the mechanics are)? | | |
| 4 | Expertly balanced interesting choices | Are the interesting decisions in §3 genuinely balanced? Are all options viable? | | |
| 5 | Player experience goals satisfied | Is there clear evidence that Fellowship, Challenge, and Drama are achieved? | | |
| 6 | Form and fiction readability | Are card names, territory names, and game terminology consistent and clear? | | |
| 7 | Professional level clarity | Could a marker unfamiliar with the game understand the rules from this doc alone? | | |

### A2. Game Communication (25%)

| # | Criterion | Check | Status | Issues Found |
|---|-----------|-------|--------|-------------|
| 8 | Documentation encapsulates game design | Does the doc cover all aspects: mechanics, dynamics, decisions, experience? | | |
| 9 | Mobilises relevant theory | Does the doc reference game design theory (MDA, interesting choices, etc.)? | | |
| 10 | Depth of insight | Does the doc explain WHY decisions were made, not just WHAT they are? | | |
| 11 | Production processes outlined | Is §6 specific about tools, roles, and workflow? | | |
| 12 | Evidence of forward planning | Does the timeline show intentional progression, not just chronology? | | |
| 13 | Reflections are actionable | Does §7 say "if we did this again, we would..." not just "this could be better"? | | |

### A3. Playtesting Design (25%)

| # | Criterion | Check | Status | Issues Found |
|---|-----------|-------|--------|-------------|
| 14 | At least 3 distinct playtests | Are 3 separate playtests documented with different design questions? | | |
| 15 | Design questions per playtest | Does each playtest have a clear, specific question it's trying to answer? | | |
| 16 | Mixed-methods testing | Is there evidence of both physical prototype AND digital testing? | | |
| 17 | Methodology described | Is the data collection method (observation, survey, scores) specified? | | |
| 18 | Instruments included | Are raw data, survey templates, or observation checklists in the appendices? | | |

### A4. Playtesting Execution (25%)

| # | Criterion | Check | Status | Issues Found |
|---|-----------|-------|--------|-------------|
| 19 | Multiple sessions per playtest | Does each playtest have 2+ sessions (pass) or 4+ sessions (HD)? | | |
| 20 | External participants | Were playtests conducted with people outside the team? | | |
| 21 | Raw results in appendices | Are actual scores, survey responses, or observation notes included? | | |
| 22 | Iteration evidence | Does the doc show "Playtest 1 → changed X → Playtest 2 confirmed Y"? | | |
| 23 | Thoughtful application | Are playtesting results clearly linked to specific design changes? | | |

---

## Part B: Section-by-Section Review

### B1. §1 Target Experience (~800 words)

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 24 | High Concept (2-3 sentences) | Does it include theme, genre, player count, core fantasy? | | |
| 25 | Fellowship | Does it describe competitive/cooperative dynamic and what drives interaction? | | |
| 26 | Challenge | Does it describe intellectual AND social challenges separately? | | |
| 27 | Drama | Does it describe the dramatic arc (beginning, middle, end)? | | |
| 28 | Fantasy | Does it describe the world/setting and how form supports fiction? | | |
| 29 | Word count | Is it approximately 800 words (±200)? | | |

### B2. §2 Core Gameplay (~1200 words)

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 30 | 3+ core systems identified | Are Economy, Land/Deployment, and Contest systems clearly separated? | | |
| 31 | Each system has mechanics | Is the "how it works" described with enough detail? | | |
| 32 | Each system has design intent | Is the "why it exists" explained? | | |
| 33 | System interactions described | Does the doc explain how systems connect to each other? | | |
| 34 | Additional mechanics covered | Are supporting mechanics (turn order, draw pile timer, etc.) described? | | |
| 35 | Word count | Is it approximately 1200 words (±300)? | | |

### B3. §3 Interesting Decisions (~1500 words)

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 36 | 3-5 decisions identified | Are there at least 3 distinct decisions? | | |
| 37 | Each decision has Balanced analysis | Are options roughly equally viable? Is this convincing? | | |
| 38 | Each decision has Informed analysis | Does the player have enough info? What's uncertain? | | |
| 39 | Each decision has Consequential analysis | What are the stakes? What happens if you choose wrong? | | |
| 40 | Each decision has Situational analysis | How does context change the value of options? | | |
| 41 | Word count | Is it approximately 1500 words (±300)? | | |

### B4. §4 Adding Variety (~300 words)

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 42 | Random elements described | Are card shuffle, turn order randomisation, etc. covered? | | |
| 43 | Player-driven variability | Does it explain how player behaviour creates different games? | | |
| 44 | Replayability argument | Is there a convincing case that each game feels different? | | |
| 45 | Word count | Is it approximately 300 words (±100)? | | |

### B5. §5 Meeting the Design Brief (~300 words)

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 46 | Custom deck requirement | Is it explicitly addressed? | | |
| 47 | 3-4 players requirement | Is it explicitly addressed? | | |
| 48 | 2+ resources requirement | Are Gold and Investors described as distinct resources? | | |
| 49 | 15-min gameplay requirement | Is there evidence (timing calculation or playtest data)? | | |
| 50 | playingcards.io compatibility | Is the .pcio file referenced? | | |
| 51 | Experience goals (Fellowship, Challenge, Drama) | Are all three addressed with specific evidence? | | |
| 52 | Word count | Is it approximately 300 words (±100)? | | |

### B6. §6 Production Process (~400 words)

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 53 | Tools described | Are playingcards.io, prototyping tools, and other tools listed? | | |
| 54 | Team roles described | Are all 4 members (James, Louis, Marcus, Aidan) mentioned with roles? | | |
| 55 | Timeline included | Is there a clear chronology of milestones? | | |
| 56 | Challenges described | Are obstacles and how they were overcome mentioned? | | |
| 57 | Word count | Is it approximately 400 words (±100)? | | |

### B7. §7 Reflection (~400 words)

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 58 | Strengths identified | Are at least 3 specific strengths described? | | |
| 59 | Areas for improvement | Are at least 2 specific weaknesses described honestly? | | |
| 60 | Lessons learned | Are there actionable takeaways for future projects? | | |
| 61 | Playtest-informed | Are reflections grounded in playtesting data, not just opinion? | | |
| 62 | Word count | Is it approximately 400 words (±100)? | | |

### B8. Appendices

| # | Item | Check | Status | Issues Found |
|---|------|-------|--------|-------------|
| 63 | Appendix A: Complete card list | Are all cards listed with effects and costs? | | |
| 64 | Appendix A: Card images referenced | Are card images available and linked? | | |
| 65 | Appendix B: Map/Land layout | Is the territory structure clearly presented? | | |
| 66 | Appendix B: Adjacency/income info | Are all mechanical details included? | | |
| 67 | Appendix C: Quick reference | Can a new player use it during gameplay? | | |
| 68 | Appendix D: Playtest data | Are raw results and instruments included? | | |

---

## Part C: PENDING Items Check

| # | PENDING Item in Doc | Status | Action Needed |
|---|---------------------|--------|--------------|
| 69 | §6 Timeline: specific dates | | Provide actual dates for each milestone |
| 70 | §7 Reflection: playtest data | | Provide 3 playtest results (scores, observations) |
| 71 | Game rules alignment | | Verify all rules in Design Doc match the actual Super Quickplay rules |

---

## Part D: Total Score Estimate

| Component | Items | ✅ Count | ⚠️ Count | ❌ Count | Estimated Grade |
|-----------|-------|---------|---------|---------|----------------|
| A1. Game Design | 1-7 | | | | |
| A2. Game Communication | 8-13 | | | | |
| A3. Playtesting Design | 14-18 | | | | |
| A4. Playtesting Execution | 19-23 | | | | |
| B. Section Quality | 24-68 | | | | |
| C. PENDING Items | 69-71 | | | | |
| **Total** | | | | | |

**Grade Guide:**
- **Outstanding (85-100%):** Most items ✅, very few ⚠️ or ❌
- **Distinction (75-84%):** Most items ✅, some ⚠️, no ❌
- **Credit (65-74%):** Mix of ✅ and ⚠️, few ❌
- **Pass (50-64%):** Many ⚠️, some ❌
- **Fail (<50%):** Many ❌

---

## AI Prompt Template

> **Instructions:** After completing the review above, copy the template below, fill in the bracketed sections with your specific findings, and send it to an AI assistant.

```
You are helping revise a COMP2150 university assignment Design Document for a tabletop game called "Wolves of Wand Street".

## Context
- The game is a card-driven area-control game for 3-4 players, ~10 min per game
- It uses simultaneous action phases, independent per-player draw piles, and simplified contest mechanics
- The full rules are in the attached file: [Super Quickplay rules]
- The current Design Doc is in the attached file: [Design_Doc.md]
- The COMP2150 rubric requires 4 equally weighted components: Game Design (25%), Game Communication (25%), Playtesting Design (25%), Playtesting Execution (25%)

## What Needs Fixing
[Paste your ⚠️ and ❌ items from the review rubric here, grouped by section]

## Specific Requests
1. [First specific change needed]
2. [Second specific change needed]
3. [Third specific change needed]
...

## Constraints
- Total word count for §1-§7 should be approximately 5000 words
- Appendices do NOT count toward word count
- The document should be written in [English/Chinese]
- The document should reference game design theory where appropriate (MDA framework, interesting choices, etc.)
- All playtesting claims must be grounded in actual data (provide PENDING markers where data is missing)
- The tone should be professional but not overly academic — this is a game design course, not a research paper

## Output Format
- Provide the revised text for each section that needs changes
- Use markdown formatting consistent with the existing document
- Mark any remaining gaps with: <!-- [PENDING: description of what's needed] -->
```

---

## Example Usage

**Scenario:** Team member Alex reads the Design Doc and finds:
- §3 only has 3 decisions (needs 4-5)
- §7 doesn't mention specific playtest scores
- No game design theory is referenced anywhere

**Alex's filled prompt:**

```
You are helping revise a COMP2150 university assignment Design Document for a tabletop game called "Wolves of Wand Street".

## Context
[copy as-is]

## What Needs Fixing
### §3 Interesting Decisions
- ❌ Only 3 decisions listed (need 4-5)
- ⚠️ Decision 3 "Draw Card Timing" analysis is shallow — the Balanced section doesn't explain why Redeployment is as valuable as holding Investors

### §7 Reflection
- ❌ No specific playtest scores or data mentioned
- ⚠️ "Lessons Learned" section is generic — needs specific examples from playtesting

### Game Communication
- ❌ No game design theory referenced (MDA framework, interesting choices, resource scarcity, etc.)

## Specific Requests
1. Add 2 more interesting decisions to §3 (e.g., "When to use Market Cards" and "Target selection in contests")
2. Add playtest score data to §7 with [PENDING] markers where actual scores are missing
3. Add theory references throughout: MDA in §2, "interesting choices" in §3, information asymmetry in §3.4

## Constraints
[copy as-is]