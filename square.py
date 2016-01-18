from point import Point
from line import Line,CardinalDirection

class Square:

  TopPixel = "TO"
  BottomPixel = "BO"
  LeftPixel = "LT"
  RightPixel = "RT"

  def __init__(self, p1, p2):
    if type(p1) is tuple and type(p2) is tuple:
      p1 = Point(p1[0], p1[1])
      p2 = Point(p2[0], p2[1])
    self.__points = []
    self.__top = self.SetTop(p1, p2)
    self.__bottom = self.SetBottom(p1, p2)
    self.__left = self.SetLeft(p1, p2)
    self.__right = self.SetRight(p1, p2)
    self.SetPoints()

  def GetTop(self):
    return self.__top

  def GetBottom(self):
    return self.__bottom

  def GetLeft(self):
    return self.__left

  def GetRight(self):
    return self.__right

  def GetPoints(self):
    return self.__points

  def SetTop(self, p1, p2):
    beg = Point(min(p1.X, p2.X), max(p1.Y, p2.Y))
    end = Point(max(p1.X, p2.X), max(p1.Y, p2.Y))
    return Line(beg, end)

  def SetBottom(self, p1, p2):
    beg = Point(min(p1.X, p2.X), min(p1.Y, p2.Y))
    end = Point(max(p1.X, p2.X), min(p1.Y, p2.Y))
    return Line(beg, end)

  def SetLeft(self, p1, p2):
    beg = Point(min(p1.X, p2.X), min(p1.Y, p2.Y))
    end = Point(min(p1.X, p2.X), max(p1.Y, p2.Y))
    return Line(beg, end)

  def SetRight(self, p1, p2):
    beg = Point(max(p1.X, p2.X), min(p1.Y, p2.Y))
    end = Point(max(p1.X, p2.X), max(p1.Y, p2.Y))
    return Line(beg, end)

  def SetPoints(self):
    top = self.__top.GetPoints()
    bot = self.__bottom.GetPoints()
    lef = self.__left.GetPoints()
    rig = self.__right.GetPoints()
    
    top = self.SetPixels(top, self.TopPixel)
    bot = self.SetPixels(bot, self.BottomPixel)
    lef = self.SetPixels(lef, self.LeftPixel)
    rig = self.SetPixels(rig, self.RightPixel)

    self.__points = top + bot + lef + rig

  def SetPixels(self, points, pixel):
    for p in points:
      p.Value = pixel
    return points
