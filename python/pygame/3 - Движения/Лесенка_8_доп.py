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

countF = 0

blocks = []
blockWidth = 50
blockChangeHeight = 50

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    if countF > 60:
        blocks.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        countF = 0

    for i in range(len(blocks)):
        x = WIDTH - blockWidth - i * blockWidth
        numberBlock = i + 1
        height = (numberBlock % 4) * blockChangeHeight

        if height == 0:
            height = ((numberBlock - 2) % 4) * blockChangeHeight

        y = HEIGHT - height

        color = blocks[i]
        pygame.draw.rect(mainScreen, color, (x, y, blockWidth, height))

    countF += 1

    pygame.display.flip()
    clock.tick(FPS)
