import pygame
import random
import time

pygame.init()

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)

# Display
WIDTH = 800
HEIGHT = 600

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GAME SNAKE BY PYTHON')

# Time
clock = pygame.time.Clock()

# Snake infor
snake_block = 10
snake_speed = 30

# Style
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Main


def Game_score(score):
    value = score_font.render("Your score: " + str(score), True, YELLOW)
    display.blit(value, [0, 0])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [WIDTH/6, HEIGHT/3])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, BLACK, [x[0], x[1], snake_block, snake_block])


def gameLoop():
    game_over = False
    game_close = False

    # Toado
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    FOOD_X = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    FOOD_Y = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(BLUE)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            Game_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            # End
            if event.type == pygame.QUIT:
                game_close = True

            # Controle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.fill(BLUE)

        # Draw
        pygame.draw.rect(display, GREEN, [FOOD_X, FOOD_Y, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)

        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        Game_score(snake_length - 1)

        pygame.display.update()

        if x1 == FOOD_X and y1 == FOOD_Y:
            FOOD_X = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            FOOD_Y = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    # Quit Game
    pygame.quit()
    quit()


gameLoop()
