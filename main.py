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

# Enemy 1
enemy1Img = pygame.image.load('enemy1.png')
enemy1X = 50
enemy1Y = 50
enemy1X_change = 0
enemy1Y_change = 0

# Enemy 2
enemy2Img = pygame.image.load('enemy2.png')
enemy2X = 400
enemy2Y = 50
enemy2X_change = 0
enemy2Y_change = 0



def player(x, y):
    screen.blit(playerImg,(playerX, playerY))

def enemy1(x, y):
    screen.blit(enemy1Img,(enemy1X, enemy1Y))

def enemy2(x, y):
    screen.blit(enemy2Img,(enemy2X, enemy2Y))

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((33, 33, 33))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        # If keystroke is pressed, check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >= 775:
        playerX = 775

    player(playerX, playerY)
    
    enemy1(enemy1X, enemy1Y)
    enemy2(enemy2X, enemy2Y)

    pygame.display.update()







#bibliography
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>