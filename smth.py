from pygame_functions import *
import random
from collections import deque
from units_and_buildings import *
#from numba import *
import numpy as np
screenSize(1000, 730)
setBackgroundColour((43, 94, 65))
setAutoUpdate(0)
text = makeTextBox(0, 450, 1000, fontSize=20)
showTextBox(text)
'''
wood = "wood.png"
rock = "rock.png"
owl = "owl.png"
bush = "bush.png"
warriorowl = "warriorowl.png"
tree = "tree.png"
warriortree = "warriortree.png"
storage = "storage.png"
pebble = "pebble.png"
branch = "branch.png"
berry = "berries.png"
menu = "menu.png"
sawmill = "sawmill.png"
quarry = "quarry.png"
'''
wood = "Desktop/project folder/wood.png"
rock = "Desktop/project folder/rock.png"
owl = "Desktop/project folder/owl.png"
bush="Desktop/project folder/bush.png"
warriorowl="Desktop/project folder/warriorowl.png"
tree="Desktop/project folder/tree.png"
warriortree="Desktop/project folder/warriortree.png"
storage="Desktop/project folder/storage.png"
pebble="Desktop/project folder/pebble.png"
branch="Desktop/project folder/branch.png"
berry="Desktop/project folder/berries.png"
menu="Desktop/project folder/menu.png"
sawmill = "Desktop/project folder/sawmill.png"
quarry = "Desktop/project folder/quarry.png"
fpsDisplay = makeLabel("FPS:", 30, 10, 10, "white")
showLabel(fpsDisplay)
xPositon = 500
yPosition = 320
menustorage = makeSprite(storage)
menustorage.clickability = 0
menumainhall = makeSprite(tree)
menumainhall.clickability = 0
menuforge = makeSprite(warriortree)
menuforge.clickability = 0
menusawmill = makeSprite(sawmill)
menusawmill.clickability = 0
menuquarry = makeSprite(quarry)
menuquarry.clickability = 0
menusprite = makeSprite(menu)
menuowl = makeSprite(owl)
menuowl.clickability = 0
menuwarrior = makeSprite(warriorowl)
menuwarrior.clickability = 0
moveSprite(menusprite, 700, 70)
moveSprite(menustorage, 725, 100)
moveSprite(menumainhall, 825, 100)
moveSprite(menuforge, 925, 100)
moveSprite(menusawmill, 725, 250)
moveSprite(menuquarry, 825, 250)
moveSprite(menuowl, 925, 250)
moveSprite(menuwarrior, 725, 400)
showSprite(menusprite)
showSprite(menustorage)
showSprite(menumainhall)
showSprite(menuforge)
showSprite(menusawmill)
showSprite(menuquarry)
showSprite(menuowl)
showSprite(menuwarrior)
hideSprite(menusprite)
hideSprite(menustorage)
hideSprite(menumainhall)
hideSprite(menuforge)
hideSprite(menusawmill)
hideSprite(menuquarry)
hideSprite(menuowl)
hideSprite(menuwarrior)
pebbleicon = makeSprite(pebble)
branchicon = makeSprite(branch)
berryicon = makeSprite(berry)
moveSprite(pebbleicon, 210, 10)
moveSprite(branchicon, 310, 10)
moveSprite(berryicon, 410, 10)
pos = (500, 300)
def main():
    labelpebble = makeLabel("0", 30, 250, 10, "white")
    lableberry = makeLabel("0", 30, 450, 10, "white")
    labelbranch = makeLabel("0", 30, 350, 10, "white")
    nextFrame_woods = clock()
    nextFrame_rocks = clock()
    bushes = np.array([],dtype=object)
    woods = np.array([],dtype=object)
    rocks = np.array([],dtype=object)
    pebbles = np.array([],dtype=object)
    branches = np.array([],dtype=object)
    normalunits = deque()
    storages = deque()
    sawmills = deque()
    quarries = deque()
    warriors = deque()
    allspries=np.array([])
    forges=np.array([],dtype=object)
    mainhalls=np.array([],dtype=object)
    allspries = np.append(allspries,[mainhalls,forges,warriors,quarries,sawmills,storages,normalunits,branches,pebbles,rocks,woods,bushes])
    for x in range(300):
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
    def menu():
        for pebl in pebbles:
            if pebl.xpos >= 640 and pebl.xpos<=1100  and pebl.ypos >= 0 and pebl.ypos<=450:
                if pebl.hp[0] <= 0:
                    killSprite(pebl.building)
                else:
                    hideSprite(pebl.building)
        for rck in rocks:
            if rck.xpos >= 640 and rck.xpos<=1100  and rck.ypos >= 0 and rck.ypos<=450:
                if rck.hp[0] <= 0:
                    killSprite(rck.building)
                else:
                    hideSprite(rck.building)
        for bsh in bushes:
            if bsh.xpos >= 640 and bsh.xpos<=1100  and bsh.ypos >= 0 and bsh.ypos<=450:
                if bsh.hp[0] <= 0:
                    killSprite(bsh.building)
                else:
                    hideSprite(bsh.building)
        for wds in woods:
            if wds.xpos >= 640 and wds.xpos<=1100  and wds.ypos >= 0 and wds.ypos<=450:
                if wds.hp[0] <= 0:
                    killSprite(wds.building)
                else:
                    hideSprite(wds.building)
        for brnch in branches:
            if brnch.xpos >= 640 and brnch.xpos<=1100  and brnch.ypos >= 0 and brnch.ypos<=450:
                if brnch.hp[0] <= 0:
                    killSprite(brnch.building)
                else:
                    hideSprite(brnch.building)
        showSprite(menusprite)
        showSprite(menustorage)
        showSprite(menumainhall)
        showSprite(menuforge)
        showSprite(menusawmill)
        showSprite(menuquarry)
        showSprite(menuowl)
        showSprite(menuwarrior)
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
    while True:

        pos2=pygame.mouse.get_pos()
        if drawmenu == 0:
            menu()
            menustorage.clickability = 1
            menumainhall.clickability = 1
            menuforge.clickability = 1
            menusawmill.clickability = 1
            menuquarry.clickability = 1
            menuowl.clickability = 1
            menuwarrior.clickability = 1
        elif drawmenu == 1:
            menustorage.clickability = 0
            menumainhall.clickability = 0
            menuforge.clickability = 0
            menusawmill.clickability = 0
            menuquarry.clickability = 0
            menuowl.clickability = 0
            menuwarrior.clickability = 0
            for pebl in pebbles:
                if pebl.xpos >= 640 and pebl.xpos<=1100  and pebl.ypos >= 0 and pebl.ypos<=450:
                    if pebl.hp[0] <= 0:
                        killSprite(pebl.building)
                    else:
                        showSprite(pebl.building)
            for rck in rocks:
                if rck.xpos >= 640 and rck.xpos<=1100  and rck.ypos >= 0 and rck.ypos<=450:
                    if rck.hp[0] <= 0:
                        killSprite(rck.building)
                    else:
                        showSprite(rck.building)
            for bsh in bushes:
                if bsh.xpos >= 640 and bsh.xpos<=1100  and bsh.ypos >= 0 and bsh.ypos<=450:
                    if bsh.hp[0] <= 0:
                        killSprite(bsh.building)
                    else:
                        showSprite(bsh.building)
            for wds in woods:
                if wds.xpos >= 640 and wds.xpos<=1100  and wds.ypos >= 0 and wds.ypos<=450:
                    if wds.hp[0] <= 0:
                        killSprite(wds.thissprie)
                    else:
                        showSprite(wds.building)
            for brnch in branches:
                if brnch.xpos >= 640 and brnch.xpos<=1100  and brnch.ypos >= 0 and brnch.ypos<=450:
                    if brnch.hp[0] <= 0:
                        killSprite(brnch.thissprie)
                    else:
                        showSprite(brnch.building)
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
        fps = tick(100)
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
                        pos[0]+=-0.012*pos2[0]+6
                        pos[1]+=-0.01643835616438356*pos2[1]+6
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
