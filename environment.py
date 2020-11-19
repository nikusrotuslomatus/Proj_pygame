from pygame_functions import *
import random
from collections import deque
from units_and_buildings import *
class start(object):
    def __init__(self):
        screenSize(1000, 1000)
        setBackgroundColour((43,94,65))
        drawRect(0,450,1000,280,"black")
        setAutoUpdate(0)
        self.text=makeTextBox(0,450,1000,fontSize=20)
        showTextBox(self.text)
        self.wood = "Desktop/project folder/wood.png"
        self.rock = "Desktop/project folder/rock.png"
        self.owl = "Desktop/project folder/owl.png"
        self.bush="Desktop/project folder/bush.png"
        self.warriorowl="Desktop/project folder/warriorowl.png"
        self.tree="Desktop/project folder/tree.png"
        self.warriortree="Desktop/project folder/warriortree.png"
        self.storage="Desktop/project folder/storage.png"
        self.pebble="Desktop/project folder/pebble.png"
        self.branch="Desktop/project folder/branch.png"
        self.berry="Desktop/project folder/berries.png"
        self.menu="Desktop/project folder/menu.png"
        self.sawmill = "Desktop/project folder/sawmill.png"
        self.quarry = "Desktop/project folder/quarry.png"
        self.fpsDisplay = makeLabel("FPS:",30,10,10,"white")
        showLabel(self.fpsDisplay)
        self.xPositon = 500
        self.yPosition = 320
        self.menustorage=makeSprite(self.storage)
        self.menumainhall=makeSprite(self.tree)
        self.menuforge=makeSprite(self.warriortree)
        self.menusawmill=makeSprite(self.sawmill)
        self.menuquarry=makeSprite(self.quarry)
        self.menusprite=makeSprite(self.menu)
        self.menuowl=makeSprite(self.owl)
        self.menuwarrior=makeSprite(self.warriorowl)
        moveSprite(self.menusprite,700,70)
        moveSprite(self.menustorage,725,100)
        moveSprite(self.menumainhall,825,100)
        moveSprite(self.menuforge,925,100)
        moveSprite(self.menusawmill,725,250)
        moveSprite(self.menuquarry,825,250)
        moveSprite(self.menuowl,925,250)
        moveSprite(self.menuwarrior,725,400)
        showSprite(self.menusprite)
        showSprite(self.menustorage)
        showSprite(self.menumainhall)
        showSprite(self.menuforge)
        showSprite(self.menusawmill)
        showSprite(self.menuquarry)
        showSprite(self.menuowl)
        showSprite(self.menuwarrior)
        hideSprite(self.menusprite)
        hideSprite(self.menustorage)
        hideSprite(self.menumainhall)
        hideSprite(self.menuforge)
        hideSprite(self.menusawmill)
        hideSprite(self.menuquarry)
        hideSprite(self.menuowl)
        hideSprite(self.menuwarrior)
        self.normalunits=deque()
        self.warriors=deque()
        self.pebbleicon=makeSprite(self.pebble)
        self.branchicon=makeSprite(self.branch)
        self.berryicon=makeSprite(self.berry)
        moveSprite(self.pebbleicon,210,10)
        moveSprite(self.branchicon,310,10)
        moveSprite(self.berryicon,410,10)