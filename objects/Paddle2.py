import pygame
from pygame import Surface

WIDTH = 1280


class Paddle2:
    def __init__(self, position_x, position_y, width, height, color: pygame.Color):
        self.__position_x = position_x
        self.__position_y = position_y
        self.__width = width
        self.__height = height
        self.__speed = 10  # Adjust speed as necessary
        self.__color = color
        self.paddle_rect = pygame.Rect(self.__position_x - self.__width / 2, self.__position_y, self.__width, self.__height)

    def move_left(self):
        self.__position_x -= self.__speed
        if self.__position_x - self.__width / 2 < 0:
            self.__position_x = self.__width / 2
        self.paddle_rect.x = self.__position_x - self.__width / 2

    def move_right(self):
        self.__position_x += self.__speed
        if self.__position_x + self.__width / 2 > WIDTH:
            self.__position_x = WIDTH - self.__width / 2
        self.paddle_rect.x = self.__position_x - self.__width / 2

    def draw(self, screen: Surface):
        pygame.draw.rect(screen, self.__color, self.paddle_rect)
