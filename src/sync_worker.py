"""Acme sync worker: pulls orders from the shop API and pushes them to the warehouse."""
import time

RETRY_LIMIT = 3

def sync_orders(client, warehouse):
    for order in client.fetch_orders():
        for attempt in range(RETRY_LIMIT):
            try:
                warehouse.push(order)
                break
            except TimeoutError:
                time.sleep(2 ** attempt)
