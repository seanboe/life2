from graphics import *        # https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
import random as rnd
import time

from configuration import CharacterDefaults, Settings, CharacterRole, GameSettings
from Character import Character, Predator

FRAME_WIDTH  = Settings.FRAME_WIDTH.value
FRAME_HEIGHT = Settings.FRAME_HEIGHT.value

def drawCharacters(window, characters):
  # refill the window
  window_background = Rectangle(Point(0, 0), Point(Settings.FRAME_WIDTH.value, Settings.FRAME_HEIGHT.value))
  window_background.setFill("white")
  window_background.setOutline("black")
  window_background.draw(window)

  for character in characters:
    c = Circle(Point(character.posX, character.posY), GameSettings.CharacterWidth.value)
    c.setOutline(GameSettings.PREDATOR_COLOR.value if character.role == CharacterRole.PREDATOR else GameSettings.PREY_COLOR.value)
    if character.role == CharacterRole.PREDATOR:
      c2 = Circle(Point(character.posX, character.posY), CharacterDefaults.PREDATOR_SIGHT_RADIUS.value)
      c2.setOutline("red")
      c2.draw(window)
    if character.role == CharacterRole.PREY:
      c2 = Circle(Point(character.posX, character.posY), CharacterDefaults.PREY_SIGHT_RADIUS.value)
      c2.setOutline("blue")
      c2.draw(window)
    c.draw(window)


def runSim(window):

  predators = []
  prey = []

  # This is initial creation of the characters
  for x in range(0, rnd.randint(3, 5)):
    predators.append(Predator(CharacterRole.PREDATOR, rnd.randint(0, FRAME_WIDTH), rnd.randint(0, FRAME_HEIGHT)))
  for x in range(0, rnd.randint(10, 15)):
    prey.append(Character(CharacterRole.PREY, rnd.randint(0, FRAME_WIDTH), rnd.randint(0, FRAME_HEIGHT)))

  for cycle in range(0, GameSettings.GAME_LOOPS.value):

    # Predators attack prey
    for predator in predators:
      has_victim = False
      for victim in prey:
        if predator.canSee(victim.posX, victim.posY):
          has_victim = True
          predator.setTargetStatus(has_victim, victim.posX, victim.posY)
          
        if (predator.posX == victim.posX) and (predator.posY == victim.posY):
          prey.remove(victim)

      if (not has_victim) and predator.has_victim:
        predator.setTargetStatus(has_victim, rnd.randint(0, FRAME_WIDTH), rnd.randint(0, FRAME_WIDTH))
      elif (not has_victim) and (not predator.has_victim) and (predator.posX == predator.targetX) and (predator.posY == predator.targetY):
        predator.setTargetStatus(has_victim, rnd.randint(0, FRAME_WIDTH), rnd.randint(0, FRAME_WIDTH))

      predator.moveByPoint(predator.targetX, predator.targetY, True)

    # Prey run away from predators
    for victim in prey:
      for predator in predators:
        if victim.canSee(predator.posX, predator.posY):
          victim.moveByPoint(predator.posX, predator.posY, False)

    time.sleep(2)

    characters = predators + prey
    drawCharacters(window, characters)
    Text(Point(30, 10), f"Cycle: {cycle}").draw(window)

def main():
  window = GraphWin("Predators", Settings.FRAME_WIDTH.value, Settings.FRAME_HEIGHT.value)
  runSim(window)
  time.sleep(5)
  window.close()

if __name__ == "__main__":
  main()

