def f(key, val, d={}):
    d[key] = val
    return d

f('a', 1)
f('b', 2)

print(f('c', 3)['a'])