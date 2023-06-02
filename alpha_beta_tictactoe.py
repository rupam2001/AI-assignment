import random
import math

board_state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def printBoard(board_state):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for x in board_state:
        for y in x:
            ch = chars[y]
            print(f'| {ch} |', end='')
        print('\n' + '---------------')
    print('===============')

def clearBoard(board_state):
    for x, row in enumerate(board_state):
        for y, col in enumerate(row):
            board_state[x][y] = 0

def win(board_state, player):
    conditions = [[board_state[0][0], board_state[0][1], board_state[0][2]],
                     [board_state[1][0], board_state[1][1], board_state[1][2]],
                     [board_state[2][0], board_state[2][1], board_state[2][2]],
                     [board_state[0][0], board_state[1][0], board_state[2][0]],
                     [board_state[0][1], board_state[1][1], board_state[2][1]],
                     [board_state[0][2], board_state[1][2], board_state[2][2]],
                     [board_state[0][0], board_state[1][1], board_state[2][2]],
                     [board_state[0][2], board_state[1][1], board_state[2][0]]]

    if [player, player, player] in conditions:
        return True

    return False

def gameWon(board_state):
    return win(board_state, 1) or win(board_state, -1)

def printResult(board_state):
    if win(board_state, 1):
        print('X has won! ' + '\n')

    elif win(board_state, -1):
        print('O\'s have won! ' + '\n')

    else:
        print('Draw' + '\n')

def blanks(board_state):
    blank = []
    for x, row in enumerate(board_state):
        for y, col in enumerate(row):
            if board_state[x][y] == 0:
                blank.append([x, y])

    return blank

def isboardFull(board_state):
    if len(blanks(board_state)) == 0:
        return True
    return False

def setMove(board_state, x, y, player):
    board_state[x][y] = player

def playerMove(board_state):
    e = True
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while e:
        try:
            move = int(input('Enter a number from 1 to 9 corresponding to the cell:  '))
            if move < 1 or move > 9:
                print('Invalid Move! Try again!')
            elif not (moves[move] in blanks(board_state)):
                print('Invalid Move! Try again!')
            else:
                setMove(board_state, moves[move][0], moves[move][1], 1)
                printBoard(board_state)
                e = False
        except(KeyError, ValueError):
            print('Enter a number!')

def getScore(board_state):
    if win(board_state, 1):
        return 10
    elif win(board_state, -1):
        return -10
    return 0

def alphabetaMinMaxPruning(board_state, depth, alpha, beta, player):
    row = -1
    col = -1
    if depth == 0 or gameWon(board_state):
        return [row, col, getScore(board_state)]

    else:
        for cell in blanks(board_state):
            setMove(board_state, cell[0], cell[1], player)
            score = alphabetaMinMaxPruning(board_state, depth - 1, alpha, beta, -player)
            if player == 1:
                # X is always the max player
                if score[2] > alpha:
                    alpha = score[2]
                    row = cell[0]
                    col = cell[1]

            else:
                if score[2] < beta:
                    beta = score[2]
                    row = cell[0]
                    col = cell[1]

            setMove(board_state, cell[0], cell[1], 0)

            if alpha >= beta:
                break

        if player == 1:
            return [row, col, alpha]

        else:
            return [row, col, beta]

def o_comp(board_state):
    if len(blanks(board_state)) == 9:
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])
        setMove(board_state, x, y, -1)
        printBoard(board_state)

    else:
        result = alphabetaMinMaxPruning(board_state, len(blanks(board_state)), -math.inf, math.inf, -1)
        setMove(board_state, result[0], result[1], -1)
        printBoard(board_state)

def x_comp(board_state):
    if len(blanks(board_state)) == 9:
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])
        setMove(board_state, x, y, 1)
        printBoard(board_state)

    else:
        result = alphabetaMinMaxPruning(board_state, len(blanks(board_state)), -math.inf, math.inf, 1)
        setMove(board_state, result[0], result[1], 1)
        printBoard(board_state)

def makeMove(board_state, player, mode):
    if mode == 1:
        if player == 1:
            playerMove(board_state)

        else:
            o_comp(board_state)
    else:
        if player == 1:
            o_comp(board_state)
        else:
            x_comp(board_state)

def main():
    while True:
        try:
            order = int(input('Enter to play 1st or 2nd: '))
            if not (order == 1 or order == 2):
                print('Please pick 1 or 2')
            else:
                break
        except(KeyError, ValueError):
            print('Enter a number')

    clearBoard(board_state)
    if order == 2:
        currentPlayer = -1
    else:
        currentPlayer = 1

    while not (isboardFull(board_state) or gameWon(board_state)):
        makeMove(board_state, currentPlayer, 1)
        currentPlayer *= -1

    printResult(board_state)

# Driver Code
print("=================================================")
print("TIC-TAC-TOE using MINIMAX with ALPHA-BETA Pruning")
print("=================================================")
main()