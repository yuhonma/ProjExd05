import sys
import time

import pygame as pg


WIDTH = 500  # ゲームウィンドウの幅
HEIGHT = 600  # ゲームウィンドウの高さ


class Player:
    """
    主人公に関するクラス
    """
    _delta = {  # 押下キーと移動量の辞書
        pg.K_LEFT: (-1.0, 0),
        pg.K_RIGHT: (+1.0, 0),
    }

    def __init__(self, xy: tuple[int, int]):
        """
        主人公の画像Surfaceを生成する
        引数xy：画像を表示する座標タプル
        """
        self.img = pg.transform.rotozoom(pg.image.load("ex05-2/fig/boy.png"), 0, 0.4) # ロードした画像を0.4倍に
        self.rect = self.img.get_rect()
        self.rect.center = xy

    def update(self,key_lst: list[bool],screen: pg.Surface):
        """
        押されたキーに応じて左右に移動する
        引数key_list：押されたキーのリスト
        """
        for k, mv in __class__._delta.items():
            if key_lst[k]:
                self.rect.move_ip(mv)
        screen.blit(self.img, self.rect)


class Enemy:
    """
    敵に関する仮クラス
    """
    def __init__(self, xy: tuple[int, int]):
        """
        敵(赤い四角形)のSurface生成と座標設定
        引数xy：敵を表示させる座標タプル
        """
        self.img = pg.Surface((20,20))
        pg.draw.rect(self.img, (255, 0, 0), pg.Rect(0, 0, 20, 20)) # 赤い四角形に設定
        self.rect = self.img.get_rect()
        self.rect.center = xy

    def update(self,screen: pg.Surface):
        """
        画面に敵を表示させる
        引数 screen：画面Surface
        """
        screen.blit(self.img,self.rect)


class Explosion:
    """
    爆発エフェクトに関するクラス
    """

    def __init__(self,enemy:Enemy):
        """
        爆弾が爆発するエフェクトを生成する
        引数 enemy：爆発する敵インスタンス
        """
        img = pg.image.load("ex05-2/fig/explosion.gif")
        self.imgs = [img, pg.transform.flip(img, 1, 1)] # 通常の画像と、左右上下を反転させた画像
        self.image = self.imgs[0]
        self.rect = self.image.get_rect(center=enemy.rect.center)
        self.life = 200 # 表示時間を200に設定
    
    def update(self,screen:pg.Surface):
        """
        爆発時間を1減算した爆発経過時間_lifeに応じて爆発画像を切り替えることで
        爆発エフェクトを表現する
        引数 screen：画像Surface
        """
        self.life -= 1
        self.image = self.imgs[self.life//10%2] # 時間が経過するごとに交互に画像を変更させる
        screen.blit(self.image,self.rect)


def main():
    pg.display.set_caption("縦シュー！")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    bg_img = pg.transform.rotozoom(pg.image.load("ex05-2/fig/pg_bg.jpg"), 0, 2)
    
    exps = None
    player = Player((WIDTH//2,HEIGHT-100))
    enemy = Enemy((200,100)) # 200,100の位置に敵を配置

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                exps = Explosion(enemy) # Spaceが押された場合、敵が爆発し消される
                enemy = None

        key_lst = pg.key.get_pressed() # 押されたキーの取得
            
        screen.blit(bg_img, [0, 0])
        
        if exps is not None: 
            exps.update(screen)
            if exps.life < 0: # 表示時間が終了したら爆発エフェクトを消す
                exps = None

        if enemy is not None:
            enemy.update(screen)
        
        player.update(key_lst,screen)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()