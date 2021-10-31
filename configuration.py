from enum import Enum

class Settings(Enum):
  FRAME_WIDTH  = 800
  FRAME_HEIGHT = 500
  FRAME_MARGIN = 150

# Character settings
class GameSettings(Enum):
  GAME_LOOPS      = 1000
  PREDATOR_COLOR  = "red"
  PREY_COLOR      = "blue"
  CHARACTER_WIDTH = 5
  CYCLE_DELAY     = 250

class CharacterDefaults(Enum):

  PREDATOR_MOVEMENT_RADIUS  = 65
  PREDATOR_SIGHT_RADIUS     = 75
  PREDATOR_KILL_SATURATION = 10
  PREDATOR_MAX_SIGHT_RADIUS_PERCENT_MUTATION = 10  # Children will randomly be up to 5% different than their parents
  PREDATOR_MOVEMENT_RADIUS_MUTATION_FACTOR = 10  # Children will randomly be up to 5% different than their parents
  PREDATOR_REPRODUCTION_CYCLES = 15

  PREY_MOVEMENT_RADIUS = 25
  PREY_SIGHT_RADIUS    = 100
  PREY_MAX_SIGHT_RADIUS_PERCENT_MUTATION = 10  # Children will randomly be up to 5% different than their parents
  PREY_MOVEMENT_RADIUS_MUTATION_FACTOR = 10
  PREY_REPRODUCTION_CYCLES = 8


class CharacterRole(Enum):
  PREDATOR = 0
  PREY     = 1

class Colors(Enum):
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  BLUE  = (0, 0, 255)
  RED   = (255, 0, 0)
  GREEN = (0, 255, 0)

