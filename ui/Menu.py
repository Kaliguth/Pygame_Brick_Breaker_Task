# Menu class file

# pygame imports
import pygame
from pygame import Surface
# Game class import
from game.Game import Game

# Import required global vars
from util.globals import WIDTH, HEIGHT, BACKGROUND, DARK_RED, LIGHT_RED, TITLE_TEXT, START_TEXT, QUIT_TEXT


class Menu:
    # Constructor
    def __init__(self):
        self.clock = pygame.time.Clock()  # pygame's Clock module for fps management
        self.screen: Surface = pygame.display.set_mode((WIDTH, HEIGHT))  # Set window resolution
        self.game_is_running = True  # Boolean to determine if the game app is running
        self.start_text_visible = True  # Boolean to determine when start text is visible (for blinking)
        self.blink_counter = 0  # Counter to manage start text blinking
        self.quit_button_rect = pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 + 150, 190, 50)  # Quit button rectangle position
        pygame.display.set_caption("Kali Breakout")  # App caption text (displayed in top left of the window)

        self.run()  # run the menu's main method

    # Run method
    # This method runs the main loop and all other methods
    def run(self):
        while self.game_is_running:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            self.handle_events(mouse_pos)
            self.draw_menu(mouse_pos)
            self.start_text_blink()
            self.clock.tick(60)  # Set FPS to 60

    # Method to handle user events
    def handle_events(self, mouse_pos):
        for event in pygame.event.get():
            # Quitting by pressing window's X button
            if event.type == pygame.QUIT:
                self.game_is_running = False
            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quitting by pressing QUIT button
                if self.quit_button_rect.collidepoint(mouse_pos):
                    self.game_is_running = False
            # Key press events
            if event.type == pygame.KEYDOWN:
                # Start a game by pressing ENTER
                if event.key == pygame.K_RETURN:
                    self.start_game()

    # Method to start a new game
    def start_game(self):
        new_game = Game(self.screen)  # New game object
        new_game.run_game()  # Runs the game's run method

    # Method to manage start text blinking
    def start_text_blink(self):
        # Add 1 to the blink counter (counts frames)
        self.blink_counter += 1
        # Blink the start text every 30 frames (around every 1 second)
        if self.blink_counter >= 30:
            # Change start_text_visible to True or False (depending on current status)
            self.start_text_visible = not self.start_text_visible
            self.blink_counter = 0  # Restart blink counter

    # Method to draw/render all menu objects
    def draw_menu(self, mouse_pos):
        # Screen background fill
        self.screen.fill(BACKGROUND)

        # Buttons:
        # Quit button render
        # Check if the mouse is hovering over the quit button
        # Used to change color accordingly when hovering or not
        if self.quit_button_rect.collidepoint(mouse_pos):
            # Mouse hovering over - Dark red color
            pygame.draw.rect(self.screen, DARK_RED, self.quit_button_rect)
        else:
            # Mouse not hovering - Light red color
            pygame.draw.rect(self.screen, LIGHT_RED, self.quit_button_rect)

        # Texts:
        # Render and position the title text
        title_text_pos = (WIDTH / 2 - 190, HEIGHT / 2 - 200)
        self.screen.blit(TITLE_TEXT, title_text_pos)

        # Start text
        # Render and position the start text if start_text_visible is true
        start_text_pos = (WIDTH / 2 - 140, HEIGHT / 2)
        if self.start_text_visible:
            self.screen.blit(START_TEXT, start_text_pos)

        # Render and position the quit text (over the quit button)
        quit_text_pos = (WIDTH / 2 - 35, HEIGHT / 2 + 155)
        self.screen.blit(QUIT_TEXT, quit_text_pos)

        # Update the display
        pygame.display.update()
