"""Warehouse client. Pushes one order at a time."""
import json
import urllib.request

WAREHOUSE_URL = "https://warehouse.example.test/orders"
TIMEOUT_SECONDS = 10

def push(order):
    body = json.dumps({"id": order["id"], "sku": order["sku"], "qty": order["qty"]}).encode()
    request = urllib.request.Request(WAREHOUSE_URL, data=body, headers={"content-type": "application/json"})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return response.status == 201
