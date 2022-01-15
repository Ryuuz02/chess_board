chess_board = []


def add_chess_rows():
    for i in range(0, 8):
        chess_board.append([])


def fill_chess_rows():
    for i in range(0, 8):
        for j in range(0, 8):
            chess_board[i].append("_")


def print_chessboard():
    for i in range(0, 8):
        current_line = chess_board[i]
        print("|" + "|".join(current_line) + "|")


def replace_spot(new_piece, x, y):
    index_accounted_y = 8 - y
    index_accounted_x = x - 1
    chess_board[index_accounted_y][index_accounted_x] = new_piece


def build_chessboard():
    for row in range(1, 9):
        if row == 1 or row == 8:
            for col in range(1, 9):
                if col == 1 or col == 8:
                    unit = "R"
                elif col == 2 or col == 7:
                    unit = "N"
                elif col == 3 or col == 6:
                    unit = "B"
                elif row == 1:
                    if col == 4:
                        unit = "Q"
                    elif col == 5:
                        unit = "K"
                else:
                    if col == 5:
                        unit = "Q"
                    elif col == 4:
                        unit = "K"
                replace_spot(unit, col, row)
        elif row == 2 or row == 7:
            for col in range(1, 9):
                replace_spot("P", col, row)


def create_chessboard():
    add_chess_rows()
    fill_chess_rows()
    build_chessboard()


create_chessboard()
print_chessboard()
