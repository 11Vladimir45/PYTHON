import pygame

# Инициализация Pygame
pygame.init()

# Определение размера экрана
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра в шашки")

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Размеры доски
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Функция отрисовки доски
def draw_board():
    screen.fill(GRAY)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Основной игровой цикл
def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board()
        pygame.display.update()

    pygame.quit()
