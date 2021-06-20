import pygame

class Map:
    def __init__(self, _map, _square):
        self.map       = _map    # the map shape
        self.square    = _square # the size of each map cell 
        self.playerPos = (75,75)
        self.mapW      = 0
        self.mapH      = 0

        _y = _x = 0
        for i in self.map:
            if (i == "\n"):
                self.mapW = _x
                _x  = 0
                _y += 1
            else: _x += 1
        self.mapH = _y + 1


    def draw(self, _surface):
        _y = _x = 0
        
        for i in self.map:
            if (i == "#"):
                pygame.draw.rect(_surface,(255,255,255), (_x*self.square+2, _y*self.square+2, self.square-2, self.square-2))
                _x += 1
            
            if (i == "."):
                pygame.draw.rect(_surface,(  0,  0,  0), (_x*self.square+2, _y*self.square+2, self.square-2, self.square-2))
                _x += 1

            if (i == "\n"):
                _x  = 0
                _y += 1
            if (i == "P"):
                pygame.draw.rect(_surface,(  0,  0,  0), (_x*self.square+2, _y*self.square+2, self.square-2, self.square-2))
                _x += 1
                self.playerPos = (_x * self.square, _y * self.square) 

    def getPX(self):
        _y = _x = 0
        
        for i in self.map:
            if (i == "P" ): self.playerPos = (_x * self.square + self.square / 2, _y * self.square + self.square / 2)
            elif (i == "\n"): _x  = 0; _y += 1
            else: _x += 1

        return self.playerPos[0]
    def getPY(self):
        _y = _x = 0
        
        for i in self.map:
            if (i == "P" ): self.playerPos = (_x * self.square + self.square / 2, _y * self.square + self.square / 2)
            elif (i == "\n"): _x  = 0; _y += 1
            else: _x += 1

        return self.playerPos[1]