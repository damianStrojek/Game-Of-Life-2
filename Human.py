# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from random import randrange
from Animal import Animal

class Human(Animal):
    cooldownTime = 0            # Time to the next use of skill

    def __init__(self, _currentWorld=None, _positionX=None, _positionY=None):
        super(Human, self).__init__(5, 4, _currentWorld, _positionX, _positionY)

    def getName(self):
        return "Human"
    
    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'humanhex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'human.jpg'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def getCooldownTime(self):
        return self.cooldownTime

    def setCooldownTime(self):
        self.cooldownTime = 6

    def setCooldownTimeTo(self, _cooldownTime):
        self.cooldownTime = _cooldownTime
    
    def action(self):
        self.age += 1

    def specialPower(self):
        if self.cooldownTime == 0:
            self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," +\
            str(self.getY()+1) +") activated his special ability - Speed of antelope!")
            self.setCooldownTime()
        elif self.cooldownTime < 3:
            randomTick = randrange(2)
            if randomTick == 0:
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," +\
                str(self.getY()+1) + ") is very lucky! He got speed of antelope again!")
                self.setCooldownTime()
            elif randomTick == 1:
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," +\
                str(self.getY()+1) + ") unfortunately doesn't get the speed of antelope again.")
        else:
            self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," +\
            str(self.getY()+1) + ") tried to use his ability when it was on cooldown.")

    def movement(self, keyPressed):
        # CHANGE THE COOLDOWN
        if self.cooldownTime > 0:
            self.cooldownTime -= 1
        # SPECIAL POWER
        if keyPressed == pygame.K_r:
            self.specialPower()
        # NEXT ROUND, WAITING IN PLACE
        elif keyPressed == pygame.K_p:
            return
        else:
            from Dirt import Dirt
            # Square world
            if self.currentWorld.getWorldType() == 0:
                # IF SPECIAL POWER IS ON
                if self.cooldownTime >= 3:
                    # UP 2
                    if keyPressed == pygame.K_UP and \
                    self.positionY-2 != -1 and self.positionY-2 != -2:
                        if isinstance(self.currentWorld.myMap[self.getX()][self.getY()-2], Dirt):
                            self.setDirtOnMap()
                            self.positionY -= 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()][self.getY()-2])
                    # DOWN 2
                    elif keyPressed == pygame.K_DOWN and \
                    self.positionY+2 != self.currentWorld.getWorldHeight() and \
                    self.positionY+2 != self.currentWorld.getWorldHeight()+1:
                        if isinstance(self.currentWorld.myMap[self.getX()][self.getY()+2], Dirt):
                            self.setDirtOnMap()
                            self.positionY += 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()][self.getY()+2])
                    # LEFT 2
                    elif keyPressed == pygame.K_LEFT and \
                    self.positionX-2 != -1 and self.positionX-2 != -2:
                        if isinstance(self.currentWorld.myMap[self.getX()-2][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-2][self.getY()])
                    # RIGHT 2
                    elif keyPressed == pygame.K_RIGHT and \
                    self.positionX+2 != self.currentWorld.getWorldWidth() and \
                    self.positionX+2 != self.currentWorld.getWorldWidth()+1:
                        if isinstance(self.currentWorld.myMap[self.getX()+2][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+2][self.getY()])
                # SPECIAL POWER IS OFF
                else:
                    # UP
                    if keyPressed == pygame.K_UP and self.positionY-1 != -1:
                        if isinstance(self.currentWorld.myMap[self.getX()][self.getY()-1], Dirt):
                            self.setDirtOnMap()
                            self.positionY -= 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()][self.getY()-1])
                    # DOWN
                    elif keyPressed == pygame.K_DOWN and self.positionY+1 != self.currentWorld.getWorldHeight():
                        if isinstance(self.currentWorld.myMap[self.getX()][self.getY()+1], Dirt):
                            self.setDirtOnMap()
                            self.positionY += 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()][self.getY()+1])
                    # LEFT
                    elif keyPressed == pygame.K_LEFT and self.positionX-1 != -1:
                        if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-1][self.getY()])
                    # RIGHT
                    elif keyPressed == pygame.K_RIGHT and self.positionX+1 != self.currentWorld.getWorldWidth():
                        if isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+1][self.getY()])
            # HEX WORLD
            elif self.currentWorld.getWorldType() == 1:
                #IF SPECIAL POWER IS ON
                if self.cooldownTime >= 3:
                    # UP LEFT 2
                    if keyPressed == pygame.K_t and \
                    self.positionY-2 != -1 and self.positionY-2 != -2 and \
                    self.positionX-2 != -1 and self.positionX-2 != -2:
                        if isinstance(self.currentWorld.myMap[self.getX()-2][self.getY()-2], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 2
                            self.positionY -= 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-2][self.getY()-2])
                    # UP RIGHT 2
                    elif keyPressed == pygame.K_y and \
                    self.positionY-2 != -1 and self.positionY-2 != -2 and \
                    self.positionX+2 != self.currentWorld.getWorldWidth() and \
                    self.positionX+2 != self.currentWorld.getWorldWidth()+1:
                        if isinstance(self.currentWorld.myMap[self.getX()+2][self.getY()-2], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 2
                            self.positionY -= 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+2][self.getY()+2])
                    # RIGHT 2
                    elif keyPressed == pygame.K_h and \
                    self.positionX+2 != self.currentWorld.getWorldWidth() and \
                    self.positionX+2 != self.currentWorld.getWorldWidth()+1:
                        if isinstance(self.currentWorld.myMap[self.getX()+2][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+2][self.getY()])
                    # DOWN RIGHT 2
                    elif keyPressed == pygame.K_n and \
                    self.positionX+2 != self.currentWorld.getWorldWidth() and \
                    self.positionX+2 != self.currentWorld.getWorldWidth()+1 and \
                    self.positionY+2 != self.currentWorld.getWorldHeight() and \
                    self.positionY+2 != self.currentWorld.getWorldHeight()+1:
                        if isinstance(self.currentWorld.myMap[self.getX()+2][self.getY()+2], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 2
                            self.positionY += 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+2][self.getY()+2])
                    # DOWN LEFT 2
                    elif keyPressed == pygame.K_b and \
                    self.positionX-2 != -1 and self.positionX-2 != -2 and \
                    self.positionY+2 != self.currentWorld.getWorldHeight() and \
                    self.positionY+2 != self.currentWorld.getWorldHeight()+1:
                        if isinstance(self.currentWorld.myMap[self.getX()-2][self.getY()+2], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 2
                            self.positionY += 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-2][self.getY()+2])
                    # LEFT 2
                    elif keyPressed == pygame.K_g and \
                    self.positionX-1 != -1 and self.positionX-2 != -2:
                        if isinstance(self.currentWorld.myMap[self.getX()-2][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 2
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-2][self.getY()])
                # SPECIAL POWER IS OFF
                else:
                    # UP LEFT 1
                    if keyPressed == pygame.K_t and \
                    self.positionY-1 != -1 and self.positionX-1 != -1:
                        if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()-1], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 1
                            self.positionY -= 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-1][self.getY()-1])
                    # UP RIGHT 1
                    elif keyPressed == pygame.K_y and \
                    self.positionY-1 != -1 and \
                    self.positionX+1 != self.currentWorld.getWorldWidth():
                        if isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()-1], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 1
                            self.positionY -= 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+1][self.getY()+1])
                    # RIGHT 1
                    elif keyPressed == pygame.K_h and \
                    self.positionX+1 != self.currentWorld.getWorldWidth():
                        if isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+1][self.getY()])
                    # DOWN RIGHT 1
                    elif keyPressed == pygame.K_n and \
                    self.positionX+1 != self.currentWorld.getWorldWidth() and \
                    self.positionY+1 != self.currentWorld.getWorldHeight():
                        if isinstance(self.currentWorld.myMap[self.getX()+1][self.getY()+1], Dirt):
                            self.setDirtOnMap()
                            self.positionX += 1
                            self.positionY += 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()+1][self.getY()+1])
                    # DOWN LEFT 1
                    elif keyPressed == pygame.K_b and \
                    self.positionX-1 != -1 and \
                    self.positionY+1 != self.currentWorld.getWorldHeight():
                        if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()+1], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 1
                            self.positionY += 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-1][self.getY()+1])
                    # LEFT 1
                    elif keyPressed == pygame.K_g and \
                    self.positionX-1 != -1:
                        if isinstance(self.currentWorld.myMap[self.getX()-1][self.getY()], Dirt):
                            self.setDirtOnMap()
                            self.positionX -= 1
                            self.setMyselfOnMap()
                        else:
                            self.collision(self.currentWorld.myMap[self.getX()-1][self.getY()])
 