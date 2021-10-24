import pygame, sys
from pygame.locals import *
import random as rnd

from configuration import CharacterDefaults, Settings, CharacterRole, GameSettings, Colors
from Character import Character, Predator, Prey

FRAME_WIDTH  = Settings.FRAME_WIDTH.value
FRAME_HEIGHT = Settings.FRAME_HEIGHT.value
FRAME_MARGIN = Settings.FRAME_MARGIN.value

def getRandomCharacterPosition(x_or_y):
  if x_or_y == "x":
    return rnd.randint(FRAME_MARGIN, FRAME_MARGIN + FRAME_WIDTH)
  elif x_or_y == "y":
    return rnd.randint(FRAME_MARGIN, FRAME_MARGIN + FRAME_HEIGHT)

def drawText(canvas, text, font_size, posX, posY):
  font = pygame.font.SysFont("didot.ttc", font_size)
  text_img = font.render(text, True, Colors.BLACK.value)
  canvas.blit(text_img, (posX, posY))
  pygame.display.update()

def drawCharacters(canvas, characters):
  # Clear the canvas
  canvas.fill(Colors.WHITE.value)

  # Draw the frame
  pygame.draw.rect(canvas, Colors.BLACK.value, (FRAME_MARGIN, FRAME_MARGIN, FRAME_WIDTH, FRAME_HEIGHT), 2)

  # draw the characters
  for character in characters:
    pygame.draw.circle(canvas, character.color, (character.posX, character.posY), GameSettings.CHARACTER_WIDTH.value, 2)
    pygame.draw.circle(canvas, character.color, (character.posX, character.posY), character.sight_radius, 2)
  pygame.display.update()


def runSim(canvas):

  predators = []
  prey = []

  # This is initial creation of the characters
  for x in range(0, rnd.randint(6, 8)):
    predators.append(Predator(getRandomCharacterPosition("x"), getRandomCharacterPosition("y"), Colors.RED.value, 0))
  for x in range(0, rnd.randint(5, 10)):
    prey.append(Prey(getRandomCharacterPosition("x"), getRandomCharacterPosition("y"), Colors.BLUE.value))

  characters = predators + prey

  drawCharacters(canvas, characters)

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
        predator_children.append(predator.reproduce(Predator(predator.posX + rnd.randint(-10, 10), predator.posY + rnd.randint(-10, 10), Colors.RED.value, cycle)))
    predators += predator_children

    # Prey Reproduce
    prey_children = []
    if cycle % CharacterDefaults.PREY_REPRODUCTION_CYCLES.value == 0:
      for victim in prey:
        prey_children.append(victim.reproduce(Prey(victim.posX + rnd.randint(-50, 50), victim.posY + rnd.randint(-50, 50), Colors.BLUE.value)))
    prey += prey_children


    characters = predators + prey
    drawCharacters(canvas, characters)
    drawText(canvas, f"Cycle: {cycle}", 24, 20, 20)

    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()

    pygame.time.wait(1000)

def main():
  pygame.init()
  canvas = pygame.display.set_mode((Settings.FRAME_WIDTH.value + 2 * FRAME_MARGIN, Settings.FRAME_HEIGHT.value + 2 * FRAME_MARGIN))
  runSim(canvas)
  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main()