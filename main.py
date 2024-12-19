import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

# Background color
background_color = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

#game parameters
game_score = 0
snake_speed = 20
snake_block = 10
direction = 'RIGHT'
fps = pygame.time.Clock()

fruit_position = [random.randrange(0, width // snake_block) * snake_block,
                  random.randrange(1, height // snake_block) * snake_block]
fruit_spawned = False

#kill game when game over occurs
def die():
    my_font = pygame.font.SysFont("saucecodepronerdfont", 50)

    game_over_surface = my_font.render("GAME OVER", True, red)
    
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = [(width/2), (height/2)]

    screen.blit(game_over_surface, game_over_rect)

    pygame.display.flip()

    time.sleep(2)

    pygame.quit()
    quit()

def score(value):
    score_font = pygame.font.SysFont("saucecodepronerdfont", 20)
    
    score_surface = score_font.render(f"Score: {value}", True, red)

    score_rect = score_surface.get_rect()

    screen.blit(score_surface, score_rect)

    pygame.display.flip()

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction = 'RIGHT'
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction = 'LEFT'
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        direction = 'UP'
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        direction = 'DOWN'

    if direction == 'RIGHT':
        snake_position[0] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'UP':
        snake_position[1] -= 10
    else:
        snake_position[1] += 10

    #conditions to end game
    if snake_position[0] < -10 or snake_position[0] > width:
        die()
    if snake_position[1] < -10 or snake_position[1] > height:
        die()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            die()
    
    if not fruit_spawned:
        pygame.draw.rect(screen, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position == fruit_position:
        print("Jackpot")
        fruit_spawned = True

    fruit_spawned = False

    score(game_score)

    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    pygame.display.flip()


    fps.tick(snake_speed)

pygame.quit()

