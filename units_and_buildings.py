from pygame_functions import *
import random
from collections import deque
wood = "wood.png"
rock = "rock.png"
owl = "owl.png"
bush="bush.png"
warriorowl="warriorowl.png"
tree="tree.png"
warriortree="warriortree.png"
storage="storage.png"
sawmill = 'sawmill.png'
quarry = 'quarry.png'
'''
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
'''
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
            self.building=makeSprite(owl)
            self.berry=10000
            self.wood=10000
            self.rock=10000
            self.building.hp=[30]
            self.hp = self.building.hp
            moveSprite(self.building,self.xpos,self.ypos)
            showSprite(self.building)
        def move(self):
            if self.building.hp[0] > 0:
                if keyPressed("left"):
                    self.xpos -= self.speed
                elif keyPressed("right"):
                    self.xpos += self.speed
                if keyPressed("up"):
                    self.ypos -= self.speed
                elif keyPressed("down"):
                    self.ypos += self.speed
                moveSprite(self.building, self.xpos, self.ypos)
        def goto(self,xgoto,ygoto):
            if self.building.hp[0] > 0:
                self.xgoto=xgoto
                self.ygoto=ygoto
                for i in range(300):
                    if self.xgoto>self.xpos:
                        self.xpos+=0.01
                    elif self.xgoto<self.xpos:
                        self.xpos-=0.01
                    else:
                        self.xpos=self.xgoto
                    if self.ygoto>self.ypos:
                        self.ypos+=0.01
                    elif self.ygoto<self.ypos:
                        self.ypos-=0.01
                    else:
                        self.ypos=self.ygoto
        def get(self,sawmills,bushes,quarries,pebbles,branches):
            if self.building.hp[0] > 0:
                self.sawmills=sawmills
                self.bushes=bushes
                self.quarries=quarries
                self.pebbles=pebbles
                self.branches=branches
                for i in range(len(sawmills)):
                    if (((self.sawmills[i].x - self.xpos)**2+(self.sawmills[i].y-self.ypos)**2) ** 0.5) <= 25 and self.sawmills[i].hp[0]>0:
                        self.wood+=self.sawmills[i].wood
                        self.sawmills[i].wood=0
                for i in range(len(quarries)):
                    if (((self.quarries[i].x - self.xpos)**2+(self.quarries[i].y-self.ypos)**2) ** 0.5) <= 25 and self.quarries[i].hp[0]>0:
                        self.rock+=self.quarries[i].rock
                        self.quarries[i].rock=0
                for i in range(len(self.bushes)):
                    if (((((self.bushes[i].x - self.xpos) ** 2 + (self.bushes[i].y - self.ypos) ** 2) ** 0.5) <= 39) and iscollectible(bushes[i])) and self.bushes[i].hp[0]>0:
                        changeSpriteImage(bushes[i],1)
                        self.berry+=1
                        bushes[i].collectability=1
                for i in range(len(self.branches)):
                    if (((((self.branches[i].x - self.xpos) ** 2 + (self.branches[i].y - self.ypos) ** 2) ** 0.5) <= 39) and (iscollectible(branches[i]))) and self.branches[i].hp[0]>0:
                        self.wood += 1
                        branches[i].collectability = 1
                        branches[i].hp=-1
                        killSprite(branches[i])
                for i in range(len(self.pebbles)):
                    if ((((self.pebbles[i].x - self.xpos) ** 2 + (self.pebbles[i].y - self.ypos) ** 2) ** 0.5) <= 39) and(iscollectible(pebbles[i])) and self.pebbles[i].hp[0]>0:
                        self.rock += 1
                        pebbles[i].collectability = 1
                        pebbles[i].hp=-1
                        killSprite(pebbles[i])
        def put_res(self,storage_name):
            if self.building.hp[0] > 0:
                self.storage_name=storage_name
                self.storage_name.berry+=self.berry
                self.storage_name.wood+=self.wood
                self.storage_name.rock+=self.rock
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
            self.building=makeSprite(warriorowl)
            self.building.hp=[60]
            self.hp = self.building.hp
            moveSprite(self.building,self.xpos,self.ypos)
            showSprite(self.building)
        def move(self):
            if self.building.hp[0] > 0:
                if keyPressed("left"):
                    self.xpos -= self.speed
                elif keyPressed("right"):
                    self.xpos += self.speed
                if keyPressed("up"):
                    self.ypos -= self.speed
                elif keyPressed("down"):
                    self.ypos += self.speed
                moveSprite(self.building, self.xpos, self.ypos)
        def attack(self):
            if self.building.hp[0] > 0:
                enemies=allTouching(self.building)
                for enemy in enemies:
                    enemy.hp[0] = 0
                    if enemy.hp[0]<=0:
                        killSprite(enemy)
class buildings(object):
    class main_hall(object):
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
            self.building=makeSprite(tree)
            self.building.hp = [200]
            self.hp = self.building.hp
        def build(self):
            moveSprite(self.building,self.xPos,self.yPos)
            showSprite(self.building)
        def born_normal_unit(self):
            if self.building.hp[0] > 0:
                self.normunit=units.normal_unit(self.xPos,self.yPos)
                return self.normunit
    class forge(object):
        def __init__(self,builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
            self.building=makeSprite(warriortree)
            self.building.hp=[300]
            self.hp = self.building.hp
        def build(self):
            moveSprite(self.building,self.xPos,self.yPos)
            showSprite(self.building)
        def born_warrior(self):
            if self.building.hp[0] > 0:
                self.warriorowl=units.warrior(self.xPos,self.yPos)
                return self.warriorowl
    class storage(object):
        def __init__(self, builder):
            self.xPos=builder.xpos
            self.yPos=builder.ypos
            self.building = makeSprite(storage)
            self.building.hp = [200]
            self.hp = self.building.hp
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
            self.building = makeSprite(sawmill)
            self.x = builder.xpos
            self.y = builder.ypos
            for i in range(len(self.woods)):
                if ((((((self.woods[i].x - self.x)**2+(self.woods[i].y-self.y)**2) ** 0.5) <= 300))):
                    self.near_woods.append(0)
                    self.near_woods[self.a] = self.woods[i]
                    self.a += 1
            self.building.hp = [200]
            self.hp = self.building.hp
            self.wood = 0
            self.building.damage_to_trees = 100
            moveSprite(self.building,self.x, self.y)
            showSprite(self.building)
        def sawing(self):
            if self.building.hp[0] > 0:
                if len(self.near_woods):
                    self.wood+=1
                    self.near_woods[0].hp = 0
                    changeSpriteImage(self.near_woods[0],1)
                    self.near_woods.pop(0)
    class quarry(object):
        def __init__(self, builder, stones):
            self.stones = stones
            self.a = 0
            self.near_stones = []
            self.building = makeSprite(quarry)
            self.x = builder.xpos
            self.y = builder.ypos
            for i in range(len(self.stones)):
                if (((self.stones[i].x - self.x) ** 2 + (
                    self.stones[i].y - self.y) ** 2) ** 0.5) <= 300:
                    self.near_stones.append(0)
                    self.near_stones[self.a] = self.stones[i]
                    self.a += 1
            self.building.hp = [400]
            self.hp = self.building.hp
            self.rock = 0
            self.building.damage_to_trees = 100
            moveSprite(self.building, self.x, self.y)
            showSprite(self.building)
        def stonecutting(self):
            if self.building.hp[0] > 0:
                if len(self.near_stones):
                    self.rock+=2
                    self.near_stones[0].hp = 0
                    changeSpriteImage(self.near_stones[0], 1)
                    self.near_stones.pop(0)
