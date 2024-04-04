import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Move Selection")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load sprite images
move_images = [
    pygame.image.load("left.png"),
    pygame.image.load("right.png"),
    pygame.image.load("up.png"),
    pygame.image.load("down.png"),
    pygame.image.load("jump.png"),
    pygame.image.load("crouch.png")
]

# Define move sprites
moves = ["1-Left", "2-Right", "3-Up", "4-Down", "5-Jump", "6-Crouch"]
move_sprites = []
for i, move in enumerate(moves):
    sprite = pygame.sprite.Sprite()
    sprite.image = move_images[i]
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = i * 100 + 50
    sprite.rect.y = WINDOW_HEIGHT // 2
    move_sprites.append(sprite)

def remove_from_list():
    move_list = moves.copy()
    while move_list:
        selected_move = random.choice(move_list)
        print(f"Selected move: {selected_move}")
        selected_index = moves.index(selected_move)
        selected_sprite = move_sprites[selected_index]

        # Display the selected sprite
        window.fill(WHITE)
        for sprite in move_sprites:
            window.blit(sprite.image, sprite.rect)
        pygame.display.update()
        pygame.time.delay(1000)  # Delay for 1 second

        # Remove the selected move from the list and sprite list
        move_list.remove(selected_move)
        move_sprites.pop(selected_index)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    remove_from_list()

# Quit Pygame
pygame.quit()