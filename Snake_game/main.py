import pygame
from sys import exit
import random

rows = 25
columns = rows
tile_size = 25

game_width = tile_size * columns
game_height = tile_size * rows

pygame.init()
window = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


def get_random(limit):
    return random.randint(0, limit - 1) * tile_size

# Food
food = pygame.Rect(get_random(columns),get_random(rows),tile_size,tile_size)

# Snake
snake = []
snake.append(pygame.Rect(get_random(columns),get_random(rows),tile_size,tile_size))
snake_velocity = (0, 0)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game Loop
while True:
    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                snake_velocity = (0, -tile_size)

            elif event.key in (pygame.K_DOWN, pygame.K_s):
                snake_velocity = (0, tile_size)

            elif event.key in (pygame.K_LEFT, pygame.K_a):
                snake_velocity = (-tile_size, 0)

            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                snake_velocity = (tile_size, 0)

    # Move Snake
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1].copy()
    snake[0].move_ip(snake_velocity)


    # Snake eats food
    if snake[0].center == food.center:
        score += 1
        snake.append(food)
        food = pygame.Rect(get_random(columns),get_random(rows),tile_size,tile_size)

    # Snake hits wall
    if not window.get_rect().contains(snake[0]):
        score = 0
        snake.clear()
        snake.append(pygame.Rect(get_random(columns),get_random(rows),tile_size,tile_size))
        food = pygame.Rect(get_random(columns),get_random(rows),tile_size,tile_size)


    # Draw
    window.fill("black")
    # Draw Food
    pygame.draw.rect(window, "yellow", food)

    # Draw Snake
    for snake_part in snake:
        pygame.draw.rect(window, "cyan", snake_part)

    # Draw Score
    score_text = font.render(f"Score: {score}", True,"white")
    window.blit(score_text, (10, 10))

    # Update Screen
    pygame.display.update()

    # Game Speed
    clock.tick(10)