from cart import calculate_total

def test_total_with_discount():
    # 3 items totaling 100, with 10% discount = 90
    assert calculate_total([50, 30, 20], 10) == 90.0

def test_no_discount():
    assert calculate_total([50, 30, 20], 0) == 100.0
