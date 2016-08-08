import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(700, 450, 450, 700)
level.addwall(50,  400, 50,  750)
level.addwall(400, 750, 50,  400)
level.addwall(400, 550, 400, 550)
level.addwall(600, 750, 600, 750)
