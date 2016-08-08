import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(700, 100, 100, 100)
level.addwall(50,  100, 200, 750)
level.addwall(100, 200, 300, 750)
level.addwall(200, 300, 400, 750)
level.addwall(300, 400, 500, 750)
level.addwall(400, 500, 600, 750)
level.addwall(500, 600, 700, 750)
level.addwall(500, 600, 50,  400)
level.addwall(400, 500, 50,  300)
level.addwall(300, 400, 50,  200)
level.addwall(200, 300, 50,  100)
