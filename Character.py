from tkinter.constants import X
import math
import random as rnd
from configuration import CharacterRole, CharacterDefaults

# Computes the distance between two points
def find_distance(x1, y1, x2, y2):
  dX = x2 - x1
  dY = y2 - y1
  return math.sqrt(pow(dX, 2) + pow(dY, 2))

# Declaration of Character Class, used to define the predators and the prey
class Character:

  def __init__(self, x, y):
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

    return self

  def reproduce(self, child):

    if self.role == CharacterRole.PREDATOR:
      SIGHT_RADIUS_MUTATION_FACTOR = (rnd.random() * CharacterDefaults.PREDATOR_MAX_SIGHT_RADIUS_PERCENT_MUTATION.value) / 100
    elif self.role == CharacterRole.PREY:
      SIGHT_RADIUS_MUTATION_FACTOR = (rnd.random() * CharacterDefaults.PREY_MAX_SIGHT_RADIUS_PERCENT_MUTATION.value) / 100

    if self.role == CharacterRole.PREDATOR:
      MOVEMENT_RADIUS_MUTATION_FACTOR = (rnd.random() * CharacterDefaults.PREDATOR_MOVEMENT_RADIUS_MUTATION_FACTOR.value) / 100
    elif self.role == CharacterRole.PREY:
      MOVEMENT_RADIUS_MUTATION_FACTOR = (rnd.random() * CharacterDefaults.PREY_MOVEMENT_RADIUS_MUTATION_FACTOR.value) / 100

    child.sight_radius = self.sight_radius + (self.sight_radius * SIGHT_RADIUS_MUTATION_FACTOR) * (-1 if rnd.random() < 0.5 else 1)
    child.movement_radius = self.movement_radius + (self.movement_radius * MOVEMENT_RADIUS_MUTATION_FACTOR) * (-1 if rnd.random() < 0.5 else 1)

    return child

class Predator(Character):

  role = CharacterRole.PREDATOR

  has_victim = True

  next_starve_cycle = CharacterDefaults.PREDATOR_KILL_SATURATION.value

  def setTargetStatus(self, has_target, targetX, targetY):
    self.has_victim = has_target
    self.targetX = targetX
    self.targetY = targetY

    return self

  def giveFood(self):
    self.next_starve_cycle += CharacterDefaults.PREDATOR_KILL_SATURATION.value

    return self

class Prey(Character):
  role = CharacterRole.PREY