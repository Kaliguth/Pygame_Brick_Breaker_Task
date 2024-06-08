# Game class file

# pygame imports
import pygame
from pygame import Surface
# Object imports
from objects.Paddle import Paddle
from objects.Ball import Ball
# Logic imports
from logic.PaddleLogic import PaddleLogic
from logic.BallLogic import BallLogic
from logic.BrickLogic import BrickLogic
# UI imports
from ui.Pause import PauseScreen

# Import required global vars
from util.globals import WIDTH, HEIGHT, BACKGROUND, BLACK, LIGHT_RED, HUGE_FONT, GAME_OVER_TEXT, YOU_WIN_TEXT


class Game:
    # Constructor
    def __init__(self, screen):
        self.screen: Surface = screen  # Set the screen's resolution to be the same as menu's
        self.clock = pygame.time.Clock()  # pygame's Clock module for fps management
        self.game_in_progress = True  # Boolean to determine if the game is in progress
        self.game_is_paused = False  # Boolean to determine if the game is paused
        self.countdown = 3  # Variable for countdown before game starts
        self.__paddle = Paddle(WIDTH / 2, HEIGHT - 40, 170, 20, LIGHT_RED)  # Paddle object creation
        self.__ball = Ball(WIDTH / 2, HEIGHT / 2 - 80)  # Ball object creation
        self.__paddle_logic = PaddleLogic(self.__paddle)  # Paddle logic object creation
        self.__ball_logic = BallLogic(self.__ball)  # Ball logic object creation
        self.__brick_logic = BrickLogic()  # Brick logic object creation
        self.__bricks = self.__brick_logic.bricks  # Bricks list creation (out of game's brick logic object)

        self.run_game()  # Run the game's main method

    # Run method
    # This method runs the main loop and all other methods
    def run_game(self):
        while self.game_in_progress:
            self.handle_events()
            self.draw_game_objects()
            # Countdown before game starts
            if self.countdown > 0:
                self.display_countdown()
            # If game is not paused
            elif not self.game_is_paused:
                self.handle_game_logic()
            # If game is paused
            else:
                self.pause_game()
            self.clock.tick(60)  # Set FPS to 60

            # If ball's handle_ball_logic returns True - means the ball fell below the paddle
            if self.__ball_logic.handle_ball_logic():
                # Display game over screen
                self.show_game_over()

    # Method to handle user events
    def handle_events(self):
        for event in pygame.event.get():
            # Quit by X button
            if event.type == pygame.QUIT:
                # Quits game
                self.game_in_progress = False
            if event.type == pygame.KEYDOWN:
                # Pause game by pressing ESC
                if event.key == pygame.K_ESCAPE:
                    # Changes the Boolean for displaying pause menu
                    self.game_is_paused = True

    # Method to handle all game logics
    def handle_game_logic(self):
        keys = pygame.key.get_pressed()  # Variable for key inputs list
        # If left key is pressed - paddle moves left
        if keys[pygame.K_LEFT]:
            self.__paddle_logic.move_left()
        # If right key is pressed - paddle moves right
        if keys[pygame.K_RIGHT]:
            self.__paddle_logic.move_right()

        self.__ball_logic.handle_ball_logic()  # Initiate ball logic method
        self.__ball_logic.check_collision(self.__paddle)  # Initiate ball collisions logic
        self.__brick_logic.handle_collisions(self.__ball)  # Initiate bricks collisions logic

        # If bricks list is empty
        if not self.__bricks:
            # Displays You Win screen
            self.show_you_win()

    # Method to draw/render all game objects
    def draw_game_objects(self):
        # Screen background fill
        self.screen.fill(BACKGROUND)

        # Objects:
        # Paddle render
        self.__paddle.draw(self.screen)
        # Ball render
        self.__ball.draw(self.screen)

        # Bricks render
        for brick in self.__bricks:
            pygame.draw.rect(self.screen, brick.color, brick.rect)

        # Update the display
        pygame.display.update()

    # Method to display the countdown before game start
    def display_countdown(self):
        # Countdown text render (This cannot be in global variables file because it is not static and text changes)
        countdown_text = HUGE_FONT.render(str(self.countdown), True, BLACK)
        # Draw/render the countdown text in the middle of the screen
        self.screen.blit(countdown_text,
                         (WIDTH / 2 - countdown_text.get_width() / 2, HEIGHT / 2 - countdown_text.get_height() / 2))

        pygame.display.update()  # Update the display
        pygame.time.delay(1000)  # One-second delay between numbers
        self.countdown -= 1  # Decrement countdown number by 1 (this runs until countdown is 0)

    # Method to display pause screen
    def pause_game(self):
        pause_screen = PauseScreen(self.screen)  # New pause screen object

        action = pause_screen.run()  # collect the action returned from the pause screen run method
        # If Resume clicked
        if action == "resume":
            self.game_is_paused = False  # Resume the game
        # If Restart clicked
        elif action == "restart":
            self.__init__(self.screen)  # Restart the game
        # If Quit clicked
        elif action == "quit":
            self.game_in_progress = False  # Quit to menu

    # Method to display game over screen
    def show_game_over(self):
        # Hide all objects by filling the background again
        self.screen.fill(BACKGROUND)

        # Render game over text in the middle of the screen
        self.screen.blit(GAME_OVER_TEXT,
                         (WIDTH / 2 - GAME_OVER_TEXT.get_width() / 2, HEIGHT / 2 - GAME_OVER_TEXT.get_height() / 2))

        pygame.display.update()  # Update the display
        pygame.time.delay(2000)  # Display for 2 seconds
        self.game_in_progress = False  # Quit the game

    # Method to display you win screen
    def show_you_win(self):
        # Hide all objects by filling the background again
        self.screen.fill(BACKGROUND)

        # Render you win text in the middle of the screen
        self.screen.blit(YOU_WIN_TEXT,
                         (WIDTH / 2 - YOU_WIN_TEXT.get_width() / 2, HEIGHT / 2 - YOU_WIN_TEXT.get_height() / 2))

        pygame.display.update()  # Update the display
        pygame.time.delay(2000)  # Display for 2 seconds
        self.game_in_progress = False  # Quit the game
