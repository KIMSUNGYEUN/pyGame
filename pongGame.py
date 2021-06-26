import pygame, sys
from pygame.locals import *
from math import pi
import random
from pongClass import *
pygame.init()
screen=pygame.display.set_mode((600,400))
WHITE=(255,255,255); RED=(255,0,0); BLACK=(0,0,0)
FPS=pygame.time.Clock()
size=screen.get_size()

class BALL(Ball):
    def __init__(self,direction,screen_size,radius,speed):
        super().__init__(direction,screen_size,radius, speed)

    def drawing(self):
        pygame.draw.circle(screen,BLACK,\
                           (self.x,self.y),self.r,0)
        

class BAR(Bar):
    def __init__(self,ck,x,screen_size):
        Bar.__init__(self,ck,x,screen_size)

    def drawing(self):
        pygame.draw.line(screen,BLACK, \
                         (self.x,self.y-40),(self.x,self.y+40),6)

ball = BALL(pi/3*random.random()+pi/3,size,10,15)
Bars = [BAR((K_a,K_z),10,size), BAR((K_UP, K_DOWN),590,size)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressedKey=pygame.key.get_pressed()
    screen.fill(WHITE)

    ball.setNextPosition()
    ball.drawing()

    for bar in Bars:
        bar.setNextPosition(pressedKey)
        bar.drawing()
    pygame.display.update()
    FPS.tick(24)

