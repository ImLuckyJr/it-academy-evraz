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

isWhite = True
colorCount = 0

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    if isWhite == True:
        pygame.draw.rect(mainScreen, WHITE, (0, 0, WIDTH, HEIGHT))

        if colorCount >= 60:
            isWhite = False
            colorCount = 0
    else:
        pygame.draw.rect(mainScreen, BLACK, (0, 0, WIDTH, HEIGHT))

        if colorCount >= 60:
            isWhite = True
            colorCount = 0

    colorCount += 1

    pygame.display.flip()
    clock.tick(FPS)
