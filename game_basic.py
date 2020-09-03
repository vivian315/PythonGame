import pygame
from plane_sprites import *

#游戏初始化
pygame.init()
mys = pygame.display.set_mode((480, 700), 0, 32)
pygame.display.set_caption("")
# 为什么背景图片就是不显示呢，在pycharm -> preferences -> project interpreter
# 将pygame的版本改成2.0.0.dev8，才能与mac Mojave 兼容

# 设置背景图片
bg = pygame.image.load("./images/background.png")
mys.blit(bg, (0, 0))
#pygame.display.update()

# 设置战机图片
hero = pygame.image.load("./images/hero1.png")
mys.blit(hero, (200, 500))

# 所有绘制完成后统一调用
pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(200, 500, 96, 124)

# 创建敌机精灵和精灵组
enemy = GameSprite("./images/enemy1.png")
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环
while True:
    # 游戏时钟内的刷新频率，每秒60次
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏。。。")
            pygame.quit()
            exit()  # 直接终止当前正在执行的程序
    # 移动飞机、重绘背景，重绘飞机
    hero_rect.y -= 5
    if (hero_rect.y + hero_rect.height) <= 0:
        hero_rect.y = 700
    mys.blit(bg, (0, 0))
    mys.blit(hero, hero_rect)

    # 精灵组更新所有精位置并重绘
    enemy_group.update()
    enemy_group.draw(mys)

    pygame.display.update()






