from enum import Enum

class Settings(Enum):
  FRAME_WIDTH  = 1000
  FRAME_HEIGHT = 700

# Character settings
class GameSettings(Enum):
  GAME_LOOPS            = 100
  PREDATOR_COLOR = "red"
  PREY_COLOR     = "blue"
  CharacterWidth = 5

class CharacterDefaults(Enum):
  PREY_MOVEMENT_RADIUS  = 10
  PREY_SIGHT_RADIUS = 75
  PREDATOR_MOVEMENT_RADIUS = 15
  PREDATOR_SIGHT_RADIUS = 50

class CharacterRole(Enum):
  PREDATOR = 0
  PREY     = 1
