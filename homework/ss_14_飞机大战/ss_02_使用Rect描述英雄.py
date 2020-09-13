import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 {0} {1}".format(hero_rect.x, hero_rect.y))
print("英雄的尺寸 {0} {1}".format(hero_rect.width, hero_rect.height))
print("英雄大小 {0}" .format(hero_rect.size))
