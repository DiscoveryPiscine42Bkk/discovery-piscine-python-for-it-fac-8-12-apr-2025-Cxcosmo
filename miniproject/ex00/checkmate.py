class Chess :
    def __init__(self, board) :
        self.board = board
        self.list_board = board.split()
        self.position_K = []

    def Pawns(self, row, col) :
        if [row - 1, col - 1] == self.position_K or [row - 1, col + 1] == self.position_K :
            print("Success")
            return True
        return False

    def move_Bishops_Rooks(self, row, col, move) :
        for i in move :
            check_position = [row, col]
            while len(self.list_board) >= check_position[0] >= 0 and len(self.list_board) >= check_position[1] >= 0 :
                check_position[0] += i[0]
                check_position[1] += i[1]
                if check_position == self.position_K :
                    print("Success")
                    return True
        return False

    def Bishops(self, row, col) :
        move = [[-1,-1], [-1,1], [1, -1], [1, 1]]
        return self.move_Bishops_Rooks(row, col, move)

    def Rooks(self, row, col) :
        move = [[-1,0], [1,0], [0, -1], [0, 1]]
        return self.move_Bishops_Rooks(row, col, move)

    def Queens(self, row, col) :
        if self.Bishops(row, col) :
            return True
        elif self.Rooks(row, col) :
            return True
        return False

    def King(self) :
        line = (self.board.find("K") - 1) // len(self.list_board)
        position_K = (self.board.find("K") - line) - (line * len(self.list_board))
        self.position_K.append(line)
        self.position_K.append(position_K)

    def check(self) :
        self.King()
        for i in range(len(self.list_board)) :
            for j in range(len(self.list_board[i])) :
                if self.list_board[i][j] == "P" :
                    if self.Pawns(i, j) :
                        return
                if self.list_board[i][j] == "B" :
                    if self.Bishops(i, j) :
                        return
                if self.list_board[i][j] == "R" :
                    if self.Rooks(i, j) :
                        return
                if self.list_board[i][j] == "Q" :
                    if self.Queens(i, j) :
                        return
        print("Fail")

def checkmate(board) :
    if board.count("K") != 1 :
        return print("Need one King .")
    list_board = board.split()
    for i in list_board :
        if len(i) != len(list_board) :
            return print("This board is not square .")
    check_chess = Chess(board)
    check_chess.check()
