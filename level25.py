import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(100, 700, 100, 100)
level.addwall(50, 600, 390, 410)
level.addwall(160, 180, 50, 189)
level.addwall(390, 410, 690, 710)
enemy0 = c.SmallEnemy(79, 200)
enemy0.xdir = -1
enemy0.start, enemy0.end = 79, 727
level.addleftright(enemy0)
enemy1 = c.SmallEnemy(151, 250)
enemy1.xdir = 1
enemy1.start, enemy1.end = 79, 727
level.addleftright(enemy1)
enemy2 = c.SmallEnemy(223, 300)
enemy2.xdir = 1
enemy2.start, enemy2.end = 79, 727
level.addleftright(enemy2)
enemy3 = c.SmallEnemy(295, 350)
enemy3.xdir = 1
enemy3.start, enemy3.end = 79, 727
level.addleftright(enemy3)
enemy4 = c.SmallEnemy(439, 450)
enemy4.xdir = 1
enemy4.start, enemy4.end = 79, 727
level.addleftright(enemy4)
enemy5 = c.SmallEnemy(511, 500)
enemy5.xdir = 1
enemy5.start, enemy5.end = 79, 727
level.addleftright(enemy5)
enemy6 = c.SmallEnemy(583, 550)
enemy6.xdir = 1
enemy6.start, enemy6.end = 79, 727
level.addleftright(enemy6)
enemy7 = c.SmallEnemy(655, 600)
enemy7.xdir = 1
enemy7.start, enemy7.end = 79, 727
level.addleftright(enemy7)
enemy8 = c.SmallEnemy(727, 650)
enemy8.xdir = 1
enemy8.start, enemy8.end = 79, 727
level.addleftright(enemy8)
