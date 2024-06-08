# Paddle class file

# pygame imports
import pygame
from pygame import Surface


class Paddle:
    # Constructor
    def __init__(self, position_x, position_y, width, height, color: pygame.color):
        self.__position_x = position_x  # X position
        self.__position_y = position_y  # Y position
        self.__width = width  # Paddle width
        self.__height = height  # Paddle height
        self.__color = color  # Paddle color
        # Paddle rectangle
        self.paddle_rect = pygame.Rect(self.__position_x - self.__width / 2, self.__position_y,
                                       self.__width, self.__height)

    # Method to draw/render the paddle
    def draw(self, screen: Surface):
        pygame.draw.rect(screen, self.__color, self.paddle_rect)
