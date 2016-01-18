class Point:

  Empty = "  "
  Full = "XX"

  def __init__(self, x, y):
    if not type(x) == int \
    or not type(y) == int:
      raise Exception('Can only assign int type to x or y value')
    self.X = x
    self.Y = y
    self.Value = self.Empty

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.X == other.X and self.Y == other.Y

  def __ne__(self, other):
    return not self.__eq__(other)

  def __str__(self):
    return "P(" + str(self.X) + "," + str(self.Y) + ")"

  def __repr__(self):
    return "P(" + str(self.X) + "," + str(self.Y) + ")"
