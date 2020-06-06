import pygame

# 按钮类
class Button():
    # 初始化基本参数
    def __init__(self, image_path, choose_image_path, position):
        self.image = pygame.image.load(image_path)
        self.choose_image = pygame.image.load(choose_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = position

    # 绘制按钮
    def draw(self, screen, position):
        if self.rect.collidepoint(position):
            screen.blit(self.choose_image, self.rect)
            return True
        else:
            screen.blit(self.image, self.rect)
            return False
