import rectangles
import circles
import pygame

class Game:
    pygame.init()
    WHITE = (255, 255, 255)
    def __init__(self, player_x, player_y, goal_x, goal_y):
        self.player_x = player_x
        self.player_y = player_y
        self.goal_x   = goal_x
        self.goal_y   = goal_y
        self.walls = []
        self.updowns = []
        self.leftrights = []
    def addwall(self, xmin, xmax, ymin, ymax):
        wall  = rectangles.Wall(xmin, xmax, ymin, ymax)
        self.walls.append(wall)
    def addleftright(self, enemy):
        self.leftrights.append(enemy)
        enemy.x_init = enemy.x
        enemy.y_init = enemy.y
        enemy.xdir_init = enemy.xdir
    def addupdown(self, enemy):
        self.updowns.append(enemy)
        enemy.x_init = enemy.x
        enemy.y_init = enemy.y
        enemy.ydir_init = enemy.ydir
    def run(self):
        clock = pygame.time.Clock()
        font  = pygame.font.Font(None, 50)
        gameover = [False, False]
        score = 0
        #starting constants
        size = width, height = 800, 800
        screen = pygame.display.set_mode(size)
        #starting objects
        border = rectangles.Border(50, width, height)
        goal   = circles.Goal(self.goal_x, self.goal_y)
        player = circles.Player(self.player_x, self.player_y)
        circle = circles.Circle(0, 0)
        circle.colour = self.WHITE
        #enemy reset
        for i in self.leftrights:
            i.x = i.x_init
            i.y = i.y_init
            i.xdir = i.xdir_init  
        for i in self.updowns:
            i.x = i.x_init
            i.y = i.y_init
            i.ydir = i.ydir_init            
        #screen draw
        screen.fill(self.WHITE)
        #border draw
        border.draw(screen)
        #walls draw
        for i in self.walls:
            i.draw(screen)
        #goal draw
        goal.draw(screen)    
        while gameover[0] == False:
            pygame.event.get()
            #border collide
            if border.collide(player): gameover[0] = True
            #wall collide
            for i in self.walls:
                if i.collide(player):
                    gameover[0] = True  
            #goal collide
            if goal.collide(player): gameover = (True, True)
            #player move
            w = pygame.key.get_pressed()[pygame.K_w]
            a = pygame.key.get_pressed()[pygame.K_a]
            s = pygame.key.get_pressed()[pygame.K_s]
            d = pygame.key.get_pressed()[pygame.K_d]
            circle.x, circle.y, circle.size = player.x, player.y, player.size
            circle.draw(screen)
            player.move(w, a, s, d)
            player.draw(screen)
            #enemy move
            for i in self.leftrights:
                circle.x, circle.y, circle.size = i.x, i.y, i.size
                circle.draw(screen)
                i.leftright(i.start, i.end)
                i.draw(screen)
                if i.collide(player): 
                    gameover[0] = True
            for i in self.updowns:
                circle.x, circle.y, circle.size = i.x, i.y, i.size
                circle.draw(screen)
                i.updown(i.start, i.end)
                i.draw(screen)
                if i.collide(player): 
                    gameover[0] = True
            # update score 
            score += 1
            renderscore = font.render(str(score), 0, self.WHITE, (0, 0, 0))
            screen.blit(renderscore, (50, 760))
            #update display
            clock.tick(60)
            pygame.display.update()            
        if gameover[1] == True: 
            return score
        else: return 9999999999
            

