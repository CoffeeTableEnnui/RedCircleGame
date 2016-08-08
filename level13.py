import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(700, 700, 100, 100)
level.addwall(50, 350, 450, 750)
level.addwall(450, 750, 50, 350)
enemy0 = c.SmallEnemy(400, 400)
enemy0.ydir = -1
enemy0.start, enemy0.end = 73, 732
level.addupdown(enemy0)
enemy1 = c.SmallEnemy(400, 400)
enemy1.xdir = -1
enemy1.start, enemy1.end = 73, 732
level.addleftright(enemy1)
