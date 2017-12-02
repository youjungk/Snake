import pygame, random, os
from random import randint
# initializing
pygame.init()

# colors (R/G/B)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

BACKGROND_IMAGE = pygame.image.load('background.jpg')
FOOD_IMAGE = pygame.image.load('food.png')
FOOD_IMAGE = pygame.transform.scale(FOOD_IMAGE, (10, 10))
# Base Window
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')
pygame.display.update()

#loop variables
gameExit = False
gameScore = 0
lead_x = 300
lead_y = 300
food_x = randint(1, 65)*10
food_y = randint(1, 50)*10
lead_x_change = 0
lead_y_change = 0

game_frequency = 15

body_length = 1
snakelist = []


# left_flag = False
# right_flag = False
# up_flag = False
# down_flag = False

clock = pygame.time.Clock()

def draw_Snake(snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], 15, 15])  # [xpos,ypos,w,h]
        for i in range (1, len(snakelist)):
            if snakelist[0] == snakelist[i]:
                return 1

def food_Loop(fx,fy, sx, sy) :
    #generate food at random spot
    # gameDisplay.blit(FOOD_IMAGE, (fx,fy))
    pygame.draw.rect(gameDisplay, red, [fx, fy, 15, 15])
    #food gets eaten
    if abs(sx - fx) < 10 and abs(sy - fy) < 10:
        pygame.draw.rect(gameDisplay, black , [fx, fy, 15, 15])
        return 1
    else:
        return 0

def print_score(gameScore):
    font = pygame.font.Font(None, 30)
    scoretext = font.render("Score: " + str(gameScore), 1, (0,0,0))
    gameDisplay.blit(scoretext, (700, 20))

def game_level(gameScore):
    if gameScore == 0:
        return 15
    elif gameScore == 10:
        return 20
    elif gameScore == 20:
        return 25
    elif gameScore == 30:
        return 30
    elif gameScore == 40:
        return 60
    elif gameScore == 50:
        return 120
    elif gameScore == 60:
        return 150

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -15
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 15
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = 15
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = -15
                lead_x_change = 0
    lead_x += lead_x_change
    lead_y -= lead_y_change

    # rendering graphics
    gameDisplay.fill(white)
    gameDisplay.blit(BACKGROND_IMAGE,(0,0))
    # boundary check
    if lead_x > 800:
        lead_x -= 800
    elif lead_x < 0:
        lead_x += 800
    if lead_y > 600:
        lead_y -= 600
    elif lead_y < 0:
        lead_y += 600

    if food_Loop(food_x, food_y,lead_x,lead_y):
        body_length += 1
        gameScore += 1
        food_x = randint(0, 70)*10
        food_y = randint(0, 60)*10

    snakehead = []
    snakehead.append(lead_x)
    snakehead.append(lead_y)
    snakelist.append(snakehead)

    if len(snakelist) > body_length:
        del(snakelist[0])

    if draw_Snake(snakelist):
        gameScore = 0
        lead_x = 300
        lead_y = 300
        food_x = randint(1, 65) * 10
        food_y = randint(1, 50) * 10
        lead_x_change = 0
        lead_y_change = 0
        body_length = 1
        snakelist = []

    print_score(gameScore)
    pygame.display.update()
    if gameScore%10 == 0:
        game_frequency = game_level(gameScore)
    else:
        game_frequency = game_frequency
    #frames per second
    clock.tick(game_frequency)
    # print(event)

pygame.quit()
quit()

