import pygame

class Rectangle:
    def collide(self, circle):
        x_range = range(self.xmin - circle.size, self.xmax + circle.size)
        y_range = range(self.ymin - circle.size, self.ymax + circle.size)
        return circle.x in x_range and circle.y in y_range

class LevelButton(Rectangle):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    width   = 75
    height  = 75
    pygame.init()
    colour  = WHITE
    fill    = BLACK
    font  = pygame.font.Font(None, 75)
    def __init__(self, levelnumber, xmin, ymin):
        self.num  = levelnumber
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmin + self.width
        self.ymax = ymin + self.height
    def draw(self, background):
        pygame.draw.polygon(background,
                            self.BLACK,
                            [(self.xmax, self.ymax),
                             (self.xmax, self.ymin),
                             (self.xmin, self.ymin),
                             (self.xmin, self.ymax),],
                            0)
        renderlevelbutton = self.font.render(str(self.num), 0, self.colour, self.fill)
        background.blit(renderlevelbutton, (self.xmin, self.ymin))

class BackButton(Rectangle):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    width   = 125
    height  = 50
    pygame.init()
    colour  = WHITE
    fill    = BLACK
    font  = pygame.font.Font(None, 50)
    def __init__(self, xmin, ymin):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmin + self.width
        self.ymax = ymin + self.height
    def draw(self, background):
        pygame.draw.polygon(background,
                            self.BLACK,
                            [(self.xmax, self.ymax),
                             (self.xmax, self.ymin),
                             (self.xmin, self.ymin),
                             (self.xmin, self.ymax),],
                            0)
        renderbackbutton = self.font.render("BACK", 0, self.colour, self.fill)
        background.blit(renderbackbutton, (self.xmin, self.ymin))
        
    
class Wall(Rectangle):
    colour = (0, 0, 0)
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
    def draw(self, background):
        pygame.draw.polygon(background, 
                            self.colour, 
                            [(self.xmax, self.ymax), 
                             (self.xmax, self.ymin), 
                             (self.xmin, self.ymin), 
                             (self.xmin, self.ymax),], 
                            0)
                            
    
class Border:
    colour = (0, 0, 0)
    def __init__(self, thickness, width, height):
        self.thick = thickness
        self.height = height
        self.width = width
    def draw(self, background):
        pygame.draw.polygon(background, self.colour, 
                            [(self.thick, self.thick), (self.thick, 0), (self.width - self.thick, 0), (self.width - self.thick, self.thick),], 
                            0)
        pygame.draw.polygon(background, self.colour, 
                            [(self.thick, self.height), (self.thick, 0), (0, 0), (0, self.height),], 
                            0)
        pygame.draw.polygon(background, self.colour, 
                            [(self.width - self.thick, self.height), (self.width - self.thick, 0), (self.width, 0), (self.width, self.height),], 
                            0)
        pygame.draw.polygon(background, self.colour, 
                            [(self.thick, self.height), (self.thick, self.height - self.thick), 
                             (self.width - self.thick, self.height - self.thick), (self.width - self.thick, self.height),], 
                            0)
    def collide(self, circle):
        x_range = range(self.thick + circle.size, self.width - self.thick - circle.size)
        y_range = range(self.thick + circle.size, self.height - self.thick - circle.size)
        return not (circle.x in x_range and circle.y in y_range)


