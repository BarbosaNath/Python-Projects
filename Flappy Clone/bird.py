from globals import (
    pygame,
    WHITE,
    SCREEN,
    SCREEN_HEIGHT,
)
class Bird:
    def __init__(self, pos, size, gravity):
        self.size    = size
        self.pos     = pos
        self.gravity = gravity
        self.accel   = gravity
        self.isDead  = True
        self.points  = 0

    def flap(self):
        self.accel = -self.gravity  * 2

    def pipeCollide(self, pipe):
        if self.pos[0] + self.size[0] >= pipe.pos and self.pos[0] <= pipe.pos + pipe.width:
            if self.pos[1] - self.size[1] <= pipe.height - pipe.gap and self.pos[1] + self.size[1] >= 0:
                self.isDead = True
                pass
            if self.pos[1] + self.size[1] >= pipe.height and self.pos[1] - self.size[1] <= (SCREEN_HEIGHT/6) *5:
                self.isDead = True
                pass

    def score(self):
        self.points += 1

    def reset(self):
        self.points = 0
        self.isDead = False
        posList     = list(self.pos)
        posList[1]  = (int)((SCREEN_HEIGHT/6)*2.5)
        self.pos    = tuple(posList)
        self.accel  = 0


    def update(self):
        posList     = list(self.pos)
        posList[1] += self.accel
        self.pos    = tuple(posList)
        self.accel += (int)(self.gravity / 5)
        self.isDead = False
        if self.pos[1] - self.size[1] <= 0 or self.pos[1] + self.size[1] >= (SCREEN_HEIGHT/6) *5:
            self.isDead = True


    def render(self):
        pygame.draw.circle(SCREEN, WHITE, self.pos, self.size[0])
