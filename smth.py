from pygame_functions import *
import random
from collections import deque
from units_and_buildings import *
screenSize(1000, 1000)
setBackgroundColour("blue")
drawRect(0,450,1000,280,"black")
setAutoUpdate(0)
text=makeTextBox(0,450,1000,fontSize=20)
showTextBox(text)
storage="storage.png"
owl = "owl.png"
bush="bush.png"
warriorowl="warriorowl.png"
tree="tree.png"
warriortree="warriortree.png"
rock = "rock.png"
wood = "wood.png"
fpsDisplay = makeLabel("FPS:",30,10,10,"white")
showLabel(fpsDisplay)
xPositon = 500
yPosition = 320
nextframe = clock()
normalunits=deque()
warriors=deque()
def create_random_env(spritename,secondspritename,hp,collectability):
    thissprite = makeSprite(spritename)
    addSpriteImage(thissprite, secondspritename)
    thissprite.x = random.random()*1000-30
    thissprite.y = random.random()*375-20
    thissprite.collectability=collectability
    thissprite.hp=hp
    moveSprite(thissprite, thissprite.x, thissprite.y)
    showSprite(thissprite)
    return thissprite

def main():
    bushes = []
    woods=[]
    rocks=[]
    for x in range(10):
        envbush=create_random_env(bush,"bushcollected.png",20,0)
        bushes.append(envbush)
        envwood=create_random_env(wood,"woodcollected.png",100,1)
        woods.append(envwood)
        envrock=create_random_env(rock,"rockcollected.png",400,1)
        rocks.append(envrock)
    owlunit1=units.normal_unit(xPositon,yPosition)
    normalunits.append(owlunit1)
    acounter = False
    mainhall = False
    storages = deque()
    sawmills = deque()
    while True:
        if keyPressed("0"):
            acounter=False
            normalunits.rotate(1)
            pause(200)
        if keyPressed("9"):
            acounter=True
            warriors.rotate(1)
            pause(200)
        if keyPressed("8"):
            storages.rotate(1)
            stsign=makeSprite(owl)
            moveSprite(stsign,storages[0].x,storages[0].y+50)
            showSprite(stsign)
            pause(300)
            hideSprite(stsign)
        if keyPressed("7"):
            if storages[0].berry>=3:
                normalunits.append(mh.born_normal_unit())
                storages[0].berry-=3
                pause(200)
        if keyPressed("6"):
            warriors.append(forge.born_warrior())
            pause(200)
        if  not acounter :
            normalunits[0].move()
            if keyPressed("1"):
                normalunits[0].harvest(bushes)
            if keyPressed("3"):
                normalunits[0].put_res(storages[0])
            if keyPressed("2"):
                sg = buildings.storage(normalunits[0])
                storages.append(sg.build())
                pause(200)
            if keyPressed("n"):
                sw = buildings.sawmill(normalunits[0])
                sawmills.append(sw.build()[0])
                sw.sawing(woods)
                if woods[0] == 100:
                    changeSpriteImage(woods[0],1)
                pause(200)

            if keyPressed("4"):
                if not mainhall:
                    mh=buildings.main_hall(normalunits[0])
                    mh.build()
                    pause(500)
                    mainhall=True
            if keyPressed("5"):
                forge=buildings.forge(normalunits[0])
                forge.build()
                pause(500)
        if acounter:
            warriors[0].move()
            if keyPressed("k"):
                warriors[0].attack()
                pause(200)
        fps= tick(60)
        changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
        updateDisplay()
    endWait()

if __name__ == '__main__':
    main()
