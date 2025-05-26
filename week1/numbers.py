class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("__add__ called")
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, int | float):
            return Number(self.value + other)
        
        else:
            raise TypeError("unsupported operand type for +")
    
    def __radd__(self, other):
        print("__radd__ called")
        return self.__add__(other)
    
# trying it out
five = Number(5)
ten = Number(10)
fifteen = five + ten

print(fifteen.value)

six = five + 1
print(six.value)

twelve = 2 + ten
print(twelve.value)