import pygame, sys
pygame.init()

# цвета
BLACK = (0, 0, 0)

SPEED = 10
changeX = 0
changeY = 0

# настройки главного экрана
WIDTH = 1000
HEIGHT = 800
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

block1 = pygame.image.load('27640596.png')
block1rect = block1.get_rect(center = (WIDTH//2 - 100, HEIGHT//2))
block2 = pygame.image.load('27640596.png')
block2rect = block1.get_rect(center = (WIDTH//2 + 100, HEIGHT//2))

activeBlock = 1

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                activeBlock = 1
            elif event.key == pygame.K_2:
                activeBlock = 2

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        changeX = -1 * SPEED

    if keys[pygame.K_RIGHT]:
        changeX = SPEED

    if keys[pygame.K_UP]:
        changeY = -1 * SPEED

    if keys[pygame.K_DOWN]:
        changeY = SPEED

    if not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        changeY = 0

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        changeX = 0

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    if activeBlock == 1:
        block1.set_alpha(255)
        block2.set_alpha(150)

        block1rect.x += changeX
        block1rect.y += changeY
    else:
        block1.set_alpha(150)
        block2.set_alpha(255)

        block2rect.x += changeX
        block2rect.y += changeY

    mainScreen.blit(block1, block1rect)
    mainScreen.blit(block2, block2rect)

    pygame.display.flip()
    clock.tick(FPS)
