import pygame
from util.globals import WIDTH, HEIGHT, WHITE


class Ball2:
    def __init__(self, position_x, position_y):
        self.position = [position_x, position_y]
        self.speed = [2, 2]
        self.radius = 10
        self.color = WHITE

    def update(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        if self.position[0] <= 0 or self.position[0] >= WIDTH:
            self.speed[0] = -self.speed[0]
        if self.position[1] <= 0:
            self.speed[1] = -self.speed[1]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def reset_position(self):
        self.position = [WIDTH / 2, HEIGHT / 2]
        self.speed = [5, 5]

    def check_collision(self, paddle):
        if paddle.paddle_rect.collidepoint(self.position[0], self.position[1] + self.radius):
            self.speed[1] = -self.speed[1]