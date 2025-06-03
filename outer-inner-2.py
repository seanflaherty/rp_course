def outer():
    def inner():
        print(message)

    message = 'hello'
    inner()
    message = 'world'
    inner()
    return inner

# try it out
inner_returned = outer()
inner_returned()