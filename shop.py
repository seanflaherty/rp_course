class Product:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def cost(self):
        cost = self.quantity * self.price
        return cost

# He sells tea, coffee, and cookies. 

tea = Product(1, 2.00)

coffee = Product(2, 3.00)

cookie = Product(6, 1.00)

print(f"Tea Cost: ${tea.cost(),.2f}, Coffee Cost: ${coffee.cost()}, Cookie Cost: ${cookie.cost()}")