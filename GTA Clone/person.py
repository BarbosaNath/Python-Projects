from entity import Entity
class Person(Entity):
    def __init__(self, position, size, image_path):
       super().__init__(position, size, image_path)
       self.isAlive = True
       self.health_points = 100
