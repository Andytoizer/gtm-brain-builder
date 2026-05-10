# GTM Brain Builder

This plugin packages lessons from a production GTM Brain build into a shareable starter system for building another company's version.

The core idea: connect the tools first, then build durable GTM context from source-backed evidence plus human interpretation. The plugin includes specialist agent definitions, skills those agents use as playbooks, an always-on Grill-me decision gate, a Session Relay workflow, and a scaffolding script for a blank GTM Brain repo.

## Fast Start

Create a new brain repo:

```bash
python3 scripts/init_gtm_brain.py "Acme GTM Brain" --path ./Acme-GTM-Brain
```

Then ask Codex:

```text
Use $gtm-brain-builder to build this company GTM brain. Start with tool connections and source coverage.
```

## Plugin Hierarchy

```text
gtm-brain-builder/
  .codex-plugin/plugin.json      # marketplace/plugin metadata
  agents/                        # specialist agent definitions
  skills/                        # reusable playbooks and routing instructions
  references/                    # shared build lessons and rubrics
  scripts/                       # deterministic setup helpers
```

Use the hierarchy like this:

- **Plugin**: the installable package.
- **Agents**: specialist roles that can own a workstream when an agent runtime supports them.
- **Skills**: the procedural knowledge each agent uses.
- **References**: shared context loaded only when needed.
- **Scripts**: deterministic scaffolding.

## Included Agents

- `gtm-brain-orchestrator`: owns phase control, MVP checklist, sequencing, and handoffs.
- `source-connector-agent`: maps connected tools and source coverage.
- `company-core-agent`: builds company/product truth.
- `customer-icp-agent`: builds customers, proof, ICP, personas, and segments.
- `messaging-market-agent`: builds buyer language, objections, value props, and market context.
- `brand-voice-agent`: builds brand guidance and speaker-tone profiles.
- `sales-memory-agent`: builds sales memory and campaign learnings.
- `freshness-automation-agent`: designs recurring refresh workflows.

## Included Skills

- `gtm-brain-builder`: orchestrates the build.
- `source-connector-inventory`: maps tools, source priority, and access gaps.
- `company-core-agent`: playbook for company definition, product truth, claims, and tone foundation.
- `customer-icp-agent`: playbook for customer, proof, ICP, persona, and segment context.
- `messaging-market-agent`: playbook for buyer language, objections, value props, positioning, competitors, and alternatives.
- `brand-voice-agent`: playbook for brand guidance and separate speaker-tone profiles.
- `sales-memory-agent`: playbook for campaign memory, outbound copy learnings, sales process, and offers.
- `freshness-automation-agent`: playbook for recurring refresh workflows.
- `grill-me`: asks one pointed question before interpretation becomes durable truth.
- `session-relay`: keeps long builds resumable without rereading transcripts by default.

## Build Biases

- Start with connected sources: CRM, revenue, product usage, support, email, Slack, call recordings, campaign tools, docs, and public website.
- Define the MVP checklist before doing section work so agents stay focused on building the brain before operating from it.
- Keep raw evidence, working theories, proposed changes, and approved truth separate.
- Ask the operator for meaning. Tools can show what happened; accountable owners decide what it means.
- Make downstream assets consult the brain. Do not organize the brain around one campaign, website, deck, or outbound push.
- Automate refreshes only after the canonical sections have enough shape.

## Public Packaging Notes

This repo intentionally ships reusable workflows, templates, and generic lessons. It does not include private GTM data, customer evidence, credentials, transcripts, or company-specific source exports.
