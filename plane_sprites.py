# 官方模块导入
import random

# 第三方模块导入
import pygame

# 导入自己的模块

# 常量定义
# 主屏幕尺寸常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PRE_SEC = 60
# 背景、英雄、敌机、子弹图像
BACK_IMAGE = "./images/background.png"
HERO_IMAGE = "./images/hero1.png"
ENEMY_IMAGE = "./images/enemy1.png"
BULLET_IMAGE = "./images/bullet1.png"

# 创建敌机的定时器常量
ENEMY_PLANE_TRIGE = pygame.USEREVENT
BULLET_TRIGE = pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1、调用父类实现初始化
        super().__init__(BACK_IMAGE)

        # 2、 判断是否是替换图片
        if not is_alt:
            self.rect.y = - self.rect.height

    def update(self):
        # 1、移动，调用父类实现
        super().update()

        # 2、判断背景是否移出屏幕，如果是，背景图片移动到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        super().__init__(ENEMY_IMAGE)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.speed = random.randint(1, 5)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法可以将敌机精灵从精灵组移出并销毁
            self.kill()

class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__(BULLET_IMAGE, -2)

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()



class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__(HERO_IMAGE, 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def shoot(self):
        i = 0
        while i < 3:
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - (bullet.rect.height + 10)*i
            bullet.rect.x = self.rect.centerx
            self.bullets.add(bullet)
            i += 1