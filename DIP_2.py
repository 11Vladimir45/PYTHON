import pygame
#import pygame as pg
#pg.init()


# Определяем константы для размеров доски и фишек
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Определяем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

class Board:
    def __init__(self):
        self.board = [[0 for j in range(COLS)] for i in range(ROWS)]
        self.selected_piece = None

    def draw_squares(self, screen):
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(screen, GRAY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(screen, WHITE, (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2), SQUARE_SIZE//2-10)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(screen, BLACK, (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2), SQUARE_SIZE//2-10)

    def draw_selected_piece(self, screen):
        if self.selected_piece is not None:
            row, col = self.selected_piece
            pygame.draw.circle(screen, RED, (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2), SQUARE_SIZE//2-10, 5)

    def update(self):
        pass

    def draw(self, screen):
        self.draw_squares(screen)
        self.draw_pieces(screen)
        self.draw_selected_piece(screen)
        pygame.display.update()


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False

    def move(self, row, col):
        self.row = row
        self.col = col

    def make_king(self):
        self.is_king = True


class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player(WHITE)
        self.player2 = Player(BLACK)
        self.current_player = self.player1
        self.selected_piece = None

    def update(self):
        pass

    def draw(self, screen):
        self.board.draw(screen)
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Шашки")

    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.draw(screen)

    pygame.quit()
    #pygame.init()

