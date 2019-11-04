import pygame, sys
from pygame.locals import *

pygame.init() # this always needs to be called after importing pygame.
Display_Window = pygame.display.set_mode((400, 300)) # sets up the main display window for the game.
pygame.display.set_caption('Block Get') # sets up caption on the top-left of the game window
#Setup clock/FPS
clock = pygame.time.Clock()
#Setup Sprite Images
player_sprite = [pygame.image.load('player.xcf')]
#Draw game Characters and objects
#x = 50
#y = 50
#width = 25
#height = 25
#speed = 3
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 3
    def draw(self, Display_Window):
        self.rect = pygame.draw.rect(Display_Window, (green), (x, y, width, height))
def redrawGameWindow():
    (Display_Window.fill((black)))
    player.draw(Display_Window)

    pygame.display.update()
#treasure = pygame.draw.rect(Display_Window, blue, (350, 200, 20, 20))
#goal = pygame.draw.rect(Display_Window, yellow, (85, 200, 20, 20))
#Setup Walls
#wall = pygame.draw.rect(Display_Window, gray, (150, 75, 25, 25))
#wall_l_long_top = pygame.draw.rect(Display_Window, gray, (0, 0, 400, 25)) # (x, y, length, width)
#wall_l_long_bottom = pygame.draw.rect(Display_Window, gray, (0, 275, 400, 25))
#wall_l_long_left = pygame.draw.rect(Display_Window, gray, (0, 0, 25, 275))
#wall_l_long_right = pygame.draw.rect(Display_Window, gray, (375, 0, 25, 275))


#Main Loop
player = Player(50, 50, 25, 25)
while True: # PRIMARY GAME LOOP. The loop's condition is "True", but the loop will always evaluate to "False" which always keeps the loop repeating. Only a break statement will end the loop.
    #This "Game Loop" 1. Handles Events, 2: Updates the gate state, 3: Draws the game state to the screen.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Change the keyboard variables/get input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > player.speed: #Making sure the top left of 'player' is greater than our 'speed', so we can never move off the screen.
        player.x -= player.speed
    if keys[pygame.K_RIGHT] and player.x < 400 - player.speed - player.width: #Making sure the top right corner of 'player' is less than screen width and its width.
        player.x += player.speed
    if keys[pygame.K_UP] and y > speed: # Same principles apply for the y coordinate
        player.y -= player.speed
    if keys[pygame.K_DOWN] and player.y < 300 - player.height - player.speed:
        player.y += player.speed
    if keys[pygame.K_a] and player.x > player.speed: #Making sure the top left of 'player' is greater than our 'speed', so we can never move off the screen.
        player.x -= player.speed
    if keys[pygame.K_d] and player.x < 400 - player.speed - player.width: #Making sure the top right corner of 'player' is less than screen width and its width.
        player.x += player.speed
    if keys[pygame.K_w] and player.y > player.speed: # Same principles apply for the y coordinate
        player.y -= player.speed
    if keys[pygame.K_s] and player.y < 300 - player.height - player.speed:
        player.y += player.speed
    #Draw 'background' color.

    #Draw 'player' onto the screen.

    pygame.display.update() #This allows objects to be drawn onto the screen.

    clock.tick(30) #Frames Per Second
pygame.quit()