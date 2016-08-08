import rectangles as r
import circles as  c
import games as g
import pygame

level = g.Game(111, 724, 724, 76)
level.addwall(701, 750, 102, 114)
level.addwall(689, 750, 114, 138)
level.addwall(665, 750, 138, 186)
level.addwall(617, 750, 186, 282)
level.addwall(521, 750, 282, 474)
level.addwall(329, 750, 474, 666)
level.addwall(137, 750, 666, 750)

level.addwall(50,  649, 50,  62)
level.addwall(50,  637, 62,  86)
level.addwall(50,  613, 86,  134)
level.addwall(50,  565, 134, 230)
level.addwall(50,  469, 230, 422)
level.addwall(50,  277, 422, 614)
level.addwall(50,  85,  614, 750)
