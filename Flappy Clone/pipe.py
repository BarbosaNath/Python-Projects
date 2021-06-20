from globals import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SCREEN,
    pygame,
)
from random import randint
class Pipe:
    def __init__(self, pos, width, gap, color, speed):
        self.pos    = pos
        self.width  = width
        self.height = randint(gap, (SCREEN_HEIGHT/6)*5)
        self.gap    = gap
        self.speed  = speed
        self.color  = color

    def newHeight(self):
        self.height = randint(self.gap, (SCREEN_HEIGHT/6)*5)

    def update(self, bird):
        self.pos -= self.speed

        if self.pos + self.width == bird.pos[0]:
            if not bird.isDead: bird.score()
        if self.pos <= -self.width:
            self.newHeight()
            self.pos = SCREEN_WIDTH * 2 - self.width


    def render(self):
        pygame.draw.rect(SCREEN, self.color, (self.pos, self.height, self.width, (int)((SCREEN_HEIGHT / 6)*5) - self.height))
        pygame.draw.rect(SCREEN, self.color, (self.pos,           0, self.width,              self.height - self.gap   ))
