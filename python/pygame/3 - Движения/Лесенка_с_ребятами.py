import pygame, sys
import random
pygame.init()

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# настройки главного экрана
WIDTH = 1000
HEIGHT = 800
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

colors = []
blocks = []
blockWidth = 50
count = 0

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # высота столбика
    height = 0
    # вниз/вверх
    heightDir = 1

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    if count > 60:
        numberBlock = len(blocks)
        blocks.append(numberBlock * blockWidth)
        colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        count = 0

    # for i in blocks:
    for i in range(len(blocks)):
        height += 50 * heightDir
        pygame.draw.rect(mainScreen, colors[i], (blocks[i], 0, 50, height))

        if i % 2 == 0 and i != 0:
            heightDir = -heightDir

    count += 1
    pygame.display.flip()
    clock.tick(FPS)
