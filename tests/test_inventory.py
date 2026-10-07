from inventory import apply_discount, average_price, total_price


def test_total_price_uses_quantity():
    assert total_price([{"price": 10.0, "qty": 3}, {"price": 2.5, "qty": 2}]) == 35.0


def test_total_price_empty():
    assert total_price([]) == 0


def test_apply_discount():
    assert apply_discount(200.0, 25) == 150.0


def test_average_price():
    assert average_price([{"price": 10.0, "qty": 1}, {"price": 20.0, "qty": 1}]) == 15.0


def test_average_price_empty_list():
    assert average_price([]) == 0.0
