from pygame_functions import *
import random
from collections import deque
import environment
a=environment.start()
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
            self.sprite=makeSprite(a.owl)
            self.berry=0
            self.wood=0
            self.rock=0
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
        def get(self,sawmills,bushes,quarries,pebbles,branches):
            self.sawmills=sawmills
            self.bushes=bushes
            self.quarries=quarries
            self.pebbles=pebbles
            self.branches=branches
            collectibles=allTouching(self.sprite)
            for i in range(len(sawmills)):
                 if (((self.sawmills[i].x - self.xpos)**2+(self.sawmills[i].y-self.ypos)**2) ** 0.5) <= 30:
                    self.wood+=self.sawmills[i].wood
                    sawmills[i].wood=0
            for collectible in collectibles:
                if collectible in self.bushes and iscollectible(collectible):
                    changeSpriteImage(collectible,1)
                    self.berry+=1
                    collectible.collectability=1
                if collectible in self.branches:
                    self.wood+=1
                    killSprite(collectible)
                    collectible.collectability=1
                if collectible in self.pebbles:
                    self.rock+=1
                    killSprite(collectible)
                    collectible.collectability=1
            for i in range(len(quarries)):
                 if (((self.quarries[i].x - self.xpos)**2+(self.quarries[i].y-self.ypos)**2) ** 0.5) <= 30:
                    self.rock+=self.quarries[i].rock
                    quarries[i].rock=0
        def put_res(self,storage_name):
            self.storage_name=storage_name
            self.storage_name.berry+=self.berry
            self.storage_name.wood+=self.rock
            self.storage_name.rock+=self.wood
            reslabel=makeLabel("ты положил "+str(self.berry)+" ягод на склад",50,30,30)
            reslabel1=makeLabel("ты положил "+str(self.rock)+" камней на склад",50,30,70)
            reslabel2=makeLabel("ты положил "+str(self.wood)+" дров на склад",50,30,110)
            showLabel(reslabel)
            showLabel(reslabel1)
            showLabel(reslabel2)
            self.berry=0
            self.wood=0
            self.rock=0
            pause(1000)
            hideLabel(reslabel)
            hideLabel(reslabel1)
            hideLabel(reslabel2)
    class warrior(normal_unit):
        def __init__(self,xpos,ypos):
            self.xpos=xpos
            self.ypos=ypos
            self.speed=3
            self.sprite=makeSprite(a.warriorowl)
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
                enemy.hp-=100
                if enemy.hp<=0:
                    hideSprite(enemy)
class buildings(object):
    class main_hall(object):
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
            self.building=None
        def build(self):
            self.building=makeSprite(a.tree)
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
            self.building=makeSprite(a.warriortree)
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
            self.building = makeSprite(a.storage)
            self.building.hp = 200
            self.building.berry = 0
            self.building.rock = 0
            self.building.wood = 0
            self.building.x = self.xPos
            self.building.y = self.yPos
        def build(self):
            moveSprite(self.building, self.xPos, self.yPos)
            showSprite(self.building)
            return self.building

    class sawmill(object):
        def __init__(self, builder,woods):
            self.woods = woods
            self.a = 0
            self.near_woods = []
            self.building = makeSprite(a.sawmill)
            self.building.x = builder.xpos
            self.building.y = builder.ypos
            for i in range(len(self.woods)):
                if (((self.woods[i].x - self.building.x)**2+(self.woods[i].y-self.building.y)**2) ** 0.5) <= 300:
                    self.near_woods.append(0)
                    self.near_woods[self.a] = self.woods[i]
                    self.a += 1
            self.building.hp = 200
            self.building.wood = 0
            self.building.damage_to_trees = 100
            moveSprite(self.building,self.building.x, self.building.y)
            showSprite(self.building)


        def sawing(self):
            if len(self.near_woods):
                self.building.wood+=1
                self.near_woods[0].hp = 0
                changeSpriteImage(self.near_woods[0],1)
                self.near_woods.pop(0)

    class quarry(object):
        def __init__(self, builder, stones):
            self.stones = stones
            self.a = 0
            self.near_stones = []
            self.building = makeSprite(a.quarry)
            self.building.x = builder.xpos
            self.building.y = builder.ypos
            for i in range(len(self.stones)):
                if (((self.stones[i].x - self.building.x) ** 2 + (
                    self.stones[i].y - self.building.y) ** 2) ** 0.5) <= 300:
                    self.near_stones.append(0)
                    self.near_stones[self.a] = self.stones[i]
                    self.a += 1
            self.building.hp = 200
            self.building.rock = 0
            self.building.damage_to_trees = 100
            moveSprite(self.building, self.building.x, self.building.y)
            showSprite(self.building)

        def stonecutting(self):
            if len(self.near_stones):
                self.building.rock+=11
                self.near_stones[0].hp = 0
                changeSpriteImage(self.near_stones[0], 1)
                self.near_stones.pop(0)
