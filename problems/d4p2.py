from itertools import chain


def mark(num, board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == num:
                # why mark spots with -100?
                # valid board numbers are 0 to 99
                # thereby picking a negative 3 digit number is least likely to result in a complete row or column sum
                # unless the entire row or column is marked with the negative 3 digit number.
                board[y][x] = -100
    return board


def remove_winner(boards):
    for board in boards:
        # check row and column sums
        row_sums = min([sum(row) for row in board])
        col_sums = min([sum(col) for col in zip(*board)])
        if row_sums == -500 or col_sums == -500:
            boards.remove(board)


def solve(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    draw = list(map(int, lines.pop(0).split(',')))
    boards = []

    # read in boards
    lpb = 5  # lines per board
    num_boards = int(len(lines)/lpb)
    for i in range(num_boards):
        board = [[int(part.strip()) for part in line.split(' ') if len(part.strip()) > 0]
                 for line in lines[lpb * i:(lpb * i) + lpb]]
        boards.append(board)

    # draw first five numbers
    for i in range(5):
        last_draw = draw.pop(0)
        boards = [mark(last_draw, b) for b in boards]
        remove_winner(boards)

    while len(boards) > 1:
        last_draw = draw.pop(0)
        boards = [mark(last_draw, b) for b in boards]
        remove_winner(boards)

    print('LAST WINNING BOARD:')
    last_draw = draw.pop(0)
    lwb = mark(last_draw, boards[0])
    for row in lwb:
        print(row)

    # sum unmarked numbers
    flat_board_sum = sum([x for x in list(chain.from_iterable(lwb)) if x != -100])
    print(flat_board_sum * last_draw)
