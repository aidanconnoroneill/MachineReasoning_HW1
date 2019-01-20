import random


class Puzzle:

    squares = []
    size = -1

    def __init__(self, size):
        self.size = size
        so_far = []
        cur = -1
        for i in range(0, size):
            my_row = []
            for j in range(0, size):
                while True:
                    cur = random.randint(0, size * size - 1)
                    if not cur in so_far:
                        break
                so_far.append(cur)
                if cur != 0:
                    my_row.append(cur)
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
        print ""

    def h1(self):
        count = 0
        cur = -1
        for row in range(0, self.size):
            for col in range(0, self.size):
                cur = self.squares[row][col]
                if (cur != -1 and cur != row * self.size + col + 1):
                    count += 1
        return count

    def h2(self):
        count = 0
        proper_row = 0
        proper_col = 0
        cur = -1
        for row in range(0, self.size):
            for col in range(0, self.size):
                cur = self.squares[row][col]
                if cur != -1:
                    proper_row = (cur - 1) / self.size
                    proper_col = (cur - 1) % self.size
                    count += abs(proper_row - row)
                    count += abs(proper_col - col)
        return count


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
puzzle.pretty_print()
#right
print puzzle.right()
puzzle.pretty_print()
#up
print puzzle.up()
puzzle.pretty_print()
#down
print puzzle.down()
puzzle.pretty_print()
print puzzle.h1()
print puzzle.h2()
