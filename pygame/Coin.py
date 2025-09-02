import thing
from random import randint
class Coin(thing.thing):
    def __init__(self):
        rand_x = randint(20,180)
        rand_y = randint(128,140)
        super().__init__(rand_x, rand_y)
        self.falling=False
        self.active=True

    def hit_player(self,player):
        if abs(self.position_x - player.position_x) < 12 and abs(self.position_y - player.position_y) < 12:
            return True

    def move(self):
        # 左に移動
        self.position_x -= 0.5
        self.position_y-=1
    
    def fall(self):
        self.position_y+=3

    def overScreen(self):
        if self.position_x < -16 or self.position_y < -16:
            return True
        if (self.falling == True) and (self.position_y>144):

            return True
