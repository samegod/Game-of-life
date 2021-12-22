import random as rand


def init_board(height : int, width : int) -> list[list[int]]:
    return [[0 for j in range(width)] for i in range(height)]

def print_board(board : list[list[int]]):
    for i in range(len(board)):
        print(board[i])

def init_cells(board: list[list[int]], prob: tuple[float]) -> list[list[int]]:
    options1 = [0, 3]
    distribution1 = [1 - prob[3], prob[3]]
    board = [[rand.choices(options1, distribution1)[0] for j in i] for i in board]
    options2 = [0, 1, 2]
    distribution2 = [prob[0], prob[1], prob[2]]
    board = [[rand.choices(options2, distribution2)[0] if j == 0 else j for j in i] for i in board]
    return board

def init_main() -> list[list[int]]:
    width = int(input('Enter the width of the game board: '))
    height = int(input('Enter the height of the game board: '))
    return [width, height]

if __name__ == '__main__':
    init_main()