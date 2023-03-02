import pygame, sys
pygame.init()

# цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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

block1 = pygame.Surface((100, 100))
block1rect = block1.get_rect(center = (WIDTH//2 - 100, HEIGHT//2))

# block2 = pygame.Surface((100, 100))
block2d = pygame.image.load('snake.png')
block2u = block2d.copy()
block2u = pygame.transform.flip(block2u, False, True)
block2l = block2d.copy()
block2l = pygame.transform.rotate(block2l, -90)
block2r = block2d.copy()
block2r = pygame.transform.rotate(block2r, 90)

block2 = block2u
block2rect = block2.get_rect(center = (WIDTH//2 + 100, HEIGHT//2))

block1.fill(RED)
# block2.fill(GREEN)

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

    block1rect_old = block1rect.copy()
    block2rect_old = block2rect.copy()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        changeX = -1 * SPEED
        block2 = block2l

    if keys[pygame.K_RIGHT]:
        changeX = SPEED
        block2 = block2r

    if keys[pygame.K_UP]:
        changeY = -1 * SPEED
        block2 = block2u

    if keys[pygame.K_DOWN]:
        changeY = SPEED
        block2 = block2d

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

    print(block1rect.x, block1rect_old.x)

    if block1rect.colliderect(block2rect) == True:
        block1rect = block1rect_old
        block2rect = block2rect_old

    mainScreen.blit(block1, block1rect)
    mainScreen.blit(block2, block2rect)


    pygame.display.flip()
    clock.tick(FPS)
