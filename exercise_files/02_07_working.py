import time
import os
from termcolor import colored

#Canvas class that defines some height and width along with
#a matrix of characters to track where TerminalScribes are moving

class Canvas:
  def __init__(self, width, height):
    self._x = width
    self._y = height
    # This is a grid that contains data about where the
    # TerminalScribes have visited
    self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

  #hitsWall returns True if the given point is outside the boundaries of the canvas
  def hitsWall(self, point):
    return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y
  
  #set the given position to the provided character on the canvas
  def setPos(self,pos,mark):
    self._canvas[pos[0]][pos[1]] = mark

  # clear the terminal and then print each line in the canvas
  def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')

  def print(self):
    self.clear()
    for y in range(self._y):
      print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
  def __init__(self, canvas):
    self.canvas = canvas
    self.trail = '.'
    self.mark = '*'
    self.framerate = 0.2
    self.pos = [0,0]

  def up(self):
    pos = [self.pos[0], self.pos[1]-1]
    if not self.canvas.hitsWall(pos):
      self.draw(pos)

  def down(self):
    pos = [self.pos[0], self.pos[1]+1]
    if not self.canvas.hitsWall(pos):
      self.draw(pos)

  def right(self):
    pos = [self.pos[0]+1, self.pos[1]]
    if not self.canvas.hitsWall(pos):
      self.draw(pos)

  def left(self):
    pos = [self.pos[0]-1, self.pos[1]]
    if not self.canvas.hitsWall(pos):
      self.draw(pos)

  def draw(self, pos):
    # Set the old position to the "trail" symbol
    self.canvas.setPos(self.pos, self.trail)
    # Update position
    self.pos = pos
    # Set the new position to the "mark" symbol
    self.canvas.setPos(self.pos, colored(self.mark, 'red'))
    #Print everything to the screen
    self.canvas.print()
    #Sleep for a little bit to create the animation
    time.sleep(self.framerate)

  def drawSquare(self, size):
    
    for i in range(size):  
      scribe.right()
    for i in range(size):
      scribe.down()
    for i in range(size):
      scribe.left()
    for i in range(size):
      scribe.up()

# Create a new Canvas instance that is 30 units wide by 30 units tall
canvas = Canvas(30,30)
# Create a new scribe and give it the canvas object
scribe = TerminalScribe(canvas)

scribe.drawSquare(5)

# first fill-in example
'''
for i in range(0, 10):
  for j in range(0, 10):
    scribe.draw((i,j))
'''
