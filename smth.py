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

tree="Desktop/project folder/tree.png"
fpsDisplay = makeLabel("FPS:",30,10,10,"white")
showLabel(fpsDisplay)
xPositon = 500
yPosition = 320
nextframe = clock()

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
                if collectible in bushes:
                    changeSpriteImage(collectible,1)
                    self.berry+=1

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
    moveSprite(thisbush, thisbush.x, thisbush.y)
    showSprite(thisbush)
    bushes.append(thisbush)
owlunit1=units.normal_unit(xPositon+100,yPosition+100)
owlunit2=units.normal_unit(xPositon,yPosition)
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
        owlunit2.move()
    if keyPressed("h"):
        owlunit1.harvest()
    fps= tick(60)
    changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
    updateDisplay()
endWait()
