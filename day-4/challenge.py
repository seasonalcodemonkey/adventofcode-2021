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

    def unmark(self):
        self.marked = False

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

    def unmark(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                self.board[row][col].unmark()

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

    def print_marked(self):
        marked = []

        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.board[row][col].marked:
                    marked.append(self.board[row][col].value)

        print(marked, len(marked))

        

def bingo(number, board, last_win = False):
    win = None

    for num in number:
        for i in range(0, len(board)):
            board[i].mark(num)

            if not board[i].bingo and board[i].check():
                if last_win:
                    win = (board[i].sum_unmarked(), num)
                else:
                    return (board[i].sum_unmarked(),  num)
    
    return win


if __name__ == "__main__":
    filename = "input"
    input = load_input(filename)
    
    if isinstance(input, Exception):
        print("Could not load from %s: %s" % (filename, input)) 
    else:
        number, board = parse_input(input)
        
        for i in range(0, len(board)):
            board[i] = Board(board[i])

        sum, num = bingo(number, board)
        print("First to win: %i x %i %i" % (sum, num, sum * num))
        
        for i in range(0, len(board)):
            board[i].unmark()

        sum, num = bingo(number, board, True)
        print("Last to win: %i x %i %i" % (sum, num, sum * num))