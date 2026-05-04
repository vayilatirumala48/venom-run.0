import pygame
import random

pygame.init()

# screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Snake")

# colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

snake_block = 10
clock = pygame.time.Clock()

# snake start
x = width // 2
y = height // 2
dx = 0
dy = 0

snake = [[x, y]]
length = 1

# food
foodx = random.randrange(0, width, snake_block)
foody = random.randrange(0, height, snake_block)

running = True

while running:
    screen.fill(black)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -snake_block, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = snake_block, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -snake_block
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, snake_block

    # move snake
    x += dx
    y += dy

    # wall collision
    if x < 0 or x >= width or y < 0 or y >= height:
        running = False

    snake.append([x, y])
    if len(snake) > length:
        snake.pop(0)

    # self collision
    if [x, y] in snake[:-1]:
        running = False

    # draw snake
    for part in snake:
        pygame.draw.rect(screen, green, (*part, snake_block, snake_block))

    # draw food
    pygame.draw.rect(screen, red, (foodx, foody, snake_block, snake_block))

    # eat food
    if x == foodx and y == foody:
        length += 1
        foodx = random.randrange(0, width, snake_block)
        foody = random.randrange(0, height, snake_block)

    pygame.display.update()
    clock.tick(10)

pygame.quit()