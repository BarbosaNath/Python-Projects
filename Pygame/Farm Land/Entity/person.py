from Entity.entity import Entity


class Person(Entity):
    def __init__(self, position, size, image_path, scale=(1, 1)):
        super().__init__(position, size, image_path, scale)
        self.isAlive = True
        self.health_points = 100
