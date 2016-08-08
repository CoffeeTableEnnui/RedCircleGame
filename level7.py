import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(400, 700, 400, 100)
level.addwall(0, 350, 0, 385)
level.addwall(450, 800, 0, 385)
level.addwall(0, 350, 415, 800)
level.addwall(450, 800, 415, 800)
enemy0 = c.SmallEnemy(400, 400)
enemy0.xdir = -1
enemy0.start, enemy0.end = 73, 729
level.addleftright(enemy0)
