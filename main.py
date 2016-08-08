import rectangles
import pygame
import circles
import level0, level1, level2, level3, level4, \
       level5, level6, level7, level8, level9, \
       level10, level11, level12, level13, level14, \
       level15, level16, level17, level18, level19, \
       level20, level21, level22, level23, level24, \
       level25, level26, level27, level28, level29


class LevelSelect:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED   = (255, 0, 0)
    levelbuttons = []
    levels       = {}
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        font  = pygame.font.Font(None, 50)
        levelselect = True
        file = open("highscores.txt", "r")
        scores = file.readlines()
        #backbutton = rectangles.BackButton(25, 25)
        #starting constants
        size = width, height = 800, 800
        screen = pygame.display.set_mode(size)
        #starting objects
        mouse    = circles.Mouse()
        #screen draw
        screen.fill(self.WHITE)
        while levelselect == True:
            pygame.event.get()
            # screenfill
            screen.fill(self.WHITE)
            #button draw
            if pygame.key.get_pressed()[pygame.K_p]: levelselect = False
            #backbutton.draw(screen)
            for i in self.levelbuttons:
                i.draw(screen)
            # mouse
            mouse.get_pos()
            for i in self.levelbuttons:
                if i.collide(mouse):
                    i.colour = self.RED
                    try: 
                        screen.blit(font.render("BEST SCORE: " + str(int(scores[int(i.num)])), 
                                                0, self.BLACK, self.WHITE), 
                                                (100, 700))
                    except ValueError:
                        screen.blit(font.render("BEST SCORE: --", 
                                                0, self.BLACK, self.WHITE), 
                                                (100, 700))
                if not i.collide(mouse):
                    i.colour = self.WHITE
                if pygame.mouse.get_pressed()[0] and i.colour == self.RED:
                    bestscore = scores[int(i.num)] if scores[int(i.num)] != "" else float(inf)
                    lastscore = str(self.levels[i.num].run())
                    try:
                        if int(lastscore) < int(bestscore): print "NEW HIGHSCORE: %s" % lastscore
                        bestscore = min(int(bestscore), int(lastscore))
                    except ValueError:
                        pass
                    scores[int(i.num)] = str(bestscore) + "\n"  
                    file = open('highscores.txt', 'w')
                    file.writelines(scores)       
            #update display
            clock.tick(60)
            pygame.display.update()
    def addlevelbutton(self, name, x_pos, y_pos, level_mod):
        levelbutton = rectangles.LevelButton(name, x_pos, y_pos)
        self.levelbuttons.append(levelbutton)
        self.levels[name] = level_mod.level

menu = LevelSelect()
menu.addlevelbutton("00", 100, 100, level0)
menu.addlevelbutton("01", 200, 100, level1)
menu.addlevelbutton("02", 300, 100, level2)
menu.addlevelbutton("03", 400, 100, level3)
menu.addlevelbutton("04", 500, 100, level4) 
menu.addlevelbutton("05", 600, 100, level5)
menu.addlevelbutton("06", 100, 200, level6)
menu.addlevelbutton("07", 200, 200, level7)
menu.addlevelbutton("08", 300, 200, level8)
menu.addlevelbutton("09", 400, 200, level9)
menu.addlevelbutton("10", 500, 200, level10)
menu.addlevelbutton("11", 600, 200, level11)
menu.addlevelbutton("12", 100, 300, level12)
menu.addlevelbutton("13", 200, 300, level13)
menu.addlevelbutton("14", 300, 300, level14)
menu.addlevelbutton("15", 400, 300, level15)
menu.addlevelbutton("16", 500, 300, level16)
menu.addlevelbutton("17", 600, 300, level17)
menu.addlevelbutton("18", 100, 400, level18)
menu.addlevelbutton("19", 200, 400, level19) 
menu.addlevelbutton("20", 300, 400, level20)
menu.addlevelbutton("21", 400, 400, level21)
menu.addlevelbutton("22", 500, 400, level22)
menu.addlevelbutton("23", 600, 400, level23)
menu.addlevelbutton("24", 100, 500, level24) 
menu.addlevelbutton("25", 200, 500, level25) 
menu.addlevelbutton("26", 300, 500, level26) 
menu.addlevelbutton("27", 400, 500, level27)
menu.addlevelbutton("28", 500, 500, level28)
menu.addlevelbutton("29", 600, 500, level29) 
menu.run()
