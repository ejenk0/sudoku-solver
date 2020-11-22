debug = False

#Puzzle 1(0.87):[[0,7,8,0,0,4,0,5,0],[0,0,0,0,0,0 0,0,7],[0,5,0,1,8,0,0,9,0],[0,8,9,0,0,0,5,7,0],[3,0,2,0,0,0,9,0,1],[0,1,7,0,0,0,2,4,0],[0,9,0,0,5,2,0,3,0],[8,0,0,0,0,0,0,0,0],[0,6,0,3,0,0,7,1,0]]
#Puzzle 2(0.80):[[8,1,2,0,9,0,0,0,0],[0,0,9,6,0,0,0,5,0],[6,0,0,0,3,0,0,0,0],[7,0,0,0,0,3,1,9,0],[9,0,3,0,0,0,6,0,5],[0,6,1,8,0,0,0,0,3],[0,0,0,0,5,0,0,0,4],[0,9,0,0,0,6,7,0,0],[0,0,0,0,7,0,5,2,9]]

class Board():
    def __init__(self, puzzle=[[8,1,2,0,9,0,0,0,0],[0,0,9,6,0,0,0,5,0],[6,0,0,0,3,0,0,0,0],[7,0,0,0,0,3,1,9,0],[9,0,3,0,0,0,6,0,5],[0,6,1,8,0,0,0,0,3],[0,0,0,0,5,0,0,0,4],[0,9,0,0,0,6,7,0,0],[0,0,0,0,7,0,5,2,9]]):
        self.puzzle, self.data = puzzle, puzzle

class Cell():
    def __init__(self, board, row, column):
        if row < 3:
            self.bigcellrow = 0
        elif row < 6:
            self.bigcellrow = 1
        else:
            self.bigcellrow = 2
        if column < 3:
            self.bigcellcolumn = 0
        elif column < 6:
            self.bigcellcolumn = 1
        else:
            self.bigcellcolumn = 2
        self.board = board
        self.row = row
        self.column = column
        self.value = 0
        self.known_failures = []
        if debug:
            print(f"New cell at {row}, {column}")
    def find_lowest(self):
        candidate = 0
        searching = True
        samerow = self.board.data[self.row]
        samecolumn = [self.board.data[0][self.column],self.board.data[1][self.column],self.board.data[2][self.column],self.board.data[3][self.column],self.board.data[4][self.column],self.board.data[5][self.column],self.board.data[6][self.column],self.board.data[7][self.column],self.board.data[8][self.column]]
        rowoffset = self.bigcellrow * 3
        columnoffset = self.bigcellcolumn * 3
        samebigcell = [self.board.data[rowoffset + 0][columnoffset + 0], self.board.data[rowoffset + 0][columnoffset + 1], self.board.data[rowoffset + 0][columnoffset + 2],
                        self.board.data[rowoffset + 1][columnoffset + 0], self.board.data[rowoffset + 1][columnoffset + 1], self.board.data[rowoffset + 1][columnoffset + 2],
                        self.board.data[rowoffset + 2][columnoffset + 0], self.board.data[rowoffset + 2][columnoffset + 1], self.board.data[rowoffset + 2][columnoffset + 2]]
        if debug:
            print(f"Cell at row:{self.row}, column:{self.column} found {samerow} in it's row, {samecolumn} in it's column and {samebigcell} in it's bigcell.")

        while searching:
            candidate += 1
            if candidate not in samerow + samecolumn + samebigcell + self.known_failures:
                searching = False

        if debug:
            print(f"Cell at row:{self.row}, column:{self.column} found {candidate} as it's lowest possible value, given {self.known_failures} had already been tried.")
        return candidate

#A new comment

def display(data):
    x = 0
    for row in data:
        y = 0
        for cell in row:
            y += 1
            if y == 3 or y == 6:
                space = "|"
            else:
                space = " "
            print(str(cell) + space, end="")
        x += 1
        if x == 3 or x == 6:
            print("\n-----+-----+-----")
        else:
            print()




def create_cells(board):
    cells = []
    row_num = 0
    for row in board.data:
        column_num = 0
        for cell in row:
            if cell == 0:
                cells.append(Cell(board, row_num, column_num))
            column_num += 1
        row_num += 1
    return cells



if __name__ == "__main__":
    gameBoard = Board()
    print("\nUnsolved state:")
    display(gameBoard.puzzle)
    cells = create_cells(gameBoard)


    solved = False
    current_cell = 0
    while not solved:
        x = cells[current_cell].find_lowest()
        if not cells[current_cell].value == 0:
            cells[current_cell].known_failures.append(cells[current_cell].value)
            cells[current_cell].value = 0
            gameBoard.data[cells[current_cell].row][cells[current_cell].column] = 0
        if not x > 9:
            cells[current_cell].value = x
            gameBoard.data[cells[current_cell].row][cells[current_cell].column] = x
            current_cell += 1
        else:
            cells[current_cell].value = 0
            gameBoard.data[cells[current_cell].row][cells[current_cell].column] = 0
            cells[current_cell].known_failures = []
            current_cell -= 1
        if debug:
            input()

        if current_cell >= len(cells):
            solved = True
            print(f"\nSolved state:")
            display(gameBoard.data)
