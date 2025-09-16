import pygame
import sys
import random

pygame.init()

# Window size
WIN_WIDTH, WIN_HEIGHT = 800, 600
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Snake Game - Choose Difficulty & Replay")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

block_size = 20
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

def random_food():
    return [
        random.randrange(0, WIN_WIDTH // block_size) * block_size,
        random.randrange(0, WIN_HEIGHT // block_size) * block_size
    ]

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(win, GREEN, (x, y, block_size, block_size))

def draw_food(food_pos):
    pygame.draw.rect(win, RED, (food_pos[0], food_pos[1], block_size, block_size))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))

def show_level(level):
    level_text = font.render(f"Level: {level}", True, WHITE)
    win.blit(level_text, (WIN_WIDTH - 150, 10))

def menu():
    while True:
        win.fill(BLACK)
        title = big_font.render("Snake Game", True, YELLOW)
        win.blit(title, (WIN_WIDTH//2 - title.get_width()//2, 60))

        msg = font.render("Choose Difficulty:", True, WHITE)
        win.blit(msg, (WIN_WIDTH//2 - msg.get_width()//2, 200))

        easy_text = font.render("1. Easy", True, GREEN)
        win.blit(easy_text, (WIN_WIDTH//2 - easy_text.get_width()//2, 260))
        medium_text = font.render("2. Medium", True, YELLOW)
        win.blit(medium_text, (WIN_WIDTH//2 - medium_text.get_width()//2, 320))
        hard_text = font.render("3. Hard", True, RED)
        win.blit(hard_text, (WIN_WIDTH//2 - hard_text.get_width()//2, 380))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 10, "Easy"
                if event.key == pygame.K_2:
                    return 18, "Medium"
                if event.key == pygame.K_3:
                    return 25, "Hard"

def ask_replay(score):
    while True:
        win.fill(BLACK)
        go_text = big_font.render("Game Over!", True, RED)
        win.blit(go_text, (WIN_WIDTH // 2 - go_text.get_width() // 2, 120))
        score_text = font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (WIN_WIDTH // 2 - score_text.get_width() // 2, 220))
        replay_text = font.render("Play Again? Y/N", True, YELLOW)
        win.blit(replay_text, (WIN_WIDTH // 2 - replay_text.get_width() // 2, 320))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

def game_loop(speed, level_name):
    x, y = WIN_WIDTH // 2, WIN_HEIGHT // 2
    dx, dy = block_size, 0  # <--- Start moving right by default!
    snake_list = []
    snake_length = 1
    food_pos = random_food()
    score = 0
    level = level_name

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -block_size, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = block_size, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -block_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, block_size

        x += dx
        y += dy

        # Check for collision with boundaries
        if x < 0 or x >= WIN_WIDTH or y < 0 or y >= WIN_HEIGHT:
            break

        # Check for collision with itself
        snake_head = [x, y]
        if snake_head in snake_list:
            break

        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for eating food
        if x == food_pos[0] and y == food_pos[1]:
            food_pos = random_food()
            snake_length += 1
            score += 1

        # Drawing
        win.fill(BLACK)
        draw_snake(snake_list)
        draw_food(food_pos)
        show_score(score)
        show_level(level)
        pygame.display.update()
        clock.tick(speed)

    return score

def main():
    while True:
        speed, level_name = menu()
        score = game_loop(speed, level_name)
        replay = ask_replay(score)
        if not replay:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()