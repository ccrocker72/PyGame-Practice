import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Title & Icons
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480

playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg,(playerX, playerY))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # RGB - Red, Green, Blue
    screen.fill((0, 128, 128))

    player(playerX, playerY)
    pygame.display.update()







#bibliography
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>