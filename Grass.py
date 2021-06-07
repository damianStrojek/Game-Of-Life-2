# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from Plant import Plant

class Grass(Plant):
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Grass, self).__init__(_currentWorld, _positionX, _positionY)

    def getName(self):
        return "Grass"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'grasshex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'grass.jpg'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Grass(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])
