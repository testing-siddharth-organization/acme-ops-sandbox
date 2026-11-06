"""Billing helpers for Acme invoices."""

def invoice_total(lines, tax_rate=0.2):
    subtotal = sum(round(line["qty"] * line["unit_price"]) for line in lines)
    return round(subtotal * (1 + tax_rate), 2)
