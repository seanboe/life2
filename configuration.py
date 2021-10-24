from enum import Enum

class Settings(Enum):
  FRAME_WIDTH  = 800
  FRAME_HEIGHT = 500
  FRAME_MARGIN = 150

# Character settings
class GameSettings(Enum):
  GAME_LOOPS     = 1000
  PREDATOR_COLOR = "red"
  PREY_COLOR     = "blue"
  CharacterWidth = 10

class CharacterDefaults(Enum):

  PREDATOR_MOVEMENT_RADIUS  = 30
  PREDATOR_SIGHT_RADIUS     = 45
  PREDATOR_KILL_SATURATION = 10
  PREDATOR_MAX_SIGHT_RADIUS_PERCENT_MUTATION = 5  # Children will randomly be up to 5% different than their parents
  PREDATOR_MOVEMENT_RADIUS_MUTATION_FACTOR = 5  # Children will randomly be up to 5% different than their parents
  PREDATOR_REPRODUCTION_CYCLES = 15

  PREY_MOVEMENT_RADIUS = 20
  PREY_SIGHT_RADIUS    = 60
  PREY_MAX_SIGHT_RADIUS_PERCENT_MUTATION = 5  # Children will randomly be up to 5% different than their parents
  PREY_MOVEMENT_RADIUS_MUTATION_FACTOR = 5
  PREY_REPRODUCTION_CYCLES = 10


class CharacterRole(Enum):
  PREDATOR = 0
  PREY     = 1
