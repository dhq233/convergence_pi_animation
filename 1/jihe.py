import pygame
import math
import sys

# 初始化 Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Convergence to π using Polygons")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 动画参数
center = (WIDTH // 2, HEIGHT // 2 - 50)
radius = 200
n_sides = 4  # 初始边数
max_sides = 300  # 最大边数
FPS = 7
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    
    # 计算数学表达式的值
    if n_sides > 0:
        y1 = 2 * n_sides * math.tan(math.pi / (2 * n_sides))
        y2 = n_sides * math.sin(math.pi / n_sides)
    else:
        y1, y2 = 0, 0
    
    # 计算多边形顶点
    points = []
    for i in range(n_sides):
        angle = 2 * math.pi * i / n_sides
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    
    # 绘制多边形
    if len(points) > 2:
        pygame.draw.polygon(screen, BLUE, points, 2)
    
    # 绘制圆
    pygame.draw.circle(screen, BLACK, center, radius, 1)
    
    # 显示数学表达式的值
    screen.blit(font.render(f"2n·tan(π/2n) = {y1:.6f}", True, BLUE), (50, HEIGHT - 100))
    screen.blit(font.render(f"n·sin(π/n) = {y2:.6f}", True, GREEN), (50, HEIGHT - 70))
    screen.blit(font.render(f"n = {n_sides}", True, BLACK), (50, HEIGHT - 40))
    
    pygame.display.flip()
    clock.tick(FPS)
    
    # 增加边数，直到最大值
    if n_sides < max_sides:
        n_sides += 1
    
pygame.quit()
sys.exit()
