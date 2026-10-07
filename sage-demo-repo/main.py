from inventory import apply_discount, average_price, total_price

ITEMS = [
    {"name": "keyboard", "price": 49.99, "qty": 2},
    {"name": "mouse", "price": 19.50, "qty": 3},
    {"name": "cable", "price": 4.25, "qty": 10},
]


def main():
    total = total_price(ITEMS)
    print(f"Items in stock : {len(ITEMS)}")
    print(f"Total value    : ${total:.2f}")
    print(f"After 10% off  : ${apply_discount(total, 10):.2f}")
    print(f"Avg unit price : ${average_price(ITEMS):.2f}")


if __name__ == "__main__":
    main()
