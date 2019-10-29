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
class Player:
    def __init__(self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.color = green
        #self.x_speed = 5
        #self.y_speed = 5
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.player_image = player_image
    def draw(self, player_image):
        self.player_image = True
    def move(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
player_image = pygame.draw.rect(Display_Window, green, (150, 150, 25, 25))
#treasure = pygame.draw.rect(Display_Window, blue, (350, 200, 20, 20))
#goal = pygame.draw.rect(Display_Window, yellow, (85, 200, 20, 20))
#Setup Walls
wall = pygame.draw.rect(Display_Window, gray, (150, 75, 25, 25))
wall_l_long_top = pygame.draw.rect(Display_Window, gray, (0, 0, 400, 25)) # (x, y, length, width)
wall_l_long_bottom = pygame.draw.rect(Display_Window, gray, (0, 275, 400, 25))
wall_l_long_left = pygame.draw.rect(Display_Window, gray, (0, 0, 25, 275))
wall_l_long_right = pygame.draw.rect(Display_Window, gray, (375, 0, 25, 275))


#Main Loop
player = Player(150, 150, 25, 25, 5)
while True: # PRIMARY GAME LOOP. The loop's condition is "True", but the loop will always evaluate to "False" which always keeps the loop repeating. Only a break statement will end the loop.
    #This "Game Loop" 1. Handles Events, 2: Updates the gate state, 3: Draws the game state to the screen.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            # Change the keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                player.right = False
                player.left = True
            if event.key == K_RIGHT or event.key == K_d:
                player.left = False
                player.right = True
            if event.key == K_UP or event.key == K_w:
                player.up = True
                player.down = False
            if event.key == K_DOWN or event.key == K_s:
                player.up = False
                player.down = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                player.left = False
            if event.key == K_RIGHT or event.key == K_d:
                player.right = False
            if event.key == K_UP or event.key == K_w:
                player.up = False
            if event.key == K_DOWN or event.key == K_s:
                player.down = False
    #Setup keyboard input for movement

    #Draw 'player' onto the screen.

    #Draw 'background' color.
    #Display_Window.fill((0, 0, 0))
    pygame.display.update() #This allows objects to be drawn onto the screen.
