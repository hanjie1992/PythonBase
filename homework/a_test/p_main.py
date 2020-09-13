import pygame

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from homework.a_test.p_sprites import  *

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 每隔 0.5 秒发射一次子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        """ 创建精灵组 """

        # 背景组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 敌机组
        self.enemy_group = pygame.sprite.Group()

        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        pass


    def start_game(self):
        print("开始游戏...")
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(60)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新精灵组
            self.__update_sprites()
            # 5. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                self.enemy_group.add(Enemy())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()


            # 获取用户按键
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0
        pass

    def __check_collide(self):
        """碰撞检测"""

        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表时候有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()
        pass

    def __update_sprites(self):
        """更新精灵组"""
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        pass

    @staticmethod
    def __game_over():
        """游戏结束"""
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()