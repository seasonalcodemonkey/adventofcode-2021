def load_input(filename):
    try:
        file = open(filename, "r")
    except Exception as exc:
        return exc
    
    lines = []

    for line in file:
        lines.append(line.strip())

    file.close()    

    return lines

def parse_input(input):
    number, board = [], []
    board_i = -1
    num_found = False

    for line in input:
        if not num_found and line.find(",") != -1:
            number = [int(i) for i in line.split(",")]
            num_found = True

        elif len(line) == 0:
            board_i = board_i + 1
            board.append([])

        elif line.split()[0].isnumeric():
            board[board_i].append([int(i) for i in line.split()])

    return (number, board)

class BoardNum:
    def __init__(self, value):
        self.value = value
        self.marked = False

    def mark(self):
        self.marked = True

class Board:
    def __init__(self, board):
        self.num = {}
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = [[None for i in range(0, self.cols)] for i in range(0, self.rows)]
        self.bingo = False

        for row in range(0, self.rows):
            for col in range(0, self.cols):
                value = board[row][col]
                self.board[row][col] = BoardNum(value)
            
                if value not in self.num:
                    self.num[value] = []
                
                self.num[value].append([row, col])

    def mark(self, number):
        if number in self.num:
            for row, col in self.num[number]:
                self.board[row][col].mark()

    def check(self):
        for row in range(0, self.rows):
            mark = [num.marked for num in self.board[row]]

            if False not in mark:
                self.bingo = True
                return self.bingo

        for col in range(0, self.cols):
            mark = [self.board[r][col].marked for r in range(0, self.rows)]

            if False not in mark:
                self.bingo = True
                return self.bingo
            

        return self.bingo

    def sum_unmarked(self):
        sum = 0

        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if not self.board[row][col].marked:
                    sum += self.board[row][col].value

        return sum

        

def bingo(number, board):
    for i in range(0, len(board)):
        board[i] = Board(board[i])

    for num in number:
        for i in range(0, len(board)):
            board[i].mark(num)

            if board[i].check():
                return (board[i].sum_unmarked(),  num)


if __name__ == "__main__":
    filename = "input"
    input = load_input(filename)
    
    if isinstance(input, Exception):
        print("Could not load from %s: %s" % (filename, input)) 
    else:
        number, board = parse_input(input)
        sum, number = bingo(number, board)
        print("%i x %i %i" % (sum, number, sum * number))

        