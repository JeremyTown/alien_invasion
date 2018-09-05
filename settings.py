# coding=utf-8
class Settings():
    """
    存储《外星人入侵》的所有设置的类
    """

    def __init__(self):
        """
        初始化游戏的设置
        """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 191, 255)

        # 飞船的速度
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 限制子弹最大数量
        self.bullets_allowed = 3
