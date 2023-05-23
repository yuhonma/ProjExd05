import random
import sys
import time

import pygame as pg


WIDTH = 500  # ゲームウィンドウの幅
HEIGHT = 600  # ゲームウィンドウの高さ


def main():
    pg.display.set_caption("縦シュー！")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
