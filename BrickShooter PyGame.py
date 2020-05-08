import pygame
from random import randint
import sys
from pygame.locals import *
from enum import Enum


class type_bloc(Enum):
    neutre = 0
    defil = 1
    depla = 2
    tir = 3

class meteor:
    def __init__(self, posX, posY):
        percent = randint(0, 100) # vitesse de défilement individuelle
        if percent < 15:
            self.defil = 2
        elif percent < 50:
            self.defil = 1
        else:
            self.defil = 0
        percent_type = randint(0, 100)
        self.value = randint(1,3)
        if percent_type < 5 :
            self.type = type_bloc.defil.name
            self.texture = asteroid_defil
        elif percent_type < 10:
            self.type = type_bloc.depla.name
            self.texture = asteroid_depla
        elif percent_type < 15:
            self.type = type_bloc.tir.name
            self.texture = asteroid_tir
        else:
            self.type = type_bloc.neutre.name
            self.texture = asteroid
            self.value = 0
        self.x_bloc = posX
        self.y_bloc = posY
        screen.blit(self.texture, (self.x_bloc, self.y_bloc))
    def move(self, posX, posY, speed_falling):
        self.x_bloc = posX
        self.y_bloc = posY + speed_falling + self.defil # vitesse de défilement individuelle
        screen.blit(self.texture, (self.x_bloc, self.y_bloc))

class bullet:
    def __init__(self, texture, posX, posY = 800):
        self.shoot_x = posX
        self.shoot_y = posY
        screen.blit(texture, (self.shoot_x, self.shoot_y))
    def move(self, texture, posX, posY, speed_shot):
        self.shoot_x = posX
        self.shoot_y = posY - speed_shot
        screen.blit(texture, (self.shoot_x, self.shoot_y))

def loadImg(name):
    return pygame.image.load("Images/" + name)

def font(size = 40):
    return pygame.font.SysFont("twcen", size)

def drawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x,y)
    surface.blit(textobj, textrect)

def getHighscore():
    try:
        myFile = open("HighScore.txt", "r")
        highScore = myFile.read()
        myFile.close()
    except:
        highScore = 0
    return highScore

def menu():
    pygame.mouse.set_visible(1)
    button_height = 50
    button_length = 200
    border = 6
    selected = 0
    while True:
        screen.blit(background, (0, 0))
        drawText('BrickShooter', font(80), (255, 255, 0), screen, centerX, 200)

        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(centerX-int(button_length/2), 425, button_length, button_height)
        button_shop = pygame.Rect(centerX-int(button_length/2), 525, button_length, button_height)
        button_instructions = pygame.Rect(centerX-int(button_length/2), 625, button_length, button_height)

        if button_play.collidepoint((mx, my)) or selected == 1:
            selected = 1
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX-int((button_length+border)/2), int(425 - border/2), button_length+border, button_height+border))
        if button_shop.collidepoint((mx, my)) or selected == 2:
            selected = 2
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX - int((button_length + border) / 2), int(525 - border / 2), button_length + border, button_height + border))
        if button_instructions.collidepoint((mx, my)) or selected == 3:
            selected = 3
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX-int((button_length+border)/2), int(625 - border/2), button_length+border, button_height+border))

        pygame.draw.rect(screen, (45, 175, 230), button_play)
        pygame.draw.rect(screen, (45, 175, 230), button_shop)
        pygame.draw.rect(screen, (45, 175, 230), button_instructions)

        drawText('Play', font(), (255, 255, 255), screen, centerX, 450)
        drawText('Shop', font(), (255, 255, 255), screen, centerX, 550)
        drawText('Instructions', font(), (255, 255, 255), screen, centerX, 650)

        highScore = getHighscore()
        if highScore:
            drawText('Best Score :', font(), (255, 255, 0), screen, centerX, 750)
            drawText(str(highScore), font(), (255, 255, 0), screen, centerX, 800)

        drawText('Developped by Aloin Rémi & Grégory Mostacci', font(20), (255, 255, 255), screen, centerX, HEIGHT-15)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key and event.key == K_UP:
                    selected -= 1
                    if selected < 1:
                        selected = 3
                if event.key and event.key == K_DOWN:
                    selected += 1
                    if selected > 3:
                        selected = 1
                if event.key == K_RETURN and selected == 1:
                    game()
                    selected = 0
                if event.key == K_RETURN and selected == 2:
                    shop()
                    selected = 0
                if event.key == K_RETURN and selected == 3:
                    instructions()
                    selected = 0
            if event.type == MOUSEBUTTONDOWN:
                if button_play.collidepoint((mx, my)):
                    game()
                if button_shop.collidepoint((mx, my)):
                    shop()
                if button_instructions.collidepoint((mx, my)):
                    instructions()
                selected = 0

        pygame.display.update()
        clock.tick(30)

def pause():
    pause = True
    while pause:
        drawText('Game Paused', font(), (255, 255, 0), screen, centerX, centerY)
        drawText('Press [Enter] to resume', font(20), (255, 255, 0), screen, centerX, centerY+200)
        drawText('Press [Backspace] to return menu', font(20), (255, 255, 0), screen, centerX, centerY+250)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                    pygame.mouse.set_visible(1)
                    pause = False
                if (event.key == K_ESCAPE or event.key == K_RETURN or event.key == K_SPACE):
                    running = True
                    pause = False
        pygame.display.update()
        clock.tick(30)
    return running

def endGame(scoreInt):
    highScore = getHighscore()
    scoreBeatten = False
    end = True
    while end:
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(centerX - int(WIDTH / 2), centerY - 50, WIDTH, 100))
        drawText('Game Over !', font(50), (255, 0, 0), screen, centerX, centerY)
        if scoreInt > int(highScore) or scoreBeatten:
            if not(scoreBeatten) :
                highScore = scoreInt
                myFile = open("HighScore.txt", "w+")
                myFile.write(str(highScore))
                myFile.close()
                scoreBeatten = True
            drawText('NEW BEST SCORE :', font(), (255, 255, 0), screen, centerX, centerY+150)
            drawText(str(highScore), font(), (255, 255, 0), screen, centerX, centerY+200)
        else:
            drawText('Your score :', font(30), (255, 255, 0), screen, centerX, centerY + 100)
            drawText(str(scoreInt), font(30), (255, 255, 0), screen, centerX, centerY + 130)
            drawText('Best score :', font(30), (255, 255, 0), screen, centerX, centerY + 200)
            drawText(str(highScore), font(30), (255, 255, 0), screen, centerX, centerY + 230)
        drawText('Press [Enter] to restart', font(20), (255, 255, 0), screen, centerX, centerY+350)
        drawText('Press [Backspace] or [Escape] to return menu', font(20), (255, 255, 0), screen, centerX, centerY+375)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE or event.key == K_ESCAPE:
                    end = False
                if event.key == K_RETURN:
                    game()
                    end = False
        pygame.display.update()
        clock.tick(30)


def game():
    pygame.mouse.set_visible(0)
    x = centerX - player.get_width()/2 # Position joueur
    y =  HEIGHT - player.get_height()
    meteors = [] # initialisation de la liste de blocs
    bullets = [] # initialisation de la liste de balles
    scoreInt = 0 # Score
    left_pressed = False # Binds (pour rester appuyé)
    right_pressed = False
    speed_player = 5 # vitesse joueur
    speed_shot = 15 # vitesse de la balle
    speed_falling = 1 # vitesse des blocs
    freq_apparition = 60/speed_falling # fréquence d'apparition des blocs
    fallingTimes = 0 # incrémente à chaque while

    running = True
    while running:

# Affichage du backgound
        screen.blit(background, (0, 0))

# Gestion des blocs
        for meteor in meteors:
            meteor.move(meteor.x_bloc, meteor.y_bloc, speed_falling)
            if meteor.y_bloc > HEIGHT-40 and running:
                running = False
                endGame(scoreInt)
        if fallingTimes%freq_apparition == 0:
            generate_meteor(meteors)
        fallingTimes += 1

# Affichage du score et du joueur
        screen.blit(scoreback, (0, 0))
        drawText('Score :', font(20), (255, 255, 0), screen, centerX, 10)
        drawText(str(scoreInt), font(), (255, 255, 0), screen, centerX, 32)
        screen.blit(player, (int(x), y))

# Binds
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: # Retour menu
                    running = False
                    pygame.mouse.set_visible(1)
                if (event.key == K_ESCAPE): # Pause
                    running = pause()
                if (event.key == K_UP or event.key == K_SPACE): # Tir
                    newbullet = bullet(shot, int(x + player.get_width()/2 -2))
                    bullets.append(newbullet)
                if (event.key == K_LEFT or event.key == K_a): # Gauche enfoncée
                    left_pressed = True
                    right_pressed = False
                if (event.key == K_RIGHT or event.key == K_d): # Droite enfoncée
                    right_pressed = True
                    left_pressed = False
            if event.type == KEYUP:
                if (event.key == K_LEFT or event.key == K_a): # Gauche relachée
                    left_pressed = False
                if (event.key == K_RIGHT or event.key == K_d): # Droite relachée
                    right_pressed = False
        if left_pressed:
            if (x > 0 - player.get_width()/3): # Aller à gauche dans la limite de l'écran
                x -= speed_player
        if right_pressed:
            if (x < WIDTH - 2*player.get_width()/3): # Aller à droite dans la limite de l'écran
                x += speed_player

# Gestion de la balle
        for singleBullet in bullets:
            i = 0
            destroyBullet = 0
            while i < len(meteors) and destroyBullet == 0:
                if ((singleBullet.shoot_y < meteors[i].y_bloc + 60 and singleBullet.shoot_y > meteors[i].y_bloc) and (singleBullet.shoot_x > meteors[i].x_bloc and singleBullet.shoot_x < meteors[i].x_bloc + 60)):  # Si la balle croise un bloc dans la liste
                    scoreInt += 10
                    if meteors[i].type != "neutre":
                        if meteors[i].type == "defil":
                            speed_falling += meteors[i].value
                            freq_apparition = 60 / speed_falling
                        if meteors[i].type == "depla":
                            speed_player += meteors[i].value
                        if meteors[i].type == "tir":
                            speed_shot += meteors[i].value
                    meteors.pop(i) # Suppression du bloc
                    destroyBullet = 1
                i += 1
            if singleBullet.shoot_y > 0 and destroyBullet == 0: # Continuité de la balle
                singleBullet.move(shot, singleBullet.shoot_x, singleBullet.shoot_y, speed_shot)
            else:
                bullets.remove(singleBullet)

# Difficulté
#         if fallingTimes%1000 == 0:
#             speed_falling +=1

# Rafraichissement de la fenetre
        if running :
            pygame.display.update()
            clock.tick(30)
    pygame.mouse.set_visible(1)

def generate_meteor(meteors):
    for i in range(0,8):
        appear = randint(0,100)
        if appear < 30:
            x_bloc = 66 + 66*i
            y_bloc = -50
            newMeteor = meteor(int(x_bloc-asteroid.get_width()/2), int(y_bloc-asteroid.get_height()/2))
            meteors.append(newMeteor)
    if meteors == []:
        generate_meteor(meteors)

def shop():
    button_length = 50
    border = 6
    shopping = True
    while shopping:
        screen.blit(background, (0, 0))

        drawText('Shop', font(60), (255, 255, 0), screen, centerX, 100)

        mx, my = pygame.mouse.get_pos()

        button_defil_moins = pygame.Rect(centerX - int(WIDTH / 4) - int(button_length / 2), 425, button_length, button_length)
        button_tir_moins = pygame.Rect(centerX - int(WIDTH / 4) - int(button_length / 2), 525, button_length, button_length)
        button_depla_moins = pygame.Rect(centerX - int(WIDTH / 4) - int(button_length / 2), 625, button_length, button_length)

        button_defil_plus = pygame.Rect(centerX + int(WIDTH / 4) - int(button_length / 2), 425, button_length, button_length)
        button_tir_plus = pygame.Rect(centerX + int(WIDTH / 4) - int(button_length / 2), 525, button_length, button_length)
        button_depla_plus = pygame.Rect(centerX + int(WIDTH / 4) - int(button_length / 2), 625, button_length, button_length)

        if button_defil_moins.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX-int(WIDTH/4)-int((button_length+border)/2), int(425 - border/2), button_length+border, button_length+border))
        if button_tir_moins.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX-int(WIDTH/4) - int((button_length + border) / 2), int(525 - border / 2), button_length + border, button_length + border))
        if button_depla_moins.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX-int(WIDTH/4)-int((button_length+border)/2), int(625 - border/2), button_length+border, button_length+border))

        if button_defil_plus.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX+int(WIDTH/4)-int((button_length+border)/2), int(425 - border/2), button_length+border, button_length+border))
        if button_tir_plus.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX+int(WIDTH/4) - int((button_length + border) / 2), int(525 - border / 2), button_length + border, button_length + border))
        if button_depla_plus.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(centerX+int(WIDTH/4)-int((button_length+border)/2), int(625 - border/2), button_length+border, button_length+border))

        pygame.draw.rect(screen, (45, 175, 230), button_defil_moins)
        pygame.draw.rect(screen, (45, 175, 230), button_tir_moins)
        pygame.draw.rect(screen, (45, 175, 230), button_depla_moins)

        drawText('-', font(60), (255, 255, 255), screen, centerX - int(WIDTH / 4), 450)
        drawText('-', font(60), (255, 255, 255), screen, centerX - int(WIDTH / 4), 550)
        drawText('-', font(60), (255, 255, 255), screen, centerX - int(WIDTH / 4), 650)

        drawText('Meteor speed', font(), (255, 255, 255), screen, centerX, 450)
        drawText('Bullet speed', font(), (255, 255, 255), screen, centerX, 550)
        drawText('Player speed', font(), (255, 255, 255), screen, centerX, 650)

        pygame.draw.rect(screen, (45, 175, 230), button_defil_plus)
        pygame.draw.rect(screen, (45, 175, 230), button_tir_plus)
        pygame.draw.rect(screen, (45, 175, 230), button_depla_plus)

        drawText('+', font(60), (255, 255, 255), screen, centerX + int(WIDTH/4), 450)
        drawText('+', font(60), (255, 255, 255), screen, centerX + int(WIDTH/4), 550)
        drawText('+', font(60), (255, 255, 255), screen, centerX + int(WIDTH/4), 650)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    shopping = False

        pygame.display.update()
        clock.tick(30)

def instructions():
    instructionning = True
    while instructionning:
        screen.blit(background, (0, 0))

        drawText('Instructions', font(60), (255, 255, 0), screen, centerX, 100)
        drawText('The purpose of this Brickshooter is to do', font(30), (255, 255, 255), screen, centerX, 250)
        drawText('the highest score, for that you have to', font(30), (255, 255, 255), screen, centerX, 290)
        drawText('destroy the asteroids which approach the', font(30), (255, 255, 255), screen, centerX, 330)
        drawText('the spaceship using its laser cannon' , font(30), (255, 255, 255), screen, centerX, 370)
        drawText('Warning, if the ship doesn\'t destroy all the' , font(30), (255, 255, 255), screen, centerX, 410)
        drawText('asteroids that arrive on it, the game ends.' , font(30), (255, 255, 255), screen, centerX, 450)
        drawText('Good Luck !' , font(50), (255, 255, 255), screen, centerX, 550)
        drawText('Use [Q] [D] or arrows to move' , font(), (255, 255, 0), screen, centerX, 720)
        drawText('Use [SPACE] or up arrow to shoot' , font(), (255, 255, 0), screen, centerX, 800)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    instructionning = False

        pygame.display.update()
        clock.tick(30)


clock = pygame.time.Clock()

pygame.init()

WIDTH = 600
HEIGHT = 900
centerX = int(WIDTH/2)
centerY = int(HEIGHT/2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BrickShooter')

background = loadImg("background_space.gif")
scoreback = loadImg("scoreback.png")
player = loadImg("spaceship.png")
shot = loadImg("bullet.png")
asteroid = loadImg("asteroid.png")
asteroid_defil = loadImg("asteroid_defil.png")
asteroid_depla = loadImg("asteroid_depla.png")
asteroid_tir = loadImg("asteroid_tir.png")

menu()