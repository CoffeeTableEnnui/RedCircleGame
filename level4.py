import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(150, 100, 450, 400)
level.addwall(200, 400, 50,  600)
level.addwall(50,  100, 50,  750)
level.addwall(100, 750, 700, 750)
level.addwall(500, 750, 50,  700)
level.addwall(400, 500, 50,  350)
