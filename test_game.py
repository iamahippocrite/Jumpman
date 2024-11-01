import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Jump")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rectangle settings
rect_width, rect_height = 50, 50
rect_x = WIDTH // 2
rect_y = HEIGHT - rect_height
rect_y_velocity = 0  # Velocity in Y direction
gravity = 1          # Gravity applied each frame
jump_strength = 15   # Initial jump velocity

# Game loop variables
clock = pygame.time.Clock()
is_jumping = False   # Track if the rectangle is in the air

# Game loop
while True:
    screen.fill(WHITE)  # Fill the screen with white

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                rect_y_velocity = -jump_strength  # Start the jump
                is_jumping = True  # Set jumping to True

    # Apply gravity if jumping
    if is_jumping:
        rect_y_velocity += gravity  # Add gravity to the Y velocity
        rect_y += rect_y_velocity   # Update rectangle position by its velocity

        # Stop jump if it reaches the ground
        if rect_y >= HEIGHT - rect_height:
            rect_y = HEIGHT - rect_height
            rect_y_velocity = 0
            is_jumping = False

    # Draw the rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # 30 frames per second
