board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

WIN_COMBOS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (6, 4, 2)
]

PLAYER = "O"
CPU = "X"


def printBoard():
    print("\nCurrent board position: ")
    print()
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def isDraw():
    for ele in board:
        if ele not in ["X", "O"]:
            return False
    return True


def playerPlay():
    while True:
        position = int(input("\nEnter your position: ")) - 1

        if board[position] not in [CPU, PLAYER]:
            setMove(PLAYER, position)
            break
        else:
            print(f"Position {position + 1} already filled.")


def minimax(board, depth, isMax):
    if getWinner(CPU):
        return 1
    if getWinner(PLAYER):
        return -1
    if isDraw():
        return 0

    if isMax:
        optimalScore = -float('inf')

        for i in range(len(board)):
            if board[i] not in [CPU, PLAYER]:
                temp = board[i]
                board[i] = CPU
                score = minimax(board, depth + 1, False)
                board[i] = temp

                optimalScore = max(optimalScore, score)

        return optimalScore

    else:
        optimalScore = float('inf')

        for i in range(len(board)):
            if board[i] not in [CPU, PLAYER]:
                temp = board[i]
                board[i] = PLAYER
                score = minimax(board, depth + 1, True)
                board[i] = temp

                optimalScore = min(optimalScore, score)

        return optimalScore


def cpuPlay():
    optimalScore = -float('inf')
    optimalMove = None

    for pos in range(len(board)):
        if board[pos] not in [CPU, PLAYER]:
            temp = board[pos]
            board[pos] = CPU
            score = minimax(board, 0, False)
            board[pos] = temp

            if score > optimalScore:
                optimalScore = score
                optimalMove = pos

    setMove(CPU, optimalMove)


def checkWin():
    # playerPos.sort()
    # cpuPos.sort()

    for combo in WIN_COMBOS:
        if all(board[pos] == board[combo[0]] and board[pos] in ["X", "O"] for pos in combo):
            return True
    return False


def getWinner(symbol):
    for combo in WIN_COMBOS:
        if all(board[pos] == board[combo[0]] and board[pos] is symbol for pos in combo):
            return True
    return False


def setMove(char, position):
    board[position] = char
    printBoard()

    if isDraw():
        print("\nGame drawn!")
        exit()

    if checkWin() and char == CPU:
        print("\nCPU Wins!")
        exit()
    elif checkWin() and char == PLAYER:
        print("\nYou win!")
        exit()


print("\nWelcome to Unbeatable TicTacToe!")
print("Computer plays first. All the best!")
printBoard()

while not checkWin():
    cpuPlay()
    playerPlay()
