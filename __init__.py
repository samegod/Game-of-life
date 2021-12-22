from math import isclose
import csv


def set_probabilities() -> tuple[float]:
    p_3 = float(input('Enter probability of plant cells in range (0, 1): '))
    
    while 0 >= p_3 or p_3 >= 1.0:
        p_3 = float(input('Enter probability of plant cells again:'))
        
    p_0 = float(input('Enter probability of empty cells: '))
    p_1 = float(input('Enter probability of herbivores cells: '))
    p_2 = float(input('Enter probability of predators cells: '))
    P = (p_0, p_1, p_2, p_3)

    if not isclose(sum(P[:-1]), 1.0):
        raise ValueError('Probabilities are not distribution')
    return P
                
def save_board_to_file(board : list[list[int]]):
    with open("board.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(board)

def read_board_from_file() -> list[list[int]]:
    with open("board.csv", 'r') as file:
        reader = csv.reader(file)
        board = list(reader)
    board = [[int(j) for j in i ] for i in board]
    return board