from colorama import Fore


class ChessBoard:
    def __init__(self, rows=8, cols=8):
        self.board = []
        self.rows = rows
        self.cols = cols
        for row in range(0, rows):
            self.board.append([])
        for col in range(0, cols):
            for row in range(0, rows):
                self.board[col].append("_")
        for row in range(1, rows + 1):
            if row == 1 or row == 8:
                unit = ""
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
                    if row == 1:
                        self.replace_spot(unit, col, row)
                    elif row == 8:
                        self.replace_spot(unit, col, row)
            elif row == 2:
                for col in range(1, 9):
                    self.replace_spot("P", col, row)
            elif row == 7:
                for col in range(1, 9):
                    self.replace_spot("P", col, row)

    def print_board(self):
        for row in range(0, self.rows):
            current_line = self.board[row]
            print("|" + "|".join(current_line) + "|")

    def replace_spot(self, new_piece, x, y):
        index_accounted_y = y - self.cols
        index_accounted_x = x - self.rows
        self.board[-index_accounted_y][index_accounted_x] = new_piece


class ChessPiece:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name


class Pawn(ChessPiece):
    def __init__(self, name):
        super().__init__("P", name)


class Rook(ChessPiece):
    def __init__(self):
        pass


class Knight(ChessPiece):
    def __init__(self):
        pass


class Queen(ChessPiece):
    def __init__(self):
        pass


class Bishop(ChessPiece):
    def __init__(self):
        pass


class King(ChessPiece):
    def __init__(self):
        pass


def move_piece(piece_symbol):
    pass


chess_board = ChessBoard()
chess_board.print_board()
