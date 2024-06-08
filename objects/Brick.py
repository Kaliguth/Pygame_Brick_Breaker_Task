# Brick class file

# pygame imports
import pygame

# Import required global vars
from util.globals import BRICK_WIDTH, BRICK_HEIGHT


class Brick:
    # Constructor
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)  # Brick rectangle
        self.color = color  # Brick color
