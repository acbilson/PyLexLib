import sys
sys.path.append('..\..\LexLib')
from triangle import Triangle
from page import Page
from shapemaker import ShapeMaker
from line import Line,CardinalDirection
from point import Point
from iofactory import ConsoleIO

cio = ConsoleIO()
g = Page(60)
m = ShapeMaker(g, cio)

# Positive slope equilateral
beg = Point(1,1)
end = Point(10,10)
pet = Triangle(beg, end)

# Negative slope equilateral
beg = Point(10,25)
end = Point(25,10)
net = Triangle(beg, end)

m.Draw(pet)
m.Draw(net)
