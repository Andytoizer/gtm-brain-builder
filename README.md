# GTM Brain Builder

Built by Andy Toizer — I write [Agent Operator](https://agentoperator.substack.com/), a newsletter about what it actually looks like to build real systems with coding agents as a non-engineer, using live company data.

A GTM Brain is a shared operating context for marketing, sales, support, CS, founders, and AI agents. It captures what your company does, who you sell to, what customers actually say, what proof is usable, what messaging works, and which sources should be trusted.

GTM Brain Builder creates the repo structure, starts with real tools and source coverage, uses specialist agents and skills to fill each section, and keeps the work grounded with Grill-me questions, an MVP checklist, and session handoffs.

It was originally built for [Freckle.io](https://www.freckle.io/)'s company GTM brain, then repurposed into a public plugin anyone can use to build their own version.

## Why This Exists

Most GTM docs become one of three things:

- A pile of old notes nobody trusts.
- A campaign workspace that only helps with the next launch.
- A generic wiki that sounds polished but is not grounded in real customer and system evidence.

GTM Brain Builder is designed to avoid that.

The core principle is simple:

```text
Connect the tools first.
Use evidence to sharpen questions.
Use human judgment to decide meaning.
Store the durable truth in the brain.
```

## What It Builds

The scaffold creates a GTM Brain repo with sections like:

```text
company/       what you do, product truth, approved claims
icp/           best customers, ICP, personas, segments
customers/     customer list, proof, quotes, feedback
messaging/     buyer language, objections, value props, positioning
market/        category, competitors, alternatives
brand/         brand guidance, design-system brief, speaker-tone profiles
sales/         campaign memory, outbound copy guide, sales learnings
systems/       sources, tools, MVP checklist, automations
session-relay/ handoff notes and transcript archive policy
```

The most important generated file is:

```text
systems/mvp-checklist.md
```

That checklist keeps the agent focused on building the brain before drifting into operating GTM, launching campaigns, making dashboards, or creating downstream assets.

## Install

The repo ships two manifests so the same plugin works under both runtimes:

- `.codex-plugin/plugin.json` for Codex
- `.claude-plugin/plugin.json` (and `.claude-plugin/marketplace.json`) for Claude Code

### Codex

Clone the repo into your Codex plugin path; the `.codex-plugin/plugin.json` manifest registers it.

```bash
git clone https://github.com/Andytoizer/gtm-brain-builder.git
cd gtm-brain-builder
```

### Claude Code

Add the repo as a plugin marketplace, then install the plugin:

```text
/plugin marketplace add Andytoizer/gtm-brain-builder
/plugin install gtm-brain-builder@gtm-brain-builder
```

The second `@gtm-brain-builder` is the marketplace name from `.claude-plugin/marketplace.json`.

## Fast Start

Create a new GTM Brain:

```bash
python3 scripts/init_gtm_brain.py "Acme GTM Brain" --path ./Acme-GTM-Brain
```

Then start the build:

```text
Codex:        Use $gtm-brain-builder to build this company GTM Brain.
              Start with tool connections and source coverage.

Claude Code:  /gtm-brain-builder Build this company GTM Brain.
              Start with tool connections and source coverage.
```

In Claude Code you can also describe the goal in plain English — the orchestrator skill auto-triggers from its description without needing the slash command.

## The First Session

The first session should not start with positioning or campaigns. It should start with source coverage.

Ask the agent to map:

- CRM: HubSpot, Salesforce, Attio, etc.
- Revenue/billing: ChartMogul, Stripe, Chargebee, etc.
- Product usage: PostHog, Amplitude, Mixpanel, warehouse, app DB.
- Support/customer conversations: Pylon, Intercom, Zendesk, customer Slack.
- Email and team comms: Gmail, Outlook, Slack, Teams.
- Call recordings: Fathom, Gong, Sybill, Zoom transcripts.
- Campaign tools: Instantly, HeyReach, Smartlead, Customer.io, ads.
- Docs and brand sources: Notion, Drive, website, Figma, Claude.ai/design, Codex design workflows, public docs, brand assets.

The output should be:

```text
systems/tools.md
systems/sources.md
systems/source-coverage.md
```

Each source should say what it is trusted for and what it should not be used for.

## Design System With Claude.ai/Design And Codex

When the brain has enough company, ICP, messaging, proof, and tone context, the agent can help the operator prepare the right design brief, use [Claude.ai/design](https://claude.ai/design) or a Codex design workflow, and import the approved design system back into the GTM Brain.

Use this flow:

1. Gather the source-backed brand brief from the GTM Brain: `company/product-truth.md`, `company/approved-claims.md`, `icp/`, `messaging/`, `customers/proof-approval.md`, `brand/voice-system.md`, and any existing website, deck, Figma, Canva, logo, or screenshot assets.
2. Ask `$design-system-agent` to prepare `brand/design-system-brief.md` with audience, category, desired perception, tone boundaries, visual references, proof constraints, required outputs, and explicit do-not-claim rules.
3. Open `https://claude.ai/design`, create a brand-kit or design-system project, paste the brief, and upload approved visual assets. If the next step is implementation, ask the agent to convert the approved brief into Codex instructions for tokens, components, CSS, slides, or site assets.
4. Ask the design tool for brand-kit/design-system outputs: logo usage, color palette with hex values, typography recommendations, layout rules, image style, component examples, slide/social examples, and do/don't examples.
5. Review the output with Grill-me before treating it as durable taste. Store approved decisions in `brand/brandkit.md`, project links and exports in `brand/design-resources.md`, import instructions in `brand/design-system-brief.md`, and voice implications in `brand/voice-system.md`.

Claude.ai/design and Codex can help turn approved strategy into usable visual direction and implementation instructions. They should not invent positioning, customer proof, or product claims that are not already supported by the brain.

## How The Agent System Works

This plugin has a hierarchy:

```text
Plugin
  agents/      specialist roles that own workstreams
  skills/      playbooks those agents follow
  references/  shared lessons and rubrics
  scripts/     deterministic helpers
```

The orchestrator agent owns the overall build:

- Maintains the MVP checklist.
- Chooses the next section to build.
- Delegates to specialist agents when the runtime supports it.
- Uses Grill-me before promoting interpretation into durable truth.
- Updates session relay before handoff.

Specialist agents own specific sections:

- `source-connector-agent`: connected tools and source coverage.
- `company-core-agent`: company/product truth and claims.
- `customer-icp-agent`: customers, proof, ICP, personas.
- `messaging-market-agent`: buyer language, objections, positioning, market.
- `brand-voice-agent`: brand and speaker-tone profiles.
- `design-system-agent`: design-system briefs, Claude.ai/design or Codex design workflows, and import guidance.
- `sales-memory-agent`: campaigns, sales memory, outbound lessons.
- `freshness-automation-agent`: recurring refresh workflows.

Skills are the procedural playbooks those agents use. If the runtime does not spawn separate agents, the main Codex/Claude Code agent can still use the same skills sequentially.

## The Build Order

The recommended order is:

1. Lock the operating rules: MVP checklist, source priority, Grill-me, session relay.
2. Inventory connected tools and source coverage.
3. Fill company/product truth.
4. Build customer/proof and ICP from commercial, CRM, usage, and customer evidence.
5. Build messaging and market context from buyer language, objections, campaigns, and proof.
6. Build brand and speaker-tone profiles.
7. Create the design-system brief and import workflow when visual systems are needed.
8. Build sales memory and campaign learnings.
9. Design recurring freshness workflows.

This order matters because it keeps the brain grounded. Campaigns, decks, website copy, and sales assets should consult the brain after it has enough source-backed shape.

## Grill-me

Grill-me is the decision-quality layer.

The agent should ask one pointed question at a time when evidence needs interpretation:

```text
Question:
My current best hypothesis:
Why this matters:
What changes depending on your answer:
```

Tools answer what happened. Operators decide what it means.

Use Grill-me before changing:

- Positioning
- ICP
- Value-prop hierarchy
- Customer proof claims
- Tone/taste
- Major GTM strategy

## Session Relay

Long builds need continuity. Session relay keeps a short handoff file as the source of truth and stores transcript links only for deep reference.

Normal pickup should read:

```text
README.md
AGENTS.md
systems/mvp-checklist.md
session-relay/README.md
```

It should not read full JSONL transcripts by default.

## What Good Looks Like

A useful GTM Brain is not just full. It is trustworthy.

It should clearly separate:

- `Approved`: reviewed durable truth.
- `Working theory`: plausible but not final.
- `Evidence`: source-backed observations.
- `Question`: needs operator or owner review.
- `Do not claim`: unsafe, stale, or unsupported claims.

It should also separate:

- Speaker tone from sales copy.
- Design-system rules from unreviewed generated design drafts.
- Customer names from approved proof claims.
- Raw evidence from durable interpretation.
- Building the brain from operating GTM.

## Public Package Scope

This repo intentionally ships reusable workflows, templates, and generic lessons. It does not include private GTM data, customer evidence, credentials, transcripts, or company-specific source exports.

## Validate Locally

Check the plugin manifests:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
```

Test the scaffold:

```bash
rm -rf /tmp/Test-GTM-Brain
python3 scripts/init_gtm_brain.py "Test GTM Brain" --path /tmp/Test-GTM-Brain
test -f /tmp/Test-GTM-Brain/systems/mvp-checklist.md
```

Check for accidental private data before publishing changes:

```bash
rg -n "api[_-]?key|secret|password|token|/Users/|\\.env|customer export|transcript" .
```

## License

MIT
