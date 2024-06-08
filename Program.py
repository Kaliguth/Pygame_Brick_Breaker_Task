# Main file to initiate the game

# pygame imports
import pygame
# UI imports
from ui.Menu import Menu

if __name__ == '__main__':
    pygame.init()  # Initiate pygame
    Menu()  # Run Menu
    pygame.quit()  # Turn off pygame
