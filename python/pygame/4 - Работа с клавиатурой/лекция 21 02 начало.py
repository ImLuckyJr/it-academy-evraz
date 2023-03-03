import pygame, sys
pygame.init()

# цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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
blockH = blockW

block = pygame.Surface((blockW, blockH))
blockrect = block.get_rect()
blockrect.centerx = WIDTH // 2
blockrect.centery = HEIGHT // 2

block.fill(RED)

speed = 10

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         blockX -= speed
        #     elif event.key == pygame.K_RIGHT:
        #         blockX += speed
        #     elif event.key == pygame.K_UP:
        #         blockY -= speed
        #     elif event.key == pygame.K_DOWN:
        #         blockY += speed

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] == True:
        blockrect.x -= speed
    elif keys[pygame.K_RIGHT] == True:
        blockrect.x += speed

    if keys[pygame.K_UP] == True:
        blockrect.y -= speed
    elif keys[pygame.K_DOWN] == True:
        blockrect.y += speed

    if blockrect.x < 0:
        blockrect.x = 0

    if blockrect.x + blockW > WIDTH:
        blockrect.x = WIDTH - blockW

    if blockrect.y < 0:
        blockrect.y = 0

    if blockrect.y + blockH > HEIGHT:
        blockrect.y = HEIGHT - blockH

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    # pygame.draw.rect(mainScreen, RED, (blockX, blockY, blockW, blockH))
    mainScreen.blit(block, blockrect)

    pygame.display.flip()
    clock.tick(FPS)
