# Pause screen class

# pygame imports
import pygame
from pygame import Surface

# Import required global vars
from util.globals import WIDTH, HEIGHT, DARK_RED, LIGHT_RED, PAUSE_TEXT, QUIT_TEXT, RESTART_TEXT, RESUME_TEXT


class PauseScreen:
    # Constructor
    def __init__(self, screen):
        self.screen: Surface = screen  # Set the screen's resolution to be the same as game's
        self.clock = pygame.time.Clock()  # pygame's Clock module for fps management
        self.game_is_paused = True  # Boolean to determine if the game is paused
        self.resume_text = RESUME_TEXT  # Resume text
        self.restart_text = RESTART_TEXT  # Restart text
        self.quit_text = QUIT_TEXT  # Quit text
        self.resume_button_rect = pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 - 50, 190, 50)  # Resume button
        self.restart_button_rect = pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 + 25, 190, 50)  # Restart button
        self.quit_button_rect = pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 + 100, 190, 50)  # Quit button

    # Run method
    # This method runs the main loop and all other methods
    def run(self):
        while self.game_is_paused:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            action = self.handle_events(mouse_pos)  # Get action string returned from handle_events
            if action:
                return action  # Return the action
            self.draw(mouse_pos)
            self.clock.tick(60)  # Set FPS to 60

    # Method to handle user events
    def handle_events(self, mouse_pos):
        for event in pygame.event.get():
            # Quitting by pressing X button
            if event.type == pygame.QUIT:
                self.game_is_paused = False
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Resume button clicked
                if self.resume_button_rect.collidepoint(mouse_pos):
                    self.game_is_paused = False  # Disable pause
                    return "resume"  # Return "resume" to resume the game
                # Quit button clicked
                if self.quit_button_rect.collidepoint(mouse_pos):
                    self.game_is_paused = False  # Disable pause
                    return "quit"  # Return "quit" to quit the game
                # Restart button clicked
                if self.restart_button_rect.collidepoint(mouse_pos):
                    self.game_is_paused = False  # Disable pause
                    return "restart"  # Return "restart" to restart the game
            if event.type == pygame.KEYDOWN:
                # ESC key pressed again
                if event.key == pygame.K_ESCAPE:
                    self.game_is_paused = False  # Disable pause
                    return "resume"  # Return "resume" to resume the game

    # Method to draw/render all pause screen objects
    def draw(self, mouse_pos):
        # Buttons:
        # All buttons change color when hovered over

        # Resume button
        if self.resume_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, DARK_RED, self.resume_button_rect)
        else:
            pygame.draw.rect(self.screen, LIGHT_RED, self.resume_button_rect)
        # Resume text
        self.screen.blit(self.resume_text, (WIDTH / 2 - 85, HEIGHT / 2 - 44))

        # Restart button
        if self.restart_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, DARK_RED, self.restart_button_rect)
        else:
            pygame.draw.rect(self.screen, LIGHT_RED, self.restart_button_rect)
        # Restart text
        self.screen.blit(self.restart_text, (WIDTH / 2 - 85, HEIGHT / 2 + 31))

        # Quit button
        if self.quit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, DARK_RED, self.quit_button_rect)
        else:
            pygame.draw.rect(self.screen, LIGHT_RED, self.quit_button_rect)
        # Quit text
        self.screen.blit(self.quit_text, (WIDTH / 2 - 85, HEIGHT / 2 + 106))

        # Render and position the "GAME PAUSED" text over all buttons
        paused_text = PAUSE_TEXT
        paused_text_pos = (WIDTH / 2 - paused_text.get_width() / 2, HEIGHT / 2 - 150)
        self.screen.blit(paused_text, paused_text_pos)

        pygame.display.update()  # Update the display
