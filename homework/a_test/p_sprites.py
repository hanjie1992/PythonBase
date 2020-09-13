import pygame
import random
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1. 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2. 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1. 调用父类方法，创建敌机精灵，并且指定敌机的图像
        super().__init__("./images/enemy1.png")

        # 2. 设置敌机的随机初始速度
        self.speed = random.randint(1, 3)
        # 3. 设置敌机的随机初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1. 调用父类方法，让敌机在垂直方向运动
        super().update()

        # 2. 判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
            print("敌机飞出屏幕...")

class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        super().__init__("./images/me1.png", 0)

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 飞机水平移动
        self.rect.x += self.speed

        # 判断屏幕边界
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (1, 2, 3):
            # 1. 创建子弹精灵
            bullet = Bullet()

            # 2. 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)
        print("发射子弹...")

class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()

        # 判断是否超出屏幕，如果是，从精灵组删除
        if self.rect.bottom < 0:
            self.kill()