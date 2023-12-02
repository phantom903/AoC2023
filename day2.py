from aoc import *
import time

class DayTwo:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    pass

  def partTwo(self):
    pass

if __name__ == '__main__':
  y = fileOpenLines(2)
  dayTwo = DayTwo(y)
  startTime = time.time()
  print("Part 1: ", dayTwo.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwo.partTwo(), " in ", round(time.time() - startTime, 2), "s")