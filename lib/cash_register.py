class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        total_price = price * quantity
        self.total += total_price
        self.last_transaction = total_price
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount != 0:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0.0