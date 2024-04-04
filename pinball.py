import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pinball Pachinko")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the ball
BALL_RADIUS = 10
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT - BALL_RADIUS - 20
ball_speed_x = random.randint(-5, 5)
ball_speed_y = -10

# Define the pins (obstacles)
pins = []
for i in range(20):
    pin_x = random.randint(20, WINDOW_WIDTH - 20)
    pin_y = random.randint(20, WINDOW_HEIGHT // 2)
    pins.append((pin_x, pin_y))

# Define the flippers
flipper_left_x = 20
flipper_left_y = WINDOW_HEIGHT - 50
flipper_right_x = WINDOW_WIDTH - 20
flipper_right_y = WINDOW_HEIGHT - 50

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > WINDOW_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - BALL_RADIUS < 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with pins
    for pin_x, pin_y in pins:
        distance = ((ball_x - pin_x) ** 2 + (ball_y - pin_y) ** 2) ** 0.5
        if distance < BALL_RADIUS + 10:
            ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_y

    # Clear the window
    window.fill(WHITE)

    # Draw the pins
    for pin_x, pin_y in pins:
        pygame.draw.circle(window, BLACK, (pin_x, pin_y), 10)

    # Draw the flippers
    pygame.draw.rect(window, BLACK, (flipper_left_x, flipper_left_y, 20, 10))
    pygame.draw.rect(window, BLACK, (flipper_right_x, flipper_right_y, 20, 10))

    # Draw the ball
    pygame.draw.circle(window, RED, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()