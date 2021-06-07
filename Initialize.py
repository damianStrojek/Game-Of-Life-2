# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
from pygame.locals import *
import pygame
pygame.font.init()

class InitializeGame:
    def __init__(self):
        pass
    
    def getKey(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                return event.key
            else:
                pass

    def initGame(self):
        WIN = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Game of Life - Size of World")
        WIN.fill((255, 255, 255))
        text1 = pygame.font.SysFont('times new roman', 23).render("Type in width and length of your world", False, (0, 0, 0))
        text2 = pygame.font.SysFont('times new roman', 23).render("separated by space", False, (0, 0, 0))
        WIN.blit(text1, (10, 130))
        WIN.blit(text2, (110, 160))
        pygame.display.update()
        currentInput = ""
        while True:
            inputKey = self.getKey()
            if inputKey == pygame.K_RETURN:
                break
            elif inputKey == pygame.K_q:
                exit()
            elif inputKey <= 127:
                currentInput += chr(inputKey)
        return (currentInput.split())