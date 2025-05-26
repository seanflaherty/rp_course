class TestIterable:
    def __init__(self, data):
        self.data = list(data)

test = TestIterable([2, 4, 6, 8])

for value in test.data:
    print(value)