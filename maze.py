import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the maze (0 for walls, 1 for paths)
maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

# Define the cell size
CELL_SIZE = 50

# Define the player's starting position
player_x = 1
player_y = 1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and maze[player_y][player_x - 1] == 1:
        player_x -= 1
    if keys[pygame.K_RIGHT] and maze[player_y][player_x + 1] == 1:
        player_x += 1
    if keys[pygame.K_UP] and maze[player_y - 1][player_x] == 1:
        player_y -= 1
    if keys[pygame.K_DOWN] and maze[player_y + 1][player_x] == 1:
        player_y += 1

    # Clear the window
    window.fill(WHITE)

    # Draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if maze[row][col] == 0:
                pygame.draw.rect(window, BLACK, rect)
            else:
                pygame.draw.rect(window, WHITE, rect, 1)

    # Draw the player
    player_rect = pygame.Rect(player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(window, RED, player_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()