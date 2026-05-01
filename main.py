import pygame
import random
import sys

# --- 常量定义 ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
ENEMY_SIZE = 30
FPS = 60

# 颜色定义 (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
RED = (255, 50, 50)
BLACK = (20, 20, 20)

# --- 玩家类 ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 7
        
        # 增加一个变量记录触摸位置
        self.touch_pos = None 

    def update(self):
        # --- 1. 键盘控制 (电脑测试用) ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

        # --- 2. 触摸控制 (安卓手机用) ---
        # 获取所有触摸点
        touches = pygame.mouse.get_pressed() # 简单的鼠标模拟
        # 在安卓上，通常用 finger 事件，但在 pgs4a 简易模式下，
        # 我们可以简单地让方块跟随鼠标/手指位置
        
        # 获取鼠标/手指位置
        mx, my = pygame.mouse.get_pos()
        
        # 如果鼠标按下了（或者手指按在屏幕上），让方块跟着走
        # 这里做一个简单的逻辑：手指按在哪，方块就往哪移动（平滑跟随）
        if touches[0]: # 左键/手指按下
             # 简单的跟随算法
             if self.rect.centerx < mx: self.rect.x += self.speed
             if self.rect.centerx > mx: self.rect.x -= self.speed
             if self.rect.centery < my: self.rect.y += self.speed
             if self.rect.centery > my: self.rect.y -= self.speed

# --- 敌人类 ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 创建一个红色的圆球作为敌人
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # 随机生成位置
        self.rect.x = random.randrange(0, SCREEN_WIDTH - ENEMY_SIZE)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(3, 8)
        self.speed_x = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        
        # 如果敌人跑出屏幕下方，重置到上方
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(0, SCREEN_WIDTH - ENEMY_SIZE)

# --- 主程序 ---
def main():
    # 1. 初始化 Pygame
    pygame.init()
    
    # 2. 创建窗口
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame 打包测试 - 躲避红球")
    
    # 3. 设置时钟 (控制帧率)
    clock = pygame.time.Clock()
    
    # 4. 创建精灵组
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    
    # 创建玩家
    player = Player()
    all_sprites.add(player)
    
    # 创建 10 个敌人
    for i in range(10):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    
    # 5. 游戏主循环
    running = True
    while running:
        # --- 事件处理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # --- 更新逻辑 ---
        all_sprites.update()
        
        # 简单的碰撞检测 (如果玩家碰到敌人，游戏重置或打印信息)
        # 这里演示：如果碰到，打印 "Game Over" 到控制台
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            print("哎呀！撞到了！(碰撞检测正常)")

        # --- 画面渲染 ---
        screen.fill(BLACK)  # 填充背景色
        all_sprites.draw(screen)  # 绘制所有精灵
        
        # 翻转显示
        pygame.display.flip()
        
        # 限制帧率为 60 FPS
        clock.tick(FPS)
    
    # 6. 退出
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
