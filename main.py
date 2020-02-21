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
animalImg = []
animalX = []
animalY = []
animalX_change = []
animalY_change = []
height = 0

for i in range(2):
    url = shuffle()
    animalImg.append(pygame.image.load(url))

    # Position animal randomly at top
    animalX.append(random.randint(100,700))
    animalY.append(height) 
    animalX_change.append(0)  
    animalY_change.append(3)

    height += 200

def player(x,y):
    # blit(image, coordinates) to print player onto game screen  
    screen.blit(playerImg, (x,y))

def animal(x,y,i):
    # blit(image, coordinates) to print animal onto game screen 
    screen.blit(animalImg[i], (x,y))

def isCollision(animalX, animalY, playerX, playerY):
    distance = math.sqrt(math.pow(animalX-playerX, 2) + math.pow(animalY-playerY,2))

# Score 
score_value = 0 
font = pygame.font.Font('freesansbold.ttf',40)
textX= 10
textY= 10

def showScore(x, y):
    score = font.render("SCORE: "+ str(score_value), True, (10,10,10))
    screen.blit(score, (x,y))

# Time 
startTime = time.time() 

def showTime(time):
    minutes = time//60
    seconds = time%60

    if(seconds < 10):
        time = font.render("TIME " + str(minutes) + ":0" + str(seconds), True, (10,10,10))
    else:
        time = font.render("TIME " + str(minutes) + ":" + str(seconds), True, (10,10,10))
    screen.blit(time, (10,50))

# Game Over 
over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    game_over = over_font.render("GAME OVER", True, (10,10,10))
    screen.blit(game_over, (200,380))

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
                playerX_change = -10 

            # Right key pressed 
            if event.key == pygame.K_RIGHT:
                playerX_change = +10
        
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

    for i in range(2):
        # Updating animal direction vertically 
        if animalY[i] <= 536:
            animalY[i] += animalY_change[i]

        # Collision
        collision = isCollision(animalX[i], animalY[i], playerX, playerY)

        if collision:
            score_value +=1

            score_sound = mixer.Sound('assets/PointScore.wav')
            score_sound.play()

            animalX[i] = random.randint(0,736)
            animalY[i] = 30
        
        # TIMER
        if(animalY[i] < 534):
            updated_time = int(time.time() - startTime)

        # GameOver
        if animalY[i] == 534:
            gameover_sound = mixer.Sound('assets/GameOver.flac')
            gameover_sound.play()
            
            
        if animalY[i] >= 534:
            game_over_text()
            for i in range(2):
                    animalY[i] = 2000

        animal(animalX[i],animalY[i], i)

    player(playerX,playerY)
    showScore(textX, textY)
    showTime(updated_time)

    # Continually update game screen 
    pygame.display.update()
