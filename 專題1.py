import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(3)
mc.postToChat('start mining in ')
time.sleep(1)
mc.postToChat('3 ')
time.sleep(1)
mc.postToChat('2')
time.sleep(1)
mc.postToChat('1')
time.sleep(1)
x,y,z=mc.player.getTilePos() #得到玩家位置

block_num=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            block_ID=mc.getBlock(x+i,y-j,z+k) #得到礦物ID
            if block_ID==56 or block_ID==14:  #判斷是否為寶物
                mc.postToChat('we find it!!!')
                block_num=block_num+1         #目前找到幾個寶物
            else:
                mc.setBlock(x+i,y-j,z+k,0)   #把廢物清掉
        mc.setBlock(x+i,y-j,z+k,50)#放火把
    mc.postToChat('we find {} good blocks now'.format(block_num))
mc.postToChat('end mining')
time.sleep(1)
mc.postToChat('total,we find {} good blocks'.format(block_num))
