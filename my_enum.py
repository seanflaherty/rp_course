def my_enum(sequence, start=0):
    count = start
    for item in sequence:
        yield count, item
        count += 1

# try it out
seasons = ["Spring", "Summer", "Fall", "Winter"]
start = 1
counted_seasons = my_enum(seasons, start)
# try 1
print("Try 1 \n")
for val in counted_seasons:
    print(val)

# try 2
print("Try 2 \n")
for val in counted_seasons:
    print(val)