# Игра "Шашки"

# Задаем размер игрового поля
BOARD_SIZE = 8

# Инициализируем игровое поле
board = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]


# Функция для отображения игрового поля
def display_board():
    print('   A  B  C  D  E  F  G  H')
    print('  ┌─' + '─┬─' * (BOARD_SIZE - 1) + '─┐')
    for i in range(BOARD_SIZE):
        row = str(i + 1) + ' |'
        for j in range(BOARD_SIZE):
            row += board[i][j] + ' |'
        print(row)
        if i < BOARD_SIZE - 1:
            print('  ├─' + '─┼─' * (BOARD_SIZE - 1) + '─┤')
    print('  └─' + '─┴─' * (BOARD_SIZE - 1) + '─┘')


# Функция для проверки валидности хода
def is_valid_move(player, start, end):
    print(player)
    print(start)
    print(end)
    if start == end:
        if start[0] < 0:
            if start[0] >= BOARD_SIZE:
                if start[1] < 0:
                    if start[1] >= BOARD_SIZE:
                        if end[0] < 0:
                            if end[0] >= BOARD_SIZE:
                                if end[1] < 0:
                                    if end[1] >= BOARD_SIZE:
                                        return False

        # # Проверка в зависимости от игрока (для короля и обычных шашек)
        elif player == 'X':
            tmp = board[start[0]][start[1]]
            print(tmp)
            if board[start[0]][start[1]] != 'X':
                return False
            if abs(start[0] - end[0]) != 1 or abs(start[1] - end[1]) != 1:
                return False
        elif player == 'O':
            if board[start[0]][start[1]] != 'O':
                return False
            if abs(start[0] - end[0]) != 1 or abs(start[1] - end[1]) != 1:
                return False

    # Проверка на свободную клетку
    elif board[end[0]][end[1]] != ' ':
        return False
    else:
        return True


# Функция для выполнения хода
def make_move(player, start, end):
    board[start[0]][start[1]] = ' '
    board[end[0]][end[1]] = player

    # Проверка, становится ли шашка королем
    if player == 'X' and end[0] == BOARD_SIZE - 1:
        board[end[0]][end[0]] = 'K'

    elif player == 'O' and end[0] == 0:
        board[end[0]][end[0]] = 'K'


# Главная функция игры
def play_game():
    current_player = 'X'
    Flag = True
    while Flag:
        display_board()
        print(f"Ходит игрок {current_player}")
        Flag = True
        while Flag:
            start = input("Введите начальную позицию (строка столбец, например 3A): ")
            end = input("Введите конечную позицию (строка столбец, например 4B): ")

            # Преобразуем введенные значения в координаты на игровом поле
            start_row = int(start[0]) - 1
            start_col = ord(start[1]) - ord('A')
            end_row = int(end[0]) - 1
            end_col = ord(end[1]) - ord('A')

            if is_valid_move(current_player, (start_row, start_col), (end_row, end_col)):
                print('Перед')
                make_move(current_player, (start_row, start_col), (end_row, end_col))
                print('После')
                break
            else:
                print("Неверный ход, попробуйте снова!")

            # Проверка на победу
            # if 'X' not in sum(board, []) or 'O' not in sum(board, []):
            #     winner = 'X' if 'O' not in sum(board, []) else '0'
            def remove_opponent_piece(player, position):
                row, col = position
                player = 'O' if player == 'X' else 'X'  # Определение фигуры противника

                # Удаляем фигуру противника из игрового поля
                board[row][col] = ' '

                # Дополнительные действия, если была удалена королевская фигура противника
                if player == 'X' and board[row][col] == 'K':
                    for i in range(BOARD_SIZE):
                        for j in range(BOARD_SIZE):
                            if board[i][j] == 'O':
                                board[i][j] = ' '  # Удаляем обычные шашки противника
                elif player == 'O' and board[row][col] == 'K':
                    for i in range(BOARD_SIZE):
                        for j in range(BOARD_SIZE):
                            if board[i][j] == 'X':
                                board[i][j] = ' '  # Удаляем обычные шашки противника

                remove_opponent_piece()

            display_board()
            print(f"Игра окончена! Победил игрок {winner}!")
            break

        # Смена хода
        current_player = 'X' if current_player == 'O' else 'O'


# Запуск игры
play_game()
