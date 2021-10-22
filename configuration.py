from enum import Enum

class Settings(Enum):
  FRAME_WIDTH  = 1000
  FRAME_HEIGHT = 700

# Character settings
class GameSettings(Enum):
  GAME_LOOPS            = 100
  PREDATOR_COLOR = "red"
  PREY_COLOR     = "blue"
  CharacterWidth = 10

class CharacterDefaults(Enum):
  PREY_MOVEMENT_RADIUS  = 5
  PREY_SIGHT_RADIUS = 5
  PREDATOR_MOVEMENT_RADIUS = 25
  PREDATOR_SIGHT_RADIUS = 100

class CharacterRole(Enum):
  PREDATOR = 0
  PREY     = 1
