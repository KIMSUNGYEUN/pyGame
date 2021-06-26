from math import sin, cos

class Ball:
    def __init__(self,direction,screen_size,radius,speed):
        self.d = direction
        self.dx=speed*sin(self.d)
        self.dy=speed*cos(self.d)
        
        self.x=screen_size[0]//2
        self.y=screen_size[1]//2
        self.r=10

        self.r_End=screen_size[0]-10
        self.l_End=10
        self.t_End = 10
        self.b_End = screen_size[1]-10

    def setNextPosition(self):
        if self.x > self.r_End or self.x < self.l_End:
            self.dx*=-1

        if self.y < self.t_End or self.y > self.b_End:
            self.dy*=-1
            
        self.x += self.dx
        self.y += self.dy

class Bar:
    def __init__(self,control_key,x,screen_size):
        self.kb=control_key
        self.x=x
        self.y=screen_size[1]//2

    def setNextPosition(self,pk):
        if pk[self.kb[0]]:
            self.y-=10
        if pk[self.kb[1]]:
            self.y+=10

