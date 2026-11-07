"""Acme sync worker: pulls orders from the shop API and pushes them to the warehouse."""
import time

import os

RETRY_LIMIT = int(os.environ.get("SYNC_RETRIES", "0"))

def sync_orders(client, warehouse):
    for order in client.fetch_orders():
        for attempt in range(RETRY_LIMIT):
            try:
                warehouse.push(order)
                break
            except TimeoutError:
                time.sleep(2 ** attempt)
