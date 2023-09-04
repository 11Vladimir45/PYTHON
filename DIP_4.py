import pygame

pygame.init()
# Создание доски

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw_board(win):
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkers")
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board(win)
        pygame.display.update()

    pygame.quit()


main()
# Создание фигур


class Piece:
    PADDING = 15
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

    def draw(self, win):
        pygame.draw.circle(win, self.color,
                           (self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2),
                           SQUARE_SIZE // 2 - self.PADDING + self.BORDER)
        pygame.draw.circle(win, WHITE,
                           (self.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.col * SQUARE_SIZE + SQUARE_SIZE // 2),
                           SQUARE_SIZE // 2 - self.PADDING)

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col


# Обновление функции отрисовки доски


def draw_board(win, board):
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != None:
                piece.draw(win)


# Создание класса доски и инициализация фигур


class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.create_pieces()

    def create_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                if row % 2 == col % 2:
                    if row < 3:
                        self.board[row][col] = Piece(row, col, RED)
                    elif row > 4:
                        self.board[row][col] = Piece(row, col, BLUE)

    def draw(self, win):
        draw_board(win, self.board)




# Обновление основной функции
def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkers")
    clock = pygame.time.Clock()
    run = True
    board = Board()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.draw(win)
        pygame.display.update()

    pygame.quit()


main()