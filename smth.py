from pygame_functions import *
import random
from collections import deque
screenSize(1000, 1000)
setBackgroundColour("blue")
drawRect(0,450,1000,280,"black")
setAutoUpdate(10)
text=makeTextBox(0,450,1000,fontSize=20)
showTextBox(text)
owl = "Desktop/project folder/owl.png"
bush="Desktop/project folder/bush.png"
warriorowl="Desktop/project folder/warriorowl.png"
tree="Desktop/project folder/tree.png"
fpsDisplay = makeLabel("FPS:",30,10,10,"white")
showLabel(fpsDisplay)
xPositon = 500
yPosition = 320
nextframe = clock()
normalunits=deque()
warriors=[]
def iscollectible(x):
    if x.collectability==0:
        return True
    else:
        return False
class units(object):
    class normal_unit(object):
        def __init__(self,xpos,ypos):
            self.xpos=xpos
            self.ypos=ypos
            self.speed=3
            self.sprite=makeSprite(owl)
            self.berry=0
            showSprite(self.sprite)
        def move(self):
            if keyPressed("left"):
                self.xpos -= self.speed
            elif keyPressed("right"):
                self.xpos += self.speed
            if keyPressed("up"):
                self.ypos -= self.speed
            elif keyPressed("down"):
                self.ypos += self.speed
            moveSprite(self.sprite, self.xpos, self.ypos)
        def harvest(self):
            collectibles=allTouching(self.sprite)
            for collectible in collectibles:
                if collectible in bushes and iscollectible(collectible):
                    changeSpriteImage(collectible,1)
                    self.berry+=1
                    collectible.collectability=1
        def put_res(self):
            reslabel=makeLabel("ты положил "+str(self.berry)+" ягод на склад",50,30,30)
            showLabel(reslabel)
            self.berry=0
            pause(1000)
            hideLabel(reslabel)
    class warrior(normal_unit):
        def __init__(self,xpos,ypos):
            self.xpos=xpos
            self.ypos=ypos
            self.speed=3
            self.sprite=makeSprite(warriorowl)
            showSprite(self.sprite)
        def move(self):
            if keyPressed("left"):
                self.xpos -= self.speed
            elif keyPressed("right"):
                self.xpos += self.speed
            if keyPressed("up"):
                self.ypos -= self.speed
            elif keyPressed("down"):
                self.ypos += self.speed
            moveSprite(self.sprite, self.xpos, self.ypos)
        def attack(self):
            enemies=allTouching(self.sprite)
            for enemy in enemies:
                killSprite(enemy)
class buildings(object):
    class main_hall(object):
        global normalunits
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
        def build(self):
            building=makeSprite(tree)
            moveSprite(building,self.xPos,self.yPos)
            showSprite(building)
        def born_normal_unit(self):
            normunit=units.normal_unit(self.xPos,self.yPos)
            normalunits.append(normunit)
bushes = []
for x in range(10):
    thisbush = makeSprite("Desktop/project folder/bush.png")
    addSpriteImage(thisbush, "Desktop/project folder/bushcollected.png")
    thisbush.x = random.randint(0,1000)
    thisbush.y = random.randint(0,375)
    thisbush.collectability=0
    moveSprite(thisbush, thisbush.x, thisbush.y)
    showSprite(thisbush)
    bushes.append(thisbush)
owlunit1=units.normal_unit(xPositon,yPosition)
normalunits.append(owlunit1)
warrior=units.warrior(100,100)
acounter=False
mainhall=False
while True:
    if keyPressed("n"):
        acounter=False
        normalunits.rotate(1)
        pause(200)
    if keyPressed("w"):
        acounter=True
    if keyPressed("u"):
        if not mainhall:
            mh=buildings.main_hall(normalunits[0])
            mh.build()
            pause(500)
            mainhall=True
    if keyPressed("b"):
        mh.born_normal_unit()
        pause(200)
    if  not acounter :
        normalunits[0].move()
        if keyPressed("h"):
            normalunits[0].harvest()
        if keyPressed("p"):
            normalunits[0].put_res()
    if acounter:
        warrior.move()
        if keyPressed("k"):
            warrior.attack()
    fps= tick(60)
    changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
    updateDisplay()
endWait()
