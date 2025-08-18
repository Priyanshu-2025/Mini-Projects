import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
BG_COLOR = (35, 40, 50)
PADDLE_COLOR = (72, 224, 228)
BALL_COLOR = (255, 215, 0)
NET_COLOR = (126, 230, 248)
TEXT_COLOR = (255, 255, 255)
AI_COLOR = (255, 165, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 16, 100
PADDLE_MARGIN = 24
PADDLE_SPEED = 7

# Ball settings
BALL_SIZE = 18
BALL_SPEED = 7

# Scores
MAX_SCORE = 10
FONT = pygame.font.SysFont("Segoe UI", 36)
BIG_FONT = pygame.font.SysFont("Segoe UI", 48)

clock = pygame.time.Clock()

def draw_net():
    for y in range(0, HEIGHT, 32):
        pygame.draw.rect(WIN, NET_COLOR, (WIDTH // 2 - 2, y, 4, 18))

def draw(paddle_left, paddle_right, ball, scores, game_over=False, winner=None):
    WIN.fill(BG_COLOR)
    draw_net()
    # Paddles
    pygame.draw.rect(WIN, PADDLE_COLOR, paddle_left)
    pygame.draw.rect(WIN, AI_COLOR, paddle_right)
    # Ball
    pygame.draw.ellipse(WIN, BALL_COLOR, ball)
    # Scoreboard
    left_score, right_score = scores
    score_text = FONT.render(f"{left_score}    :    {right_score}", True, TEXT_COLOR)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 24))
    label_left = FONT.render("You", True, PADDLE_COLOR)
    label_ai = FONT.render("AI", True, AI_COLOR)
    WIN.blit(label_left, (WIDTH // 2 - 120, 65))
    WIN.blit(label_ai, (WIDTH // 2 + 70, 65))
    # Footer
    footer = pygame.font.SysFont("Segoe UI", 20).render(
        "Move your mouse up or down to control your paddle.", True, NET_COLOR)
    WIN.blit(footer, (WIDTH // 2 - footer.get_width() // 2, HEIGHT - 36))
    # Game Over
    if game_over:
        over_text = BIG_FONT.render(winner + " wins!", True, BALL_COLOR)
        WIN.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 40))
        info_text = FONT.render("Press SPACE to restart", True, TEXT_COLOR)
        WIN.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT // 2 + 20))
    pygame.display.flip()

def main():
    # Paddles
    paddle_left = pygame.Rect(PADDLE_MARGIN, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_right = pygame.Rect(WIDTH - PADDLE_MARGIN - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    # Ball
    ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
    ball_dx = BALL_SPEED * random.choice((1, -1))
    ball_dy = BALL_SPEED * random.choice((1, -1))

    player_score = 0
    ai_score = 0
    running = True
    game_over = False
    winner = None

    while running:
        clock.tick(60)
        mouse_y = pygame.mouse.get_pos()[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return main()  # Restart

        if not game_over:
            # Player paddle follows mouse, clamped to screen
            paddle_left.y = mouse_y - PADDLE_HEIGHT // 2
            paddle_left.y = max(0, min(HEIGHT - PADDLE_HEIGHT, paddle_left.y))

            # AI paddle follows the ball with some delay
            if paddle_right.centery < ball.centery - 12:
                paddle_right.y += PADDLE_SPEED * 0.9
            elif paddle_right.centery > ball.centery + 12:
                paddle_right.y -= PADDLE_SPEED * 0.9
            paddle_right.y = max(0, min(HEIGHT - PADDLE_HEIGHT, paddle_right.y))

            # Ball movement
            ball.x += ball_dx
            ball.y += ball_dy

            # Ball collision with top and bottom
            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_dy = -ball_dy

            # Ball collision with paddles
            if ball.colliderect(paddle_left):
                ball.left = paddle_left.right
                ball_dx = abs(ball_dx)
                # Add spin
                offset = (ball.centery - paddle_left.centery) * 0.2
                ball_dy = offset

            if ball.colliderect(paddle_right):
                ball.right = paddle_right.left
                ball_dx = -abs(ball_dx)
                offset = (ball.centery - paddle_right.centery) * 0.2
                ball_dy = offset

            # Score update
            if ball.left <= 0:
                ai_score += 1
                if ai_score == MAX_SCORE:
                    game_over = True
                    winner = "AI"
                ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
                ball_dx = BALL_SPEED * random.choice((1, -1))
                ball_dy = BALL_SPEED * random.choice((1, -1))

            if ball.right >= WIDTH:
                player_score += 1
                if player_score == MAX_SCORE:
                    game_over = True
                    winner = "You"
                ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
                ball_dx = BALL_SPEED * random.choice((1, -1))
                ball_dy = BALL_SPEED * random.choice((1, -1))

        draw(paddle_left, paddle_right, ball, (player_score, ai_score), game_over, winner)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()