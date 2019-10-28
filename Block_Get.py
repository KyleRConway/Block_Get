import pygame, sys
from pygame.locals import *

pygame.init() # this always needs to be called after importing pygame.
Display_Window = pygame.display.set_mode((400, 300)) # sets up the main display window for the game.
pygame.display.set_caption('Block Get') # sets up caption on the top-left of the game window

#Setup Colors
green = (0, 128, 0)
blue = (0, 0, 255)
gray =  (128, 128, 128)
yellow = (255, 255, 0)
#Draw game Characters and objects
player = pygame.draw.rect(Display_Window, green, (200, 150, 25, 25))
treasure = pygame.draw.rect(Display_Window, blue, (350, 200, 20, 20))
goal = pygame.draw.rect(Display_Window, yellow, (85, 200, 20, 20))
#Setup character attributes
x = 50
y = 50
vel = 5
#Setup Walls
wall = pygame.draw.rect(Display_Window, gray, (150, 75, 25, 25))
wall_l_long_top = pygame.draw.rect(Display_Window, gray, (0, 0, 400, 25)) # (x, y, length, width)
wall_l_long_bottom = pygame.draw.rect(Display_Window, gray, (0, 275, 400, 25))
wall_l_long_left = pygame.draw.rect(Display_Window, gray, (0, 0, 25, 275))
wall_l_long_right = pygame.draw.rect(Display_Window, gray, (375, 0, 25, 275))



while True: # PRIMARY GAME LOOP. The loop's condition is "True", but the loop will always evaluate to "False" which always keeps the loop repeating. Only a break statement will end the loop.
    #This "Game Loop" 1. Handles Events, 2: Updates the gate state, 3: Draws the game state to the screen.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #Setup keyboard input for movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel
    #Draw 'player' onto the screen.

    #Draw 'background' color.
    #Display_Window.fill((0, 0, 0))
    pygame.display.update() #This allows objects to be drawn onto the screen.
