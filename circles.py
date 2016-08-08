import pygame

class Circle:
    colour = (255, 255, 255)
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position    
    def down(self):
        self.y += self.speed 
    def up(self):
        self.y -= self.speed        
    def left(self):
        self.x -= self.speed 
    def right(self):
        self.x += self.speed
    def draw(self, background):
        pygame.draw.circle(background, self.colour, (self.x, self.y), self.size, 0) 
    def collide(self, circle):
        return ((abs(self.x - circle.x))**2. + (abs(self.y - circle.y))**2.)**.5 < self.size + circle.size 

class Mouse:
    size = 0    
    def get_pos(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
    
class Enemy(Circle):
    colour = (0, 0, 0)
    def leftright(self, start, end):
        if self.x <= start or self.x >= end:
            self.xdir *= -1
        if self.xdir == 1:
            self.right()
        if self.xdir == -1:
            self.left()
    def updown(self, start, end):
        if self.y <= start or self.y >= end:
            self.ydir *= -1
        if self.ydir == 1:
            self.down()
        if self.ydir == -1:
            self.up()

class BigEnemy(Enemy):
    size = 60
    speed = 4

class SmallEnemy(Enemy):
    size = 10
    speed = 12

class Player(Circle):
    size = 25
    speed = 6
    colour = (255, 0, 0)
    def move(self, w, a, s, d):
        if w: self.up()
        if a: self.left()
        if s: self.down()
        if d: self.right()

class Goal(Circle):
    size = 10
    speed = 0
    colour = (255, 215, 0)
