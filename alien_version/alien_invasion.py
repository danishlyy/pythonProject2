import sys
import pygame
from alien_version.settings import Settings
from alien_version.ship import Ship
import alien_version.game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # 设置背景色
    # bg_color = (230,230,230)
    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # bullets.update(bullets)
        # 删除已消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     # 每次循环时都重绘屏幕
        #     screen.fill(ai_settings.bg_color)
        #     ship.blitme()
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     # 让最近绘制的屏幕可见
        #     pygame.display.flip()


run_game()
