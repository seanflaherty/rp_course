def outer_func():
    name = "Pythonista"
    def inner_func():
        print(f"Hello, {name}!")
    inner_func()

# try it our
ret1 = outer_func()
print(ret1)

greeter = outer_func()
print(greeter)