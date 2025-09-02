import thing
import math
import numpy as np
import pyxel
class Player(thing.thing):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.rotateCount = 0 
        self.rotate_x = 0
        self.rotate_y = 0
        self.r = 20
        #1フレームに4度
        self.rotate_distance = 10
        self.speed = 4

    #回転スタート
    def startRotate(self):
        self.rotateCount = self.rotate_distance
        self.rotate_x=self.position_x
        self.rotate_y=self.position_y - self.r
    #回転中
    def rotate(self):
        rad = math.radians(self.rotateCount)
        self.position_x = self.rotate_x + np.sin(rad)*self.r
        self.position_y = self.rotate_y + np.cos(rad)*self.r
        self.rotateCount += self.rotate_distance
    #回転終了
    def endRotate(self):
        self.rotateCount=0
        self.position_x=self.rotate_x
        self.position_y=self.rotate_y + self.r

    #ここで出てくるpyxelとかpyxel.widthとかがよくわからない
    def move(self):
            # max関数 min関数で画面外に行かないようにしているのか
        if pyxel.btn(pyxel.KEY_LEFT):
            self.position_x = max(self.position_x - self.speed, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.position_x = min(self.position_x + self.speed, pyxel.width - 16)
        if pyxel.btn(pyxel.KEY_UP):
            self.position_y = max(self.position_y - self.speed, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.position_y = min(self.position_y + self.speed, pyxel.height - 16)

        # key入力
        if (self.rotateCount) > 0 and (self.rotateCount) < 360:
            self.rotate()
            if self.rotateCount==360:
                self.endRotate()
        if self.rotateCount==0:
            if pyxel.btn(pyxel.KEY_F):
                self.startRotate()
        
            

    