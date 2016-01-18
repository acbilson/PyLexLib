import sys
sys.path.append('..\..\LexLib')
from page import Page
from shapemaker import ShapeMaker
from line import Line,CardinalDirection
from point import Point
from iofactory import ConsoleIO

cio = ConsoleIO()
g = Page(50)
#g.Draw()
m = ShapeMaker(g, cio)

# NORTH
beg = Point(25,25)
end = Point(25,49)
end.Value = '0'
n = Line(beg, end)

# NORTHEAST
beg = Point(25,25)
end = Point(49,49)
end.Value = '1'
ne = Line(beg, end)

# EAST
beg = Point(25,25)
end = Point(49, 25)
end.Value = '2'
e = Line(beg, end)

# SOUTHEAST
beg = Point(25,25)
end = Point(49,1)
end.Value = '3'
se = Line(beg, end)

# SOUTH
beg = Point(25,25)
end = Point(25,1)
end.Value = '4'
s = Line(beg, end)

# SOUTHWEST
beg = Point(25,25)
end = Point(1,1)
end.Value = '5'
sw = Line(beg, end)

# WEST
beg = Point(25,25)
end = Point(1,25)
end.Value = '6'
w = Line(beg, end)

# NORTHWEST
beg = Point(25,25)
end = Point(1,49)
end.Value = '7'
nw = Line(beg, end)

#0 - Success!
m.Draw(n)
#1 - Success!
m.Draw(ne)
#2 - Success!
m.Draw(e)
#3 - Success!
m.Draw(se)
#4 - Success!
m.Draw(s)
#5 - Success!
m.Draw(sw)
#6 - Success!
m.Draw(w)
#7 -Success!
m.Draw(nw)
