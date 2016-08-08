import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(100, 700, 700, 100)
level.addwall(0, 350, 0, 299)
level.addwall(0, 350, 320, 479)
level.addwall(0, 350, 500, 650)
level.addwall(450, 750, 150, 299)
level.addwall(450, 750, 320, 479)
level.addwall(450, 750, 500, 750)
enemy0 = c.SmallEnemy(729, 310)
enemy0.xdir = 1
enemy0.start, enemy0.end = 73, 729
level.addleftright(enemy0)
enemy1 = c.SmallEnemy(73, 490)
enemy1.xdir = -1
enemy1.start, enemy1.end = 73, 729
level.addleftright(enemy1)
