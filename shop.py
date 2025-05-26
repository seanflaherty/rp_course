class Product:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def cost(self):
        cost = self.quantity * self.price
        return cost
    
    def __str__(self):
        return f"Product(quantity='{self.quantity}')"

    def __repr__(self):
        return f"Product(quantity='{self.quantity}', price={self.price})"

class Sandwich(Product):
    def __init__(self, quantity, price, filling):
        super().__init__(quantity, price)
        self.filling = filling
    
    def __str__(self):
        return f"Sandwich(quantity='{self.quantity}')"

    def __repr__(self):
        return f"Sandwich(quantity='{self.quantity}', price={self.price}, filling='{self.filling}')"
        

# They sell tea, coffee, and cookies. And now Sandwiches 

tea = Product(1, 2.00)

coffee = Product(2, 3.00)

cookie = Product(6, 1.00)

ham_sandwich = Sandwich(1, 8.00, "ham")

print(ham_sandwich.filling)

print(f"Tea Cost: ${tea.cost():,.2f}, Coffee Cost: ${coffee.cost():,.2f}, Cookie Cost: ${cookie.cost():.2f}")
print(tea.__str__())
print(tea.__repr__())

print(ham_sandwich.__str__())
print(ham_sandwich.__repr__())