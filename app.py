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



# Particle class
class Particle:
		def __init__(self, x, y, radius, color, speed, angle) -> None:
				self.x = x
				self.y = y
				self.radius = radius
				self.color = color
				self.speed = speed
				self.angle = angle
		
		def move(self):
			self.x += self.speed * math.cos(self.angle)
			self.y += self.speed * math.sin(self.angle)

			# Collision with walls
			if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
				self.angle = math.pi - self.angle
			if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:
				self.angle = -self.angle
		

		def draw(self, screen):
			pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)



# Make some particles, and asign them random properties
particles = []

for _ in range(10):
	x = random.randint(50, SCREEN_WIDTH - 50)
	y = random.randint(50, SCREEN_HEIGHT - 50)

	radius = random.randint(10, 20)
	color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	speed = random.uniform(1, 3)
	angle = random.uniform(0, 2 * math.pi)

	particles.append(Particle(x, y, radius, color, speed, angle))



# Game loop
running = True

while running:
		# Check if the player wants to close the window
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
						running = False
		
		# Clear screen
		screen.fill((0, 0, 0))

		# Draw the particles
		for particle in particles:
			particle.move()
			particle.draw(screen)

		# Update the screen
		pygame.display.flip()

		# Cap the FPS to 60
		clock.tick(60)

pygame.quit()