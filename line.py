from point import Point
import math

class CardinalDirection():
  North = "NO"
  South = "SO"
  East = "EA"
  West = "WE"
  Northeast = "NE"
  Northwest = "NW"
  Southeast = "SE"
  Southwest = "SW"

class Line:

  def __init__(self, begin, end):
    if type(begin) is tuple and type(end) is tuple:
      begin = Point(begin[0], begin[1])
      end = Point(end[0], end[1])
    self.Begin = begin
    self.End = end
    self.__points = []
    self.__direction = ""
    self.SetPoints()

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.__dict__ == other.__dict__
    else:
      return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def __str__(self):
    return "L(" + str(self.Begin) + "," + str(self.End) + ")"

  def __repr__(self):
    return "L(" + str(self.Begin) + "," + str(self.End) + ")"

  def GetPoints(self):
    return self.__points

  def GetDirection(self):
    return self.__direction

  def SetPoints(self):

    if self.OnlyTwoPointsInLine():
      self.__points.append(self.Begin)
      self.__points.append(self.End)
      return

    endRange = self.EndRange()
    slopeX = 0
    slopeY = 0

    if self.IsNorth():
      self.__direction = "North"

      for x in range(0, endRange):
        p = Point(self.Begin.X, self.Begin.Y + x)
        p.Value = CardinalDirection.North
        self.__points.append(p)

    elif self.IsSouth():
      self.__direction = "South"

      for x in range(0, endRange):
        p = Point(self.Begin.X, self.Begin.Y - x)
        p.Value = CardinalDirection.South
        self.__points.append(p)

    elif self.IsEast():
      self.__direction = "East"

      for x in range(0, endRange):
        p = Point(self.Begin.X + x, self.Begin.Y)
        p.Value = CardinalDirection.East
        self.__points.append(p)

    elif self.IsWest():
      self.__direction = "West"

      for x in range(0, endRange):
        p = Point(self.Begin.X - x, self.Begin.Y)
        p.Value = CardinalDirection.West
        self.__points.append(p)

    elif self.IsNorthEast():
      self.__direction = "Northeast" 

      for x in range(0, endRange):
        slope = self.GetSlopesAsPoint(x)
        p = Point(self.Begin.X + slope.X, self.Begin.Y + slope.Y)
        p.Value = CardinalDirection.Northeast
        self.__points.append(p)

    elif self.IsNorthWest():
      self.__direction = "Northwest"

      for x in range(0, endRange):
        slope = self.GetSlopesAsPoint(x)
        p = Point(self.Begin.X - slope.X, self.Begin.Y + slope.Y)
        p.Value = CardinalDirection.Northwest
        self.__points.append(p)

    elif self.IsSouthEast():
      self.__direction = "Southeast"

      for x in range(0, endRange):
        slope = self.GetSlopesAsPoint(x)
        p = Point(self.Begin.X + slope.X, self.Begin.Y - slope.Y)
        p.Value = CardinalDirection.Southeast
        self.__points.append(p)

    elif self.IsSouthWest():
      self.__direction = "Southwest"

      for x in range(0, endRange):
        slope = self.GetSlopesAsPoint(x)
        p = Point(self.Begin.X - slope.X, self.Begin.Y - slope.Y)
        p.Value = CardinalDirection.Southwest
        self.__points.append(p)

  def EndRange(self):
      endRange = 0
      axisX = self.SpanX()
      axisY = self.SpanY()

      if self.IsVertical():
        endRange = axisY
      elif self.IsHorizontal():
        endRange = axisX
      else:
        if self.IsRegularSlope():
          # Doesn't matter which axis
          endRange = axisX
        else:
          if self.IsLineWiderThanTall():
            endRange = axisX
          else:
            endRange = axisY

      return endRange + 1

  def IsRegularSlope(self):
    return self.GetSlope() == 1

  def GetSlopesAsPoint(self, x):
    slopeY = x
    slopeX = x

    if self.IsLineWiderThanTall():
      # Shorten the height by the slope
      slopeY = self.GetSlopeY(x)
    else:
      # Shorten the width by the inverted slope
      slopeX = self.GetSlopeX(x)

    return Point(slopeX, slopeY)

  def IsLineWiderThanTall(self):
    return self.SpanY() < self.SpanX()

  def GetSlopeY(self, y):
    return math.ceil(y * self.GetSlope())

  def GetSlopeX(self, x):
    return math.ceil(x * self.GetInvertedSlope())

  def GetSlope(self):
    return self.SpanY() / self.SpanX()

  def GetInvertedSlope(self):
    return self.SpanX() / self.SpanY()

  def SpanX(self):
    return abs(self.End.X - self.Begin.X)

  def SpanY(self):
    return abs(self.End.Y - self.Begin.Y)

  def IsNorth(self):
    return (self.Begin.X == self.End.X and self.Begin.Y < self.End.Y)

  def IsNorthEast(self):
    return (self.Begin.X < self.End.X and self.Begin.Y < self.End.Y)

  def IsEast(self):
    return(self.Begin.X < self.End.X and self.Begin.Y == self.End.Y)

  def IsSouthEast(self):
    return (self.Begin.X < self.End.X and self.Begin.Y > self.End.Y)

  def IsSouth(self):
    return (self.Begin.X == self.End.X and self.Begin.Y > self.End.Y)

  def IsSouthWest(self):
    return (self.Begin.X > self.End.X and self.Begin.Y > self.End.Y)

  def IsWest(self):
    return (self.Begin.X > self.End.X and self.Begin.Y == self.End.Y)

  def IsNorthWest(self):
    return (self.Begin.X > self.End.X and self.Begin.Y < self.End.Y)

  def OnlyTwoPointsInLine(self):
    return self.SpanX() + self.SpanY() < 2

  def IsFlat(self, span):
    return span == 0

  def IsVertical(self):
    spanX = self.SpanX()
    return self.IsFlat(spanX)

  def IsHorizontal(self):
    spanY = self.SpanY()
    return self.IsFlat(spanY)
