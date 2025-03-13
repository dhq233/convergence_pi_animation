# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:07:12 2025

@author: DuOH
"""
import pygame
import math
import sys

# 初始化 Pygame
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Convergence to π")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 图表参数
margin = 60
graph_width = WIDTH - 2 * margin
graph_height = HEIGHT - 2 * margin

# 生成数据
x_values = list(range(90, 10000))
y1_values = [2*i * math.tan(math.pi/(2*i)) for i in x_values]
y2_values = [i * math.sin(math.pi/i) for i in x_values]

# 自动计算坐标范围
all_y = y1_values + y2_values
y_min = min(all_y) * 0.9999  # 留出边距
y_max = max(all_y) * 1.0001

# 坐标转换函数
def to_screen_coords(i, y_val):
    x = margin + (i - 90) * graph_width / (999 - 90)
    y = margin + graph_height - (y_val - y_min) * graph_height / (y_max - y_min)
    return (x, y)

# 预计算所有点
points = [
    (to_screen_coords(i, y1), to_screen_coords(i, y2))
    for i, (y1, y2) in zip(x_values, zip(y1_values, y2_values))
]

# 动画参数
current_frame = 0
FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    
    # 绘制坐标轴
    pygame.draw.line(screen, BLACK, (margin, HEIGHT-margin), (WIDTH-margin, HEIGHT-margin), 2)  # X轴
    pygame.draw.line(screen, BLACK, (margin, margin), (margin, HEIGHT-margin), 2)  # Y轴

    # 绘制π参考线
    pi_y = to_screen_coords(90, math.pi)[1]
    pygame.draw.line(screen, RED, (margin, pi_y), (WIDTH-margin, pi_y), 1)

    # 绘制文本
    font = pygame.font.SysFont('Arial', 24)
    screen.blit(font.render('i →', True, BLACK), (WIDTH-margin-30, HEIGHT-margin+10))
    screen.blit(font.render('π', True, RED), (margin-40, pi_y-15))
    
    # 动态绘制曲线
    if current_frame < len(points):
        current_frame += 1

    # 绘制曲线
    visible_points = points[:current_frame]
    if len(visible_points) > 1:
        # 绘制 2i·tan(π/(2i)) 曲线
        pygame.draw.lines(screen, BLUE, False, [p[0] for p in visible_points], 2)
        # 绘制 i·sin(π/i) 曲线
        pygame.draw.lines(screen, GREEN, False, [p[1] for p in visible_points], 2)

    # 绘制图例
    legend_rect = pygame.Rect(WIDTH-200, margin, 180, 80)
    pygame.draw.rect(screen, WHITE, legend_rect)
    pygame.draw.rect(screen, BLACK, legend_rect, 1)
    screen.blit(font.render('2i·tan(π/2i)', True, BLUE), (WIDTH-180, margin+10))
    screen.blit(font.render('i·sin(π/i)', True, GREEN), (WIDTH-180, margin+40))
    screen.blit(font.render(f"Current i: {x_values[current_frame-1] if current_frame>0 else ''}", 
                           True, BLACK), (margin+10, margin//2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()