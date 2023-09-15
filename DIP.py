'''
TODO:
* Реализовать проверку "Игрок обязан съесть фигуру противника, если есть такая возможность"
    Как воспроизвести:
    * запустить программу
    * ход игрока X: 6A -> 5B
    * ход игрока O: 3D -> 4C
    * ход игрока X: 6G -> 5H - ! место ошибки 
    
    Игра позволяет сделать последний ход игроку X без съедения фигуры противника. 
    Ожидаемое поведение - проинформировать, что ход неверен из-за необходимости съесть фигуру противника, предложить повторить ход.
* ...
'''
# В блоке главной функции нужно создать условие ,при
# котором при съедании всех шашек противника игра будет заканчиваться, т.е.
# программа выйдет из цикла while с командой break. Также дамка не ест на дальнии
# дистанции и за раз несколько шашек.В этом и есть пока моя трудность.

# Игра "Шашки"

# Задаем размер игрового поля
BOARD_SIZE = 8

# Инициализируем игровое поле
board = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]


# Функция для начальной расстановки шашек
def initialize_board():
    for i in range(3):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 == 1:
                board[i][j] = 'O'

    for i in range(5, BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 == 1:
                board[i][j] = 'X'


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

         # Проверка в зависимости от игрока (для короля и обычных шашек)
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
        print('занято')
        return False
    else:
        return True


# Функция для выполнения хода
def make_move(player, start, end):
    board[start[0]][start[1]] = ' '
    board[end[0]][end[1]] = player

    # Проверка, становится ли шашка королем
    if player == 'X' and end[0] == 0:
        board[end[0]][end[1]] = 'KX'
    elif player == 'O' and end[0] == BOARD_SIZE - 1:
        board[end[0]][end[1]] = 'KO'

    # Проверка на съедание фигур противника
    if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 2:
        mid_row = (start[0] + end[0]) // 2
        mid_col = (start[1] + end[1]) // 2
        if board[mid_row][mid_col] == 'O' or board[mid_row][mid_col] == 'X':
            remove_opponent_piece(player, (mid_row, mid_col))


# Функция для удаления фигур противника
def remove_opponent_piece(player, position):
    row, col = position
    opponent = 'O' if player == 'X' else 'X'  # Определение фигуры противника

    # Удаляем фигуру противника из игрового поля
    board[row][col] = ' '

    # Дополнительные действия, если была удалена королевская фигура противника
    # if opponent == 'X' and 'KX' in board[i][j]:
    #     for i in range(BOARD_SIZE):
    #         for j in range(BOARD_SIZE):
    #             if board[i][j] == 'O':
    #                 board[i][j] = ' '  # Удаляем обычные шашки противника
    # elif opponent == 'O' and 'KO' in board[i][j]:
    #     for i in range(BOARD_SIZE):
    #         for j in range(BOARD_SIZE):
    #             if board[i][j] == 'X':
    #                 board[i][j] = ' '  # Удаляем обычные шашки противника

    # winner_player()


def winner_player():
    counter_X = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 == 1 and board[i][j] == 'X':
                counter_X += 1
    if counter_X == 0:
        print(f"Игра окончена!Победил игрок: 'O'!")
    print(f'checkers X = {counter_X}')

    counter_O = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 == 1 and board[i][j] == 'O':
                counter_O += 1
    if counter_O == 0:
        print(f"Игра окончена!Победил игрок: 'X'!")
    print(f'checkers O = {counter_O}')
    return counter_O, counter_X


# Главная функция игры
def play_game(counter_X, counter_O):
    initialize_board()  # Инициализируем начальное состояние игрового поля
    current_player = 'X'
    Flag = True
    while Flag:
        display_board()
        if counter_O == 0 or counter_X == 0:
            print(f"Игра окончена!")
            # print(f"Ходит игрок {current_player}")
            break
        else:
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
                winner_player()
                break
            else:
                print("Неверный ход, попробуйте снова!")

            # # Добавляем логику для съедания фигур противника
            # if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 2:
            #     mid_row = (start_row + end_row) // 2
            #     mid_col = (start_col + end_col) // 2
            #     if board[mid_row][mid_col] == 'O' or board[mid_row][mid_col] == 'X':
            #         remove_opponent_piece(current_player, (mid_row, mid_col))

            # Проверка на победу

            # if 'X' not in sum(board, []) or 'O' not in sum(board, []):
            # winner = 'X' if 'O' not in sum(board, []) else '0'

            # def remove_opponent_piece(player, position):
            #     row, col = position
            #     player = 'O' if player == 'X' else 'X'  # Определение фигуры противника
            #
            #     # Удаляем фигуру противника из игрового поля
            #     board[row][col] = ' '
            #
            #     # Дополнительные действия, если была удалена королевская фигура противника
            #     if player == 'X' and board[row][col] == 'KX':
            #         for i in range(BOARD_SIZE):
            #             for j in range(BOARD_SIZE):
            #                 if board[i][j] == 'O':
            #                     board[i][j] = ' '  # Удаляем обычные шашки противника
            #     elif player == 'O' and board[row][col] == 'KO':
            #         for i in range(BOARD_SIZE):
            #             for j in range(BOARD_SIZE):
            #                 if board[i][j] == 'X':
            #                     board[i][j] = ' '  # Удаляем обычные шашки противника

            # remove_opponent_piece()

            # display_board()

            # if counter_O == 0 or counter_X == 0:
            # print(f"Игра окончена!")  # Победил игрок {winner}
            # break

        # Смена хода
        current_player = 'X' if current_player == 'O' else 'O'


# Запуск игры
play_game(12, 12)
