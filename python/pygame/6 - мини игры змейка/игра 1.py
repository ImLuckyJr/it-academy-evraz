import pygame, sys
import random
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

foodblock = pygame.Surface((20, 20))
foodblock.fill(RED)

# массив rect'ов для еды
foods = []

count = 0

f = pygame.font.Font(None, 60)

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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

    block2rect.x += changeX
    block2rect.y += changeY

    # создание ректа блока еды
    if len(foods) == 0:
        foodrect = foodblock.get_rect()
        foodrect.centerx = random.randint(0, WIDTH)
        foodrect.centery = random.randint(0, HEIGHT)
        foods.append(foodrect)

    # проверка столкновения блока еды и змеи
    if len(foods) > 0:
        if block2rect.colliderect(foods[0]) == True:
            # foods = []
            foods.pop(0)
            count += 1

    # рисуем блок еды
    if len(foods) > 0:
        mainScreen.blit(foodblock, foods[0])

    # рисуем змею
    mainScreen.blit(block2, block2rect)

    sc_text = f.render('Съедено блоков: ' + str(count), 1, RED)
    mainScreen.blit(sc_text, (0, 0))

    print('Съедено блоков: ' + str(count))

    pygame.display.flip()
    clock.tick(FPS)


# 1. Сделать подсчет съеденных блоков (пишем в консоли) (если очень сильно присильно хотите, сделайте счет на экране, но самостоятельно).
# 2. Подумать и реализовать выход за рамки
## 3. Сделать так, чтобы появлялось сразу 2 блока. Их съедали. И как всё съели, появляются новые 2 блока.
# 4. Тоже самое, что и 3, но 10 блоков.
