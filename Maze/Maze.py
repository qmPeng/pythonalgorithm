import turtle

class Maze:
    def __init__(self,mazeFileName):
        rows = 0
        columns = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rows
                    self.startCol = col
                col = col + 1
            rows = rows + 1
            self.mazelist.append(rowList)
            columns = len(rowList)

        self.rowsInMaze = rows
        self.columnsInMaze = columns
        self.xTranslate = -columns / 2
        self.yTranslate = rows / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columns - 1) / 2 - .5, -(rows - 1) / 2 - .5,(columns - 1) / 2 + .5, (rows - 1) / 2 + .5)

    def draw(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == '+':
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'brown')
        self.t.color('black')
        self.t.fillcolor('green')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move(self,x ,y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropMark(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.move(col,row)
        if val == '0':
            color = 'green'
        elif val == '+':
            color = 'red'
        elif val == '.':
            color = 'black'
        else:
            color = None

        if color:
            self.dropMark(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1)

    def __getitem__(self,idx):
        return self.mazelist[idx]


def searchFrom(maze, row, column):

    maze.updatePosition(row,column)
    if maze[row][column] == '+':
        return False
    if maze[row][column] == '.':
        return False
    if maze.isExit(row,column):
        maze.updatePosition(row,column,'0')
        return True
    maze.updatePosition(row, column, '.')

    found = searchFrom(maze, row - 1, column) or searchFrom(maze, row + 1, column) or searchFrom(maze, row, column - 1) or searchFrom(maze, row, column + 1)
    if found:
        maze.updatePosition(row, column, '0')
    else:
        maze.updatePosition(row, column, '+')
    return found


myMaze = Maze('map.txt')
myMaze.draw()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)