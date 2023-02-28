import pygame, sys
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
higher = True
higherFrom = 0

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    if countF > 60:
        blocks.append(True)
        countF = 0

    for i in range(len(blocks)):
        x = i * blockWidth
        height = (i + 1) * blockChangeHeight

        pygame.draw.rect(mainScreen, WHITE, (x, 0, blockWidth, height))

    countF += 1

    pygame.display.flip()
    clock.tick(FPS)
