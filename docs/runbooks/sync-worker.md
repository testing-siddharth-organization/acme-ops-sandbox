# Sync worker runbook

1. Check the warehouse API status first. Timeouts from the warehouse are retried 3 times with exponential backoff (1, 2, 4 seconds).
2. If orders are stuck for more than 30 minutes, page platform.
3. A `KeyError: 'sku'` means the shop API returned an order without line items. Skip the order and file a bug; do not retry.
