import numpy as np
n = int(input("Шахмат тақтасының өлшемін енгізіңіз (мысалы, 8): "))
chess_board = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            chess_board[i][j] = 0  # Ақ ұяшық
        else:
            chess_board[i][j] = 1  # Қара ұяшық

print("Шахмат тақтасы:")
print(chess_board)