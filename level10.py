import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(100, 600, 700, 200)
level.addwall(0, 339, 0, 550)
level.addwall(0, 339, 650, 800)
level.addwall(460, 750, 0, 150)
level.addwall(460, 750, 250, 750)
enemy0 = c.BigEnemy(400, 400)
enemy0.ydir = 1
enemy0.start, enemy0.end = 113, 687
level.addupdown(enemy0)
