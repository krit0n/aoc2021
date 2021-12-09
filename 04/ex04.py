class Board:
    def __init__(self, array):
        self.rows = [set(l) for l in array]
        self.columns = [set(c) for c in zip(*array)]

    def call_number(self, number):
        for r in self.rows:
            r.discard(number)
        for c in self.columns:
            c.discard(number)

    def is_bingo(self):
        return not all(self.rows) or not all(self.columns)

    def remaining_numbers(self):
        return {number for row in self.rows for number in row}    


with open('input.txt') as file:
    lines = file.read().split('\n\n')
    numbers = [int(n) for n in lines[0].split(',')]
    boards = [[list(map(int, row.split())) for row in board.splitlines()] for board in lines[1:]]

### exercise 1

def find_winner(boards):
    boards = [Board(b) for b in boards]
    for n in numbers:
        for b in boards:
            b.call_number(n)
            if b.is_bingo():
                return b, n
    return None

board, called_number = find_winner(boards)
print("solution 1:", sum(board.remaining_numbers()) * called_number)


### exercise 2

def find_loser(boards):
    boards = {Board(b) for b in boards}
    last = None
    called_number = None
    for n in numbers:
        next_boards = boards.copy()
        for b in boards:
            b.call_number(n)
            if b.is_bingo():
                last = b
                called_number = n
                next_boards.remove(b)
        boards = next_boards

    return b, called_number

board, called_number = find_loser(boards)
print("solution 2:", sum(board.remaining_numbers()) * called_number)
