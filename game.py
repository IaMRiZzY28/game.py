import pygame
import random


pygame.init()


width, height = 600, 400
screen = pygame.display.set_mode((width, height))
player_x, player_y, player_speed = width // 2, height - 50, 5
player_width, block_width, block_height = 50, 50, 50


WHITE, RED = (255, 255, 255), (255, 0, 0)


blocks = []
running = True
while running:
    screen.fill(WHITE)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed
    
   
    if random.randint(1, 20) == 1:
        blocks.append([random.randint(0, width - block_width), 0])
    for block in blocks[:]:
        block[1] += 5
        pygame.draw.rect(screen, RED, (*block, block_width, block_height))
        if block[1] > height:
            blocks.remove(block)
     Draw player
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, player_width, 50))
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
