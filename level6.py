import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(400, 700, 400, 100)
level.addwall(0, 350, 0, 339)
level.addwall(450, 800, 0, 339)
level.addwall(0, 350, 460, 800)
level.addwall(450, 800, 460, 800)
enemy0 = c.BigEnemy(115, 400)
enemy0.xdir = -1
enemy0.start, enemy0.end = 115, 686
level.addleftright(enemy0)
