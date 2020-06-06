import pygame

# 物体类
class Object(pygame.sprite.Sprite):
    # 初始化基本参数
    def __init__(self, filepath, position, string = '', status = 'NPC'):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = []
        self.image = 0
        self.string = ''
        self.string_list = []
        if status == 'NPC':
            for i in range(1, 9):
                self.image_list.append(pygame.image.load(filepath % i))

            self.image = self.image_list[0]
            self.string = string
        elif status == 'Board':
            self.image = pygame.image.load(filepath)
            self.string_list = string
        else:
            self.image = pygame.image.load(filepath)
            self.string = string

        self.rect = self.image.get_rect()
        self.rect.center = position
        self.font = pygame.font.Font('pygame/font/方正.TTF', 30)
        self.font_board = pygame.font.Font('pygame/font/方正.TTF', 14)
        self.dialogue = pygame.image.load('pygame/image/对话框.png')
        self.dialogue_rect = self.dialogue.get_rect()
        self.dialogue_rect.center = (400, 400)
        self.status = status
        self.count = 0
        self.current_time = pygame.time.get_ticks()
        self.last_time = self.current_time

    # 控制角色移动
    def update(self, direction, speed):
            if direction == 'left':
                self.rect.centerx += speed
            elif direction == 'right':
                self.rect.centerx -= speed
            elif direction == 'up':
                self.rect.centery += speed
            elif direction == 'down':
                self.rect.centery -= speed

    # 绘制角色
    def draw(self, screen):
        if self.status == 'NPC':
            self.current_time = pygame.time.get_ticks()
            rate = 100
            if self.current_time >= self.last_time + rate:
                self.count += 1
                self.last_time = self.current_time

            screen.blit(self.image_list[self.count % 8], self.rect)
        else:
            screen.blit(self.image, self.rect)

    # 绘制角色对话
    def say(self, screen):
        if self.string != '':
            if abs(400 - self.rect.centerx) < 110 and abs(300 - self.rect.centery) < 110:
                score_text = self.font.render(self.string, 1, (0, 0, 0))
                screen.blit(self.dialogue, (0, 0))
                screen.blit(score_text, (20, 10))

    # 绘制路牌文字
    def draw_board_text(self, screen):
        if self.string_list != []:
            score_text = self.font_board.render(self.string_list[0], 1, (0, 0, 0))
            screen.blit(score_text, (self.rect.centerx - 90, self.rect.centery - 37))
            if len(self.string_list) > 1:
                score_text = self.font_board.render(self.string_list[1], 1, (0, 0, 0))
                screen.blit(score_text, (self.rect.centerx - 60, self.rect.centery - 17))
