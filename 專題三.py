from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random
#得到玩家位置
x_start,y_start,z_start=mc.player.getTilePos()
#在腳下放一片TNT
mc.setBlocks(x_start-20,y_start-1,z_start-20,x_start+20,y_start-1,z_start+20,46)
time.sleep(3)
mc.postToChat('start in ')
time.sleep(1)
mc.postToChat('3 ')
time.sleep(1)
mc.postToChat('2')
time.sleep(1)
mc.postToChat('1')
time.sleep(1)
mc.postToChat("game start")
while True:
    x,y,z=mc.player.getTilePos()
    a=random.randrange(-20,21)
    b=random.randrange(-20,21)
    mc.setBlock(x_start+a,y_start+30,z_start+b,145)
    time.sleep(0.2)
    mc.setBlock(x_start+a,y_start-1,z_start+b,0)
    if y<y_start:
        mc.postToChat('you lose QQ')
        break
