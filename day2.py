from aoc import *
import time

class DayTwo:

  mem = []

  def __init__(self, mem):
    for line in mem:
      game = line.split(':')
      self.mem.append({ints(game[0])[0]: [games.split(',') for games in game[1].split(';')]}) 

  def partOne(self):
    print(self.mem[0])

  def partTwo(self):
    pass

if __name__ == '__main__':
  y = fileOpenLines(2)
  dayTwo = DayTwo(y)
  startTime = time.time()
  print("Part 1: ", dayTwo.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwo.partTwo(), " in ", round(time.time() - startTime, 2), "s")