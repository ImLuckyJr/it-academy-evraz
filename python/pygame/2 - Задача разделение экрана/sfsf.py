import pygame, sys
pygame.init()
3
# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1000
HEIGHT = 800
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

isWhite = True
countFrame = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mainScreen.fill(mainScreenColor)

    if isWhite == True:
        pygame.draw.rect(mainScreen, WHITE, (0, 0, WIDTH, HEIGHT))

        if countFrame > 60:
            isWhite = False
            countFrame = 0
    else:
        pygame.draw.rect(mainScreen, BLACK, (0, 0, WIDTH, HEIGHT))

        if countFrame > 60:
            isWhite = True
            countFrame = 0

    countFrame += 1

    pygame.display.flip()
    clock.tick(FPS)
