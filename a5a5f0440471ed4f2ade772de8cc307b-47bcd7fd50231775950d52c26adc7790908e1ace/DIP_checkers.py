import pygame
import sys

# Constants
SQUARE_SIZE = 100  # Size of each square on the checkers board
BOARD_SIZE = 8  # Number of squares on one side of the checkers board
SCREEN_SIZE = SQUARE_SIZE * BOARD_SIZE  # Total screen size

# Define colors used in the game (определяем цвета,используемые в игре)
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREY": (180, 180, 180),
    "BLUE": (0, 0, 255)
}

# Constants for Players' pieces (константы для фигур игроков)
WHITE = COLORS["WHITE"]
BLACK = COLORS["BLACK"]


class Board:
    def __init__(self):
        # Initialize an empty checkers board
        self.board = self.create_board()

    def create_board(self):
        # Create the initial board setup with pieces in their starting positions
        board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                # Populate only dark squares with pieces
                if self.is_dark_square(row, col):
                    # Top 3 rows for WHITE pieces
                    if row < 3:
                        board[row][col] = Piece(COLORS["WHITE"], row, col)
                    # Bottom 3 rows for BLACK pieces
                    elif row > 4:
                        board[row][col] = Piece(COLORS["BLACK"], row, col)
        return board

    @staticmethod
    def is_dark_square(row, col):
        # Determine if a square should be dark (i.e., a valid square for placing pieces)
        return (row + col) % 2 == 1

    def can_capture(self, piece):
        """Check if the given piece has a valid capture move."""
        # Define the possible moves (directions) based on the color
        if piece.color == WHITE:
            directions = [(-2, -2), (-2, 2)]  # Up-left, Up-right
        else:
            directions = [(2, -2), (2, 2)]  # Down-left, Down-right

        # If the piece is a king, it can move in all four directions
        if piece.is_king:
            directions += [(-2, -2), (-2, 2), (2, -2), (2, 2)]

        # Check each direction to see if a capture is possible
        for dr, dc in directions:
            new_row, new_col = piece.row + dr, piece.col + dc
            mid_row, mid_col = piece.row + dr // 2, piece.col + dc // 2
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
                middle_piece = self.board[mid_row][mid_col]
                end_square = self.board[new_row][new_col]
                if middle_piece and middle_piece.color != piece.color and not end_square:
                    return True  # A valid capture exists
        return False

    def mandatory_capture_exists(self, current_player):
        """Check if any piece of the current player has a valid capture move."""
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.board[row][col]
                if piece and piece.color == current_player and self.can_capture(piece):
                    return True
        return False

    def move_piece(self, piece, row, col):
        # Check if it's a valid diagonal move
        diff_row = abs(row - piece.row)
        diff_col = abs(col - piece.col)
        if diff_row == 1 and diff_col == 1:
            if self.board[row][col] is None:
                self.board[piece.row][piece.col], self.board[row][col] = None, piece
                piece.move(row, col)
        elif diff_row == 2 and diff_col == 2:
            middle_row = (row + piece.row) // 2
            middle_col = (col + piece.col) // 2
            if self.board[middle_row][middle_col] and self.board[middle_row][middle_col].color != piece.color:
                if self.board[row][col] is None:
                    # Capture the opponent's piece
                    self.board[middle_row][middle_col] = None
                    self.board[piece.row][piece.col], self.board[row][col] = None, piece
                    piece.move(row, col)

        # Check for making a piece a king
        if piece.color == COLORS["WHITE"] and row == 0:
            piece.make_king()
        elif piece.color == COLORS["BLACK"] and row == BOARD_SIZE - 1:
            piece.make_king()


class Piece:
    def __init__(self, color, row, col):
        # Initialize a checkers piece with given color and position
        self.color = color
        self.row = row
        self.col = col
        self.is_king = False  # Initially, the piece is not a king

    def move(self, row, col):
        self.row, self.col = row, col

    def make_king(self):
        self.is_king = True


def is_game_over(board):
    # Check if the game is over (i.e., one side has no more pieces)
    white_pieces = 0
    black_pieces = 0
    for row in board.board:
        for piece in row:
            if piece:
                if piece.color == COLORS["WHITE"]:
                    white_pieces += 1
                else:
                    black_pieces += 1

    return white_pieces == 0 or black_pieces == 0


def switch_player(current_player):
    # Toggle between WHITE and BLACK player
    return COLORS["WHITE"] if current_player == COLORS["BLACK"] else COLORS["BLACK"]


def is_valid_selection(piece, current_player):
    # Check if the selected piece belongs to the current player
    return piece and piece.color == current_player


def determine_piece_color(piece):
    # Determine the color of a piece, especially if it's a king
    return COLORS["RED"] if piece.color == COLORS["BLACK"] and piece.is_king else piece.color


def draw_board(screen, board):
    # Draw the game board and pieces on the screen
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = COLORS["GREY"] if Board.is_dark_square(row, col) else COLORS["BLACK"]
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            piece = board.board[row][col]
            if piece:
                color = determine_piece_color(piece)
                pygame.draw.circle(screen, color, (int((col + 0.5) * SQUARE_SIZE), int((row + 0.5) * SQUARE_SIZE)),
                                   SQUARE_SIZE // 2 - 5)
                if piece.is_king:
                    pygame.draw.circle(screen, COLORS["BLACK"],
                                       (int((col + 0.5) * SQUARE_SIZE), int((row + 0.5) * SQUARE_SIZE)),
                                       SQUARE_SIZE // 4)


def draw_current_player_indicator(screen, current_player):
    # Display an indicator showing which player's turn it is
    pygame.draw.circle(screen, current_player, (SCREEN_SIZE // 2, SQUARE_SIZE // 2), SQUARE_SIZE // 4)
    pygame.draw.circle(screen, COLORS["BLACK"], (SCREEN_SIZE // 2, SQUARE_SIZE // 2), SQUARE_SIZE // 4,
                       3)  # Adding a border to make it distinct


def main():
    # Main game loop
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption('Checkers')
    board = Board()
    selected_piece = None
    current_player = WHITE

    while True:
        # Update game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle Player Moves (for both BLACK and WHITE players)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
                if selected_piece:
                    # Ensure we move the piece only if it's a valid move
                    initial_pos = (selected_piece.row, selected_piece.col)
                    board.move_piece(selected_piece, row, col)
                    if (selected_piece.row, selected_piece.col) != initial_pos:
                        current_player = switch_player(current_player)
                    selected_piece = None
                else:
                    potential_selection = board.board[row][col]
                    if is_valid_selection(potential_selection, current_player):
                        selected_piece = potential_selection

        if is_game_over(board):
            print("Game Over")
            break

        # Render game state
        draw_board(screen, board)

        # Show current player's turn
        draw_current_player_indicator(screen, current_player)

        pygame.display.flip()


# Start the game
if __name__ == "__main__":
    main()
