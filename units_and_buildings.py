from pygame_functions import *
import random
from collections import deque
from units_and_buildings import *
from environment import *
#from numba import *
import numpy as np
def main():
    global labelpebble,lableberry,labelbranch,nextFrame_woods,nextFrame_rocks,bushes,woods,rocks,pebbles,branches,normalunits,storages,sawmills,quarries,warriors,allspries,forges,mainhalls 
    for x in range(200):
        envbush = buildings.environment(bush, "Desktop/project folder/bushcollected.png", [20], 0)
        # Desktop/project folder/
        bushes=np.append(bushes,envbush)
        envwood = buildings.environment(wood, "Desktop/project folder/woodcollected.png", [100], 0)
        woods=np.append(woods,envwood)
        envrock = buildings.environment(rock, "Desktop/project folder/rockcollected.png", [400], 0)
        rocks=np.append(rocks,envrock)
        envpebble = buildings.environment(pebble, pebble, [20], 0)
        pebbles=np.append(pebbles,envpebble)
        envbranch = buildings.environment(branch, branch, [20], 0)
        branches=np.append(branches,envbranch)
    owlunit1 = units.normal_unit(xPositon, yPosition)
    normalunits.append(owlunit1)
    warrior1 = units.warrior(xPositon + 100, yPosition + 100)
    warriors.append(warrior1)
    acounter = False
    mainhall = False   
    drawmenu = 1
    pos = (500, 500)
    xmovescreen=0
    ymovescreen=0
    menudrawn=False
    while True:

        pos2=pygame.mouse.get_pos()
        if not menudrawn:
            if drawmenu == 0:
                menu()
                menustorage.clickability = 1
                menumainhall.clickability = 1
                menuforge.clickability = 1
                menusawmill.clickability = 1
                menuquarry.clickability = 1
                menuowl.clickability = 1
                menuwarrior.clickability = 1
                menudrawn=True
        if drawmenu == 1:
            menustorage.clickability = 0
            menumainhall.clickability = 0
            menuforge.clickability = 0
            menusawmill.clickability = 0
            menuquarry.clickability = 0
            menuowl.clickability = 0
            menuwarrior.clickability = 0
            menu(closing=True)
            hideSprite(menusprite)
            hideSprite(menustorage)
            hideSprite(menumainhall)
            hideSprite(menuforge)
            hideSprite(menusawmill)
            hideSprite(menuquarry)
            hideSprite(menuowl)
            hideSprite(menuwarrior)
            drawmenu += 1
        drawRect(175, 0, 830, 60, (102, 0, 204))
        showSprite(pebbleicon)
        showSprite(branchicon)
        showSprite(berryicon)
        showLabel(labelpebble)
        showLabel(lableberry)
        showLabel(labelbranch)
        mainloopwoods = 0
        mainlooprocks = 0
        mainloopberries = 0
        if keyPressed("0"):
            try:
                sawmills.rotate(1)
                stsign = makeSprite(owl)
                moveSprite(stsign, sawmills[0].xpos, sawmills[0].ypos + 50)
                showSprite(stsign)
                pause(200)
                hideSprite(stsign)
            except Exception as e:
                print(e)
                errorlabel = makeLabel("ты еще не строил лесопилок", 50, 30, 30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if keyPressed("q"):
            drawmenu = 0
            menudrawn=False
        if keyPressed("l"):
            drawmenu = 1
        mouseState = pygame.mouse.get_pressed()
        if mouseState[0] and keyPressed("space"):
            pos = [pygame.mouse.get_pos()[0] - 30, pygame.mouse.get_pos()[1] - 30]
            normalunits[0].havecome=False
        if not acounter:
            if not normalunits[0].havecome:
                normalunits[0].goto(pos[0], pos[1])
                if abs(normalunits[0].xpos - pos[0]) <= 3.2 and abs(normalunits[0].ypos - pos[1]) <= 3.1:
                    normalunits[0].get(sawmills, bushes, quarries, pebbles, branches)
        elif acounter:
            warriors[0].goto(pos[0]-xmovescreen, pos[1]-ymovescreen)
            if abs(warriors[0].xpos - pos[0]) <= 3.2 and abs(warriors[0].ypos - pos[1]) <= 3.1:
                warriors[0].attack()
        if keyPressed("r"):
            try:
                acounter = False
                normalunits.rotate(1)
                pause(200)
            except Exception as e:
                print(e)
                errorlabel = makeLabel("ты еще не создавал рабочих", 50, 30, 30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if keyPressed("9"):
            acounter = True
            warriors.rotate(1)
            pause(200)
        if keyPressed("8"):
            try:
                storages.rotate(1)
                stsign = makeSprite(owl)
                moveSprite(stsign, storages[0].xpos, storages[0].ypos + 50)
                showSprite(stsign)
                pause(300)
                hideSprite(stsign)
            except Exception as e:
                print(e)
                errorlabel = makeLabel("ты еще не построил склад", 50, 30, 30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if spriteClicked(menuowl) and menuowl.clickability:
            try:
                if normalunits[0].hp[0] > 0:
                    if storages[0].berry >= 3 and mainhall:
                        normalunits.append(mh.born_normal_unit())
                        storages[0].berry -= 3
                        pause(200)
            except Exception as e:
                print(e)
                errorlabel = makeLabel("ты еще не построил склад или мэинхол", 50, 30, 30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if spriteClicked(menuwarrior) and menuwarrior.clickability:
            try:
                if normalunits[0].hp[0] > 0:
                    if storages[0].rock >= 1:
                        storages[0].rock -= 1
                        warriors.append(forges[0].born_warrior())
                        pause(200)
            except Exception as e:
                print(e)
                errorlabel = makeLabel("ты еще не построил кузницу", 50, 30, 30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if not acounter:
            normalunits[0].move()
            try:
                if keyPressed("3"):
                    normalunits[0].put_res(storages[0])
            except Exception as e:
                print(e)
                errorlabel = makeLabel("ты еще не построил склад", 50, 30, 30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
            if spriteClicked(menustorage) and menustorage.clickability:
                try:
                    if normalunits[0].hp[0] > 0:
                        if normalunits[0].wood >= 1:
                            normalunits[0].wood -= 1
                            sg = buildings.storage(normalunits[0])
                            storages.append(sg)
                            pause(200)
                        elif storages[0].wood >= 1:
                            storages[0].wood -= 1
                            sg = buildings.storage(normalunits[0])
                            storages.append(sg.build())
                            pause(200)
                except Exception as e:
                    print(e)
            if spriteClicked(menusawmill) and menusawmill.clickability:
                try:
                    if normalunits[0].hp[0] > 0:
                        if storages[0].wood >= 2:
                            storages[0].wood -= 2
                            sawmills.append(buildings.sawmill(normalunits[0], woods))
                            nextFrame_woods = clock() + 5000
                            pause(200)
                except Exception as e:
                    print(e)
            if spriteClicked(menuquarry) and menuquarry.clickability:
                try:
                    if normalunits[0].hp[0] > 0:
                        if storages[0].wood >= 2 and storages[0].rock >= 2:
                            storages[0].wood -= 2
                            storages[0].rock -= 2
                            quarries.append(buildings.quarry(normalunits[0], rocks))
                            nextFrame_rocks = clock() + 5000
                            pause(200)
                except Exception as e:
                    print(e)
            if spriteClicked(menumainhall) and menumainhall.clickability:
                if not mainhall:
                    try:
                        if normalunits[0].hp[0] > 0:
                            if storages[0].wood >= 4:
                                storages[0].wood -= 4
                                mh = buildings.main_hall(normalunits[0])
                                mainhalls=np.append(mainhalls,mh)
                                pause(500)
                                mainhall = True
                    except Exception as e:
                        print(e)
            if spriteClicked(menuforge) and menuforge.clickability:
                try:
                    if normalunits[0].hp[0] > 0:
                        if storages[0].rock >= 4 and storages[0].wood >= 3:
                            storages[0].rock -= 4
                            storages[0].wood -= 3
                            myforge = buildings.forge(normalunits[0])
                            forges=np.append(forges,myforge)
                            pause(500)
                except Exception as e:
                    print(e)
               
        elif acounter:
            try:
                warriors[0].move()
            except Exception as e:
                print(e)
                errorlabel = makeLabel("Вы еще не готовы атаковать эту цель", 50, 30, 30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if len(sawmills):
            if clock() >= nextFrame_woods:
                sawmills[0].sawing()
                nextFrame_woods += 200
        if len(quarries) and len(quarries[0].near_stones):
            if clock() >= nextFrame_rocks:
                quarries[0].stonecutting()
                nextFrame_rocks += 200
        fps = tick(3000)
        changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
        for mainloopstorage in storages:
            mainloopberries += mainloopstorage.berry
            mainloopwoods += mainloopstorage.wood
            mainlooprocks += mainloopstorage.rock
        try:
            changeLabel(labelpebble, str(mainlooprocks))
            changeLabel(labelbranch, str(mainloopwoods))
            changeLabel(lableberry, str(mainloopberries))
        except Exception as e:
            print(e)
        if keyPressed("space"):
            if pos2[0] <=5 or pos2[0] >= 995 or pos2[1] <=5 or pos2[1] >= 725:
                allspries = np.array([mainhalls,forges,warriors,quarries,sawmills,storages,normalunits,branches,pebbles,rocks,woods,bushes])
                for listsprite in allspries:
                    for sprite in listsprite:
                        sprite.movescreen(-0.012*pos2[0]+6,-0.01643835616438356*pos2[1]+6)
                        if sprite.xpos<=-100 or sprite.xpos>=1100 or sprite.ypos<=-100 or sprite.ypos>=410:
                            hideSprite(sprite.building)
                        else:
                            showSprite(sprite.building)

        drawRect(0, 450, 1000, 280, "black")
        updateDisplay()
        if keyPressed("esc"):
            endWait()
if __name__ == '__main__':
    main()
