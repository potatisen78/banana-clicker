import pygame
from sys import exit
from directKeys import *
pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F6:
                if go:
                    go = False
                elif go == False:
                    go = True

    if go:
        click()