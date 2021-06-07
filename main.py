# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
from pygame.locals import *
import pygame
pygame.font.init()

def main():
    from World import World
    from Initialize import InitializeGame
    size = InitializeGame().initGame()
    # Making new world that we can play on
    newWorld = World(int(size[0]), int(size[1]))
    # Window
    WIN = pygame.display.set_mode((newWorld.getWorldWidth()*20+newWorld.getWidthMargin(), \
    newWorld.getWorldHeight()*20+newWorld.getHeightMargin()))
    # To fit the legend we need to resize our window
    if newWorld.getWorldWidth() < 20 or newWorld.getWorldHeight() < 20:
        WIN = pygame.display.set_mode((20*20+newWorld.getWidthMargin(), \
        20*20+newWorld.getNumber()))

    pygame.display.set_caption("Game of Life - Damian Strojek")

    newWorld.startGame()
    newWorld.drawWindow(WIN)

    # While our human is alive we can play the game
    while newWorld.myHuman.getIsAlive():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                newWorld.myHuman.humanAlive = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # Exiting the game with Q
                    exit()
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
                    event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                    event.key == pygame.K_p or event.key == pygame.K_r or \
                    event.key == pygame.K_g or event.key == pygame.K_t or \
                    event.key == pygame.K_y or event.key == pygame.K_h or \
                    event.key == pygame.K_n or event.key == pygame.K_b:
                    # Movement of human
                    newWorld.myHuman.movement(event.key)
                    newWorld.nextRound()
                    newWorld.drawWindow(WIN)
                    if not newWorld.myHuman.getIsAlive():
                        newWorld.gameOver(WIN)
                elif event.key == pygame.K_s:
                    # Saving the world
                    newWorld.saveWorld()
                    newWorld.log("Save has been successfully saved!")
                    newWorld.drawWindow(WIN)
                elif event.key == pygame.K_l:
                    # Loading the world
                    newWorld.loadWorld()
                    newWorld.log("World has been successfully loaded!")
                    newWorld.drawWindow(WIN)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # So my idea (I know its not perfect) is to get first click and if it was on empty space
                # We mark flag (lastClick) True and next click we check if it was on some organism to spawn
                pos = pygame.mouse.get_pos()
                if pos[0] < newWorld.getWorldWidth()*20 and pos[1] < newWorld.getWorldHeight()*20:
                    newWorld.handleMouse(pos)
                    newWorld.drawWindow(WIN)
                elif newWorld.getLastClick() and pos[0] > newWorld.getWorldWidth()*20+newWorld.getNumber():
                    # 
                    newWorld.addClickedOrganism(pos)
                    newWorld.drawWindow(WIN)
                elif pos[0] > newWorld.getWorldWidth()*20 and pos[1] > newWorld.getWorldHeight()*10:
                    # Change the world type
                    newWorld.handleChangeTheWorldType(pos, WIN)
                    newWorld.drawWindow(WIN)
                    newWorld.setLastClick()
                else:
                    newWorld.setLastClick()
    pygame.quit()

if __name__ == "__main__":
    main()