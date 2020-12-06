from pygame_functions import *
import random
from collections import deque
from units_and_buildings import *
import numpy as np
from numba import jit
screenSize(1000, 730)
nazi="Desktop/project folder/nazi.jpg"
setBackgroundImage(nazi)
text = makeTextBox(0, 450, 1000, fontSize=20)

xPositon = 500
yPosition = 320
#все массивы в которых будут
nextFrame_woods = clock()
nextFrame_rocks = clock()
bushes = np.array([],dtype=object)
woods = np.array([],dtype=object)
rocks = np.array([],dtype=object)
pebbles = np.array([],dtype=object)
branches = np.array([],dtype=object)
normalunits = deque()
storages = deque()
sawmills = deque()
quarries = deque()
warriors = deque()
allspries=np.array([])
forges=np.array([],dtype=object)
mainhalls=np.array([],dtype=object)
allspries = np.append(allspries,[mainhalls,forges,warriors,quarries,sawmills,storages,normalunits,branches,pebbles,rocks,woods,bushes])
#имена файлов со спрайтами
wood = "wood.png"
rock = "rock.png"
owl = "owl.png"
bush = "bush.png"
warriorowl = "warriorowl.png"
tree = "tree.png"
warriortree = "warriortree.png"
storage = "storage.png"
pebble = "pebble.png"
branch = "branch.png"
berry = "berries.png"
menu = "menu.png"
sawmill = "sawmill.png"
quarry = "quarry.png"
#переименование в случае если у пользователя мак
try:
    menustorage = makeSprite(storage)
except:
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
    menustorage = makeSprite(storage)
#верх экрана
labelpebble = makeLabel("0", 30, 250, 10, "white")
lableberry = makeLabel("0", 30, 450, 10, "white")
labelbranch = makeLabel("0", 30, 350, 10, "white")
fpsDisplay = makeLabel("FPS:", 30, 10, 10, "white")
pebbleicon = makeSprite(pebble)
branchicon = makeSprite(branch)
berryicon = makeSprite(berry)
moveSprite(pebbleicon, 210, 10)
moveSprite(branchicon, 310, 10)
moveSprite(berryicon, 410, 10)
setAutoUpdate(0)
showLabel(fpsDisplay)
#
menustorage.clickability = 0
menumainhall = makeSprite(tree)
menumainhall.clickability = 0
menuforge = makeSprite(warriortree)
menuforge.clickability = 0
menusawmill = makeSprite(sawmill)
menusawmill.clickability = 0
menuquarry = makeSprite(quarry)
menuquarry.clickability = 0
menusprite = makeSprite(menu)
menuowl = makeSprite(owl)
menuowl.clickability = 0
menuwarrior = makeSprite(warriorowl)
menuwarrior.clickability = 0
moveSprite(menusprite, 700, 70)
moveSprite(menustorage, 725, 100)
moveSprite(menumainhall, 825, 100)
moveSprite(menuforge, 925, 100)
moveSprite(menusawmill, 725, 250)
moveSprite(menuquarry, 825, 250)
moveSprite(menuowl, 925, 250)
moveSprite(menuwarrior, 725, 400)
pos = (500, 300)
@jit(fastmath=True)
def menu(closing=False):
    for pebl in pebbles:
        if pebl.xpos >= 640 and pebl.xpos<=1100  and pebl.ypos >= 0 and pebl.ypos<=450:
            if pebl.hp[0] <= 0:
                killSprite(pebl.building)
            elif closing:
                showSprite(pebl.building)
            else:
                hideSprite(pebl.building)
    for rck in rocks:
        if rck.xpos >= 640 and rck.xpos<=1100  and rck.ypos >= 0 and rck.ypos<=450:
            if rck.hp[0] <= 0:
                killSprite(rck.building)
            elif closing:
                showSprite(rck.building)
            else:
                hideSprite(rck.building)
    for bsh in bushes:
        if bsh.xpos >= 640 and bsh.xpos<=1100  and bsh.ypos >= 0 and bsh.ypos<=450:
            if bsh.hp[0] <= 0:
                killSprite(bsh.building)
            elif closing:
                showSprite(bsh.building)
            else:
                hideSprite(bsh.building)
    for wds in woods:
        if wds.xpos >= 640 and wds.xpos<=1100  and wds.ypos >= 0 and wds.ypos<=450:
            if wds.hp[0] <= 0:
                killSprite(wds.building)
            elif closing:
                showSprite(wds.building)
            else:
                hideSprite(wds.building)
    for brnch in branches:
        if brnch.xpos >= 640 and brnch.xpos<=1100  and brnch.ypos >= 0 and brnch.ypos<=450:
            if brnch.hp[0] <= 0:
                killSprite(brnch.building)
            elif closing:
                showSprite(brnch.building)
            else:
                hideSprite(brnch.building)
    showSprite(menusprite)
    showSprite(menustorage)
    showSprite(menumainhall)
    showSprite(menuforge)
    showSprite(menusawmill)
    showSprite(menuquarry)
    showSprite(menuowl)
    showSprite(menuwarrior)
def iscollectible(x):
    if x.collectability==0:
        return True
    else:
        return False
