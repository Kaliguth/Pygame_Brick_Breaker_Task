# Global variables file

# Import pygame's font module
import pygame.font

# Screen resolution
WIDTH, HEIGHT = 1280, 720

# Colors
BACKGROUND = 150, 200, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0
LIGHT_RED = 160, 40, 40
DARK_RED = 80, 30, 30

# Brick parameters
BRICK_WIDTH = 182
BRICK_HEIGHT = 50
BRICK_ROWS = 4
BRICK_SPACING_X = 2
BRICK_SPACING_Y = 2

# Fonts
pygame.font.init()  # Initiate pygame font module
TITLE_FONT = pygame.font.SysFont("Comic Sans", 60, bold=True)
SMALL_FONT = pygame.font.SysFont("Arial", 35, bold=True)
HUGE_FONT = pygame.font.SysFont("Comic Sans", 120, bold=True)

# Rendering different texts
TITLE_TEXT = TITLE_FONT.render("Kali Breakout", True, LIGHT_RED)
START_TEXT = SMALL_FONT.render("Press ENTER to start", True, BLACK)
QUIT_TEXT = SMALL_FONT.render("QUIT", True, WHITE)
PAUSE_TEXT = TITLE_FONT.render("GAME PAUSED", True, BLACK)
RESUME_TEXT = SMALL_FONT.render("RESUME", True, WHITE)
RESTART_TEXT = SMALL_FONT.render("RESTART", True, WHITE)
GAME_OVER_TEXT = HUGE_FONT.render("GAME OVER", True, LIGHT_RED)
YOU_WIN_TEXT = HUGE_FONT.render("YOU WIN!", True, LIGHT_RED)
