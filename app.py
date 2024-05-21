import pygame
import random
import math

# Initializing pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption (title)
pygame.display.set_caption("Particle Simulation")

# Clock for controlling the FPS
clock = pygame.time.Clock()
