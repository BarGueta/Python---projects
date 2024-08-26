import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fidget Spinner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Spinner parameters
spinner_radius = 50
spinner_center = (WIDTH // 2, HEIGHT // 2)
spinner_speed = 0.1

# Button parameters
button_width, button_height = 200, 50
button_color = (100, 100, 100)
button_text_color = (255, 255, 255)
button_font = pygame.font.SysFont(None, 30)
button_text = button_font.render("Start Spinner", True, button_text_color)
button_rect = pygame.Rect((WIDTH - button_width) // 2, HEIGHT - 100, button_width, button_height)

# Main loop
running = True
angle = 0
clock = pygame.time.Clock()
spinner_running = False

while running:
    screen.fill(WHITE)

    # Draw spinner
    pygame.draw.circle(screen, BLACK, spinner_center, spinner_radius)
    spinner_arm_length = 100
    spinner_arm_width = 10
    arm_angle_offset = math.radians(30)
    arm1_angle = angle
    arm2_angle = angle + math.radians(120)
    arm3_angle = angle + math.radians(240)
    arm1_end = (spinner_center[0] + spinner_arm_length * math.cos(arm1_angle),
                spinner_center[1] + spinner_arm_length * math.sin(arm1_angle))
    arm2_end = (spinner_center[0] + spinner_arm_length * math.cos(arm2_angle),
                spinner_center[1] + spinner_arm_length * math.sin(arm2_angle))
    arm3_end = (spinner_center[0] + spinner_arm_length * math.cos(arm3_angle),
                spinner_center[1] + spinner_arm_length * math.sin(arm3_angle))
    pygame.draw.line(screen, RED, spinner_center, arm1_end, spinner_arm_width)
    pygame.draw.line(screen, GREEN, spinner_center, arm2_end, spinner_arm_width)
    pygame.draw.line(screen, BLUE, spinner_center, arm3_end, spinner_arm_width)

    # Draw button
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))

    # Update angle if spinner is running
    if spinner_running:
        angle += spinner_speed

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                spinner_running = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
