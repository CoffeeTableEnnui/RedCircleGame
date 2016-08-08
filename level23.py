import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(172, 76, 172, 724)
level.addwall(208, 712, 722, 750)
level.addwall(185, 640, 520, 650)
level.addwall(208, 712, 418, 448)
level.addwall(185, 640, 214, 346)
level.addwall(208, 712, 50,  142)
level.addwall(712, 750, 50,  750)
level.addwall(50,  136, 50,  750)
enemy1 = c.SmallEnemy(172, 400)
enemy1.ydir = -1
enemy1.start, enemy1.end = 182, 686
level.addupdown(enemy1)
