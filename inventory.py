"""Tiny inventory toolkit (demo target for S.A.G.E.)."""


def total_price(items):
    """Total value of stock: sum of price * qty for every item."""
    total = 0.0
    for item in items:
        total += item["price"] * item.get("qty", 1)
    return round(total, 2)


def apply_discount(price, percent):
    """Price after applying a percentage discount."""
    discounted = price * (1 - percent / 100)
    return round(discounted, 2)


def average_price(items):
    """Mean unit price; 0.0 for an empty list."""
    if not items:
        return 0.0
    return round(sum(i["price"] for i in items) / len(items), 2)
