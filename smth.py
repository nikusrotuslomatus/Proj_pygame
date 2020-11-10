from pygame_functions import *
import random
screenSize(1000, 1000)
setBackgroundColour("blue")
drawRect(0,450,1000,280,"black")
setAutoUpdate(False)
owl = makeSprite("Desktop/project folder/owl.png")
fpsDisplay = makeLabel("FPS:",30,10,10,"white")
showLabel(fpsDisplay)
xPos = 500
yPos = 320
moveSprite(owl, xPos, yPos,True)
showSprite(owl)
nextframe = clock()

class units(object):
    def __init__(self,xpos,ypos):
        self.xpos=xpos
        self.ypos=ypos
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
xSpeed = 0
ySpeed = 0
while True:
    xSpeed,ySpeed=0,0
    if keyPressed("left"):
        xSpeed=-2
    elif keyPressed("right"):
        xSpeed=2
    if keyPressed("up"):
        ySpeed=-2
    elif keyPressed("down"):
        ySpeed=2
    #xSpeed += math.sin(math.radians(angle)) * thrustAmount
    #ySpeed -= math.cos(math.radians(angle)) * thrustAmount
    if yPos > 420:
        yPos=420
    xPos += xSpeed
    yPos += ySpeed
    moveSprite(owl, xPos, yPos,True)
    fps= tick(60)
    changeLabel(fpsDisplay, "FPS: {0}".format(str(round(fps, 2))))
    updateDisplay()
endWait()
