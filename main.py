import pygame
import random
import math 
import time
from shuffleimages import shuffle
from pygame import mixer 

# Initialize the pygame 
pygame.init()

# Set game screen
screen = pygame.display.set_mode((800,600))

# Background 
background = pygame.image.load('assets/sky.jpg')

# Background sound
mixer.music.load('assets/GameMusicTheme.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Raining Cats and Dogs")

icon = pygame.image.load('assets/rain.png')
pygame.display.set_icon(icon)

# PLAYER 
playerImg = pygame.image.load('assets/basket.png')

# Position basket at bottom centre 
playerX = 350
playerY = 480
playerX_change = 0 

# CAT/DOG
url = shuffle()
animalImg = pygame.image.load(url)

# Position animal randomly at top
animalX = random.randint(0,736)
animalY = 30
animalX_change = 0 
animalY_change = 4

def player(x,y):
    # blit(image, coordinates) to print player onto game screen  
    screen.blit(playerImg, (x,y))

def animal(x,y):
    # blit(image, coordinates) to print animal onto game screen  
    screen.blit(animalImg, (x,y))

def isCollision(animalX, animalY, playerX, playerY):
    distance = math.sqrt(math.pow(animalX-playerX, 2) + math.pow(animalY-playerY,2))
    
    if distance < 60:
        return True
    else:
        return False 

# Score 
score_value = 0 
font = pygame.font.Font('freesansbold.ttf',40)
textX= 10
textY= 10

def showScore(x, y):
    score = font.render("SCORE: "+ str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))

# Time 
startTime = time.time() 

def showTime(time):
    time = font.render("TIME: " + time, True, (0,0,0))
    screen.blit(time, (10,50))

# Game Over 
over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    game_over = over_font.render("GAME OVER", True, (0,0,0))
    screen.blit(game_over, (200,250))

# Game loop (persistence of game screen)
running = True

while running:
    
    # Background (R,G,B)
    screen.fill((26, 152, 201))
    screen.blit(background, (0,0))

    # Defining every possible event occurence in game screen 
    for event in pygame.event.get():

        # Quitting application 
        if event.type == pygame.QUIT:
            running = False 
        
        # Checking keystrokes (pressing down a key)
        if event.type == pygame.KEYDOWN:
            
            # Left key pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -7 

            # Right key pressed 
            if event.key == pygame.K_RIGHT:
                playerX_change = +7
        
        # Checking keystrokes (releasing a key)
        if event.type == pygame.KEYUP:
            
            # Key released 
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0 

    # Adding boundaries 
    if playerX <= 0:
        playerX = 0
    
    if playerX >= 670:
        playerX = 670
    
    # Updating basket position horizontally 
    playerX += playerX_change

    # Updating animal direction vertically 
    if animalY <= 536:
        animalY += animalY_change

    # Collision
    collision = isCollision(animalX, animalY, playerX, playerY)

    if collision:
        score_value +=1

        score_sound = mixer.Sound('assets/PointScore.wav')
        score_sound.play()

        animalX = random.randint(0,736)
        animalY = 30
    
    # TIMER
    updated_time = str(time.time() - startTime)
    updated_time = str(int(time.time() - startTime))

    # GameOver
    if animalY == 534:
        game_over_text()
        gameover_sound = mixer.Sound('assets/GameOver.flac')
        gameover_sound.play()

    player(playerX,playerY)
    animal(animalX,animalY)
    showScore(textX, textY)
    showTime(updated_time)

    # Continually update game screen 
    pygame.display.update()

        


