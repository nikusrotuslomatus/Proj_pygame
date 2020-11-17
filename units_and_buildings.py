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
sawmill = 'sawmill.png'
quarry = 'quarry.png'
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
            self.building.wood = 0
            self.building.x = self.xPos
            self.building.y = self.yPos
            moveSprite(self.building, self.xPos, self.yPos)
            showSprite(self.building)
            return self.building

    class sawmill(object):
        def __init__(self, builder,woods):
            self.woods = woods
            self.a = 0
            self.near_woods = []
            self.building = makeSprite(sawmill)
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
                self.near_woods[0].hp -= self.building.damage_to_trees
                changeSpriteImage(self.near_woods[0],1)
                self.building.wood += 1
                self.near_woods.pop(0)


    class quarry(object):
        def __init__(self, builder, stones):
            self.stones = stones
            self.a = 0
            self.near_stones = []
            self.building = makeSprite(quarry)
            self.building.x = builder.xpos
            self.building.y = builder.ypos
            for i in range(len(self.stones)):
                if (((self.stones[i].x - self.building.x) ** 2 + (
                    self.stones[i].y - self.building.y) ** 2) ** 0.5) <= 300:
                    self.near_stones.append(0)
                    self.near_stones[self.a] = self.stones[i]
                    self.a += 1
            self.building.hp = 200
            self.building.stones = 0
            self.building.damage_to_stones = 100
            moveSprite(self.building, self.building.x, self.building.y)
            showSprite(self.building)

        def stonecutting(self):
            if len(self.near_stones):
                self.near_stones[0].hp -= self.building.damage_to_stones
                changeSpriteImage(self.near_stones[0], 1)
                self.building.stones += 1
                self.near_stones.pop(0)

            '''
            self.woods = woods
            showSprite(self.collader_of_building)
            collectibles=allTouching(self.collader_of_building)
            hideSprite(self.collader_of_building)
            for collectible in collectibles:
                if collectible in self.woods:
                    collectible.hp -= 100
                    if collectible.hp <= 0:
                        changeSpriteImage(collectible,1)
                        
            print(len(self.collectibles))
            self.collectibles = allTouching(self.collader_of_building)
             for collectible in self.collectibles:
             if collectible not in self.woods:
             self.collectibles.remove(collectible)
             moveSprite(self.collectibles[0], 0 , 0)
            changeSpriteImage(self.collectibles[self.kost], 1)

            self.collectibles.remove(self.collectibles[0])
                self.collectibles[0].hp -= self.building.damage_to_trees
                if self.collectibles[0].hp <= 0:
                    changeSpriteImage(self.collectibles[0],1)
                    self.collectibles.popleft()
                self.kost += 1
                '''