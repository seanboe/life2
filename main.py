from graphics import *        # https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
import random as rnd
import time

from configuration import CharacterDefaults, Settings, CharacterRole, GameSettings
from Character import Character


# def main():
#     win = GraphWin("My Circle", Settings.FRAME_HEIGHT.value, Settings.FRAME_WIDTH.value)
#     c = Circle(Point(50,50), 5)
#     c.setOutline("red")
#     c.draw(win)
#     win.getMouse() # Pause to view result, otherwise the window will disappear
#     win.close()
# main()

def drawCharacters(window, characters):
  # refill the window
  window_background = Rectangle(Point(0, 0), Point(Settings.FRAME_WIDTH.value, Settings.FRAME_HEIGHT.value))
  window_background.setFill("white")
  window_background.setOutline("white")
  window_background.draw(window)

  for character in characters:
    c = Circle(Point(character.posX, character.posY), GameSettings.CharacterWidth.value)
    c.setOutline(GameSettings.PREDATOR_COLOR.value if character.role == CharacterRole.PREDATOR else GameSettings.PREY_COLOR.value)
    if character.role == CharacterRole.PREDATOR:
      c2 = Circle(Point(character.posX, character.posY), CharacterDefaults.PREDATOR_SIGHT_RADIUS.value)
      c2.draw(window)
    c.draw(window)

    

def runSim(window):
  characters = []

  # This is initial creation of the characters
  for x in range(0, rnd.randint(1, 3)):
    characters.append(Character(CharacterRole.PREDATOR, rnd.randint(0, Settings.FRAME_WIDTH.value), rnd.randint(0, Settings.FRAME_HEIGHT.value)))
  for x in range(0, rnd.randint(1, 30)):
    characters.append(Character(CharacterRole.PREY, rnd.randint(0, Settings.FRAME_WIDTH.value), rnd.randint(0, Settings.FRAME_HEIGHT.value)))

  for x in range(0, GameSettings.GAME_LOOPS.value):

    for moving_character in characters:
      if moving_character.role == CharacterRole.PREDATOR:
        for victim in characters:
          if victim.role == CharacterRole.PREY:
            if (moving_character.canSee(victim.posX, victim.posY)):
              moving_character.moveByPoint(victim.posX, victim.posY)

    time.sleep(1)

    drawCharacters(window, characters)

    
def main():
  window = GraphWin("Predators", Settings.FRAME_WIDTH.value, Settings.FRAME_HEIGHT.value)
  runSim(window)
  time.sleep(5)
  window.close()

if __name__ == "__main__":
  main()

