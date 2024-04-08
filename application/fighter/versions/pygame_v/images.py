import os
import skimage as ski
# from pprint import pprint
import pygame

MARIO = "C:/Users/Tobiathan/Desktop/mariotest.png"
BLOCK_SIZE = 10
screen = None

def mario(a, c, m, block=BLOCK_SIZE,img=ski.io.imread(os.path.normpath(MARIO))):
    """makes mario pixel art in pygame"""
    w, h, _ = img.shape
    if abs(m) == w-5:
        a *= -1
    for x in range(w):
        img_arr = img[x]
        for y in range(h):
            b = x
            d = y
            if y == abs(m):
                b += a
            if x == abs(m):
                d += a
            color = list(img_arr[y])
            if color[3] != 0:
                pygame.draw.rect(
                    screen,
                    pygame.Color(color[0], color[1], color[2], a=color[3]),
                    pygame.Rect((d*block), (b*block+10), block, block),
                )
    print(m, c)
    if c == 2:
        m+=a
        c = -1
    c += 1
    return a, c, m
_a, _c, _m = 1, 0, 1 # For Mario Function  put ->  a, c, m = mario(a, c, m) | in Running Loop
