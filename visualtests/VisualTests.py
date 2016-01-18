import sys
sys.path.append('..\..\LexLib')
from triangle import Triangle
from page import Page
from shapemaker import ShapeMaker
from line import Line,CardinalDirection
from point import Point
from iofactory import ConsoleIO

class TestPage:

  def test_Draw(self):

    cio = ConsoleIO()
    size = 10
    page = Page(size)

    print("Visual test of a 20 pixel page")
    print("")
    page.Draw(cio)
    print("")

class TestShapeMaker:

  cio = ConsoleIO()

  def test_DrawFlatLine(self):

    # Make Line
    beg = Point(0,0)
    end = Point(3,0)
    line = Line(beg, end)

    # Make Page
    size = 10
    page = Page(size)

    maker = ShapeMaker(page, self.cio)

    print("Visual test of a line drawn from (0,0) to (3,0) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

  def test_DrawVerticalLine(self):

    # Make Line
    beg = Point(0,0)
    end = Point(0,3)
    line = Line(beg, end)

    # Make Page
    size = 10
    page = Page(size)

    maker = ShapeMaker(page, self.cio)

    print("Visual test of a line drawn from (0,0) to (0,3) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

  def test_DrawRegularSlopeLine(self):

    # Make Line
    beg = Point(1,1)
    end = Point(6,6)
    line = Line(beg, end)

    # Make Page
    size = 10
    page = Page(size)

    maker = ShapeMaker(page, self.cio)

    print("Visual test of a line drawn from (1,1) to (6,6) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

  def test_DrawTwoLines(self):

    # Make Line 1
    beg = Point(0,0)
    end = Point(5,5)
    line1 = Line(beg, end)

    # Make Line 2
    beg = Point(0,0)
    end = Point(0,5)
    line2 = Line(beg, end)

    # Make Page
    size = 10
    page = Page(size)

    maker = ShapeMaker(page, self.cio)

    maker.Load(line1)
    maker.Load(line2)

    print("Visual test of two lines drawn from (0,0)(5,5) to (0,0)(0,5) on a 10 pixel page")
    print("")
    maker.Draw()
    print("")

  def test_DrawEquilateralTriangle(self):

    page = Page(10)

    maker = ShapeMaker(page, self.cio)

    beg = Point(0,0)
    end = Point(8,8)

    triangle = Triangle(beg, end)

    print("Visual test of an equilateral triangle from (0,0)(8,8) on a 10 pixel page")
    print("")
    maker.Draw(triangle)
    print("")

  def test_DrawIrregularSlopeLine(self):

    page = Page(10)

    maker = ShapeMaker(page, self.cio)

    beg = Point(0,0)
    end = Point(10,5)

    line = Line(beg, end)

    print("Visual test of an irregular line from (0,0)(10,5) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

  def test_DrawAnotherIrregularSlopeLine(self):

    page = Page(10)

    maker = ShapeMaker(page, self.cio)

    beg = Point(0,0)
    end = Point(10,3)

    line = Line(beg, end)

    print("Visual test of an irregular line from (0,0)(10,3) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

  def test_DrawNegativeRegularSlopeLine(self):

    page = Page(10)

    maker = ShapeMaker(page, self.cio)

    beg = Point(9,9)
    end = Point(0,0)

    line = Line(beg, end)

    print("Visual test of a negative regular line from (9,9)(0,0) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

  def test_DrawNegativeVerticalLine(self):

    page = Page(10)

    maker = ShapeMaker(page, self.cio)

    beg = Point(2,9)
    end = Point(2,0)

    line = Line(beg, end)

    print("Visual test of a negative vertical line from (2,9)(2,0) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

  def test_DrawThreeNegativeLines(self):

    page = Page(10)

    maker = ShapeMaker(page, self.cio)

    beg = Point(1,8)
    end = Point(1,0)

    line = Line(beg, end)

    beg = Point(4,6)
    end = Point(4,0)

    line2 = Line(beg, end)

    beg = Point(7,4)
    end = Point(7,0)

    line3 = Line(beg, end)

    maker.Load(line)
    maker.Load(line2)

    print("Visual test of three negative lines from (1,8)(1,0),(4,6)(4,0) and (7,4)(7,0) on a 10 pixel page")
    print("")
    maker.Draw(line3)
    print("")
  
  def test_DrawDownSlopeLine(self):

    page = Page(10)

    maker = ShapeMaker(page, self.cio)

    beg = Point(5,5)
    end = Point(10,0)

    line = Line(beg, end)

    print("Visual test of a down sloping line from (5,5)(10,0) on a 10 pixel page")
    print("")
    maker.Draw(line)
    print("")

if __name__ == "__main__":

  pageTest = TestPage()
  pageTest.test_Draw()

  shapeMakerTest = TestShapeMaker()
  shapeMakerTest.test_DrawFlatLine()
  shapeMakerTest.test_DrawVerticalLine()
  shapeMakerTest.test_DrawRegularSlopeLine()
  shapeMakerTest.test_DrawTwoLines()
  shapeMakerTest.test_DrawEquilateralTriangle()
  shapeMakerTest.test_DrawIrregularSlopeLine()
  shapeMakerTest.test_DrawAnotherIrregularSlopeLine()
  shapeMakerTest.test_DrawNegativeRegularSlopeLine()
  shapeMakerTest.test_DrawNegativeVerticalLine()
  shapeMakerTest.test_DrawThreeNegativeLines()
  shapeMakerTest.test_DrawDownSlopeLine()
