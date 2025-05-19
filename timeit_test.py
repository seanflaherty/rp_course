import random
import timeit

TAX_RATE = .08
transactions = [random.randrange(100) for _ in range(100000)]

def get_price(transaction):
    return transaction * (1 + TAX_RATE)

# map
def get_prices_with_map():
    return list(map(get_price, transactions))

# comprehension
def get_prices_with_comprehension():
    return [get_price(transaction) for transaction in transactions]

# loop
def get_prices_with_loop():
        prices = []
        for transaction in transactions:
             prices.append(get_price(transaction))
        return prices

# time it
print("Map: ", timeit.timeit(get_prices_with_map, number=100))
print("Comprehension: ", timeit.timeit(get_prices_with_comprehension, number=100))
print("Loop: ", timeit.timeit(get_prices_with_loop, number=100))
