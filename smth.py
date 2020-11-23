from pygame_functions import *
import random
from collections import deque
from units_and_buildings import *
screenSize(1000, 1000)
setBackgroundColour((43,94,65))
drawRect(0,450,1000,280,"black")
setAutoUpdate(0)
text=makeTextBox(0,450,1000,fontSize=20)
showTextBox(text)

wood = "wood.png"
rock = "rock.png"
owl = "owl.png"
bush="bush.png"
warriorowl="warriorowl.png"
tree="tree.png"
warriortree="warriortree.png"
storage="storage.png"
pebble="pebble.png"
branch="branch.png"
berry="berries.png"
menu="menu.png"
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
'''
fpsDisplay = makeLabel("FPS:",30,10,10,"white")
showLabel(fpsDisplay)
xPositon = 500
yPosition = 320
menustorage=makeSprite(storage)
menustorage.clickability = 0
menumainhall=makeSprite(tree)
menumainhall.clickability = 0
menuforge=makeSprite(warriortree)
menuforge.clickability = 0
menusawmill=makeSprite(sawmill)
menusawmill.clickability = 0
menuquarry=makeSprite(quarry)
menuquarry.clickability = 0
menusprite=makeSprite(menu)
menuowl=makeSprite(owl)
menuowl.clickability = 0
menuwarrior=makeSprite(warriorowl)
menuwarrior.clickability = 0
moveSprite(menusprite,700,70)
moveSprite(menustorage,725,100)
moveSprite(menumainhall,825,100)
moveSprite(menuforge,925,100)
moveSprite(menusawmill,725,250)
moveSprite(menuquarry,825,250)
moveSprite(menuowl,925,250)
moveSprite(menuwarrior,725,400)
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
normalunits=deque()
warriors=deque()
pebbleicon=makeSprite(pebble)
branchicon=makeSprite(branch)
berryicon=makeSprite(berry)
moveSprite(pebbleicon,210,10)
moveSprite(branchicon,310,10)
moveSprite(berryicon,410,10)
pos=(0,0)

def create_random_env(spritename,secondspritename,hp,collectability):
    thissprite = makeSprite(spritename)
    addSpriteImage(thissprite, secondspritename)
    thissprite.x = random.random()*1000-30
    thissprite.y = random.randrange(100,370)
    thissprite.collectability=collectability
    thissprite.hp=hp
    moveSprite(thissprite, thissprite.x, thissprite.y)
    showSprite(thissprite)
    return thissprite

def main():
    labelpebble=makeLabel("0",30,250,10,"white")
    lableberry=makeLabel("0",30,450,10,"white")
    labelbranch=makeLabel("0",30,350,10,"white")
    nextFrame_woods = clock()
    nextFrame_rocks = clock()
    bushes = []
    woods=[]
    rocks=[]
    pebbles=[]
    branches=[]
    for x in range(11):
        envbush=create_random_env(bush,"bushcollected.png",20,0)
        #Desktop/project folder/
        bushes.append(envbush)
        envwood=create_random_env(wood,"woodcollected.png",100,0)
        woods.append(envwood)
        envrock=create_random_env(rock,"rockcollected.png",400,0)
        rocks.append(envrock)
        envpebble=create_random_env(pebble,pebble,20,0)
        pebbles.append(envpebble)
        envbranch=create_random_env(branch,branch,20,0)
        branches.append(envbranch)
    def menu():
        unhideAll()
        for pebl in pebbles:
            if pebl.x>=640:
                hideSprite(pebl)
        for rck in rocks:
            if rck.x>=640:
                hideSprite(rck)
        for bsh in bushes:
            if bsh.x>=640:
                hideSprite(bsh)
        for wds in woods:
            if wds.x>=640:
                hideSprite(wds)
        for brnch in branches:
            if brnch.x>=640:
                hideSprite(brnch)
    owlunit1=units.normal_unit(xPositon,yPosition)
    normalunits.append(owlunit1)
    warrior1=units.warrior(xPositon+100,yPosition+100)
    warriors.append(warrior1)
    acounter = False
    mainhall = False
    storages = deque()
    sawmills = deque()
    quarries = deque()
    drawmenu=1
    pos=(0,0)
    while True:
        if drawmenu==0:
            menu()
            menustorage.clickability = 1
            menumainhall.clickability =1
            menuforge.clickability =1
            menusawmill.clickability = 1
            menuquarry.clickability = 1
            menuowl.clickability = 1
            menuwarrior.clickability = 1
        elif drawmenu==1:
            menustorage.clickability = 0
            menumainhall.clickability =0
            menuforge.clickability =0
            menusawmill.clickability = 0
            menuquarry.clickability = 0
            menuowl.clickability = 0
            menuwarrior.clickability = 0

            for pebl in pebbles:
                if pebl.x>=640 and pebl.collectability==0:
                    showSprite(pebl)
                for rck in rocks:
                    if rck.x>=640 and rck.collectability==0:
                        showSprite(rck)
                for bsh in bushes :
                    if bsh.x>=640 and bsh.collectability==0:
                        showSprite(bsh)
                for wds in woods:
                    if wds.x>=640 and wds.collectability==0: 
                        showSprite(wds)
                for brnch in branches :
                    if brnch.x>=640 and brnch.collectability==0:
                        showSprite(brnch)
            hideSprite(menusprite)
            hideSprite(menustorage)
            hideSprite(menumainhall)
            hideSprite(menuforge)
            hideSprite(menusawmill)
            hideSprite(menuquarry)
            hideSprite(menuowl)
            hideSprite(menuwarrior)
            drawmenu+=1
        drawRect(175,0,830,60,(102,0,204))
        showSprite(pebbleicon)
        showSprite(branchicon)
        showSprite(berryicon)
        showLabel(labelpebble)
        showLabel(lableberry)
        showLabel(labelbranch)
        mainloopwoods=0
        mainlooprocks=0
        mainloopberries=0
        
        if keyPressed("0"):
            try:
                sawmills.rotate(1)
                stsign = makeSprite(owl)
                moveSprite(stsign, sawmills[0].xPos, sawmills[0].yPos + 50)
                showSprite(stsign)
                pause(200)
                hideSprite(stsign)
            except:
                errorlabel=makeLabel("ты еще не строил лесопилок",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if keyPressed("q"):
            drawmenu=0
        if keyPressed("l"):
            drawmenu=1
        mouseState = pygame.mouse.get_pressed()    
        if mouseState[0]:
            pos = (pygame.mouse.get_pos()[0]-30,pygame.mouse.get_pos()[1]-30)
        if keyPressed("r"):
            try:
                acounter=False
                normalunits.rotate(1)
                pause(200)
            except:
                errorlabel=makeLabel("ты еще не создавал рабочих",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)

        if keyPressed("9"):
            acounter=True
            warriors.rotate(1)
            pause(200)
        if keyPressed("8"):
            try:
                storages.rotate(1)
                stsign=makeSprite(owl)
                moveSprite(stsign,storages[0].x,storages[0].y+50)
                showSprite(stsign)
                pause(300)
                hideSprite(stsign)
            except:
                errorlabel=makeLabel("ты еще не построил склад",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if spriteClicked(menuowl) and menuowl.clickability:
            try:
                if storages[0].berry>=3 and mainhall:
                    normalunits.append(mh.born_normal_unit())
                    storages[0].berry-=3
                    pause(200)
            except:
                errorlabel=makeLabel("ты еще не построил склад или мэинхол",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if spriteClicked(menuwarrior) and menuwarrior.clickability:
            try:
                if  storages[0].rock>=1:
                        storages[0].rock-=1
                        warriors.append(forge.born_warrior())
                        pause(200)
            except:
                errorlabel=makeLabel("ты еще не построил кузницу",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if  not acounter :
            normalunits[0].move()
            try:
                if keyPressed("3"):
                    normalunits[0].put_res(storages[0])
            except:
                errorlabel=makeLabel("ты еще не построил склад",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
            if spriteClicked(menustorage)and menustorage.clickability:
                try:
                    if normalunits[0].wood>=1:
                        normalunits[0].wood-=1
                        sg = buildings.storage(normalunits[0])
                        storages.append(sg.build())
                        pause(200)
                    elif storages[0].wood>=1:
                        storages[0].wood-=1
                        sg = buildings.storage(normalunits[0])
                        storages.append(sg.build())
                        pause(200)
                    

                except:
                    pass
            if spriteClicked(menusawmill) and menusawmill.clickability:
                try:
                    if  storages[0].wood>=2:
                        storages[0].wood-=2
                        sawmills.append(buildings.sawmill(normalunits[0],woods))
                        #buildings.sawmill(normalunits[0]).sawing(woods)
                        nextFrame_woods =clock() + 5000
                        pause(200)
                except:
                    pass
            if spriteClicked(menuquarry)and menuquarry.clickability:
                try:
                    if  storages[0].wood>=2 and storages[0].rock>=2:
                        storages[0].wood-=2
                        storages[0].rock-=2
                        quarries.append(buildings.quarry(normalunits[0],rocks))
                        #buildings.sawmill(normalunits[0]).sawing(woods)
                        nextFrame_rocks = clock() + 5000
                        pause(200)
                except:
                    pass
            if spriteClicked(menumainhall) and menumainhall.clickability:
                if not mainhall:
                    try:
                        if  storages[0].wood>=4:
                            storages[0].wood-=4
                            mh=buildings.main_hall(normalunits[0])
                            mh.build()
                            pause(500)
                            mainhall=True
                    except:
                        pass
            if spriteClicked(menuforge)and menuforge.clickability:
                try:
                    if storages[0].rock>=4 and storages[0].wood>=3:
                        storages[0].rock-=4
                        storages[0].wood-=3
                        forge=buildings.forge(normalunits[0])
                        forge.build()
                        pause(500)
                except:
                    pass
        if acounter:
            try:
                warriors[0].move()
                if keyPressed("k"):
                    warriors[0].attack()
                    pause(200)
            except:
                errorlabel=makeLabel("ты еще не обучил воинов",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if len(sawmills):
           # print("Pudge is not happy")
            if clock() >= nextFrame_woods:
                sawmills[0].sawing()
                nextFrame_woods += 200
        if len(quarries) and len(quarries[0].near_stones):
            if clock() >= nextFrame_rocks:
                quarries[0].stonecutting()
                nextFrame_rocks += 200
        fps= tick(60)
        changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
        for mainloopstorage in storages:
            mainloopberries+=mainloopstorage.berry
            mainloopwoods+=mainloopstorage.wood
            mainlooprocks+=mainloopstorage.rock



        try:
            changeLabel(labelpebble,str(mainlooprocks))
            changeLabel(labelbranch,str(mainloopwoods))
            changeLabel(lableberry,str(mainloopberries))
        except:
            pass


        if not acounter:
            normalunits[0].goto(pos[0],pos[1])
            if abs(normalunits[0].xpos-pos[0])<=3.2 and abs(normalunits[0].ypos-pos[1])<=3.1:
                normalunits[0].get(sawmills,bushes,quarries,pebbles,branches)
        else:
            warriors[0].goto(pos[0],pos[1])
        updateDisplay()

    endWait()

if __name__ == '__main__':
    main()
