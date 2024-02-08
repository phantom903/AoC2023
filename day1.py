from aoc import *

def digitsFromNames(mixedStr, asChars=False):
  mixedStr = mixedStr.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e')
  if asChars:
    return [val for val in mixedStr if val.isdigit()]
  else:
    return [int(val) for val in mixedStr if val.isdigit()]
  
class DayOne:

  mem = []
  vals = []
  valspt2 = []

  def __init__(self, mem):
    self.mem = mem.copy()
    for line in mem:
      self.vals.append(digits(line, True))
      self.valspt2.append(digitsFromNames(line, True))

  def partOne(self):
    return sum(int(i[0] + i[-1]) for i in self.vals)

  def partTwo(self):
    return sum(int(i[0] + i[-1]) for i in self.valspt2)

