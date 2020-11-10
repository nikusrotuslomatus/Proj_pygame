from pygame_functions import *
import random
screenSize(1000, 1000)
setBackgroundColour("blue")
drawRect(0,450,1000,280,"black")
setAutoUpdate(10)
text=makeTextBox(0,450,1000,fontSize=20)
showTextBox(text)
owl = makeSprite("Desktop/project folder/owl.png")
fpsDisplay = makeLabel("FPS:",30,10,10,"white")
showLabel(fpsDisplay)
xPositon = 500
yPosition = 320
moveSprite(owl, xPositon, yPosition,True)
showSprite(owl)
nextframe = clock()

class units(object):
    class normal_unit(object):
        def __init__(self,xpos,ypos,spritename):
            self.xpos=xpos
            self.ypos=ypos
            self.spritename=spritename
            self.speed=3
        def move(self):
            if keyPressed("left"):
                self.xpos -= self.speed
            elif keyPressed("right"):
                self.xpos += self.speed
            if keyPressed("up"):
                self.ypos -= self.speed
            elif keyPressed("down"):
                self.ypos += self.speed
            moveSprite(self.spritename, self.xpos, self.ypos)

class buildings(object):
    def __init__(self,xpos,ypos):
        self.xpos=xpos
        self.ypos=ypos

bushes = []
for x in range(10):
    thisbush = makeSprite("Desktop/project folder/bush.png")
    addSpriteImage(thisbush, "Desktop/project folder/tree.png")
    thisbush.x = random.randint(0,1000)
    thisbush.y = random.randint(0,375)
    moveSprite(thisbush, thisbush.x, thisbush.y)
    showSprite(thisbush)
    bushes.append(thisbush)
owlunit=units.normal_unit(xPositon,yPosition,owl)
while True:
    owlunit.move() 
    fps= tick(60)
    changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
    updateDisplay()
endWait()
