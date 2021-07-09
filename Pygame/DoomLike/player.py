import pygame
from math import pi  as PI
from math import tan as TAN
from math import cos as COS
from math import sin as SIN
from math import sqrt
DR    = 0.0174533

class Player:
    def __init__(self, _x, _y, _vel, _dx, _dy, _a, _fov, _res=1):
        self.x   = _x
        self.y   = _y
        self.vel = _vel
        self.dx  = COS(_dx) * self.vel
        self.dy  = SIN(_dy) * self.vel
        self.a   = _a
        self.fov = _fov
        self.res = _res

    def getX(): return self.x
    def getY(): return self.y

    def draw(self, _win):
        pygame.draw.circle( _win, (255,255,0), (int(self.x), int(self.y)), 10)
        pygame.draw.aaline( _win, (255,255,0), (int(self.x), int(self.y)), (self.x+self.dx*15,self.y+self.dy*15))



class Ray:
    def __init__(self, _p, _m, _o):
        self.x = 0        # Ray X position
        self.y = 0        # Ray Y position
        self.p = _p       # Player object
        self.o = _o       # Ray offset
        self.a = self.p.a-self.o # Ray angle
        self.m = _m       # Map object

        self.original_color= None
        self.color         = (0,255,0)
        self.change        = False
        self.dist_change   = False


        self.mx    = 0 # Map X
        self.my    = 0 # Map Y
        self.mp    = 0 # Map position
        self.dof   = 0 # Depth of field
        self.maxdof= 8 # Max value to the Depth of field
        self.xo    = 0 # X offset
        self.yo    = 0 # Y offset

        self.dof = 0

        self.distT = 0
        
    def dist(self, ax, ay, bx, by):
        return (sqrt( (bx - ax)*(bx - ax) + (by - ay)*(by - ay) ))

    

    def color_wall(self, _c):
        color_temp = [self.color[0], self.color[1], self.color[2]]
        if not self.change:
            for i in range(len(color_temp)):
                color_temp[i] += _c
                if color_temp[i] > 255: color_temp[i] = 255
                if color_temp[i] <   0: color_temp[i] =   0
            self.color = tuple(color_temp)



    def update(self):
        aTan = -1/TAN(self.a)
        nTan = -1*TAN(self.a)

        distV = 1000000
        distH = 1000000
        
        vx = self.p.x
        vy = self.p.y
        
        hx = self.p.x
        hy = self.p.y


        self.a = self.p.a-self.o

        if (self.a < 0   ): self.a += 2 * PI
        if (self.a > 2*PI): self.a -= 2 * PI

        # Vertical Check ---------------------------------------------------
        self.dof = 0


        if self.a > PI/2 and self.a < (3*PI)/2: # Looking left
            self.x = int(self.p.x/self.m.square)*self.m.square-0.00000001
            self.y = (self.p.x-self.x) * nTan + self.p.y
            self.xo= -self.m.square
            self.yo= -self.xo*nTan

        if self.a < PI/2 or self.a > (3*PI)/2: # Looking right
            self.x = int(self.p.x/self.m.square)*self.m.square + self.m.square
            self.y = (self.p.x-self.x) * nTan + self.p.y
            self.xo=  self.m.square
            self.yo= -self.xo*nTan

        if self.a == 0 or self.a == PI : #up down
            self.x   = self.p.x
            self.y   = self.p.y
            self.dof = self.maxdof

        while self.dof < self.maxdof:
            self.mx = int( int(self.x)/self.m.square)
            self.my = int( int(self.y)/self.m.square)
            self.mp = self.my*(self.m.mapW+1)+self.mx
            
            if self.mp > 0 and self.mp < (self.m.mapW*self.m.mapH+self.m.mapW-1) and self.m.map[self.mp] == '#':
                vx = self.x
                vy = self.y
                distV = self.dist(self.p.x,self.p.y,vx,vy)
                self.dof = self.maxdof
            else:
                self.x   += self.xo
                self.y   += self.yo
                self.dof += 1


     
        # Horizontal Check -------------------------------------------------
        
        hx = self.p.x
        hy = self.p.y

        self.dof = 0


        if self.a > PI: # Looking UP
            self.y = int(self.p.y/self.m.square)*self.m.square -0.00000001
            self.x = (self.p.y-self.y) * aTan + self.p.x
            self.yo= -self.m.square
            self.xo= -self.yo*aTan

        if self.a < PI: # Looking DOWN
            self.y = int(self.p.y/self.m.square)*self.m.square +self.m.square
            self.x = (self.p.y-self.y) * aTan + self.p.x
            self.yo=  self.m.square
            self.xo= -self.yo*aTan

        if self.a == 0 or self.a == PI : #looking left/right 
            self.x   = self.p.x
            self.y   = self.p.y
            self.dof = self.maxdof

        while self.dof < self.maxdof:
            self.mx = int(self.x/self.m.square)
            self.my = int(self.y/self.m.square)
            self.mp = self.my*(self.m.mapW+1)+self.mx#-self.m.mapW
            
            if self.mp > 0 and self.mp < (self.m.mapW*self.m.mapH+self.m.mapW-1) and self.m.map[self.mp] == '#':
                hx = self.x
                hy = self.y
                distH = self.dist(self.p.x,self.p.y,hx,hy)

                self.dof = self.maxdof
            else:
                self.x   += self.xo
                self.y   += self.yo
                self.dof += 1
        


        if self.original_color == None: self.original_color = [self.color[0], self.color[1], self.color[2]]



        # Check smaller -------------------------------------------------
        if distH<distV: self.x = hx; self.y = hy; self.distT = distH
        if distV<distH: self.x = vx; self.y = vy; self.distT = distV
        # ---------------------------------------------------------------


        #if self.distT/self.m.square >  1:
        #    self.color_wall(-200)
        #    self.dist_change = True

        #if self.distT/self.m.square <= 1:
        #    self.color = tuple(self.original_color)
        #    self.dist_change = False

        if distH<distV: 
            self.color_wall(-100)
            self.change = True
            
        if distV<distH:
            self.x = vx; self.y = vy; self.distT = distV
            self.color = tuple(self.original_color)
            self.change = False


    def draw(self, _win):
        pygame.draw.aaline(_win, self.color, (self.p.x, self.p.y), (int(self.x), int(self.y)))

    def draw_wall(self, _win, _screenSize, _ww, _x=0):
        da = self.p.a - self.a  # Delta Angle

        if (da < 0   ): da += 2 * PI
        if (da > 2*PI): da -= 2 * PI

        self.distT *= COS(da)

        teste = ((-1*(self.o/DR))*_ww)-(-1*(self.o/DR))

        lineH = (self.m.square*_screenSize)/self.distT
        lineO = _screenSize/2 - lineH/2
        lineX = int((-1*(self.o/DR)*_ww)*self.p.res -0.0000000001) +400

        #if lineH > _screenSize: lineH = _screenSize

        if lineO < 0 or lineO > _screenSize: lineO = 0
        if lineH < -_screenSize or lineH > _screenSize: lineH = _screenSize
    

        print (self.distT)
        
        pygame.draw.line(_win,  self.color, (lineX, lineO), (lineX, lineH+lineO), _ww)

