# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import os, pygame
from Organism import Organism

class Dirt(Organism):
    # Default block that makes our world
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Dirt, self).__init__(0, 0, _currentWorld, _positionX, _positionY, False)

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'dirthex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'dirt.jpg'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def getName(self):
        return "Dirt"