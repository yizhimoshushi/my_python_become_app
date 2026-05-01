import pygame
# import sys # 注释掉 sys，避免在安卓上退出出错

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

    def update(self):
        # --- 键盘控制 ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

        # 注意：Pygame 的触摸在安卓上支持有限，建议先用键盘测试

# --- 敌人类 ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - ENEMY_SIZE)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(3, 8)
        self.speed_x = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(0, SCREEN_WIDTH - ENEMY_SIZE)

# --- 主程序 ---
def main():
    # 1. 初始化
    pygame.init()
    
    # 2. 创建窗口 (全屏或指定大小)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame 打包测试")
    
    # 3. 时钟
    clock = pygame.time.Clock()
    
    # 4. 精灵组
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    # 创建 10 个敌人
    for i in range(10):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # 5. 主循环
    running = True
    while running:
        # 帧率
        dt = clock.tick(FPS)

        # --- 事件 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # 不要调用 sys.exit()

        # --- 更新 ---
        all_sprites.update()

        # 碰撞检测
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            print("Game Over!")

        # --- 渲染 ---
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    # 6. 退出
    pygame.quit()
    # sys.exit() # 在安卓上，直接结束 main 函数即可，不要调用 sys.exit()

if __name__ == "__main__":
    main()
