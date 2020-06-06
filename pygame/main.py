from map import *
from object import *
from player import *
from button import *
import random

# 初始化基本参数
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
direction = ''
story_type = 'start'
mouse_postion = (0, 0)
button_down = False

# 创建对象
start_bg = Map('pygame/image/开场背景.jpg', (400, 300))
start_button = Button('pygame/image/按钮/开始按钮.png', 'pygame/image/按钮/开始按钮_点击.png', (550, 400))
end_button = Button('pygame/image/按钮/结束按钮.png', 'pygame/image/按钮/结束按钮_点击.png', (550, 480))
map = Map('pygame/image/地图.png', (400, 300))
player = Player()
group = pygame.sprite.Group()
group.add(Object('pygame/image/npc/树木1.png', (-250, 300), '', 'Tree'))
group.add(Object('pygame/image/npc/枯木.png', (0, 700), '', 'Tree'))
group.add(Object('pygame/image/npc/椰树3.png', (1150, -300), '', 'Tree'))
group.add(Object('pygame/image/npc/椰树2.png', (1150, 200), '', 'Tree'))
group.add(Object('pygame/image/npc/椰树1.png', (600, 820), '', 'Tree'))
group.add(Object('pygame/image/npc/帐篷1.png', (1100, 550), '', 'Room'))
group.add(Object('pygame/image/npc/帐篷2.png', (1000, -100), '', 'Room'))
group.add(Object('pygame/image/npc/帐篷3.png', (1100, -200), '', 'Room'))
group.add(Object('pygame/image/npc/羊/羊%d.png', (-100, -100), '咩～咩～'))
group.add(Object('pygame/image/npc/狗/狗%d.png', (900, -50), '汪汪～汪汪～'))
group.add(Object('pygame/image/npc/海豚/海豚%d.png', (0, 1000), '哗啦啦～哗啦啦～'))
group.add(Object('pygame/image/npc/商人/商人%d.png', (900, 200), '听说国王遇到麻烦了，帮助他可有一大笔奖励哟~'))
group.add(Object('pygame/image/npc/诗人/诗人%d.png', (300, 800), 'To be or not be, that is a question.'))
group.add(Object('pygame/image/npc/美人鱼/美人鱼%d.png', (1300, 400), '在那蓝色的海洋上～有座美丽的城堡～'))
group.add(Object('pygame/image/npc/猫/猫咪%d.png', (950, 600), '喵～喵～'))
group.add(Object('pygame/image/路牌.png', (200, 300), ['欢迎来到', '克罗斯的冒险世界'], 'Board'))

# 加载音乐文件
pygame.mixer.init()
pygame.mixer.music.load('pygame/media/背景音乐.wav')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# 主循环
while True:
    # 事件检测
    for event in pygame.event.get():
        # 退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()

        # 键盘事件检测
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
            elif event.key == pygame.K_SPACE:
                direction = 'space'
                print(direction)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE:
                direction = ""

        # 鼠标事件检测
        if event.type == pygame.MOUSEMOTION:
            mouse_postion = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_down = True
            mouse_postion = pygame.mouse.get_pos()

    # 启动页面
    if story_type == 'start':
        # 绘制启动页面背景
        start_bg.draw(screen)

        # 判断是否点击开始游戏按钮
        if start_button.draw(screen, mouse_postion):
            if button_down:
                story_type = 'field'

        # 判断是否点击结束游戏按钮
        if end_button.draw(screen, mouse_postion):
            if button_down:
                pygame.quit()

        button_down = False

    # 游戏页面
    else:
        # 控制地图与角色的移动
        map.move(direction, 10)
        #group.update(direction, 10)  #add
        if map.is_border():
            group.update(direction, 10)
            if pygame.sprite.spritecollide(player, group, False):
                group.update(direction, -10)
                map.move(direction, -10)
        else:
            map.touch_border()

        # 绘制地图与角色
        map.draw(screen)
        for object in group:
            object.draw(screen)
            if object.status == 'NPC':
                object.say(screen)
            elif object.status == 'Board':
                object.draw_board_text(screen)

        # 绘制主角
        player.draw(screen, direction)

    # 更新屏幕
    pygame.display.update()

    # 设置游戏速度
    clock.tick(12)
