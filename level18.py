import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(724, 76, 230, 688)
level.addwall(150,200,150,200)
level.addwall(375,425,150,200)
level.addwall(150,750,200,400)
level.addwall(150,630,550,600)
level.addwall(150,200,600,750)
level.addwall(600,750,102,200)
enemy0 = c.SmallEnemy(700,436)
enemy0.ydir = -1
enemy0.start, enemy0.end = 436,724
level.addupdown(enemy0)
enemy1 = c.SmallEnemy(76,100)
enemy1.xdir = -1
enemy1.start, enemy1.end = 76,580
level.addleftright(enemy1)
enemy2 = c.SmallEnemy(100,220)
enemy2.ydir = -1
enemy2.start, enemy2.end = 220,724
level.addupdown(enemy2)
