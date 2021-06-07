# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from random import randrange
from Animal import Animal

class Antelope(Animal):
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Antelope, self).__init__(4, 4, _currentWorld, _positionX, _positionY)
    
    def getName(self):
        return "Antelope"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'antelopehex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'antelope.png'))
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Antelope(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])

    def findNewField(self):
        returnPosition = [self.positionX, self.positionY]
        if self.currentWorld.getWorldType() == 0:
            while True:
                field = randrange(8)
                # UP 1
                if field == 0:
                    if returnPosition[1]-1 != -1:
                        returnPosition[1] -= 1
                        return returnPosition
                # RIGHT 1
                elif field == 1: 
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth():
                        returnPosition[0] += 1
                        return returnPosition
                # DOWN 1
                elif field == 2:
                    if returnPosition[1]+1 != self.currentWorld.getWorldHeight():
                        returnPosition[1] += 1
                        return returnPosition
                # LEFT 1
                elif field == 3:
                    if returnPosition[0]-1 != -1:
                        returnPosition[0] -= 1
                        return returnPosition
                # UP 2
                elif field == 4:
                    if returnPosition[1]-2 != -1 and returnPosition[1]-2 != -2:
                        returnPosition[1] -= 2
                        return returnPosition
                # RIGHT 2
                elif field == 5:
                    if returnPosition[0]+2 != self.currentWorld.getWorldWidth() and \
                        returnPosition[0]+2 != self.currentWorld.getWorldWidth()+1:
                        returnPosition[0] += 2
                        return returnPosition
                # DOWN 2
                elif field == 6:
                    if returnPosition[1]+2 != self.currentWorld.getWorldHeight() and \
                        returnPosition[1]+2 != self.currentWorld.getWorldHeight()+1:
                        returnPosition[1] += 2
                        return returnPosition
                # LEFT 2
                elif field == 7:
                    if returnPosition[0]-2 != -1 and returnPosition[0]-2 != -2:
                        returnPosition[0] -= 2
                        return returnPosition
        elif self.currentWorld.getWorldType() == 1:
            while True:
                field = randrange(12)
                # UP LEFT 1
                if field == 0:
                    if returnPosition[0]-1 != -1 and \
                        returnPosition[1]-1 != -1:
                        returnPosition[0] -= 1
                        returnPosition[1] -= 1
                        return returnPosition
                # UP RIGHT 1
                elif field == 1: 
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth() and \
                        returnPosition[1]-1 != -1:
                        returnPosition[0] += 1
                        returnPosition[1] -= 1
                        return returnPosition
                # RIGHT 1
                elif field == 2:
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth():
                        returnPosition[0] += 1
                        return returnPosition
                # DOWN RIGHT 1
                elif field == 3:
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth() and \
                        returnPosition[1]+1 != self.currentWorld.getWorldHeight():
                        returnPosition[0] += 1
                        returnPosition[1] += 1
                        return returnPosition
                # DOWN LEFT 1
                elif field == 4:
                    if returnPosition[0]-1 != -1 and \
                        returnPosition[1]+1 != self.currentWorld.getWorldHeight():
                        returnPosition[0] -= 1
                        returnPosition[1] += 1
                        return returnPosition
                # LEFT 1
                elif field == 5:
                    if returnPosition[0]-1 != -1:
                        returnPosition[0] -= 1
                        return returnPosition
                # UP LEFT 2
                elif field == 6:
                    if returnPosition[0]-2 != -1 and returnPosition[0]-2 != -2 and \
                        returnPosition[1]-2 != -1 and returnPosition[1]-2 != -2:
                        returnPosition[0] -= 2
                        returnPosition[1] -= 2
                        return returnPosition
                # UP RIGHT 2
                elif field == 7:
                    if returnPosition[0]+2 != self.currentWorld.getWorldWidth() and \
                        returnPosition[0]+2 != self.currentWorld.getWorldWidth()+1 and \
                        returnPosition[1]-2 != -1 and returnPosition[1]-2 != -2:
                        returnPosition[0] += 2
                        returnPosition[1] -= 2
                        return returnPosition
                # RIGHT 2
                elif field == 8:
                    if returnPosition[0]+2 != self.currentWorld.getWorldWidth() and \
                        returnPosition[0]+2 != self.currentWorld.getWorldWidth()+1:
                        returnPosition[0] += 2
                        return returnPosition
                # DOWN RIGHT 2
                elif field == 9:
                    if returnPosition[0]+2 != self.currentWorld.getWorldWidth() and \
                        returnPosition[0]+2 != self.currentWorld.getWorldWidth()+1 and \
                        returnPosition[1]+2 != self.currentWorld.getWorldHeight() and \
                        returnPosition[1]+2 != self.currentWorld.getWorldHeight()+1:
                        returnPosition[0] += 2
                        returnPosition[1] += 2
                        return returnPosition
                # DOWN LEFT 2   
                elif field == 10:   
                    if returnPosition[0]-2 != -1 and returnPosition[0]-2 != -2 and \
                        returnPosition[1]+2 != self.currentWorld.getWorldHeight() and \
                        returnPosition[1]+2 != self.currentWorld.getWorldHeight()+1:
                        returnPosition[0] -= 2
                        returnPosition[1] += 2
                        return returnPosition
                # LEFT 2
                elif field == 11:
                    if returnPosition[0]-2 != -1 and returnPosition[0]-2 != -2:
                        returnPosition[0] -= 2
                        return returnPosition