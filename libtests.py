import unittest
from iofactory import *
from point import Point
from line import Line,CardinalDirection
from triangle import Triangle
from square import Square
from page import *
from shapemaker import ShapeMaker
from task import *

class TestPoint(unittest.TestCase):

  def test_point_ctor(self):

    point = Point(1,2)
    self.assertEqual(point.X, 1)
    self.assertEqual(point.Y, 2)
    self.assertEqual(point.Value, '  ')

  def test_point_instance(self):

    p1 = Point(1,2)
    p2 = Point(3,1)

    self.assertNotEqual(p1.X, p2.X)
    self.assertNotEqual(p1.Y, p2.Y)

  def test_point_equality(self):

    p1 = Point(1,1)
    p2 = Point(1,1)

    self.assertEqual(p1, p2)

  def test_point_nonequality(self):

    p1 = Point(1,1)
    p2 = Point(2,2)

    self.assertNotEqual(p1, p2)

  def test_point_intOnly(self):
    
    def failedassign(): p = Point(1, 'b')
    self.assertRaises(Exception, failedassign)

class TestLine(unittest.TestCase):

  def test_line_ctor(self):

    beg = Point(3,0)
    end = Point(0,1)

    line = Line(beg, end)
    self.assertEqual(line.Begin.X, 3)
    self.assertEqual(line.Begin.Y, 0)
    self.assertEqual(line.End.X, 0)
    self.assertEqual(line.End.Y, 1)

  def test_line_simplector(self):

    line = Line((1,3),(2,3))

    self.assertEqual(line.Begin, Point(1,3))
    self.assertEqual(line.End, Point(2,3))

  def test_line_instance(self):

    beg = Point(3,0)
    end = Point(0,1)
    line1 = Line(beg, end)

    beg = Point(2,3)
    end = Point(4,0)
    line2 = Line(beg, end)

    self.assertNotEqual(line1.Begin.X, line2.Begin.X)
    self.assertNotEqual(line1.Begin.Y, line2.Begin.Y)
    self.assertNotEqual(line1.End.X, line2.End.X)
    self.assertNotEqual(line1.End.Y, line2.End.Y)

  def test_line_equal(self):

    l1 = Line((1,3),(3,4))
    l2 = Line((1,3),(3,4))

    self.assertEqual(l1, l2)

  def test_line_firstandlast(self):

    beg = Point(1,2)
    end = Point(1,3)

    line = Line(beg, end)

    actual = line.GetPoints()

    self.assertEqual(actual[0], beg)
    self.assertEqual(actual[1], end)

  def test_line_horizontal(self):

    beg = Point(2,0)
    end = Point(5,0)

    line = Line(beg, end)

    actual = line.GetPoints()

    expectedPoints = [Point(2,0), Point(3,0), Point(4,0), Point(5,0)]
    self.assertEqual(actual, expectedPoints)

  def test_line_vertical(self):

    beg = Point(1,0)
    end = Point(1,4)

    line = Line(beg, end)

    actual = line.GetPoints()

    expectedPoints = [Point(1,0), Point(1,1), Point(1,2), Point(1,3), Point(1,4)]
    self.assertEqual(actual, expectedPoints)

  def test_line_north(self):

    n1 = Line(Point(0,0), Point(0,10))
    n2 = Line(Point(5,2), Point(5,32))
    n3 = Line(Point(30,2), Point(30,15))

    direction = "North"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_north(self):

    n1 = Line(Point(0,0), Point(0,5))
    n2 = Line(Point(5,2), Point(5,5))
    n3 = Line(Point(30,2), Point(30,5))

    p1 = [Point(0,0), Point(0,1), Point(0,2), Point(0,3), Point(0,4), Point(0,5)]
    p2 = [Point(5,2), Point(5,3), Point(5,4), Point(5,5)]
    p3 = [Point(30,2), Point(30,3), Point(30,4), Point(30,5)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_south(self):

    n1 = Line(Point(0,30), Point(0,10))
    n2 = Line(Point(15,20), Point(15,2))
    n3 = Line(Point(40,15), Point(40,10))

    direction = "South"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_south(self):

    n1 = Line(Point(0,5), Point(0,2))
    n2 = Line(Point(8,5), Point(8,2))
    n3 = Line(Point(1,20), Point(1,17))

    p1 = [Point(0,5), Point(0,4), Point(0,3), Point(0,2)]
    p2 = [Point(8,5), Point(8,4), Point(8,3), Point(8,2)]
    p3 = [Point(1,20), Point(1,19), Point(1,18), Point(1,17)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_east(self):

    n1 = Line(Point(0,0), Point(20,0))
    n2 = Line(Point(15,3), Point(35,3))
    n3 = Line(Point(10,20), Point(15,20))

    direction = "East"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_east(self):

    n1 = Line(Point(0,0), Point(3,0))
    n2 = Line(Point(5,2), Point(8,2))
    n3 = Line(Point(0,10), Point(3,10))

    p1 = [Point(0,0), Point(1,0), Point(2,0), Point(3,0)]
    p2 = [Point(5,2), Point(6,2), Point(7,2), Point(8,2)]
    p3 = [Point(0,10), Point(1,10), Point(2,10), Point(3,10)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_west(self):

    n1 = Line(Point(20,0), Point(5,0))
    n2 = Line(Point(40,10), Point(9,10))
    n3 = Line(Point(30,40), Point(20,40))

    direction = "West"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_west(self):

    n1 = Line(Point(5,0), Point(2,0))
    n2 = Line(Point(5,2), Point(2,2))
    n3 = Line(Point(5,10), Point(2,10))

    p1 = [Point(5,0), Point(4,0), Point(3,0), Point(2,0)]
    p2 = [Point(5,2), Point(4,2), Point(3,2), Point(2,2)]
    p3 = [Point(5,10), Point(4,10), Point(3,10), Point(2,10)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_northeast(self):

    n1 = Line(Point(0,0), Point(10,10))
    n2 = Line(Point(2,5), Point(5,8))
    n3 = Line(Point(50,15), Point(65,30))

    direction = "Northeast"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_northeast(self):

    n1 = Line(Point(0,0), Point(3,3))
    n2 = Line(Point(2,5), Point(5,8))
    n3 = Line(Point(30,2), Point(33,5))

    p1 = [Point(0,0), Point(1,1), Point(2,2), Point(3,3)]
    p2 = [Point(2,5), Point(3,6), Point(4,7), Point(5,8)]
    p3 = [Point(30,2), Point(31,3), Point(32,4), Point(33,5)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_northwest(self):

    n1 = Line(Point(10,0), Point(0,10))
    n2 = Line(Point(12,12), Point(9,15))
    n3 = Line(Point(20,30), Point(10,40))

    direction = "Northwest"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_northwest(self):

    n1 = Line(Point(3,0), Point(0,3))
    n2 = Line(Point(5,2), Point(2,5))
    n3 = Line(Point(30,2), Point(27,5))

    p1 = [Point(3,0), Point(2,1), Point(1,2), Point(0,3)]
    p2 = [Point(5,2), Point(4,3), Point(3,4), Point(2,5)]
    p3 = [Point(30,2), Point(29,3), Point(28,4), Point(27,5)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_southeast(self):

    n1 = Line(Point(25,25), Point(30,20))
    n2 = Line(Point(4,15), Point(10,9))
    n3 = Line(Point(40,30), Point(45,25))

    direction = "Southeast"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_southeast(self):

    n1 = Line(Point(5,5), Point(8,2))
    n2 = Line(Point(7,3), Point(10,0))
    n3 = Line(Point(5,10), Point(8,7))

    p1 = [Point(5,5), Point(6,4), Point(7,3), Point(8,2)]
    p2 = [Point(7,3), Point(8,2), Point(9,1), Point(10,0)]
    p3 = [Point(5,10), Point(6,9), Point(7,8), Point(8,7)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_southwest(self):

    n1 = Line(Point(25,25), Point(10,10))
    n2 = Line(Point(8,6), Point(3,1))
    n3 = Line(Point(35,55), Point(25,45))

    direction = "Southwest"
    self.assertEqual(n1.GetDirection(), direction)
    self.assertEqual(n2.GetDirection(), direction)
    self.assertEqual(n3.GetDirection(), direction)

  def test_line_southwest(self):

    n1 = Line(Point(5,5), Point(2,2))
    n2 = Line(Point(8,3), Point(5,0))
    n3 = Line(Point(3,9), Point(0,6))

    p1 = [Point(5,5), Point(4,4), Point(3,3), Point(2,2)]
    p2 = [Point(8,3), Point(7,2), Point(6,1), Point(5,0)]
    p3 = [Point(3,9), Point(2,8), Point(1,7), Point(0,6)]
    self.assertEqual(p1, n1.GetPoints())
    self.assertEqual(p2, n2.GetPoints())
    self.assertEqual(p3, n3.GetPoints())

  def test_line_halfslopene_heightgreater(self):

    l = Line((4,4),(6,8))

    p = l.GetPoints()

    e = [Point(4,4), Point(5,5), Point(5,6), Point(6,7), Point(6,8)]
    self.assertEqual(p, e)

  def test_line_halfslopene_widthgreater(self):

    l = Line((6,2),(10,4))

    p = l.GetPoints()

    e = [Point(6,2), Point(7,3), Point(8,3), Point(9,4), Point(10,4)]
    self.assertEqual(p, e)

  def test_line_halfslopenw_heightgreater(self):

    l = Line((5,5),(3,9))

    p = l.GetPoints()

    e = [Point(5,5), Point(4,6), Point(4,7), Point(3,8), Point(3,9)]
    self.assertEqual(p, e)

  def test_line_halfslopenw_widthgreater(self):

    l = Line((5,5),(1,7))

    p = l.GetPoints()

    e = [Point(5,5), Point(4,6), Point(3,6), Point(2,7), Point(1,7)]
    self.assertEqual(p, e)

class TestPage(unittest.TestCase):

  def test_page_ctor(self):

    size = 10
    page = Page(size)

    actual = page.GetPage()
    self.assertEqual(len(actual), size + 1) # Y Axis
    self.assertEqual(len(actual[0]), size + 1) # X Axis

  def test_page_ctor_irregular(self):

    size = (10,5)
    page = Page(size)

    rows = page.GetPage()
    self.assertEqual(len(rows), 5+1)
    self.assertEqual(len(rows[0]), 10+1)

  def test_page_instance(self):

    size1 = 10
    size2 = 20
    page1 = Page(10)
    page2 = Page(20)

    actual1 = page1.GetPage()
    actual2 = page2.GetPage()
    self.assertEqual(len(actual1), size1 + 1) # Y Axis
    self.assertEqual(len(actual1[0]), size1 + 1) # X Axis
    self.assertEqual(len(actual2), size2 + 1) # Y Axis
    self.assertEqual(len(actual2[0]), size2 + 1) # X Axis

  def test_page_generaterow(self):
    p = Page(2)
    row = p.GenerateRow(0)
    points = [Point(0,0), Point(1,0), Point(2,0)]
    self.assertEqual(points, row)

  def test_page_generatepagerows(self):
    p = Page(2)
    pages = p.GeneratePageRows()
    points = [[Point(0,0), Point(1,0), Point(2,0)],
              [Point(0,1), Point(1,1), Point(2,1)],
              [Point(0,2), Point(1,2), Point(2,2)]]

    self.assertEqual(points, pages)

  def test_page_draw(self):
    
    io = FakeIO()
    p = Page(2)
    p.Draw(io)
    expectedPage = ('      \n'
                    '      \n'
                    '      \n')

    drawnPage = ''.join(io.writeContent)
    self.assertEqual(expectedPage, drawnPage)

class TestTriangle(unittest.TestCase):

  def test_triangle_ctor(self):

    beg = Point(0,0)
    end = Point(4,4)

    triangle = Triangle(beg, end)

  def test_triangle_simplector(self):

    triangle = Triangle((0,0),(4,4))

    self.assertEqual(triangle.GetHypotenuse(), Line((0,0),(4,4)))

  def test_triangle_instance(self):

    beg = Point(0,0)
    end = Point(4,4)

    triangle1 = Triangle(beg, end)

    beg = Point(3,3)
    end = Point(7,7)

    triangle2 = Triangle(beg, end)

    self.assertNotEqual(triangle1.GetHypotenuse(), triangle2.GetHypotenuse())

  def test_triangle_hypotenuse(self):

    beg = Point(0,0)
    end = Point(4,4)
    hypotenuse = Line(beg, end)

    triangle = Triangle(beg, end)

    self.assertEqual(hypotenuse, triangle.GetHypotenuse())

  def test_triangle_base(self):

    beg = Point(0,0)
    end = Point(4,4)
    base = Line(Point(0,0), Point(4,0))

    triangle = Triangle(beg, end)

    self.assertEqual(base, triangle.GetBase())

  def test_triangle_height(self):

    beg = Point(0,0)
    end = Point(4,4)
    height = Line(Point(4,0), Point(4,4))

    triangle = Triangle(beg, end)

    self.assertEqual(height, triangle.GetHeight())

  def test_triangle_horizontal_shouldthrow(self):

    beg = Point(0,0)
    end = Point(6,0)
    flatLine = Line(beg, end)

    with self.assertRaises(Exception) as ex:
      triangle = Triangle(beg, end)

  def test_triangle_vertical_shouldthrow(self):

    beg = Point(0,0)
    end = Point(0,6)
    flatLine = Line(beg, end)

    with self.assertRaises(Exception) as ex:
      triangle = Triangle(beg, end)

  def test_triangle_equilateraltriangle(self):

    beg = Point(50,15)
    end = Point(65,30)
    triangle = Triangle(beg, end)

    y = triangle.GetHypotenuse()
    b = triangle.GetBase()
    h = triangle.GetHeight()

    self.assertEqual(Line(beg,end).GetPoints(), y.GetPoints())
    self.assertEqual(Line(Point(50,15),Point(65,15)).GetPoints(), b.GetPoints())
    self.assertEqual(Line(Point(65,15),Point(65,30)).GetPoints(), h.GetPoints())
    self.assertEqual(y.GetPoints()+b.GetPoints()+h.GetPoints(), triangle.GetPoints())

  def test_triangle_reverseequilateraltriangle(self):

    beg = Point(10,25)
    end = Point(25,10)
    triangle = Triangle(beg, end)

    y = triangle.GetHypotenuse()
    b = triangle.GetBase()
    h = triangle.GetHeight()

    self.assertEqual(Line(beg,end).GetPoints(), y.GetPoints())
    self.assertEqual(Line(Point(10,25),Point(25,25)).GetPoints(), b.GetPoints())
    self.assertEqual(Line(Point(25,25),Point(25,10)).GetPoints(), h.GetPoints())
    self.assertEqual(y.GetPoints()+b.GetPoints()+h.GetPoints(), triangle.GetPoints())

  def test_triangle_scalenetriangle(self):

    p1 = Point(10,10)
    p2 = Point(30,20)
    p3 = Point(16,3)
    triangle = Triangle(p1, p2, p3)

    y = triangle.GetHypotenuse()
    b = triangle.GetBase()
    h = triangle.GetHeight()

    self.assertEqual(Line(p1, p2), y)
    self.assertEqual(Line(p2, p3), b)
    self.assertEqual(Line(p3, p1), h)

class TestSquare(unittest.TestCase):

  def test_square_ctor(self):

    beg = Point(1,1)
    end = Point(9,9)
    square = Square(beg, end)

  def test_square_simplector(self):

    square = Square((1,1),(9,9))

    self.assertEqual(square.GetTop(), Line((1,9),(9,9)))

  def test_square_top(self):

    beg = Point(1,1)
    end = Point(9,9)
    square = Square(beg, end)

    actual = square.GetTop()

    expected = Line(Point(1,9),Point(9,9))
    self.assertEqual(actual, expected)

  def test_square_bottom(self):

    beg = Point(1,1)
    end = Point(9,9)
    square = Square(beg, end)

    actual = square.GetBottom()

    expected = Line(Point(1,1),Point(9,1))
    self.assertEqual(actual, expected)

  def test_square_left(self):

    beg = Point(1,1)
    end = Point(9,9)
    square = Square(beg, end)

    actual = square.GetLeft()

    expected = Line(Point(1,1),Point(1,9))
    self.assertEqual(actual, expected)

  def test_square_right(self):

    beg = Point(1,1)
    end = Point(9,9)
    square = Square(beg, end)

    actual = square.GetRight()

    expected = Line(Point(9,1),Point(9,9))
    self.assertEqual(actual, expected)

  def test_square_points(self):

    beg = Point(1,1)
    end = Point(4,4)
    square = Square(beg, end)

    actual = square.GetPoints()

    top = [Point(1,4), Point(2,4), Point(3,4), Point(4,4)]
    bot = [Point(1,1), Point(2,1), Point(3,1), Point(4,1)]
    lef = [Point(1,1), Point(1,2), Point(1,3), Point(1,4)]
    rig = [Point(4,1), Point(4,2), Point(4,3), Point(4,4)]
    self.assertEqual(actual, top+bot+lef+rig)

class TestShapeMaker(unittest.TestCase):

  def setUp(self):
    self.tio = FakeIO()

  def tearDown(self):
    self.tio = None

  def test_shapemaker_ctor(self):

    page = Page(25)
    maker = ShapeMaker(page, self.tio)

    self.assertEqual(maker.mypage, page.GetPage())

  def test_shapemaker_load(self):

    page = Page(25)
    maker = ShapeMaker(page, self.tio)
    line = Line((0,0),(3,0))

    maker.Load(line)

    self.assertEqual(maker.mypage[0][0].Value, CardinalDirection.East)
    self.assertEqual(maker.mypage[0][1].Value, CardinalDirection.East)
    self.assertEqual(maker.mypage[0][2].Value, CardinalDirection.East)

  def test_shapemaker_load_withtext_shortandeven(self):

    page = Page(5)
    maker = ShapeMaker(page, self.tio)

    line = Line(Point(0,0), Point(4,0))
    maker.Load(line, "astrings")
    maker.Draw()

    line = ('            \n'
            '            \n'
            '            \n'
            '            \n'
            '            \n'
            'astringsEA  \n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(line, drawnPage)

  def test_shapemaker_load_withtext_shortandodd_extends(self):

    page = Page(5)
    maker = ShapeMaker(page, self.tio)

    line = Line(Point(0,0), Point(4,0))
    maker.Load(line, "astring")
    maker.Draw()

    line = ('            \n'
            '            \n'
            '            \n'
            '            \n'
            '            \n'
            'astring.EA  \n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(line, drawnPage)

  def test_shapemaker_load_withtext_longandeven(self):

    page = Page(5)
    maker = ShapeMaker(page, self.tio)

    line = Line(Point(0,5), Point(0,0))
    maker.Load(line, "astringisabeautifulthing")
    maker.Draw()

    line = ('as          \n'
            'tr          \n'
            'in          \n'
            'gi          \n'
            'sa          \n'
            'be          \n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(line, drawnPage)

  def test_shapemaker_drawblank(self):

    p = Page(2)
    maker = ShapeMaker(p, self.tio)
    maker.Draw()

    line = ('      \n'
            '      \n'
            '      \n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(line, drawnPage)

  def test_shapemaker_drawline(self):

    p = Page(2)
    l = Line((0,0),(0,2))
    maker = ShapeMaker(p, self.tio)
    maker.Draw(l)

    line = ('NO    \n'
            'NO    \n'
            'NO    \n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(line, drawnPage)

  def test_shapemaker_drawlines(self):

    p = Page(5)
    l1 = Line((1,1),(1,4))
    l2 = Line((5,5),(0,0))
    maker = ShapeMaker(p, self.tio)
    maker.Load(l1)
    maker.Load(l2)
    maker.Draw()

    line = ('          SW\n'
            '  NO    SW  \n'
            '  NO  SW    \n'
            '  NOSW      \n'
            '  SW        \n'
            'SW          \n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(line, drawnPage)

  def test_shapemaker_drawirregularline(self):

    p = Page(5)
    l = Line((1,5),(3,0))
    maker = ShapeMaker(p, self.tio)
    maker.Draw(l)
    line = ('  SE        \n'
            '    SE      \n'
            '    SE      \n'
            '      SE    \n'
            '      SE    \n'
            '      SE    \n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(line, drawnPage)

  def test_shapemaker_drawtriangle(self):
    p = Page(5)

    beg = Point(5,0)
    end = Point(0,5)
    tri = Triangle(beg, end)
    maker = ShapeMaker(p, self.tio)
    maker.Draw(tri)

    triangle = ('HE          \n'
                'HEHY        \n'
                'HE  HY      \n'
                'HE    HY    \n'
                'HE      HY  \n'
                'HEBABABABABA\n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(triangle, drawnPage)

  def test_shapemaker_drawsquare(self):
    p = Page(5)

    beg = Point(5,0)
    end = Point(0,5)
    sq = Square(beg, end)
    maker = ShapeMaker(p, self.tio)
    maker.Draw(sq)

    sqr = ('LTTOTOTOTORT\n'
           'LT        RT\n'
           'LT        RT\n'
           'LT        RT\n'
           'LT        RT\n'
           'LTBOBOBOBORT\n')

    drawnPage = ''.join(self.tio.writeContent)
    self.assertEqual(sqr, drawnPage)

class TestTask(unittest.TestCase):

  """Test the Task object"""

  def test_task_ctor_setsproperties(self):
    t = Task('Test')
    self.assertEqual(t.priority, 0)
    self.assertEqual(t.urgency, 0)
    self.assertEqual(t.name, 'Test')
    self.assertEqual(t.eisenhower, 0)

  def test_task_ctor_differentinstance(self):
    t1 = Task('Test')
    t2 = Task('Other Test')
    self.assertNotEqual(t1.name, t2.name)

  def test_task_printasstring(self):
    t = Task('Test')    
    s = t.__str__()
    self.assertEqual(s, "T(Test,0,0,0)")

  def test_task_repr(self):
    t = Task('Test')    
    s = t.__repr__()
    self.assertEqual(s, "T(Test,0,0,0)")

class TestGraph(unittest.TestCase):

  """Tests the Graph object, descendant of Page"""

  def setUp(self):
    self.tio = FakeIO()

  def tearDown(self):
    self.tio = None

  def test_graph_ctor_hasinheritedvalues(self):
    g = Graph(5)
    self.assertIsNotNone(g.XAxis)
    self.assertIsNotNone(g.YAxis)

  def test_graph_addaxis(self):

    g = Graph(5)
    g.Draw(self.tio)

    expectedGraph = ('                      \n'
                     '05                    \n'
                     '                      \n'
                     '04                    \n'
                     '                      \n'
                     '03                    \n'
                     '                      \n'
                     '02                    \n'
                     '                      \n'
                     '01                    \n'
                     '  01  02  03  04  05  \n')

    drawnGraph = ''.join(self.tio.writeContent)
    self.assertEqual(expectedGraph, drawnGraph)

class TestIOFactory(unittest.TestCase):

  """ Test the IO Factory and it's factory objects """

  def setUp(self):
    self.readFilePath = 'C:\\SourceCode\\PersonalRepo\\Python\\LexLib\\testfiles\\read.txt'
    self.readJsonPath = 'C:\\SourceCode\\PersonalRepo\\Python\\LexLib\\testfiles\\read.json'
    self.readJsonPath_Task = 'C:\\SourceCode\\PersonalRepo\\Python\\LexLib\\testfiles\\readTask.json'

  def test_iofactory_ctor_getconsoleio(self):
    factory = IOFactory()
    cio = factory.GetInstance()
    self.assertEqual(type(cio), ConsoleIO)

  def test_iofactory_ctor_getfileio(self):
    factory = IOFactory()
    fio = factory.GetInstance(self.readFilePath)
    self.assertEqual(type(fio), FileIO)

  def test_file_read(self):
    factory = IOFactory()
    fio = factory.GetInstance(self.readFilePath)
    content = fio.read()
    self.assertEqual(content[0], "This is my test content\n")
 
  def test_json_read(self):
    jio = JsonIO(self.readJsonPath)
    content = jio.read()
    self.assertEqual(content[0], "This is my test content")

  def test_json_read_decodetask(self):
    jio = JsonIO(self.readJsonPath_Task)
    decoder = CustomDecoder()
    content = jio.read(decoder.as_task)
    self.assertEqual(content, Task('TestName', 5, 2, 1))

if __name__ == '__main__':
  unittest.main()
