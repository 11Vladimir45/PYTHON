import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 10
Window_SIZE = (800, 800)
BACKGROUND = (150, 90, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
YELLOW = (255, 255, 0)
CELL_QTY = 8
CELL_SIZE = 80
COLORS = [BLACK, GREY]

screen = pg.display.set_mode(Window_SIZE)
screen.fill(BACKGROUND)
is_even_gty = (CELL_QTY % 2 == 0)
cell_color_index = 1 if (is_even_gty) else 0

for y in range(CELL_QTY):
    for x in range(CELL_QTY):
        pg.draw.rect(screen, COLORS[cell_color_index], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        cell_color_index ^= True  # бинарное XOR
    cell_color_index = cell_color_index ^ True if (is_even_gty) else cell_color_index
# r1 = pg.draw.rect(screen, BLACK, (10, 10, 60, 40))
# r2 = pg.draw.rect(screen, GREY, (60, 60, 60, 40), 5)
# r3 = pg.draw.rect(screen, WHITE, (110, 110, 60, 40))
# print(r1)
#
# c1 = pg.draw.circle(screen, GREY, (200, 200,), 40, 5)
# print(c1)
# r4 = pg.draw.rect(screen, YELLOW, (160, 160, 80, 80), 4)
# print(r4)
# s1 = pg.draw.ellipse(screen, BLACK, (160, 160, 80, 80), 5)
# print(s1)

pg.display.update()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    clock.tick(FPS)
