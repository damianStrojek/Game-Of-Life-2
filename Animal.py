# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
from random import randrange
from Organism import Organism
from Dirt import Dirt

class Animal(Organism):
    def __init__(self, _strength, _initiative, _currentWorld, _positionX, _positionY):
        super().__init__(_strength, _initiative, _currentWorld, _positionX, _positionY, True)
    
    def action(self):
        # Every round = +1 to age
        self.age += 1
        # We change the cooldown to breed
        if self.cooldownToBreed > 0:
            self.cooldownToBreed -= 1
        # If organism is newBorn it can't move
        if self.newBorn:
            self.newBorn = False
        else:
            # Finding new position for our organism
            newPosition = self.findNewField()
            if isinstance(self.currentWorld.myMap[newPosition[0]][newPosition[1]], Dirt):
                # Moving instantly
                self.setDirtOnMap()
                self.setPositionX(newPosition[0])
                self.setPositionY(newPosition[1])
                self.setMyselfOnMap()
            else:
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + \
                ") collided with " + self.currentWorld.myMap[newPosition[0]][newPosition[1]].getName() + " at (" + \
                str(newPosition[0]+1) + "," + str(newPosition[1]+1) + ").")

                self.collision(self.currentWorld.myMap[newPosition[0]][newPosition[1]])

    def doSpeciesMatch(self, _secondOrganism):
        if self.getName() == _secondOrganism.getName():
            return True
        else:
            return False

    def getName(self):
        pass

    def getImage(self):
        pass

    def reflected(self, _collidingEntity):
        pass

    def breed(self, _collidingEntity):
        # Find new unoccupied field and clone there
        newField = self.findNewUnoccupiedField()
        if newField[0] == None or newField[1] == None:
            self.currentWorld.log(self.getName() + " have no space to breed.")
            return
        else:
            self.setCooldownToBreed()
            _collidingEntity.setCooldownToBreed()
            self.clone(newField)

    def collision(self, _collidingEntity):
        # If species match they can breed
        if self.doSpeciesMatch(_collidingEntity):
            from Human import Human
            if(isinstance(self, Human)):
                return
            else:
                # Both cooldowns to breed need to equal = 0
                if self.cooldownToBreed == 0 and _collidingEntity.cooldownToBreed == 0:
                    self.currentWorld.log(self.getName() +" at (" + str(self.getX()+1) + "," + str(self.getY()+1) + \
                    ") meets new friend " + _collidingEntity.getName() + " at (" + str(_collidingEntity.getY()+1) + \
                    "," + str(_collidingEntity.getX()+1) + "). [BREED]")

                    self.breed(_collidingEntity)
                else:
                    self.currentWorld.log(self.getName() +" at (" + str(self.getX()+1) + "," + str(self.getY()+1) + \
                    ") is on cooldown and can't breed with " + _collidingEntity.getName() + " at (" + \
                    str(_collidingEntity.getY()+1) + "," + str(_collidingEntity.getX()+1) + ").")
        # FIGHT
        else:
            # Cybersheep eats hogweed
            from Cybersheep import Cybersheep
            from Hogweed import Hogweed
            from Turtle import Turtle
            from Guarana import Guarana
            if isinstance(self, Cybersheep) and isinstance(_collidingEntity, Hogweed):
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + \
                ") eats " + _collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + "," + \
                str(_collidingEntity.getY()+1) + ").")

                self.setDirtOnMap()
                self.setPositionX(_collidingEntity.getX())
                self.setPositionY(_collidingEntity.getY())
                self.setMyselfOnMap()
                _collidingEntity.died()
            # Turtle is colliding entity and reflected attack
            elif isinstance(_collidingEntity, Turtle) and _collidingEntity.getStrength() < self.getStrength() and \
                _collidingEntity.reflected(self):
                self.currentWorld.log(_collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + "," + \
                str(_collidingEntity.getY()+1) + ") reflected " + self.getName() + " at (" + str(self.getX()+1) + \
                "," + str(self.getY()+1) + ").")
                return
            # Turtle is this organism and reflected attack
            elif isinstance(self, Turtle) and self.getStrength() < _collidingEntity.getStrength() and \
                self.reflected(_collidingEntity):
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + \
                str(self.getY()+1) + ") reflected " + _collidingEntity.getName() + " at (" + \
                str(_collidingEntity.getX()+1) + "," + str(_collidingEntity.getY()+1) + ").")
                return
            # Eating guarana += 3 to strength
            elif isinstance(_collidingEntity, Guarana):
                self.currentWorld.log(_collidingEntity.getName() + " at ("+ str(_collidingEntity.getX()+1) + "," + \
                str(_collidingEntity.getY()+1) + ") gets eaten by " + self.getName() + " at (" + str(self.getX()+1) + \
                "," + str(self.getY()+1) + "). " + self.getName() + " has increased strength by 3.")

                self.setStrength(3)
                self.setDirtOnMap()
                self.setPositionX(_collidingEntity.getX())
                self.setPositionY(_collidingEntity.getY())
                self.setMyselfOnMap()
                _collidingEntity.died()
            # Fight between organisms
            else:
                randomTick = randrange(2)
                # Colliding entity won
                # Antelope have a chance to run away
                from Antelope import Antelope
                from Plant import Plant
                from Belladonna import Belladonna
                from Grass import Grass
                from Dandelion import Dandelion
                from Fox import Fox
                if isinstance(self, Antelope) and self.getStrength() < _collidingEntity.getStrength():
                    # There is only 50% chance to run away
                    if randomTick == 1:
                        self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + \
                        ") has escaped from " + _collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + \
                        "," + str(_collidingEntity.getY()+1) + ").")

                        newPosition = self.findNewUnoccupiedField()
                        if newPosition[0] != None and newPosition[1] != None:
                            self.setDirtOnMap()
                            self.setMyselfOnPosition(newPosition)
                            self.setPositionX(newPosition[0])
                            self.setPositionY(newPosition[1])
                        return
                elif isinstance(_collidingEntity, Antelope) and self.getStrength() > _collidingEntity.getStrength():
                    if randomTick == 1:
                        self.currentWorld.log(_collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + \
                        "," + str(_collidingEntity.getY()+1) + ") has escaped from " + self.getName() + " at (" + \
                        str(self.getX()+1) + "," + str(self.getY()+1) + ").")

                        newPosition = _collidingEntity.findNewUnoccupiedField()
                        if newPosition[0] != None and newPosition[1] != None:
                            _collidingEntity.setDirtOnMap()
                            _collidingEntity.setMyselfOnPosition(newPosition)
                            _collidingEntity.setPositionX(newPosition[0])
                            _collidingEntity.setPositionY(newPosition[1])
                        return
    
                # Normal fight
                if _collidingEntity.getStrength() > self.getStrength() and not isinstance(_collidingEntity, Plant):
                    self.currentWorld.log(_collidingEntity.getName() + " at ("+ str(_collidingEntity.getX()+1) + \
                    "," + str(_collidingEntity.getY()+1) + ") kills " + self.getName() + " at (" + str(self.getX()+1) + \
                    "," + str(self.getY()+1) + ").")
                    
                    self.setDirtOnMap()
                    self.died()
                    return
                # If it is belladonna, organism dies instantly
                elif isinstance(_collidingEntity, Belladonna):
                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + \
                    ") eats " + _collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + "," + \
                    str(_collidingEntity.getY()+1) + "). Dies instantly.")

                    self.setDirtOnMap()
                    self.died()
                    _collidingEntity.setDirtOnMap()
                    _collidingEntity.died()
                    return
                # If it is other plant than Belladonna or Hogweed
                elif isinstance(_collidingEntity, Grass) or isinstance(_collidingEntity, Dandelion):
                    self.setDirtOnMap()
                    self.setPositionX(_collidingEntity.getX())
                    self.setPositionY(_collidingEntity.getY())
                    self.setMyselfOnMap()
                    _collidingEntity.died()
                    return
                # Colliding entity loses
                else:
                    # Fox can run away always if loses
                    if isinstance(_collidingEntity, Fox):
                        self.currentWorld.log(_collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + \
                        "," + str(_collidingEntity.getY()+1) + ") refused to fight with " + self.getName() + " at (" + \
                        str(self.getX()+1) + "," + str(self.getY()+1) + ").")
                        
                        newPosition = _collidingEntity.findNewUnoccupiedField()
                        if newPosition[0] != None and newPosition[1] != None:
                            self.setDirtOnMap()
                            self.setPositionX(_collidingEntity.getX())
                            self.setPositionY(_collidingEntity.getY())
                            self.setMyselfOnMap()
                            _collidingEntity.setPositionX(newPosition[0])
                            _collidingEntity.setPositionY(newPosition[1])
                            _collidingEntity.setMyselfOnMap()
                        # Fox cannot run away anywhere so he loses
                        else:
                            self.currentWorld.log(self.getName() + " at ("+ str(self.getX()+1) + "," + str(self.getY()+1) + \
                            ") kills " + _collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + "," + \
                            str(_collidingEntity.getY()+1) + "). He had nowhere to run.")

                            self.setDirtOnMap()
                            self.setPositionX(_collidingEntity.getX())
                            self.setPositionY(_collidingEntity.getY())
                            self.setMyselfOnMap()
                            _collidingEntity.died()
                        return
                    # Rest of the organisms that loses fight
                    else:
                        self.currentWorld.log(self.getName() + " at ("+ str(self.getX()+1) + "," + str(self.getY()+1) + \
                        ") kills " + _collidingEntity.getName() + " at (" + str(_collidingEntity.getX()+1) + "," + \
                        str(_collidingEntity.getY()+1) + ").")

                        self.setDirtOnMap()
                        self.setPositionX(_collidingEntity.getX())
                        self.setPositionY(_collidingEntity.getY())
                        self.setMyselfOnMap()
                        _collidingEntity.died()
                        return