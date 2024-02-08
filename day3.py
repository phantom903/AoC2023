from aoc import *
import time

class DayThree:

  mem = []

  def __init__(self, mem):
    for line in mem:
      self.mem.append([i for i in line])

  def partOne(self):
    print(self.mem)

  def partTwo(self):
    pass

if __name__ == '__main__':
  y = fileOpenLines(3)
  dayThree = DayThree(y)
  startTime = time.time()
  print("Part 1: ", dayThree.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayThree.partTwo(), " in ", round(time.time() - startTime, 2), "s")