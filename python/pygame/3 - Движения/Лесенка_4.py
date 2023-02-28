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

blocksColors = []
blocksHeights = []
blockWidth = 50

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    if countF > 60:
        blocksColors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        blocksHeights.append(random.randint(0, HEIGHT))
        countF = 0

    for i in range(len(blocksColors)):
        x = i * blockWidth

        color = blocksColors[i]
        height = blocksHeights[i]
        pygame.draw.rect(mainScreen, color, (x, 0, blockWidth, height))

    countF += 1

    pygame.display.flip()
    clock.tick(FPS)
