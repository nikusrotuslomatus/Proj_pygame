from pygame_functions import *
import random
from collections import deque
from units_and_buildings import *
import environment
a=environment.start()
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
    for x in range(10):
        envbush=create_random_env(a.bush,"Desktop/project folder/bushcollected.png",20,0)
        bushes.append(envbush)
        envwood=create_random_env(a.wood,"Desktop/project folder/woodcollected.png",100,0)
        woods.append(envwood)
        envrock=create_random_env(a.rock,"Desktop/project folder/rockcollected.png",400,0)
        rocks.append(envrock)
        envpebble=create_random_env(a.pebble,a.pebble,20,0)
        pebbles.append(envpebble)
        envbranch=create_random_env(a.branch,a.branch,20,0)
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
    owlunit1=units.normal_unit(a.xPositon,a.yPosition)
    a.normalunits.append(owlunit1)
    warrior1=units.warrior(a.xPositon+100,a.yPosition+100)
    a.warriors.append(warrior1)
    acounter = False
    mainhall = False
    storages = deque()
    sawmills = deque()
    quarries = deque()
    drawmenu=False
    while True:
        if drawmenu:
            menu()
        else:
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
            hideSprite(a.menusprite)
            hideSprite(a.menustorage)
            hideSprite(a.menumainhall)
            hideSprite(a.menuforge)
            hideSprite(a.menusawmill)
            hideSprite(a.menuquarry)
            hideSprite(a.menuowl)
            hideSprite(a.menuwarrior)
        drawRect(175,0,830,60,(102,0,204))
        showSprite(a.pebbleicon)
        showSprite(a.branchicon)
        showSprite(a.berryicon)
        showLabel(labelpebble)
        showLabel(lableberry)
        showLabel(labelbranch)
        mainloopwoods=0
        mainlooprocks=0
        mainloopberries=0
        if keyPressed("0"):
            try:
                sawmills.rotate(1)
                stsign = makeSprite(a.owl)
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
            drawmenu=True
        if keyPressed("l"):
            drawmenu=False
            
        if keyPressed("r"):
            try:
                acounter=False
                a.normalunits.rotate(1)
                pause(200)
            except:
                errorlabel=makeLabel("ты еще не создавал рабочих",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if keyPressed("9"):
            acounter=True
            a.warriors.rotate(1)
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
        if spriteClicked(a.menuowl):
            try:
                if storages[0].berry>=3 and mainhall:
                    a.normalunits.append(mh.born_normal_unit())
                    storages[0].berry-=3
                    pause(200)
            except:
                errorlabel=makeLabel("ты еще не построил склад или мэинхол",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if spriteClicked(a.menuwarrior):
            try:
                if  storages[0].rock>=1:
                        storages[0].rock-=1
                        a.warriors.append(forge.born_warrior())
                        pause(200)
            except:
                errorlabel=makeLabel("ты еще не построил кузницу",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
        if  not acounter :
            a.normalunits[0].move()
            try:
                if keyPressed("1"):
                    a.normalunits[0].get(sawmills,bushes,quarries,branches,pebbles)
            except:
                pass
            try:
                if keyPressed("3"):
                    a.normalunits[0].put_res(storages[0])
            except:
                errorlabel=makeLabel("ты еще не построил склад",50,30,30)
                showLabel(errorlabel)
                pause(1000)
                hideLabel(errorlabel)
            if spriteClicked(a.menustorage):
                try:
                    if a.normalunits[0].wood>=1:
                        a.normalunits[0].wood-=1
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
            if spriteClicked(a.menusawmill):
                try:
                    if  storages[0].wood>=2:
                        storages[0].wood-=2
                        sawmills.append(buildings.sawmill(normalunits[0],woods))
                        #buildings.sawmill(normalunits[0]).sawing(woods)
                        nextFrame_woods =clock() + 5000
                        pause(200)
                except:
                    pass
            if spriteClicked(a.menuquarry):
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
            if spriteClicked(a.menumainhall):
                if not mainhall:
                    try:
                        if  storages[0].wood>=4:
                            storages[0].wood-=4
                            mh=buildings.main_hall(a.normalunits[0])
                            mh.build()
                            pause(500)
                            mainhall=True
                    except:
                        pass
            if spriteClicked(a.menuforge):
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
                a.warriors[0].move()
                if keyPressed("k"):
                    a.warriors[0].attack()
                    pause(200)
            except:
                errorlabel=makeLabel("ты еще не обучил воинов",50,30,30)
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
        fps= tick(60)
        changeLabel(a.fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
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
        updateDisplay()

    endWait()

if __name__ == '__main__':
    main()
