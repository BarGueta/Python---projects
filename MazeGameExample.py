from tkinter import messagebox
import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 40
MAZE_WIDTH = 15  # Adjusted maze width
MAZE_HEIGHT = 10  # Adjusted maze height
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the maze structure with a bigger matrix
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Adjusted player and goal positions
player_pos = (1, 1)
goal_pos = (MAZE_WIDTH - 2, MAZE_HEIGHT - 2)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

# Function to draw the maze
def draw_maze():
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to draw the player and goal
def draw_entities():
    pygame.draw.rect(screen, (0, 255, 0), (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (goal_pos[0] * CELL_SIZE, goal_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to handle player movement
def move_player(dx, dy):
    global player_pos
    new_pos = (player_pos[0] + dx, player_pos[1] + dy)
    if 0 <= new_pos[0] < MAZE_WIDTH and 0 <= new_pos[1] < MAZE_HEIGHT:
        if maze[new_pos[1]][new_pos[0]] == 0:
            player_pos = new_pos

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)
            elif event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)

    # Check for win condition
    if player_pos == goal_pos:
        print("You win!")
        messagebox.showinfo("Congratulations!", "You win!")
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    draw_maze()
    draw_entities()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
