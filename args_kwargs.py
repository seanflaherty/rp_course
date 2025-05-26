def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

def concatenate(**kwargs):
    result = ""

    for arg in kwargs.values():
        result += arg
    return result

# try it out
ans = my_sum(1, 2, 3)
print("\n", ans)

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))