from discount import apply_discount

def calculate_total(prices, discount_percent):
    subtotal = sum(prices)
    final = apply_discount(subtotal, discount_percent)
    return final
