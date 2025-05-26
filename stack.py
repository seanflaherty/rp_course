class Stack:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        return type(self)(self.items + other.items)
    
    def __iadd__(self, other):
        self.items.extend(other.items)
        return self
    
    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __len__(self):
        return len(self.items)
    
    def __reversed__(self):
        return type(self)(reversed(self.items))

# try it out

# try 1
# stack = Stack([2, 3, 5, 9, 7])
# print(2 in stack)
# print(10 in stack)
# print(2 not in stack)
# print(10 not in stack)

# try 2
# stack = Stack([1, 2, 3])

# stack += Stack([4, 5, 6])

# print(stack)

# try 3
stack = Stack([1, 2, 3, 4])

print(stack[1])
print(stack[-1])
print(reversed(stack))