import pygame
from pygame import mixer

pygame.init()
mixer.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("background.jpg-")
player = pygame.Rect(50, 300, 25, 25)

boxRed = pygame.Rect(200, 100, 50, 50)
boxGreen = pygame.Rect(400, 100, 50, 50)
boxBlue = pygame.Rect(600, 100, 50, 50)

buttonRed = pygame.Rect(225, 550, 10, 10)
buttonGreen = pygame.Rect(425, 550, 10, 10)
buttonBlue = pygame.Rect(625, 550, 10, 10)

your_winner = pygame.image.load("your_winner.jpg")

clock_object = pygame.time.Clock()

walking_sound = pygame.mixer.music.load("walking.ogg")
donk_sound = pygame.mixer.Sound("donk.mp3")
win_sound = pygame.mixer.Sound("yay.mp3")


ceiling = pygame.Rect(0, 0, 800, 1)
floor = pygame.Rect(0, 600, 800, 1)
left_wall = pygame.Rect(0, 1, 1, 500)
right_wall = pygame.Rect(800, 1, 1, 500)

evil_wall = pygame.Rect(350, 300 , 150, 20)

win = False

run = True
while run:

    screen.fill((0, 0, 0)) #keeps the screen from leaving trails on moving objects      
    clock_object.tick(600) #limits FPS and update rate, and therefore speed

   


    #box logic and rendering

    screen.blit(background, (0, 0))

    if boxRed.colliderect(buttonRed):
        pygame.draw.rect(screen, (255, 255, 0), boxRed)
    else:
        pygame.draw.rect(screen, (255, 0, 0), boxRed)

    if boxGreen.colliderect(buttonGreen):
        pygame.draw.rect(screen, (255, 255, 0), boxGreen)
    else:
        pygame.draw.rect(screen, (0, 255, 0), boxGreen)

    if boxBlue.colliderect(buttonBlue):
        pygame.draw.rect(screen, (255, 255, 0), boxBlue)
    else:
        pygame.draw.rect(screen, (0, 0, 255), boxBlue)

    #button rendering
    pygame.draw.rect(screen, (255, 0, 0), buttonRed)
    pygame.draw.rect(screen, (0, 255, 0), buttonGreen)
    pygame.draw.rect(screen, (0, 0, 255), buttonBlue)

    pygame.draw.rect(screen, (175, 175, 175), evil_wall)

    #win condition and sound logic
    if boxRed.colliderect(buttonRed) and boxGreen.colliderect(buttonGreen) and boxBlue.colliderect(buttonBlue):
        screen.blit(your_winner, (50, 50))
        if win == False:
            pygame.mixer.Sound.play(win_sound)
            win = True
    else:
        win = False 

    key = pygame.key.get_pressed()

    pygame.draw.rect(screen, (175, 175, 175), player)

    #detects collision for moving
    def box_detect():
        if player.colliderect(boxRed):
            return True
        elif player.colliderect(boxGreen):
            return True
        elif player.colliderect(boxBlue):
            return True
        elif player.colliderect(ceiling):
            return True
        elif player.colliderect(floor):
            return True
        elif player.colliderect(left_wall):
            return True
        elif player.colliderect(right_wall):
            return True
        elif player.colliderect(evil_wall):
            return True
        
    #detects which box player is on
    def color_detect():
        if player.colliderect(boxRed):
            return boxRed
        elif player.colliderect(boxGreen):
            return boxGreen
        elif player.colliderect(boxBlue):
            return boxBlue


    #movement
    if key[pygame.K_UP] == True:
        if box_detect():

            if color_detect() == boxRed:
                boxRed.move_ip(0, -1)
            elif color_detect() == boxGreen:
                boxGreen.move_ip(0, -1)
            elif color_detect() == boxBlue:
                boxBlue.move_ip(0, -1)
            player.move_ip(0, 3)
            
        else:
            player.move_ip(0, -1)

    elif key[pygame.K_DOWN] == True:
        if box_detect():

            if color_detect() == boxRed:
                boxRed.move_ip(0, 1)
            elif color_detect() == boxGreen:
                boxGreen.move_ip(0, 1)
            elif color_detect() == boxBlue:
                boxBlue.move_ip(0, 1)
            player.move_ip(0, -3)

        else:
            player.move_ip(0, 1)

    elif key[pygame.K_LEFT] == True:
        if box_detect():

            if color_detect() == boxRed:
                boxRed.move_ip(-1, 0)
            elif color_detect() == boxGreen:
                boxGreen.move_ip(-1, 0)
            elif color_detect() == boxBlue:
                boxBlue.move_ip(-1, 0)
            player.move_ip(3, 0)

        else:
            player.move_ip(-1, 0)

    elif key[pygame.K_RIGHT] == True:
        if box_detect():

            if color_detect() == boxRed:
                boxRed.move_ip(1, 0)
            elif color_detect() == boxGreen:            
                boxGreen.move_ip(1, 0)
            elif color_detect() == boxBlue:
                boxBlue.move_ip(1, 0)   
            player.move_ip(-3, 0)

        else:
            player.move_ip(1, 0)


    #handles if items or the player go out of bounds for some reason
    if player.x > 800 or player.x < 0 or player.y > 600 or player.y < 0:
        player.x = 50
        player.y = 300
    if boxRed.x > 800 or boxRed.x < 0 or boxRed.y > 600 or boxRed.y < 0:
        boxRed.x = 200
        boxRed.y = 100
    if boxGreen.x > 800 or boxGreen.x < 0 or boxGreen.y > 600 or boxGreen.y < 0:
        boxGreen.x = 400
        boxGreen.y = 100
    if boxBlue.x > 800 or boxBlue.x < 0 or boxBlue.y > 600 or boxBlue.y < 0:
        boxBlue.x = 600
        boxBlue.y = 100

    #does the funny breakcore when moving
    if (key [pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]) and pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play(-1)
    elif (key[pygame.K_UP] == False and key[pygame.K_DOWN] == False and key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False) and pygame.mixer.music.get_busy() == True:
        pygame.mixer.music.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
