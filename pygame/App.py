import Player
import Coin
import Baloon
import Bird
import pyxel

#画面遷移用の定数
SCENE_TITLE = 0	#タイトル画面
SCENE_PLAY = 1	#ゲーム画面
SCENE_GAME_OVER = 2 #ゲームオーバー画面

TITLE_BGM = 2
GAME_BGM = 1
END_BGM = 0


class App:
    def __init__(self):
        # 画面サイズの設定　captionはwindow枠にtext出せる
        pyxel.init(160, 128, title="Hello Pysel")
        # editorデータ読み込み(コードと同じフォルダにある)
        pyxel.load("sky.pyxres")
        #画面遷移の初期化
        self.scene = SCENE_TITLE
        #得点初期化
        self.score = 0
        # player初期配置
        self.player = Player.Player(80,60)
        # coin,baloon,bird初期配置 
        self.coins = []
        self.baloons = []
        self.birds = []
        self.rup = False
        self.rup_x = 0
        self.rup_y = 0
        for i in range(5):
            bird = Bird.Bird()
            self.birds.append(bird)
        for i in range(4):
            coin = Coin.Coin()
            baloon = Baloon.Baloon(coin)
            self.coins.append(coin)
            self.baloons.append(baloon)

        # 実行開始 更新関数 描画関数
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #処理の画面分岐
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_GAME_OVER:
            self.update_game_over_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()


    #タイトル画面処理用update
    def update_title_scene(self):
        #ENTERでゲーム画面に遷移
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.scene = SCENE_PLAY
            #BGMをloop再生
            pyxel.playm(GAME_BGM, loop = True)            

    #ゲームオーバー画面処理用update
    def update_game_over_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = SCENE_PLAY
            #BGMをloop再生
            pyxel.playm(GAME_BGM, loop = True) 
            #得点初期化
            self.score = 0
            # 初期配置
            self.player.position_x = 80
            self.player.position_y = 60
            self.coins = []
            self.baloons = []
            self.birds = []
            self.rup = False
            self.rup_x = 0
            self.rup_y = 0
            for i in range(5):
                bird = Bird.Bird()
                self.birds.append(bird)
            for i in range(4):
                coin = Coin.Coin()
                baloon = Baloon.Baloon(coin)
                self.coins.append(coin)
                self.baloons.append(baloon)
            

    #ゲーム画面処理用update
    def update_play_scene(self):
        self.rup = False
        self.update_player()
        self.update_coin()
        self.update_baloon()
        self.update_bird()

    def update_player(self):   
        self.player.move()

    def update_coin(self):
        for i in range(len(self.coins)):
            coin = self.coins[i]

            #プレイヤーに当たったら
            if coin.hit_player(self.player) and coin.active:
                coin.active=False
                self.score += 10    #scoe加算

            #移動
            #落下状態
            if coin.falling == True:
                coin.fall()
            #通常状態
            else:
                coin.move()
            # 画面外に出たら
            if coin.overScreen():
                self.coins[i] = Coin.Coin()
                self.baloons[i] = Baloon.Baloon(self.coins[i])
                

    def update_baloon(self):
        for i in range(len(self.baloons)):
            baloon = self.baloons[i]

            #プレイヤーに当たったら
            if (baloon.hit_player(self.player)):
                self.rup = True
                self.rup_x = baloon.position_x
                self.rup_y = baloon.position_y
                #下の方に隠す
                baloon.position_y = -10
                
                self.coins[i].falling = True
                
            #移動
            baloon.move()
            # 画面外に出たら
            if self.coins[i].overScreen():
                self.baloons[i] = Baloon.Baloon(self.coins[i])
    
    def update_bird(self):
        for i in range(len(self.birds)):
            bird = self.birds[i]
            bird.move()
            if bird.hit_player(self.player):
                self.scene = SCENE_GAME_OVER
                #タイトル音楽再生(MUSIC 0番をloop再生)
                pyxel.playm(END_BGM, loop = True)
            # 画面外に出たら
            if bird.overScreen():
                self.birds[i] = Bird.Bird()

         
    def draw(self):
        # 画面クリア 0は黒
        # 12は空の色
        pyxel.cls(12)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 256)

        #描画の画面分岐
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_GAME_OVER:
            self.draw_game_over()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()

        #score表示用に整形(format関数の文字列操作を利用)
        s = "Score:{:>4}".format(self.score)
        #text表示(x座標、y座標、文字列、color)
        pyxel.text(5, 4, s, 7)

    #タイトル画面描画用update
    def draw_title_scene(self):
        pyxel.text(70, 40, "GAME", 7)
        pyxel.text(50, 80, "- PRESS ENTER -", 7)

    #ゲーム画面描画用update
    def draw_play_scene(self):
        # editorデータ描画
        '''コピー先x, コピー先y, イメージバンク番号, イメージバンクx, 
         イメージバンクy, イメージバンク領域x, イメージバンク領域y, 透過する色コード,回転'''   
        #draw player     
        pyxel.blt(self.player.position_x, self.player.position_y, 0, 32, 0, 16, 16, 12, self.player.rotateCount)

        # draw coins
        for coin in self.coins:
            if coin.active == True:
                pyxel.blt(coin.position_x, coin.position_y, 0, 0, 0, 16, 16, 12)
        #draw baloons
        for baloon in self.baloons:
            pyxel.blt(baloon.position_x,baloon.position_y,0,16,32,16,16,12)
        #draw birds
        for bird in self.birds:
            pyxel.blt(bird.position_x,bird.position_y,0,16,16,16,16,12)
        
        if self.rup:
            pyxel.blt(self.rup_x,self.rup_y,0,0,48,16,16,12)

    #ゲームオーバー画面描画用update
    def draw_game_over(self):
        pyxel.cls(12)
        pyxel.bltm(0, 0, 2, 0, 0, 256, 256)      

App()

