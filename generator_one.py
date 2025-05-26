def infinite_sequence():
    num = 0
    while True:
        # return num
        yield num
        num += 1

infinite = infinite_sequence()

print(infinite)