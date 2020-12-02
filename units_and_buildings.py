from pygame_functions import *
import random
from collections import deque
'''
wood = "wood.png"
rock = "rock.png"
owl = "owl.png"
bush="bush.png"
warriorowl="warriorowl.png"
tree="tree.png"
warriortree="warriortree.png"
storage="storage.png"
sawmill = 'sawmill.png'
quarry = "quarry.png"
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
            self.hp=[30]
            self.building.hp = self.hp
            self.havecome=False
            moveSprite(self.building,self.xpos,self.ypos)
            showSprite(self.building)
        def move(self):
            if self.hp[0] > 0:
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
            if self.hp[0] > 0:
                self.xgoto=xgoto
                self.ygoto=ygoto
                if abs(self.xpos-self.xgoto)>3 or abs(self.ypos-self.ygoto)>3:
                    if self.havecome:
                        self.havecome=False
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
                    self.havecome=True
                if self.ypos<=420 and self.xpos<=1100 and self.xpos>=-100 and self.ypos>=-100:
                    showSprite(self.building)
        def get(self,sawmills,bushes,quarries,pebbles,branches):
            if self.hp[0] > 0:
                self.sawmills=sawmills
                self.bushes=bushes
                self.quarries=quarries
                self.pebbles=pebbles
                self.branches=branches
                for i in range(len(self.sawmills)):
                    if (((self.sawmills[i].xpos - self.xpos)**2+(self.sawmills[i].ypos-self.ypos)**2) ** 0.5) <= 25 and self.sawmills[i].hp[0]>0:
                        self.wood+=self.sawmills[i].wood
                        self.sawmills[i].wood=0
                for i in range(len(self.quarries)):
                    if (((self.quarries[i].xpos - self.xpos)**2+(self.quarries[i].ypos-self.ypos)**2) ** 0.5) <= 25 and self.quarries[i].hp[0]>0:
                        self.rock+=self.quarries[i].rock
                        self.quarries[i].rock=0
                for i in range(self.bushes.shape[0]):
                    if (((((self.bushes[i].xpos - self.xpos) ** 2 + (self.bushes[i].ypos - self.ypos) ** 2) ** 0.5) <= 39) and iscollectible(bushes[i])) and self.bushes[i].hp[0]>0:
                        changeSpriteImage(bushes[i].building,1)
                        self.berry+=1
                        bushes[i].collectability=1
                for i in range(self.branches.shape[0]):
                    if (((((self.branches[i].xpos - self.xpos) ** 2 + (self.branches[i].ypos - self.ypos) ** 2) ** 0.5) <= 39) and (iscollectible(branches[i]))) and self.branches[i].hp[0]>0:
                        self.wood += 1
                        branches[i].collectability = 1
                        branches[i].hp=-1
                        killSprite(branches[i].building)
                for i in range(self.pebbles.shape[0]):
                    if ((((self.pebbles[i].xpos - self.xpos) ** 2 + (self.pebbles[i].ypos - self.ypos) ** 2) ** 0.5) <= 39) and(iscollectible(pebbles[i])) and self.pebbles[i].hp[0]>0:
                        self.rock += 1
                        pebbles[i].collectability = 1
                        pebbles[i].hp=-1
                        killSprite(pebbles[i].building)
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-50 or self.xpos>=1050 or self.ypos<=-50 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)
        def put_res(self,storage_name):
            if self.hp[0] > 0:
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
            self.havecome=False
            self.hp=[60]
            self.building.hp = self.hp
            moveSprite(self.building,self.xpos,self.ypos)
            showSprite(self.building)
        def move(self):
            if self.hp[0] > 0:
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
            if self.hp[0] > 0:
                enemies=allTouching(self.building)
                for enemy in enemies:
                    enemy.hp[0] = 0
                    if enemy.hp[0]<=0:
                        killSprite(enemy)
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-50 or self.xpos>=1050 or self.ypos<=-50 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)
class buildings(object):
    class environment(object):
        def __init__(self,spritename,secondspritename,hp,collectability):
            self.spritename = spritename
            self.secondspritename = secondspritename
            self.hp=hp
            self.collectability=collectability
            self.building=makeSprite(spritename)
            self.building.hp=self.hp
            addSpriteImage(self.building, self.secondspritename)
            self.xpos = random.randint(-2500,2500)
            self.ypos = random.randrange(-1500,1500)
            moveSprite(self.building, self.xpos, self.ypos)
            if (self.ypos>=410 and self.ypos<=750)==False:
                showSprite(self.building)    
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-100 or self.xpos>=1100 or self.ypos<=-100 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)
    class main_hall(object):
        def __init__(self,builder):
            self.xpos=builder.xpos
            self.ypos=builder.ypos
            self.building=makeSprite(tree)
            self.hp = [200]
            self.building.hp = self.hp
            moveSprite(self.building,self.xpos,self.ypos)
            showSprite(self.building)
        def born_normal_unit(self):
            if self.hp[0] > 0:
                self.normunit=units.normal_unit(self.xpos,self.ypos)
                return self.normunit
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-100 or self.xpos>=1100 or self.ypos<=-100 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)

    class forge(object):
        def __init__(self,builder):
            self.xpos=builder.xpos
            self.ypos=builder.ypos
            self.building=makeSprite(warriortree)
            self.hp=[300]
            self.building.hp = self.hp
            moveSprite(self.building,self.xpos,self.ypos)
            showSprite(self.building)
        def born_warrior(self):
            if self.hp[0] > 0:
                self.warriorowl=units.warrior(self.xpos,self.ypos)
                return self.warriorowl
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-100 or self.xpos>=1100 or self.ypos<=-100 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)

    class storage(object):
        def __init__(self, builder):
            self.xpos=builder.xpos
            self.ypos=builder.ypos
            self.building = makeSprite(storage)
            self.hp = [200]
            self.building.hp = self.hp
            self.berry = 0
            self.rock = 0
            self.wood = 0
            moveSprite(self.building, self.xpos, self.ypos)
            showSprite(self.building)
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-100 or self.xpos>=1100 or self.ypos<=-100 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)
    class sawmill(object):
        def __init__(self, builder,woods):
            self.woods = woods
            self.a = 0
            self.near_woods = []
            self.building = makeSprite(sawmill)
            self.xpos = builder.xpos
            self.ypos = builder.ypos
            for i in range(len(self.woods)):
                if ((((((self.woods[i].xpos - self.xpos)**2+(self.woods[i].ypos-self.ypos)**2) ** 0.5) <= 300))):
                    self.near_woods.append(0)
                    self.near_woods[self.a] = self.woods[i]
                    self.a += 1
            self.hp = [200]
            self.building.hp = self.hp
            self.wood = 0
            self.damage_to_trees = 100
            moveSprite(self.building,self.xpos, self.ypos)
            showSprite(self.building)
        def sawing(self):
            if self.hp[0] > 0:
                if len(self.near_woods):
                    self.wood+=1
                    self.near_woods[0].hp = [0]
                    changeSpriteImage(self.near_woods[0].building,1)
                    self.near_woods.pop(0)
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-100 or self.xpos>=1100 or self.ypos<=-100 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)

    class quarry(object):
        def __init__(self, builder, stones):
            self.stones = stones
            self.a = 0
            self.near_stones = []
            self.building = makeSprite(quarry)
            self.xpos = builder.xpos
            self.ypos = builder.ypos
            for i in range(len(self.stones)):
                if (((self.stones[i].xpos - self.xpos) ** 2 + (self.stones[i].ypos - self.ypos) ** 2) ** 0.5) <= 300:
                    self.near_stones.append(0)
                    self.near_stones[self.a] = self.stones[i]
                    self.a += 1
            self.hp = [400]
            self.building.hp = self.hp
            self.rock = 0
            self.damage_to_trees = 100
            moveSprite(self.building, self.xpos, self.ypos)
            showSprite(self.building)
        def stonecutting(self):
            if self.hp[0] > 0:
                if len(self.near_stones):
                    self.rock+=2
                    self.near_stones[0].hp = [0]
                    changeSpriteImage(self.near_stones[0].building, 1)
                    self.near_stones.pop(0)
        def movescreen(self,screenx,screeny):
            self.screenx=screenx
            self.screeny=screeny
            self.xpos+=screenx
            self.ypos+=screeny
            if (self.xpos<=-100 or self.xpos>=1100 or self.ypos<=-100 or self.ypos>=420)==False:
                moveSprite(self.building,self.xpos,self.ypos)
