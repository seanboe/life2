from tkinter.constants import X
import math
from configuration import CharacterDefaults, CharacterRole

# Computes the distance between two points
def find_distance(x1, y1, x2, y2):
  dX = x2 - x1
  dY = y2 - y1
  return math.sqrt(pow(dX, 2) + pow(dY, 2))

# Declaration of Character Class, used to define the predators and the prey
class Character:

  def __init__(self, predator_prey, x, y):
    self.role = predator_prey
    self.sight_radius = 0
    self.movement_radius = 0

    self.posX = x
    self.posY = y

    if self.role == CharacterRole.PREY:
      self.sight_radius = CharacterDefaults.PREY_SIGHT_RADIUS.value
      self.movement_radius = CharacterDefaults.PREY_MOVEMENT_RADIUS.value
    elif self.role == CharacterRole.PREDATOR:
      self.sight_radius = CharacterDefaults.PREDATOR_SIGHT_RADIUS.value
      self.movement_radius = CharacterDefaults.PREDATOR_MOVEMENT_RADIUS.value

  def canSee(self, coordX, coordY):

    distance = find_distance(self.posX, self.posY, coordX, coordY)

    if self.sight_radius >= distance:
      return True
    else:
      return False

  def moveByPoint(self, coordX, coordY, go_towards_point):
    dX = coordX - self.posX
    dY = coordY - self.posY

    angle = math.atan2(dY, dX)

    seperation = find_distance(self.posX, self.posY, coordX, coordY)

    if seperation < self.movement_radius:
      movement_distance = seperation
    else:
      movement_distance = self.movement_radius

    if not go_towards_point:
      movement_distance *= -1

    self.posX += int(movement_distance * math.cos(angle))
    self.posY += int(movement_distance * math.sin(angle))

  def updateAge(self, newAge):
    self.age = newAge


# class Predator(Character):
  
#   has_target = False
#   survey_coords = ()    # If a predator doesn't see anything, then it will begin going to a random coordinate held here

#   def setTargetStatus(self, has_target, *survey_coords):
#     self.has_target = has_target

#     self.survey_coords = survey_coords
