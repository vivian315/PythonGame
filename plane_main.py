from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        """ 游戏初始化 """

        # 1、创建游戏主窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2、创建游戏时钟
        self.clock = pygame.time.Clock()

        # 3、调用私有方法，精灵和精灵组创建
        self.__create_sprites()

        # 4、创建事件定时器
        pygame.time.set_timer(ENEMY_PLANE_TRIGE, 1000)
        pygame.time.set_timer(BULLET_TRIGE, 500)


    def __create_sprites(self):
        """创建精灵和精灵组"""
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        enemy = Enemy()
        self.enemy_group = pygame.sprite.Group(enemy)

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        """ 游戏开始 """
        while True:
            # 1、 设置刷新帧率
            self.clock.tick(FRAME_PRE_SEC)

            # 2、 事件监听
            self.__event_handle()

            # 3、 碰撞检测
            self.__check_collide()

            # 4、 更新/绘制精灵组
            self.__update_sprites()

            # 5、 更新显示
            pygame.display.update()


    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == ENEMY_PLANE_TRIGE:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == BULLET_TRIGE:
                self.hero.shoot()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #    # 键盘方法捕获方法一
            #     self.hero.update(-10)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     self.hero.update(10)

        # 键盘捕获方法二，使用键盘提供的方法捕获键盘按键
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, True, True)
        #敌机摧毁英雄
        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemys) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束。。。")
        pygame.quit()
        exit()

# 确保主模块可以执行也可以被别的模块导入
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()


