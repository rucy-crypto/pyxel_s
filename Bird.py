import thing
import random
from random import randint
class Bird(thing.thing):
    def __init__(self):
        x = randint(180,300)
        y = randint(0,128)
        super().__init__(x, y)
        self.speed = randint(2,5)

    def move(self):
        self.position_x -= self.speed

    def hit_player(self,player):
        if abs(self.position_x - player.position_x) < 12 and abs(self.position_y - player.position_y) < 12:
            return True

    def overScreen(self):
        if self.position_x < -16:
            return True