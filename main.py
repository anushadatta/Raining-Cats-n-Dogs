import pygame

# Initialize the pygame 
pygame.init()

# Set game screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Raining Cats and Dogs")

icon = pygame.image.load('rain.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('basket.png')

# Position basket at bottom centre 
playerX = 350
playerY = 480
playerX_change = 0 

def player(x,y):
    
    # blit(image, coordinates) to print player onto game screen  
    screen.blit(playerImg, (x,y))

# Game loop (persistence of game screen)
running = True

while running:
    
    # Background (R,G,B)
    screen.fill((26, 152, 201))

    # Defining every possible event occurence in game screen 
    for event in pygame.event.get():

        # Quitting application 
        if event.type == pygame.QUIT:
            running = False 
        
        # Checking keystrokes (pressing down a key)
        if event.type == pygame.KEYDOWN:
            
            # Left key pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3 

            # Right key pressed 
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.3
        
        # Checking keystrokes (releasing a key)
        if event.type == pygame.KEYUP:
            
            # Key released 
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0 

    # Updating basket position horizontally 
    playerX += playerX_change
    player(playerX,playerY)

    # Continually update game screen 
    pygame.display.update()

        


