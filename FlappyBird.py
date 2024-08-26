import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 415, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load background image and resize it to match the screen size
background_image = pygame.image.load("AnimatedBeach.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Bird parameters
bird_width = 40
bird_height = 30
bird_x = 100
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5

# Pipe parameters
pipe_width = 70
pipe_gap = 200  # Increased gap between pipes
pipe_velocity = 3
pipes = []

# Fonts
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.rect(screen, (255, 255, 0), (x, y, bird_width, bird_height))

def draw_pipe(x, y, height):
    pygame.draw.rect(screen, (0, 128, 0), (x, 0, pipe_width, y))
    pygame.draw.rect(screen, (0, 128, 0), (x, y + height, pipe_width, HEIGHT - y - height))

def display_score(score):
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

def main():
    bird_y = HEIGHT // 2
    bird_velocity = 0
    pipes.clear()
    score = 0

    running = True
    while running:
        screen.blit(background_image, (0, 0))  # Draw background image

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -8

        # Bird movement
        bird_y += bird_velocity
        bird_velocity += gravity
        draw_bird(bird_x, bird_y)

        # Pipe movement and collision detection
        if len(pipes) == 0 or pipes[-1][0] < WIDTH - 200:
            pipe_height = random.randint(50, HEIGHT - pipe_gap - 50)
            pipes.append([WIDTH, pipe_height])

        for pipe in pipes:
            draw_pipe(pipe[0], pipe[1], pipe_gap)
            pipe[0] -= pipe_velocity

            if pipe[0] == bird_x:
                score += 1

            if bird_x < pipe[0] + pipe_width and bird_x + bird_width > pipe[0]:
                if bird_y < pipe[1] or bird_y + bird_height > pipe[1] + pipe_gap:
                    game_over()

            if pipe[0] + pipe_width == bird_x:
                score += 1

            if pipe[0] + pipe_width < 0:
                pipes.remove(pipe)

        display_score(score)

        # Check if bird is out of bounds
        if bird_y < 0 or bird_y + bird_height > HEIGHT:
            game_over()

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
