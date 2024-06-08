# Paddle logic class file

# Object imports
from objects.Paddle import Paddle

# Import required global vars
from util.globals import WIDTH


class PaddleLogic:
    # Constructor
    def __init__(self, paddle: Paddle):
        self.paddle = paddle  # Paddle to apply logics on
        self.speed = 11  # Paddle speed

    # Method to move paddle left
    def move_left(self):
        if self.paddle.paddle_rect.left > 4:
            self.paddle.paddle_rect.x -= self.speed

    # Method to move paddle right
    def move_right(self):
        if self.paddle.paddle_rect.right < WIDTH - 4:
            self.paddle.paddle_rect.x += self.speed
