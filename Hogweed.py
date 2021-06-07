# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from random import randrange
from Plant import Plant

class Hogweed(Plant):
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Hogweed, self).__init__(_currentWorld, _positionX, _positionY)
        self.strength = 10

    def getName(self):
        return "Hogweed"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'hogweedhex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'hogweed.png'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Hogweed(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])

    def action(self):
        self.age += 1
        from Dirt import Dirt
        from Cybersheep import Cybersheep
        from Animal import Animal
        if self.currentWorld.getWorldType() == 0:
            # UP 
            if self.getY() != 0 and not \
            isinstance(self.currentWorld.myMap[self.getX()][self.getY()-1], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()][self.getY()-1], Animal) and not \
                    isinstance(self.currentWorld.myMap[self.getX()][self.getY()-1], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()][self.getY()-1].getName() + \
                    " at (" + str(self.getX()+1) + "," + str(self.getY()) + ").")

                    self.currentWorld.myMap[self.getX()][self.getY()-1].died()
                    self.currentWorld.myMap[self.getX()][self.getY()-1].setDirtOnMap()
            # RIGHT
            if self.getX() != self.currentWorld.getWorldWidth()-1 and not \
            isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Animal) and not \
                    isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()+1][self.getY()].getName() + \
                    " at (" + str(self.getX()+2) + "," + str(self.getY()+1) + ").")

                    self.currentWorld.myMap[self.getX()+1][self.getY()].died()
                    self.currentWorld.myMap[self.getX()+1][self.getY()].setDirtOnMap()
            # DOWN
            if self.getY() != self.currentWorld.getWorldHeight()-1 and not \
            isinstance(self.currentWorld.myMap[self.getX()][self.getY()+1], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()][self.getY()+1], Animal) and not \
                    isinstance(self.currentWorld.myMap[self.getX()][self.getY()+1], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()][self.getY()+1].getName() + \
                    " at (" + str(self.getX()+1) + "," + str(self.getY()+2) + ").")

                    self.currentWorld.myMap[self.getX()][self.getY()+1].died()
                    self.currentWorld.myMap[self.getX()][self.getY()+1].setDirtOnMap()
            # LEFT
            if self.getX() != 0 and not \
            isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Animal) and not \
                    isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()-1][self.getY()].getName() + \
                    " at (" + str(self.getX()) + "," + str(self.getY()+1) + ").")

                    self.currentWorld.myMap[self.getX()-1][self.getY()].died()
                    self.currentWorld.myMap[self.getX()-1][self.getY()].setDirtOnMap()
        elif self.currentWorld.getWorldType() == 1:
            # UP LEFT
            if self.getX() != 0 and self.getY() != 0 and not \
            isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()-1], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()-1], Animal) and not \
                    isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()-1], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()-1][self.getY()-1].getName() + \
                    " at (" + str(self.getX()) + "," + str(self.getY()) + ").")

                    self.currentWorld.myMap[self.getX()-1][self.getY()-1].died()
                    self.currentWorld.myMap[self.getX()-1][self.getY()-1].setDirtOnMap()
            # UP RIGHT
            if self.getY() != 0 and self.getX() != self.currentWorld.getWorldWidth()-1 and not \
            isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()-1], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()][self.getY()-1], Animal) and not \
                isinstance(self.currentWorld.myMap[self.getX()][self.getY()-1], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()+1][self.getY()-1].getName() + \
                    " at (" + str(self.getX()+2) + "," + str(self.getY()) + ").")

                    self.currentWorld.myMap[self.getX()+1][self.getY()-1].died()
                    self.currentWorld.myMap[self.getX()+1][self.getY()-1].setDirtOnMap()
            # RIGHT
            if self.getX() != self.currentWorld.getWorldWidth()-1 and not \
            isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Animal) and not \
                isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()+1][self.getY()].getName() + \
                    " at (" + str(self.getX()+2) + "," + str(self.getY()-1) + ").")

                    self.currentWorld.myMap[self.getX()+1][self.getY()].died()
                    self.currentWorld.myMap[self.getX()+1][self.getY()].setDirtOnMap()
            # DOWN RIGHT
            if self.getX() != self.currentWorld.getWorldWidth()-1 and \
            self.getY() != self.currentWorld.getWorldHeight()-1 and not \
            isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()+1], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()+1], Animal) and not \
                isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()+1], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()+1][self.getY()+1].getName() + \
                    " at (" + str(self.getX()+2) + "," + str(self.getY()+2) + ").")

                    self.currentWorld.myMap[self.getX()+1][self.getY()+1].died()
                    self.currentWorld.myMap[self.getX()+1][self.getY()+1].setDirtOnMap()
            # DOWN LEFT
            if self.getX() != 0 and \
            self.getY() != self.currentWorld.getWorldHeight()-1 and not \
            isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()+1], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()+1], Animal) and not \
                isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()+1], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()-1) + "," \
                    + str(self.getY()-1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()-1][self.getY()+1].getName() + \
                    " at (" + str(self.getX()) + "," + str(self.getY()+1) + ").")

                    self.currentWorld.myMap[self.getX()-1][self.getY()+1].died()
                    self.currentWorld.myMap[self.getX()-1][self.getY()+1].setDirtOnMap()
            # LEFT
            if self.getX() != 0 and not \
            isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Dirt):
                if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Animal) and not \
                isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Cybersheep):

                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," \
                    + str(self.getY()+1) + ") burns down " + \
                    self.currentWorld.myMap[self.getX()-1][self.getY()].getName() + \
                    " at (" + str(self.getX()) + "," + str(self.getY()+1) + ").")

                    self.currentWorld.myMap[self.getX()-1][self.getY()].died()
                    self.currentWorld.myMap[self.getX()-1][self.getY()].setDirtOnMap()

        # SEWING, only 15% to sew
        randomTick = randrange(1, 100, 1)
        if randomTick > 85:
            self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + ") is sewing.")
            newPosition = self.findNewUnoccupiedField()

            if newPosition[0] == None or newPosition[1] == None:
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + " sewing failed.")
                return
            else:
                self.clone(newPosition)