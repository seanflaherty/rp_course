transactions = [1.09, 23.56, 57.84, 4.56, 6.78]
tax_rate = .05

def price_with_tax(transactions):
    return transactions * (1 + tax_rate)

# try it out
final_costs = map(price_with_tax, transactions)
print(list(final_costs))