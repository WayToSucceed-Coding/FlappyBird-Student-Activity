import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Bird properties
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_size = 20
bird_speed = 0
gravity = 0.5
jump = -10

# Pipe properties
pipe_width = 50
pipe_gap = 150
pipe_speed = 5
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(100, 400)

# Score
score = 0

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock
clock = pygame.time.Clock()

# Main game loop
running = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                bird_speed = jump

    # Bird movement
    bird_speed += gravity
    bird_y += bird_speed

    # Move pipe
    pipe_x -= pipe_speed

    # Respawn pipe and increase score
    if pipe_x < -pipe_width:
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Check for collision
    if bird_y < 0 or bird_y > SCREEN_HEIGHT - bird_size:
        running = False
    if (pipe_x < bird_x < pipe_x + pipe_width or pipe_x < bird_x + bird_size < pipe_x + pipe_width):
        if bird_y < pipe_height or bird_y + bird_size > pipe_height + pipe_gap:
            running = False

    # Fill screen with white background
    screen.fill(WHITE)

    # Draw bird
    pygame.draw.rect(screen, BLACK, [bird_x, bird_y, bird_size, bird_size])

    # Draw pipe
    pygame.draw.rect(screen, GREEN, [pipe_x, 0, pipe_width, pipe_height])
    pygame.draw.rect(screen, GREEN, [pipe_x, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap])

    # Display the score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(30)

# Quit Pygame
pygame.quit()
 