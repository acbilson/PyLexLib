from point import Point
from line import Line
import math

# IDEAS:
#
#   * Draw string in pairs
#   * Draw Rhombus
#   * Draw multi-sided shape
#   * Prepend drawing to the top of a file
#   * Add Calculate class that can take a shape and calculate length, area, etc
#   * Create some template drawings, such as a header
#   * Auto-determine the page size based on the shapes entered
#

class Triangle:

  HypotenusePixel = "HY"
  BasePixel = "BA"
  HeightPixel = "HE"
  Default = "default"

  def __init__(self, p1, p2, p3=Default):
    if type(p1) is tuple and type(p2) is tuple:
      p1 = Point(p1[0], p1[1])
      p2 = Point(p2[0], p2[1])
    if p3 != self.Default and type(p3) is tuple:
      p3 = Point(p3[0], p3[1])

    self.SetSides(p1,p2,p3)
    self.__points = []
    self.SetPoints()

  def __str__(self):
    return "T(Y" + str(self.__hypotenuse) + ",B" + str(self.__base) + ",H" + str(self.__height) + ")"

  def __repr__(self):
    return "T(Y" + str(self.__hypotenuse) + ",B" + str(self.__base) + ",H" + str(self.__height) + ")"

  def GetPoints(self):
    return self.__points

  def SetSides(self, p1, p2, p3):
    if p3 == self.Default:
      self.__hypotenuse = self.SetHypotenuse(p1, p2)
      self.__base = self.SetBase(p1, p2)
      self.__height = self.SetHeight(p1, p2)
    else:
      self.__hypotenuse = self.SetSide(p1, p2)
      self.__base = self.SetSide(p2, p3)
      self.__height = self.SetSide(p3, p1)

  def SetSide(self, beg, end):
    return Line(beg, end)

  def GetHypotenuse(self):
    return self.__hypotenuse

  def GetBase(self):
    return self.__base

  def GetHeight(self):
    return self.__height

  def SetHypotenuse(self, p1, p2):
    hypotenuse = self.SetSide(p1, p2)

    if hypotenuse.IsHorizontal() or hypotenuse.IsVertical():
      raise Exception("Points must slope to create triangle")

    return hypotenuse

  def SetBase(self, p1, p2):
    return Line(p1, Point(p2.X, p1.Y))

  def SetHeight(self, p1, p2):
    return Line(Point(p2.X, p1.Y), Point(p2.X, p2.Y))

  def SetPoints(self):
    hypotenusePoints = self.__hypotenuse.GetPoints()
    basePoints = self.__base.GetPoints()
    heightPoints = self.__height.GetPoints()

    # Set all pixels by line
    hypotenusePoints = self.SetPixels(hypotenusePoints, self.HypotenusePixel)
    basePoints = self.SetPixels(basePoints, self.BasePixel)
    heightPoints = self.SetPixels(heightPoints, self.HeightPixel)

    self.__points = hypotenusePoints + basePoints + heightPoints

  def SetPixels(self, points, pixel):
    for p in points:
      p.Value = pixel
    return points
