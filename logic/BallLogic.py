# Ball logic class file

# Object imports
from objects.Ball import Ball

# Import required global vars
from util.globals import WIDTH, HEIGHT


class BallLogic:
    # Constructor
    def __init__(self, ball: Ball):
        self.ball = ball  # Ball to apply logics on
        self.first_hit = False  # Boolean to determine if paddle hit ball yet (used to direction)
        # Explanation:
        # Ball first moves straight down, once paddle hits it for the first time, it moves sideways

    # Method to handle ball logics
    def handle_ball_logic(self):
        # Movement by using ball speed
        self.ball.position[0] += self.ball.speed[0]
        self.ball.position[1] += self.ball.speed[1]

        # Changing directions when walls are hit
        if self.ball.position[0] <= 0 or self.ball.position[0] >= WIDTH:
            self.ball.speed[0] = -self.ball.speed[0]
        if self.ball.position[1] <= 0:
            self.ball.speed[1] = -self.ball.speed[1]
        # If ball falls below the paddle
        if self.ball.position[1] >= HEIGHT + 5:
            return True  # Returns True for the game class to return game over screen

    # Method to check collisions with the ball
    def check_collision(self, paddle):
        # Paddle hits ball - changes direction
        if paddle.paddle_rect.collidepoint(self.ball.position[0], self.ball.position[1] + self.ball.radius):
            self.ball.speed[1] = -self.ball.speed[1]

            # When ball first hits the paddle, change ball's x speed to start moving sideways
            if not self.first_hit:
                self.ball.speed[0] = 3
                self.first_hit = True  # Change first hit boolean to True
