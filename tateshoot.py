import random
import sys
import time

import pygame as pg


WIDTH = 500  # ゲームウィンドウの幅
HEIGHT = 600  # ゲームウィンドウの高さ

class Player:
    _delta = {  # 押下キーと移動量の辞書
        pg.K_UP: (0, -0.5),
        pg.K_DOWN: (0, +0.5),
        pg.K_LEFT: (-1.0, 0),
        pg.K_RIGHT: (+1.0, 0),
    }

    def __init__(self, xy: tuple[int, int]):
        self.img = pg.transform.rotozoom(pg.image.load(f"ex05-2/fig/boy.png"), 0, 0.4)
        self.rect = self.img.get_rect()
        self.rect.center = xy

    def update(self,key_lst: list[bool],screen: pg.Surface):
        for k, mv in __class__._delta.items():
            if key_lst[k]:
                self.rect.move_ip(mv)
        screen.blit(self.img, self.rect)

def main():
    pg.display.set_caption("縦シュー！")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    player = Player((WIDTH//2,HEIGHT-100))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        
        key_lst = pg.key.get_pressed()
        player.update(key_lst,screen)
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
