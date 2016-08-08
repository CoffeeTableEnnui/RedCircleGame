import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(724,76,400,700)
level.addwall(50,  374, 102, 200)
level.addwall(426, 750, 102, 200)
level.addwall(50,  250, 200, 750)
level.addwall(550, 750, 200, 750)
enemy1 = c.SmallEnemy(400, 260)
enemy1.xdir = 1
enemy1.start, enemy1.end = 280, 520
level.addleftright(enemy1)
enemy2 = c.SmallEnemy(520, 320)
enemy2.xdir = 1
enemy2.start, enemy2.end = 280, 520
level.addleftright(enemy2)
enemy3 = c.SmallEnemy(400, 380)
enemy3.xdir = -1
enemy3.start, enemy3.end = 280, 520
level.addleftright(enemy3)
enemy4 = c.SmallEnemy(280, 440)
enemy4.xdir = -1
enemy4.start, enemy4.end = 280, 520
level.addleftright(enemy4)
enemy5 = c.SmallEnemy(400, 500)
enemy5.xdir = 1
enemy5.start, enemy5.end = 280, 520
level.addleftright(enemy5)
enemy6 = c.SmallEnemy(520, 560)
enemy6.xdir = 1
enemy6.start, enemy6.end = 280, 520
level.addleftright(enemy6)
enemy7 = c.SmallEnemy(400, 620)
enemy7.xdir = -1
enemy7.start, enemy7.end = 280, 520
level.addleftright(enemy7)
