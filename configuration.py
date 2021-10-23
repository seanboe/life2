from enum import Enum

class Settings(Enum):
  FRAME_WIDTH  = 800
  FRAME_HEIGHT = 500
  FRAME_MARGIN = 150

# Character settings
class GameSettings(Enum):
  GAME_LOOPS            = 1000
  PREDATOR_COLOR = "red"
  PREY_COLOR     = "blue"
  CharacterWidth = 2

class CharacterDefaults(Enum):
  PREY_MOVEMENT_RADIUS  = 7
  PREY_SIGHT_RADIUS = 35
  PREDATOR_MOVEMENT_RADIUS = 11
  PREDATOR_SIGHT_RADIUS = 25

class CharacterRole(Enum):
  PREDATOR = 0
  PREY     = 1
