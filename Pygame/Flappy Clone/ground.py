from globals import (
    pygame,
    SCREEN,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
class Ground:
    def __init__(self, pos, size, speed, color):
        self.pos   =   pos
        self.size  =  size
        self.speed = speed
        self.color = color

    def update(self):
        self.pos -= self.speed
        if self.pos == -SCREEN_WIDTH:
            self.pos =  SCREEN_WIDTH


    def render(self):
        pygame.draw.rect(SCREEN, self.color, (self.pos, SCREEN_HEIGHT - self.size, SCREEN_WIDTH, self.size))
