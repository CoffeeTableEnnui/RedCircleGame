import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(100, 250, 705, 350)
level.addwall(0, 800, 0, 200)
level.addwall(0, 800, 400, 800)
level.addwall(150, 160, 200, 320)
level.addwall(250, 260, 280, 400)
level.addwall(350, 360, 200, 320)
level.addwall(450, 460, 280, 400)
level.addwall(550, 560, 200, 320)
level.addwall(650, 660, 280, 400)
