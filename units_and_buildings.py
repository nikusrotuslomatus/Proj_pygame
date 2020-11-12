from pygame_functions import *
import random
from collections import deque
wood = "Desktop/project folder/wood.png"
rock = "rock.png"
owl = "owl.png"
bush="bush.png"
warriorowl="warriorowl.png"
tree="tree.png"
warriortree="warriortree.png"
storage="storage.png"
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
        def harvest(self,bushes):
            self.bushes=bushes
            collectibles=allTouching(self.sprite)
            for collectible in collectibles:
                if collectible in self.bushes and iscollectible(collectible):
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
            self.normunit=units.normal_unit(self.xPos,self.yPos)
            return self.normunit
    class forge(object):
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
        def build(self):
            self.building=makeSprite(warriortree)
            self.building.hp=300
            moveSprite(self.building,self.xPos,self.yPos)
            showSprite(self.building)
        def born_warrior(self):
            self.warriorowl=units.warrior(self.xPos,self.yPos)
            return self.warriorowl
    class storage(object):
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
            moveSprite(self.building, self.xPos, self.yPos)
            showSprite(self.building)
            return self.building