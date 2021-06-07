# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from Plant import Plant

class Guarana(Plant):
    def __init__(self, _currentWorld=None, _positionX=None, _positionY=None):
        super(Guarana, self).__init__(_currentWorld, _positionX, _positionY)
    
    def getName(self):
        return "Guarana"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'guaranahex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'guarana.png'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Guarana(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])