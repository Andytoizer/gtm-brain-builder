#!/usr/bin/env python3
"""Create a compact starter GTM Brain repository."""

from __future__ import annotations

import argparse
from pathlib import Path


SECTION_FILES = {
    "company": [
        "what-we-do.md",
        "product-truth.md",
        "approved-claims.md",
        "tone-foundation.md",
    ],
    "icp": [
        "best-customers.md",
        "our-icp.md",
        "personas.md",
        "segments.md",
    ],
    "messaging": [
        "buyer-language.md",
        "objections.md",
        "value-props.md",
        "positioning.md",
        "offers.md",
    ],
    "market": [
        "category.md",
        "competitors.md",
        "alternatives.md",
    ],
    "customers": [
        "customer-list.md",
        "proof-approval.md",
        "top-customers.md",
        "feedback.md",
        "quotes.md",
        "case-study-notes.md",
    ],
    "brand": [
        "brandkit.md",
        "design-resources.md",
        "voice-system.md",
        "speaker-tone-operator.md",
    ],
    "sales": [
        "campaigns.md",
        "campaign-process.md",
        "campaign-results.md",
        "outbound-copy-guide.md",
        "email-examples.md",
    ],
    "systems": [
        "mvp-checklist.md",
        "sources.md",
        "tools.md",
        "source-coverage.md",
        "grill-me.md",
        "automations.md",
        "source-update-log.md",
    ],
    "projects/operator/building-the-brain": [
        "README.md",
    ],
    "session-relay": [
        "README.md",
    ],
    "skills": [
        "README.md",
    ],
    "session-relay/transcripts": [
        ".gitkeep",
    ],
}


def title_from_filename(name: str) -> str:
    if name == ".gitkeep":
        return ""
    return name.removesuffix(".md").replace("-", " ").title()


def write(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def starter_doc(title: str) -> str:
    return f"""# {title}

Status: Empty starter

## Purpose

Describe what belongs here and which sources should feed it.

## Current Context

- Working theory:
- Evidence:
- Questions:
- Do not claim:

## Source Notes

- Source:
- Date range:
- Caveats:
"""


def root_readme(name: str) -> str:
    return f"""# {name}

This is the shared GTM Brain for the company. Use it as an operating brain for marketing, sales, support, CS, product-adjacent GTM work, and agents.

## First Rule: Connect Sources First

Before filling strategy, map the tools in `systems/tools.md` and source coverage in `systems/source-coverage.md`.

## Current Build Phase

Read `systems/mvp-checklist.md` before each session. Until the MVP checklist is complete, focus on building the brain itself, not launching campaigns, operating GTM workflows, or creating downstream website/deck/campaign assets.

## Always-On Grill Me

Use `systems/grill-me.md` before turning evidence into durable interpretation. Ask one pointed question at a time with a current best hypothesis.

## Where Things Live

- `company/`: what we do, product truth, approved claims, tone foundation.
- `icp/`: best customers, ICP, personas, and segments.
- `messaging/`: buyer language, objections, value props, positioning, offers.
- `market/`: category, competitors, and alternatives.
- `customers/`: customer list, proof, quotes, case studies, feedback.
- `brand/`: brandkit, design resources, voice system, speaker tones.
- `sales/`: campaigns, process, results, outbound copy, examples.
- `systems/`: sources, tools, automations, update rules, relay behavior.
- `projects/`: unpublished workspaces.
- `skills/`: reusable agent/operator workflows.

## Update Model

- Direct edit allowed: facts, links, metadata, routing, typos, formatting.
- Propose update: campaign lessons, buyer language, objections, customer notes, proof candidates.
- Owner review required: positioning, ICP, value-prop hierarchy, public proof claims, tone/taste, customer interpretation, major strategy.
"""


def agents_md(name: str) -> str:
    return f"""# Agent Instructions

This repository contains {name}. Start with `README.md`, then read only the smallest relevant doc set.

## Operating Rules

- Treat operators as decision owners, not passive readers.
- Use tools for evidence and Grill-me for interpretation.
- Keep raw evidence out of canonical docs unless summarized with source context.
- Mark unapproved conclusions as `Working theory`.
- Do not read JSONL transcripts by default; use session relay first.
- Read `systems/mvp-checklist.md` before doing work. Respect the current phase and non-goals.

## Common Task Routing

- Tool/source questions: `systems/tools.md`, `systems/sources.md`, `systems/source-coverage.md`.
- Company/product claims: `company/`.
- Customers, proof, and ICP: `customers/`, `icp/`.
- Buyer language, objections, value props: `messaging/`.
- Brand and speaker tone: `brand/`.
- Campaign learnings and outbound: `sales/`.
"""


def systems_docs(name: str) -> dict[str, str]:
    return {
        "systems/mvp-checklist.md": f"""# MVP Checklist

Status: Build the brain MVP

This file keeps agents focused on building {name} before operating from it.

## Current Phase

Build the GTM Brain MVP: source coverage, canonical docs, proof/ICP/messaging/tone/sales memory foundations, and relay handoff.

## In Scope Now

- Map connected tools and access gaps.
- Define source priority and update rules.
- Fill company/product truth with approved vs working claims.
- Build customer/proof/ICP context from evidence.
- Build messaging and market context from buyer language, objections, campaigns, and proof.
- Build brand and speaker-tone profiles.
- Build sales memory from campaign evidence.
- Maintain session relay and next checklist.
- Design refresh workflows after the canonical docs have shape.

## Out Of Scope Until MVP Complete

- Launching campaigns.
- Running sales or marketing operations.
- Building operating dashboards.
- Creating website pages, decks, ads, or outbound campaigns as final deliverables.
- Adding heavy automations that assume the brain is already stable.

## MVP Completion Checklist

- [ ] Source connector inventory is complete enough to know what is connected, partial, blocked, and missing.
- [ ] `systems/sources.md`, `systems/tools.md`, and `systems/source-coverage.md` are usable.
- [ ] Company/product truth has approved, working, question, and do-not-claim sections.
- [ ] Customer/proof and ICP docs are grounded in at least commercial, CRM, usage, and customer evidence where available.
- [ ] Messaging/market docs preserve buyer language and objections before interpretation.
- [ ] Brand and speaker-tone docs separate tone from sales copy.
- [ ] Sales memory distinguishes what ran from what worked.
- [ ] Session relay is updated with decisions, status, and next work.
- [ ] Freshness automation is proposed, not silently applied.

## Next Checklist

1. Start with source connector inventory.
2. Fill the highest-priority empty canonical docs.
3. Ask one Grill-me question before promoting interpretation.
4. Update this checklist and session relay before handoff.
""",
        "systems/grill-me.md": """# Grill Me Protocol

This protocol is always on when evidence needs interpretation.

Ask one pointed question at a time:

```text
Question:
My current best hypothesis:
Why this matters:
What changes depending on your answer:
```

Tools answer what happened. Accountable owners decide what it means.
""",
        "systems/sources.md": """# Sources

Use this file to decide where evidence should come from and how conflicts should be resolved.

## Source Priority

1. Operator or accountable owner direct answers
2. Current product/app reality and approved public materials
3. Customer/prospect evidence
4. GTM system data
5. External research
6. Agent interpretation

Agent interpretation should not overwrite source-backed context.
""",
        "systems/tools.md": """# Tools

Inventory every source system here.

| Tool | Status | Use for | Do not use for |
|---|---|---|---|
| CRM | Unknown | lifecycle, pipeline, account context | product usage truth alone |
| Revenue/Billing | Unknown | commercial value, active customers | buyer meaning alone |
| Product analytics/DB | Unknown | usage, activation, capability checks | public claims without review |
| Support | Unknown | customer pain and requests | revenue truth |
| Email | Unknown | real buyer/customer language and speaker tone | campaign totals |
| Slack/Teams | Unknown | recent context and customer-channel language | final truth alone |
| Calls | Unknown | objections, buyer language, buying reasons | revenue truth |
| Campaign tools | Unknown | copy, audience, replies, performance | current capability truth |
""",
        "systems/source-coverage.md": f"""# Source Coverage

Track what is connected before filling {name}.

## Connected

- TBD

## Partial

- TBD

## Blocked

- TBD

## Missing

- TBD
""",
    }


def relay_doc(name: str) -> str:
    return f"""# Building The Brain

This is the persistent handoff layer for {name}.

Future agents should read this after the root `README.md`. Do not read transcripts by default. Use transcript links only for exact history or missing context.

## Status

- [ ] MVP checklist current
- [ ] Source connector inventory
- [ ] Company core
- [ ] Customer/proof/ICP
- [ ] Messaging/market
- [ ] Brand/voice
- [ ] Sales memory
- [ ] Freshness automation

## Decisions

- TBD

## Next Step

Start with `systems/mvp-checklist.md`, then `systems/tools.md` and `systems/source-coverage.md`.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Human-readable GTM Brain name")
    parser.add_argument("--path", required=True, help="Output directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    write(root / "README.md", root_readme(args.name), args.force)
    write(root / "AGENTS.md", agents_md(args.name), args.force)

    for rel, content in systems_docs(args.name).items():
        write(root / rel, content, args.force)

    for section, files in SECTION_FILES.items():
        for filename in files:
            target = root / section / filename
            if filename == ".gitkeep":
                write(target, "", args.force)
            elif section in {"projects/operator/building-the-brain", "session-relay"} and filename == "README.md":
                write(target, relay_doc(args.name), args.force)
            else:
                write(target, starter_doc(title_from_filename(filename)), args.force)

    print(root)


if __name__ == "__main__":
    main()
