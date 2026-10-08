# Chief Sales Officer for Orgo

A persistent Hermes sales co-founder that keeps real conversations, deals and commitments moving. Built for the existing Content Studio computer, with Slack as the accountability channel and an independent Boppy app instance.

**Every active opportunity has an owner, evidence, next action and due date. Every reported outcome has a receipt.**

The CSO reconciles email, LinkedIn replies, bookings, calls and handoffs from AI Go-to-Market and Revenue Partner. It separates buyers, partners and clients; drives daily follow-ups; proposes quotas; reviews KPIs; tracks call/transcription gaps; prepares referral asks and verified proof-page updates.

## Included

- Complete [Hermes identity](profiles/SOUL.md) and [operating skill](skills/chief-sales-officer/SKILL.md).
- Sales, partner and client pipeline rules, team ownership and daily/weekly runbooks.
- SQLite recovery ledger with idempotent event ingestion, evidence-gated stage changes, follow-up ownership, due-work reviews and adapter-request receipts.
- Isolated overlay installer that backs up the old Content Studio identity and preserves credentials and existing runtime.
- Slack Socket Mode manifest and connection instructions.
- Tests and CI. No new Python dependencies for the ledger.

## Install on the existing computer

```bash
./orgo/setup.sh
./orgo/verify.sh
python3 cso/ledger.py --db ~/.hermes/cso/pipeline.db review
```

Follow [START-HERE.md](START-HERE.md). Existing runtimes are inspected and preserved, not downgraded to an older template release. This repository does not create or buy a computer.

## Deployment status and honest limits

The local journal and Hermes brief work independently of business connectors. CRM writes, shared tasks, email/LinkedIn/calendar imports, agent dispatch, transcription, Slack reminders and proof publication need verified integration mappings and authorized executors. Queued requests are not completed external actions. The example integration contract is disabled until those connections are verified. Never infer live coverage from this repository's tests.

## Design lineage

The October 8, 2026 review compared `true-revenue-partner`, `affiliate-manager-agent`, `revenue-partner-orgo` and `ai-cofounder-orgo`. True Revenue Partner and Affiliate Manager provide relationship context, sourced facts, call commitments, portfolio reviews and stage discipline. Co-Founder supplies the newer reviewed Orgo deployment pattern. This project uses those operating ideas with a narrower CSO identity; it preserves the runtime already on Content Studio.

See [OPERATING-MODEL.md](docs/OPERATING-MODEL.md), [SECURITY.md](SECURITY.md) and [integration.example.json](integration.example.json).

```bash
python3 -m unittest discover -s tests -v
```
