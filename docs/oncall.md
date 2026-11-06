# On-call

| component | owner team | GitHub handle | escalation |
| --- | --- | --- | --- |
| sync worker (`src/sync_worker.py`) | platform | @platform-oncall | page within 15 minutes |
| billing (`src/billing.py`) | billing | @billing-oncall | post in #billing, page only for refunds over $10,000 |
| warehouse client (`src/warehouse.py`) | fulfillment | @fulfillment-oncall | next business day unless orders are stuck |
| docs | developer experience | @devex | no page |

Severity:

- sev1: customers cannot place or receive orders, or money moves wrongly.
- sev2: a component is degraded but has a workaround.
- sev3: cosmetic, docs, or internal tooling.
