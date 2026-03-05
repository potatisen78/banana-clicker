import pygame
from sys import exit

from pygame import mouse

pygame.init()
gameactive = True
screen = pygame.display.set_mode((1920, 1100))

bango = 0
banvar = 10
banspeed = 0
money = 0

def clicked(firstrun):
    if firstrun:
        bango = 0
        banvar = 10
        banspeed = 0
        money = 0
        firstrun = False
    banana2_rect.y -= 2
    bango += 1


    if bango > 28:
        # banvar -= 0.37037037037
        ##if banvar < 0:
        banana2_rect.y -= banspeed
        banvar += 0.1
        banspeed += 0.3
        if banana2_rect.y < -500:
            bango = 0
            banana2_rect.center = (660, 540)
            money += 1
    return bango, banvar, banspeed, money




grassbackround = pygame.image.load("grassbackround.png").convert_alpha()
grassrect = grassbackround.get_rect(center=( 960, 575))

banana1 = pygame.image.load("banana/banana1.png").convert_alpha()
banana2 = pygame.image.load("banana/banana2.png").convert_alpha()
banana3 = pygame.image.load("banana/banana3.png").convert_alpha()

banana1_rect = banana1.get_rect(center=( 620, 575))
banana2_rect = banana2.get_rect(center=(660, 540 ))
banana3_rect = banana3.get_rect(center=(620, 600))

clicked(True)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameactive = False
            pygame.quit()
            exit()

    while gameactive:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked(False)

        if event.type == pygame.QUIT:
                gameactive = False
                pygame.quit()
                exit()
        screen.blit(grassbackround, grassrect)

        screen.blit(banana1, banana1_rect)
        screen.blit(banana2, banana2_rect)
        screen.blit(banana3, banana3_rect)



        pygame.display.update()
