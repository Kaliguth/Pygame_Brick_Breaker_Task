# Ball class file

# pygame imports
import pygame

# Import required global vars
from util.globals import WHITE


class Ball:
    # Constructor
    def __init__(self, position_x, position_y):
        self.position = [position_x, position_y]  # Ball x y position
        self.speed = [0, 3]  # Ball x y speed
        self.radius = 10  # Ball radius
        self.color = WHITE  # Ball color

    # Method to draw/render the ball
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
