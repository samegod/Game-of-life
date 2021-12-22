import init
import __init__ as initsub
import random as rand
import numpy as np


def set_iteration_number() -> int:
    iterations = int(input('Enter number of iterations (start from 2): '))
    while iterations <= 1:
        iterations = int(input('Enter number of iterations again: '))
    return iterations

def game_iterator(board : list[list[int]], iterations : int) -> list[list[int]]:
    options = [0, 3]
    distribution = [0.5, 0.5]
    for l in range(iterations):
        print('ITERATION ' + str(l + 1))
        board = [[rand.choices(options, distribution)[0] if j == 0 or j == 3 else j for j in i] for i in board]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    top = i - 2 if i - 2 >= 0 else 0
                    bottom = i + 2 if i + 2 <= len(board) else len(board)
                    left = j - 2 if j - 2 >= 0 else 0
                    right = j + 2 if j + 2 <= len(board[i]) else len(board[i])
                    temp_board = np.array(board)
                    subboard = temp_board[top : bottom + 1, left : right + 1]
                    plant_count = 0
                    herbivore_count = 0
                    
                    for k in range(len(subboard)):
                        for m in range(len(subboard[k])):
                            if board[k][m] == 3:
                                plant_count += 1
                            elif board[k][m] == 1:
                                herbivore_count += 1
                                
                    if plant_count >= 4 and herbivore_count >= 1:
                        herbivore_count = 1
                        empty_count = 0
                        x = rand.randrange(0, len(subboard))
                        y = rand.randrange(0, len(subboard[0]))
                        
                        while herbivore_count != 0:
                            if board[x][y] == 0:
                                board[x][y] = 1
                                herbivore_count -= 1
                            x = rand.randrange(0, len(subboard))
                            y = rand.randrange(0, len(subboard[0]))
                            
                        while empty_count != 4:
                            if board[x][y] == 3:
                                board[x][y] = 1
                                empty_count += 1
                            x = rand.randrange(0, len(subboard))
                            y = rand.randrange(0, len(subboard[0]))
                            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 2:
                    top = i - 1 if i - 1 >= 0 else 0
                    bottom = i + 1 if i + 1 <= len(board) else len(board)
                    left = j - 1 if j - 1 >= 0 else 0
                    right = j + 1 if j + 1 <= len(board[i]) else len(board[i])
                    temp_board2 = np.array(board)
                    subboard2 = temp_board2[top : bottom + 1, left : right + 1]
                    herbivore_count = 0
                    predator_count = 0
                    
                    for k in range(len(subboard2)):
                        for m in range(len(subboard2[0])):
                            if board[k][m] == 1:
                                herbivore_count += 1
                            elif board[k][m] == 2:
                                predator_count += 1
                                
                    if predator_count == 1 and herbivore_count >= 1:
                        herbivore_count = 1
                        x = rand.randrange(0, len(subboard2))
                        y = rand.randrange(0, len(subboard2[0]))
                        
                        while herbivore_count != 0:
                            if board[x][y] == 1:
                                board[x][y] == 0
                                herbivore_count -= 1
                            x = rand.randrange(0, len(subboard2))
                            y = rand.randrange(0, len(subboard2[0]))
                            
                    elif predator_count >= 2 and herbivore_count > 1:
                        herbivore_count = 2
                        x = rand.randrange(0, len(subboard2))
                        y = rand.randrange(0, len(subboard2[0]))
                        
                        while herbivore_count != 0:
                            if board[x][y] == 1 and herbivore_count == 2:
                                board[x][y] == 0
                                herbivore_count -= 1
                            elif board[x][y] == 1 and herbivore_count == 1:
                                board[x][y] = 2
                                herbivore_count -= 1
                            x = rand.randrange(0, len(subboard2))
                            y = rand.randrange(0, len(subboard2[0]))
                            
                    move_top = i - 3 if i - 3 >= 0 else 0
                    move_bottom = i + 3 if i + 3 <= len(board) else len(board)
                    move_left = j - 3 if j - 3 >= 0 else 0
                    move_right = j + 3 if j + 3 <= len(board[i]) else len(board[i])
                    temp_board3 = np.array(board)
                    subboard3 = temp_board3[move_top : move_bottom + 1, move_left : move_right + 1]
                    herbivores = []
                    
                    for k in range(len(subboard3)):
                        for m in range(len(subboard3[k])):
                            if board[k][m] == 1:
                                herbivores.append((k, m))
                                
                    if herbivores:
                        path = {herbivore : abs(i - herbivore[0]) + abs(1 - herbivore[1]) for herbivore in herbivores}
                        path = {k: v for k, v in sorted(path.items(), key = lambda item: item[1])}
                        
                        for p in path:
                            x = i - p[0]
                            y = j - p[1]
                            if x == 0 and y > 0: #left
                                if board[i][j - 1] == 0:
                                    board[i][j - 1] == 2
                                    board[i][j] == 0
                                    break
                                    
                            elif x == 0 and y < 0: #right
                                if board[i][j + 1] == 0:
                                    board[i][j + 1] == 2
                                    board[i][j] == 0
                                    break
                                    
                            elif x < 0 and y == 0: #bottom 
                                if board[i + 1][j] == 0:
                                    board[i + 1][j] == 2
                                    board[i][j] == 0
                                    break
                                    
                            elif x > 0 and y == 0: #top
                                if board[i - 1][j] == 0:
                                    board[i - 1][j] == 2
                                    board[i][j] = 0
                                    break
        init.print_board(board)
    return board

if __name__ == "__main__":
    size = init.init_main()
    h = size[0]
    w = size[1]
    init_board = init.init_board(h, w)
    
    P = initsub.set_probabilities()

    start_board = init.init_cells(init_board, P)
    init.print_board(start_board)
    initsub.save_board_to_file(start_board)
    iterations = set_iteration_number()
    
    game = game_iterator(start_board, iterations)
    initsub.save_board_to_file(game)