import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(100, 300, 700, 700)
level.addwall(300, 350, 400, 450)
level.addwall(250, 300, 200, 250)
level.addwall(250, 300, 450, 500)
level.addwall(200, 250, 250, 300)
level.addwall(250, 300, 300, 400)
level.addwall(400, 450, 600, 650)
level.addwall(500, 550, 350, 400)
level.addwall(200, 250, 600, 650)
level.addwall(150, 200, 650, 700)
level.addwall(600, 650, 700, 750)
level.addwall(500, 550, 550, 600)
level.addwall(450, 500, 500, 550)
level.addwall(50, 100, 500, 550)
level.addwall(300, 350, 700, 750)
level.addwall(550, 600, 400, 450)
level.addwall(700, 750, 500, 550)
level.addwall(600, 700, 350, 400)
level.addwall(450, 500, 150, 200)
level.addwall(700, 750, 100, 150)
level.addwall(650, 700, 50, 100)
