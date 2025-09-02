import thing
class Baloon(thing.thing):
    def __init__(self,coin):
        x=coin.position_x
        y=coin.position_y-16
        super().__init__(x,y)

    def hit_player(self,player):
        if abs(self.position_x - player.position_x) < 12 and abs(self.position_y - player.position_y) < 12:
            return True

    def move(self):
        # 左に移動
        self.position_x -= 0.5
        self.position_y -= 1

                    

        