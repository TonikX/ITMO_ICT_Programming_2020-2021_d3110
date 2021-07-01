import pygame
from random import randint
from copy import deepcopy


Res = WIDTH, HEIGHT = 1600,900
#设置窗口长和宽
TILE = 20 #数值
W, H = WIDTH // TILE, HEIGHT // TILE #设置一个小格子长和宽
fps = 10 #刷新频率

pygame. init()#初始化游戏
surface = pygame.display.set_mode(Res)#设置一个启动窗口res
CLOCK = pygame.time.Clock()

next_field = [[0 for i in range(W)]for j in range(H)]
current_field = [[randint(0, 1)for i in range(W)]for j in range(H)]#初始领域
#current_field = [[1 if not i % 33 else 0 for i in range(W)]for j in range(H)]


def check_cell(current_field, x, y,):#设置算法
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:#如果count等于2或者3则异常返回
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0
while True:

    surface.fill(pygame.Color('black'))#设置游戏退出
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            exit()
     #绘画格子
    [pygame.draw.line(surface, pygame.Color('dimgray'),(x, 0), (x, HEIGHT))for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('dimgray'),(0, y), (WIDTH, y))for y in range(0,HEIGHT,TILE)]
    #绘画人生
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'),(x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)


    pygame.display.flip()
    CLOCK.tick(fps)
