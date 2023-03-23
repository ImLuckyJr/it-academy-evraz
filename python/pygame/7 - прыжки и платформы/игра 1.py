import pygame, sys
import random
pygame.init()

# цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

SPEED = 10
changeX = 0

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1200
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
mainScreenColor = WHITE
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

vel = 5
jump = False
jumpCount = 0
jumpMax = 25
onGround = True
onPlatform = False

# block2 = pygame.Surface((100, 100))
manjump = pygame.image.load('man_jump.png')
manstand = pygame.image.load('man_stand.png')
manr = pygame.image.load('man_walk.png')
manl = manr.copy()
manl = pygame.transform.flip(manl, True, False)

man = manstand
manrect = manr.get_rect()
manrect.bottom = HEIGHT//2
manrect.left = WIDTH//2

platform = pygame.image.load('кирпич шоколадка small.png')

# platform = pygame.Surface((250, 100))

# массив rect'ов для еды
platforms = [
    # platform.get_rect(left = 0, bottom = HEIGHT - 200)
]

map =  [
    '******************************',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*            **              *',
    '*                            *',
    '*                            *',
    '*                            *',
    '*          ******        *****',
    '*****                        *',
    '*                            *',
    '******************************'
]

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax
                onGround = False
                onPlatform = False

    platforms = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '*':
                platformrect = platform.get_rect()
                platformrect.x = 50 * j
                platformrect.y = 50 * i
                platforms.append(platformrect)
                mainScreen.blit(platform, platformrect)

    manrect_old = manrect.copy()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        changeX = -1 * SPEED
        man = manl

    if keys[pygame.K_RIGHT]:
        changeX = SPEED
        man = manr

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        changeX = 0
        man = manstand

    if jump:
        manrect.y -= jumpCount
        man = manjump

    if jumpCount > -jumpMax or (manrect.bottom < HEIGHT and onGround == False):
        jumpCount -= 1
        man = manjump
    else:
        jump = False
        onGround = True

    if manrect.bottom > HEIGHT:
        manrect.bottom = HEIGHT
        onGround = True
        jump = False

    manrect.x += changeX

    # проверка столкновения блока еды и змеи
    for platformrect in platforms:
        if manrect.colliderect(platformrect) == True:
            # движемся налево
            if manrect.left < manrect_old.left:
                manrect.x -= changeX
                # manrect.left = platformrect.right

            # движемся направо
            if manrect.right > manrect_old.right:
                manrect.x -= changeX
                # manrect.left = platformrect.right

        if manrect.colliderect(platformrect) == True:
            # движемся вниз
            if manrect.bottom > manrect_old.bottom:
                jump = False
                onGround = True
                onPlatform = True
                manrect.bottom = platformrect.top

    # Проверка падаем с платформы, потому что вышли с неё
    if onPlatform == True:
        manrect_next = manrect.copy()
        manrect_next.y += 1

        if manrect_next.collidelist(platforms) == -1:
            jump = True
            jumpCount = -1
            onGround = False
            onPlatform = False

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    # рисуем блок еды
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)

    # рисуем змею
    mainScreen.blit(man, manrect)

    pygame.display.flip()
    clock.tick(FPS)


# 1. Сделать подсчет съеденных блоков (пишем в консоли) (если очень сильно присильно хотите, сделайте счет на экране, но самостоятельно).
# 2. Подумать и реализовать выход за рамки
# 3. Сделать так, чтобы появлялось сразу 2 блока. Их съедали. И как всё съели, появляются новые 2 блока.
# 4. Тоже самое, что и 3, но 10 блоков.
