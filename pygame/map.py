import pygame

class Map():
    # 初始化基本参数
    def __init__(self, filepath, position):
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.center = position

    # 控制地图相对运动
    def move(self, direction, speed):
        # 你需要在这里编写 [地图相对运动] 的代码
        #pass
        if direction == 'left':
            self.rect.centerx += speed
        elif direction == 'right':
            self.rect.centerx -= speed
        elif direction == 'up':
            self.rect.centery += speed
        elif direction == 'down':
            self.rect.centery -= speed
    # 判断是否走出陆地
    def is_border(self):
        touch_border = False
        if -400 <= self.rect.centerx <= 1200 and -250 <= self.rect.centery <= 900: # -400<= ...
            touch_border = True
        return touch_border

    # 防止走出陆地
    def touch_border(self):
        if self.rect.centerx > 1200:
            self.rect.centerx = 1200
        if self.rect.centerx < -400:
            self.rect.centerx = -400
        if self.rect.centery > 900:
            self.rect.centery = 900
        if self.rect.centery < -250:
            self.rect.centery = -250

    # 绘制地图
    def draw(self, screen):
        screen.blit(self.image, self.rect)
