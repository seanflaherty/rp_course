class Greeter:
    def __init__(self, name, formal = False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Good mprmint, {self.name}!")
        else:
            print(f"Hello, {self.name}!")
