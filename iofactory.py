import os
import sys
import json

# Note: should not include JsonIO because it cannot be used in all 
#       circumstances the others may because of encode/decode.
class IOFactory(object):

  """ Produces IO objects that manage the user's interaction with data """
  
  def GetInstance(self, path=None):
    if path == None:
      return ConsoleIO()
    else:
      return FileIO(path)

class ConsoleIO(object):

  """ Manages IO with the console """

  def read(self):
    val = input()
    return val

  def write(self, content):
    sys.stdout.write(content)

  def clear(self):
    os.system('cls')


class FileIO(object):

  """ Manage IO with a File """

  def __init__(self, path):
    self.path = path

  def read(self):
    with open(self.path, 'r') as f:
      return f.readlines()

  def write(self, content):
    with open(self.path, 'w') as f:
      f.write(str(content))

class JsonIO(FileIO):

  """ Manage IO with a Json File """

  def __init__(self, path):
    FileIO.__init__(self, path)

  def read(self, JSONDecodeFunc=None):
    with open(self.path, 'r') as f:
      if JSONDecodeFunc == None:
        return json.load(f)
      else:
        return json.load(f, object_hook=JSONDecodeFunc)

  def write(self, content, JSONEncodeClass=None):
    with open(self.path, 'w') as f:
      if JSONEncodeClass == None:
        json.dump(content, f, sort_keys=True, indent=2)
      else:
        json.dump(content, f, cls=JSONEncodeClass, sort_keys=True, indent=2)

# TODO: Move FakeIO and StackItem into their own test file
# TODO: Make FakeIO generic and/or make a base fake IO with inherited members
#       unique to the needs of different IO objects
class FakeIO(object):

  """ A Mock IO object to use for testing purposes """

  def __init__(self, path=None, callStack=None):
    self.path = path
    self.writeContent = []
    self.writeCount = 0
    self.lastWrite = ''
    self.readCount = 0
    self.callStack = callStack
    self.wasCleared = False
    
  def read(self, exitCode=None, returnType=None, JSONDecodeFunc=None):
    self.readCount += 1
    if self.callStack != None:
      return self.getFromCallStack()

  def write(self, content, JSONEncodeClass=None):
    self.writeContent.append(content)
    self.lastWrite = content
    self.writeCount += 1

  def clear(self):
    self.wasCleared = True

  def getFromCallStack(self):
    response = None
    # Ensure the calls follow order
    self.callStack.sort(key=lambda i: i.order)
    for item in self.callStack:
      if item.message == self.lastWrite:
        # Gets response and removes this item
        # from the stack so it's not called again
        response = item.response
        self.callStack.remove(item)
    return response

class StackItem(object):

  """ A representation of the mock's call stack, used for complex integration testing """

  def __init__(self, order, message, response):
    self.order = order
    self.message = message
    self.response = response

  def __str__(self):
    return 'Stack(' + str(self.order) + ', mes:' + self.message + ', resp:' + str(self.response) + ')'
  
  def __repr__(self):
    return self.__str__()
