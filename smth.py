from pygame_functions import *
import random
from collections import deque
screenSize(1000, 1000)
setBackgroundColour((91,118,27))
drawRect(0,450,1000,280,"black")
setAutoUpdate(0)
text=makeTextBox(0,450,1000,fontSize=20)
showTextBox(text)
wood = "Desktop/project folder/wood.png"
rock = "Desktop/project folder/rock.png"
owl = "Desktop/project folder/owl.png"
bush="Desktop/project folder/bush.png"
warriorowl="Desktop/project folder/warriorowl.png"
tree="Desktop/project folder/tree.png"

warriortree="Desktop/project folder/warriortree.png"
storage="Desktop/project folder/storage.png"
fpsDisplay = makeLabel("FPS:",30,10,10,"white")
showLabel(fpsDisplay)
xPositon = 500
yPosition = 320
nextframe = clock()
normalunits=deque()
warriors=deque()
def iscollectible(x):
    if x.collectability==0:
        return True
    else:
        return False
def create_random_env(spritename,secondspritename,hp,collectability):
    thissprite = makeSprite(spritename)
    addSpriteImage(thissprite, secondspritename)
    thissprite.x = random.randint(0,1000)
    thissprite.y = random.randint(0,375)
    thissprite.collectability=collectability
    thissprite.hp=hp
    moveSprite(thissprite, thissprite.x, thissprite.y)
    showSprite(thissprite)
    return thissprite
    
class units(object):
    class normal_unit(object):
        def __init__(self,xpos,ypos):
            self.xpos=xpos
            self.ypos=ypos
            self.speed=3
            self.sprite=makeSprite(owl)
            self.berry=0
            self.sprite.hp=30
            moveSprite(self.sprite,self.xpos,self.ypos)
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
        def put_res(self,storage_name):
            reslabel=makeLabel("ты положил "+str(self.berry)+" ягод на склад",50,30,30)
            showLabel(reslabel)
            self.storage_name=storage_name
            self.storage_name.berry+=self.berry
            self.berry=0
            pause(1000)
            hideLabel(reslabel)
    class warrior(normal_unit):
        def __init__(self,xpos,ypos):
            self.xpos=xpos
            self.ypos=ypos
            self.speed=3
            self.sprite=makeSprite(warriorowl)
            self.sprite.hp=60
            moveSprite(self.sprite,self.xpos,self.ypos)
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
                enemy.hp-=10
                if enemy.hp==0:
                    hideSprite(enemy)
class buildings(object):
    class main_hall(object):
        global normalunits
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
            self.building=None
        def build(self):
            self.building=makeSprite(tree)
            self.building.hp=200
            moveSprite(self.building,self.xPos,self.yPos)
            showSprite(self.building)
        def born_normal_unit(self):
            normunit=units.normal_unit(self.xPos,self.yPos)
            normalunits.append(normunit)
    class forge(object):
        global warriors
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
        def build(self):
            self.building=makeSprite(warriortree)
            self.building.hp=300
            moveSprite(self.building,self.xPos,self.yPos)
            showSprite(self.building)
        def born_warrior(self):
            warriorowl=units.warrior(self.xPos,self.yPos)
            warriors.append(warriorowl)
    class storage(object):
        global storages
        def __init__(self, builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
            self.building=None
        def build(self):
            self.building = makeSprite(storage)
            self.building.hp = 200
            self.building.berry = 0
            self.building.wood = 0
            self.building.stone = 0
            self.building.x = self.xPos
            self.building.y = self.yPos
            storages.append(self.building)
            moveSprite(self.building, self.xPos, self.yPos)
            showSprite(self.building)

bushes = []
woods=[]
rocks=[]
for x in range(10):
    envbush=create_random_env(bush,"Desktop/project folder/bushcollected.png",20,0)
    bushes.append(envbush)
    envwood=create_random_env(wood,"Desktop/project folder/woodcollected.png",100,1)
    woods.append(envwood)
    envrock=create_random_env(rock,"Desktop/project folder/rockcollected.png",400,1)
    rocks.append(envrock)
owlunit1=units.normal_unit(xPositon,yPosition)
normalunits.append(owlunit1)
acounter=False
mainhall=False
storages=deque()
while True:
    if keyPressed("1"):
        acounter=False
        normalunits.rotate(1)
        pause(200)
    if keyPressed("2"):
        acounter=True
        warriors.rotate(1)
        pause(200)
    if keyPressed("3"):
        storages.rotate(1)
        stsign=makeSprite(owl)
        moveSprite(stsign,storages[0].x,storages[0].y+50)
        showSprite(stsign)
        pause(300)
        hideSprite(stsign)
    if keyPressed("n"):
        if storages[0].berry>=3:
            mh.born_normal_unit()
            storages[0].berry-=3
            pause(200)
    if keyPressed("w"):
        forge.born_warrior()
        pause(200)
    if  not acounter :
        normalunits[0].move()
        if keyPressed("h"):
            normalunits[0].harvest()
        if keyPressed("p"):
            normalunits[0].put_res(storages[0])
        if keyPressed("s"):
            sg=buildings.storage(normalunits[0])
            sg.build()
            pause(200)

        if keyPressed("b"):
            if not mainhall:
                mh=buildings.main_hall(normalunits[0])
                mh.build()
                pause(500)
                mainhall=True
        if keyPressed("f"):
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
