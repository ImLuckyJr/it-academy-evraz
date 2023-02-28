import pygame, sys
pygame.init()

# цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (136, 0, 255)

# настройки главного экрана
WIDTH = 1000
HEIGHT = 800
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

blockW = 100
blockH = 100
speed = 10

block1 = pygame.Surface((blockW, blockH))
block2 = pygame.Surface((blockW, blockH))

block1.fill(GREEN)
block2.fill(PURPLE)

blockrect1 = block1.get_rect()
blockrect1.x = WIDTH//2 - 150
blockrect1.y = HEIGHT//2 - 50
blockrect2 = block2.get_rect()
blockrect2.x = WIDTH//2
blockrect2.y = HEIGHT//2 - 50

activeBlock = 1
block1.set_alpha(255)
block2.set_alpha(150)

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                activeBlock = 1
                block1.set_alpha(255)
                block2.set_alpha(150)
            elif event.key == pygame.K_2:
                activeBlock = 2
                block1.set_alpha(150)
                block2.set_alpha(255)

    keys = pygame.key.get_pressed()

    if activeBlock == 1:
        if keys[pygame.K_LEFT]:
            blockrect1.x -= speed
        elif keys[pygame.K_RIGHT]:
            blockrect1.x += speed

        if keys[pygame.K_UP]:
            blockrect1.y -= speed
        elif keys[pygame.K_DOWN]:
            blockrect1.y += speed

        if blockrect1.x < 0:
            blockrect1.x = 0

        if blockrect1.x + blockW > WIDTH:
            blockrect1.x = WIDTH - blockW

        if blockrect1.y < 0:
            blockrect1.y = 0

        if blockrect1.y + blockH > HEIGHT:
            blockrect1.y = HEIGHT - blockH
    elif activeBlock == 2:
        if keys[pygame.K_LEFT]:
            blockrect2.x -= speed
        elif keys[pygame.K_RIGHT]:
            blockrect2.x += speed

        if keys[pygame.K_UP]:
            blockrect2.y -= speed
        elif keys[pygame.K_DOWN]:
            blockrect2.y += speed

        if blockrect2.x < 0:
            blockrect2.x = 0

        if blockrect2.x + blockW > WIDTH:
            blockrect2.x = WIDTH - blockW

        if blockrect2.y < 0:
            blockrect2.y = 0

        if blockrect2.y + blockH > HEIGHT:
            blockrect2.y = HEIGHT - blockH

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    # pygame.draw.rect(mainScreen, GREEN, (blockX, blockY, blockW, blockH))
    mainScreen.blit(block1, blockrect1)
    mainScreen.blit(block2, blockrect2)

    pygame.display.flip()
    clock.tick(FPS)
