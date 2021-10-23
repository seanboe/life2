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
  PREY_MOVEMENT_RADIUS  = 20
  PREY_SIGHT_RADIUS = 60
  PREDATOR_MOVEMENT_RADIUS = 30
  PREDATOR_SIGHT_RADIUS = 45

  # Initial hunger level
  PREDATOR_KILL_SATURATION = 10

class CharacterRole(Enum):
  PREDATOR = 0
  PREY     = 1
