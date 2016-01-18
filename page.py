from point import Point
import sys

class Page:

  def __init__(self, size):
    if type(size) is tuple:
      self.XAxis = size[0]
      self.YAxis = size[1]
    else:
      self.XAxis = size
      self.YAxis = self.XAxis
    self.__PageRows = self.GeneratePageRows()

  def GetPage(self):
    return self.__PageRows

  def GeneratePageRows(self):
    page = []
    for x in range(0, self.YAxis + 1):
      row = self.GenerateRow(x)
      page.append(row)
    return page

  def GenerateRow(self, rowNumber):
    row = []
    for x in range(0, self.XAxis + 1):
      p = Point(x, rowNumber)
      row.append(p)
    return row

  def Draw(self, io):
    for row in reversed(self.__PageRows):
      for p in row:
        io.write(p.Value)
      io.write('\n')  

# TODO: Add optional axis headings
class Graph(Page):

  def __init__(self, pageSize):
    super().__init__(pageSize * 2)
    page = self.GetPage()
    self.AddRowNumbers(page)
    self.AddColumnNumbers(page)

  def AddRowNumbers(self, page):
    everyOtherX = [p for p in page[0] \
                   if p.X % 2 == 1]
    self._SetAxisNumber(everyOtherX)

  def AddColumnNumbers(self, page):
    everyOtherY = [row[0] for row in page \
                   if row[0].Y % 2 == 1]
    self._SetAxisNumber(everyOtherY)

  def _SetAxisNumber(self, everyOther):
    for i,p in enumerate(everyOther, 1):
      p.Value = self._GetTwoDigitNumber(i)

  def _GetTwoDigitNumber(self, n):
    s = str(n)
    if len(s) == 1:
      s = '0' + s
    elif len(s) > 2:
      s = '99'
    return s
