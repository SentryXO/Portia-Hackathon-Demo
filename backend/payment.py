def process_payment(amount, card_number, cvv):
    # BUG: No error handling
    charge = payment_gateway.charge(card_number, amount)
    return charge.transaction_id  # Will crash if charge fails
    
def calculate_total(items):
    # BUG: No validation
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total