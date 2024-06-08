# Brick logic class file

# random Import for random colors
import random

# Object imports
from objects.Brick import Brick

# Import required global vars
from util.globals import WIDTH, BRICK_WIDTH, BRICK_HEIGHT, BRICK_ROWS, BRICK_SPACING_X, BRICK_SPACING_Y


class BrickLogic:
    def __init__(self):
        self.bricks = self.create_bricks()

    # Method to create and return a list of bricks
    # Static method because it does not rely on any of the class' variables
    @staticmethod
    def create_bricks():
        bricks = []  # List of bricks
        num_bricks_x = WIDTH // BRICK_WIDTH  # Number of bricks in a row ( // to floor because it has to be an int)
        num_rows = BRICK_ROWS  # Number of rows

        # loop to create bricks using rows and num_bricks vars
        for row in range(num_rows):
            for col in range(num_bricks_x):
                x = col * (BRICK_WIDTH + BRICK_SPACING_X)  # Column
                y = row * (BRICK_HEIGHT + BRICK_SPACING_Y)  # Row
                # Randomize color for the brick
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Create the brick
                brick = Brick(x, y, color)
                # Add the newly created brick to the list
                bricks.append(brick)

        # Return the bricks list
        return bricks

    # Method to handle collisions of the ball on a brick
    def handle_collisions(self, ball):
        # Goes over the bricks list and checks if any of them came in contact with the ball
        for brick in self.bricks:
            # Check if the ball came in contact with the brick from any direction
            if (brick.rect.left <= ball.position[0] + ball.radius <= brick.rect.right or  # Left or right
                    brick.rect.left <= ball.position[0] - ball.radius <= brick.rect.right) and \
                (brick.rect.top <= ball.position[1] + ball.radius <= brick.rect.bottom or  # Top or bottom
                    brick.rect.top <= ball.position[1] - ball.radius <= brick.rect.bottom):

                # Check specific side hit to determine next movement
                # Top is hit
                if ball.position[1] - ball.radius <= brick.rect.top and ball.speed[1] > 0:
                    ball.speed[1] = -ball.speed[1]  # Ball moves up
                # Bottom is hit
                elif ball.position[1] + ball.radius >= brick.rect.bottom and ball.speed[1] < 0:
                    ball.speed[1] = -ball.speed[1]  # Ball moves down
                # Left is hit
                elif ball.position[0] + ball.radius >= brick.rect.left and ball.speed[0] > 0:
                    ball.speed[0] = -ball.speed[0]  # Ball moves left
                # Right is hit
                elif ball.position[0] - ball.radius <= brick.rect.right and ball.speed[0] < 0:
                    ball.speed[0] = -ball.speed[0]  # Ball move right

                # Remove the brick from the list (will no longer be displayed)
                self.bricks.remove(brick)
                break  # Break to make sure only one brick is removed
