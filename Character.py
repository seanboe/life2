from tkinter.constants import X
import math
from configuration import CharacterDefaults, CharacterRole

# Declaration of Character Class, used to define the predators and the prey
class Character:
  
  def __init__(self, predator_prey, x, y):
    self.posX = x
    self.posY = y
    self.role = predator_prey
    self.age = 0
    self.sight_radius = 0
    self.movement_radius = 0

    if self.role == CharacterRole.PREY:
      self.sight_radius = CharacterDefaults.PREY_SIGHT_RADIUS.value
      self.movement_radius = CharacterDefaults.PREY_MOVEMENT_RADIUS.value
    elif self.role == CharacterRole.PREDATOR:
      self.sight_radius = CharacterDefaults.PREDATOR_SIGHT_RADIUS.value
      self.movement_radius = CharacterDefaults.PREDATOR_MOVEMENT_RADIUS.value

  def canSee(self, coordX, coordY):
    dX = coordX - self.posX
    dY = coordY - self.posY

    distance = math.sqrt(pow(dX, 2) + pow(dY, 2))

    if self.sight_radius >= distance:
      return True
    else:
      return False

  def moveByPoint(self, coordX, coordY):
    dX = coordX - self.posX
    dY = coordY - self.posY

    angle = math.atan2(dY, dX)

    distance = math.sqrt(pow(dX, 2) + pow(dY, 2))

    if distance < self.movement_radius:
      self.posX += int(distance * math.cos(angle))
      self.posY += int(distance * math.sin(angle))
    else:
      self.posX = self.posX + int(self.movement_radius * math.cos(angle))
      self.posY = self.posY + int(self.movement_radius * math.sin(angle))