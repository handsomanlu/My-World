import pygame

class Player():
    # 初始化基本参数
    def __init__(self):
        self.left_list = [pygame.image.load('pygame/image/主角/向左1.png'),
                          pygame.image.load('pygame/image/主角/向左2.png'),
                          pygame.image.load('pygame/image/主角/向左3.png'),
                          pygame.image.load('pygame/image/主角/向左4.png'),
                          pygame.image.load('pygame/image/主角/向左5.png'),
                          pygame.image.load('pygame/image/主角/向左6.png'),
                          pygame.image.load('pygame/image/主角/向左7.png'),
                          pygame.image.load('pygame/image/主角/向左8.png')]
        self.right_list = [pygame.image.load('pygame/image/主角/向右1.png'),
                           pygame.image.load('pygame/image/主角/向右2.png'),
                           pygame.image.load('pygame/image/主角/向右3.png'),
                           pygame.image.load('pygame/image/主角/向右4.png'),
                           pygame.image.load('pygame/image/主角/向右5.png'),
                           pygame.image.load('pygame/image/主角/向右6.png'),
                           pygame.image.load('pygame/image/主角/向右7.png'),
                           pygame.image.load('pygame/image/主角/向右8.png')]
        self.up_list = [pygame.image.load('pygame/image/主角/向上1.png'),
                        pygame.image.load('pygame/image/主角/向上2.png'),
                        pygame.image.load('pygame/image/主角/向上3.png'),
                        pygame.image.load('pygame/image/主角/向上4.png'),
                        pygame.image.load('pygame/image/主角/向上5.png'),
                        pygame.image.load('pygame/image/主角/向上6.png'),
                        pygame.image.load('pygame/image/主角/向上7.png'),
                        pygame.image.load('pygame/image/主角/向上8.png')]
        self.down_list = [pygame.image.load('pygame/image/主角/向下1.png'),
                          pygame.image.load('pygame/image/主角/向下2.png'),
                          pygame.image.load('pygame/image/主角/向下3.png'),
                          pygame.image.load('pygame/image/主角/向下4.png'),
                          pygame.image.load('pygame/image/主角/向下5.png'),
                          pygame.image.load('pygame/image/主角/向下6.png'),
                          pygame.image.load('pygame/image/主角/向下7.png'),
                          pygame.image.load('pygame/image/主角/向下8.png')]

        self.image = pygame.image.load('pygame/image/主角/向左1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        # 你需要在这里编写 [初始化 count] 的代码
        self.count =0


    # 绘制主角
    def draw(self, screen, direction):
        # 你需要在这里编写 [主角方向选择与帧动画切换] 的代码
        self.count += 1
        if direction == 'left':
            self.image = self.left_list[self.count % 8]
            #screen.blit(self.image, self.rect)
        elif direction == 'right':
            self.image = self.right_list[self.count % 8]
            #screen.blit(self.image, self.rect)
        elif direction == 'up':
            self.image = self.up_list[self.count % 8]
            #screen.blit(self.image, self.rect)
        elif direction == 'down':
            self.image = self.down_list[self.count % 8]
            #screen.blit(self.image, self.rect)
        elif direction == 'space':
            self.image = pygame.image.load('pygame/image/npc/商人/商人1.png')
            #screen.blit(self.image, self.rect)

        screen.blit(self.image, self.rect)
