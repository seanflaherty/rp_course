import turtle
from collections.abc import Sequence

class ShapePoints(Sequence):
    def __init__(self, points):
        self.points = points
        if points and self.points[0] != self.points[-1]:
            self.points.append(self.points[0])

    def __repr__(self):
        return f"ShapePoints({self.points})"
    
    def __getitem__(self, index):
        return self.points[index]
    
    def __len__(self):
        if self.points:
            return len(self.points) -1
        return 0
    
    def __iter__(self):
        return iter(self.points)
    
    def count(self, value):
        return self.points[:-1].count(value)
    
    def __contains__(self, item):
        print("Checking if item is in SahapePoints.")
        return item in self.points
    


# use it
triangle = ShapePoints([(100, 100), (-200, 100), (-200, -200)])
# print(triangle.points)
print(triangle)
print(triangle[0])
print(triangle[:2])
print ((100, 100) in triangle)
print(sorted(triangle))
print ("Is triangle an instance of Sequence?: ", isinstance(triangle, Sequence))

another_shape = ShapePoints([])
print(another_shape)
print(bool(another_shape))

for point in triangle:
    print(point)

# draw using turtle
drawn_triangle = ShapePoints([(100, 100), (-200, 100), (-200, -200)])
turtle.penup()
turtle.setposition(drawn_triangle[0])
turtle.pendown()
for point in triangle[1:]:
    turtle.setposition(point)

turtle.done()

