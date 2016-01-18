from page import Page
from point import Point
from line import Line

class ShapeMaker:

  def __init__(self, page, io):
    self.io = io
    self.__pageObj = page
    self.mypage = page.GetPage()

  def Load(self, shape, text=None):
    if text == None:
      self.InsertPixels(shape)
    else:
      self.InsertText(shape, text)
      self.InsertPixels(shape)

  def Draw(self, shape=None):
    if shape != None:
      self.Load(shape)
    self.__pageObj.Draw(self.io)

  def Print(self, fileName):
    with open(fileName, 'a') as shapeFile:
      for row in self.mypage:
        for pixel in row:
          shapeFile.write(pixel.Value)
        shapeFile.write("\n")

  # Note: Because of the way lists are accessed, X and Y are flipped here
  def InsertPixels(self, shape):
    pixels = shape.GetPoints()
    for pixel in pixels:
      self.mypage[pixel.Y][pixel.X].Value = pixel.Value

  def InsertText(self, shape, text):

    """ Set the text of a shape from the default to the text specified """

    points = shape.GetPoints()
    pointsLength = self._GetLengthOfPoints(points)
    minimumLength = min(len(text), pointsLength)

    # take a slice of the text that's no longer than the minimum length
    text = text[:minimumLength]

    # add a character if the end of the text is odd and less than the number of points
    if self.ShouldExtend(minimumLength, pointsLength):
      text += '.'
    
    pairedLetters = self._GetLetterPairs(text)

    for i,l in enumerate(pairedLetters):
      points[i].Value = ''.join(l)

    return points

  def _GetLengthOfPoints(self, points):
    pointValues = [p.Value for p in points]
    strOfValues = ''.join(pointValues)
    return len(strOfValues)

  def _GetLetterPairs(self, text):
    firstLetters = text[::2]
    secondLetters = text[1::2]
    return zip(firstLetters, secondLetters)

  def ShouldExtend(self, textLength, pointsLength):
    return (textLength % 2 != 0 and textLength <= pointsLength)
