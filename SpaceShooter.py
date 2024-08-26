import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player
player_image = pygame.image.load("ship.png")
player_width = 64
player_height = 64
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 45
player_speed = 5

# Enemy
enemy_image = pygame.image.load("enemyspaceship.png")
enemy_width = 64
enemy_height = 64
enemy_speed = 3
enemies = []

# Bullets
bullet_image = pygame.image.load("bullet.png")
bullet_width = 60
bullet_height = 60
bullet_speed = 8
bullets = []

# Shooting cooldown
shoot_cooldown = 0
shoot_delay = 10  # Adjust the delay as needed (in frames)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game states
GAME_RUNNING = 0
GAME_START = 1
GAME_OVER = 2
game_state = GAME_START

# Buttons
start_button_rect = pygame.Rect(300, 300, 200, 50)
restart_button_rect = pygame.Rect(300, 300, 200, 50)

# Game loop
running = True
clock = pygame.time.Clock()

def spawn_enemy():
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(-screen_height, 0)
    enemies.append([enemy_x, enemy_y])

def draw_player(x, y):
    screen.blit(player_image, (x, y))

def draw_enemy(x, y):
    screen.blit(enemy_image, (x, y))

def draw_bullet(x, y):
    screen.blit(bullet_image, (x, y))

def is_collision(obj1_x, obj1_y, obj2_x, obj2_y, obj1_width, obj1_height, obj2_width, obj2_height):
    obj1_rect = pygame.Rect(obj1_x, obj1_y, obj1_width + 35, obj1_height)
    obj2_rect = pygame.Rect(obj2_x, obj2_y, obj2_width + 35, obj2_height)
    return obj1_rect.colliderect(obj2_rect)

def draw_start_button():
    pygame.draw.rect(screen, WHITE, start_button_rect)
    start_text = font.render("Start", True, BLACK)
    screen.blit(start_text, (start_button_rect.x + 70, start_button_rect.y + 15))

def draw_restart_button():
    pygame.draw.rect(screen, WHITE, restart_button_rect)
    restart_text = font.render("Restart", True, BLACK)
    screen.blit(restart_text, (restart_button_rect.x + 57, restart_button_rect.y + 15))

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == GAME_START and start_button_rect.collidepoint(event.pos):
                game_state = GAME_RUNNING
            elif game_state == GAME_OVER and restart_button_rect.collidepoint(event.pos):
                # Reset game state
                game_state = GAME_RUNNING
                score = 0
                enemies.clear()
                bullets.clear()
                player_x = (screen_width - player_width) // 2
                player_y = screen_height - player_height - 45

    if game_state == GAME_START:
        draw_start_button()

    elif game_state == GAME_RUNNING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > player_speed:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width - player_speed:
            player_x += player_speed

        # Player shooting
        if keys[pygame.K_SPACE] and shoot_cooldown <= 0:
            bullet_x = player_x + (player_width - bullet_width) // 2
            bullet_y = player_y
            bullets.append([bullet_x, bullet_y])
            shoot_cooldown = shoot_delay  # Set cooldown

        # Decrease shoot cooldown
        if shoot_cooldown > 0:
            shoot_cooldown -= 1

        # Spawn enemies
        if len(enemies) < 5:  # Adjust enemy count as needed
            spawn_enemy()

        # Move and draw enemies
        for enemy in enemies:
            enemy[1] += enemy_speed
            draw_enemy(enemy[0], enemy[1])

            if enemy[1] > screen_height:
                enemies.remove(enemy)

            # Check player-enemy collision
            if is_collision(enemy[0], enemy[1], player_x, player_y, enemy_width, enemy_height, player_width, player_height):
                # Game over logic
                game_state = GAME_OVER

            for bullet in bullets:
                bullet[1] -= bullet_speed
                draw_bullet(bullet[0], bullet[1])

                # Check bullet-enemy collision
                if is_collision(bullet[0], bullet[1], enemy[0], enemy[1], bullet_width, bullet_height, enemy_width, enemy_height):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1

        # Move and draw player
        draw_player(player_x, player_y)

        # Draw score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

    elif game_state == GAME_OVER:
        draw_restart_button()

    pygame.display.update()
    clock.tick(60)  # Adjust FPS as needed

pygame.quit()

#------------------------------------------------------------------------------
# import pygame
# import random
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the screen
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Space Shooter")
#
# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
#
# # Player
# player_image = pygame.image.load("ship.png")
# player_width = 64
# player_height = 64
# player_x = (screen_width - player_width) // 2
# player_y = screen_height - player_height - 45
# player_speed = 5
#
# # Enemy
# enemy_image = pygame.image.load("enemyspaceship.png")
# enemy_width = 64
# enemy_height = 64
# enemy_speed = 3
# enemies = []
#
# # Bullets
# bullet_image = pygame.image.load("bullet.png")
# bullet_width = 60
# bullet_height = 60
# bullet_speed = 8
# bullets = []
#
# # Shooting cooldown
# shoot_cooldown = 0
# shoot_delay = 10  # Adjust the delay as needed (in frames)
#
# # Score
# score = 0
# font = pygame.font.Font(None, 36)
#
# # Game loop
# running = True
# clock = pygame.time.Clock()
#
# def spawn_enemy():
#     enemy_x = random.randint(0, screen_width - enemy_width)
#     enemy_y = random.randint(-screen_height, 0)
#     enemies.append([enemy_x, enemy_y])
#
# def draw_player(x, y):
#     screen.blit(player_image, (x, y))
#
# def draw_enemy(x, y):
#     screen.blit(enemy_image, (x, y))
#
# def draw_bullet(x, y):
#     screen.blit(bullet_image, (x, y))
#
# def is_collision(obj1_x, obj1_y, obj2_x, obj2_y, obj1_width, obj1_height, obj2_width, obj2_height):
#     obj1_rect = pygame.Rect(obj1_x, obj1_y, obj1_width + 35, obj1_height)
#     obj2_rect = pygame.Rect(obj2_x, obj2_y, obj2_width + 35, obj2_height)
#     return obj1_rect.colliderect(obj2_rect)
#
# while running:
#     screen.fill(BLACK)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_x > player_speed:
#         player_x -= player_speed
#     if keys[pygame.K_RIGHT] and player_x < screen_width - player_width - player_speed:
#         player_x += player_speed
#
#     # Player shooting
#     if keys[pygame.K_SPACE] and shoot_cooldown <= 0:
#         bullet_x = player_x + (player_width - bullet_width) // 2
#         bullet_y = player_y
#         bullets.append([bullet_x, bullet_y])
#         shoot_cooldown = shoot_delay  # Set cooldown
#
#     # Decrease shoot cooldown
#     if shoot_cooldown > 0:
#         shoot_cooldown -= 1
#
#     # Spawn enemies
#     if len(enemies) < 5:  # Adjust enemy count as needed
#         spawn_enemy()
#
#     # Move and draw enemies
#     for enemy in enemies:
#         enemy[1] += enemy_speed
#         draw_enemy(enemy[0], enemy[1])
#
#         if enemy[1] > screen_height:
#             enemies.remove(enemy)
#
#         # Check player-enemy collision
#         if is_collision(enemy[0], enemy[1], player_x, player_y, enemy_width, enemy_height, player_width, player_height):
#             # Game over logic
#             running = False
#
#         for bullet in bullets:
#             bullet[1] -= bullet_speed
#             draw_bullet(bullet[0], bullet[1])
#
#             # Check bullet-enemy collision
#             if is_collision(bullet[0], bullet[1], enemy[0], enemy[1], bullet_width, bullet_height, enemy_width, enemy_height):
#                 bullets.remove(bullet)
#                 enemies.remove(enemy)
#                 score += 1
#
#     # Move and draw player
#     draw_player(player_x, player_y)
#
#     # Draw score
#     score_text = font.render("Score: " + str(score), True, WHITE)
#     screen.blit(score_text, (10, 10))
#
#     pygame.display.update()
#     clock.tick(60)  # Adjust FPS as needed
#
# pygame.quit()