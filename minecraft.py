import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

Stone = block.STONE.id
Gold = block.GOLD_BLOCK.id
FlowerC = block.FLOWER_CYAN.id
FlowerY = block.FLOWER_YELLOW.id
Grass = block.GRASS.id
TNT = block.TNT.id
Lava = block.LAVA.id
Glowstone = block.GLOWSTONE_BLOCK.id

pos = mc.player.getTilePos()

mc.setBlocks(pos.x-1,pos.y,pos.z+3,
             pos.x+1,pos.y+2,pos.z+3,
             block.STONE.id)

blocksLit = 0
points = 0

mc.postToChat("Get ready...")
time.sleep(2)
mc.postToChat("Go")

while blocksLit < 9: 
    time.sleep(1)
    blocksLit = blocksLit +1
    lightCreated = False
    while not lightCreated:
        xPos = pos.x + random.randint(-1,1)
        yPos = pos.y + random.randint(0,2)
        zPos = pos.z + 3
        if mc.getBlock(xPos,yPos,zPos) == block.STONE.id:
            mc.setBlock(xPos,yPos,zPos,Glowstone)
            lightCreated = True
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
            mc.setBlock(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z,block.STONE.id)
            blocksLit = blocksLit -1
            points = points +1
mc.postToChat("Game Over - Points = " + str(points))
          

#mc.setBlocks(x,y,z)

#while True:
   # x,y,z = mc.player.getPos() #player position (x,y,z)
    #blockBeneath = mc.getBlock(x,y-1,z) #get the block ID
   # if blockBeneath == Grass:
            #mc.setBlock(x,y,z, FlowerC)
    #else:
        #mc.setBlock(x,y-1,z, Grass)
#sleep(0.5)
    
#thisBlock = mc.getBlock(x,y,z) #block ID

