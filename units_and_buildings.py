from pygame_functions import *
import random
import functools
import numpy as np
from collections import deque
wood = "wood.png"
rock = "rock.png"
owl = "owl.png"
bush="bush.png"
warriorowl="warriorowl.png"
tree="tree.png"
warriortree="warriortree.png"
storage="storage.png"
hellish_sawmill = 'sawmill.png'
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
'''
def iscollectible(x):
   return x.collectability == 0
class abstract_unit(object):
    def __init__(self,xpos,ypos,hp,spritename):
        self.xpos = xpos
        self.ypos = ypos
        self.hp = hp
        self.havecome = False
        self.building = makeSprite(spritename)
        self.building.hp = self.hp
        moveSprite(self.building, self.xpos, self.ypos)
        showSprite(self.building)
    def movescreen(self, screenx, screeny):
        self.screenx = screenx
        self.screeny = screeny
        self.xpos += screenx
        self.ypos += screeny
        if (self.xpos <= -50 or self.xpos >= 1050 or self.ypos <= -50 or self.ypos >= 850) == False:
            moveSprite(self.building, self.xpos, self.ypos)

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

    def goto(self, xgoto, ygoto):
        if self.hp[0] > 0:
            self.xgoto = xgoto
            self.ygoto = ygoto
            if abs(self.xpos - self.xgoto) > 3 or abs(self.ypos - self.ygoto) > 3:
                if self.havecome:
                    self.havecome = False
                for i in range(300):
                    if self.xgoto > self.xpos:
                        self.xpos += 0.01
                    elif self.xgoto < self.xpos:
                        self.xpos -= 0.01
                    else:
                        self.xpos = self.xgoto
                    if self.ygoto > self.ypos:
                        self.ypos += 0.01
                    elif self.ygoto < self.ypos:
                        self.ypos -= 0.01
            else:
                self.havecome = True
            if self.ypos <= 850 and self.xpos <= 1100 and self.xpos >= -100 and self.ypos >= -100:
                showSprite(self.building)


class abstract_building(object):
    def __init__(self, builder,hp,spritename):
        self.building = makeSprite(spritename)
        self.xpos = builder.xpos
        self.ypos = builder.ypos
        self.hp = hp
        self.building.hp = self.hp
        moveSprite(self.building, self.xpos, self.ypos)
        showSprite(self.building)

    def movescreen(self, screenx, screeny):
        self.screenx = screenx
        self.screeny = screeny
        self.xpos += screenx
        self.ypos += screeny
        if (self.xpos <= -100 or self.xpos >= 1100 or self.ypos <= -100 or self.ypos >= 850) == False:
            moveSprite(self.building, self.xpos, self.ypos)


class units(object):
    class normal_unit(abstract_unit):
        def __init__(self,xpos,ypos):
            abstract_unit.__init__(self,xpos,ypos,[50],owl)
            self.berry=1000
            self.wood=1000
            self.rock=1000
            '''
        def disti(self,resourses,name):
            for i in range(len(resourses)):
                if (((resourses[i].xpos - self.xpos) ** 2 + (
                        resourses[i].ypos - self.ypos) ** 2) ** 0.5) <= 25 and resourses[i].hp[0] > 0:
                    if name[0] == "1":
                        if name[1] == "0":
                            self.wood += resourses[i].wood
                            resourses[i].wood = 0
                        else:
                            self.wood += 1
                            changeSpriteImage(resourses[i].building, 1)
                            resourses[i].collectability = 1
                            resourses[i].hp = [-1]
                            killSprite(resourses[i].building)
                            k = resourses[i]
                            resourses[i] = buildings.environment(owl,owl,[10],1)
                    elif name[0] == "2":
                        self.berry += 1
                        changeSpriteImage(resourses[i].building, 1)
                        resourses[i].collectability = 1
                        resourses[i].hp = [-1]
                    elif name[0] == "3":
                        if name[1] == "0":
                            self.rock += resourses[i].stones

                        else:
                            self.rock += 1
                            changeSpriteImage(resourses[i].building, 1)
                            resourses[i].collectability = 1
                            resourses[i].hp = [-1]
                            killSprite( resourses[i].building)
                            resourses[i] = buildings.environment(owl,owl,[-1],1)
                            '''
        def touching_sprite(self,xpos,ypos,hp):
            return (((xpos - self.xpos) ** 2 + (ypos - self.ypos) ** 2) ** 0.5) <= 25 and hp[0] > 0

        def get(self,sawmills,bushes,quarries,pebbles,branches):
            if self.hp[0] > 0:
                for i in range(len(sawmills)):
                    if self.touching_sprite(sawmills[i].xpos,sawmills[i].ypos,sawmills[i].hp) is True:
                        self.wood += sawmills[i].wood
                        sawmills[i].wood = 0
                for i in range(len(bushes)):
                    if self.touching_sprite(bushes[i].xpos,bushes[i].ypos,bushes[i].hp) is True:
                        self.berry += 1
                        changeSpriteImage(bushes[i].building, 1)
                        bushes[i].collectability = 1
                        bushes[i].hp = [-1]
                for i in range(len(quarries)):
                    if self.touching_sprite(quarries[i].xpos, quarries[i].ypos, quarries[i].hp) is True:
                        self.rock += quarries[i].stones
                        quarries[i].wood = 0
                for i in range(len(pebbles)):
                    if self.touching_sprite(pebbles[i].xpos,pebbles[i].ypos,pebbles[i].hp) is True:
                        self.rock += 1
                        changeSpriteImage(pebbles[i].building, 1)
                        pebbles[i].collectability = 1
                        pebbles[i].hp = [-1]
                        killSprite(pebbles[i].building)
                        pebbles[i] = buildings.environment(owl, owl, [10], 1)
                for i in range(len(branches)):
                    if self.touching_sprite(branches[i].xpos, branches[i].ypos, branches[i].hp) is True:
                        self.wood += 1
                        changeSpriteImage(branches[i].building, 1)
                        branches[i].collectability = 1
                        branches[i].hp = [-1]
                        killSprite(branches[i].building)
                        branches[i] = buildings.environment(owl, owl, [10], 1)
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
            abstract_unit.__init__(self,xpos,ypos,[100],warriorowl)
        def attack(self):
            if self.hp[0] > 0:
                enemies=allTouching(self.building)
                for i in range(len(enemies)):
                    enemies[i].hp[0] = -1
                    if enemies[i].hp[0]<=0:
                        killSprite(enemies[i])
                        enemies[i] = buildings.environment(owl, owl, [-1], 1)
class buildings(object):
    class main_hall(abstract_building):
        def __init__(self,builder):
            abstract_building.__init__(self,builder,[500],tree)
        def born_normal_unit(self):
            if self.hp[0] > 0:
                self.normunit=units.normal_unit(self.xpos,self.ypos)
                return self.normunit

    class forge(abstract_building):
        def __init__(self,builder):
            abstract_building.__init__(self,builder,[500],warriortree)
        def born_warrior(self):
            if self.hp[0] > 0:
                self.warriorowl=units.warrior(self.xpos,self.ypos)
                return self.warriorowl

    class storage(abstract_building):
        def __init__(self,builder):
            abstract_building.__init__(self,builder,[500],storage)
            self.berry = 0
            self.rock = 0
            self.wood = 0
    class sawmill(abstract_building):
        def __init__(self,builder,woods):
            abstract_building.__init__(self,builder,[500],hellish_sawmill)
            self.woods = woods
            self.a = 0
            self.near_woods = []
            for i in range(len(self.woods)):
                if ((((((self.woods[i].xpos - self.xpos)**2+(self.woods[i].ypos-self.ypos)**2) ** 0.5) <= 300))):
                    self.near_woods.append(0)
                    self.near_woods[self.a] = self.woods[i]
                    self.a += 1
            self.wood = 0
            self.damage_to_trees = 100
        def do_smth(self):
            #sawing
            if self.hp[0] > 0:
                if len(self.near_woods):
                    self.wood+=1
                    self.near_woods[0].hp = [0]
                    changeSpriteImage(self.near_woods[0].building,1)
                    self.near_woods.pop(0)
    class quarry(abstract_building):
        def __init__(self,builder, stones):
            abstract_building.__init__(self, builder, [500], quarry)
            self.stones = stones
            self.a = 0
            self.near_stones = []
            for i in range(len(self.stones)):
                if (((self.stones[i].xpos - self.xpos) ** 2 + (self.stones[i].ypos - self.ypos) ** 2) ** 0.5) <= 300:
                    self.near_stones.append(0)
                    self.near_stones[self.a] = self.stones[i]
                    self.a += 1
            self.rock = 0
            self.damage_to_trees = 100
        def do_smth(self):
            #stonecutting
            if self.hp[0] > 0:
                if len(self.near_stones):
                    self.rock+=2
                    self.near_stones[0].hp = [0]
                    changeSpriteImage(self.near_stones[0].building, 1)
                    self.near_stones.pop(0)

    class environment(object):
        def __init__(self, spritename, secondspritename, hp, collectability):
            self.spritename = spritename
            self.secondspritename = secondspritename
            self.hp = hp
            self.collectability = collectability
            self.building = makeSprite(spritename)
            self.building.hp = self.hp
            addSpriteImage(self.building, self.secondspritename)
            self.xpos = random.randint(-2500, 2500)
            self.ypos = random.randrange(-1500, 1500)
            moveSprite(self.building, self.xpos, self.ypos)
            if (self.ypos >= 410 and self.ypos <= 750) == False:
                showSprite(self.building)

        def movescreen(self, screenx, screeny):
            self.screenx = screenx
            self.screeny = screeny
            self.xpos += screenx
            self.ypos += screeny
            if (self.xpos <= -50 or self.xpos >= 1050 or self.ypos <= -50 or self.ypos >= 850) == False:
                moveSprite(self.building, self.xpos, self.ypos)