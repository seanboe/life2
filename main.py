from graphics import *        # https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
import random as rnd
import time

from configuration import CharacterDefaults, Settings, CharacterRole, GameSettings
from Character import Character, Predator, Prey

FRAME_WIDTH  = Settings.FRAME_WIDTH.value
FRAME_HEIGHT = Settings.FRAME_HEIGHT.value
FRAME_MARGIN = Settings.FRAME_MARGIN.value

def getRandomCharacterPosition(x_or_y):
  if x_or_y == "x":
    return rnd.randint(FRAME_MARGIN, FRAME_MARGIN + FRAME_WIDTH)
  elif x_or_y == "y":
    return rnd.randint(FRAME_MARGIN, FRAME_MARGIN + FRAME_HEIGHT)


def drawCharacters(window, characters):
  # refill the window
  window_background = Rectangle(Point(0, 0), Point(FRAME_WIDTH + 2 * FRAME_MARGIN, FRAME_HEIGHT + 2 * FRAME_MARGIN))
  window_background.setFill("white")
  window_background.setOutline("black")
  window_background.draw(window)

  frame = Rectangle(Point(FRAME_MARGIN, FRAME_MARGIN), Point(FRAME_MARGIN + FRAME_WIDTH, FRAME_MARGIN + FRAME_HEIGHT))
  frame.setOutline("black")
  frame.draw(window)

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
  for x in range(0, rnd.randint(0, 0)):
    predators.append(Predator(getRandomCharacterPosition("x"), getRandomCharacterPosition("y")))
  for x in range(0, rnd.randint(0, 1)):
    prey.append(Prey(getRandomCharacterPosition("x"), getRandomCharacterPosition("y")))

  for cycle in range(1, GameSettings.GAME_LOOPS.value):

    # Predators look for and attack prey. Otherwise, they find a random position
    # to move towards and travel there until they see prey
    for predator in predators:
      has_victim = False
      for victim in prey:
        if predator.canSee(victim.posX, victim.posY):
          has_victim = True
          predator.setTargetStatus(has_victim, victim.posX, victim.posY)
          
        if (predator.posX == victim.posX) and (predator.posY == victim.posY):
          predator.giveFood()
          prey.remove(victim)

      if (not has_victim) and predator.has_victim:
        predator.setTargetStatus(has_victim, getRandomCharacterPosition("x"), getRandomCharacterPosition("y"))
      elif (not has_victim) and (not predator.has_victim) and (predator.posX == predator.targetX) and (predator.posY == predator.targetY):
        predator.setTargetStatus(has_victim, getRandomCharacterPosition("x"), getRandomCharacterPosition("y"))

      predator.moveByPoint(predator.targetX, predator.targetY, True)

    # Prey run away from predators
    for victim in prey:
      for predator in predators:
        if victim.canSee(predator.posX, predator.posY):
          victim.moveByPoint(predator.posX, predator.posY, False)

    # Check if predators have starved
    predators = [predator for predator in predators if cycle < predator.next_starve_cycle]

    # Predators reproduce
    predator_children = []
    if cycle % CharacterDefaults.PREDATOR_REPRODUCTION_CYCLES.value == 0:
      for predator in predators:
        predator_children.append(predator.reproduce(Predator(predator.posX + rnd.randint(-10, 10), predator.posY + rnd.randint(-10, 10))))
    predators += predator_children

    # Prey Reproduce
    prey_children = []
    if cycle % CharacterDefaults.PREY_REPRODUCTION_CYCLES.value == 0:
      for victim in prey:
        prey_children.append(victim.reproduce(Prey(victim.posX + rnd.randint(-50, 50), victim.posY + rnd.randint(-50, 50))))
    prey += prey_children

    time.sleep(0.5)

    characters = predators + prey
    drawCharacters(window, characters)
    Text(Point(30, 10), f"Cycle: {cycle}").draw(window)

def main():
  window = GraphWin("Predators", Settings.FRAME_WIDTH.value + 2 * FRAME_MARGIN, Settings.FRAME_HEIGHT.value + 2 * FRAME_MARGIN)
  runSim(window)
  time.sleep(5)
  window.close()

if __name__ == "__main__":
  main()

