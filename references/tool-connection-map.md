# Tool Connection Map

Create `systems/tools.md` and `systems/sources.md` before filling canonical GTM docs.

## Recommended Source Classes

| Source class | Use for | Do not use for |
|---|---|---|
| Operator/accountable owner | Meaning, taste, priority, interpretation, approvals | Raw counts or system state |
| Website/public docs | Current public story and claims | Private strategy or hidden capabilities |
| CRM | lifecycle, pipeline, deals, source fields, notes, owner context | product usage truth by itself |
| Billing/revenue | commercial value, active customers, expansion/churn | buyer meaning or public names without alias cleanup |
| Product DB | current product reality, usage shape, backend truth | public claims without review |
| Product analytics | activation, retention, feature adoption, usage cohorts | revenue or customer meaning alone |
| Support | customer pain, feature requests, friction, proof candidates | commercial truth by itself |
| Email | customer/prospect language, objections, tone samples | campaign performance totals |
| Slack | recent corrections, team context, customer-channel language | final truth without source context |
| Call recordings | buyer language, objections, buying reasons, competitive mentions | revenue truth or final interpretation |
| Outbound tools | tested copy, audiences, reply rates, campaign performance | current product capability without date caveats |
| Docs/Notion/Drive | internal plans and historical context | current public truth when website/app disagrees |
| Design tools | visual source assets, brand-kit drafts, design-system references, Codex import instructions | positioning, proof, or product claims without GTM Brain support |

## First-Pass Connector Checklist

- CRM: HubSpot, Salesforce, Attio, or equivalent.
- Revenue: ChartMogul, Stripe, Chargebee, ProfitWell, or equivalent.
- Product usage: PostHog, Amplitude, Mixpanel, warehouse, or app DB.
- Support/customer: Pylon, Intercom, Zendesk, HelpScout, customer Slack.
- Email: Gmail or Outlook.
- Team comms: Slack or Teams.
- Call recordings: Fathom, Gong, Sybill, Fireflies, Zoom transcripts.
- Campaign tools: Instantly, HeyReach, Smartlead, Customer.io, HubSpot Marketing, LinkedIn ads.
- Docs/design: Notion, Drive, Figma, Claude.ai/design, Codex design workflows, website, brand assets.

## Rule

Use tools to gather evidence. Use Grill-me before turning evidence into durable GTM context.
