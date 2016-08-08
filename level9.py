import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(400, 700, 400, 100)
level.addwall(0, 350, 0, 339)
level.addwall(450, 800, 0, 339)
level.addwall(0, 350, 460, 800)
level.addwall(450, 800, 460, 800)
level.addwall(0, 225, 339, 460)
level.addwall(574, 800, 339, 460)
enemy0 = c.BigEnemy(290, 400)
enemy0.xdir = -1
enemy0.start, enemy0.end = 290, 510
level.addleftright(enemy0)
