from pygame import display

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
SCALE = 0

def load(width, height, scale=1, fullscreen=False):
    if(display.get_init()):
        raise Exception("ALREADY INITIATED")
    SCREEN_WIDTH = width * scale
    SCREEN_HEIGHT = height * scale
    SCALE = scale
