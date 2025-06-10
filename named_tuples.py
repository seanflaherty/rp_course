from collections import namedtuple, OrderedDict


# Point
Point = namedtuple("Point", "x y")

# using it
point = Point(2, 4)
print(point.x, point.y)
print (point[0], point[1])

# dictionary for arguments
parms = {
    "x" :5,
    "y" :6,
}
p_dict = Point(**parms)
print(p_dict.x, p_dict.y)

# auto-renaming of arguments
columns = "_id name class name"
Passenger = namedtuple("Passenger", columns, rename=True)
p = Passenger(1234, "Jake", "Business", "Jake Doe")

# default arguments
Developer = namedtuple("Developer", "name level language", defaults=["Junior", "Python"])

Developer1 = Developer("John")
Developer2 = Developer("Jane", language="Ruby")

print(Developer1.name, Developer1.level, Developer1.language)
print(Developer2.name, Developer2.level, Developer2.language)

# module argument
Point2 = namedtuple("Point2", "x y", module="custom")
print(Point2.__module__)

