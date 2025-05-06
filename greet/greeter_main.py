from greet import Greeter

informal_greeter = Greeter("Pythonista")
print(informal_greeter.greet())

formal_greeter = Greeter("dave", True)
print(formal_greeter.greet())