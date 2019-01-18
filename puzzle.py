class Puzzle:

    squares = []
    size = -1

    def __init__(self, size):
        self.size = size

        for i in range(0, size):
            my_row = []
            for j in range(0, size):
                if ((i != size - 1 or j != size - 1)):
                    my_row.append(i * size + j + 1)
                else:
                    my_row.append(-1)
            self.squares.append(my_row)

    def get_state(self):
        return squares

    def down(self):
        for row in range(0, self.size - 1):
            for col in range(0, self.size):
                if (self.squares[row][col] == -1):
                    self.squares[row][col] = self.squares[row + 1][col]
                    self.squares[row + 1][col] = -1
                    return True
        return False

    def up(self):
        for row in range(1, self.size):
            for col in range(0, self.size):
                if (self.squares[row][col] == -1):
                    self.squares[row][col] = self.squares[row - 1][col]
                    self.squares[row - 1][col] = -1
                    return True
        return False

    def left(self):
        for row in range(0, self.size):
            for col in range(1, self.size):
                if (self.squares[row][col] == -1):
                    self.squares[row][col] = self.squares[row][col - 1]
                    self.squares[row][col - 1] = -1
                    return True
        return False

    def right(self):
        for row in range(0, self.size):
            for col in range(0, self.size - 1):
                if (self.squares[row][col] == -1):
                    self.squares[row][col] = self.squares[row][col + 1]
                    self.squares[row][col + 1] = -1
                    return True
        return False

    def pretty_print(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                print(self.squares[row][col]),
            print " "


##testing
puzzle = Puzzle(3)
puzzle.pretty_print()

#error testing
print "Should be four falses"
print puzzle.down()
print puzzle.right()

#put it to the top left
puzzle.up()
puzzle.up()
puzzle.left()
puzzle.left()

print puzzle.up()
print puzzle.left()

#left
print puzzle.left()
print " "
puzzle.pretty_print()
#right
print puzzle.right()
print " "
puzzle.pretty_print()
#up
print puzzle.up()
print " "
puzzle.pretty_print()
#down
print puzzle.down()
print " "
puzzle.pretty_print()
