class Item:
    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # run validations
        assert price >= 0, f"Price {price} is not greater than on equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 20, 5)
item5 = Item("Keyboard", 80, 5)

print(Item.all)
