from pygame_functions import *
import random
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
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
        def build(self):
            building=makeSprite(tree)
            moveSprite(building,self.xPos,self.yPos)
            showSprite(building)
        


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
owlunit1=units.normal_unit(xPositon+100,yPosition+100)

owlunit2=units.normal_unit(xPositon,yPosition)
warrior=units.warrior(100,100)
acounter=False
while True:
    if keyPressed("a"):
        acounter=True
    if keyPressed("b"):
        acounter=False
    if keyPressed("u"):
        mh=buildings.main_hall(owlunit1)
        mh.build()
        pause(500)
    if  not acounter :
        owlunit1.move()
    if acounter:
        warrior.move()
    if keyPressed("h"):
        owlunit1.harvest()
    if keyPressed("p"):
        owlunit1.put_res()
    if keyPressed("k"):
        warrior.attack()
    fps= tick(60)
    changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
    updateDisplay()
endWait()
