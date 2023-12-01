from aoc import *

class DayOne:

  mem = []
  vals = []

  def __init__(self, mem):
    self.mem = mem.copy()
    for line in mem:
      print(digits(line))
      self.vals.append(ints(line))

  def partOne(self):
    return sum(sum([i[0], i[-1]]) for i in self.vals)
      

  def partTwo(self):
    pass