import json

class Task(object):

  """Represents the tasks to be prioritized"""
  Minimum = 0
  Maximum = 5

  def __init__(self, n, p=0, u=0, i=0):
    """ Initializes Task """
    self.uid = 'aa'
    self.name = n
    self.priority = p
    self.urgency = u
    self.importance = i
    self.eisenhower = u + i

  def __str__(self):
    return 'T(' + self.name + ',' + str(self.priority) + ',' + str(self.urgency) + ',' + str(self.importance) + ')'

  def __repr__(self):
    return self.__str__()

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return (self.name == other.name and
              self.priority == other.priority and
              self.urgency == other.urgency and
              self.importance == other.importance)

  def __ne__(self, other):
    return not self.__eq__(other)

class TaskEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, Task):
      return {"__Task__": True, "name": o.name, "priority": o.priority, "urgency": o.urgency, "importance": o.importance}
    return json.JSONEncoder.default(self, o)

# TODO: Move encoding/decoding to another file
class CustomDecoder(object):
  def as_task(self, dct):
    if '__Task__' in dct:
      return Task(dct['name'], dct['priority'], dct['urgency'], dct['importance'])
    return dct;


